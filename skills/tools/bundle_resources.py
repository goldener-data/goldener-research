#!/usr/bin/env python3
"""Bundle workflow references and templates; generate catalog descriptions from SKILL.md.

Run from any directory; --check verifies generated files without writing them.
SKILL.md frontmatter is the source of truth for each catalog description.
"""
import argparse
import json
from pathlib import Path
import re
import shutil


def resources(root):
    for skill in sorted(root.glob('sync-*-issues')):
        if (skill / 'SKILL.md').is_file():
            yield root / '_shared/sync-workflow.md', skill / 'references/sync-workflow.md'
    source = root / 'paper-review'
    destination = root / 'short-paper-review/references/paper-review'
    for relative in ('SKILL.md', 'template.html'):
        yield source / relative, destination / relative


def description(skill):
    """Read this repository's single-line plain-scalar description convention."""
    content = (skill / 'SKILL.md').read_text(encoding='utf-8')
    frontmatter = content.split('---', 2)[1]
    match = re.search(r'^description: (.+)$', frontmatter, re.M)
    if not match or match[1].strip() in ('>', '|', '>-', '|-'):
        raise ValueError(f'{skill}: expected a single-line description')
    return match[1].strip()


def catalog(root):
    path = root / '.claude-plugin/marketplace.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    for plugin in data['plugins']:
        plugin['description'] = description(root / plugin['source'] / plugin['skills'][0])
    return path, json.dumps(data, indent=2, ensure_ascii=False) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    stale = []
    for source, target in resources(root):
        if args.check:
            if not target.is_file() or source.read_bytes() != target.read_bytes():
                stale.append(str(target.relative_to(root)))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
    path, expected = catalog(root)
    if args.check:
        if path.read_text(encoding='utf-8') != expected:
            stale.append(str(path.relative_to(root)))
    else:
        path.write_text(expected, encoding='utf-8')
    if stale:
        parser.exit(1, 'Stale or missing generated resources:\n' + '\n'.join(stale) + '\n')
    print('Generated resources are current.' if args.check else 'Generated resources updated.')


if __name__ == '__main__':
    main()
