📘 CaveCode Validator (Reference Tool)

This folder contains reference implementations of CaveCode validators.

These scripts verify that a .cavecode file follows the official CaveCode format, ensuring:

correct block structure

correct glyph usage

required sections are present

basic internal sanity checks


All validators are:

readable on a phone

easy to modify

suitable for both humans and AI tooling workflows



---

🧪 Available Validators

1️⃣ validate_cavecode.py — Minimal Validator

This simple validator checks:

presence of block headers

general CaveCode formatting

basic sanity of file structure


It is intentionally lightweight and ideal for quick checks or when working in constrained environments.


---

2️⃣ validate_cavecode_v1_1.py — Enhanced Protocol Validator

This improved validator adds deeper, protocol-aligned checks:

strict block-header format verification

enforcement of official glyphs

required blocks must be present:

🧱 BLOCK 1 — SHELL

🎮 BLOCK 2 — (GAME LOOP / PROGRAM BEHAVIOR)

🖍️ BLOCK 3 — TUNING KNOBS

🌐 BLOCK 4 — PUBLIC TEXT

📝 BLOCK 5 — HUMAN NOTES


warnings if:

tuning knobs block contains no editable parameters

public text block contains no user-facing fields



Use this version when you need full CaveCode compliance or when preparing artifacts for public release.


---

🧰 Usage

python tools/validator/validate_cavecode.py path/to/file.cavecode

python tools/validator/validate_cavecode_v1_1.py path/to/file.cavecode


---

✔ Validator Status

Both tools are stable.
For all new .cavecode artifacts, v1.1 is recommended.


---

📝 Notes for Developers

These validators are intentionally simple so they can be adapted by teams, teachers, or multiple AIs.

If you extend the CaveCode protocol, you may also extend the validator to align with your custom blocks or glyphs.

Additional validators can be added in this folder (e.g., v1.2 with auto-fix mode).

---
🪨 Generated & Maintained by the CaveCode Protocol Team
