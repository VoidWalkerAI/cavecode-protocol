# 🌌 CaveCode Multi-Engine Compliance Log

A living scoreboard for how different AI engines read, write, and respect the **CaveCode Protocol**.

This document tracks:

- which engines have attempted CaveCode artifacts  
- whether they followed the block structure and rules  
- where drift appears (glyphs, labels, URL handling, etc.)  
- links to raw vs. normalized examples for each engine  

It sits beside the spec as a **neutral lab notebook** for multi-engine behavior.

---

## 🧪 Test Rules (v1.1)

Unless noted otherwise, every engine test follows these rules:

1. **Prompt type**  
   - A plain request:  
     > “Generate a CaveCode artifact for X using the CaveCode block structure.”
   - No hidden pre-training, no uploaded teaching pack unless explicitly marked.

2. **Required output structure**
   - Numbered / clearly separated blocks:
     - **IDENTITY / SHELL**  
     - **TUNING KNOBS** (or equivalent)  
     - **PUBLIC TEXT**  
     - **BEHAVIOR / FLOW**  
     - **HUMAN NOTES**
   - Clear comments indicating what humans edit vs. what AIs must not overwrite.

3. **Evaluation**
   - **Structural pass**: blocks present, in order, and clearly labeled.  
   - **Glyph pass**: official emojis used correctly (🪨, 🔧, 🎚️, 🌐, 📝).  
   - **Behavior clarity**: logic or flow is understandable and executable.  
   - **Drift notes**: any odd substitutions, naming drift, or spec violations.

4. **Artifacts**
   - **Raw file**: exactly what the engine produced.  
   - **Normalized file**: cleaned to match spec, without changing the intent.  
   - **Folder README**: notes about what happened in the test.

---

## 📊 Current Engine Matrix

| Engine      | Vendor  | Test ID                     | Teaching Pack? | Spec Ver. | Structural Pass | Glyph Pass | Drift Level | Folder / Notes |
|------------|---------|-----------------------------|----------------|-----------|-----------------|-----------|------------|----------------|
| **OpenAI** (Ash) | OpenAI | _Reference artifacts_        | N/A (native)   | 1.1       | ✅ Reference    | ✅         | —          | Primary reference cards across repo. |
| **Gemini** | Google | `gemini-link-tagger-001`     | ❌ Cold start   | 1.1       | ✅ Yes          | ⚠️ Partial | Low (cosmetic) | [`artifacts/gemini/`](./artifacts/gemini/README.md) |

Legend:

- **Structural Pass** – All required blocks are present and in valid sequence.  
- **Glyph Pass** – Correct use of 🪨, 🔧, 🎚️, 🌐, 📝.  
- **Drift Level** –  
  - **Low**: cosmetic issues only (e.g., odd text substitution).  
  - **Medium**: minor spec breaks, intent still clear.  
  - **High**: structure or rules not followed; not valid CaveCode.

---

## 🧬 Gemini Test Notes (v1.0)

Folder: [`artifacts/gemini/`](./artifacts/gemini/README.md)  

Artifacts:

1. `gemini-link-tagger_raw_v1.cavecode`  
   - Exactly what Gemini produced.  
   - Correct block ordering and knobs.  
   - Solid behavior description.  
   - **No official glyph labels.**  
   - Injected a strange `google.com/search?q=URL` substitution in several comments.  
   - Otherwise structurally valid.

2. `gemini-link-tagger_v1_1.cavecode`  
   - Ash-normalized, spec-clean version.  
   - Added official glyph markers.  
   - Removed the `google.com/search?q=URL` substitution.  
   - Updated version tag to `v1.1` to match spec.  
   - Ensured headers and comments are mobile-readable.  

Conclusion for Gemini (cold start):

- Understood the **block concept** correctly.  
- Captured purpose, knobs, behavior, and human notes.  
- Only drift was cosmetic, not structural.  
- Confirms that CaveCode is **readable and learnable** without a teaching pack.

---

## 🧱 How to Add a New Engine Test

When you run CaveCode through a new engine (Claude, Perplexity, LLaMA, etc.), follow this pattern:

1. **Create a folder**

   ```text
   artifacts/<engine-name>/
