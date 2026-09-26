# CaveCode Specification — v1.0

Status: **Stable**
Scope: Core concepts, glyph meanings, block structure, artifact maps, and
repository master project maps.

## 1. Purpose

CaveCode is a plain-text protocol for describing systems so that:

- humans can understand and edit them on any device
- AI agents can locate intent, authority, and safe change boundaries
- interrupted work can be resumed without reconstructing old conversations
- decisions and implementation state can travel with the work

CaveCode is not a programming language. It is a map for implementation,
behavior, project state, and human intent.

## 2. Canonical glyph vocabulary

The five standard v1.0 glyphs are normative:

- 🪨 **Locked** — protected rules, identity, invariants, or structure
- 🖍️ **Human Edit Zone / Crayon** — safe and intended for human editing
- 🔧 **Expandable** — extensions, experiments, future work, or open areas
- 🎮 **Behavior** — mechanics, processing, flow, and state transitions
- 🌐 **Public-Safe** — material approved for public-facing use

Their full definitions are in
[`cavecode-glyphs_and_crayons.md`](cavecode-glyphs_and_crayons.md).

Other symbols may decorate prose, but they are not standard CaveCode block-role
glyphs. A v1.x document MUST NOT redefine the five standard meanings.

## 3. Block model

A CaveCode document contains labeled blocks.

```text
🪨 BLOCK 1 — SYSTEM IDENTITY
🎮 BLOCK 2 — MAIN FLOW
🖍️ BLOCK 3 — OPERATOR SETTINGS
🔧 BLOCK 4 — FUTURE INTEGRATIONS
```

- Block number or identifier = location/address.
- Glyph = semantic role.
- Block title = specific subject.
- There is no fixed block count.
- A standard glyph may be reused.
- Block order does not assign glyph meaning.

See [`cavecode-block-and-structure.md`](cavecode-block-and-structure.md).

## 4. Profiles

### 4.1 Artifact Map

An Artifact Map describes one implementation, tool, component, device,
workflow, game, or other bounded artifact.

It SHOULD make clear:

- what the artifact is
- important behavior and constraints
- what is protected
- what humans may safely edit
- what may be expanded
- what may be shown publicly

No fixed five-block template is required.

### 4.2 Repository Master Project Map

A repository managed with CaveCode SHOULD contain one root-level file named:

```text
PROJECT-NAME.cavecode.txt
```

A repository claiming **CaveCode Project-Managed v1.0** compliance MUST contain
one such file and designate it as its read-first Master Project Map.

The map MUST identify:

- project identity and purpose
- its authority and relationship to deeper sources
- current project state
- settled decisions or protected contracts
- known problems or unresolved questions
- current work and next action
- a cold-start resume or handoff point

It SHOULD distinguish, when relevant:

- planned
- implemented
- tested
- committed
- deployed
- superseded or rejected

Subsystem maps MAY exist. They MUST state their scope and point back to the
repository master map. They must not quietly become competing master truths.

## 5. Atomic state rule

When a meaningful commit changes project state, contracts, architecture,
behavior, deployment status, known problems, or next work, the Master Project
Map MUST be updated in the same commit.

The map describes the state produced by the commit. Planned work may be
forecast under an explicitly future-facing heading, but it MUST NOT be recorded
as implemented, tested, or deployed before that is true.

The map need not contain its own commit hash. Git history supplies the exact
hash and avoids a circular second commit.

## 6. Core compliance

A file is **CaveCode v1.0 compliant** when:

1. It is plain UTF-8 text.
2. It has at least one clearly labeled `BLOCK` header.
3. Each CaveCode block header uses one of the five standard glyphs.
4. Glyphs retain their canonical meanings.
5. A human reader can identify the purpose and intended interaction boundaries.

The validator performs structural and heuristic checks. Human judgment remains
necessary for semantic truth.

## 7. File extensions

The preferred human-facing form is `*.cavecode.txt`, because ordinary mobile
applications can open it. Bare `.cavecode` remains valid for tools and
environments that support it. Clearly labeled `.md` and `.txt` files MAY also
contain CaveCode.

## 8. Backwards compatibility

Future versions MUST preserve:

- the meanings of 🪨, 🖍️, 🔧, 🎮, and 🌐
- variable block counts
- reusable glyph roles
- readability without special software
- validity of conforming v1.0 documents

## 9. Governance and history

Governance is defined in
[`cavecode-governance.md`](cavecode-governance.md).

Historical artifacts, including the Arcade Planet founding declaration and the
Builder's Log, preserve origin and development context. They do not override
the ratified specification or a project's current Master Project Map.
