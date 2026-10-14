---
name: export-chat-history
description: Use when exporting, syncing, or formatting the current session's prompt history and chat interactions into PROMPT_HISTORY.md.
---

# Export Chat History Skill

This skill synchronizes the student's prompts and conversation history into `PROMPT_HISTORY.md` to ensure full transparency for assignment submission.

## Step 1: Review Current Conversation Session

Review the prompts and responses exchanged during the current session:
- Identify each distinct student prompt or task instruction.
- Categorize each interaction (e.g., *Conceptual Query*, *Code Generation*, *Debugging*, *Unit Testing*, *Refactoring*).
- Summarize Bob's actions, tool calls, and files created or modified.

## Step 2: Format and Append to `PROMPT_HISTORY.md`

Append formatted entries to `PROMPT_HISTORY.md` in the project root:

```markdown
### [<YYYY-MM-DD HH:MM:SS>] Prompt #<N>
- **Student Prompt**: "<Exact user prompt>"
- **Assistance Category**: <Category>
- **Bob's Actions & Response**: <Summary of actions and file changes>
```

If `PROMPT_HISTORY.md` does not exist, initialize it with the student metadata header from `STUDENT_INFO.json` before appending.

## Step 3: Confirmation

Inform the student that the chat interaction history has been synchronized to `PROMPT_HISTORY.md` and recommend making a Git commit.
