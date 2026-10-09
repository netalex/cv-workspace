import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import inventory_sources as inv

class InventoryTests(unittest.TestCase):
    def test_identical_files_share_id_and_originals_stay_unchanged(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);raw=root/'sources/raw';raw.mkdir(parents=True)
            content=('Esperienza professionale verificabile. '*3).encode()
            (raw/'a.txt').write_bytes(content);(raw/'b.txt').write_bytes(content)
            first=inv.build_inventory(root);second=inv.build_inventory(root)
            self.assertEqual(first,second)
            self.assertEqual(first['files'],2);self.assertEqual(first['unique_contents'],1)
            self.assertEqual(len(first['records'][0]['paths']),2)
            self.assertEqual((raw/'a.txt').read_bytes(),content)

    def test_cloud_link_is_not_treated_as_cv_text(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);raw=root/'sources/raw';raw.mkdir(parents=True)
            (raw/'cv.gdoc').write_text('{"url":"https://example.com/doc","doc_id":"x"}')
            record=inv.build_inventory(root)['records'][0]
            self.assertEqual(record['status'],'requires_export')
            self.assertNotIn('extracted_path',record)

    def test_docx_table_paragraphs_are_extracted(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'cv.docx'
            xml='<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>Profilo</w:t></w:r></w:p><w:tbl><w:tr><w:tc><w:p><w:r><w:t>Esperienza</w:t></w:r></w:p></w:tc></w:tr></w:tbl></w:body></w:document>'
            with zipfile.ZipFile(p,'w') as z:z.writestr('word/document.xml',xml)
            self.assertEqual(inv.office_xml(p),'Profilo\nEsperienza')

    def test_one_failed_extraction_does_not_lose_inventory(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);raw=root/'sources/raw';raw.mkdir(parents=True)
            (raw/'bad.docx').write_bytes(b'not a zip')
            record=inv.build_inventory(root)['records'][0]
            self.assertEqual(record['status'],'extraction_error')

if __name__=='__main__':unittest.main()
