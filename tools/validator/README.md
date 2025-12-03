# CaveCode Validator (Reference Tool)

This folder contains a **reference implementation** of a CaveCode
validator.

The script:

- checks for BLOCK headers
- checks for presence of standard glyphs
- warns about obviously empty blocks

It is intentionally simple:

- easy to read on a phone
- easy to modify for custom workflows

Usage:

```bash
python tools/validator/validate_cavecode.py path/to/file.cavecode
