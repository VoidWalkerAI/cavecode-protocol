# 📘 CaveCode Micro Teaching Pack (v1.1)

A minimal training reference for engines learning to generate CaveCode.

This pack teaches:
- block ordering
- glyph usage
- human-edit zones
- AI-safe behavior rules

---

## 🧱 Core Structure (Always in this order)

1. 🪨 **BLOCK 1 — IDENTITY**  
   Locked. AIs must not rewrite.  
   Contains title, purpose, version, audience.

2. 🎚️ **BLOCK 2 — TUNING KNOBS**  
   Human-editable values. AIs preserve names, humans edit values.

3. 🌐 **BLOCK 3 — PUBLIC TEXT**  
   UI strings, labels, dialog. Safe for humans to modify.

4. 🔧 **BLOCK 4 — BEHAVIOR**  
   Logic, flow, or procedural steps. AIs may extend but must not delete meaning.

5. 📝 **BLOCK 5 — HUMAN NOTES**  
   Freeform human comments, TODOs, ideas.

---

## 🌀 Glyph Legend

🪨 structural shell  
🔧 behavior / flow  
🎚️ knobs  
🌐 public text  
📝 human notes  

Engines must use these glyphs in headings and lists.

---

## ⚠️ AI Rules

- Never overwrite BLOCK 1.  
- Never delete human comments in BLOCK 5.  
- Never change knob *names* — only values.  
- Maintain block order exactly.  
- Preserve indentation, formatting, and glyphs.  
- Additions must appear inside the appropriate block.

---

## ✔️ Minimal Example Card

```
+------------------------------+
|  CAVECODE ARTIFACT — EXAMPLE |
+------------------------------+

// BLOCK 1 — IDENTITY [LOCKED]
TITLE: Example Artifact
PURPOSE: Demonstrate minimal CaveCode
VERSION: 1.0

// BLOCK 2 — TUNING KNOBS
example_rate: 10
message_color: "blue"

// BLOCK 3 — PUBLIC TEXT
ui_header: "Hello World"
ui_button: "Press"

// BLOCK 4 — BEHAVIOR
FLOW_START:
 - DISPLAY ui_header.
 - WAIT for button.
 - PRINT confirmation.

FLOW_END

// BLOCK 5 — HUMAN NOTES
[TODO] Add options.
```

---

Engines should be able to reproduce this format without drift.
