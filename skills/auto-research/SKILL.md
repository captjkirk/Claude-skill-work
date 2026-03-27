---
name: auto-research
description: >
  Autonomous skill improvement using the autoresearch pattern. Reads any target
  skill, dynamically generates binary evaluation criteria and success metrics,
  runs simulated test cases, scores outputs, and iteratively improves the skill —
  keeping changes only when they raise the pass rate. First iteration runs
  interactively for approval; subsequent iterations run autonomously. Invoke on:
  "auto-research [skill]", "improve this skill automatically", "run autoresearch
  on [skill]", "optimize [skill] overnight", "what's the pass rate for [skill]".
  Also invoke when dream's EVO pass surfaces a proposal and the user says
  "auto-improve it" or "run the research loop on that". Use this skill any time
  someone wants to measure, benchmark, or autonomously improve a skill's
  reliability — even if they don't use the word "autoresearch".
---

# Auto-Research — Autonomous Skill Improvement

Applies the autoresearch pattern (Karpathy / Saraev) to Claude skills: define
success criteria upfront, evaluate the skill against them, iterate with atomic
changes, and keep only what measurably improves the pass rate.

Dream's EVO pass catches problems reactively from session transcripts.
Auto-research catches problems proactively by stress-testing skills in isolation
and improving them through a controlled experiment loop.

---

## How It Works (Overview)

```
Phase 1 — Analyze the target skill
Phase 2 — Dynamically generate criteria + test cases
Phase 3 — Run baseline evaluation
Phase 4 — First iteration (interactive — user approves before continuing)
Phase 5 — Autonomous iteration loop (keep/discard based on pass rate)
Phase 6 — Return SKILL RESULT to PM
```

---

## Arguments

```
$ARGUMENTS: <path-to-skill> [--iterations N] [--criteria-only] [--auto] [--interactive]
```

| Flag | Default | What it does |
|------|---------|-------------|
| `<path-to-skill>` | required | Path to the target SKILL.md |
| `--iterations N` | 10 | Maximum improvement iterations |
| `--criteria-only` | off | Stop after generating criteria (for review before running) |
| `--auto` | off | Skip the interactive first iteration — go fully autonomous |
| `--interactive` | off | Stay interactive for ALL iterations (pause for approval each time) |

If neither `--auto` nor `--interactive` is passed, the default behavior is:
first iteration interactive, remaining iterations autonomous.

---

## Phase 1 — Analyze Target Skill

Before generating any criteria, deeply understand the skill and its role in the
orchestration hierarchy.

### 1a — Read the Skill

Read the target SKILL.md in full. Extract:

- **Name and purpose** — what does this skill do?
- **Input format** — what does `$ARGUMENTS` or the SKILL REQUEST expect?
- **Output format** — what does the SKILL RESULT look like? What fields does PM expect?
- **Domain classification** — orchestration, customer research, content generation, memory management, product knowledge, utility, or other
- **Dependencies** — which skills does it invoke or get invoked by?
- **PM routing triggers** — what signals in PM's routing table cause this skill to fire?
- **Tier classification** — which of its actions are Tier 1 (autonomous) vs. Tier 2 (flag to user)?

### 1b — Read Contextual Signals

Gather evidence of known issues before generating criteria:

1. **PROCESS-LESSONS.md** — scan for any entries mentioning this skill by name.
   Extract: what went wrong, what the correct approach should be, which workflows
   were affected.

2. **EVO proposals** — check `outputs/evo-proposals/` for any pending proposals
   targeting this skill. Extract: pattern detected, root cause, proposed change.

3. **PM's Skill Catalog entry** — read PM's routing table and the specific catalog
   entry for this skill. Note what PM expects in the SKILL RESULT and when PM
   would deepen or re-route.

4. **Upstream/downstream skills** — identify which skills feed into this one and
   which skills consume its output. This informs the hierarchy-aware evaluation.

### 1c — Classify Position in Hierarchy

Determine where this skill sits in the orchestration chain:

| Layer | Examples | Evaluation Focus |
|-------|----------|-----------------|
| **Orchestrator** | PM, morning-orchestrator | Routing correctness, signal detection, parallel handling, Tier 1/2 classification |
| **Primary worker** | customer-dossier, fathom, email-templates, com-update, dream, blackthorn-support | SKILL RESULT schema compliance, confidence calibration, "Suggested next" accuracy, Tier 2 flagging |
| **Chained skill** | day-prep-recap (after morning-orchestrator), product-feedback-poster (after blackthorn-support) | Handling of upstream SKILL RESULT as input, format compatibility |
| **Utility** | memory-create, memory-delete, subfolders, process-mistakes | Idempotency, correct file targeting, confirmation in SKILL RESULT |

Save the full analysis to `outputs/auto-research/<skill-name>/analysis.md`.

---

## Phase 2 — Generate Criteria & Test Cases

This is the core of auto-research. Criteria and test cases are generated
dynamically based on the Phase 1 analysis — not from a fixed template.

### 2a — Generate Evaluation Criteria

Create 3–6 binary (PASS/FAIL) criteria. Read `references/criteria-templates.md`
for domain-specific heuristics, but adapt them to the specific skill.

**Rules for criteria:**

- Every criterion MUST be binary — PASS or FAIL, never a scale or score
- 3–6 criteria total. Below 3 leaves loopholes. Above 6 invites checklist gaming.
- Criteria must be **independently evaluable** — one failing should not auto-fail another
- Criteria must cover **orthogonal quality dimensions** — not three variants of "format compliance"
- At least one criterion must test **SKILL RESULT schema compliance** (does the output match what PM expects?)
- If PROCESS-LESSONS.md or EVO proposals flagged specific issues, include a criterion targeting that failure pattern

**Criterion format:**

```json
{
  "id": "C1",
  "name": "Short descriptive name",
  "description": "What this criterion checks and why it matters",
  "evaluation_prompt": "Specific question to ask when evaluating. Answer PASS or FAIL with one sentence justification.",
  "source": "domain-heuristic | evo-proposal | process-lesson | cross-skill"
}
```

### 2b — Generate Test Cases

Create 5–10 test scenarios that exercise the skill across its expected operating range.

**Test case categories:**

| Category | Count | What it tests |
|----------|-------|--------------|
| Happy path | 2–3 | Typical, well-formed inputs the skill sees daily |
| Edge cases | 2–3 | Boundary conditions, minimal input, unusual formats |
| Cross-skill integration | 1–2 | Realistic upstream SKILL RESULT as input (for chained skills) or realistic SKILL REQUEST from PM |
| Known failure patterns | 1–2 | Scenarios drawn from PROCESS-LESSONS.md or EVO proposals |

**For chained skills:** Generate test cases using realistic upstream output, not
synthetic prompts. For example, if testing `day-prep-recap`, create test input
that looks like a real `morning-orchestrator` SKILL RESULT — with actual meeting
structures, dossier flags, and the formatting PM would pass through.

**Test case format:**

```json
{
  "id": "T1",
  "category": "happy_path",
  "name": "Descriptive name for this scenario",
  "input": "The simulated $ARGUMENTS or SKILL REQUEST content",
  "context": "Any additional context the skill would have (dossier state, MEMORY.md entries, etc.)",
  "description": "What this test case is designed to reveal"
}
```

Save criteria to `outputs/auto-research/<skill-name>/criteria.json`.
Save test cases to `outputs/auto-research/<skill-name>/test-cases.json`.

**If `--criteria-only` was passed:** Stop here. Present criteria and test cases
to the user for review. Include a note: "Review these criteria and test cases.
When ready, run `/auto-research <skill-path>` again to execute the evaluation loop."

---

## Phase 3 — Baseline Evaluation

Run the full evaluation suite against the current (unmodified) skill.

### 3a — Simulated Execution

Since skills are prompts (not executable code), evaluation works through
**simulated execution** — Claude role-plays invoking the skill.

For each test case:

1. Read the current skill file as the system context
2. Use the test case's `input` as the simulated `$ARGUMENTS` or SKILL REQUEST
3. Use the test case's `context` to simulate the workspace state
4. Generate what the skill **would produce** — the full SKILL RESULT or output

**Generate ALL outputs first, write them to disk, THEN evaluate.** This temporal
separation prevents the evaluator from being influenced by generation intent.

Save each simulated output to:
`outputs/auto-research/<skill-name>/iterations/000/outputs/T<id>-output.md`

### 3b — Evaluation Pass

For each simulated output, evaluate against EVERY criterion:

**Adopt a strict reviewer mindset.** You are looking for genuine failures, not
confirming success. A PASS means the criterion is unambiguously met. If there
is any reasonable doubt, mark FAIL. Do not rubber-stamp outputs. Do not give
the benefit of the doubt. This adversarial stance is essential — without it,
the same model generating and evaluating will converge on inflated scores.

For each (test case, criterion) pair:
1. Read the criterion's `evaluation_prompt`
2. Read the simulated output
3. Answer PASS or FAIL with a one-sentence justification

### 3c — Aggregate Results

Calculate pass rate: `(passed_checks / total_checks) * 100`

Where `total_checks = number_of_test_cases * number_of_criteria`

Save full results to:
`outputs/auto-research/<skill-name>/iterations/000/eval-output.json`

```json
{
  "iteration": 0,
  "timestamp": "ISO 8601",
  "pass_rate": 66.7,
  "total_checks": 30,
  "passed": 20,
  "failed": 10,
  "results": [
    {
      "test_case": "T1",
      "criterion": "C1",
      "result": "PASS",
      "justification": "..."
    }
  ],
  "failure_patterns": [
    "C3 fails on edge case inputs — skill does not handle empty context gracefully",
    "C2 fails across all test cases — SKILL RESULT missing 'Gaps/failures' field"
  ]
}
```

Write baseline to `results.tsv`:
```
iteration	timestamp	pass_rate	delta	status	description
0	[timestamp]	66.7	0.0	baseline	Initial evaluation
```

Save original skill to `outputs/auto-research/<skill-name>/baseline.md`.

Present baseline results to the user:
- Overall pass rate
- Which criteria pass/fail most often
- Top failure patterns identified
- Which test cases are hardest

---

## Phase 4 — Interactive First Iteration

Unless `--auto` was passed, the first improvement iteration runs interactively.

### 4a — Analyze Failures

Group failures by:
1. **By criterion** — which criterion fails most often? This indicates a systematic gap.
2. **By test case** — which test case fails the most criteria? This indicates a weak scenario.
3. **By pattern** — are failures clustered around a common root cause?

### 4b — Propose ONE Change

Following the autoresearch principle of atomic modifications, propose exactly
ONE focused change to the skill:

- Add a missing instruction or clarification
- Add or improve an example
- Fix an ambiguous or contradictory section
- Add explicit handling for an edge case
- Restructure a confusing section
- Remove text that causes confusion (simpler is often better)

**What NOT to propose:**
- Meta-instructions like "ensure all criteria pass" or "always produce correct output"
- Multiple changes bundled together (one change per iteration)
- Changes that reference the evaluation framework itself
- Additions that would grow the skill by more than 15% in a single iteration

### 4c — Present to User

Use `AskUserQuestion` (following PM's Hard Rule 1 — never ask as plain text):

Show the user:
- The top failure pattern
- The root cause in the skill's text
- The proposed change (what to add/modify/remove)
- Expected impact on pass rate

Options:
- "Apply this change" — proceed with the proposed change
- "Modify the approach" — user provides alternative direction
- "Skip — try something else" — discard this proposal, try a different angle
- "Stop here" — end the loop, report current results

### 4d — Execute

If approved:
1. Apply the change to the skill file
2. Re-run the full evaluation suite (Phase 3)
3. Compare to baseline
4. If pass rate improved or held steady: **KEEP** the change
5. If pass rate declined: **REVERT** the change, inform the user

Present the updated results. If the user is satisfied, switch to autonomous mode
for remaining iterations.

---

## Phase 5 — Autonomous Loop

After the interactive first iteration (or immediately if `--auto` was passed),
run the remaining iterations autonomously.

```
previous_best = current pass rate

FOR i = 2 to N (where N = --iterations, default 10):

    1. Analyze failure patterns from most recent eval
    2. Propose ONE atomic change (same rules as Phase 4b)
    3. Apply the change to the skill file
    4. Snapshot the skill to iterations/<NNN>/skill-snapshot.md
    5. Re-run full evaluation suite
    6. Record results

    IF pass_rate >= previous_best:
        STATUS = "keep"
        previous_best = pass_rate
    ELSE:
        STATUS = "discard"
        Revert the skill file to previous version

    Append to results.tsv:
    [iteration]  [timestamp]  [pass_rate]  [delta]  [status]  [one-line description]

    Write iteration summary to iterations/<NNN>/summary.md

    TERMINATION CONDITIONS:
    - pass_rate == 100% → stop (perfect score achieved)
    - 3 consecutive discards → try a "radical change" (rewrite a section
      rather than tweaking, or try a completely different approach to the
      most stubborn failure)
    - 5 consecutive discards → stop (convergence failure — further
      iteration is unlikely to help without human guidance)

END FOR
```

### Prompt Bloat Guard

After each kept iteration, check the skill's word count:
- If word count has grown >50% from baseline → flag it
- If pass rate is equal but word count is lower → prefer the shorter version
- If a kept change only adds words without improving pass rate → consider reverting

The goal is the *minimum effective prompt* — as lean as possible while
maximizing the pass rate.

---

## Phase 6 — Return SKILL RESULT to PM

When the loop completes (or is stopped), package results and return to PM.

```
## SKILL RESULT: auto-research
Timestamp: [ISO 8601]
Customer: None
Actions taken: Analyzed [skill-name]. Generated [N] criteria, [N] test cases.
  Ran [N] iterations. Baseline: [X]% → Final: [Y]%.

Findings:

  === ITERATION SUMMARY ===
  - Iteration 0 (baseline): [X]% — [N] criteria, [N] test cases
  - Iteration 1 (interactive): [description] — [KEEP/DISCARD] — [X]% → [Y]%
  - Iteration 2: [description] — [KEEP/DISCARD] — [X]% → [Y]%
  ...

  === PROPOSED SKILL PATCH ===
  Skill: [skill-name]
  Current file: [path]
  Baseline word count: [N] → Final word count: [N]
  Changes applied (cumulative diff from baseline):
  [For each kept change: one-line description of what was changed and why]

  === CRITERIA & PASS RATES ===
  - C1: [name] — baseline [X]% → final [Y]%
  - C2: [name] — baseline [X]% → final [Y]%
  ...

  === FULL RESULTS ===
  See outputs/auto-research/[skill-name]/results.tsv

  === TASKS.md ADDITIONS ===
  - [ ] [AUTO-RESEARCH] Review skill improvement for [skill-name] — [baseline]% → [final]%. See outputs/auto-research/[skill-name]/

Confidence: [High if pass rate improved significantly and converged;
  Medium if improvement was modest or loop hit the discard limit;
  Low if no improvement was achieved]
Gaps/failures: [any eval limitations — e.g., simulated execution can't test
  API calls, some criteria may need real-world validation]
Suggested next: Review proposed changes in outputs/auto-research/[skill-name]/
Flags for Jared: Skill patch requires human review before applying (Tier 2).
  Review the cumulative diff and test it in a real session before installing.
```

---

## Edge Cases

**Target skill doesn't exist** — report error and exit cleanly.

**Target skill has no SKILL RESULT block** — generate a criterion specifically
for adding one (this is a cross-skill compliance issue PM depends on).

**Target skill is PM itself** — PM is the orchestration hub. Evaluating PM
requires simulating full multi-skill workflows. Flag this as high-complexity
and recommend `--interactive` mode with `--iterations 3` to start.

**No PROCESS-LESSONS.md or EVO proposals exist** — that's fine. Generate
criteria purely from the skill analysis and domain heuristics.

**Skill depends on external APIs (Fathom, Gmail, Slack, Calendar)** — simulated
execution cannot call real APIs. Generate realistic mock responses for test cases.
Flag in the SKILL RESULT that real-world validation is needed.

**Multiple auto-research runs on the same skill** — check for existing
`outputs/auto-research/<skill-name>/` data. If a previous run exists, load the
previous criteria and results as context. Build on prior work rather than
starting fresh — unless the user explicitly asks to reset.

---

## Integration with Dream's EVO Pass

Auto-research and dream's EVO pass are complementary:

| | Dream EVO | Auto-Research |
|---|---|---|
| **Trigger** | End of session (reactive) | On demand or scheduled (proactive) |
| **Input** | Session transcripts, PROCESS-LESSONS.md | Skill file + generated criteria |
| **Method** | Pattern matching across sessions | Simulated execution + binary eval |
| **Output** | EVO proposals (qualitative) | Pass rate + cumulative diff (quantitative) |
| **Applies changes** | Never (proposes only) | Never (proposes only — Tier 2) |

**Handoff from EVO to auto-research:** When dream surfaces an EVO proposal, the
user can say "run auto-research on that" and this skill will:
1. Read the EVO proposal to understand the pattern
2. Generate criteria that specifically target the identified failure
3. Run the improvement loop to find a fix
4. Return a tested, measured patch (not just a proposal)

This turns EVO's qualitative signal into a quantitative improvement.

---

## Scheduling

Auto-research can be scheduled to run overnight using the `schedule` skill:

```
/schedule create --name "auto-research-email-templates" \
  --cron "0 1 * * 6" \
  --prompt "/auto-research skills/email-templates --auto --iterations 10"
```

This runs every Saturday at 1 AM, autonomously improving the target skill.
Results are available in `outputs/auto-research/` for review on Monday morning.

The morning-orchestrator could optionally be extended to surface auto-research
results in the daily brief if any ran overnight.
