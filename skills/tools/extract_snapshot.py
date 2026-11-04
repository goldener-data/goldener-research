#!/usr/bin/env python3
"""Extract root/topic research documents from a recorded commit in a scratch Git store.

Usage: extract_snapshot.py OBJECT_STORE COMMIT NEW_OUTPUT_DIRECTORY
Never checks out or executes repository content. Uses only the Python standard library.
"""
import argparse
from pathlib import Path, PurePosixPath
import re
import subprocess


DOCUMENTS = {'README.md', 'RESEARCHERS.md', 'BIBLIOGRAPHY.md'}


def extract_snapshot(store, commit, destination):
    if not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', commit):
        raise ValueError('commit must be a full hexadecimal SHA')
    git = ['git', f'--git-dir={store}']
    listing = subprocess.run(git + ['ls-tree', '-rz', '--full-tree', commit],
                             capture_output=True, check=True).stdout
    documents = []
    for entry in listing.split(b'\0'):
        if not entry:
            continue
        metadata, raw_path = entry.split(b'\t', 1)
        mode, kind, object_id = metadata.decode('ascii').split()
        name = raw_path.decode('utf-8')
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or '\\' in name:
            raise ValueError(f'unsafe snapshot path: {name!r}')
        if len(path.parts) not in (1, 2) or path.name not in DOCUMENTS:
            continue
        if path.parts[0].startswith('.') or path.parts[0] == 'skills':
            continue
        if kind != 'blob' or mode not in ('100644', '100755'):
            raise ValueError(f'snapshot document is not a regular file: {name!r}')
        documents.append((path, object_id))
    # Validate the entire selection before creating or writing the output directory.
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=False)
    for path, object_id in documents:
        content = subprocess.run(git + ['cat-file', 'blob', object_id],
                                 capture_output=True, check=True).stdout
        output = destination.joinpath(*path.parts)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(content)
    return len(documents)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('store', type=Path)
    parser.add_argument('commit')
    parser.add_argument('destination', type=Path)
    args = parser.parse_args()
    count = extract_snapshot(args.store, args.commit, args.destination)
    print(f'Extracted {count} research documents into {args.destination}')


if __name__ == '__main__':
    main()
