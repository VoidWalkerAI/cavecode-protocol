# 🪨 CaveCode Teacher Pack v1.0  
_For any AI learning to read and write CaveCode_

---

## 1. What CaveCode Is

CaveCode is a **plain-text blueprint format** for describing systems
(games, programs, workflows) in a way that:

- humans can read and edit on a small phone  
- AI can generate and parse  
- developers can wire into engines or code

It is **not a programming language**.  
It is a **structured specification** sitting beside the code.

A CaveCode file is made of numbered **BLOCKS** with clear labels and
emoji glyphs describing purpose and safety.

---

## 2. Core Glyphs (You MUST Respect These)

Use ONLY these glyphs unless the user explicitly extends the set:

- `🧱` — Structural / Shell (title, purpose, high-level anatomy)  
- `🎮` — Behavior / Flow (game loop, program steps, state changes)  
- `🖍️` — Tuning Knobs / Human Edit Zone (parameters humans can safely edit)  
- `🌐` — Public Text (UI strings, messages, labels, dialog)  
- `🪨` — Fixed / Locked core identity (rarely changed; central rules)  
- `📝` — Human Notes (comments, ideas, TODOs, scratchpad)

**Do not invent new glyphs unless the user asks you to.**

---

## 3. Required Block Set (v1.0)

For any **complete CaveCode artifact** (game or program), include at least:

1. `🧱 BLOCK 1 — SHELL`  
   - Title  
   - Short Description  
   - Goal (what success looks like)

2. `🎮 BLOCK 2 — BEHAVIOR`  
   - For games: GAME LOOP / BEHAVIOR  
   - For scripts/programs: PROGRAM BEHAVIOR  
   - Describe:
     - What happens on start  
     - What inputs exist  
     - What happens on update/execute  
     - How it ends (finish/exit)

3. `🖍️ BLOCK 3 — TUNING KNOBS`  
   - Numeric / boolean / simple string parameters that can be safely tweaked:
     - speeds, limits, thresholds, difficulty, messages, flags  

4. `🌐 BLOCK 4 — PUBLIC TEXT`  
   - Any text shown to a human:
     - titles, prompts, labels, messages, narrative text  

5. `📝 BLOCK 5 — HUMAN NOTES`  
   - Comments, ideas, implementation tips, TODOs, future plans  

You may add more blocks (levels, entities, APIs, etc.) but these **five**
form a minimal, well-structured CaveCode card for most use cases.

---

## 4. Formatting Rules

- Use **plain text** (UTF-8).
- Separate major sections with ASCII dividers, for example:

  ```text
  ========================================
