#!/usr/bin/env python3
"""Compatibility launcher for the removed, unratified v1.1 dialect."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_cavecode import main  # noqa: E402


if __name__ == "__main__":
    print(
        "NOTICE: CaveCode v1.1 was never ratified; using the stabilized v1.0 validator.",
        file=sys.stderr,
    )
    raise SystemExit(main())
