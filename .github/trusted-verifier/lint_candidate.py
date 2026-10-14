#!/usr/bin/env python3
"""Lint changed candidate files as data without importing candidate code."""

from __future__ import annotations

import argparse
import ast
import json
import subprocess
import sys
from pathlib import Path


TEXT_SUFFIXES = {".json", ".md", ".py", ".sql", ".yml", ".yaml"}


def git(root: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["/usr/bin/git", *args], cwd=root, capture_output=True, check=False
    )
    if result.returncode:
        raise ValueError(f"GIT:{' '.join(args)}:{result.stderr.decode(errors='replace').strip()}")
    return result.stdout


def changed_paths(root: Path, base: str, head: str) -> list[str]:
    raw = git(root, "diff", "--no-ext-diff", "--no-renames", "--name-only", "-z", base, head, "--")
    return [item.decode("utf-8") for item in raw.split(b"\0") if item]


def lint(root: Path, base: str, head: str) -> list[str]:
    errors: list[str] = []
    check = subprocess.run(
        ["/usr/bin/git", "diff", "--check", base, head, "--"],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    if check.returncode:
        errors.append("DIFF_CHECK:" + check.stdout.strip())
    for relative in changed_paths(root, base, head):
        path = root / relative
        if not path.exists() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            errors.append(f"UNSAFE_PATH:{relative}")
            continue
        try:
            data = path.read_bytes()
            text = data.decode("utf-8")
        except (OSError, UnicodeDecodeError) as error:
            errors.append(f"TEXT_READ:{relative}:{error.__class__.__name__}")
            continue
        if b"\r" in data:
            errors.append(f"CRLF:{relative}")
        if data and not data.endswith(b"\n"):
            errors.append(f"FINAL_NEWLINE:{relative}")
        try:
            if path.suffix == ".json":
                json.loads(text)
            elif path.suffix == ".py":
                ast.parse(text, filename=relative)
        except (json.JSONDecodeError, SyntaxError) as error:
            errors.append(f"SYNTAX:{relative}:{error.lineno}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--base-sha", required=True)
    parser.add_argument("--head-sha", required=True)
    args = parser.parse_args()
    try:
        errors = lint(args.candidate.resolve(strict=True), args.base_sha, args.head_sha)
    except (OSError, ValueError) as error:
        errors = [str(error)]
    print(json.dumps({"errors": errors, "result": "FAIL" if errors else "PASS"}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
