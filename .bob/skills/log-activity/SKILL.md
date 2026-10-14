---
name: log-activity
description: Use when recording a milestone, prompt intent, architectural decision, or test result into AI_AUDIT_TRAIL.md.
---

# Log Activity Skill

This skill guides recording milestones and development decisions into `AI_AUDIT_TRAIL.md` to maintain transparent provenance.

## Step 1: Gather Milestone Details

Identify or confirm the following details with the student:
- **Milestone / Task Name**: Brief title of what was accomplished.
- **Prompt Intent**: What problem was being solved or asked of IBM Bob.
- **Files Affected**: Paths of files created or modified.
- **Key Technical Rationale**: Why this approach, pattern, or algorithm was chosen.
- **Verification / Testing**: How the solution was validated (unit tests, manual testing, CLI output).

## Step 2: Append to `AI_AUDIT_TRAIL.md`

Format the entry and append it to `AI_AUDIT_TRAIL.md`:

```markdown
### [<YYYY-MM-DD HH:MM:SS>] <Milestone / Task Name>
- **Objective / Prompt Intent**: <Summary>
- **Mode Used**: 🎓 Student Lab Developer (`student-dev`)
- **Files Modified / Created**: `<file1>`, `<file2>`
- **Key Technical Rationale**: <Explanation>
- **Verification Performed**: <Test results or execution proof>
```

If `AI_AUDIT_TRAIL.md` does not exist yet, create it with the standard header from the repository template before appending.

## Step 3: Confirm with Student

Inform the student that the activity has been logged to `AI_AUDIT_TRAIL.md` and suggest committing the changes with Git.
