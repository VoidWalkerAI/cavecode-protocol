# CaveCode Governance (v1.0)

This document describes how the CaveCode protocol evolves.

---

## 1. Stewardship

The primary steward of CaveCode is:

- **SageWire Syndicate** (project identity)
- with authorship attributed to the original forgemaster(s)
  operating under the VoidWalker / SageWire banners.

Stewardship here means:

- maintaining the spec
- publishing new versions
- keeping glyph meanings stable
- curating official examples

---

## 2. Versioning

Versions follow a simple pattern:

- `v1.0` — Initial stable specification
- `v1.1`, `v1.2` — Backwards-compatible refinements
- `v2.0` — Potentially breaking changes (not expected soon)

Drafts are stored as:

- `cavecode-spec-v1.1-draft.md`
- `cavecode-spec-v2.0-draft.md`

Once approved, they become:

- `cavecode-spec-v1.1.md` (etc.)

---

## 3. Change Principles

Any proposed change MUST respect:

1. **Glyph Stability**  
   The meanings of 🪨, 🖍️, 🔧, 🎮, 🌐 are **not negotiable**.

2. **Human Readability**  
   Changes should not make CaveCode harder for non-coders to understand.

3. **Device Agnosticism**  
   The protocol must remain implementable on low-power devices and phones.

4. **AI Cooperation**  
   The format must remain easy for AI agents to read and generate.

---

## 4. Community Input

While this repository is stewarded by SageWire Syndicate, outside
contributors may:

- open issues describing real-world use cases
- propose improvements via pull requests
- share example CaveCode artifacts

Stewards retain final say over the official spec, but real usage informs
future versions.

---

## 5. Compliance & Badges

Projects MAY advertise compliance using badges from `/badges/`.

- “CaveCode Compliant” — uses glyphs and blocks per spec.
- “CaveCode Inside” — uses CaveCode internally for architecture.

Badges are a **signal**, not a legal certification.

---

## 6. Deviation & Forks

Anyone may:

- fork this repo
- create alternate conventions
- experiment with new glyphs

However, they MUST NOT claim to be “CaveCode v1.x compliant” if they
change the meaning of the standard glyphs.

They are encouraged instead to:

- link back to this repo as the original spec
- describe their work as “CaveCode-inspired” or “CaveCode-derived”
