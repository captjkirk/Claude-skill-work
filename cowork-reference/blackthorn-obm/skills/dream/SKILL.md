---
name: dream
description: >
  Memory consolidation and process evolution skill. Reviews session transcripts, routes facts to
  the right MEMORY.md or customer dossier, prunes stale entries, and runs an EVO pass that
  identifies recurring mistakes or workflow gaps and drafts skill improvement patches for review.
  Run nightly at midnight or on demand. Invoke on: "dream", "consolidate memory", "review
  session", "clean up memory", "update my memories", "run the dream function". Also invoke
  proactively at the end of any long session where significant new information surfaced.
---

# Dream — Memory Consolidation

Reviews today's session transcripts and updates memory files at the correct folder level. Named after the theory that sleep consolidates memories — distilling signal from noise and routing it to the right place.

---

## Step 1 — Orient

Read the current state of memory before touching anything:

1. Read `/Cowork-OS/MEMORY.md` (root) — note what's already on file
2. Wait to read subfolder MEMORY.md files until Step 2 reveals which subfolders were active today

---

## Step 2 — Gather Signal

List today's sessions and read their transcripts:

- Call `mcp__session_info__list_sessions` to get sessions from today
- For each session, call `mcp__session_info__read_transcript` to read the full transcript
- If no sessions exist for today, say so and exit cleanly

From the transcripts, extract anything in these categories:

- **Team / org facts** — new people, role changes, reporting structure
- **Workflow preferences** — how Jared corrected something, how he wants things done differently
- **Process insights** — anything that changes how a recurring workflow should work
- **Customer facts** — anything tied to a named customer account (status, contacts, blockers, milestones)
- **Constraints** — tools that don't work, known limits, things to avoid
- **Subfolder-specific context** — facts that belong in a specific subfolder's MEMORY.md (e.g., LMO nav notes, email conventions, onboarding process changes)
- **Feature explanations** — any moment where Jared explains how a Blackthorn feature works, describes his personal approach to a topic, or states a standard caveat/disclaimer he uses with customers (e.g., "I always tell them...", "the way I explain it is...", "I'm not an expert on X but...")

Skip: one-off conversational filler, things already captured in memory or personal preferences, anything that's only relevant to a single session with no future value.

---

## Step 2.5 — Feature Explanation Extraction

After gathering signal from session transcripts, run a dedicated pass to extract feature explanations and personal approach notes for `reference/feature-explanations.md`.

### What to look for

- Jared explaining how a Blackthorn feature works in plain English or technical terms
- Jared describing his standard framing for a topic (e.g., "the way I explain it to customers is...")
- Jared stating a personal caveat or disclaimer he uses regularly (e.g., "I'm not the expert on X but...")
- Any post-meeting-sweep output or Fathom summary that references a feature being explained on a call

### When a call summary mentions a feature explanation

If a Fathom summary (from post-meeting-sweep or the meeting cache) indicates that Jared explained a feature on a call — but the summary is too brief to capture the exact language — pull the full transcript:

1. Check `customers/<name>/meetings/` first — if the call is already cached, read it directly
2. If not cached, call `mcp__fathom__fathom_get_transcript` for that meeting
3. Scan the transcript for the specific segment where the feature was explained
4. Extract Jared's exact language, clean it up minimally (fix transcription artifacts, preserve his voice)

### How to write to `reference/feature-explanations.md`

Read the file first. Then add or update the appropriate section:

```markdown
### [Feature Name]

**Plain English:** [Jared's non-technical explanation, in his voice]

**Technical:** [More detailed version for admins/developers, if captured]

**Jared's approach:** [Any caveats, framing, or go-to language he uses when introducing this topic]

**Source:** [Call date + Fathom link if available, or "Session transcript YYYY-MM-DD"]
```

- If an entry already exists for that feature, append the new version below the existing one with a new source date — do not overwrite, as evolution of the explanation over time is useful
- If only a plain-English or only a technical version was captured, write what you have and leave the other field blank
- Personal approach notes (disclaimers, caveats) go in the **Personal Approach Notes** section at the bottom, not under a specific feature — unless they're feature-specific

### Routing rule

Feature explanations go to `reference/feature-explanations.md` only. Do not also write them to MEMORY.md or customer dossiers.

---

## Step 3 — Package Proposed Changes

Route each extracted fact to its target destination — but do NOT write yet. All writes
are executed by PM after receiving the SKILL RESULT. Package each proposed change as:

| Fact type | Target destination |
|-----------|-------------|
| Customer-specific (tied to a named account) | `customers/<name>/<name>.md` |
| Subfolder-specific (LMO, emails, onboarding-process, personal-growth, productivity) | `<subfolder>/MEMORY.md` |
| General (team, workflow, preferences, constraints) | `/Cowork-OS/MEMORY.md` (root) |
| Feature explanations and personal approach notes | `reference/feature-explanations.md` |

**Confident additions** — include in SKILL RESULT Findings as ready-to-write entries.
Each entry must include: target file path, section to write under, and full entry text.

**Ambiguous items** — do not include as writes. Instead, flag them in the SKILL RESULT
as TASKS.md additions:
```
[ ] [DREAM] Review memory item: "[brief description]" — unclear if/where to save.
```

PM will create any missing MEMORY.md files before writing.

---

## Step 4 — Identify Entries to Prune

Scan existing MEMORY.md entries against today's transcripts:

- **Directly contradicted** → flag in SKILL RESULT as a proposed update (include target file, entry text to remove, replacement text)
- **Clearly outdated** (e.g., a customer status that changed, a process that's been retired) → flag in SKILL RESULT as a proposed deletion
- **Uncertain** → leave it alone; never prune what you're not confident about

Do NOT edit MEMORY.md files directly. Package all proposed changes for PM to execute.

---

## Step 4.5 — MEMORY.md Size Check

After the prune pass, count the lines in `/Cowork-OS/MEMORY.md`:

```bash
wc -l /sessions/*/mnt/Cowork-OS/MEMORY.md
```

- **175 lines or fewer** → no action needed
- **176–199 lines** → flag in SKILL RESULT: "MEMORY.md is approaching the 200-line truncation limit ([N] lines). Recommend reviewing for consolidation candidates." Include suggested sections to audit (e.g., entries that are time-bound, superseded, or duplicated between MEMORY.md and customer dossiers).
- **200+ lines** → treat as urgent. Flag to Jared as a Tier 2 item: "MEMORY.md is at [N] lines and may be silently truncating. Review needed before next session."

Do not auto-prune to resolve the size — only flag candidates and let Jared decide what to remove.

---

## Step 5 — EVO Pass (Process Evolution)

After memory is consolidated, run a pattern-recognition sweep to find workflow gaps and skill improvement opportunities. This is the equivalent of John Natoli's EVO agent — it reviews what happened, finds what's broken or suboptimal, and drafts fixes.

### 5a — Scan for Patterns

Review PROCESS-LESSONS.md, today's transcripts, and the current state of all skill files for:

| Signal | What it means |
|---|---|
| Same mistake logged 2+ times in PROCESS-LESSONS.md | The skill that causes this mistake needs a patch |
| User corrected Claude mid-task on the same point 2+ times across sessions | A skill is missing a rule or has a wrong default |
| A skill was manually invoked that should have auto-triggered | The triggering skill's handoff logic is incomplete |
| A workflow required more back-and-forth than it should | A skill is under-specified or missing a decision step |
| A user said "I always have to remind you to..." | A persistent rule is missing from the relevant skill |
| Skill A says one thing, Skill B says the opposite about the same scenario | Cross-skill contradiction — both may need patching; flag both |
| A skill consistently returns Low or Medium confidence on the same topic | The skill lacks context, decision rules, or source guidance for that topic |
| A skill's routing table or trigger criteria don't match the PM Routing Logic | Drift between PM and the skill — one of them is wrong |
| A skill references another skill by a wrong or outdated name | Stale internal cross-reference — update the reference |
| A skill's SKILL RESULT format is missing a field PM relies on | Schema drift — align the skill's output format to what PM expects |
| A skill has no PM Handoff / SKILL RESULT block | The skill cannot return results to PM — must be added |
| An EVO proposal from a previous session was never applied | Flag it again; the gap persists |
| A workflow completed but a natural follow-on skill was never triggered | Either PM's routing table is missing a row, or the skill's "Suggested next" is empty |
| PM had to make a judgment call not covered by any routing rule | A decision gap — log the call PM made as a candidate rule to add to PM routing |

### 5b — Draft Improvement Proposals

For each pattern identified, draft a proposed skill patch:

```
## EVO Proposal — [Skill Name]

**Pattern detected:** [What keeps going wrong, with examples from transcripts/lessons]
**Root cause:** [Which part of the skill is missing or wrong]
**Proposed change:**
[Exact text to add, remove, or modify — written as a diff: what the current text says vs. what it should say]
**Confidence:** High / Medium / Low
**Risk:** [Could this change break anything? What to watch for after applying?]
```

- **High confidence, low risk** → include full proposal text in SKILL RESULT for PM to write to `outputs/evo-proposals/YYYY-MM-DD-[skill-name].md`
- **Medium/low confidence or higher risk** → include a summary (not full text) in SKILL RESULT for PM to write to `outputs/evo-proposals/YYYY-MM-DD-[skill-name].md`
- **All proposals regardless of confidence** → ALSO add a TASKS.md entry: `[ ] [EVO] Review skill improvement proposal: [skill name] — [one-line description] — see outputs/evo-proposals/YYYY-MM-DD-[skill-name].md`

The TASKS.md entry ensures every proposal surfaces in the next morning's brief. PM creates the TASKS.md entry in the same write pass as the evo-proposals file.

- Never apply patches directly to skills. EVO proposes; the human decides.
- Do NOT write EVO proposal files or TASKS.md entries directly. Include them in the SKILL RESULT for PM to execute.

### 5c — EVO Log Entry

Add an EVO section to the dream log (Step 6):

```
## EVO Pass
- Proposals written: [skill names]
- Flagged for review: [skill names + reason]
- No patterns detected: [if nothing found]
```

---

## Step 6 — Return SKILL RESULT to PM

Dream does not write anything directly. Package all findings and return to PM.
PM receives this SKILL RESULT, executes all Tier 1 writes, and presents a summary to Jared.

```
## SKILL RESULT: dream
Timestamp: [ISO 8601]
Customer: None
Actions taken: Read [N] session transcripts. Extracted [N] memory candidates.
  Ran EVO pass — [N] proposals identified.

Findings:

  === PROPOSED WRITES ===

  Root MEMORY.md (`/Cowork-OS/MEMORY.md`):
  - ADD under [section]: [full entry text]
  - UPDATE: replace "[old text]" with "[new text]"
  - PRUNE: remove "[entry text]"
  - (nothing to write)

  Customer Dossiers:
  - customers/<name>/<name>.md: ADD to interaction log — [entry text]
  - (nothing to write)

  Subfolder MEMORY.md (`<subfolder>/MEMORY.md`):
  - ADD under [section]: [full entry text]
  - (nothing to write)

  Feature Explanations (`reference/feature-explanations.md`):
  - ADD under [Feature Name]: [full block text]
  - (nothing to write)

  === EVO PROPOSALS ===
  - outputs/evo-proposals/[YYYY-MM-DD-skill-name].md: [full proposal text]
  - (none)

  === TASKS.md ADDITIONS ===
  - [ ] [DREAM] Review memory item: "[description]"
  - [ ] [EVO] Review skill improvement proposal for [skill name]
  - (none)

  === DREAM LOG (for PM to write to Daily Prep/YYYY-MM-DD-dream-log.md) ===
  [Full dream log content — PM writes this file verbatim]

Confidence: High
Gaps/failures: [sessions that couldn't be read; customers without dossiers; ambiguous items]
Suggested next: None — PM executes all writes from this SKILL RESULT
Flags for Jared: None (all dream work is Tier 1)
```

**PM execution protocol after receiving this SKILL RESULT:**
1. Execute all PROPOSED WRITES — write directly to each target file
2. Write EVO PROPOSAL files to `outputs/evo-proposals/`
3. Add TASKS.md ADDITIONS to `Productivity/TASKS.md`
4. Write the DREAM LOG file to `Daily Prep/YYYY-MM-DD-dream-log.md`
5. Append to ACTIVITY-LOG.md
6. Surface brief summary to Jared: "Dream complete. [N] memory updates, [N] dossier updates, [N] EVO proposals. Log at Daily Prep/[date]-dream-log.md."

---

## Edge Cases

**Multiple sessions today** — process all of them; deduplicate before writing so the same fact isn't logged twice.

**Customer with no dossier** — if a customer fact surfaces for an account that has no folder in `customers/`, add it to root MEMORY.md with a note: "Consider creating a dossier for [name]."

**Scheduled run (midnight)** — behave identically to an on-demand run. No confirmation needed, just execute and report.

---

## PM Handoff — SKILL RESULT

When running under PM orchestration, complete all memory consolidation and EVO pass work,
then return a SKILL RESULT block. Dream is typically the last skill to run in a session.

```
## SKILL RESULT: dream
Timestamp: [ISO 8601]
Customer: None (session-level consolidation)
Actions taken: [sessions reviewed; facts routed; memory updated; dossiers updated;
  EVO pass run; any patches drafted]
Findings: [summary of what was added, updated, pruned; any EVO proposals drafted]
Confidence: High
Gaps/failures: [any sessions that couldn't be read; files that couldn't be written]
Suggested next: None — memory consolidation complete.
Flags for Jared: [EVO proposals are Tier 2 — always flag and present for human review
  before any skill patch is applied. Include the proposal summary in the flag.
  Skill patches require human install via Cowork "Copy to your skills".]
```
