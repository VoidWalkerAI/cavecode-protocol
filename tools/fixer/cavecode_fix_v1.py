#!/usr/bin/env python3
"""Gently normalize legacy CaveCode block glyphs without fixing block order."""

import argparse
import re
from pathlib import Path


HEADER_RE = re.compile(
    r"^(?P<indent>\s*)(?P<glyph>\S+)\s+BLOCK\s+(?P<address>[0-9]+[A-Za-z]?)"
    r"\s+(?P<dash>—|-)\s+(?P<title>.+?)(?P<newline>\n?)$"
)


def semantic_glyph(old_glyph: str, title: str) -> str:
    upper = title.upper()
    if old_glyph == "🧱":
        return "🪨"
    if old_glyph in {"🎚️", "✏️", "📝"}:
        return "🖍️"
    if old_glyph == "🔧" and any(
        word in upper for word in ("BEHAVIOR", "FLOW", "LOGIC", "LOOP", "PROCESS")
    ):
        return "🎮"
    return old_glyph


def fix_text(text: str) -> str:
    output: list[str] = []
    for line in text.splitlines(keepends=True):
        match = HEADER_RE.match(line)
        if not match:
            output.append(line)
            continue
        glyph = semantic_glyph(match.group("glyph"), match.group("title"))
        output.append(
            f"{match.group('indent')}{glyph} BLOCK {match.group('address')} "
            f"— {match.group('title')}{match.group('newline')}"
        )
    return "".join(output)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    print(fix_text(args.path.read_text(encoding="utf-8")), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
