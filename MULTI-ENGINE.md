# CaveCode Multi-Engine Compliance Log

This is the lab notebook for testing how AI engines read and write the ratified
CaveCode v1.0 contract.

## Current test contract

An engine receives the v1.0 teaching pack and is asked to create or modify an
Artifact Map or Repository Master Project Map.

Evaluation asks whether the engine:

1. uses only the canonical block-role glyphs: 🪨, 🖍️, 🔧, 🎮, 🌐
2. preserves each glyph's semantic meaning
3. understands that block numbers are addresses rather than roles
4. permits variable block counts and repeated glyphs
5. preserves protected and human-authored material
6. distinguishes planned, implemented, tested, committed, and deployed state
7. leaves a usable resume point in Repository Master Project Maps

## Current matrix

| Engine/artifact | Status under stabilized v1.0 | Notes |
|---|---|---|
| Repository templates and examples | Revalidation in progress | Covered by local automated tests |
| OpenAI historical artifacts | Historical evidence | Must not be treated as normative |
| Gemini link-tagger artifacts | Historical v1.1-drift evidence | Preserved under `artifacts/gemini/` |
| Claude drift-test artifacts | Historical evidence | Preserved under `artifacts/Claude/` |

Earlier scores that treated 🎚️ and 📝 as official or forced one five-block
order are retired. The artifacts remain useful because they show exactly how
protocol drift can occur.

## Adding a test

Store engine output under `artifacts/<engine>/` and include:

- raw output
- normalized output, if one is produced
- engine and prompt context
- validator output
- human semantic review
- the date and ratified spec version used

Never normalize the raw artifact in place. Evidence and repair are separate.
