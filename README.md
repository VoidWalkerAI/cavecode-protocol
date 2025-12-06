# CaveCode Protocol

CaveCode is a plain-text blueprint format for describing systems, games,
and tools in a way that:

- humans can read and edit on a phone  
- AI can generate and parse  
- teams can share, remix, and reason about

It is **not** a programming language.  
It sits beside the code as a structured specification: numbered BLOCKS with
clear labels, emoji glyphs, and a dedicated “human edit zone”.

---

## Status

- Spec: **v1.1**
- Core blocks: SHELL, BEHAVIOR, TUNING KNOBS, PUBLIC TEXT, HUMAN NOTES
- Official glyphs:
  - 🧱  structural / shell
  - 🎮  behavior / game loop / program flow
  - 🖍️  tuning knobs (safe for humans to edit)
  - 🌐  public text (UI, labels, copy)
  - 📁  human notes (comments, ideas, TODOs)

This repo contains:

- the **spec and teaching docs**
- a **scaffold tool** to generate new cards
- **validators** (minimal + strict v1.1)
- a **fixer/normalizer** for old or messy cards
- examples written by humans and AI

---

## Quick Start

### 1. Generate a new CaveCode card

From the repo root:

```bash
python tools/scaffold/cavecode_new_card.py "My Artifact Name" > my-artifact.cavecode
