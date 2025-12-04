#!/usr/bin/env python3
import json
import sys
import re
from pathlib import Path
from typing import Dict, Any, Tuple

TEXT_KEYS = ("text", "message", "title", "label", "caption", "prompt")


def read_input(path: Path) -> str:
    if path == Path("-"):
        return sys.stdin.read()
    return path.read_text(encoding="utf-8")


def try_parse_json(text: str) -> Tuple[bool, Dict[str, Any]]:
    try:
        data = json.loads(text)
        if isinstance(data, dict):
            return True, data
    except Exception:
        pass
    return False, {}


def strip_js_wrapper(text: str) -> str:
    """
    Try to extract the {...} part from a JS-style `const x = {...};`
    without being fancy. Good enough for simple configs.
    """
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return text
    inner = text[start : end + 1]
    # Very light cleanup: convert single quotes to double quotes
    # if it looks mostly JSON-ish already.
    if "'" in inner and '"' not in inner:
        inner = inner.replace("'", '"')
    return inner


def parse_key_values(text: str) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        # Try to coerce numbers and booleans
        if re.fullmatch(r"-?\d+(\.\d+)?", value):
            value = float(value) if "." in value else int(value)
        elif value.lower() in ("true", "false"):
            value = value.lower() == "true"
        data[key] = value
    return data


def classify_fields(data: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    knobs: Dict[str, Any] = {}
    public: Dict[str, Any] = {}
    for k, v in data.items():
        lk = k.lower()
        if any(tk in lk for tk in TEXT_KEYS):
            public[k] = v
        else:
            knobs[k] = v
    return knobs, public


def format_value(v: Any) -> str:
    if isinstance(v, str):
        return f'"{v}"'
    return str(v)


def generate_cavecode(
    data: Dict[str, Any],
    original: str,
    title_guess: str = "Auto-Converted Card",
) -> str:
    knobs, public = classify_fields(data)

    lines = []

    lines.append("========================================")
    lines.append("🪨 CAVECODE CARD — AUTO-CONVERTED (v1.0)")
    lines.append("========================================")
    lines.append("")
    lines.append(f"Title: {title_guess}")
    lines.append("Source: auto-converted from existing config.")
    lines.append("")
    lines.append("========================================")
    lines.append("🧱 BLOCK 1 — SHELL")
    lines.append("========================================")
    lines.append("Short Description:")
    lines.append("    Converted from an existing config into CaveCode format.")
    lines.append("")
    lines.append("Goal:")
    lines.append("    🌐 Let a human tune values in one place without touching code.")
    lines.append("")
    lines.append("========================================")
    lines.append("✏️ BLOCK 3 — TUNING KNOBS")
    lines.append("========================================")
    if knobs:
        for k, v in knobs.items():
            lines.append(f"{k}: {format_value(v)}")
    else:
        lines.append("# (no numeric/boolean knobs detected)")
    lines.append("")
    lines.append("========================================")
    lines.append("🌐 BLOCK 4 — PUBLIC TEXT")
    lines.append("========================================")
    if public:
        for k, v in public.items():
            lines.append(f"{k}: {format_value(v)}")
    else:
        lines.append("# (no obvious public text fields detected)")
    lines.append("")
    lines.append("========================================")
    lines.append("📝 BLOCK 5 — HUMAN NOTES")
    lines.append("========================================")
    lines.append("# Original snippet (for reference):")
    lines.append("# (do not edit unless you know what you’re doing)")
    lines.append("")
    lines.append("```source")
    lines.append(original.rstrip())
    lines.append("```")
    lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: cavecode_convert.py <input-file | ->", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    raw = read_input(path)

    # 1) Try straight JSON
    ok, data = try_parse_json(raw)
    title_guess = "Auto-Converted Card"

    if not ok:
        # 2) Try JS wrapper strip
        js_inner = strip_js_wrapper(raw)
        ok, data = try_parse_json(js_inner)

    if not ok:
        # 3) Fallback: key=value mode
        data = parse_key_values(raw)

    # Try to guess a title from data
    for key in ("title", "TITLE", "name", "NAME"):
        if key in data and isinstance(data[key], str):
            title_guess = data[key]
            break

    cavecode = generate_cavecode(data, raw, title_guess=title_guess)
    sys.stdout.write(cavecode)


if __name__ == "__main__":
    main()
