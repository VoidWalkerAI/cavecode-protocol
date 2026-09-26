# CaveCode Glyphs & Crayons (v1.0)

CaveCode uses a small set of glyphs so anyone can tell:

- what is safe to change
- what is dangerous to touch
- what is core logic
- what is public-facing text

These meanings are **normative** — they define the protocol.

---

## 🪨 Locked Block

**Symbol:** 🪨

Represents:

- engine logic
- core rules
- foundational philosophy

Change only if you understand the full consequences.
AI agents should treat these sections as **read-only** unless explicitly
instructed to refactor them.

---

## 🖍️ Human Edit Zone

**Symbol:** 🖍️

Represents:

- safe areas for non-coders to edit
- difficulty knobs, colors, messages, spawn rates
- narrative text, prompts, UI copy

These are the **crayon areas**.

A person on a phone should be able to:

- find these quickly
- change a value
- immediately feel the difference in behavior.

---

## 🔧 Expandable Block

**Symbol:** 🔧

Represents:

- optional extensions
- experimental mechanics
- future plans / hooks

These can start as comments or empty shells.
They invite humans or AI to add new behavior later.

---

## 🎮 Game Logic Block

**Symbol:** 🎮

Represents:

- core mechanics
- input handling
- update / tick logic
- collision, scoring, progression

These are often mirrored in code (HTML/JS, Python, etc.).
CaveCode makes them visible and locatable for non-coders.

---

## 🌐 Public-Safe Block

**Symbol:** 🌐

Represents:

- text that is safe to display publicly
- public-facing descriptions, credits, instructions

Use this glyph when a block is intended for screens, docs, marketing,
or classrooms.

---

## Semantic roles, not positions

Glyphs may appear on any block number and may be reused. A block number is an
address; it does not assign meaning. The crayon is always 🖍️. Symbols such as
🎚️, ✏️, 📝, and 🧱 may appear in ordinary prose, but they are not canonical
CaveCode v1.0 block-role glyphs.

## 🎨 Color Concept (Metaphor Only)

Although CaveCode is plain text, the mental color model is:

- Orange  → human-friendly titles & text
- Blue    → core logic / rules
- Green   → human-tweakable knobs
- Red     → dangerous / read-only

You do not have to literally color anything. The colors are a teaching
metaphor to help people reason about the sections.
