# 🪨 CaveCode Compiler v1.0  
**Tools → Compiler**

The CaveCode Compiler is the first official translator that converts
existing configuration formats into clean, human-friendly CaveCode
cards.

This tool is not designed for developers.  
It is designed for **everyday humans** who want to take messy,
hard-to-edit code and transform it into a readable, editable,
CaveCode artifact.

---

## 🌐 Purpose

The compiler performs:

1. **Parsing** – reads the input file  
2. **Classification** – separates knobs, public text, and metadata  
3. **Generation** – outputs a full `.cavecode` file  
4. **Preservation** – embeds the original snippet safely in a notes block  

This lets anyone:

- take a JSON object  
- take a JS config object  
- take a `.env` style key/value list  
- take a messy settings block  

…and turn it into a **clean, block-mapped CaveCode card** they
can read on a phone.

---

## 📥 Accepted Input Formats

The compiler currently supports:

### ✔ JSON
```json
{ "speed": 6, "jump": 12, "game_over_message": "Try again!" }
