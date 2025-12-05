#!/usr/bin/env python3
"""
CaveCode → Code Compiler Pass v1.0

Takes a CaveCode spec that includes an OUTPUT_MESSAGE knob (and optional
CLASS_NAME) and emits a simple "Hello, World"-style program in the
requested language.

Usage:
    python cavecode_to_code.py --lang python  path/to/card.cavecode
    python cavecode_to_code.py --lang js      path/to/card.cavecode
    python cavecode_to_code.py --lang java    path/to/card.cavecode
"""

import sys
import re
from pathlib import Path
from typing import Dict, Optional


def parse_args(argv):
    lang = None
    path = None
    i = 1
    while i < len(argv):
        if argv[i] == "--lang" and i + 1 < len(argv):
            lang = argv[i + 1].lower()
            i += 2
        else:
            path = argv[i]
            i += 1
    if not lang or not path:
        print("Usage: cavecode_to_code.py --lang [python|js|java] path/to/file.cavecode",
              file=sys.stderr)
        sys.exit(1)
    if lang not in ("python", "js", "javascript", "java"):
        print(f"Unsupported language: {lang}", file=sys.stderr)
        sys.exit(1)
    if lang == "javascript":
        lang = "js"
    return lang, Path(path)


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_knobs(text: str) -> Dict[str, str]:
    """
    Very simple parser: within the 🖍️ BLOCK 3 — TUNING KNOBS section,
    look for lines like KEY: value and capture them.
    """
    knobs: Dict[str, str] = {}
    inside_knobs = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("🖍️ BLOCK 3") or "TUNING KNOBS" in stripped:
            inside_knobs = True
            continue
        if stripped.startswith("🌐 BLOCK 4") or stripped.startswith("📝 BLOCK 5"):
            inside_knobs = False
        if not inside_knobs:
            continue
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()
        # Remove trailing inline comments like "# something"
        if "#" in value:
            value = value.split("#", 1)[0].strip()
        # Strip surrounding quotes
        value = value.strip('"').strip("'")
        knobs[key] = value
    return knobs


def extract_title(text: str) -> Optional[str]:
    for line in text.splitlines():
        if line.strip().startswith("Title:"):
            return line.split(":", 1)[1].strip()
    return None


def generate_python(title: str, output_message: str) -> str:
    return f'''"""
{title}
Auto-generated from CaveCode by cavecode_to_code.py
"""

def main():
    message = "{output_message}"
    print(message)


if __name__ == "__main__":
    main()
'''


def generate_js(title: str, output_message: str) -> str:
    return f'''// {title}
// Auto-generated from CaveCode by cavecode_to_code.js (python script output)

function main() {{
    const message = "{output_message}";
    console.log(message);
}}

main();
'''


def generate_java(title: str, output_message: str, class_name: str) -> str:
    return f'''// {title}
// Auto-generated from CaveCode by cavecode_to_code.py

public class {class_name} {{
    public static void main(String[] args) {{
        String message = "{output_message}";
        System.out.println(message);
    }}
}}
'''


def main():
    lang, path = parse_args(sys.argv)
    text = read_file(path)
    knobs = extract_knobs(text)
    title = extract_title(text) or "CaveCode Program"

    output_message = knobs.get("OUTPUT_MESSAGE", "Hello from CaveCode!")
    class_name = knobs.get("CLASS_NAME", "CaveCodeProgram")

    if lang == "python":
        code = generate_python(title, output_message)
    elif lang == "js":
        code = generate_js(title, output_message)
    elif lang == "java":
        code = generate_java(title, output_message, class_name)
    else:
        raise SystemExit(f"Unexpected lang: {lang}")

    sys.stdout.write(code)


if __name__ == "__main__":
    main()
