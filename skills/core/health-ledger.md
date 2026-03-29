# PM Health Ledger

PM logs quality observations about skill output to an append-only ledger.
Auto-research reads this ledger to inform evaluation criteria and priorities.

---

## Location

`outputs/health-ledger/observations.jsonl`

One JSON object per line. Append-only — never edited in place.

---

## Observation Format

```json
{
  "id": "HL-YYYY-MM-DD-NNN",
  "timestamp": "ISO 8601",
  "skill": "skill-name",
  "type": "honesty-violation | gap | regression | integration-failure | bloat | miscalibration | missing-resource",
  "severity": "critical | high | medium | low",
  "chain_context": "skill-a → skill-b → skill-c",
  "observation": "Human-readable description of what went wrong",
  "evidence": "Specific data — quotes, field values, timestamps",
  "recommendation": "What PM thinks would fix this",
  "resource_type": "script | reference | template | split | constraint | none",
  "consumed_by_auto_research": false,
  "resolved": false,
  "resolution_note": null
}
```

---

## Observation Types

| Type | Meaning | Example |
|------|---------|---------|
| `honesty-violation` | Skill violated honesty protocol | Email draft fabricated a meeting date |
| `gap` | Skill missing a resource that would improve output | No validation script for dates |
| `regression` | Skill performed worse than previously observed | Dossier leaving 3 fields blank that it used to populate |
| `integration-failure` | Handoff between skills broke | Fathom output missing meeting time, com-update couldn't match |
| `bloat` | Output unnecessarily verbose or irrelevant | Day-prep including full dossier instead of summary |
| `miscalibration` | Confidence doesn't match evidence | High confidence with 50% INFERRED fields |
| `missing-resource` | Specific resource would improve quality | blackthorn-support needs updated product docs |

## Severity

| Level | Criteria |
|-------|----------|
| `critical` | Affects customer-facing output. Wrong info could reach customer/colleague. |
| `high` | Affects data quality. Wrong data in dossier/COM/MEMORY propagates. |
| `medium` | Affects efficiency. Output correct but suboptimal. |
| `low` | Minor formatting/ordering/style. No data impact. |

---

## When PM Writes

### After Every Skill Chain
Scan all SKILL RESULTs for:
- Missing Source labels → `honesty-violation`
- Confidence/evidence mismatch → `miscalibration`
- Fields PM had to fabricate for downstream routing → `gap`
- SKILL RESULT missing fields downstream skills needed → `integration-failure`

### On Low Confidence for Critical Data
Customer-facing skill returns Low on data affecting interactions → log and
check: one-off (bad input) or pattern (skill needs improvement)?

### On Noticing Missing Resources
Skill output would improve with:
- Validation script → `resource_type: "script"`
- Reference document → `resource_type: "reference"`
- Output template → `resource_type: "template"`
- Skill split → `resource_type: "split"`

### On Auto-Research Persistent Failures
Skill fails same criterion across 3+ runs → auto-research writes observation.
PM surfaces as Tier 2 recommendation.

---

## How Auto-Research Reads the Ledger

### During Phase 1 (Analyze)

Filter `observations.jsonl` for:
- `skill` matches target
- `consumed_by_auto_research` is `false`

For each unconsumed observation:

| Type | Auto-Research Action |
|------|---------------------|
| `honesty-violation` | Generate criterion targeting this honesty failure. Generate test case reproducing the scenario. |
| `gap` / `missing-resource` | Generate test case exposing the gap. Criterion testing whether output improves with recommended resource. |
| `regression` | Generate test case matching regression scenario. Compare to previous passing behavior. |
| `integration-failure` | Generate cross-skill test case for the broken handoff. |
| `miscalibration` | Add Confidence Calibration criterion. Test cases with varying evidence quality. |

Mark processed observations: `consumed_by_auto_research: true`

### After Improvement Loop

- Criterion now passes → mark `resolved: true` with `resolution_note`
- Criterion still fails → leave unresolved. PM escalates.

### Writing New Observations

Auto-research writes back when it discovers:
- Persistent failures (3+ iterations) → `type: "regression"`
- Resource recommendations → `type: "missing-resource"`
- Bloat detection (>50% growth) → `type: "bloat"`

---

## Health Summary

PM produces on demand or at session end:

```
=== SKILL HEALTH SUMMARY ===
Period: Last 7 days
Total observations: 12 | Unresolved: 5 | Resolved: 7

=== TOP ISSUES ===
| Skill | Unresolved | Severity | Top Issue |
|-------|-----------|----------|-----------|
| email-templates | 2 | high | Fabricating dates |
| com-update | 1 | high | Missing field validation |
| blackthorn-support | 1 | medium | Outdated product docs |

=== RESOURCE RECOMMENDATIONS ===
| Skill | Type | Recommendation | Impact |
|-------|------|----------------|--------|
| email-templates | script | validate-dates.py | Catch date fabrication |
| com-update | script | validate-com-fields.py | Verify against dossier |
| blackthorn-support | reference | Feb 2026 PDFs | Improve answer accuracy |
```

Available to: user (on request), auto-research (as input), dream's EVO pass.
