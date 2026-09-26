# CaveCode v1.0 Fixer

The fixer performs narrow legacy-glyph repairs on block headers:

- 🧱 shell/identity → 🪨
- 🎚️, ✏️, or 📝 → 🖍️
- legacy 🔧 behavior/flow/logic headers → 🎮

```bash
python tools/fixer/cavecode_fix_v1.py old.cavecode > repaired.cavecode.txt
```

It does not renumber blocks, force a five-block layout, rewrite titles, or
claim that the repaired document is semantically correct. Review the result.
