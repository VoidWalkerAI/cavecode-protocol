# CaveCode Full Teaching Pack (v1.0)

This pack teaches humans and AI to create CaveCode without turning one useful
example into a rigid universal layout.

## 1. What CaveCode does

CaveCode is a plain-text map beside or within a project. It exposes meaning,
interaction boundaries, project truth, and the next place to resume work.

It is not executable syntax and it does not replace the implementation.

## 2. The five canonical glyphs

- 🪨 **Locked** — protected identity, rules, invariants, or structure
- 🖍️ **Human Edit Zone / Crayon** — safe and intended for human editing
- 🔧 **Expandable** — additions, experiments, future work, or open questions
- 🎮 **Behavior** — logic, mechanics, flow, processing, or state transitions
- 🌐 **Public-Safe** — material approved for public-facing use

The crayon is 🖍️. Tuning knobs, operator settings, calibration values, and
human notes may all use the crayon when they are genuinely human-editable.

## 3. Blocks

```text
🪨 BLOCK 1 — IDENTITY
🎮 BLOCK 2 — MAIN FLOW
🖍️ BLOCK 3 — SAFE SETTINGS
🖍️ BLOCK 4 — HUMAN NOTES
🔧 BLOCK 5 — FUTURE WORK
```

The number is an address, the glyph is a role, and the title is the subject.
There may be any number of blocks. Glyphs may be reused. Do not force every
artifact into five blocks or assign meaning solely from block position.

## 4. Artifact Map

Use an Artifact Map for one bounded system. Include only the blocks needed to
make its identity, behavior, boundaries, and safe edit areas plain.

```text
============================================================
EXAMPLE.cavecode.txt
Example Monitor — Artifact Map
============================================================

🪨 BLOCK 1 — IDENTITY
NAME: Example Monitor
PURPOSE: Alert when a reading crosses a threshold.

🖍️ BLOCK 2 — CRAYON SETTINGS
THRESHOLD: 10
ALERT_TEXT: "Threshold crossed."

🎮 BLOCK 3 — BEHAVIOR
1. Read the sensor.
2. Compare the reading with THRESHOLD.
3. Emit ALERT_TEXT when the threshold is crossed.

🔧 BLOCK 4 — FUTURE WORK
- Add a second sensor.

🌐 BLOCK 5 — PUBLIC DESCRIPTION
A small threshold monitor described with CaveCode.
```

## 5. Repository Master Project Map

Use a root-level `PROJECT-NAME.cavecode.txt` to manage the entire repository.
It is read first and remains the source for current project understanding.

At minimum it identifies:

- status, project identity, and purpose
- authority and deeper sources
- current project and runtime state
- settled decisions or protected contracts
- known problems and open questions
- current work and exact next action
- a dated handoff or resume checkpoint

It may grow as large as the project requires. Subsystem maps may be added when
they declare their scope and point back to the master.

## 6. Same-commit discipline

For meaningful project-state work:

1. make the implementation change
2. test it
3. update the Master Project Map to the resulting truth
4. commit the implementation, tests, and map together

Record planned work as planned. Record deployed work as deployed only after it
is deployed. The map does not need to predict its own commit hash.

## 7. AI behavior

An AI working under CaveCode should:

- read the repository master map first
- follow referenced authority before changing protected material
- honor each glyph's semantic role
- preserve human notes unless asked to change them
- update current state and the resume point with meaningful commits
- expose contradictions rather than silently choosing a convenient history
- never describe proposed work as completed

## 8. Validation

The validator can check encoding, block headers, canonical glyphs, duplicate
addresses, and required repository-map sections. It cannot determine whether a
project claim is true. CaveCode remains a human-readable truth discipline, not
a substitute for judgment.
