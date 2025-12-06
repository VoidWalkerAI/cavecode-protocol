# Link Harvester — CaveCode Artifact (v1.0)

**Type:** Mobile-first HTML utility  
**Protocol:** CaveCode v1.0 (Blocks 1–4)  
**Author:** VoidWalker + AI collaborators (Claude / Ash stack)  

---

## What this artifact does

Link Harvester is a small, browser-based tool for **archiving chat links** into
local `.md` files.

- Accepts a chat URL
- Lets you pick or type a **Project / Category**
- Auto-numbers chats (e.g., `chat_001_2025-12-05_19-37.md`)
- Stores a **harvest history** in `localStorage`
- Designed to be **mobile-first** (phone + tablet friendly)

Because of normal browser security / CORS rules, it **does not actually scrape**
remote sites. Instead it:

1. Generates a markdown stub that includes the original URL and timestamp  
2. Instructs the user to copy/paste the conversation text manually  
3. Downloads the prepared `.md` file to the device

It’s a **personal archiving assistant**, not a scraper.

---

## CaveCode structure

This artifact follows the CaveCode block pattern:

- **BLOCK 1 — IDENTITY**  
  Title, purpose, and “for whom” description (locked / not AI-rewritable).

- **BLOCK 2 — HUMAN EDIT ZONE**  
  Tunable knobs:
  - naming + counter behaviour  
  - project presets  
  - filename format  
  - storage rules  

- **BLOCK 3 — PUBLIC TEXT**  
  UI labels, button text, error messages, and help copy.

- **BLOCK 4 — LOCKED LOGIC**  
  Core app wiring:
  - state + `localStorage`  
  - filename generation  
  - fake `fetchChatContent` stub  
  - history list rendering  
  - mobile-first UI hooks

You can validate block presence and basic structure with the CaveCode validators
in `/tools/validator/`.

---

## How to run

No build step. Just open the file in a browser.

1. Download or clone this repo.
2. Open `artifacts/link-harvester/link_harvester_v1.html` in any modern browser  
   (mobile or desktop).
3. Paste a chat URL, pick a project, and click **“Harvest Chat.”**

The browser will download a `.md` file with your chosen name pattern.

---

## Notes & roadmap

- This artifact is intentionally **client-only** so it can run offline or in
  constrained environments.
- A future **server-side companion** could:
  - actually fetch and clean chat HTML  
  - normalize different providers into one markdown format  
  - push archives into Git, S3, or a knowledge base

For now, this version is meant as a **reference implementation** showing how a
full CaveCode artifact can drive a real, usable tool.
