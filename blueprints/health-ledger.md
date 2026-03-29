# PM Health Ledger — Blueprint

This is a design doc. The next Claude Code session implements the health ledger
as an addition to PM's existing skill, plus the file/schema in the live workspace.

## Sources

- [ClaudeMem](https://github.com/thedotmack/claude-mem) — Structured observation
  extraction pattern (type, concepts, narrative, evidence). Adapted from session
  memory to skill quality tracking.
- [Ruflo](https://github.com/ruflo/ruflo) — Self-learning multi-agent swarm
  pattern. The health ledger is PM's self-learning mechanism.

## What the Health Ledger Is

An append-only log where PM records observations about skill quality after every
skill chain completes. Auto-research reads this log to inform its evaluation
criteria and improvement priorities.

**Location:** `outputs/health-ledger/observations.jsonl`

One JSON object per line, append-only. Never edited in place — only appended to.

---

## Observation Schema

```json
{
  "id": "HL-2026-03-29-001",
  "timestamp": "2026-03-29T14:30:00Z",
  "skill": "email-templates",
  "type": "honesty-violation",
  "severity": "high",
  "chain_context": "post-meeting-sweep → fathom → email-templates",
  "observation": "Email draft included 'Tuesday follow-up call' — no Tuesday meeting exists in calendar or Fathom data",
  "evidence": "SKILL RESULT Findings section, paragraph 3: 'I've drafted a follow-up referencing your Tuesday call with the team.' Calendar shows no Tuesday meetings for this customer.",
  "recommendation": "Add validation script checking dates/meetings against calendar and Fathom data before presenting email drafts",
  "resource_type": "script",
  "consumed_by_auto_research": false,
  "resolved": false,
  "resolution_note": null
}
```

### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique ID: `HL-YYYY-MM-DD-NNN` |
| `timestamp` | string | yes | ISO 8601 when observation was logged |
| `skill` | string | yes | Name of the skill that produced the concerning output |
| `type` | string | yes | See Observation Types below |
| `severity` | string | yes | `critical`, `high`, `medium`, `low` |
| `chain_context` | string | yes | The full skill chain that was running when this was observed |
| `observation` | string | yes | Human-readable description of what went wrong |
| `evidence` | string | yes | Specific data — quote from output, field values, timestamps |
| `recommendation` | string | yes | What PM thinks would fix this |
| `resource_type` | string | no | Type of resource recommended: `script`, `reference`, `template`, `split`, `constraint`, `none` |
| `consumed_by_auto_research` | boolean | yes | Has auto-research read and processed this observation? |
| `resolved` | boolean | yes | Has the issue been fixed (verified by auto-research)? |
| `resolution_note` | string | no | How it was resolved, which iteration fixed it |

### Observation Types

| Type | Meaning | Example |
|------|---------|---------|
| `honesty-violation` | Skill violated the honesty protocol — unsupported inference, missing source labels, confident guess | Email draft fabricated a meeting date |
| `gap` | Skill is missing a resource that would improve output | No validation script for date checking |
| `regression` | Skill performed worse than a previous observation on the same type of task | customer-dossier used to populate all fields, now leaving 3 blank |
| `integration-failure` | Handoff between skills broke — SKILL RESULT didn't contain what downstream skill needed | fathom output missing meeting time, com-update couldn't match to calendar |
| `bloat` | Skill output is unnecessarily verbose or includes irrelevant material | day-prep-recap including full dossier text instead of summary |
| `miscalibration` | Confidence level doesn't match evidence quality | High confidence with 50% INFERRED fields |
| `missing-resource` | PM identified that adding a specific resource (script, reference, template) would meaningfully improve quality | blackthorn-support would benefit from updated Feb 2026 product docs |

### Severity Guidelines

| Severity | Criteria |
|----------|----------|
| `critical` | Affects customer-facing output. Could cause wrong information to reach a customer or colleague. |
| `high` | Affects data quality. Wrong data in dossier, COM fields, or MEMORY.md that will propagate to future work. |
| `medium` | Affects efficiency. Skill works but misses optimization. Output is correct but suboptimal. |
| `low` | Minor formatting, ordering, or style issues. No data impact. |

---

## When PM Writes Observations

PM writes to the health ledger at these trigger points:

### 1. After Every Skill Chain Completes
PM scans all SKILL RESULTs in the chain for:
- Missing Source labels (honesty-violation)
- Confidence/evidence mismatch (miscalibration)
- Fields that PM had to fabricate or skip for downstream routing (gap)
- SKILL RESULT missing fields that downstream skills needed (integration-failure)

### 2. When a Skill Returns Low Confidence on Critical Data
If a customer-facing skill returns Low confidence on data that affects
customer interactions, PM logs it and checks: is this a one-off (bad input)
or a pattern (skill needs improvement)?

### 3. When PM Notices a Missing Resource
If PM observes that a skill's output quality would meaningfully improve with
a specific addition:
- Validation script (dates, names, field consistency)
- Reference document (product docs, brand guide, voice profile)
- Output template (structured format the skill should follow)
- Skill split (progressive disclosure for oversized skills)

PM logs the recommendation with `resource_type` populated.

### 4. When Auto-Research Reports Persistent Failures
After an auto-research sweep, if a skill has failed the same criterion across
3+ runs, auto-research writes to the health ledger with specific findings.
PM then surfaces this to the user as a Tier 2 recommendation.

---

## How Auto-Research Consumes the Health Ledger

### During Phase 1 (Analyze Target Skill)

Auto-research reads `outputs/health-ledger/observations.jsonl` and filters for:
- `skill` matches the target skill name
- `consumed_by_auto_research` is `false`

For each unconsumed observation:
1. Read the observation and recommendation
2. If `type` is `honesty-violation` → generate a criterion specifically
   targeting that honesty failure pattern
3. If `type` is `gap` or `missing-resource` → generate a test case that
   would expose the gap
4. If `type` is `regression` → include a test case matching the scenario
   where regression was observed
5. Mark the observation as `consumed_by_auto_research: true`

### After Improvement Loop Completes

If auto-research successfully improved the pass rate for criteria generated
from health ledger observations, it marks those observations as:
- `resolved: true`
- `resolution_note: "Fixed in auto-research iteration N. Pass rate for [criterion] improved from X% to Y%."`

### Writing Back to the Health Ledger

Auto-research can also write new observations to the health ledger:
- Persistent failures (same criterion fails 3+ iterations despite attempts)
- Resource recommendations discovered during analysis (e.g., "this skill would
  benefit from a reference/ folder with product docs")
- Bloat detection (skill grew >50% during improvement)

---

## PM's Health Ledger Summary

At the end of each session (or on demand), PM can produce a health summary:

```
=== SKILL HEALTH SUMMARY ===
Period: Last 7 days
Total observations: 12
Unresolved: 5
Resolved by auto-research: 4
Resolved manually: 3

=== TOP ISSUES ===
| Skill | Unresolved | Severity | Top Issue |
|-------|-----------|----------|-----------|
| email-templates | 2 | high | Fabricating dates not in source data |
| com-update | 1 | high | Missing validation for COM field values |
| blackthorn-support | 1 | medium | Outdated product docs (pre-Feb 2026) |
| fathom | 1 | medium | AI summaries presented as EXTRACTED |

=== RESOURCE RECOMMENDATIONS ===
| Skill | Resource Type | Recommendation | Impact |
|-------|-------------|----------------|--------|
| email-templates | script | Add scripts/validate-dates.py | Would catch date fabrication |
| com-update | script | Add scripts/validate-com-fields.py | Would verify field values against dossier |
| blackthorn-support | reference | Update reference/ with Feb 2026 PDFs | Would improve answer accuracy |
```

This summary is available to:
- The user (on request or in the morning brief)
- Auto-research (as input for prioritizing which skills to improve next)
- Dream's EVO pass (as quantitative evidence for qualitative patterns)

---

## Integration with the Portable Core

The health ledger connects all three layers:

```
Skills produce output
        ↓
PM scans output → writes observations to health ledger
        ↓
Auto-research reads health ledger → generates targeted criteria
        ↓
Auto-research improves skill → marks observations resolved
        ↓
PM verifies improvement → confirms resolution
        ↓
If still failing → PM surfaces to user as Tier 2
```

The honesty protocol provides the vocabulary (EXTRACTED/INFERRED/BLANK).
The health ledger provides the tracking mechanism. Auto-research provides
the improvement loop. PM ties them all together.
