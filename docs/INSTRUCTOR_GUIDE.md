# Instructor Deployment & Evaluation Manual

This guide describes how to deploy the IBM Bob student framework to any student cohort, support diverse submission formats (ZIP, LMS, Folder, or Git), and evaluate work for authentic IBM Bob usage.

---

## 🏛️ Deployment Strategy (Flexible per Cohort)

### Option 1: LMS / Portal ZIP Distribution (Simplest)
* Package this workspace as a `.zip` file and upload it to your LMS (Canvas, Blackboard, Moodle, etc.).
* Students download, unzip, and open the folder in VS Code with IBM Bob installed.
* All `.bob/` rules, modes, and skills activate automatically upon opening the folder.

### Option 2: Git Template / Classroom
* If your course uses Git, host this as a template repository on GitHub/GitLab.
* Students clone the template directly.

---

## 🔍 Verification & Integrity Evaluation

### 1. Automated Verification Script
Run the built-in verifier inside any student's submitted folder:
```bash
python3 .bob/skills/package-submission/verify_submission.py
```
**Metrics Evaluated:**
* `source_code_scan.watermarked_files`: Source files containing `[IBM Bob Academic Attribution]` headers.
* `source_code_scan.missing_watermark_files`: Source files missing watermarks (indicates external copy-pasting from other tools).
* `prompt_history.prompt_count`: Number of prompt interactions in `PROMPT_HISTORY.md`.
* `audit_trail.entry_count`: Number of logged milestones in `AI_AUDIT_TRAIL.md`.
* `git_status`: Checked if Git was used (gracefully skipped if student submitted via ZIP).

### 2. Prompt History Audit (`PROMPT_HISTORY.md`)
* Verify that student prompts demonstrate authentic problem-solving, stepwise questioning, and debugging dialogues.
* Look for alignment between the questions asked in `PROMPT_HISTORY.md` and the resulting code in the project.

### 3. Oral / Practical Code Defense (Optional)
* Ask the student to open their IBM Bob chat panel and explain their reasoning for a specific decision recorded in `AI_AUDIT_TRAIL.md`.
