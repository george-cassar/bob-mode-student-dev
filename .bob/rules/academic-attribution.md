# Academic Code Attribution & Provenance Rules
<!-- Owner: Academic Program · Scope: workspace · Target: IBM Bob -->

These rules apply to all code generated or modified within this workspace using IBM Bob for any student course, lab, homework, or general project.

## 1. Mandatory File Watermarking

Every source code or configuration file created or updated with IBM Bob assistance MUST include the standard Academic Attribution header at the very top of the file.

### C / C++ / Java / JavaScript / TypeScript / Go / Rust / CSS / C# / Swift / Kotlin:
```c
/*
 * [IBM Bob Academic Attribution]
 * Student Name: <STUDENT_NAME> | Student ID: <STUDENT_ID>
 * Course / Project: <COURSE_OR_PROJECT>
 * Generated/Assisted with: IBM Bob
 * Timestamp: <YYYY-MM-DD HH:MM:SS>
 */
```

### Python / Bash / Shell / Ruby / YAML / R:
```python
# ========================================================
# [IBM Bob Academic Attribution]
# Student Name: <STUDENT_NAME> | Student ID: <STUDENT_ID>
# Course / Project: <COURSE_OR_PROJECT>
# Generated/Assisted with: IBM Bob
# Timestamp: <YYYY-MM-DD HH:MM:SS>
# ========================================================
```

### HTML / XML / Markdown:
```html
<!--
  [IBM Bob Academic Attribution]
  Student Name: <STUDENT_NAME> | Student ID: <STUDENT_ID>
  Course / Project: <COURSE_OR_PROJECT>
  Generated/Assisted with: IBM Bob
  Timestamp: <YYYY-MM-DD HH:MM:SS>
-->
```

*Note:* If `STUDENT_INFO.json` is present in the workspace root, extract `<STUDENT_NAME>`, `<STUDENT_ID>`, and `<COURSE_OR_PROJECT>` from it automatically.

---

## 2. Mandatory Prompt & Chat History Logging (`PROMPT_HISTORY.md`)

To verify authentic interaction with IBM Bob across all sessions, Bob MUST record a log of the student's prompts and conversational goals into `PROMPT_HISTORY.md` in the project root:

```markdown
### [<YYYY-MM-DD HH:MM:SS>] Prompt #<N>
- **Student Prompt**: "<Exact or summarized user prompt text>"
- **Topic / Category**: (e.g., Code Generation / Debugging / Refactoring / Test Design / Conceptual Explanation)
- **Bob's Actions & Response**: <Summary of actions, tools executed, or files edited>
```

---

## 3. Provenance Audit Logging (`AI_AUDIT_TRAIL.md`)

Whenever a new file is created, an existing file is substantially modified, or an architectural component is added:
1. Append an entry to `AI_AUDIT_TRAIL.md` in the project root.
2. Structure the entry using the following markdown format:

```markdown
### [<YYYY-MM-DD HH:MM:SS>] <Milestone / Task Name>
- **Objective / Prompt Intent**: <Summary of what the student requested>
- **Mode Used**: <Active Bob Mode>
- **Files Modified / Created**: `<relative/path/to/file1>`, `<relative/path/to/file2>`
- **Key Technical Rationale**: <Explanation of why this approach/algorithm was chosen>
- **Verification Performed**: <Unit test, manual run, or linter check passed>
```

---

## 4. Preservation of Integrity
- Never delete or truncate existing entries in `PROMPT_HISTORY.md` or `AI_AUDIT_TRAIL.md`.
- Never remove or overwrite student metadata headers.
