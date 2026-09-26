# CaveCode Protocol

**A SageWire Syndicate specification**

CaveCode is a plain-text mapping protocol for making software, hardware,
workflows, games, and other systems understandable to humans and AI.

It is not a programming language. It sits with or beside implementation and
records structure, intent, authority, safe edit areas, current state, and the
next place to resume work.

## Canonical v1.0 glyphs

| Glyph | Meaning |
|---|---|
| 🪨 | Locked — protected rules, identity, invariants, or structure |
| 🖍️ | Human Edit Zone — the **crayon**, safe and intended for human editing |
| 🔧 | Expandable — extensions, experiments, future work, or open areas |
| 🎮 | Behavior — mechanics, processing, flow, and state transitions |
| 🌐 | Public-Safe — material approved for public-facing use |

Glyphs are semantic roles. They are not five mandatory positions. A CaveCode
file may contain as many numbered blocks as clarity requires, and a glyph may
be reused.

## Two v1.0 profiles

### Artifact Map

Describes one artifact or subsystem: what it is, how it behaves, what is
protected, and what a human may safely change.

### Repository Master Project Map

Lives at the repository root as `PROJECT-NAME.cavecode.txt`. It is the
read-first source for current project understanding and human decisions.

A useful master map records:

- project identity and authority
- current implemented, tested, committed, and deployed state
- settled decisions and protected contracts
- known problems, failed approaches, and open questions
- affected repositories or subsystems
- current work, next action, and a cold-start resume point

For a meaningful project-state change, update the master map in the **same
commit** as the implementation. The commit is incomplete when its map describes
the state from before the commit.

## Read first

1. [`CAVECODE-PROTOCOL.cavecode.txt`](CAVECODE-PROTOCOL.cavecode.txt) — this
   repository's living project map
2. [`specs/cavecode_spec-v1.0.md`](specs/cavecode_spec-v1.0.md) — ratified
   protocol contract
3. [`specs/cavecode-glyphs_and_crayons.md`](specs/cavecode-glyphs_and_crayons.md)
4. [`specs/cavecode-block-and-structure.md`](specs/cavecode-block-and-structure.md)
5. [`specs/cavecode-governance.md`](specs/cavecode-governance.md)

## Quick start

Create an artifact map:

```bash
python tools/scaffold/cavecode_new_card.py "My Artifact" > MY-ARTIFACT.cavecode.txt
```

Create a repository master map:

```bash
python tools/scaffold/cavecode_new_card.py \
  --profile project "My Project" > MY-PROJECT.cavecode.txt
```

Validate either profile:

```bash
python tools/validator/validate_cavecode.py MY-PROJECT.cavecode.txt
```

Run repository tests:

```bash
python -m unittest discover -s tests -v
```

## Current status

CaveCode v1.0 is the stable foundation. The repository is undergoing a v1.0
stabilization pass that removes an inconsistent, unratified v1.1 dialect and
brings the documentation, examples, and tools back under one contract.
