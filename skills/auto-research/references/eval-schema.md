# Evaluation Schemas

JSON schemas for auto-research runtime data. These are compatible with the
skill-creator's eval framework where applicable.

---

## criteria.json

Generated in Phase 2. Contains 3–6 binary evaluation criteria.

```json
{
  "skill_name": "email-templates",
  "skill_path": "skills/email-templates/SKILL.md",
  "domain": "content-generation",
  "hierarchy_layer": "primary-worker",
  "generated_at": "2026-03-27T10:00:00Z",
  "criteria": [
    {
      "id": "C1",
      "name": "SKILL RESULT Schema Compliance",
      "description": "Output contains all required SKILL RESULT fields (Timestamp, Customer, Actions taken, Findings, Confidence, Gaps/failures, Suggested next, Flags for Jared)",
      "evaluation_prompt": "Does the output contain a properly formatted SKILL RESULT block with all required fields? Answer PASS or FAIL with one sentence justification.",
      "source": "universal"
    },
    {
      "id": "C2",
      "name": "Email Format Compliance",
      "description": "Draft includes subject line, recipients (To/CC), and full HTML body",
      "evaluation_prompt": "Does the output include a complete email draft with subject, recipients, and HTML body? Answer PASS or FAIL.",
      "source": "domain-heuristic"
    },
    {
      "id": "C3",
      "name": "No Hallucinated Details",
      "description": "Email content only references facts present in the input context",
      "evaluation_prompt": "Does the email contain any customer details, dates, or commitments not present in the input? Any fabrication is a FAIL.",
      "source": "domain-heuristic"
    },
    {
      "id": "C4",
      "name": "Template Matching",
      "description": "Skill checks for a matching template before drafting freehand",
      "evaluation_prompt": "Does the output indicate that existing templates were checked before drafting? Drafting from scratch without template lookup is a FAIL.",
      "source": "process-lesson"
    }
  ]
}
```

### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `skill_name` | string | yes | Name from the target skill's frontmatter |
| `skill_path` | string | yes | Path to the target SKILL.md |
| `domain` | string | yes | One of: `orchestration`, `customer-research`, `content-generation`, `memory-management`, `product-knowledge`, `utility` |
| `hierarchy_layer` | string | yes | One of: `orchestrator`, `primary-worker`, `chained-skill`, `utility` |
| `generated_at` | string | yes | ISO 8601 timestamp |
| `criteria[]` | array | yes | 3–6 criterion objects |
| `criteria[].id` | string | yes | Unique ID (C1, C2, ...) |
| `criteria[].name` | string | yes | Short descriptive name |
| `criteria[].description` | string | yes | What this criterion checks |
| `criteria[].evaluation_prompt` | string | yes | Question to ask when evaluating (must end with PASS/FAIL instruction) |
| `criteria[].source` | string | yes | One of: `universal`, `domain-heuristic`, `evo-proposal`, `process-lesson`, `cross-skill` |

---

## test-cases.json

Generated in Phase 2. Contains 5–10 test scenarios.

```json
{
  "skill_name": "email-templates",
  "test_cases": [
    {
      "id": "T1",
      "category": "happy_path",
      "name": "Standard follow-up email after kickoff call",
      "input": "## SKILL REQUEST: email-templates\nTimestamp: 2026-03-27T14:00:00Z\nFrom: PM\nReason: Post-kickoff follow-up needed\nCustomer: Acme Corp\nSpecific request: Draft follow-up email after kickoff call. Key points: timeline confirmed (4 weeks), main contact is Sarah Chen, next step is technical review session.\nContext: Customer is in Week 1 of onboarding. CSM is Jared. AE was Mike.",
      "context": "Customer dossier exists with current phase 'Kickoff'. MEMORY.md has Jared's email voice profile loaded.",
      "description": "Tests the most common use case — post-meeting follow-up with rich context"
    },
    {
      "id": "T2",
      "category": "edge_case",
      "name": "Email request with minimal context",
      "input": "## SKILL REQUEST: email-templates\nTimestamp: 2026-03-27T14:00:00Z\nFrom: PM\nReason: Email needed\nCustomer: Unknown Co\nSpecific request: Send a check-in email.\nContext: No prior interaction data.",
      "context": "No customer dossier exists. No recent interactions in Gmail or Fathom.",
      "description": "Tests behavior when context is sparse — should flag gaps, not fabricate details"
    }
  ]
}
```

### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `skill_name` | string | yes | Target skill name |
| `test_cases[]` | array | yes | 5–10 test case objects |
| `test_cases[].id` | string | yes | Unique ID (T1, T2, ...) |
| `test_cases[].category` | string | yes | One of: `happy_path`, `edge_case`, `cross_skill`, `known_failure` |
| `test_cases[].name` | string | yes | Descriptive name |
| `test_cases[].input` | string | yes | Simulated $ARGUMENTS or SKILL REQUEST |
| `test_cases[].context` | string | yes | Simulated workspace state (dossiers, memory, etc.) |
| `test_cases[].description` | string | yes | What this test case reveals |

---

## eval-output.json

Generated in Phase 3 (and each subsequent iteration). Full evaluation results.

```json
{
  "iteration": 0,
  "timestamp": "2026-03-27T10:05:00Z",
  "skill_snapshot_path": "outputs/auto-research/email-templates/iterations/000/skill-snapshot.md",
  "pass_rate": 66.7,
  "total_checks": 24,
  "passed": 16,
  "failed": 8,
  "word_count": 342,
  "results": [
    {
      "test_case": "T1",
      "criterion": "C1",
      "result": "PASS",
      "justification": "SKILL RESULT contains all required fields with correct formatting."
    },
    {
      "test_case": "T1",
      "criterion": "C3",
      "result": "FAIL",
      "justification": "Email references a 'technical review session next Tuesday' — no specific date was in the input context."
    }
  ],
  "failure_patterns": [
    "C3 (No Hallucinated Details) fails in 3/6 test cases — skill tends to invent specific dates and meeting types",
    "C4 (Template Matching) fails in 2/6 test cases — skill drafts freehand on edge cases without checking templates first"
  ],
  "criterion_pass_rates": {
    "C1": 100.0,
    "C2": 83.3,
    "C3": 50.0,
    "C4": 66.7
  }
}
```

### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `iteration` | number | yes | 0 = baseline, 1+ = improvement iterations |
| `timestamp` | string | yes | ISO 8601 |
| `skill_snapshot_path` | string | yes | Path to the skill version that was evaluated |
| `pass_rate` | number | yes | (passed / total_checks) * 100, one decimal |
| `total_checks` | number | yes | test_cases * criteria |
| `passed` | number | yes | Total PASS results |
| `failed` | number | yes | Total FAIL results |
| `word_count` | number | yes | Word count of the skill at this iteration |
| `results[]` | array | yes | One entry per (test_case, criterion) pair |
| `results[].test_case` | string | yes | Test case ID |
| `results[].criterion` | string | yes | Criterion ID |
| `results[].result` | string | yes | "PASS" or "FAIL" |
| `results[].justification` | string | yes | One-sentence explanation |
| `failure_patterns` | array | yes | Human-readable pattern descriptions |
| `criterion_pass_rates` | object | yes | Pass rate per criterion across all test cases |

---

## results.tsv

Append-only iteration log. Tab-separated, one row per iteration.

```
iteration	timestamp	pass_rate	delta	word_count	status	description
0	2026-03-27T10:05:00Z	66.7	0.0	342	baseline	Initial evaluation
1	2026-03-27T10:08:00Z	75.0	+8.3	358	keep	Added instruction to always check templates before drafting
2	2026-03-27T10:11:00Z	66.7	-8.3	372	discard	Restructured output format section — caused regression
3	2026-03-27T10:14:00Z	83.3	+8.3	361	keep	Added constraint against fabricating specific dates
```

### Column Reference

| Column | Description |
|--------|-------------|
| `iteration` | 0 = baseline, 1+ = improvement iterations |
| `timestamp` | ISO 8601 |
| `pass_rate` | Percentage, one decimal |
| `delta` | Change from previous best (+ or -) |
| `word_count` | Skill word count at this iteration |
| `status` | `baseline`, `keep`, or `discard` |
| `description` | One-line summary of the change attempted |

---

## Sweep Mode Schemas

### discovery.json

Generated in Stage 1 of sweep mode. Maps the full skill ecosystem.

```json
{
  "timestamp": "2026-03-27T10:00:00Z",
  "sweep_dir": "skills/",
  "skills_found": 26,
  "skills_skipped": ["schedule"],
  "dependency_graph": {
    "<skill-name>": {
      "layer": "orchestrator | primary-worker | chained-skill | utility",
      "invokes": ["skill-a", "skill-b"],
      "invoked_by": ["skill-c"],
      "criticality": "critical | high | medium | low",
      "note": "Optional context"
    }
  },
  "chains": [
    {
      "name": "descriptive-chain-name",
      "sequence": ["skill-a", "skill-b", "skill-c"],
      "trigger": "What initiates this chain"
    }
  ],
  "processing_order": ["project-manager", "morning-orchestrator", "customer-dossier", "..."]
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `timestamp` | string | yes | ISO 8601 |
| `sweep_dir` | string | yes | Directory that was scanned |
| `skills_found` | number | yes | Total SKILL.md files found |
| `skills_skipped` | array | yes | Skills excluded via `--skip` |
| `dependency_graph` | object | yes | Keyed by skill name |
| `dependency_graph.<name>.layer` | string | yes | Hierarchy classification |
| `dependency_graph.<name>.invokes` | array | yes | Skills this skill calls |
| `dependency_graph.<name>.invoked_by` | array | yes | Skills that call this one |
| `dependency_graph.<name>.criticality` | string | yes | Impact rating |
| `chains` | array | yes | Named multi-skill workflows |
| `processing_order` | array | yes | Order skills will be evaluated |

---

### integration-test-cases.json

Generated in Stage 3a. Test scenarios for multi-skill chains.

```json
{
  "test_cases": [
    {
      "id": "IT1",
      "category": "morning_workflow",
      "name": "Full morning brief with flagged account",
      "chain": ["morning-orchestrator", "customer-dossier", "day-prep-recap"],
      "trigger": "7 AM cron fires with 3 meetings, 1 flagged account",
      "simulated_inputs": {
        "morning-orchestrator": "Calendar data...",
        "customer-dossier": "SKILL REQUEST from PM with customer names...",
        "day-prep-recap": "Aggregated dossier context..."
      },
      "expected_handoffs": [
        "morning-orchestrator → PM routes customers to customer-dossier",
        "customer-dossier results buffered → PM routes to day-prep-recap"
      ],
      "integration_criteria": ["IC1", "IC2", "IC3", "IC5"]
    }
  ]
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `test_cases[].id` | string | yes | Unique ID (IT1, IT2, ...) |
| `test_cases[].category` | string | yes | One of: `morning_workflow`, `post_meeting`, `customer_lifecycle`, `escalation_path`, `session_end`, `multi_signal`, `error_recovery` |
| `test_cases[].chain` | array | yes | Ordered list of skills in the chain |
| `test_cases[].trigger` | string | yes | What initiates the chain |
| `test_cases[].simulated_inputs` | object | yes | Keyed by skill name — the input each skill receives |
| `test_cases[].expected_handoffs` | array | yes | Human-readable description of each handoff |
| `test_cases[].integration_criteria` | array | yes | Which IC criteria to evaluate against |

---

### integration-eval.json

Generated in Stage 3c. Full integration evaluation results.

```json
{
  "timestamp": "2026-03-27T12:00:00Z",
  "integration_pass_rate": 80.0,
  "total_checks": 40,
  "passed": 32,
  "failed": 8,
  "chain_results": {
    "morning-workflow": {
      "pass_rate": 83.3,
      "failing_criteria": ["IC3"],
      "root_cause": "day-prep-recap presents before all dossiers buffered"
    },
    "post-meeting": {
      "pass_rate": 75.0,
      "failing_criteria": ["IC4", "IC6"],
      "root_cause": "PM doesn't deepen when fathom returns Medium on flagged account"
    }
  },
  "results": [
    {
      "test_case": "IT1",
      "criterion": "IC1",
      "chain_step": "morning-orchestrator → customer-dossier",
      "result": "PASS",
      "justification": "All customer names present in SKILL RESULT"
    }
  ],
  "criterion_pass_rates": {
    "IC1": 90.0,
    "IC2": 100.0,
    "IC3": 70.0,
    "IC4": 60.0
  },
  "fix_recommendations": [
    {
      "priority": 1,
      "target_skill": "project-manager",
      "issue": "IC4 failures — PM doesn't deepen on Medium confidence for flagged accounts",
      "proposed_fix": "Add explicit rule: if customer is flagged AND confidence < High, always deepen",
      "impact": "Would fix 3 integration test failures"
    }
  ]
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `integration_pass_rate` | number | yes | Overall integration pass rate |
| `chain_results` | object | yes | Per-chain pass rates and failure analysis |
| `chain_results.<name>.failing_criteria` | array | yes | Which IC criteria failed |
| `chain_results.<name>.root_cause` | string | yes | Why the chain fails |
| `results[]` | array | yes | Per (test case, criterion) results |
| `results[].chain_step` | string | yes | Which handoff in the chain this tests |
| `criterion_pass_rates` | object | yes | Pass rate per IC criterion |
| `fix_recommendations` | array | yes | Prioritized list of fixes |

---

### scorecard.md

Generated at the end of sweep mode. Human-readable ecosystem health report.
See SKILL.md "Sweep Output — Ecosystem Scorecard" section for the full template.

This is a markdown file, not JSON. It's designed to be read by the user and
referenced by PM in the SKILL RESULT.

Location: `outputs/auto-research/_sweep/scorecard.md`

---

## Compatibility with skill-creator

Auto-research uses a simplified version of skill-creator's eval framework:

| skill-creator concept | auto-research equivalent |
|---|---|
| `evals/evals.json` | `test-cases.json` (similar structure, adapted for SKILL REQUEST format) |
| `eval_metadata.json` per test | Embedded in `eval-output.json` |
| `grading.json` | Embedded in `eval-output.json` results array |
| `benchmark.json` | `results.tsv` (simpler — one skill, iteration over time) |
| `feedback.json` | Not used — auto-research evaluates autonomously |

If the user wants to do a deep human-in-the-loop review of an auto-research
run, they can use skill-creator's eval viewer by pointing it at the
`outputs/auto-research/<skill-name>/iterations/<N>/` directory.
