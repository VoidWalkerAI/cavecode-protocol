#!/usr/bin/env python3
"""
CaveCode Minimal Validator v1.0
Checks for:
- Required block headers
- Empty blocks
- Basic structure issues

For strict validation, use validate_cavecode_v1_1.py
"""

import sys
import re
from pathlib import Path

REQUIRED_BLOCKS = [
    "BLOCK 1 — IDENTITY",
    "BLOCK 2 — TUNING KNOBS",
    "BLOCK 3 — PUBLIC TEXT",
    "BLOCK 4 — LOCKED LOGIC",
]

BLOCK_PATTERN = re.compile(r"^=+ +BLOCK +(\d+) +(—|-) +(.*)$")

def load_file(path):
    try:
        return Path(path).read_text(encoding="utf-8").splitlines()
    except Exception as e:
        print(f"ERROR: Cannot read file: {e}")
        sys.exit(1)

def find_blocks(lines):
    blocks = []
    for i, line in enumerate(lines):
        match = BLOCK_PATTERN.match(line.strip())
        if match:
            number = match.group(1)
            title = match.group(3).strip()
            blocks.append((int(number), title, i))
    return blocks

def validate(path):
    lines = load_file(path)
    blocks = find_blocks(lines)

    if not blocks:
        print("❌ No CaveCode blocks found.")
        return False

    # Check required block titles exist
    found_titles = [b[1] for b in blocks]
    missing = [req for req in REQUIRED_BLOCKS if req.split(" — ")[1] not in found_titles]
    if missing:
        print("❌ Missing required blocks:")
        for m in missing:
            print("   -", m)
        return False

    # Check block order
    numbers = [b[0] for b in blocks]
    if numbers != sorted(numbers):
        print("❌ Blocks out of order (must be 1, 2, 3, 4 in sequence).")
        return False

    # Check empty blocks
    for idx, (num, title, start_line) in enumerate(blocks):
        end_line = blocks[idx + 1][2] if idx + 1 < len(blocks) else len(lines)
        contents = lines[start_line + 1:end_line]

        if all(len(line.strip()) == 0 for line in contents):
            print(f"⚠️ Warning: Block {num} (‘{title}’) is empty.")

    print("✅ CaveCode file passes minimal validation.")
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_cavecode.py path/to/file.cavecode")
        sys.exit(1)

    path = sys.argv[1]
    validate(path)

if __name__ == "__main__":
    main()
