#!/usr/bin/env python3
"""Reference validator for the stabilized CaveCode v1.0 contract."""

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


CANONICAL_GLYPHS = ("🪨", "🖍️", "🔧", "🎮", "🌐")
HEADER_RE = re.compile(
    r"^(?P<glyph>🪨|🖍️|🔧|🎮|🌐)\s+BLOCK\s+"
    r"(?P<address>[0-9]+[A-Za-z]?)\s+(?:—|-)\s+(?P<title>\S.*)$"
)
HEADER_CANDIDATE_RE = re.compile(
    r"^(?:🪨|🖍️|🔧|🎮|🌐|🎚️|✏️|📝|🧱)\s+BLOCK\s+\S+"
)


@dataclass
class ValidationResult:
    profile: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    block_count: int = 0

    @property
    def ok(self) -> bool:
        return not self.errors


def detect_profile(text: str) -> str:
    upper = text.upper()
    if "MASTER PROJECT MAP" in upper or "CAVECODE READ-FIRST PROJECT FILE" in upper:
        return "project"
    return "artifact"


def validate_text(text: str, profile: str = "auto") -> ValidationResult:
    active_profile = detect_profile(text) if profile == "auto" else profile
    result = ValidationResult(profile=active_profile)
    headers: list[tuple[int, str, str, str]] = []

    in_fence = False
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.rstrip()
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADER_RE.match(line)
        if match:
            headers.append(
                (
                    line_number,
                    match.group("glyph"),
                    match.group("address").upper(),
                    match.group("title"),
                )
            )
        elif HEADER_CANDIDATE_RE.match(line):
            result.errors.append(
                f"Line {line_number}: noncanonical or malformed block header: {line}"
            )

    result.block_count = len(headers)
    if not headers:
        result.errors.append("No canonical CaveCode block headers found.")
        return result

    seen: dict[str, int] = {}
    for line_number, _glyph, address, _title in headers:
        if address in seen:
            result.errors.append(
                f"Line {line_number}: duplicate block address {address} "
                f"(first used on line {seen[address]})."
            )
        else:
            seen[address] = line_number

    if active_profile == "project":
        required_concepts: dict[str, Iterable[str]] = {
            "status": ("STATUS:",),
            "purpose of this file": ("PURPOSE OF THIS FILE:",),
            "authority": ("AUTHORITY",),
            "current state": ("PROJECT STATE:", "CURRENT STATE", "CURRENT PROJECT"),
            "next action": ("NEXT ACTION:",),
            "resume/handoff": ("RESUME HERE", "HANDOFF"),
        }
        upper = text.upper()
        for label, alternatives in required_concepts.items():
            if not any(token in upper for token in alternatives):
                result.errors.append(
                    f"Project Map is missing required concept: {label}."
                )

    if "🎚️" in text or "✏️ BLOCK" in text or "📝 BLOCK" in text or "🧱 BLOCK" in text:
        result.warnings.append(
            "Legacy v1.1-era block glyph detected; use canonical v1.0 roles."
        )

    return result


def validate_file(path: Path, profile: str = "auto") -> ValidationResult:
    return validate_text(path.read_text(encoding="utf-8"), profile=profile)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--profile", choices=("auto", "artifact", "project"), default="auto"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        result = validate_file(args.path, profile=args.profile)
    except (OSError, UnicodeError) as exc:
        print(f"FAIL: cannot read {args.path}: {exc}")
        return 1

    status = "PASS" if result.ok else "FAIL"
    if result.ok and result.warnings:
        status = "PASS WITH WARNINGS"
    print(
        f"{status}: {args.path} "
        f"({result.profile} profile, {result.block_count} blocks)"
    )
    for message in result.errors:
        print(f"ERROR: {message}")
    for message in result.warnings:
        print(f"WARN: {message}")
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
