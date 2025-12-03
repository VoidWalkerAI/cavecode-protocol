# 🪨 CaveCode Protocol

**The official specification for CaveCode** —  
a glyph-based, text-first architecture for humans and AI to co-build systems.

This repository defines:

- the **glyph legend** (🪨, 🖍️, 🔧, 🎮, 🌐)
- the **block structure** (BLOCK 1, 1A, 2, …)
- the **CaveCode v1.0 spec**
- the **validator script**
- canonical **examples**

CaveCode is:

- **Device-agnostic** — plain text, works anywhere
- **AI-native** — designed to be read, written, and enforced by AI agents
- **Human-readable** — a single person on a phone can read and tweak it
- **Governed** — the meaning of the glyphs is protected by this protocol

---

## 📂 Repository Layout

```text
founding/        # Origin documents (Founding Card)
spec/            # Protocol documents (spec, glyphs, blocks, governance)
tools/           # Validator and future automation tools
examples/        # Minimal CaveCode examples
badges/          # "Built with CaveCode" badges

Key entries:

founding/CaveCode_v1_FoundingCard.txt

spec/cavecode-spec-v1.0.md

tools/validator/validate_cavecode.py



---

📜 Versioning

Current protocol version: CaveCode v1.0

All v1.0-compliant artifacts MUST follow this spec.

Future drafts will live under /spec/ as cavecode-spec-v1.1-draft.md, etc.

The glyph meanings (🪨, 🖍️, 🔧, 🎮, 🌐) are stable and protected by license.



---

✅ What It Means To Be “CaveCode-Compliant”

A file is CaveCode v1.0 compliant if:

1. It is plain text (UTF-8).


2. It uses BLOCK sections (e.g., BLOCK 1, BLOCK 2, BLOCK 3…)


3. At least one of the standard glyphs appears and follows the meanings in spec/cavecode-glyphs-and-crayons.md


4. It is understandable by a non-coder who has read the spec.



The official validator can help check this:

python tools/validator/validate_cavecode.py path/to/file.cavecode


---

🤝 Using CaveCode in Your Own Projects

1. Read the spec:
spec/cavecode-spec-v1.0.md


2. Mark your human/AI “law zones” with glyphs:

🪨 Locked logic

🖍️ Human edit zone

🔧 Extension zone

🎮 Game/engine logic

🌐 Public-safe text



3. Optionally add the badge from badges/ to your README.


4. Keep the glyph meanings intact and include the license.




---

⚖️ License

See LICENSE.md.

Summary (not legal text):
You may use, study, remix, and build on this protocol, as long as you:

preserve the meaning of the glyph legend

give appropriate credit to SageWire Syndicate and original authors

keep CaveCode files inspectable by their users



---

🧱 Origin

CaveCode emerged from a mobile-first forge:

conceived and tested on a phone and tablet

hardened in real projects (Arcade Planet, HerdMate-adjacent tools)

documented here so others can build their own worlds


> “The world is not discovered. It is forged.”
— CaveCode Founding Card, Block 1
