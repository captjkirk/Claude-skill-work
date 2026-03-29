# Output Validation Pass — Blueprint

This is a design doc. The next Claude Code session implements this as an
addition to PM's quality auditing role in the live Cowork workspace.

## The Distinction

| Layer | What It Does | When It Runs |
|-------|-------------|-------------|
| **Honesty Protocol** | Tells skills HOW to produce honest output (rules) | During skill execution |
| **Validation Pass** | Independently VERIFIES the output is accurate (check) | After skill execution, before user sees it |
| **Auto-Research** | Measures and improves skills over time (improvement) | On schedule or on demand |
| **Health Ledger** | Tracks patterns across sessions (memory) | After each skill chain |

The honesty protocol is the rule. The validation pass is the enforcement.

## Sources

- [The Honesty Gap](https://d-squared70.github.io/ChatGPT-and-Claude-Got-Smarter.-Not-More-Honest.)
  — Verification as a separate step from generation
- [Superpowers](https://github.com/obra/superpowers) — Verification-before-
  completion: "Skip any step = lying, not verifying." Five-step verification
  process required before claiming any success.

---

## How It Works

PM already sees every SKILL RESULT before the user does (it's the central
routing hub). The validation pass adds a scan step between receiving the
SKILL RESULT and presenting it to the user.

```
Skill produces output (SKILL RESULT)
        ↓
PM receives SKILL RESULT
        ↓
=== VALIDATION PASS ===  ← NEW
        ↓
PM presents to user (with validation notes if needed)
```

---

## Validation Levels

Not every output needs the same level of scrutiny. Three levels:

### Level 1: Quick Scan (Every Output)

Runs on ALL SKILL RESULTs. Lightweight, fast, no token overhead.

PM checks:
- [ ] All required SKILL RESULT fields present?
- [ ] Source labels (EXTRACTED/INFERRED) on all values?
- [ ] BLANK fields have Flags entries?
- [ ] Confidence level present and within valid range (High/Medium/Low)?
- [ ] Red-flag words ("should," "probably," "typically," "usually," "likely")
      without a source citation?
- [ ] "Suggested next" references a real skill by correct name?
- [ ] Tier 1/2 classification present on actionable items?

**If all pass:** Present output to user. No delay, no overhead.
**If any fail:** PM appends a validation note to the output:
```
=== PM VALIDATION NOTE ===
[N] items flagged during validation:
- [Field X] is missing a source label
- Confidence is "High" but 4 of 8 fields are INFERRED — may be miscalibrated
```

### Level 2: Fact Check (Customer-Facing Output)

Runs on SKILL RESULTs from: email-templates, com-update, customer-dossier,
blackthorn-support, day-prep-recap, flagged-onboarding-sync, kickoff-deck.

Everything from Level 1, plus:
- [ ] Customer name matches the dossier? (cross-reference)
- [ ] Dates mentioned in the output — do they exist in calendar, Fathom,
      or dossier data? (date validation)
- [ ] Commitments or action items — are they sourced from a meeting transcript
      or email, not fabricated? (commitment validation)
- [ ] Product information — does it match available product docs?
      (for blackthorn-support)
- [ ] Contact names and roles — do they match the dossier's contact list?

**If any fail:** PM flags it BEFORE presenting to the user:
```
=== PM VALIDATION NOTE ===
HOLD — [N] items need verification before this output is reliable:
- "Tuesday follow-up call" — no Tuesday meeting found in calendar or Fathom
- "Sarah mentioned expanding to Messaging" — could not verify in transcript
Recommend: Review these items manually before acting on this output.
```

### Level 3: Deep Validation (High-Stakes Output)

Runs when:
- The output will be sent externally (email, Slack post)
- The output involves customer risk signals
- The output recommends irreversible actions
- Confidence is Medium or Low on customer-critical data

Everything from Level 2, plus:
- [ ] **Independent re-derivation:** For each INFERRED value, PM independently
      checks whether the inference is reasonable given the source data. PM
      doesn't just verify the label exists — it verifies the reasoning.
- [ ] **Subjective claims check:** For opinions, assessments, or predictions
      (e.g., "expansion is likely," "customer is satisfied"), PM checks:
      is this REASONABLE given the evidence? Not "is it true" (can't verify
      subjective claims) but "would a reasonable CSM draw this conclusion
      from the available data?"
- [ ] **Contradiction scan:** Does anything in the output contradict known
      data in the dossier, recent Fathom transcripts, or MEMORY.md?
- [ ] **Completeness check:** Is there relevant data in the dossier or
      recent interactions that the skill DIDN'T include but should have?

**If any fail:** PM blocks presentation and recommends correction:
```
=== PM VALIDATION — ACTION REQUIRED ===
This output has [N] validation failures on high-stakes content:

1. CONTRADICTION: Output says "contract renews Jan 2027" but dossier shows
   "early termination clause invoked Nov 2026." These conflict.
   → Recommend: Verify with dossier before sending.

2. INCOMPLETE: Recent Fathom transcript (Mar 25) mentions customer frustration
   with onboarding timeline. This is not reflected in the email draft.
   → Recommend: Address or acknowledge before sending.

3. SUBJECTIVE — UNREASONABLE: "Customer is happy with progress" — last 2
   meetings flagged concerns about timeline. This assessment contradicts
   recent signals.
   → Recommend: Revise to reflect actual sentiment.
```

---

## Validation Level Assignment

PM automatically assigns the validation level based on the source skill
and context:

| Condition | Level |
|-----------|-------|
| Any SKILL RESULT | Level 1 (always) |
| Source skill is customer-facing (see list above) | Level 2 |
| Output will be sent externally (Tier 2 flag present) | Level 3 |
| Customer risk signal detected anywhere in chain | Level 3 |
| Confidence is Medium or Low on customer-critical data | Level 3 |
| User explicitly requests deep validation | Level 3 |

---

## Handling Subjective Content

Not everything is verifiable as "true" or "false." For subjective elements:

| Content Type | Validation Approach |
|-------------|-------------------|
| **Factual claims** (dates, names, deal stages) | Verify against source data. Must be EXTRACTED or verifiably INFERRED. |
| **Assessments** (customer satisfaction, risk level) | Check for REASONABLENESS. Does the assessment align with available evidence? Flag if contradicted by recent data. |
| **Predictions** (will renew, likely to expand) | Must be labeled INFERRED with evidence. Flag if evidence is thin or contradictory. |
| **Recommendations** (next steps, suggested actions) | Check that recommendations follow logically from findings. Flag if recommendations don't connect to evidence. |
| **Tone/voice** (email drafts, brand content) | Check against voice profile/brand guidelines. Subjective but reference-checkable. |

The key phrase for subjective content: **"Would a reasonable CSM draw this
conclusion from the available data?"** If yes → pass. If the data contradicts
the conclusion or the evidence is too thin → flag.

---

## Performance Considerations

The validation pass should NOT slow down the user experience noticeably:

- **Level 1** is a pattern-matching scan — near-instant, no API calls
- **Level 2** cross-references against local files (dossier, calendar cache) —
  fast, file reads only
- **Level 3** requires deeper analysis — may add 5-10 seconds, but only runs
  on high-stakes output that should be reviewed carefully anyway

**Optimization:** PM can run Level 1 inline as it processes the SKILL RESULT.
Level 2 and 3 run only when triggered by the conditions above.

**Trade-off:** A small amount of latency on high-stakes output is worth catching
errors before they reach customers. The user sees a brief "Validating..." note
for Level 3 checks, then gets a clean or flagged output.

---

## Integration with Health Ledger

Every validation failure is logged to the health ledger:

```json
{
  "id": "HL-2026-03-29-VAL-001",
  "timestamp": "2026-03-29T14:30:00Z",
  "skill": "email-templates",
  "type": "honesty-violation",
  "severity": "high",
  "chain_context": "post-meeting-sweep → fathom → email-templates",
  "observation": "Level 2 validation caught fabricated date: 'Tuesday follow-up' not in calendar or Fathom",
  "evidence": "Validation pass Level 2, date check failed. Calendar shows no Tuesday meetings for Acme Corp.",
  "recommendation": "Add date validation script to email-templates",
  "resource_type": "script",
  "consumed_by_auto_research": false,
  "resolved": false
}
```

This feeds the continuous improvement loop:
Validation catches error → Health ledger logs it → Auto-research targets it →
Skill improves → Validation verifies the fix → Resolved.

---

## PM's Validation Summary (in SKILL RESULT to User)

When PM presents output to the user, it includes a validation status:

```
=== VALIDATION STATUS ===
Level: 2 (Customer-Facing)
Result: PASS (8/8 checks passed)
```

Or when issues are found:

```
=== VALIDATION STATUS ===
Level: 3 (High-Stakes — external send detected)
Result: 2 FLAGS — review before sending
- Date "Tuesday follow-up" not verified in calendar (see note above)
- Assessment "customer is satisfied" contradicts Mar 25 Fathom transcript
```

This gives the user immediate visibility into how much they can trust
the output without reading every detail themselves.
