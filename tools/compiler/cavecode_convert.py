#!/usr/bin/env python3
"""Convert a small configuration object into a CaveCode v1.0 Artifact Map."""

import json
import re
import sys
from pathlib import Path
from typing import Any


TEXT_KEYS = ("text", "message", "title", "label", "caption", "prompt")


def read_input(path: Path) -> str:
    return sys.stdin.read() if path == Path("-") else path.read_text(encoding="utf-8")


def parse_input(text: str) -> dict[str, Any]:
    candidates = [text]
    start, end = text.find("{"), text.rfind("}")
    if start >= 0 and end > start:
        candidates.append(text[start : end + 1].replace("'", '"'))
    for candidate in candidates:
        try:
            value = json.loads(candidate)
            if isinstance(value, dict):
                return value
        except (TypeError, ValueError):
            pass

    data: dict[str, Any] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = (part.strip() for part in line.split("=", 1))
        value = value.strip('"').strip("'")
        if re.fullmatch(r"-?\d+(?:\.\d+)?", value):
            data[key] = float(value) if "." in value else int(value)
        elif value.lower() in {"true", "false"}:
            data[key] = value.lower() == "true"
        else:
            data[key] = value
    return data


def render_value(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False)


def render(data: dict[str, Any], original: str) -> str:
    title = next(
        (str(data[key]) for key in ("title", "TITLE", "name", "NAME") if key in data),
        "Auto-Converted Artifact",
    )
    public = {
        key: value
        for key, value in data.items()
        if any(token in key.lower() for token in TEXT_KEYS)
    }
    settings = {key: value for key, value in data.items() if key not in public}
    setting_lines = "\n".join(f"{key}: {render_value(value)}" for key, value in settings.items()) or "# No settings detected."
    public_lines = "\n".join(f"{key}: {render_value(value)}" for key, value in public.items()) or "# No public text detected."

    return f"""============================================================
AUTO-CONVERTED.cavecode.txt
{title} — CaveCode Artifact Map
============================================================

🪨 BLOCK 1 — IDENTITY
NAME: {title}
PURPOSE: Preserve a configuration as a human-readable CaveCode map.

🖍️ BLOCK 2 — CRAYON / HUMAN EDIT ZONE
{setting_lines}

🌐 BLOCK 3 — PUBLIC-SAFE TEXT
{public_lines}

🎮 BLOCK 4 — BEHAVIOR
1. Load the values from Blocks 2 and 3.
2. Apply them in the consuming implementation.

🖍️ BLOCK 5 — HUMAN NOTES
Original source is preserved below for review.

```source
{original.rstrip()}
```
"""


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: cavecode_convert.py <input-file | ->", file=sys.stderr)
        return 2
    raw = read_input(Path(sys.argv[1]))
    print(render(parse_input(raw), raw), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
