#!/usr/bin/env python3
"""Local CV workflow. No network, AI API, git mutation or message sending."""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

try:
    import yaml
except ImportError:
    sys.exit('Installare le dipendenze: python -m pip install -r requirements.txt')

ROOT = Path(__file__).resolve().parents[1]
GROUPS = ('experiences', 'projects', 'skills', 'education', 'languages')
INPUTS = ('application.yaml', 'job.md', 'analysis.md', 'cv.md', 'cover-letter.md', 'message.md')
PLACEHOLDER = re.compile(r'\bTODO\b|\bTBD\b|\[DA COMPILARE\]|\{\{', re.I)


def load(path):
    data = yaml.safe_load(path.read_text(encoding='utf-8-sig'))
    if not isinstance(data, dict):
        raise ValueError(f'{path}: atteso oggetto YAML')
    return data


def write_yaml(path, data):
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def inside(path):
    path = path.resolve()
    require(path.is_relative_to(ROOT), 'Percorso esterno al progetto non consentito')
    return path


def app_path(value):
    p = Path(value)
    p = inside(p if p.is_absolute() else ROOT / p)
    require(p.is_dir(), f'Cartella non trovata: {p}')
    return p


def validate_profile(path):
    p = load(path)
    require(p.get('schema_version') == 1, 'Versione profilo non supportata')
    ident = p.get('identity')
    require(isinstance(ident, dict), 'identity deve essere un oggetto')
    for key in ('name', 'email', 'location'):
        require(isinstance(ident.get(key), str), f'identity.{key} deve essere una stringa')
    sources = p.get('sources')
    require(isinstance(sources, list), 'sources deve essere una lista')
    known, ids = {}, set()
    for s in sources:
        require(isinstance(s, dict) and isinstance(s.get('id'), str) and s['id'], 'Fonte senza ID')
        require(s['id'] not in ids, f'ID duplicato: {s["id"]}')
        ids.add(s['id'])
        require(isinstance(s.get('path'), str) and s['path'], 'Fonte senza percorso')
        file = inside(ROOT / s['path'])
        require(file.is_file(), f'Fonte mancante: {file}')
        known[s['id']] = file
    records = {}
    for group in GROUPS:
        require(isinstance(p.get(group), list), f'{group} deve essere una lista')
        for item in p[group]:
            require(isinstance(item, dict), f'{group}: record non valido')
            for key in ('id', 'label'):
                require(isinstance(item.get(key), str) and item[key].strip(), f'{group}: {key} mancante')
            require(item['id'] not in ids, f'ID duplicato: {item["id"]}')
            ids.add(item['id'])
            require(item.get('status') in ('confirmed', 'to_verify'), f'{item["id"]}: status non valido')
            refs = item.get('source_ids')
            require(isinstance(refs, list) and all(isinstance(x, str) for x in refs), 'source_ids non valido')
            require(all(x in known for x in refs), f'{item["id"]}: fonte inesistente')
            require(item['status'] != 'confirmed' or refs, f'{item["id"]}: confermato senza fonte')
            records[item['id']] = item
    return p, records, known


def validate_app(folder, demo=False):
    a = load(folder / 'application.yaml')
    require(a.get('schema_version') == 1, 'Versione candidatura non supportata')
    for key in ('demo', 'content_approved', 'layout_checked'):
        require(type(a.get(key)) is bool, f'{key} deve essere true o false')
    require(a['demo'] == demo, 'Per gli esempi usare --demo; non usare --demo sui dati reali')
    require(not demo or folder == ROOT / 'examples/demo', 'Modalità demo riservata a examples/demo')
    for key in ('company', 'role'):
        require(isinstance(a.get(key), str) and a[key].strip(), f'{key} mancante')
    require(a.get('language') in ('it', 'en'), 'language deve essere it o en')
    require(a.get('status') in ('draft', 'ready', 'sent', 'interview', 'closed'), 'status non valido')
    profile_path = ROOT / ('examples/demo/profile.yaml' if demo else 'profile/profile.yaml')
    p, records, sources = validate_profile(profile_path)
    require(p['identity']['name'].strip(), 'Nome del profilo non compilato')
    refs = a.get('evidence_ids')
    require(isinstance(refs, list) and refs and all(isinstance(x, str) for x in refs), 'evidence_ids deve contenere almeno un ID')
    for ref in refs:
        require(ref in records, f'Evidenza inesistente: {ref}')
        require(records[ref]['status'] == 'confirmed', f'Evidenza non confermata: {ref}')
    for name in INPUTS[1:]:
        text = (folder / name).read_text(encoding='utf-8-sig')
        require(text.strip() and not PLACEHOLDER.search(text), f'{name}: testo vuoto o segnaposto da risolvere')
    return a, profile_path, sources


def executable(name):
    def console_path(path):
        if sys.platform == 'win32' and name == 'soffice':
            console = Path(path).with_name('soffice.com')
            if console.is_file():
                return str(console)
        return str(path)

    override = os.environ.get(name.upper() + '_PATH')
    if override:
        require(Path(override).is_file(), f'{name.upper()}_PATH non valido')
        return console_path(override)
    names = ('soffice.com', 'soffice', 'libreoffice') if name == 'soffice' and sys.platform == 'win32' else (name,)
    for candidate in names:
        found = shutil.which(candidate)
        if found:
            return console_path(found)
    if name == 'soffice':
        found = shutil.which('libreoffice')
        if found:
            return console_path(found)
        roots = []
        for env in ('PROGRAMFILES', 'PROGRAMFILES(X86)'):
            if os.environ.get(env):
                roots.append(Path(os.environ[env]) / 'LibreOffice')
        if sys.platform == 'win32':
            scoop_roots = [Path(os.environ.get('SCOOP') or Path.home() / 'scoop')]
            if os.environ.get('SCOOP_GLOBAL'):
                scoop_roots.append(Path(os.environ['SCOOP_GLOBAL']))
            elif os.environ.get('PROGRAMDATA'):
                scoop_roots.append(Path(os.environ['PROGRAMDATA']) / 'scoop')
            for root in scoop_roots:
                current = root / 'apps/libreoffice/current'
                roots.extend((current / 'LibreOffice', current))
        for root in roots:
            for filename in ('soffice.com', 'soffice.exe'):
                path = root / 'program' / filename
                if path.is_file():
                    return console_path(path)
    raise ValueError(f'{name} non trovato. Aggiungerlo al PATH o impostare {name.upper()}_PATH.')


def run(cmd):
    result = subprocess.run([str(x) for x in cmd], capture_output=True, text=True, timeout=120)
    require(result.returncode == 0, f'Comando fallito: {cmd[0]}\n{result.stderr}\n{result.stdout}')
    return (result.stdout or result.stderr).strip()


def tool_version(exe):
    output = run([exe, '--version'])
    lines = output.splitlines()
    return lines[0] if lines else 'Versione non disponibile (output vuoto)'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inputs(folder, profile, sources):
    paths = [folder / n for n in INPUTS]
    paths += [profile, ROOT / 'templates/reference.docx', ROOT / 'scripts/cv.py']
    paths += sorted((ROOT / 'rules').glob('*.md')) + list(sources.values())
    return {str(p.relative_to(ROOT)).replace('\\', '/'): digest(p) for p in paths}


def new_app(args):
    require(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.slug), 'Slug: lettere minuscole, numeri e trattini')
    folder = ROOT / 'applications' / args.slug
    folder.mkdir(exist_ok=False)
    write_yaml(folder / 'application.yaml', dict(schema_version=1, company=args.company, role=args.role,
        language=args.language, demo=False, status='draft', job_url='', captured_on='', channel='',
        next_action='', next_action_on='', evidence_ids=[], content_approved=False, layout_checked=False))
    for name in INPUTS[1:]:
        (folder / name).write_text(f'# {name[:-3]}\n\n[DA COMPILARE]\n', encoding='utf-8')
    print(folder)


def build(args):
    folder = app_path(args.folder)
    a, profile, sources = validate_app(folder, args.demo)
    pandoc, soffice = executable('pandoc'), executable('soffice')
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    base = folder / 'build'
    base.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=base, prefix='.tmp-') as temp:
        out = Path(temp)
        for name in ('cv', 'cover-letter'):
            run([pandoc, folder / f'{name}.md', '--from=markdown', '--standalone',
                 '--reference-doc', ROOT / 'templates/reference.docx', '-o', out / f'{name}.docx'])
        with tempfile.TemporaryDirectory(prefix='cv-lo-') as lo:
            run([soffice, '-env:UserInstallation=' + Path(lo).as_uri(), '--headless',
                 '--convert-to', 'pdf', '--outdir', out, out / 'cv.docx', out / 'cover-letter.docx'])
        for name in ('cv.pdf', 'cover-letter.pdf'):
            require((out / name).is_file() and (out / name).stat().st_size > 0, f'Conversione PDF fallita: {name}')
        shutil.copy2(folder / 'message.md', out / 'message.md')
        shutil.copy2(folder / 'application.yaml', out / 'application-at-build.yaml')
        files = {p.name: digest(p) for p in out.iterdir() if p.is_file()}
        manifest = dict(created_utc=stamp, demo=args.demo, inputs=inputs(folder, profile, sources), outputs=files,
                        tools={'pandoc': tool_version(pandoc),
                               'soffice': tool_version(soffice)})
        (out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
        target = base / stamp
        out.rename(target)
    print(f'Generato: {target}\nAprire entrambi i PDF e verificare ogni pagina. Nessun invio eseguito.')
    if not a['content_approved']:
        print('BOZZA: contenuti non ancora approvati.')


def snapshot(args):
    folder = app_path(args.folder)
    a, profile, sources = validate_app(folder)
    require(a['content_approved'] and a['layout_checked'], 'Servono approvazione contenuti e verifica visiva esplicite')
    build_dir = inside(folder / 'build' / args.build)
    require(build_dir.parent == folder / 'build', 'Identificativo build non valido')
    manifest = json.loads((build_dir / 'manifest.json').read_text(encoding='utf-8'))
    require(not manifest['demo'], 'Gli esempi non possono essere archiviati come candidature reali')
    current = inputs(folder, profile, sources)
    # Approval flags may change after rendering; all other application metadata must match.
    appkey = (folder / 'application.yaml').relative_to(ROOT).as_posix()
    original = load(build_dir / 'application-at-build.yaml') if (build_dir / 'application-at-build.yaml').exists() else None
    require(original is not None, 'Build priva dei metadati originali: rigenerare')
    comparable = lambda x: {k:v for k,v in x.items() if k not in ('content_approved','layout_checked')}
    require(comparable(a) == comparable(original), 'Metadati modificati: rigenerare')
    require({k:v for k,v in current.items() if k != appkey} == {k:v for k,v in manifest['inputs'].items() if k != appkey}, 'Sorgenti modificate dopo il build: rigenerare e verificare')
    for name, sha in manifest['outputs'].items():
        require(digest(build_dir / name) == sha, f'Output modificato: {name}')
    target = folder / 'sent' / args.build
    require(not target.exists(), 'Snapshot già presente; non verrà sovrascritto')
    target.parent.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=target.parent) as temp:
        stage = Path(temp) / 'snapshot'
        shutil.copytree(build_dir, stage)
        for rel in current:
            dst = stage / 'sources' / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, dst)
        (stage / 'approval.json').write_text(json.dumps({'content_approved':True,'layout_checked':True,'archived_utc':datetime.now(timezone.utc).isoformat(),'inputs':current}, indent=2), encoding='utf-8')
        stage.rename(target)
    print(f'Archiviato: {target}\nQuesto comando non invia nulla e non modifica lo stato della candidatura.')


def register():
    rows = []
    for path in sorted((ROOT / 'applications').glob('*/application.yaml')):
        a = load(path)
        rows.append({'folder':path.parent.name, **{k:a.get(k, '') for k in ('company','role','status','channel','next_action','next_action_on')}})
    target = ROOT / 'applications/register.csv'
    with target.open('w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=['folder','company','role','status','channel','next_action','next_action_on'], delimiter=';')
        w.writeheader(); w.writerows(rows)
    print(target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('doctor')
    p = sub.add_parser('new'); p.add_argument('slug'); p.add_argument('--company', required=True); p.add_argument('--role', required=True); p.add_argument('--language', choices=['it','en'], default='it')
    for command in ('validate','build'):
        p = sub.add_parser(command); p.add_argument('folder', nargs='?' if command == 'validate' else None); p.add_argument('--demo', action='store_true')
    p = sub.add_parser('snapshot'); p.add_argument('folder'); p.add_argument('--build', required=True)
    sub.add_parser('register')
    args = parser.parse_args()
    try:
        if args.command == 'doctor':
            print(f'Python {sys.version.split()[0]} | PyYAML {yaml.__version__}')
            for name in ('pandoc','soffice'):
                exe = executable(name); print(tool_version(exe))
            require((ROOT/'templates/reference.docx').is_file(), 'Modello Word mancante')
        elif args.command == 'new': new_app(args)
        elif args.command == 'validate':
            if args.folder: validate_app(app_path(args.folder), args.demo)
            else:
                require(not args.demo, '--demo richiede una cartella')
                validate_profile(ROOT/'profile/profile.yaml')
            print('Struttura e riferimenti validi. Accuratezza dei contenuti da verificare separatamente.')
        elif args.command == 'build': build(args)
        elif args.command == 'snapshot': snapshot(args)
        else: register()
    except (ValueError, OSError, KeyError, TypeError, yaml.YAMLError, subprocess.TimeoutExpired) as e:
        print(f'Errore: {e}', file=sys.stderr); return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())

