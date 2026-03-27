# Auto-Research Skill

Autonomous skill improvement using the autoresearch pattern (Karpathy / Saraev),
adapted for Claude Cowork skills.

## What's Here

```
skills/auto-research/
  SKILL.md                          # Main skill definition
  references/
    criteria-templates.md           # Domain-specific evaluation heuristics
    eval-schema.md                  # JSON schemas for criteria, test cases, results

cowork-reference/                   # Reference copy of the Blackthorn OBM plugin
  blackthorn-obm/                   # (read-only — for understanding the skill ecosystem)
```

## How It Works

Auto-research reads a target skill, dynamically generates binary evaluation
criteria and test cases, runs a baseline evaluation, then iteratively improves
the skill — keeping changes only when they raise the pass rate.

First iteration is interactive (user approves). Subsequent iterations run
autonomously. Results return to PM via the standard SKILL RESULT protocol.

## Installation

Copy `skills/auto-research/` to your Cowork workspace's skills directory.
The skill integrates with PM, dream's EVO pass, and PROCESS-LESSONS.md.

## Runtime Data

When auto-research runs, it creates data in:
```
outputs/auto-research/<skill-name>/
```
This includes criteria, test cases, iteration snapshots, and the results log.
