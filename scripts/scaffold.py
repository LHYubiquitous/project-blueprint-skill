#!/usr/bin/env python3
"""Generate a no-overwrite project blueprint from bundled templates (stdlib-only)."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
TEMPLATES = HERE.parent / 'assets' / 'templates'
CORE = ['README.md', 'AGENTS.md', 'TASKS.md']
STANDARD = CORE + [
    'PROGRESS.md', 'HANDOFF.md',
    'docs/REQUIREMENTS.md', 'docs/RESEARCH.md', 'docs/ARCHITECTURE.md',
    'docs/DECISIONS.md', 'docs/TESTING_AND_OPERATIONS.md',
    'docs/COST_AND_LICENSE.md', 'docs/SOURCES.md',
]
FULL = STANDARD + ['docs/EXTENSIONS.md', 'docs/RISKS.md']
MODES = {'light': CORE, 'standard': STANDARD, 'full': FULL}


def slugify(name: str) -> str:
    slug = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
    return slug[:64] if slug else 'new-project'


def scaffold(name: str, output: Path, mode: str, dry_run: bool) -> tuple[int, int]:
    count, skipped = 0, 0
    output = output.expanduser().resolve()
    if output.exists() and not output.is_dir():
        raise ValueError(f'Output path exists but is not a directory: {output}')
    values = {'{{PROJECT_NAME}}': name, '{{PROJECT_SLUG}}': slugify(name), '{{DATE}}': date.today().isoformat()}
    for rel in MODES[mode]:
        src = TEMPLATES / rel
        if not src.is_file():
            raise FileNotFoundError(f'Missing bundled template: {src}')
        dest = output / rel
        if dest.exists():
            print(f'SKIP   {dest} (already exists)')
            skipped += 1
            continue
        raw = src.read_text(encoding='utf-8')
        for needle, value in values.items():
            raw = raw.replace(needle, value)
        print(f'{"WOULD CREATE" if dry_run else "CREATE"} {dest}')
        if not dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            with dest.open('x', encoding='utf-8', newline='\n') as f:
                f.write(raw)
        count += 1
    return count, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description='Create a research-first, Codex-ready project blueprint (no overwrite).')
    parser.add_argument('--name', required=True, help='Project display name')
    parser.add_argument('--output', required=True, type=Path, help='Destination directory')
    parser.add_argument('--mode', choices=sorted(MODES), default='standard')
    parser.add_argument('--dry-run', action='store_true', help='Only show planned files')
    args = parser.parse_args()
    try:
        created, skipped = scaffold(args.name, args.output, args.mode, args.dry_run)
        print(f'\nResult: {created} {"planned" if args.dry_run else "created"}, {skipped} existing files preserved.')
        if not args.dry_run:
            print('Next: replace template placeholders with verified research and accepted requirements.')
        return 0
    except (ValueError, FileNotFoundError, OSError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
