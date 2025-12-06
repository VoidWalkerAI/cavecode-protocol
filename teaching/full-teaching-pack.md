# 📘 CaveCode Full Teaching Pack (v1.1)

This document teaches engines and humans how to speak CaveCode consistently.
It enforces structure, prevents drift, and standardizes multi-engine artifacts.

---

# 1. 🪨 Block Architecture

Every CaveCode artifact contains these blocks in this exact order:

---

### 🪨 **BLOCK 1 — IDENTITY (Locked)**  
AIs must never change anything here.  
Contains:
- TITLE  
- PURPOSE  
- VERSION  
- AUDIENCE  
- AUTHOR  
- Notes about origin if needed  

This block defines *what the artifact is*.

---

### 🎚️ **BLOCK 2 — TUNING KNOBS**  
Human-editable parameters.

Rules:
- AIs preserve knob names.  
- AIs must not rewrite identifying metadata.  
- Humans freely adjust values.  
- All knobs written as `name: value`.

---

### 🌐 **BLOCK 3 — PUBLIC TEXT**  
Visible UI strings, labels, prompts, dialog.

Rules:
- Safe for humans to edit anytime.  
- AIs must preserve structure and field names.  
- Plain text only.

---

### 🔧 **BLOCK 4 — BEHAVIOR**  
Defines logic, program flow, or system sequence.

Rules:
- Written as declarative steps.  
- AIs may expand, but must not break meaning.  
- Use labels like FLOW_START / FLOW_END.  
- Subflows allowed.

---

### 📝 **BLOCK 5 — HUMAN NOTES**  
For humans only: ideas, todos, design notes.

Rules:
- AIs preserve all human notes exactly.  
- AIs may append new notes *beneath a divider* if requested.

---

# 2. 🌀 Glyph Lexicon

Official glyphs:

🪨 structural / wrapper  
🔧 behavior, flow  
🎚️ user parameters  
🌐 public UI text  
📝 human notes  

Engines must always use these glyphs in headers and lists.

---

# 3. 🚫 Drift Prevention Rules

Engines must:

- keep block order  
- preserve glyphs  
- keep human notes untouched  
- never rewrite BLOCK 1  
- maintain formatting and indentation  
- generate complete blocks, never partials  
- avoid hallucinating custom symbols unless requested  
- ensure example cards always compile under the validator

---

# 4. ✔️ Reference Mini-Artifact

```
+----------------------------------------+
|  CAVECODE ARTIFACT — COUNTER DEMO (v1) |
+----------------------------------------+

// BLOCK 1 — IDENTITY [LOCKED]
TITLE: Counter Demo
PURPOSE: Show minimal behavior logic
VERSION: 1.0
AUDIENCE: Beginners

// BLOCK 2 — TUNING KNOBS
start_value: 0
increment:   1

// BLOCK 3 — PUBLIC TEXT
ui_label: "Counter:"
ui_button: "Add"

// BLOCK 4 — BEHAVIOR
FLOW_START:
 - SET counter = start_value.
 - DISPLAY ui_label with counter.
ON_PRESS:
 - counter = counter + increment.
 - REFRESH UI.

FLOW_END

// BLOCK 5 — HUMAN NOTES
[IDEA] Add subtract mode.
```

---

# 5. 🧪 Engine Behavior Guidelines

When producing CaveCode, engines must:

- follow the structure exactly  
- not invent new blocks unless instructed  
- use only approved glyphs  
- maintain clarity and mobile readability  
- default to explicit, step-listed behavior  
- prefer declarative descriptions over code  

---

# 6. 📄 Formatting Rules

- Width flexible for mobile  
- Emojis must be preserved  
- Comments use `//`  
- Divider lines allowed but not required  
- Artifact header box recommended but optional  

---

# 7. 🔧 Best Practices for Engines

Engines should:

- request clarification when BLOCK 1 is ambiguous  
- default to minimalism when uncertain  
- standardize timestamps to ISO  
- keep human-edit knobs close to the top for mobile editing  
- keep PUBLIC TEXT readable at a glance  

---

# 8. 🧱 Validation Compatibility

This pack aligns with:

- CaveCode Spec v1.1  
- Minimal Validator  
- Strict Validator  
- Gemini, Claude, OpenAI, Perplexity engines  

Anything produced with this pack should pass strict validation.

---

End of Full Teaching Pack.
