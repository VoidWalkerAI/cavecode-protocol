#!/usr/bin/env python3
"""
CaveCode Validator v1.1

Usage:
    python validate_cavecode_v1_1.py path/to/file.cavecode

Checks:
    - Required blocks present
    - Valid glyphs on block headers
    - At least one tuning knob (🖍️)
    - At least one public text entry (🌐)
"""

import sys
import re
from pathlib import Path
from typing import List, Dict, Tuple

# Allowed glyphs for block headers
ALLOWED_GLYPHS = {"🧱", "🎮", "🖍️", "🌐", "🪨", "📝"}

# Required blocks (we match by these substrings in the header line)
REQUIRED_BLOCKS = {
    "SHELL": "🧱 BLOCK 1 — SHELL",
    "BEHAVIOR": "🎮 BLOCK 2 —",           # Allow GAME LOOP / PROGRAM BEHAVIOR label variants
    "TUNING": "🖍️ BLOCK 3 — TUNING KNOBS",
    "PUBLIC": "🌐 BLOCK 4 — PUBLIC TEXT",
    "NOTES": "📝 BLOCK 5 — HUMAN NOTES",
}

BLOCK_HEADER_RE = re.compile(
    r"^(?P<glyph>[\u2600-\u27BF\U0001F300-\U0001FAFF])\s+BLOCK\s+(?P<num>\d+)\s+—\s+(?P<title>.+)$"
)


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def find_block_headers(lines: List[str]) -> List[Tuple[int, str]]:
    headers = []
    for i, line in enumerate(lines):
        line = line.strip()
        if "BLOCK" in line and "—" in line:
            headers.append((i, line))
    return headers


def validate_headers(headers: List[Tuple[int, str]]) -> List[str]:
    messages = []
    for lineno, line in headers:
        m = BLOCK_HEADER_RE.match(line)
        if not m:
            messages.append(
                f"ERROR: Line {lineno+1}: Block header not in expected format: {line!r}"
            )
            continue
        glyph = m.group("glyph")
        if glyph not in ALLOWED_GLYPHS:
            messages.append(
                f"ERROR: Line {lineno+1}: Unknown glyph {glyph!r} on block header."
            )
    return messages


def check_required_blocks(headers: List[Tuple[int, str]]) -> List[str]:
    present = {key: False for key in REQUIRED_BLOCKS}
    header_texts = [h[1] for h in headers]

    for key, snippet in REQUIRED_BLOCKS.items():
        for ht in header_texts:
            if snippet in ht:
                present[key] = True
                break

    messages = []
    for key, ok in present.items():
        if not ok:
            messages.append(
                f"ERROR: Missing required block: {REQUIRED_BLOCKS[key]!r}"
            )
    return messages


def extract_block_sections(lines: List[str], headers: List[Tuple[int, str]]) -> Dict[str, List[str]]:
    """
    Returns mapping of header line text -> list of lines inside that block.
    """
    sections: Dict[str, List[str]] = {}
    if not headers:
        return sections

    # Add sentinel at end
    extended = headers + [(len(lines), "END-OF-FILE")]

    for idx in range(len(headers)):
        start_line, header_text = extended[idx]
        next_start, _ = extended[idx + 1]
        block_lines = lines[start_line + 1 : next_start]
        sections[header_text] = block_lines

    return sections


def has_tuning_knobs(block_lines: List[str]) -> bool:
    for line in block_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        # rough heuristic: "KEY: value"
        if ":" in stripped:
            return True
    return False


def has_public_text(block_lines: List[str]) -> bool:
    # Same heuristic as knobs: any key/value indicates text fields
    return has_tuning_knobs(block_lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_cavecode_v1_1.py path/to/file.cavecode", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: File not found: {path}", file=sys.stderr)
        sys.exit(1)

    text = read_file(path)
    lines = text.splitlines()

    headers = find_block_headers(lines)
    messages: List[str] = []

    # 1) Validate header formats and glyphs
    messages.extend(validate_headers(headers))

    # 2) Check required blocks
    messages.extend(check_required_blocks(headers))

    # 3) Deeper content checks
    sections = extract_block_sections(lines, headers)

    # tuning knobs & public text checks
    tuning_ok = False
    public_ok = False
    for header, block_lines in sections.items():
        if "TUNING KNOBS" in header:
            tuning_ok = has_tuning_knobs(block_lines)
        if "PUBLIC TEXT" in header:
            public_ok = has_public_text(block_lines)

    if not tuning_ok:
        messages.append("WARN: No obvious tuning knobs found in 🖍️ BLOCK 3 — TUNING KNOBS.")
    if not public_ok:
        messages.append("WARN: No obvious public text entries found in 🌐 BLOCK 4 — PUBLIC TEXT.")

    # Summary
    errors = [m for m in messages if m.startswith("ERROR")]
    warns = [m for m in messages if m.startswith("WARN")]

    if not errors and not warns:
        status = "PASS"
    elif errors:
        status = "FAIL"
    else:
        status = "PASS WITH WARNINGS"

    print(f"Validation result for {path.name}: {status}")
    if messages:
        print("\nDetails:")
        for m in messages:
            print(f"- {m}")


if __name__ == "__main__":
    main()
