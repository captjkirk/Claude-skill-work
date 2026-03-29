# Honesty Protocol — Blueprint

This is a design doc. The next Claude Code session implements this as a
reference file in the live Cowork workspace (e.g., `skills/core/honesty-protocol.md`).
Every skill in the system must include or reference this protocol.

## Sources

- [The Honesty Gap](https://d-squared70.github.io/ChatGPT-and-Claude-Got-Smarter.-Not-More-Honest.)
  — Force Blank, Penalize Guessing, Show the Source (adapted from document
  extraction to all skill outputs)
- [Superpowers](https://github.com/obra/superpowers) — Verification-before-
  completion pattern: claims require evidence, no "should" or "probably"

## The Three Rules

### Rule 1: Force Blank

When a value is ambiguous, missing, or unclear — leave the field **BLANK**.

Do not guess. Do not fill with the most likely answer. Do not extrapolate
from insufficient data. Leave it blank.

For every blank field, add an entry to a **Flags table** explaining why the
value could not be determined:

```
=== FLAGS ===
| Field | Reason Left Blank |
|-------|-------------------|
| Renewal Date | Dossier shows contract signed but no term length recorded |
| Primary Contact | Two contacts listed in dossier — unclear which is current primary |
```

**When to force blank:**
- Source data is ambiguous (two values conflict)
- Source data is missing entirely
- Source data is stale (>90 days old with no refresh) and the field is time-sensitive
- The answer requires information from a source the skill cannot access

**When NOT to force blank:**
- The value is clearly stated in a reliable source
- The value can be legitimately inferred with evidence (see Rule 3)

### Rule 2: Penalize Guessing

> A wrong answer is 3x worse than a blank.

This changes the incentive structure. By default, AI optimizes for
completeness — filling every field feels like success. This rule explicitly
flips that: an empty field with an explanation is better than a filled field
that might be wrong.

**When in doubt, leave it blank.**

This rule applies to:
- Customer data fields (names, dates, contacts, deal stages)
- Meeting outcomes (action items, commitments, next steps)
- Product answers (features, configurations, pricing)
- Salesforce/COM field recommendations
- Email content (dates, commitments, attendees)
- Any field visible to customers or colleagues

### Rule 3: Show the Source

Label every value in every output as one of:

- **EXTRACTED** — Directly stated in source material. Exact match. You can
  point to the specific document, email, dossier entry, meeting transcript,
  or data field it came from.

- **INFERRED** — Derived, calculated, or interpreted from evidence. The value
  is not directly stated but follows logically from available data.

For every INFERRED value, include a **one-sentence evidence trail** explaining
what it was based on.

```
=== EXAMPLE OUTPUT ===
| Field | Value | Source | Evidence |
|-------|-------|--------|----------|
| Account Owner | Sarah Chen | EXTRACTED | customer-dossier: Primary Contact field |
| Contract Start | Jan 15, 2025 | EXTRACTED | Dossier: Signed Contract section |
| Term Length | 24 months | EXTRACTED | Dossier: Contract Terms field |
| Renewal Date | Jan 15, 2027 | INFERRED | Calculated: 24 months from Jan 15, 2025 start date |
| Expansion Likelihood | — BLANK | — | See Flags table |
```

```
=== FLAGS ===
| Field | Reason Left Blank |
|-------|-------------------|
| Expansion Likelihood | No recent meeting data. Last Fathom call was 45 days ago. Insufficient evidence to assess expansion intent. |
```

---

## Important Nuance: Inference Is NOT Banned

This protocol is designed for a customer-facing CSM role. Legitimate inferences
backed by real evidence are **valuable** and should be kept. Examples:

**Good inference (keep it):**
- "Renewal date Jan 2027 — INFERRED from 24-month term starting Jan 2025"
- "Likely using Events + Payments — INFERRED from onboarding notes mentioning both products"
- "Follow-up needed by Friday — INFERRED from Sarah saying 'let's connect before end of week' in Fathom transcript"

**Bad inference (should be BLANK):**
- "Customer is happy with the product" — no evidence cited
- "Renewal is low risk" — no recent meeting data to support this
- "They'll probably expand to Messaging" — speculation without signals

**The rule: Infer when you have evidence. Flag it as inferred. Show the
evidence. Never guess silently.**

---

## Verification-Before-Completion (from Superpowers)

Before any skill presents its output as complete, it must pass this check:

1. **Scan all non-blank fields** — does each have a Source label?
2. **Scan all INFERRED fields** — does each have an evidence trail?
3. **Scan all BLANK fields** — does each have a Flags table entry?
4. **Scan for red flags** — any use of "should," "probably," "likely,"
   "typically," "usually" without a source citation?
5. **Only then** present the output.

If any check fails, fix it before presenting. Do not present and apologize
later — fix first.

---

## Pre-Delivery Checklist (from UI/UX Pro Max)

Every content-producing skill includes this checklist. It is verified
internally before the SKILL RESULT is returned to PM:

- [ ] All non-blank fields have Source labels (EXTRACTED or INFERRED)
- [ ] All INFERRED fields have one-sentence evidence trails
- [ ] All BLANK fields have Flags table entries
- [ ] No unsupported confident assertions (no "should/probably" without source)
- [ ] Confidence level (High/Medium/Low) accurately reflects evidence quality:
  - **High** = all key fields EXTRACTED, minimal blanks, recent data
  - **Medium** = mix of EXTRACTED and INFERRED, some blanks, or data >30 days old
  - **Low** = mostly INFERRED or BLANK, stale data, or missing key sources
- [ ] SKILL RESULT Gaps/failures field lists anything that couldn't be verified

---

## How Skills Reference This Protocol

Add to every skill's SKILL.md, as a top-level section after the main
instructions:

```markdown
## Honesty Protocol
Read and follow `skills/core/honesty-protocol.md` for all outputs.
All values must be labeled EXTRACTED or INFERRED with evidence.
Ambiguous or missing values must be BLANK with a Flags entry.
A wrong answer is 3x worse than a blank — when in doubt, leave it blank.
```

For skills that produce structured tables (com-update, customer-dossier,
day-prep-recap), add Source and Evidence columns to the output template.

For skills that produce prose (email-templates, blackthorn-brand), add a
Source Summary section at the end listing which facts are EXTRACTED vs INFERRED.

---

## How Auto-Research Evaluates Honesty

Auto-research includes at least one honesty criterion in every evaluation:

**Criterion: Honesty Protocol Compliance**
```json
{
  "id": "C_HONESTY",
  "name": "Honesty Protocol Compliance",
  "description": "Output follows the three honesty rules: Force Blank, Penalize Guessing, Show the Source",
  "evaluation_prompt": "Check the output against the honesty protocol. (1) Are all values labeled EXTRACTED or INFERRED? (2) Do all INFERRED values have evidence trails? (3) Are ambiguous/missing values BLANK with Flags entries? (4) Are there any confident assertions without sources? Any violation is a FAIL. Answer PASS or FAIL.",
  "source": "honesty-protocol"
}
```

This criterion is mandatory — it cannot be excluded from any eval set.

---

## How PM Enforces This Protocol

PM's quality auditing role includes honesty monitoring:

1. **After every skill chain:** PM scans all SKILL RESULTs for honesty compliance.
   If a skill returns output without Source labels, PM logs it to the health
   ledger as a `honesty-violation` observation.

2. **Confidence calibration check:** If a skill claims High confidence but has
   >30% INFERRED fields, PM flags it as miscalibrated. If a skill claims High
   but has any BLANK fields on critical customer data, PM flags it.

3. **Escalation pattern:** Repeated honesty violations by the same skill trigger
   PM to recommend auto-research focus on that skill's honesty compliance.

---

## Domain-Specific Guidance

### Customer-Facing Data (customer-dossier, com-update, email-templates)
- **Strictest enforcement.** Every customer fact must have a source.
- Names, dates, deal stages, contacts — all must be EXTRACTED from dossier
  or CRM data. If the dossier is stale, flag it.
- Never fabricate meeting outcomes, commitments, or next steps.

### Meeting Research (fathom, post-meeting-sweep)
- Fathom transcript quotes = EXTRACTED (cite timestamp)
- Fathom summary/AI-generated recap = INFERRED (cite "Fathom AI summary")
- Action items from transcripts = EXTRACTED if verbatim, INFERRED if interpreted
- "Customer sentiment" = always INFERRED (cite specific quotes as evidence)

### Product Answers (blackthorn-support)
- Answers from product docs = EXTRACTED (cite doc name/section)
- Answers generalized from related features = INFERRED (cite which feature
  docs informed the answer)
- Anything not in available docs = BLANK + recommend product-feedback-poster

### Content Generation (email-templates, blackthorn-brand)
- Customer details in drafts = must trace back to dossier (EXTRACTED)
- Meeting references = must trace back to Fathom/Gmail (EXTRACTED)
- Scheduling suggestions = INFERRED from calendar context (cite source)
- Never invent dates, meeting outcomes, or commitments not in source data

### Memory Management (dream, memory-create)
- Facts being written to MEMORY.md or dossiers must have sources
- Dream extracts from session transcripts = EXTRACTED (cite session)
- Dream interpretations of patterns across sessions = INFERRED (cite sessions)
- Pruning decisions = must cite why the entry is stale (last referenced date,
  contradicting evidence)
