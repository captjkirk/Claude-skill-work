# Auto-Research Upgrades — Blueprint

This is a design doc. The next Claude Code session modifies the existing
auto-research SKILL.md in the live Cowork workspace with these additions.

Auto-research already exists and works. These upgrades integrate it with
the health ledger, honesty protocol, and the TDD-for-skills pattern.

## Sources

- [The Honesty Gap](https://d-squared70.github.io/ChatGPT-and-Claude-Got-Smarter.-Not-More-Honest.)
  — Evaluator must follow the same honesty rules it's testing for.
- [Superpowers](https://github.com/obra/superpowers) — TDD for skills
  (RED/GREEN/REFACTOR), verification-before-completion.
- [ClaudeMem](https://github.com/thedotmack/claude-mem) — Structured
  observation extraction for the health ledger consumption pattern.

---

## Upgrade 1: Mandatory Honesty Criterion

Every auto-research evaluation must include this criterion. It cannot be
excluded from any eval set, regardless of the target skill's domain.

### Add to criteria-templates.md — New "Honesty Protocol" Section

```markdown
## Honesty Protocol Compliance (Mandatory — Every Skill)

This criterion is automatically included in every evaluation. It cannot be
removed or skipped. Source: `skills/core/honesty-protocol.md`

### Honesty Protocol Compliance
**What to check:** Does the output follow all three honesty rules?
1. Force Blank — are ambiguous/missing values BLANK with Flags entries?
2. Penalize Guessing — are there any confident assertions without evidence?
3. Show the Source — are all values labeled EXTRACTED or INFERRED with evidence?

**Evaluation prompt:** "Check the output against the honesty protocol.
(1) Are all values labeled EXTRACTED or INFERRED? (2) Do all INFERRED values
have evidence trails? (3) Are ambiguous/missing values BLANK with Flags
entries? (4) Are there any confident assertions without sources? (5) Does
the Confidence level (High/Medium/Low) match the evidence quality? Any
violation is a FAIL. Answer PASS or FAIL with specific examples of the
violation."

### Confidence Calibration
**What to check:** Does the stated confidence accurately reflect the evidence?

**Evaluation prompt:** "Compare the stated Confidence level against the
evidence in the output. High confidence requires mostly EXTRACTED values
with minimal blanks. Medium allows a mix of EXTRACTED and INFERRED. Low
should have mostly INFERRED or BLANK. Is the confidence level accurately
calibrated? Overconfidence on thin evidence is a FAIL. Answer PASS or FAIL."
```

### Add to SKILL.md — Phase 2 Criteria Generation

Add this instruction after the existing criteria generation rules:

```
**Mandatory criterion:** Every evaluation MUST include the "Honesty Protocol
Compliance" criterion from criteria-templates.md. This criterion tests whether
the skill's output labels values as EXTRACTED/INFERRED, includes evidence
trails, and leaves ambiguous values BLANK. This criterion cannot be excluded.
```

---

## Upgrade 2: Health Ledger Consumption

Auto-research now reads the PM health ledger as an input signal alongside
PROCESS-LESSONS.md and EVO proposals.

### Add to SKILL.md — Phase 1 (Analyze Target Skill)

Add step between existing steps 2 and 3:

```
### 1c — Read Health Ledger

Read `outputs/health-ledger/observations.jsonl` and filter for:
- `skill` matches the target skill name
- `consumed_by_auto_research` is `false`

For each unconsumed observation:

| Observation Type | Action |
|-----------------|--------|
| `honesty-violation` | Generate a criterion specifically targeting this honesty failure pattern. Generate a test case that reproduces the scenario. |
| `gap` or `missing-resource` | Generate a test case that would expose the gap. If the recommendation is for a script/reference/template, include a criterion testing whether the skill's output would improve with that resource. |
| `regression` | Generate a test case matching the regression scenario. Compare against the previous passing behavior. |
| `integration-failure` | Generate a cross-skill test case testing the specific handoff that broke. |
| `miscalibration` | Add the "Confidence Calibration" criterion and generate test cases with varying evidence quality to test calibration accuracy. |

After processing, mark each observation as `consumed_by_auto_research: true`
by updating the JSONL file.
```

### Add to SKILL.md — Phase 6 (Return SKILL RESULT)

Add health ledger write-back:

```
### Write Back to Health Ledger

After the improvement loop completes:

1. For each health ledger observation that was consumed:
   - If the related criterion now passes consistently → mark `resolved: true`
     with `resolution_note` describing the fix
   - If the criterion still fails → leave unresolved; PM will escalate

2. For any NEW patterns discovered during the improvement loop:
   - Persistent failures (same criterion fails across 3+ iterations despite
     attempts) → write new observation with type `regression`
   - Resource recommendations (skill would benefit from scripts/references/
     templates discovered during analysis) → write observation with type
     `missing-resource` and `resource_type` populated
   - Bloat detection (skill grew >50% during improvement) → write observation
     with type `bloat`
```

---

## Upgrade 3: TDD for Skills (from Superpowers)

Frame each improvement iteration using the RED/GREEN/REFACTOR pattern. This
provides a disciplined structure that prevents shotgun changes.

### Modify Phase 5 (Autonomous Loop) Iteration Logic

Replace the current iteration logic with:

```
FOR i = 2 to N:

    === RED ===
    Document the failure precisely:
    - Which test case fails? (cite ID)
    - Which criterion fails? (cite ID)
    - What does the skill currently produce that's wrong?
    - What SHOULD it produce instead?
    - Why does the current prompt text cause this failure?
    Write RED documentation to iterations/<NNN>/red.md

    === GREEN ===
    Make the MINIMUM change to make it pass:
    - ONE focused edit to the skill
    - No extra improvements, no cleanup, no "while we're here" additions
    - The change must directly address the RED documentation
    - If the change doesn't relate to the documented failure, reject it
    Apply the change, re-run full eval suite

    === REFACTOR ===
    If pass rate improved or held steady:
    - Can the change be expressed more concisely?
    - Did the change add unnecessary words?
    - Can anything be removed while maintaining the pass rate?
    If yes → simplify, re-run eval to verify, then KEEP
    If no → KEEP as-is

    IF pass_rate < previous_best → REVERT, log as DISCARD
    IF pass_rate >= previous_best → KEEP, update previous_best

    Log iteration: [RED description] → [GREEN change] → [REFACTOR result] → [KEEP/DISCARD]
```

### Why This Matters

Without TDD framing, auto-research tends to make changes based on "this seems
like it would help" rather than "this directly fixes the documented failure."
The RED phase forces precise diagnosis. The GREEN phase forces minimal change.
The REFACTOR phase prevents bloat.

This is the same principle as Superpowers' TDD for code, adapted for prompt
engineering: document the failure (test), fix it minimally (implementation),
then simplify (refactor).

---

## Upgrade 4: Evaluator Honesty (Anti-Rubber-Stamping)

The evaluator itself must follow the honesty protocol. This is the most
critical upgrade — without it, the same model generating and evaluating
will converge on inflated scores.

### Add to SKILL.md — Phase 3 (Baseline Evaluation)

Strengthen the adversarial evaluator instructions:

```
### Evaluator Honesty Protocol

The evaluator must follow the same honesty rules it tests for:

1. **Force Blank on uncertain judgments.** If the evaluator cannot determine
   whether a criterion is met based on the output alone, the result is FAIL
   (not a generous PASS). Uncertainty = FAIL.

2. **Penalize rubber-stamping.** A false PASS is 3x worse than a false FAIL.
   The evaluator should prefer strict judgment over generous judgment.

3. **Show the source for every judgment.** Every PASS must cite the specific
   part of the output that satisfies the criterion. Every FAIL must cite the
   specific part that violates it. "Generally looks good" is not a valid
   justification.

4. **Label evaluation confidence.** For each judgment, the evaluator notes
   whether it is CLEAR (unambiguous pass/fail) or BORDERLINE (could go either
   way). BORDERLINE judgments default to FAIL.

5. **Spot-check drift.** Every 5 iterations, the evaluator re-evaluates 2-3
   outputs from iteration 0 (baseline) using current criteria. If scores have
   drifted upward without the skill actually changing, flag it as evaluator
   drift and recalibrate.
```

---

## Upgrade 5: Escalation to PM

When auto-research identifies patterns that it cannot fix through prompt
iteration alone, it escalates to PM with specific findings.

### Escalation Triggers

| Trigger | What auto-research does |
|---------|----------------------|
| Same criterion fails 3+ iterations across separate runs | Write to health ledger: persistent failure. Recommend resource addition. |
| Skill grew >50% from baseline with marginal improvement | Write to health ledger: bloat. Recommend skill split. |
| Honesty criterion fails consistently | Write to health ledger: honesty-violation. PM flags to user. |
| Cross-skill handoff fails in integration tests | Write to health ledger: integration-failure. Identify which skill to fix. |
| 5 consecutive discards (convergence failure) | Write to health ledger: regression. Recommend human review + brainstorming session. |

### Escalation Format (Written to Health Ledger)

```json
{
  "id": "HL-2026-03-29-AR-001",
  "timestamp": "2026-03-29T22:00:00Z",
  "skill": "email-templates",
  "type": "gap",
  "severity": "high",
  "chain_context": "auto-research sweep iteration 7",
  "observation": "C3 (No Hallucinated Details) fails in 4/6 test cases across 3 consecutive auto-research runs. Prompt iteration alone cannot fix this — the skill lacks a mechanism to verify dates against calendar data.",
  "evidence": "Run 1: C3 pass rate 33%. Run 2: C3 pass rate 33%. Run 3: C3 pass rate 50% (partial improvement reverted next iteration). See outputs/auto-research/email-templates/results.tsv",
  "recommendation": "Add scripts/validate-dates.py that cross-checks any date mentioned in email drafts against calendar and Fathom data. This requires a validation script, not just prompt engineering.",
  "resource_type": "script",
  "consumed_by_auto_research": true,
  "resolved": false,
  "resolution_note": null
}
```

PM surfaces this to the user as a Tier 2 recommendation with context:
"Auto-research tried to fix date hallucination in email-templates across 3 runs
and couldn't solve it with prompt changes alone. It recommends adding a
validation script. Want me to have the research skill find existing date
validation patterns we could adapt?"

This closes the loop: auto-research identifies → PM surfaces → user approves →
research finds solutions → brainstorming evaluates → implementation proceeds.
