"""Inventory raw sources and extract searchable text without changing originals."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
import yaml
from cv import ROOT, executable

TEXT = {'.md', '.markdown', '.txt', '.json', '.yml', '.yaml', '.bak', ''}
PANDOC = {'.html':'html', '.xhtml':'html', '.rtf':'rtf', '.epub':'epub'}
DOCUMENT = {'.docx','.odt','.doc','.pdf', *PANDOC}
LINK = {'.gdoc','.glink','.lnk'}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def decode(data):
    if data.startswith((b'\xff\xfe',b'\xfe\xff')):
        return data.decode('utf-16'), 'utf-16'
    try:
        return data.decode('utf-8-sig'), 'utf-8'
    except UnicodeDecodeError:
        return data.decode('cp1252', errors='replace'), 'cp1252-fallback'

def command(args):
    r=subprocess.run([str(x) for x in args],capture_output=True,timeout=90)
    if r.returncode:
        raise ValueError(r.stderr.decode(errors='replace')[:300])
    return r.stdout.decode('utf-8',errors='replace')

def office_xml(path):
    # Includes table paragraphs and DOCX header/footer text; not a layout replica.
    with zipfile.ZipFile(path) as z:
        if path.suffix.lower()=='.docx':
            names=['word/document.xml']+sorted(n for n in z.namelist() if re.match(r'word/(header|footer)\d+\.xml$',n))
            ns='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
            blocks=[]
            for name in names:
                root=ET.fromstring(z.read(name))
                for p in root.iter(ns+'p'):
                    text=''.join((e.text or '') if e.tag==ns+'t' else '\t' if e.tag==ns+'tab' else '\n' if e.tag==ns+'br' else '' for e in p.iter())
                    if text.strip(): blocks.append(text)
            return '\n'.join(blocks)
        root=ET.fromstring(z.read('content.xml'))
        ns='{urn:oasis:names:tc:opendocument:xmlns:text:1.0}'
        return '\n'.join(''.join(e.itertext()) for e in root.iter() if e.tag in (ns+'p',ns+'h'))

def extract(path):
    suffix=path.suffix.lower()
    if suffix in TEXT:
        data=path.read_bytes()
        if b'\x00' in data[:4096] and not data.startswith((b'\xff\xfe',b'\xfe\xff')):
            return '', 'binary-not-text'
        return decode(data)
    if suffix in ('.docx','.odt'): return office_xml(path), 'office-xml'
    if suffix=='.pdf': return command(['pdftotext','-layout',path,'-']), 'pdftotext-layout'
    if suffix in PANDOC:
        return command([executable('pandoc'),'-f',PANDOC[suffix],'-t','plain','--wrap=none',path]), 'pandoc'
    if suffix=='.doc':
        with tempfile.TemporaryDirectory(prefix='cv-extract-') as temp:
            base=Path(temp);profile=base/'profile';profile.mkdir()
            # Disable macros in the isolated LibreOffice profile.
            (profile/'user').mkdir()
            (profile/'user/registrymodifications.xcu').write_text('<?xml version="1.0"?><oor:items xmlns:oor="http://openoffice.org/2001/registry"><item oor:path="/org.openoffice.Office.Common/Security/Scripting"><prop oor:name="MacroSecurityLevel" oor:op="fuse"><value>3</value></prop></item></oor:items>')
            command([executable('soffice'),'-env:UserInstallation='+profile.as_uri(),'--headless','--convert-to','txt:Text','--outdir',base,path])
            out=base/(path.stem+'.txt')
            if not out.exists(): raise ValueError('LibreOffice non ha prodotto testo')
            return decode(out.read_bytes())[0], 'libreoffice-text'
    return '', 'not-supported'

def build_inventory(root=ROOT):
    raw=root/'sources/raw';out=root/'sources/extracted';out.mkdir(parents=True,exist_ok=True)
    groups=defaultdict(list)
    for f in sorted(raw.rglob('*')):
        if f.is_file() and not f.is_symlink(): groups[sha(f.read_bytes())].append(f)
    records=[]
    for digest, paths in sorted(groups.items()):
        # Prefer an extractable suffix if identical bytes have multiple names.
        paths.sort(key=lambda p:(p.suffix.lower() not in DOCUMENT|TEXT,p.as_posix()))
        p=paths[0];rel=[f.relative_to(root).as_posix() for f in paths]
        rec={'id':'src-'+digest[:16], 'sha256':digest, 'paths':rel, 'size_bytes':p.stat().st_size,
             'category':'support_asset','status':'not_applicable','date':None,'date_basis':'not_assigned'}
        suffix=p.suffix.lower()
        if '__MACOSX' in p.parts or p.name.startswith('._'):
            rec['category']='filesystem_metadata'
        elif suffix in LINK:
            rec.update(category='external_link',status='requires_export')
            if suffix!='.lnk':
                try:
                    obj=json.loads(p.read_text());rec['url']=obj.get('url');rec['document_id']=obj.get('doc_id')
                except (ValueError,UnicodeError): pass
        elif suffix in DOCUMENT|TEXT:
            rec['category']='document_candidate'
            try:
                text,method=extract(p)
                rec['method']=method
                if len(text.strip())<40:
                    rec['status']='needs_manual_review'
                else:
                    rec.update(status='extracted',characters=len(text),text_sha256=sha(text.encode()))
                    rec['flags']=[]
                    if re.search(r'lorem ipsum|laurea in x{3,}',text,re.I):rec['flags'].append('placeholder_content')
                    if 'template' in p.name.lower():rec['flags'].append('template_in_filename')
                    if '\ufffd' in text:rec['flags'].append('replacement_characters')
                    dest=out/(rec['id']+'.txt');dest.write_text(text,encoding='utf-8')
                    rec['extracted_path']=dest.relative_to(root).as_posix()
            except (OSError,ValueError,ET.ParseError,zipfile.BadZipFile,subprocess.TimeoutExpired) as e:
                rec.update(status='extraction_error',error=str(e)[:300])
        records.append(rec)
    payload={'schema_version':1,'id_basis':'sha256 bytes; identical files share ID; edited bytes receive new ID',
             'files':sum(len(r['paths']) for r in records),'unique_contents':len(records),'records':records}
    (root/'sources/inventory.yaml').write_text(yaml.safe_dump(payload,allow_unicode=True,sort_keys=False,width=110),encoding='utf-8')
    counts=Counter(r['status'] for r in records)
    print(json.dumps({'files':payload['files'],'unique':len(records),'status':dict(counts)},ensure_ascii=False))
    return payload

if __name__=='__main__':
    build_inventory()
