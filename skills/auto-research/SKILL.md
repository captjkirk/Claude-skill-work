---
name: auto-research
description: >
  Autonomous skill improvement using the autoresearch pattern. Reads a target
  skill (or all skills via --sweep), generates binary eval criteria and test
  cases, runs simulated evaluations, and iteratively improves the skill —
  keeping only changes that raise the pass rate. Sweep mode evaluates each
  skill independently then tests cross-skill integration (handoffs, routing,
  schema consistency). First iteration is interactive; subsequent iterations
  run autonomously. Invoke on: "auto-research [skill]", "improve this skill",
  "run autoresearch", "optimize [skill]", "evaluate all my skills", "run a
  full sweep", "test skill integration". Also invoke when dream's EVO pass
  surfaces a proposal and the user says "auto-improve it". Use any time
  someone wants to measure, benchmark, or autonomously improve skill
  reliability.
---

# Auto-Research — Autonomous Skill Improvement

Applies the autoresearch pattern (Karpathy / Saraev) to Claude skills: define
success criteria upfront, evaluate the skill against them, iterate with atomic
changes, and keep only what measurably improves the pass rate.

Dream's EVO pass catches problems reactively from session transcripts.
Auto-research catches problems proactively by stress-testing skills in isolation
and improving them through a controlled experiment loop.

## Honesty Protocol
Follow `skills/core/honesty-protocol.md` for all outputs.
The evaluator must follow the same honesty rules it tests for.
A false PASS is 3x worse than a false FAIL — when in doubt, mark FAIL.

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
$ARGUMENTS: <path-to-skill> | --sweep [options]
```

### Single-Skill Mode

| Flag | Default | What it does |
|------|---------|-------------|
| `<path-to-skill>` | required | Path to the target SKILL.md |
| `--iterations N` | 10 | Maximum improvement iterations |
| `--criteria-only` | off | Stop after generating criteria (for review before running) |
| `--auto` | off | Skip the interactive first iteration — go fully autonomous |
| `--interactive` | off | Stay interactive for ALL iterations (pause for approval each time) |

If neither `--auto` nor `--interactive` is passed, the default behavior is:
first iteration interactive, remaining iterations autonomous.

### Sweep Mode

| Flag | Default | What it does |
|------|---------|-------------|
| `--sweep` | off | Discover all skills, evaluate each individually, then run cross-skill integration eval |
| `--sweep-dir <path>` | `skills/` | Directory to scan for SKILL.md files |
| `--skip <name,...>` | none | Comma-separated skill names to exclude from sweep |
| `--integration-only` | off | Skip individual skill evals — only run cross-skill integration tests |
| `--baseline-only` | off | Run baseline evals for all skills (no improvement iterations) — useful for initial assessment |
| `--iterations N` | 5 | Per-skill iteration budget in sweep mode (lower default than single-skill to manage total runtime) |
| `--auto` | **on** | Sweep mode defaults to autonomous (override with `--interactive`) |
| `--priority <strategy>` | `worst-first` | Order to process skills: `worst-first` (lowest baseline first), `critical-first` (orchestrators and high-dependency skills first), `alphabetical` |

**Examples:**
```
/auto-research --sweep                              # Full sweep: all skills + integration
/auto-research --sweep --baseline-only              # Just measure everything, no improvements
/auto-research --sweep --criteria-only              # Generate all criteria for review
/auto-research --sweep --integration-only           # Only test how skills work together
/auto-research --sweep --skip dream,schedule        # Skip specific skills
/auto-research --sweep --priority critical-first    # Start with PM, morning-orchestrator
```

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

5. **Health Ledger** — read `outputs/health-ledger/observations.jsonl` and filter
   for observations where `skill` matches the target and `consumed_by_auto_research`
   is `false`. For each unconsumed observation:

   | Observation Type | Action |
   |-----------------|--------|
   | `honesty-violation` | Generate criterion targeting this honesty failure. Generate test case reproducing the scenario. |
   | `gap` / `missing-resource` | Generate test case exposing the gap. Criterion testing whether output improves with recommended resource. |
   | `regression` | Generate test case matching regression scenario. |
   | `integration-failure` | Generate cross-skill test case for the broken handoff. |
   | `miscalibration` | Add Confidence Calibration criterion. Test cases with varying evidence quality. |

   Mark processed observations as `consumed_by_auto_research: true`.

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
- **MANDATORY: Honesty Protocol Compliance** — every evaluation MUST include a criterion testing whether the skill labels values as EXTRACTED/INFERRED, includes evidence trails, and leaves ambiguous values BLANK. This criterion cannot be excluded. See `references/criteria-templates.md` Honesty Protocol section.

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

**Evaluator Honesty Protocol** — the evaluator follows the same rules it tests:

1. **Force FAIL on uncertain judgments.** Cannot determine if criterion is met
   based on output alone? Result is FAIL, not a generous PASS.
2. **A false PASS is 3x worse than a false FAIL.** Prefer strict judgment.
3. **Show the source for every judgment.** Every PASS must cite the specific
   part of the output that satisfies the criterion. Every FAIL must cite the
   violation. "Generally looks good" is not a valid justification.
4. **Label evaluation confidence.** Each judgment is CLEAR (unambiguous) or
   BORDERLINE (could go either way). BORDERLINE defaults to FAIL.
5. **Spot-check drift.** Every 5 iterations, re-evaluate 2-3 baseline outputs
   using current criteria. If scores drift upward without skill changes, flag
   evaluator drift and recalibrate.

For each (test case, criterion) pair:
1. Read the criterion's `evaluation_prompt`
2. Read the simulated output
3. Answer PASS or FAIL with a one-sentence justification citing specific evidence

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

Each iteration follows the TDD pattern — RED/GREEN/REFACTOR (adapted from
Superpowers for prompt engineering):

```
previous_best = current pass rate

FOR i = 2 to N (where N = --iterations, default 10):

    === RED (document the failure) ===
    - Which test case fails? (cite ID)
    - Which criterion fails? (cite ID)
    - What does the skill currently produce that's wrong?
    - What SHOULD it produce instead?
    - Why does the current prompt text cause this failure?
    Write RED documentation to iterations/<NNN>/red.md

    === GREEN (minimal fix) ===
    - ONE focused edit directly addressing the RED documentation
    - No extra improvements, no cleanup, no "while we're here" additions
    - If the change doesn't relate to the documented failure, reject it
    Apply the change to the skill file
    Snapshot to iterations/<NNN>/skill-snapshot.md
    Re-run full evaluation suite

    === REFACTOR (simplify if possible) ===
    If pass rate improved or held steady:
    - Can the change be more concise?
    - Did it add unnecessary words?
    - Can anything be removed while maintaining pass rate?
    If yes → simplify, re-run eval to verify

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

### Health Ledger Write-Back

After returning the SKILL RESULT, write back to the health ledger:

1. **For consumed observations:** If the related criterion now passes
   consistently → mark `resolved: true` with `resolution_note` describing
   the fix. If still failing → leave unresolved for PM escalation.

2. **For new patterns discovered:**
   - Persistent failures (same criterion fails 3+ iterations) → write
     `type: "regression"` with specific findings
   - Resource recommendations (skill needs scripts/references/templates) →
     write `type: "missing-resource"` with `resource_type`
   - Bloat (skill grew >50%) → write `type: "bloat"`

3. **Escalation:** When auto-research cannot fix a pattern through prompt
   iteration alone, write to health ledger with specific findings and
   recommendation. PM surfaces to user as Tier 2:

   "Auto-research tried to fix [issue] in [skill] across [N] runs and
   couldn't solve it with prompt changes alone. Recommends [resource].
   Want me to have the research skill find existing options?"

---

## Sweep Mode — Full Ecosystem Evaluation

When `--sweep` is passed, auto-research shifts from single-skill mode to a
three-stage ecosystem evaluation: discover, evaluate individually, then test
collectively.

### Stage 1 — Skill Discovery

Scan `--sweep-dir` (default: `skills/`) for all SKILL.md files. For each:

1. Read the SKILL.md
2. Classify: orchestrator, primary worker, chained skill, or utility
3. Map dependencies (reads PM's routing table + each skill's references)
4. Build the **dependency graph** — which skills feed into which

Save the discovery results to `outputs/auto-research/_sweep/discovery.json`:

```json
{
  "timestamp": "ISO 8601",
  "sweep_dir": "skills/",
  "skills_found": 26,
  "skills_skipped": ["schedule"],
  "dependency_graph": {
    "project-manager": {
      "layer": "orchestrator",
      "invokes": ["customer-dossier", "fathom", "com-update", "email-templates",
                   "blackthorn-support", "product-feedback-poster", "kickoff-deck",
                   "dream", "memory-create", "memory-delete", "process-mistakes",
                   "morning-orchestrator", "day-prep-recap", "post-meeting-sweep",
                   "flagged-onboarding-sync", "onboarding-process-sync", "subfolders",
                   "blackthorn-brand", "skill-creator"],
      "invoked_by": [],
      "criticality": "critical"
    },
    "customer-dossier": {
      "layer": "primary-worker",
      "invokes": [],
      "invoked_by": ["project-manager"],
      "criticality": "high",
      "note": "Hard dependency — always runs first when customer named"
    },
    "morning-orchestrator": {
      "layer": "orchestrator",
      "invokes": ["day-prep-recap"],
      "invoked_by": ["project-manager"],
      "criticality": "high"
    },
    "dream": {
      "layer": "primary-worker",
      "invokes": [],
      "invoked_by": ["project-manager"],
      "criticality": "high",
      "note": "Proposes writes — PM executes. Never writes directly."
    }
  },
  "chains": [
    {
      "name": "morning-workflow",
      "sequence": ["morning-orchestrator", "customer-dossier", "day-prep-recap"],
      "trigger": "7 AM weekday cron"
    },
    {
      "name": "post-meeting",
      "sequence": ["post-meeting-sweep", "fathom", "com-update"],
      "trigger": "fireAt +15 min after meeting"
    },
    {
      "name": "product-question-escalation",
      "sequence": ["blackthorn-support", "product-feedback-poster"],
      "trigger": "Product question with Confidence < High"
    },
    {
      "name": "email-workflow",
      "sequence": ["email-templates", "blackthorn-brand", "gmail_create_draft"],
      "trigger": "Email needed for customer"
    },
    {
      "name": "session-end",
      "sequence": ["dream", "memory-create", "memory-delete"],
      "trigger": "Session end or nightly cron"
    },
    {
      "name": "new-customer",
      "sequence": ["customer-dossier", "kickoff-deck"],
      "trigger": "New customer assigned"
    }
  ],
  "processing_order": []
}
```

### Stage 1b — Determine Processing Order

Based on `--priority`:

| Strategy | Order Logic |
|----------|------------|
| `worst-first` | Run baseline eval on all skills first, then process from lowest pass rate to highest |
| `critical-first` | Process by criticality: orchestrators first (PM, morning-orchestrator), then high-dependency skills (customer-dossier, dream, fathom), then remaining workers, then utilities |
| `alphabetical` | A-Z by skill name |

**`critical-first` ordering (recommended for first sweep):**

```
Tier 1 — Orchestrators (routing correctness affects everything downstream)
  1. project-manager
  2. morning-orchestrator

Tier 2 — High-dependency workers (many skills depend on their output)
  3. customer-dossier      (hard dependency for all customer workflows)
  4. fathom                (primary research source)
  5. dream                 (memory consolidation + EVO proposals)
  6. post-meeting-sweep    (packages findings for PM routing)

Tier 3 — Primary workers
  7. email-templates
  8. com-update
  9. blackthorn-support
  10. kickoff-deck
  11. day-prep-recap
  12. flagged-onboarding-sync
  13. product-feedback-poster
  14. blackthorn-brand

Tier 4 — Utilities
  15. memory-create
  16. memory-delete
  17. process-mistakes
  18. onboarding-process-sync
  19. subfolders
  ...remaining skills
```

### Stage 2 — Individual Skill Evaluation

For each skill in the processing order:

1. Run Phases 1–5 (same as single-skill mode) with the per-skill `--iterations` budget
2. Save results to `outputs/auto-research/<skill-name>/`
3. Track the skill's baseline and final pass rate in the sweep summary

**If `--baseline-only`:** Run Phase 1–3 only (analyze, generate criteria, baseline eval).
No improvement iterations. This produces a "health check" scorecard for the
entire ecosystem.

**Runtime budget:** Each skill gets its own iteration budget (default 5 in sweep
mode). The sweep does NOT share iterations across skills — each skill gets a
fresh budget. This prevents one stubborn skill from consuming all iterations.

**Parallelism note:** Skills within the same tier that have no dependencies on
each other CAN be evaluated in parallel if the runtime supports it. However,
orchestrators (Tier 1) should complete before their downstream skills are
evaluated, because improvements to PM's routing may change how downstream
skills should behave.

### Stage 3 — Cross-Skill Integration Evaluation

After all individual evaluations complete (or if `--integration-only` is passed),
run the integration test suite. This evaluates how skills work **together** —
not in isolation.

Read `references/criteria-templates.md` section "Cross-Skill Integration" for
the full criteria library. The integration eval dynamically selects criteria
based on which chains exist in the dependency graph.

#### 3a — Generate Integration Test Scenarios

Create test scenarios that exercise **complete workflows**, not individual skills.
Each scenario simulates a realistic multi-skill chain from trigger to final output.

**Scenario categories:**

| Category | Count | What it tests |
|----------|-------|--------------|
| Morning workflow | 2–3 | morning-orchestrator → customer-dossier → day-prep-recap full chain |
| Post-meeting flow | 2–3 | post-meeting-sweep → fathom → com-update → email-templates chain |
| Customer lifecycle | 2–3 | New customer → dossier → kickoff-deck → first-meeting → follow-up |
| Escalation paths | 2–3 | Product question → blackthorn-support → product-feedback-poster |
| Session end | 1–2 | dream → memory-create/delete → PM execution of proposed writes |
| Multi-signal routing | 2–3 | PM receives input with multiple simultaneous signals — tests parallel routing and result buffering |
| Error recovery | 1–2 | Skill returns low confidence or fails — tests PM's deepen/re-route logic |

**Integration test case format:**

```json
{
  "id": "IT1",
  "category": "morning_workflow",
  "name": "Full morning brief with flagged account and upcoming kickoff",
  "chain": ["morning-orchestrator", "customer-dossier", "day-prep-recap"],
  "trigger": "7 AM cron fires. Calendar has 3 meetings. One account flagged for follow-up. One new customer with kickoff tomorrow.",
  "simulated_inputs": {
    "morning-orchestrator": "Calendar data with 3 meetings, 1 flagged account",
    "customer-dossier": "SKILL REQUEST from PM after morning-orchestrator surfaces customer names",
    "day-prep-recap": "Aggregated context from dossiers + morning-orchestrator findings"
  },
  "expected_handoffs": [
    "morning-orchestrator SKILL RESULT → PM routes customer names to customer-dossier",
    "customer-dossier SKILL RESULT (x3) → PM buffers all, routes to day-prep-recap",
    "day-prep-recap SKILL RESULT → PM presents consolidated morning brief"
  ],
  "integration_criteria": ["IC1", "IC2", "IC3", "IC5"]
}
```

#### 3b — Generate Integration Criteria

Integration criteria test the **boundaries between skills** — handoffs, data
format compatibility, routing decisions, and collective behavior.

**Core integration criteria (always included):**

| ID | Name | What it tests |
|----|------|--------------|
| IC1 | **SKILL RESULT → SKILL REQUEST compatibility** | When Skill A's output becomes Skill B's input (via PM routing), does Skill B receive what it needs? Does the SKILL RESULT contain all fields that the downstream SKILL REQUEST expects? |
| IC2 | **Dependency ordering** | Does the chain execute in the correct order? Does customer-dossier always run before task-specific skills when a customer is named? |
| IC3 | **Parallel buffering** | When multiple skills run in parallel, does PM buffer all results before presenting? No premature partial output? |
| IC4 | **Confidence-based routing** | When a skill returns Medium/Low confidence, does PM correctly deepen (re-request with more context) or re-route (send to different skill)? |
| IC5 | **Tier 1/2 segregation across chain** | Across the full chain, are all Tier 1 actions executed autonomously and all Tier 2 items collected into a single block at the end? No Tier 2 action executed mid-chain? |
| IC6 | **High-stakes signal propagation** | When any skill in the chain detects a high-stakes signal ("cancel", "not renewing", etc.), does it propagate up to PM and trigger the correct response (transcript pull + Tier 2 escalation) regardless of where in the chain it was detected? |
| IC7 | **No circular handoffs** | Does the chain terminate? Specifically: dream → memory-create doesn't re-trigger dream. product-feedback-poster doesn't loop back to blackthorn-support. |
| IC8 | **Schema consistency** | Do all skills in the chain use the same SKILL RESULT schema? Same field names, same confidence scale, same timestamp format? |
| IC9 | **Graceful degradation** | When one skill in the chain fails or returns empty results, does the chain continue with reduced context rather than halting? Does PM log the gap? |
| IC10 | **Memory routing consistency** | When multiple skills in a chain propose memory writes (dream + customer-dossier + com-update), do they target the correct files without conflicts or duplicates? |

#### 3c — Simulated Chain Execution

For each integration test scenario:

1. **Simulate the trigger** (e.g., 7 AM cron fires with calendar data)
2. **Execute Skill A** with the trigger as input → capture SKILL RESULT
3. **Simulate PM routing** — read PM's routing table, determine what PM would do
   with the SKILL RESULT (accept, deepen, re-route, escalate)
4. **Construct the SKILL REQUEST for Skill B** based on PM's routing decision
   and the actual SKILL RESULT from Skill A
5. **Execute Skill B** → capture SKILL RESULT
6. **Repeat** through the full chain
7. **Evaluate** the complete chain output against integration criteria

**Key difference from individual eval:** Individual eval tests one skill with
mock inputs. Integration eval tests the **actual handoff** — Skill A's real
output becomes Skill B's real input. This catches format mismatches, missing
fields, and assumption gaps that individual evals miss.

#### 3d — Integration Scoring

Integration pass rate is calculated separately from individual skill pass rates:

```
integration_pass_rate = (passed_integration_checks / total_integration_checks) * 100
```

Save to `outputs/auto-research/_sweep/integration-eval.json`.

#### 3e — Integration Improvement (Optional)

If integration failures are found, the system identifies **which skill** needs
to change to fix the handoff. This is different from individual improvement —
the change targets the skill that's producing incompatible output, even if that
skill passes its own individual eval at 100%.

Example: `email-templates` might score 100% individually but fail IC1 because
its SKILL RESULT format doesn't match what `blackthorn-brand` expects as input.
The fix goes in `email-templates` (adjust its output format), not `blackthorn-brand`.

Integration improvements follow the same keep/discard loop but re-run the
integration test suite (not just the individual skill eval) to verify the fix.

### Sweep Output — Ecosystem Scorecard

After all stages complete, generate the ecosystem scorecard at
`outputs/auto-research/_sweep/scorecard.md`:

```markdown
# Auto-Research Sweep — Ecosystem Scorecard
Generated: [timestamp]
Skills evaluated: [N] / [total found]
Skills skipped: [list]

## Individual Skill Results

| Skill | Layer | Baseline | Final | Delta | Iterations | Status |
|-------|-------|----------|-------|-------|------------|--------|
| project-manager | orchestrator | 60.0% | 80.0% | +20.0 | 5 | improved |
| customer-dossier | primary-worker | 73.3% | 86.7% | +13.4 | 4 | improved |
| morning-orchestrator | orchestrator | 83.3% | 91.7% | +8.4 | 3 | improved |
| email-templates | primary-worker | 66.7% | 83.3% | +16.6 | 5 | improved |
| memory-create | utility | 100.0% | 100.0% | 0.0 | 0 | perfect |
| ... | | | | | | |

### Ecosystem Summary
- Average baseline: [X]%
- Average final: [Y]%
- Skills at 90%+: [N]
- Skills below 70%: [N] — [list names]
- Skills unchanged: [N]

## Integration Results

| Chain | Pass Rate | Failing Criteria | Root Cause |
|-------|-----------|-----------------|------------|
| morning-workflow | 80.0% | IC3, IC5 | day-prep-recap presents partial output before all dossiers buffered |
| post-meeting | 90.0% | IC4 | PM doesn't deepen when fathom returns Medium confidence on flagged account |
| email-workflow | 70.0% | IC1, IC8 | email-templates SKILL RESULT uses different field names than blackthorn-brand expects |
| session-end | 100.0% | — | All integration criteria pass |
| ... | | | |

### Integration Summary
- Overall integration pass rate: [X]%
- Chains at 100%: [N] / [total]
- Most common failure: [criterion name] — [description]
- Highest-impact fix: [which skill] — [what change would fix the most integration failures]

## Priority Recommendations

1. **[Highest impact]** Fix [skill] — [specific change]. Would resolve [N] integration failures.
2. **[Second highest]** Improve [skill] — [specific change]. Individual pass rate only [X]%.
3. ...

## Detailed Results
See outputs/auto-research/<skill-name>/ for per-skill data.
See outputs/auto-research/_sweep/ for integration data.
```

### Sweep SKILL RESULT

The sweep returns a consolidated SKILL RESULT to PM:

```
## SKILL RESULT: auto-research (sweep)
Timestamp: [ISO 8601]
Customer: None
Actions taken: Full ecosystem sweep. Evaluated [N] skills individually +
  [N] integration chains. Ran [total] improvement iterations across all skills.

Findings:

  === ECOSYSTEM HEALTH ===
  Average pass rate: [baseline]% → [final]%
  Integration pass rate: [X]%
  Skills improved: [N]
  Skills at risk (below 70%): [list]

  === TOP INTEGRATION FAILURES ===
  [Top 3 integration failures with root cause and recommended fix]

  === HIGHEST-IMPACT IMPROVEMENTS ===
  [Top 3 skill patches that would most improve ecosystem health]

  === FULL SCORECARD ===
  See outputs/auto-research/_sweep/scorecard.md

  === TASKS.md ADDITIONS ===
  - [ ] [AUTO-RESEARCH SWEEP] Review ecosystem scorecard — avg [X]% → [Y]%. See outputs/auto-research/_sweep/scorecard.md
  - [ ] [AUTO-RESEARCH] Fix [skill] integration issue — [description]
  - [ ] [AUTO-RESEARCH] Review [skill] improvement — [baseline]% → [final]%

Confidence: [Based on how many skills were improved and integration health]
Gaps/failures: [Skills that couldn't be evaluated — API dependencies, etc.]
Suggested next: Review scorecard, approve patches, then re-run --integration-only to verify fixes
Flags for Jared: All skill patches require human review (Tier 2). Start with
  highest-impact recommendations in the scorecard.
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
