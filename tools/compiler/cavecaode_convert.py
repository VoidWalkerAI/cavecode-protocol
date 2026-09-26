#!/usr/bin/env python3
"""Compatibility launcher for the historical misspelling of cavecode_convert."""

import sys

from cavecode_convert import main


if __name__ == "__main__":
    print(
        "NOTICE: use cavecode_convert.py; this misspelled launcher is retained for compatibility.",
        file=sys.stderr,
    )
    raise SystemExit(main())
