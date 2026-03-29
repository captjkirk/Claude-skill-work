# Honesty Protocol

Every skill in this workspace must follow these three rules. No exceptions.

---

## Rule 1: Force Blank

When a value is ambiguous, missing, or unclear — leave it **BLANK**.

Do not guess. Do not fill with the most likely answer. Do not extrapolate
from insufficient data.

For every blank field, add an entry to a Flags table:

```
| Field | Reason Left Blank |
|-------|-------------------|
| Renewal Date | Dossier shows contract signed but no term length recorded |
| Primary Contact | Two contacts listed — unclear which is current primary |
```

**Force blank when:**
- Source data is ambiguous (two values conflict)
- Source data is missing entirely
- Source data is stale (>90 days, time-sensitive field)
- Answer requires a source the skill cannot access

**Do NOT force blank when:**
- Value is clearly stated in a reliable source
- Value can be legitimately inferred with evidence (see Rule 3)

---

## Rule 2: Penalize Guessing

> A wrong answer is 3x worse than a blank. When in doubt, leave it blank.

This applies to:
- Customer data (names, dates, contacts, deal stages)
- Meeting outcomes (action items, commitments, next steps)
- Product answers (features, configurations, pricing)
- Salesforce/COM field recommendations
- Email content (dates, commitments, attendees)
- Any field visible to customers or colleagues

---

## Rule 3: Show the Source

Label every value as one of:

**EXTRACTED** — Directly stated in source material. You can point to the
specific document, email, dossier entry, transcript, or data field.

**INFERRED** — Derived, calculated, or interpreted from evidence. Not
directly stated but follows logically from available data. Must include
a one-sentence evidence trail.

### Example

| Field | Value | Source | Evidence |
|-------|-------|--------|----------|
| Account Owner | Sarah Chen | EXTRACTED | customer-dossier: Primary Contact |
| Contract Start | Jan 15, 2025 | EXTRACTED | Dossier: Signed Contract section |
| Renewal Date | Jan 15, 2027 | INFERRED | Calculated: 24mo from Jan 15, 2025 |
| Expansion Likelihood | — BLANK | — | See Flags |

| Field | Reason Left Blank |
|-------|-------------------|
| Expansion Likelihood | No meeting data in 45 days. Insufficient evidence. |

---

## Inference Is NOT Banned

This workspace serves a customer-facing CSM. Legitimate inferences backed
by evidence are valuable.

**Good inference (keep):**
- "Renewal Jan 2027 — INFERRED from 24-month term starting Jan 2025"
- "Likely using Events + Payments — INFERRED from onboarding notes"
- "Follow-up by Friday — INFERRED from Sarah saying 'before end of week' in transcript"

**Bad inference (should be BLANK):**
- "Customer is happy with the product" — no evidence cited
- "Renewal is low risk" — no recent data to support
- "They'll probably expand to Messaging" — speculation without signals

**The rule: Infer when you have evidence. Flag it as inferred. Show the
evidence. Never guess silently.**

---

## Verification Before Completion

Before presenting any output, every skill must verify:

1. All non-blank fields have Source labels (EXTRACTED or INFERRED)?
2. All INFERRED fields have evidence trails?
3. All BLANK fields have Flags table entries?
4. No red-flag words ("should," "probably," "typically") without a source?
5. Confidence level matches evidence quality?

If any check fails — fix before presenting. Do not present and apologize later.

---

## Pre-Delivery Checklist

Content-producing skills verify internally before returning SKILL RESULT:

- [ ] All values labeled EXTRACTED or INFERRED
- [ ] All INFERRED values have one-sentence evidence trails
- [ ] All BLANK fields have Flags table entries
- [ ] No unsupported confident assertions
- [ ] Confidence calibrated:
  - **High** = mostly EXTRACTED, minimal blanks, recent data
  - **Medium** = mix of EXTRACTED/INFERRED, some blanks, or data >30 days
  - **Low** = mostly INFERRED or BLANK, stale data, missing key sources
- [ ] Gaps/failures field lists anything unverifiable

---

## Confidence Calibration

| Confidence | Evidence Required |
|-----------|-----------------|
| **High** | Key fields EXTRACTED from recent (<30 day) sources. Minimal INFERRED. No critical blanks. Multiple corroborating sources. |
| **Medium** | Mix of EXTRACTED and INFERRED. Some blanks on non-critical fields. Data may be 30-90 days old. Single source for some claims. |
| **Low** | Mostly INFERRED or BLANK. Data >90 days old. Key sources unavailable. Contradictions in available data. |

**Miscalibration is a violation.** High confidence on thin evidence is worse
than Low confidence on the same data — it prevents PM from deepening when
it should.

---

## Domain-Specific Application

### Customer Data (customer-dossier, com-update, email-templates)
Strictest enforcement. Every customer fact needs a source. Never fabricate
meeting outcomes, commitments, or next steps.

### Meeting Research (fathom, post-meeting-sweep)
- Transcript quotes = EXTRACTED (cite timestamp)
- AI-generated recap = INFERRED (cite "Fathom AI summary")
- Action items: EXTRACTED if verbatim, INFERRED if interpreted

### Product Answers (blackthorn-support)
- From product docs = EXTRACTED (cite doc/section)
- Generalized from related features = INFERRED (cite which docs)
- Not in docs = BLANK + recommend product-feedback-poster

### Content Generation (email-templates, blackthorn-brand)
- Customer details must trace to dossier (EXTRACTED)
- Meeting references must trace to Fathom/Gmail (EXTRACTED)
- Never invent dates, outcomes, or commitments not in source data

### Memory Management (dream, memory-create)
- Session extracts = EXTRACTED (cite session)
- Cross-session patterns = INFERRED (cite sessions)
- Pruning must cite why entry is stale

---

## How Skills Reference This File

Add to every SKILL.md:

```markdown
## Honesty Protocol
Follow `skills/core/honesty-protocol.md` for all outputs.
Label all values EXTRACTED or INFERRED with evidence.
Leave ambiguous/missing values BLANK with Flags entry.
A wrong answer is 3x worse than a blank.
```

For structured tables: add Source and Evidence columns.
For prose output: add a Source Summary section at the end.
