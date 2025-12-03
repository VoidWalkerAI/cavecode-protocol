# CaveCode Specification — v1.0

Status: **Stable**  
Scope: Core concepts, glyph meanings, block structure, and compliance rules.

---

## 1. Overview

CaveCode is a **plain-text protocol** for describing systems in a way that:

- humans can read and edit on any device
- AI agents can parse, obey, and transform safely
- culture and philosophy can be embedded alongside logic

CaveCode is **not** a programming language.  
It is a **map** for code, behavior, and narrative.

---

## 2. Core Elements

A CaveCode document is built from:

1. **Glyphs** — semantic markers (see `cavecode-glyphs-and-crayons.md`)
2. **Blocks** — labeled sections (see `cavecode-block-structure.md`)
3. **Plain text** — descriptions, lists, parameters

CaveCode makes no assumptions about the underlying implementation
(HTML/JS, Python, AppSheet, etc.). It only cares about **structure and intent**.

---

## 3. Compliance Requirements (v1.0)

A file is **CaveCode v1.0 compliant** if:

1. **Text Format**  
   - The file is plain text, encoded in UTF-8.

2. **Block Usage**  
   - The file contains at least one line containing the word `BLOCK`
     used as a section header (e.g., `BLOCK 1`, `BLOCK 2`, `BLOCK 1A`).
   - Blocks are visually separated (blank lines or separators).

3. **Glyph Usage**  
   - At least one of the standard glyphs appears:
     🪨, 🖍️, 🔧, 🎮, 🌐.
   - Glyphs are used consistently with meanings defined in
     `cavecode-glyphs-and-crayons.md`.

4. **Human Readability**  
   - A non-coder who has read this spec should be able to answer:
     - “Where is it safe to tweak things?”
     - “Where is the core logic described?”
     - “Where is the public text?”

If points (1)–(4) are met, tools MAY label the artifact:
**“CaveCode v1.0 Compliant.”**

---

## 4. Recommended File Extensions

CaveCode files MAY use:

- `.cavecode`
- `.cave`  
- `.txt` / `.md` (if clearly labeled as CaveCode within the repo)

For maximum clarity, `.cavecode` is preferred when supported.

---

## 5. The Validator

The official reference validator is:

- [`tools/validator/validate_cavecode.py`](../tools/validator/validate_cavecode.py)

It performs **heuristic checks**, not formal certification:

- presence of glyphs
- existence of BLOCK lines
- detection of obviously empty blocks

It is meant as a **helper**, not as a gatekeeping tool.

---

## 6. Backwards Compatibility

Future versions (v1.1, v2.0, etc.) MUST:

- preserve the meanings of the standard glyphs
- treat v1.0-compliant documents as valid input
- MAY introduce additional glyphs or metadata, but not change the
  semantics of 🪨, 🖍️, 🔧, 🎮, 🌐.

---

## 7. Governance

See: [`cavecode-governance.md`](cavecode-governance.md)

In summary:

- **SageWire Syndicate** acts as steward of the spec.
- Changes are proposed as text documents (e.g., `cavecode-spec-v1.1-draft.md`).
- Implementations are free to extend, but not to redefine the core glyphs.

---

## 8. Reference Implementations

Official public implementations include, but are not limited to:

- **CaveCode Arcade Planet** (VoidWalkerAI/cavecode-arcade-planet)

These show how CaveCode can guide:

- game engines
- configuration files
- teaching materials

---

## 9. Philosophy

CaveCode is rooted in three beliefs:

1. The bottleneck is **imagination**, not engineering.  
2. A human on a phone has as much right to architect as a team on workstations.  
3. Culture and logic belong in the same file.

For the full doctrinal origin, see:

- [`founding/CaveCode_v1_FoundingCard.txt`](../founding/CaveCode_v1_FoundingCard.txt)
