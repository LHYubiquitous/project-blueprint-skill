#!/usr/bin/env python3
"""Offline scan for likely secrets and private identifiers before publication."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import os
from pathlib import Path
import re
import sys
from typing import Iterable, Sequence


MAX_FILE_BYTES = 2 * 1024 * 1024
SKIPPED_DIRECTORIES = {
    ".git",
    ".hg",
    ".svn",
    ".mypy_cache",
    ".pytest_cache",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
}
SENSITIVE_FILENAMES = {
    ".env",
    ".npmrc",
    ".pypirc",
    "credentials.json",
    "id_dsa",
    "id_ed25519",
    "id_ecdsa",
    "id_rsa",
}


@dataclass(frozen=True, order=True)
class Finding:
    path: str
    line: int
    kind: str
    excerpt: str


PATTERNS = (
    (
        "private-key",
        re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
    ),
    (
        "credential",
        re.compile(
            r"(?:AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,}|"
            r"(?i:(?:api[_-]?key|client[_-]?secret|password|passwd|access[_-]?token|bearer)"
            r"\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{16,}))"
        ),
    ),
    (
        "signed-url",
        re.compile(
            r"(?i)[?&](?:X-Amz-Signature|X-Goog-Signature|Signature|sig|token)="
            r"[A-Za-z0-9_%./+=-]{16,}"
        ),
    ),
    (
        "email",
        re.compile(r"(?<![\w.+-])[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?![\w.-])"),
    ),
    (
        "absolute-home-path",
        re.compile(
            r"(?:/(?:Users|home)/[^/\s'\"`]+|[A-Za-z]:[\\/]Users[\\/][^\\/\s'\"`]+)"
        ),
    ),
)


def _iter_files(root: Path) -> Iterable[Path]:
    for current, directories, filenames in os.walk(root, followlinks=False):
        directories[:] = sorted(
            directory
            for directory in directories
            if directory not in SKIPPED_DIRECTORIES
            and not (Path(current) / directory).is_symlink()
        )
        for filename in sorted(filenames):
            path = Path(current) / filename
            if not path.is_symlink() and path.is_file():
                yield path


def _read_text(path: Path) -> str | None:
    try:
        if path.stat().st_size > MAX_FILE_BYTES:
            return None
        data = path.read_bytes()
    except OSError:
        return None
    if b"\x00" in data:
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return None


def scan(root: Path) -> list[Finding]:
    """Return deterministic findings without following links or leaving ``root``."""
    root = root.expanduser().resolve()
    findings: list[Finding] = []
    for path in _iter_files(root):
        relative = path.relative_to(root).as_posix()
        if path.name in SENSITIVE_FILENAMES or path.name.startswith(".env."):
            findings.append(Finding(relative, 0, "sensitive-filename", "[sensitive filename]"))
        text = _read_text(path)
        if text is None:
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            for kind, pattern in PATTERNS:
                for match in pattern.finditer(line):
                    findings.append(
                        Finding(
                            relative,
                            line_number,
                            kind,
                            "[REDACTED]",
                        )
                    )
    return sorted(findings)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Offline scan for likely secrets and private identifiers before publication."
    )
    parser.add_argument("directory", type=Path, help="Directory to scan")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    root = args.directory.expanduser()
    if not root.is_dir():
        print(f"ERROR: directory not found: {root}", file=sys.stderr)
        return 2
    findings = scan(root)
    if findings:
        for finding in findings:
            location = f"{finding.path}:{finding.line}" if finding.line else finding.path
            print(f"REVIEW {location} [{finding.kind}] {finding.excerpt}")
        print(f"Found {len(findings)} potential publication risk(s).", file=sys.stderr)
        return 1
    print(f"OK: no likely secrets or private identifiers in {root.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
