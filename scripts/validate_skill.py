#!/usr/bin/env python3
"""Offline structural validation for this portable Agent Skill."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    skill = ROOT / 'SKILL.md'
    data = skill.read_text(encoding='utf-8')
    if not data.startswith('---\n'):
        print('ERROR: missing YAML frontmatter')
        return 1
    sections = data.split('---\n', 2)
    if len(sections) < 3:
        print('ERROR: unclosed YAML frontmatter')
        return 1
    header = sections[1]
    name = re.search(r'^name:\s*(.+)$', header, re.M)
    desc = re.search(r'^description:\s*(.+)$', header, re.M)
    errors = []
    if not name or name.group(1).strip() != ROOT.name:
        errors.append('skill name must match directory name')
    if not name or not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', name.group(1).strip()):
        errors.append('invalid skill name')
    if not desc or not (1 <= len(desc.group(1).strip()) <= 1024):
        errors.append('description missing/too long')
    for match in re.finditer(r'(references|scripts|assets)/[a-zA-Z0-9_./-]+', data):
        rel = match.group(0).rstrip('.,;:')
        if not (ROOT / rel).exists():
            errors.append(f'missing referenced file: {rel}')
    required = ['README.md', 'AGENTS.md', 'TASKS.md', 'docs/RESEARCH.md', 'docs/SOURCES.md']
    for rel in required:
        if not (ROOT / 'assets' / 'templates' / rel).is_file():
            errors.append(f'missing template: {rel}')
    if errors:
        for issue in sorted(set(errors)):
            print('ERROR:', issue)
        return 1
    print(f'OK: {ROOT.name}; {len(list((ROOT / "assets" / "templates").rglob("*.md")))} templates; references resolved')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
