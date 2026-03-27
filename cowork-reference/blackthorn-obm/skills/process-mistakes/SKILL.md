---
name: process-mistakes
description: >
  Log, track, and surface process mistakes and lessons learned across the user's
  Cowork workflows. Trigger when: a workflow fails and the correct approach
  needs to be captured ("log this mistake", "remember this error", "don't do
  this again", "add to lessons learned", "that was wrong — note it"); before
  starting any workflow in a known error-prone area (skill updates, Salesforce
  config, COM records, packaging); or when Jared asks to review past mistakes,
  see the lessons log, or audit what's been flagged. Also invoke proactively
  when another skill hits an unexpected failure — capture it before moving on.
---

# Process Mistakes Skill

This skill maintains a persistent log of process mistakes and corrected approaches across all of the user's Cowork workflows. The goal is simple: if something goes wrong once, it should never go wrong the same way again.

The log lives at:
```
/sessions/.../mnt/Cowork-OS/PROCESS-LESSONS.md
```

Discover the path dynamically:
```bash
find /sessions -path "*/mnt/Cowork-OS/PROCESS-LESSONS.md" 2>/dev/null | head -1
# If not found, the file needs to be created at:
find /sessions -path "*/mnt/Cowork-OS" -maxdepth 4 -type d 2>/dev/null | head -1
```

---

## Mode 1 — Log a Mistake

When triggered by a workflow error or an explicit "log this" instruction:

1. **Identify the mistake clearly.** What was attempted? What went wrong? Be specific — vague entries are useless later.
2. **Capture the correct approach.** What should be done instead? Include the exact steps, commands, or decision logic that prevents recurrence.
3. **Tag affected workflows.** Which skills, folders, or task types does this apply to? This is how the lesson gets surfaced later.
4. **Write the entry** to `PROCESS-LESSONS.md` using the format below.
5. **Confirm** to Jared that it's been logged.

### Entry Format

```markdown
### [Short title of the mistake]
**Date logged:** YYYY-MM-DD
**Affected workflows:** [comma-separated list of skills or task types]
**What went wrong:** [1-2 sentences describing the failure mode]
**Correct approach:** [exact steps or decision rule to follow instead]
```

If `PROCESS-LESSONS.md` doesn't exist yet, create it with this header:
```markdown
# Process Lessons

Persistent log of workflow mistakes and corrected approaches. Read this before starting any workflow in a known error-prone area.

---
```

Then append the new entry.

---

## Mode 2 — Pre-Flight Consult

Before starting any workflow that touches known error-prone areas, read `PROCESS-LESSONS.md` and surface any relevant lessons.

**Always consult before:**
- Updating or patching any skill
- Making changes to MEMORY.md or CLAUDE.md
- Working with Salesforce COM records
- Packaging or deploying skill files
- Any task where a previous lesson is tagged as applying

**How to surface it:**
- If a relevant lesson exists, quote it briefly before starting: "Before we proceed — there's a logged lesson on this: [title]. [Correct approach in one sentence]. Proceeding with that in mind."
- If nothing relevant exists, proceed without comment.
- Don't surface irrelevant lessons just to show you checked.

---

## Mode 3 — Review Log

When Jared asks to see past mistakes, review all lessons, or audit what's been flagged:

1. Read `PROCESS-LESSONS.md` in full.
2. Present a clean summary: titles, dates, affected workflows, and correct approach for each.
3. Offer to clean up outdated entries if anything looks stale or no longer relevant.

---

## Mode 4 — Update or Remove an Entry

If Jared says a logged lesson is no longer accurate, outdated, or was logged incorrectly:

1. Read the current entry.
2. Confirm the change with Jared before editing.
3. Edit or remove the entry in `PROCESS-LESSONS.md`.
4. Confirm completion.

---

## Integration with Other Skills

Any skill that operates in an error-prone area should include a note to check `PROCESS-LESSONS.md` before starting. The standard pattern to add to those skills:

```
Before starting, check PROCESS-LESSONS.md for any lessons tagged as applying to this workflow.
```

Skills that benefit most from this pattern: `skill-creator`, `com-update`, `flagged-onboarding-sync`, `day-prep-recap`.

---

## What NOT to Log

- One-off user errors that aren't systemic (typos, paste mistakes, etc.)
- Things already covered in MEMORY.md under "Known Constraints & Workflows" — don't duplicate
- Speculative "this might go wrong" entries — log after failure, not before

If something is critical enough to need always-on awareness (not just pre-flight consult), add it to MEMORY.md's "Known Constraints & Workflows" section instead of (or in addition to) the lessons log.

---

## PM Handoff — SKILL RESULT

When running under PM orchestration, complete the log action and return:

```
## SKILL RESULT: process-mistakes
Timestamp: [ISO 8601]
Customer: None
Actions taken: [entry written to PROCESS-LESSONS.md / pre-flight surfaced / log reviewed]
Findings:
  Mode 1 (Log): Wrote entry "[title]" to PROCESS-LESSONS.md.
  Mode 2 (Pre-flight): [Relevant lesson found: "[title]" — summarized for PM context]
    [Or: No relevant lessons for this workflow.]
  Mode 3 (Review): [N] lessons on file. Summary included below if PM needs context.
Confidence: High
Gaps/failures: [file not found and created; entry already exists]
Suggested next: None
Flags for Jared: None
```
