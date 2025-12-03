# CaveCode Block Structure (v1.0)

CaveCode organizes a design into **BLOCKS** so humans and AI can see the
map of the system at a glance.

---

## 🧱 What Is a BLOCK?

A BLOCK is a labeled section that groups related ideas or parameters.

A BLOCK MUST have:

- a clear title
- a numeric or alpha index (e.g., `BLOCK 1`, `BLOCK 1A`, `BLOCK 2`, …)
- at least one glyph indicating the role of the block

Example:

- 🪨 BLOCK 1 — GAME SHELL
- 🎮 BLOCK 2 — CORE LOOP
- 🖍️ BLOCK 3 — TUNING KNOBS

---

## 🔢 Numbering

Recommended scheme (not strictly enforced, but canonical):

- `BLOCK 1`, `BLOCK 2`, `BLOCK 3`, … → major sections
- `BLOCK 1A`, `BLOCK 1B` → sub-sections
- `BLOCK 10` often used as HUMAN NOTES in Founding Card style

Blocks should be:

- easy to scan on a phone
- short enough to fit in one viewport whenever possible

---

## 🧬 Suggested Minimal Block Set (for small systems)

For simple games or tools, CaveCode v1.0 recommends:

1. 🪨 BLOCK 1 — SHELL / OVERVIEW  
   Title, short description, goals, high-level rules.

2. 🎮 BLOCK 2 — CORE LOOP / FLOW  
   What happens each tick or major step.

3. 🎮 BLOCK 3 — INPUT / CONTROLS  
   Keys, taps, gestures, or triggers.

4. 🎮 BLOCK 4 — SCORING / STATE  
   Points, counters, lives, levels.

5. 🖍️ BLOCK 5 — TUNING KNOBS  
   Speed, colors, spawn rates, limits.

6. 🌐 BLOCK 6 — PLAYER-FACING TEXT  
   On-screen instructions, messages, credits.

7. 🔧 BLOCK 7+ — EXPANSIONS  
   Optional modes, powerups, future ideas.

This is a guideline, not a prison.  
The core requirement is **clarity** for non-coders.

---

## 🧠 Design Principle

> A single person on a phone should be able to:
> read it,  
> tweak one value,  
> and feel the difference,  
> without learning syntax.

If they cannot, consider adding more BLOCKS or moving parameters into
a dedicated 🖍️ Human Edit Zone.
