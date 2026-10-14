# Technical Architecture: IBM Bob Academic Framework

This document outlines the technical design, configuration hierarchy, and rule mechanics of the IBM Bob Academic Framework.

---

## 🏗️ Architectural Overview

```
.
├── .bob/                               # Configuration & Tooling Layer
│   ├── custom_modes.yaml               # Mode Definitions (student-dev)
│   ├── rules/                          # Ambient Workspace Rules
│   │   └── academic-attribution.md     # Header Watermarking & Prompt History
│   └── skills/                         # Procedural Skills
│       ├── package-submission/         # Pre-flight Check & Packaging
│       │   ├── SKILL.md
│       │   └── verify_submission.py    # Python Integrity Scanner
│       ├── export-chat-history/        # Prompt Sync Skill
│       │   └── SKILL.md
│       └── log-activity/               # Milestone Logger Skill
│           └── SKILL.md
├── docs/                               # Documentation Layer
│   ├── index.html                      # Comprehensive HTML Visual Guide
│   ├── STUDENT_GUIDE.md                # Student Manual
│   ├── INSTRUCTOR_GUIDE.md             # Instructor Manual
│   └── ARCHITECTURE.md                 # Technical Architecture
├── STUDENT_INFO.json                   # Student Profile Metadata
├── PROMPT_HISTORY.md                   # Full Conversational Prompt Log
├── AI_AUDIT_TRAIL.md                   # Milestone & Rationale Log
└── README.md                           # Starter Entrypoint
```

---

## ⚙️ Configuration & Rule Mechanics

### 1. Custom Mode (`.bob/custom_modes.yaml`)
* **Slug**: `student-dev`
* **Role**: Socratic AI mentor for students across all courses and general programming.
* **Groups**: `read`, `edit`, `execute`, `skill`, `todo`.
* **Behavior**: Guides conceptual development, forces header injection, and maintains prompt histories.

### 2. Workspace Rule (`.bob/rules/academic-attribution.md`)
* Automatically injected by IBM Bob into the prompt context on every user turn.
* Injects language-specific comment headers and updates `PROMPT_HISTORY.md` and `AI_AUDIT_TRAIL.md`.

### 3. Verification Script (`.bob/skills/package-submission/verify_submission.py`)
* Recursively walks source files (excluding `.git`, `.bob`, `docs`, `node_modules`, `venv`).
* Verifies `[IBM Bob Academic Attribution]` regex matches in file headers.
* Parses and counts prompt and milestone entries via regex.
* Operates seamlessly with or without Git.
