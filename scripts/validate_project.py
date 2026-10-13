#!/usr/bin/env python3
"""Validate structural completeness of a project plan (does not judge factual accuracy)."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

BASIC = ['README.md', 'AGENTS.md', 'TASKS.md']
STANDARD = BASIC + ['docs/REQUIREMENTS.md', 'docs/RESEARCH.md', 'docs/ARCHITECTURE.md', 'docs/SOURCES.md']
UNRESOLVED = ('[填充]', '[待填充]', '[由用户需求', '[真实', '[实际', '[具体', '[链接', '[url]', 'TODO:', 'unverified')


def main() -> int:
    p = argparse.ArgumentParser(description='Check project blueprint files; --strict fails on unresolved placeholders.')
    p.add_argument('directory', type=Path)
    p.add_argument('--mode', choices=['light', 'standard'], default='standard')
    p.add_argument('--strict', action='store_true')
    args = p.parse_args()
    root = args.directory.expanduser().resolve()
    if not root.is_dir():
        print(f'ERROR: directory not found: {root}', file=sys.stderr)
        return 2
    files = BASIC if args.mode == 'light' else STANDARD
    missing = [f for f in files if not (root/f).is_file()]
    if missing:
        print('MISSING:', ', '.join(missing))
    flagged = []
    for rel in files:
        file = root / rel
        if not file.is_file():
            continue
        data = file.read_text(encoding='utf-8').lower()
        terms = [term for term in UNRESOLVED if term.lower() in data]
        if terms:
            flagged.append((rel, terms))
    for rel, terms in flagged:
        print(f'REVIEW {rel}: {", ".join(terms)}')
    print(f'Checked {len(files)} expected files, {len(missing)} missing, {len(flagged)} with draft markers.')
    if missing or (args.strict and flagged):
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
