# Student Lab Starter Template (IBM Bob)

Welcome! This repository is configured for your course assignments and lab exercises using **IBM Bob**. It includes preconfigured AI guidance rules, custom developer modes, prompt history logging, provenance tracking, and submission verification tools.

---

## 📖 Documentation & Guides

Comprehensive documentation is available in the [`docs/`](docs/) directory:

* 🌐 **[Visual Web Documentation (`docs/index.html`)](docs/index.html)** — Full interactive visual guide with architecture diagrams, workflow, and reference cards (open in your browser).
* 🎓 **[Student Quickstart Guide (`docs/STUDENT_GUIDE.md`)](docs/STUDENT_GUIDE.md)** — Step-by-step instructions for lab development.
* 👩‍🏫 **[Instructor Manual (`docs/INSTRUCTOR_GUIDE.md`)](docs/INSTRUCTOR_GUIDE.md)** — Deployment via GitHub Classroom and submission grading.
* 🏗️ **[Technical Architecture (`docs/ARCHITECTURE.md`)](docs/ARCHITECTURE.md)** — Overview of rules, skills, and custom modes.

---

## 🚀 Quick Start for Students

1. **Configure Profile**: Open [`STUDENT_INFO.json`](STUDENT_INFO.json) and enter your name, student ID, and course information.
2. **Open IBM Bob**: Open the Bob Chat Panel (`Ctrl+Shift+B` or `Cmd+Shift+B`).
3. **Select Mode**: Choose **🎓 Student Lab Developer (`student-dev`)** in the mode picker.
4. **Develop Your Code**: Prompt Bob for guidance. Bob will automatically add attribution headers to your files and log your prompts to [`PROMPT_HISTORY.md`](PROMPT_HISTORY.md).
5. **Package Submission**: Run `/package-submission` in the chat to verify your project and generate [`SUBMISSION_REPORT.md`](SUBMISSION_REPORT.md).

---

## 📁 Repository Structure

```files
.
├── .bob/                               # IBM Bob Configuration Root
│   ├── custom_modes.yaml               # 🎓 'student-dev' Custom Mode
│   ├── rules/                          # Automated Workspace Rules
│   │   └── academic-attribution.md     # Watermark & Prompt Logging Rules
│   └── skills/                         # Procedural Skills
│       ├── package-submission/         # /package-submission workflow
│       │   ├── SKILL.md
│       │   └── verify_submission.py    # Python automated scanner
│       ├── export-chat-history/        # /export-chat-history workflow
│       │   └── SKILL.md
│       └── log-activity/               # /log-activity workflow
│           └── SKILL.md
├── docs/                               # 📚 Documentation Folder
│   ├── index.html                      # Interactive HTML Documentation Guide
│   ├── STUDENT_GUIDE.md                # Markdown Student Guide
│   ├── INSTRUCTOR_GUIDE.md             # Markdown Instructor Deployment Guide
│   └── ARCHITECTURE.md                 # Technical Architecture Reference
├── STUDENT_INFO.json                   # Student Profile Metadata
├── PROMPT_HISTORY.md                   # Complete Prompt & Chat History Log
├── AI_AUDIT_TRAIL.md                   # Architectural Decisions & Milestones Log
└── README.md                           # Main Project Entry Point
```
