#!/usr/bin/env python3
"""Print a CaveCode v1.0 Artifact Map or Repository Master Project Map."""

import argparse
from datetime import datetime, timezone


def artifact_map(title: str, created: str) -> str:
    return f"""============================================================
{title.upper().replace(' ', '-')}.cavecode.txt
{title} — CaveCode Artifact Map
============================================================

STATUS:
DRAFT

CREATED:
{created}

============================================================
🪨 BLOCK 1 — IDENTITY
============================================================

NAME:
{title}

PURPOSE:
Describe what this artifact does.

PROTECTED CONTRACT:
Record identity, invariants, or rules that should not be casually changed.

============================================================
🖍️ BLOCK 2 — CRAYON / HUMAN EDIT ZONE
============================================================

EXAMPLE_SETTING: 10
EXAMPLE_LABEL: "Change me"

============================================================
🎮 BLOCK 3 — BEHAVIOR
============================================================

1. Describe what happens on start.
2. Describe inputs and processing.
3. Describe outputs and failure behavior.

============================================================
🌐 BLOCK 4 — PUBLIC-SAFE MATERIAL
============================================================

PUBLIC_DESCRIPTION:
Plain-language description approved for public use.

============================================================
🔧 BLOCK 5 — OPEN WORK
============================================================

- Record extensions, experiments, and unresolved work here.

============================================================
🖍️ BLOCK 6 — HUMAN NOTES
============================================================

- Preserve context the next human or AI will need.
"""


def project_map(title: str, created: str) -> str:
    return f"""============================================================
{title.upper().replace(' ', '-')}.cavecode.txt
{title} — Master Project Map
CaveCode Read-First Project File
============================================================

STATUS:
ACTIVE

PROJECT STATE:
Describe the current implemented, tested, committed, and deployed state.

CREATED:
{created}

PURPOSE OF THIS FILE:
This is the repository's read-first source for current project understanding
and current human decisions.

AUTHORITY RULE:
This map governs current understanding. Reconcile conflicts explicitly and
update this map in the same commit as meaningful project-state changes.

============================================================
🪨 BLOCK 1 — PROJECT IDENTITY
============================================================

NAME:
{title}

PURPOSE:
Describe the problem and intended outcome.

============================================================
🪨 BLOCK 2 — AUTHORITY / PROTECTED CONTRACTS
============================================================

- List ratified decisions, contracts, and authoritative files.

============================================================
🎮 BLOCK 3 — CURRENT SYSTEM / RUNTIME STATE
============================================================

IMPLEMENTED:
-

TESTED:
-

DEPLOYED:
-

============================================================
🔧 BLOCK 4 — KNOWN PROBLEMS / OPEN QUESTIONS
============================================================

-

============================================================
🖍️ BLOCK 5 — CURRENT WORK / RESUME HERE
============================================================

CURRENTLY WORKING:
-

NEXT ACTION:
-

DO NOT YET:
-

============================================================
🖍️ BLOCK 6 — HANDOFF SNAPSHOT
============================================================

DATE:
{created[:10]}

WHAT CHANGED?
-

WHAT CURRENTLY WORKS?
-

WHAT IS CURRENTLY BROKEN?
-

WHAT SHOULD HAPPEN NEXT?
-
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", nargs="?", default="New CaveCode Project")
    parser.add_argument(
        "--profile",
        choices=("artifact", "project"),
        default="artifact",
        help="artifact map (default) or repository master project map",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    created = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    output = project_map(args.title, created) if args.profile == "project" else artifact_map(args.title, created)
    print(output, end="")


if __name__ == "__main__":
    main()
