"""Local behavior checks; no network, real mailbox, or credential-file access.

Run: python3 -m unittest discover -s skills/tools -p 'test_*.py'
"""
import contextlib
import email
import email.policy
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MailboxConfigurationTests(unittest.TestCase):
    def setUp(self):
        self.mailbox = load_module('outreach_mailbox', ROOT / 'tools/mailbox.py')

    def config(self, environment, connection=None, signature=None):
        output = io.StringIO()
        # Mock the loader so tests never read the user's real private env file.
        with patch.dict(os.environ, environment, clear=True), \
                patch.object(self.mailbox, 'load_env_file', return_value=None), \
                patch.object(self.mailbox, 'connect', connection or Mock()) as connect, \
                patch.object(self.mailbox, 'signature', return_value=signature), \
                contextlib.redirect_stdout(output):
            code = self.mailbox.config()
        return code, json.loads(output.getvalue()), connect

    def test_unconfigured_does_not_connect(self):
        code, data, connect = self.config({})
        self.assertEqual((code, data['status']), (2, 'unconfigured'))
        connect.assert_not_called()

    def test_partial_reports_names_without_connecting(self):
        code, data, connect = self.config({'OUTREACH_PASSWORD': 'private-value'})
        self.assertEqual((code, data['status']), (2, 'partial'))
        self.assertIn('OUTREACH_EMAIL', data['missing'])
        self.assertNotIn('private-value', json.dumps(data))
        connect.assert_not_called()

    def test_configured_login_and_drafts(self):
        environment = {'OUTREACH_IMAP_HOST': 'mail.example.test',
                       'OUTREACH_EMAIL': 'sender@example.test',
                       'OUTREACH_PASSWORD': 'private-value'}
        conn = Mock()
        with patch.object(self.mailbox, 'drafts_folder', return_value='"Drafts"'):
            code, data, connect = self.config(environment, Mock(return_value=conn))
        self.assertEqual((code, data['status'], data['drafts_folder']), (0, 'ok', 'Drafts'))
        self.assertNotIn('private-value', json.dumps(data))
        conn.logout.assert_called_once()
        connect.assert_called_once()

    def test_provider_failure_does_not_expose_exception(self):
        environment = {'OUTREACH_IMAP_HOST': 'mail.example.test',
                       'OUTREACH_EMAIL': 'sender@example.test',
                       'OUTREACH_PASSWORD': 'private-value'}
        code, data, _ = self.config(environment, Mock(side_effect=RuntimeError('private-value')))
        self.assertEqual((code, data['status']), (1, 'error'))
        self.assertNotIn('private-value', json.dumps(data))

    def test_vault_failure_does_not_expose_stderr(self):
        result = subprocess.CompletedProcess(['vault'], 1, '', 'private-value')
        with patch.dict(os.environ, {'OUTREACH_PASSWORD_COMMAND': 'vault get item'}, clear=True), \
                patch.object(self.mailbox.subprocess, 'run', return_value=result):
            with self.assertRaises(SystemExit) as raised:
                self.mailbox.password()
        self.assertNotIn('private-value', str(raised.exception))


    def test_optional_settings_are_partial(self):
        for name in ('OUTREACH_DRAFTS_FOLDER', 'OUTREACH_IMAP_PORT',
                     'OUTREACH_BW_SESSION', 'OUTREACH_THUNDERBIRD_PROFILE'):
            with self.subTest(setting=name):
                code, data, connect = self.config({name: 'configured'})
                self.assertEqual((code, data['status']), (2, 'partial'))
                connect.assert_not_called()

    def test_missing_explicit_env_file_reports_its_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = str(Path(tmp) / 'missing.env')
            output = io.StringIO()
            with patch.dict(os.environ, {'OUTREACH_ENV_FILE': missing}, clear=True), \
                    patch.object(self.mailbox, 'connect') as connect, \
                    contextlib.redirect_stdout(output):
                code = self.mailbox.config()
            data = json.loads(output.getvalue())
            self.assertEqual((code, data['status']), (1, 'error'))
            self.assertIn(missing, data['error'])
            connect.assert_not_called()

    def test_config_resolves_password_once_and_reports_signature(self):
        environment = {'OUTREACH_IMAP_HOST': 'mail.example.test',
                       'OUTREACH_EMAIL': 'sender@example.test',
                       'OUTREACH_PASSWORD_COMMAND': 'vault get item'}
        conn = Mock()
        with patch.object(self.mailbox, 'password', return_value=('private-value', 'command')) as password, \
                patch.object(self.mailbox.imaplib, 'IMAP4_SSL', return_value=conn), \
                patch.object(self.mailbox, 'drafts_folder', return_value='"Drafts"'), \
                patch.object(self.mailbox, 'embed_images') as images:
            code, data, _ = self.config(environment, Mock(wraps=self.mailbox.connect),
                                        {'source': 'fixture-signature'})
        self.assertEqual((code, data['password_source']), (0, 'command'))
        self.assertEqual(data['signature'], 'fixture-signature')
        password.assert_called_once_with()
        conn.login.assert_called_once_with('sender@example.test', 'private-value')
        images.assert_not_called()
        self.assertNotIn('private-value', json.dumps(data))

    def test_draft_keeps_signature_date_and_message_id(self):
        for supplied_headers in (False, True):
            with self.subTest(supplied_headers=supplied_headers), tempfile.TemporaryDirectory() as tmp:
                message = email.message.EmailMessage(policy=email.policy.SMTP)
                message['To'] = 'researcher@example.test'
                if supplied_headers:
                    message['Date'] = 'Tue, 03 Nov 2026 10:00:00 +0100'
                    message['Message-ID'] = '<existing@example.test>'
                message.set_content('Research invitation')
                source = Path(tmp) / 'draft.eml'
                source.write_bytes(message.as_bytes())
                conn = Mock()
                conn.append.return_value = ('OK', [])
                signature = {'source': 'fixture-signature', 'text': 'Research signature',
                             'html': None, 'separator': True}
                with patch.dict(os.environ, {'OUTREACH_EMAIL': 'sender@example.test'}, clear=True), \
                        patch.object(self.mailbox, 'connect', return_value=conn), \
                        patch.object(self.mailbox, 'drafts_folder', return_value='"Drafts"'), \
                        patch.object(self.mailbox, 'signature', return_value=signature), \
                        contextlib.redirect_stdout(io.StringIO()):
                    self.mailbox.draft(source)
                stored = email.message_from_bytes(conn.append.call_args.args[3],
                                                  policy=email.policy.default)
                self.assertTrue(stored['Date'])
                self.assertTrue(stored['Message-ID'])
                self.assertIn('Research signature', stored.get_content())
                if supplied_headers:
                    self.assertEqual(stored['Date'], message['Date'])
                    self.assertEqual(stored['Message-ID'], message['Message-ID'])


class PackagingTests(unittest.TestCase):
    def test_plugin_installs_include_shared_helpers(self):
        claude = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
        installs = [(plugin['name'], ROOT / plugin['source'], plugin['skills'])
                    for plugin in claude['plugins']]
        codex = json.loads((ROOT / '.codex-plugin/plugin.json').read_text())
        installs.append(('codex-' + codex['name'], ROOT, [codex['skills']]))
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / 'research'
            (fixture / 'skills').mkdir(parents=True)
            (fixture / 'README.md').write_text('# Research\n', encoding='utf-8')
            (fixture / 'BIBLIOGRAPHY.md').write_text(
                '<div><a href="https://example.test/paper"><strong>Example Paper</strong></a></div>',
                encoding='utf-8')
            for name, source, skills in installs:
                with self.subTest(plugin=name):
                    installed = Path(tmp) / name
                    # Copy only the plugin's install surface.
                    shutil.copytree(source, installed, ignore=shutil.ignore_patterns('__pycache__'))
                    for skill in skills:
                        self.assertTrue(list((installed / skill).rglob('SKILL.md')))
                    for helper in ('papers.py', 'researchers.py', 'extract_snapshot.py',
                                   'mailbox.py', 'unicode_bold.py'):
                        self.assertTrue((installed / 'tools' / helper).is_file())
                    result = subprocess.run(
                        ['python3', '-I', str(installed / 'tools/papers.py'), 'list'],
                        cwd=fixture, capture_output=True, text=True, check=True)
                    self.assertEqual(json.loads(result.stdout)[0]['title'], 'Example Paper')

    def test_bundled_workflows_and_shared_tools(self):
        bundler = load_module('skill_bundler', ROOT / 'tools/bundle_resources.py')
        for source, destination in bundler.resources(ROOT):
            with self.subTest(resource=destination):
                self.assertEqual(source.read_bytes(), destination.read_bytes())
        with tempfile.TemporaryDirectory() as tmp:
            for skill in ROOT.glob('sync-*-issues'):
                installed = Path(tmp) / skill.name
                shutil.copytree(skill, installed)
                self.assertTrue((installed / 'references/sync-workflow.md').is_file())
            summary = Path(tmp) / 'short-paper-review'
            shutil.copytree(ROOT / 'short-paper-review', summary)
            dependency = summary / 'references/paper-review'
            self.assertTrue((dependency / 'SKILL.md').is_file())
            self.assertTrue((dependency / 'template.html').is_file())
            fixture = Path(tmp) / 'research'
            (fixture / 'skills').mkdir(parents=True)
            (fixture / 'README.md').write_text('# Research\n', encoding='utf-8')
            (fixture / 'BIBLIOGRAPHY.md').write_text(
                '<div><a href="https://example.test/paper"><strong>Example Paper</strong></a></div>',
                encoding='utf-8')
            tools = Path(tmp) / 'tools'
            shutil.copytree(ROOT / 'tools', tools)
            helper = str(tools / 'papers.py')
            result = subprocess.run(['python3', helper, 'list', '--root', str(fixture)],
                                    capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(result.stdout)[0]['title'], 'Example Paper')
            # An installed copy finds the checkout it is run from, topic folders included.
            topic = fixture / 'labeling'
            topic.mkdir()
            (topic / 'README.md').write_text('# Labeling\n', encoding='utf-8')
            result = subprocess.run(['python3', helper, 'list'], cwd=topic,
                                    capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(result.stdout)[0]['title'], 'Example Paper')
            # Outside any checkout it fails instead of listing no paper.
            outside = Path(tmp) / 'elsewhere'
            outside.mkdir()
            result = subprocess.run(['python3', helper, 'list'], cwd=outside,
                                    capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('--root', result.stderr)

    def test_shared_helpers_find_source_repository(self):
        for name in ('papers.py', 'researchers.py'):
            helper = ROOT / 'tools' / name
            with self.subTest(helper=helper), tempfile.TemporaryDirectory() as tmp:
                result = subprocess.run(['python3', '-I', str(helper), 'list'], cwd=tmp,
                                        capture_output=True, text=True, check=True)
                self.assertTrue(json.loads(result.stdout))


class PaperLookupTests(unittest.TestCase):
    def setUp(self):
        self.papers = load_module('paper_lookup', ROOT / 'tools/papers.py')

    def test_unicode_titles_preserve_identity(self):
        for title in ('数据选择', 'Обучение модели', 'नमस्ते शोध', 'Café learning'):
            with self.subTest(title=title):
                papers = [{'title': title}, {'title': 'Unrelated paper'}]
                results = self.papers.find(papers, title, 2)
                self.assertEqual(results[0]['title'], title)
                self.assertEqual(results[0]['score'], 1.0)
                self.assertLess(results[1]['score'], 1.0)
        self.assertEqual(self.papers.normalize_title('Cafe\u0301 LEARNING'),
                         self.papers.normalize_title('Café learning'))

    def test_explicit_topic_root_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            topic = Path(tmp) / 'labeling'
            topic.mkdir()
            (topic / 'BIBLIOGRAPHY.md').write_text('# Bibliography\n', encoding='utf-8')
            (topic / 'README.md').write_text('# Labeling\n', encoding='utf-8')
            helper = ROOT / 'tools/papers.py'
            result = subprocess.run(['python3', str(helper), 'list', '--root', str(topic)],
                                    capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('repository root', result.stderr)


class SnapshotTests(unittest.TestCase):
    def setUp(self):
        self.extractor = load_module('snapshot_extractor',
                                    ROOT / 'tools/extract_snapshot.py')

    def snapshot_fixture(self, directory, symlink=False):
        repo = directory / 'repo'
        repo.mkdir()
        subprocess.run(['git', 'init', '-q', str(repo)], check=True)
        for name in ('README.md', 'RESEARCHERS.md', 'labeling/README.md',
                     'labeling/BIBLIOGRAPHY.md', 'labeling/IDEAS.md',
                     'skills/README.md', '.hidden/README.md',
                     'labeling/nested/README.md', 'execute.py'):
            file = repo / name
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text(name, encoding='utf-8')
        if symlink:
            (repo / 'labeling/RESEARCHERS.md').symlink_to('/etc/passwd')
        subprocess.run(['git', '-C', str(repo), 'add', '.'], check=True)
        subprocess.run(['git', '-C', str(repo), '-c', 'user.name=Fixture',
                        '-c', 'user.email=fixture@example.test', 'commit', '-qm', 'Fixture'], check=True)
        sha = subprocess.run(['git', '-C', str(repo), 'rev-parse', 'HEAD'],
                             capture_output=True, text=True, check=True).stdout.strip()
        return repo / '.git', sha

    def test_only_regular_root_and_topic_documents_are_extracted(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            store, sha = self.snapshot_fixture(directory)
            destination = directory / 'snapshot'
            count = self.extractor.extract_snapshot(store, sha, destination)
            files = {str(file.relative_to(destination)) for file in destination.rglob('*') if file.is_file()}
            self.assertEqual(count, 4)
            self.assertEqual(files, {'README.md', 'RESEARCHERS.md',
                                     'labeling/README.md', 'labeling/BIBLIOGRAPHY.md'})
            self.assertEqual((destination / 'labeling/README.md').read_text(), 'labeling/README.md')
            with self.assertRaises(FileExistsError):
                self.extractor.extract_snapshot(store, sha, destination)

    def test_symlink_document_is_rejected_before_extraction(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            store, sha = self.snapshot_fixture(directory, symlink=True)
            destination = directory / 'snapshot'
            with self.assertRaisesRegex(ValueError, 'not a regular file'):
                self.extractor.extract_snapshot(store, sha, destination)
            self.assertFalse(destination.exists())

    def test_ref_names_and_traversal_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / 'snapshot'
            with self.assertRaisesRegex(ValueError, 'full hexadecimal SHA'):
                self.extractor.extract_snapshot(Path(tmp), '--help', destination)
            listing = b'100644 blob ' + b'a' * 40 + b'\t../README.md\0'
            with patch.object(self.extractor.subprocess, 'run', return_value=Mock(stdout=listing)):
                with self.assertRaisesRegex(ValueError, 'unsafe snapshot path'):
                    self.extractor.extract_snapshot(Path(tmp), 'a' * 40, destination)
            self.assertFalse(destination.exists())


if __name__ == '__main__':
    unittest.main()
