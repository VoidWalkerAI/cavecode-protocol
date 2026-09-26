# CaveCode Block Structure (v1.0)

CaveCode groups related meaning into labeled blocks that remain readable on a
phone and locatable by humans or AI.

## Required block anatomy

A block header has:

- one canonical role glyph
- the word `BLOCK`
- a numeric or alphanumeric address
- a clear title

```text
🪨 BLOCK 1 — SYSTEM IDENTITY
🎮 BLOCK 2 — MAIN FLOW
🎮 BLOCK 2A — ERROR RECOVERY
🖍️ BLOCK 3 — OPERATOR SETTINGS
🌐 BLOCK 4 — PUBLIC MESSAGES
🔧 BLOCK 5 — FUTURE INTEGRATIONS
```

## Meaning

- **Address** tells the reader where the block is.
- **Glyph** tells the reader how to treat it.
- **Title** tells the reader what it concerns.

Block number does not determine meaning. CaveCode does not require five blocks
or a fixed order. Use as many blocks as the system needs, and reuse a glyph
whenever the same semantic role appears again.

Prefer one primary role per block. If a section mixes protected rules, safe
human settings, and future ideas, split it until the interaction boundary is
clear.

## Artifact Map guidance

A small artifact will often need blocks for:

- identity or invariants — 🪨
- behavior or flow — 🎮
- safe settings or notes — 🖍️
- public-facing material — 🌐
- extensions or open work — 🔧

This is a useful pattern, not a mandatory five-position schema.

## Repository Master Project Map guidance

A repository map may be much larger. Its blocks should expose current truth,
authority, decisions, runtime state, open questions, current work, next action,
and handoff checkpoints. Historical checkpoints may be appended so long as the
current-state and resume sections remain easy to find.

## Mobile design principle

> A person on a phone should be able to find the relevant block, understand its
> role, make an authorized change, and know what happens next without first
> learning a private syntax.
