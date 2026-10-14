# Student Guide: Using IBM Bob for Coursework & Projects

This guide explains how to use IBM Bob for your programming tasks, assignments, labs, and personal projects while upholding academic integrity and verified attribution.

---

## 🛠️ Step 1: Initial Setup
1. Download or clone this workspace folder to your computer.
2. Open the folder in VS Code / IBM Bob:
   ```bash
   code .
   ```
3. Open [`STUDENT_INFO.json`](../STUDENT_INFO.json) and enter your information:
   ```json
   {
     "student_name": "Jane Doe",
     "student_id": "STU123456",
     "course_or_project": "Computer Science / Coursework",
     "academic_year": "2025-2026"
   }
   ```

---

## 💡 Step 2: Developing with IBM Bob
1. Open the IBM Bob Chat Panel (`Ctrl+Shift+B` or `Cmd+Shift+B`).
2. Select **🎓 Student Developer (`student-dev`)** in the mode dropdown (bottom left).
3. Ask questions, explore concepts, write code, and debug interactively.
   * **Automatic Watermarks**: Bob automatically adds your student attribution header to every file created or modified.
   * **Prompt History**: Your prompts and questions are automatically logged in [`PROMPT_HISTORY.md`](../PROMPT_HISTORY.md).
   * **Milestone Logging**: Major decisions and test results are logged into [`AI_AUDIT_TRAIL.md`](../AI_AUDIT_TRAIL.md).

---

## ⌨️ Step 3: Slash Commands
* `/log-activity` — Manually record a milestone, design decision, or test output.
* `/export-chat-history` — Synchronize your recent prompts to `PROMPT_HISTORY.md`.
* `/package-submission` — Verify all files and build your final summary report.

---

## 📦 Step 4: Submitting Your Work
1. In the Bob chat, run `/package-submission`.
2. Inspect the generated `SUBMISSION_REPORT.md`.
3. Submit your work using your instructor's preferred method:
   * **ZIP Archive / LMS Upload**: Compress the project folder and upload it directly.
   * **Folder Submission**: Submit the project directory directly.
   * **Git (if applicable)**: Push to your remote repository.
