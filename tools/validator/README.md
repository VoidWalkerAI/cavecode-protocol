# CaveCode v1.0 Reference Validator

The validator checks:

- canonical block-header syntax
- the five canonical glyphs
- unique block addresses
- minimum Master Project Map concepts when the project profile is detected
- obvious legacy v1.1 glyph drift

```bash
python tools/validator/validate_cavecode.py path/to/file.cavecode.txt
python tools/validator/validate_cavecode.py --profile project PROJECT.cavecode.txt
```

Validation is deliberately structural and heuristic. It cannot prove that a
status claim is true or that a human edit zone is safe. The repository map,
tests, implementation, and human judgment must agree.

`validate_cavecode_v1_1.py` remains only as a compatibility launcher. It emits
a notice and delegates to the stabilized v1.0 validator.
