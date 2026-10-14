---
name: package-submission
description: Use when the student wants to verify, package, and summarize their work — audits attribution watermarks, prompt history, and generates SUBMISSION_REPORT.md (supports ZIP, LMS upload, or Git).
---

# Package Submission Skill

This skill assists students in verifying their project's academic integrity artifacts and generating a submission report for instructors.

## Step 1: Run Verification Scan

Execute the verification script to analyze the workspace:

```bash
python3 .bob/skills/package-submission/verify_submission.py
```

Use `execute_command` to run this command and capture the JSON report.

## Step 2: Analyze Verification Results

Inspect the output from Step 1:
1. **Student Metadata**: Ensure `STUDENT_INFO.json` is filled with the student's name, ID, and course/project details.
2. **File Watermarks**: Check `missing_watermark_files`. If any source files are missing the `[IBM Bob Academic Attribution]` header, automatically apply the appropriate header format defined in `.bob/rules/academic-attribution.md`.
3. **Prompt & Chat History**: Verify `prompt_history.prompt_count` to ensure student prompts and interactions are logged in `PROMPT_HISTORY.md`.
4. **Audit Trail**: Ensure `AI_AUDIT_TRAIL.md` exists and contains entries covering major milestones and test results.

## Step 3: Generate `SUBMISSION_REPORT.md`

Generate a standardized submission report in the project root summarizing:
- Student Identification (Name, ID, Course/Project, Date)
- Summary of Developed Features and Files
- Watermark Audit (100% compliance breakdown)
- Summary of Prompt Interactions Recorded in `PROMPT_HISTORY.md`
- Summary of Milestone Entries from `AI_AUDIT_TRAIL.md`

Write this file to `SUBMISSION_REPORT.md`.

## Step 4: Submission Delivery Options

Provide the student with instructions according to their instructor's submission method:
* **ZIP Archive / LMS Upload**: Compress the project folder (including `.bob/`, `docs/`, `PROMPT_HISTORY.md`, `AI_AUDIT_TRAIL.md`, `SUBMISSION_REPORT.md`, and source files) and upload to the course portal.
* **Direct Folder Submission**: Submit the project directory directly.
* **Git Repository (if preferred)**: Commit and push changes (`git add . && git commit -m "Submission package"`).
