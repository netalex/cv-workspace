import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest
from types import SimpleNamespace
import json

spec = importlib.util.spec_from_file_location('cv', Path(__file__).resolve().parents[1] / 'scripts/cv.py')
cv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cv)

class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.old = cv.ROOT
        self.temp = tempfile.TemporaryDirectory()
        cv.ROOT = Path(self.temp.name)
        for name in ('profile','examples/demo','templates','rules','scripts'):
            shutil.copytree(self.old/name, cv.ROOT/name, ignore=shutil.ignore_patterns('build','__pycache__'))
        self.app=cv.ROOT/'applications/test'
        shutil.copytree(cv.ROOT/'examples/demo',self.app)
        profile=cv.load(cv.ROOT/'examples/demo/profile.yaml')
        cv.write_yaml(cv.ROOT/'profile/profile.yaml',profile)
        self.metadata=cv.load(self.app/'application.yaml')
        self.metadata['demo']=False
        cv.write_yaml(self.app/'application.yaml',self.metadata)

    def tearDown(self):
        cv.ROOT=self.old
        self.temp.cleanup()

    def fake_build(self):
        a,p,s=cv.validate_app(self.app)
        out=self.app/'build/test-build';out.mkdir(parents=True)
        shutil.copy2(self.app/'application.yaml',out/'application-at-build.yaml')
        (out/'cv.pdf').write_bytes(b'fake-pdf-test-only')
        manifest={'demo':False,'inputs':cv.inputs(self.app,p,s),'outputs':{x.name:cv.digest(x) for x in out.iterdir()}}
        (out/'manifest.json').write_text(json.dumps(manifest))
        self.metadata.update(content_approved=True,layout_checked=True)
        cv.write_yaml(self.app/'application.yaml',self.metadata)
        return SimpleNamespace(folder=str(self.app),build='test-build')

    def test_demo_requires_explicit_switch(self):
        with self.assertRaises(ValueError):cv.validate_app(cv.ROOT/'examples/demo')
        cv.validate_app(cv.ROOT/'examples/demo',True)
        with self.assertRaises(ValueError):cv.validate_app(self.app,True)

    def test_unknown_evidence_rejected(self):
        self.metadata['evidence_ids']=['missing'];cv.write_yaml(self.app/'application.yaml',self.metadata)
        with self.assertRaisesRegex(ValueError,'inesistente'):cv.validate_app(self.app)

    def test_unconfirmed_evidence_rejected(self):
        path=cv.ROOT/'profile/profile.yaml';p=cv.load(path)
        p['experiences'][0]['status']='to_verify';cv.write_yaml(path,p)
        with self.assertRaisesRegex(ValueError,'non confermata'):cv.validate_app(self.app)

    def test_placeholder_rejected(self):
        (self.app/'message.md').write_text('[DA COMPILARE]')
        with self.assertRaisesRegex(ValueError,'segnaposto'):cv.validate_app(self.app)

    def test_snapshot_requires_approvals(self):
        with self.assertRaisesRegex(ValueError,'approvazione'):cv.snapshot(SimpleNamespace(folder=str(self.app),build='none'))

    def test_snapshot_keeps_sources_and_refuses_overwrite(self):
        args=self.fake_build();cv.snapshot(args)
        self.assertTrue((self.app/'sent/test-build/sources/profile/profile.yaml').is_file())
        with self.assertRaisesRegex(ValueError,'già presente'):cv.snapshot(args)

    def test_changed_source_rejected(self):
        args=self.fake_build();(self.app/'cv.md').write_text('Testo cambiato')
        with self.assertRaisesRegex(ValueError,'Sorgenti modificate'):cv.snapshot(args)

    def test_changed_output_rejected(self):
        args=self.fake_build();(self.app/'build/test-build/cv.pdf').write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError,'Output modificato'):cv.snapshot(args)

    def test_path_escape_rejected(self):
        with self.assertRaises(ValueError):cv.app_path('../')



class LibreOfficeTests(unittest.TestCase):
    def test_empty_version_is_reported(self):
        from unittest.mock import patch
        with patch.object(cv, 'run', return_value=''):
            self.assertEqual(cv.tool_version('soffice'), 'Versione non disponibile (output vuoto)')

    def test_version_on_stderr_is_supported(self):
        from unittest.mock import patch
        import subprocess
        result = subprocess.CompletedProcess([], 0, '', 'LibreOffice test\n')
        with patch.object(cv.subprocess, 'run', return_value=result):
            self.assertEqual(cv.tool_version('soffice'), 'LibreOffice test')

    def test_failed_version_is_still_an_error(self):
        from unittest.mock import patch
        import subprocess
        result = subprocess.CompletedProcess([], 1, '', 'failed')
        with patch.object(cv.subprocess, 'run', return_value=result):
            with self.assertRaises(ValueError): cv.tool_version('soffice')

    def test_windows_override_prefers_adjacent_console(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as tmp:
            exe=Path(tmp)/'soffice.exe'; exe.touch()
            console=Path(tmp)/'soffice.com'; console.touch()
            with patch.object(cv.sys,'platform','win32'), patch.dict(cv.os.environ,{'SOFFICE_PATH':str(exe)},clear=True):
                self.assertEqual(cv.executable('soffice'),str(console))

    def test_windows_scoop_nested_layout(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as tmp:
            console=Path(tmp)/'apps/libreoffice/current/LibreOffice/program/soffice.com'
            console.parent.mkdir(parents=True); console.touch()
            with patch.object(cv.sys,'platform','win32'), patch.dict(cv.os.environ,{'SCOOP':tmp},clear=True), patch.object(cv.shutil,'which',return_value=None):
                self.assertEqual(cv.executable('soffice'),str(console))

    def test_invalid_override_does_not_fall_back(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as tmp:
            with patch.dict(cv.os.environ,{'SOFFICE_PATH':str(Path(tmp)/'missing')},clear=True):
                with self.assertRaisesRegex(ValueError,'non valido'): cv.executable('soffice')

    def test_linux_path_is_unchanged(self):
        from unittest.mock import patch
        with patch.object(cv.sys,'platform','linux'), patch.dict(cv.os.environ,{},clear=True), patch.object(cv.shutil,'which',return_value='/usr/bin/soffice'):
            self.assertEqual(cv.executable('soffice'),'/usr/bin/soffice')

if __name__=='__main__':unittest.main()
