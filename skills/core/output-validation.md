# Output Validation Pass

PM runs an independent validation pass on every SKILL RESULT before presenting
it to the user. The honesty protocol tells skills HOW to produce honest output.
This validation VERIFIES they actually did.

---

## Validation Levels

### Level 1: Quick Scan — Every Output

Runs on ALL SKILL RESULTs. Pattern-matching, near-instant.

- [ ] All required SKILL RESULT fields present?
- [ ] Source labels (EXTRACTED/INFERRED) on all values?
- [ ] BLANK fields have Flags entries?
- [ ] Confidence level present and valid (High/Medium/Low)?
- [ ] Red-flag words ("should," "probably," "typically," "usually," "likely")
      without a source citation?
- [ ] "Suggested next" references a real skill by correct name?
- [ ] Tier 1/2 classification present on actionable items?

**All pass →** Present output. No delay.
**Any fail →** Append validation note:
```
=== PM VALIDATION NOTE ===
[N] items flagged:
- [Field X] missing source label
- Confidence "High" but 4/8 fields INFERRED — may be miscalibrated
```

### Level 2: Fact Check — Customer-Facing Output

Runs on: email-templates, com-update, customer-dossier, blackthorn-support,
day-prep-recap, flagged-onboarding-sync, kickoff-deck.

Everything from Level 1, plus:

- [ ] Customer name matches dossier?
- [ ] Dates exist in calendar, Fathom, or dossier data?
- [ ] Commitments/action items sourced from transcript or email, not fabricated?
- [ ] Product information matches available docs?
- [ ] Contact names and roles match dossier contact list?

**Any fail →** Flag BEFORE presenting:
```
=== PM VALIDATION NOTE ===
HOLD — [N] items need verification:
- "Tuesday follow-up call" — no Tuesday meeting in calendar or Fathom
- "Sarah mentioned expanding to Messaging" — not in transcript
Recommend: Review these manually before acting on this output.
```

### Level 3: Deep Validation — High-Stakes Output

Runs when:
- Output will be sent externally (email, Slack post)
- Customer risk signals detected
- Irreversible actions recommended
- Confidence Medium or Low on customer-critical data

Everything from Level 2, plus:

- [ ] **Independent re-derivation:** For each INFERRED value, independently
      check whether the inference is reasonable given the source data.
- [ ] **Subjective claims:** For opinions/assessments/predictions — is this
      REASONABLE given the evidence? "Would a reasonable CSM draw this
      conclusion from the available data?"
- [ ] **Contradiction scan:** Does anything contradict dossier, recent
      transcripts, or MEMORY.md?
- [ ] **Completeness:** Is there relevant data the skill DIDN'T include
      but should have?

**Any fail →** Block and recommend correction:
```
=== PM VALIDATION — ACTION REQUIRED ===
[N] failures on high-stakes content:

1. CONTRADICTION: Output says "renews Jan 2027" but dossier shows
   early termination invoked Nov 2026.
   → Verify with dossier before sending.

2. INCOMPLETE: Fathom transcript (Mar 25) mentions customer frustration
   with timeline. Not reflected in email draft.
   → Address or acknowledge before sending.

3. SUBJECTIVE — UNREASONABLE: "Customer happy with progress" but last
   2 meetings flagged concerns.
   → Revise to reflect actual sentiment.
```

---

## Level Assignment

PM assigns automatically:

| Condition | Level |
|-----------|-------|
| Any SKILL RESULT | Level 1 (always) |
| Source skill is customer-facing | Level 2 |
| Output going external (Tier 2 flag present) | Level 3 |
| Customer risk signal detected in chain | Level 3 |
| Confidence Medium/Low on customer-critical data | Level 3 |
| User explicitly requests deep validation | Level 3 |

---

## Subjective Content Handling

| Content Type | Validation Approach |
|-------------|-------------------|
| **Factual claims** | Verify against source data. Must be EXTRACTED or verifiably INFERRED. |
| **Assessments** | Check REASONABLENESS. Aligns with evidence? Flag if contradicted. |
| **Predictions** | Must be INFERRED with evidence. Flag if thin or contradictory. |
| **Recommendations** | Must follow logically from findings. Flag if disconnected. |
| **Tone/voice** | Check against voice profile/brand guidelines. |

Key phrase: **"Would a reasonable CSM draw this conclusion from available data?"**

---

## Health Ledger Integration

Every validation failure → logged to health ledger:

```json
{
  "skill": "email-templates",
  "type": "honesty-violation",
  "severity": "high",
  "observation": "Level 2 validation caught fabricated date",
  "evidence": "Calendar shows no Tuesday meetings for Acme Corp",
  "recommendation": "Add date validation script"
}
```

Feeds the improvement loop:
Validation catches → Health ledger logs → Auto-research targets →
Skill improves → Validation verifies fix → Resolved.

---

## Validation Status in Output

PM always shows validation status to the user:

**Clean:**
```
=== VALIDATION: PASS ===
Level 2 (Customer-Facing) — 8/8 checks passed
```

**Flagged:**
```
=== VALIDATION: 2 FLAGS ===
Level 3 (High-Stakes — external send)
- Date "Tuesday follow-up" not verified in calendar
- Assessment "customer satisfied" contradicts Mar 25 transcript
```

---

## Performance

- Level 1: Pattern matching — instant
- Level 2: Local file cross-reference — fast
- Level 3: Deeper analysis — 5-10 seconds, only on high-stakes output

The small latency on Level 3 is worth catching errors before they reach
customers.
