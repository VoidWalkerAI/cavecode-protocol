#!/usr/bin/env python3
import sys
from datetime import datetime

def main():
    title = "New CaveCode Card"
    if len(sys.argv) > 1:
        title = sys.argv[1]

    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")

    template = f"""\
========================================
🪨 CAVECODE CARD — BLANK SCAFFOLD (v1.0)
========================================

Title: {title}
Created: {now}
Source: scaffolded by CaveCode tools.

========================================
🧱 BLOCK 1 — SHELL
========================================
Short Description:
    (What is this thing?)

Goal:
    🌐 (What should the player or user accomplish?)

========================================
🎮 BLOCK 2 — BEHAVIOR SUMMARY
========================================
On Start:
    - (What happens when this begins?)

On Input:
    - (What happens when the user presses / taps / clicks?)

On Update:
    - (What changes over time?)

========================================
✏️ BLOCK 3 — TUNING KNOBS
========================================
# Safe values for humans to tweak:

SPEED_BASE:       6.0
SPEED_INCREMENT:  0.4
MAX_LIVES:        3

========================================
🌐 BLOCK 4 — PUBLIC TEXT
========================================
TITLE_TEXT:       "{title}"
START_MESSAGE:    "Tap to begin."
GAME_OVER_TEXT:   "Game over. Try again."

========================================
📝 BLOCK 5 — HUMAN NOTES
========================================
# Use this space to keep notes, ideas, and plans.
# This file is for humans first, machines second.
"""

    sys.stdout.write(template)

if __name__ == "__main__":
    main()
