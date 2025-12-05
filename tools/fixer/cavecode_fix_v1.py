#!/usr/bin/env python3
"""
CaveCode Fixer / Normalizer v1.0

Usage:
    python cavecode_fix_v1.py input.cavecode > output.cavecode

What it does:
    - Normalizes block headers to the official glyph + title set
    - Fixes old or incorrect glyphs (e.g. ✏️ → 🖍️ for tuning knobs)
    - Leaves inner content alone

This is meant as a gentle corrector, not a linter.
"""

import sys
from pathlib import Path
from typing import List, Tuple


# Canonical headers we enforce, keyed by block number
CANON_HEADERS = {
    "1": "🧱 BLOCK 1 — SHELL",
    "2": "🎮 BLOCK 2 — GAME LOOP / BEHAVIOR",
    "3": "🖍️ BLOCK 3 — TUNING KNOBS",
    "4": "🌐 BLOCK 4 — PUBLIC TEXT",
    "5": "📝 BLOCK 5 — HUMAN NOTES",
}

def read_lines(path: Path) -> List[str]:
    if str(path) == "-":
        return sys.stdin.read().splitlines(keepends=True)
    return path.read_text(encoding="utf-8").splitlines(keepends=True)


def is_block_header(line: str) -> Tuple[bool, str]:
    """
    Returns (True, block_number) if this line looks like BLOCK N — something,
    otherwise (False, "").
    """
    stripped = line.strip()
    # Look for "BLOCK X —"
    marker = "BLOCK "
    dash = "—"
    if marker not in stripped or dash not in stripped:
        return False, ""
    try:
        after_block = stripped.split(marker, 1)[1]
        num_part = after_block.split(" ", 1)[0]
        num_part = num_part.strip()
        # basic numeric check
        int(num_part)
        return True, num_part
    except Exception:
        return False, ""


def fix_header_line(line: str) -> str:
    """
    If the line is a BLOCK header (even with wrong glyph / title),
    normalize it to the canonical header for that block number.

    Otherwise, return it unchanged.
    """
    is_header, num = is_block_header(line)
    if not is_header:
        return line

    canonical = CANON_HEADERS.get(num)
    if not canonical:
        # Unknown block number, leave it alone
        return line

    # Preserve trailing newline if present
    newline = ""
    if line.endswith("\n"):
        newline = "\n"

    return canonical + newline


def main():
    if len(sys.argv) < 2:
        print("Usage: cavecode_fix_v1.py <input-file | ->", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    lines = read_lines(path)

    fixed_lines: List[str] = []
    for line in lines:
        fixed = fix_header_line(line)
        fixed_lines.append(fixed)

    sys.stdout.write("".join(fixed_lines))


if __name__ == "__main__":
    main()
