# Portable Skill Operating System — "The Core"

A self-contained, self-improving skill system that can be dropped into any
Claude workspace. As domain-specific skills are added, they automatically
fall under three layers: PM quality auditing, auto-research continuous
improvement, and honesty protocol guardrails.

## Sources

1. [Karpathy's autoresearch](https://github.com/karpathy/autoresearch) — modify → eval → keep/discard → repeat
2. [Nick Saraev's adaptation](https://youtu.be/qKU-e0x2EmE) — binary eval criteria for Claude skills
3. [The Honesty Gap](https://d-squared70.github.io/ChatGPT-and-Claude-Got-Smarter.-Not-More-Honest.) — Force Blank, Penalize Guessing, Show the Source
4. [Anthropic: Don't Build Agents, Build Skills](https://youtu.be/wqH1hTkA6qg) — scripts, references, templates, progressive disclosure
5. [Superpowers](https://github.com/obra/superpowers) — verification gates, TDD for skills, hard gates
6. [ClaudeMem](https://github.com/thedotmack/claude-mem) — structured observations, progressive disclosure, memory decay
7. [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) — CSV-as-database, reasoning rules as data, pre-delivery checklists

## The Portable Core (6 Pieces)

| Piece | Role |
|-------|------|
| **project-manager** | Routes, audits quality, maintains health ledger, runs output validation, surfaces resource gaps |
| **auto-research** | Measures, improves, runs the continuous feedback loop, escalates persistent issues to PM |
| **brainstorming** | Explores requirements through dialogue — the "think first" gate before building anything |
| **research** | Goes outward for real-world evidence — tools, APIs, docs, verified recommendations |
| **honesty protocol** | Guardrail: Force Blank, Penalize Guessing, Show the Source — embedded in ALL skills |
| **subfolders** | Self-organizing structure — creates dirs as needed, propagates awareness to all workspace files |

## What's Here

```
skills/auto-research/
  SKILL.md                              # Main auto-research skill (built)
  references/
    criteria-templates.md               # Domain-specific evaluation heuristics
    eval-schema.md                      # JSON schemas for criteria, test cases, results

blueprints/                             # Design docs for the next implementation session
  honesty-protocol.md                   # Three rules + CSM inference nuance
  health-ledger.md                      # PM quality observation tracking
  research-skill.md                     # New research skill design
  subfolders-core.md                    # Subfolders additions + awareness propagation
  auto-research-upgrades.md             # Honesty criterion, health ledger, TDD framing
  brainstorming-upgrades.md             # Hard gate, single-question, research handoff
  skill-audit-template.md              # Per-skill audit checklist, prioritized by risk
  output-validation.md                  # Independent validation pass on all outputs

cowork-reference/                       # Reference copy of the Blackthorn OBM plugin
  blackthorn-obm/                       # (read-only — 27 skills for understanding the ecosystem)
```

## Three Layers

### Layer 1: PM as Quality Auditor
PM routes work AND monitors output quality. After every skill chain:
- Runs output validation (Level 1/2/3 depending on risk)
- Logs observations to the health ledger
- Surfaces resource recommendations ("this skill would work better if it had X")

### Layer 2: Auto-Research as the Immune System
Continuous evaluation and improvement loop:
- Consumes PM's health ledger as input signal
- Generates targeted criteria based on observed failures
- Iterates improvements using TDD pattern (RED/GREEN/REFACTOR)
- Escalates persistent issues back to PM

### Layer 3: Honesty Protocol as the Guardrail
Three rules enforced across ALL skills:
1. Force Blank — ambiguous values left blank with explanation
2. Penalize Guessing — wrong answer is 3x worse than blank
3. Show the Source — EXTRACTED vs INFERRED with evidence trail

Inference backed by evidence is valuable and kept. Unsupported guessing is caught.

## The Feedback Loop

```
Skills produce output (with honesty labels)
        ↓
PM validates output (Level 1/2/3)
        ↓
PM presents to user (with validation status)
        ↓
PM logs observations to health ledger
        ↓
Auto-research reads health ledger → generates criteria
        ↓
Auto-research improves skill → verifies improvement
        ↓
PM confirms resolution → or escalates to user (Tier 2)
```

## Runtime Data

```
outputs/
  auto-research/<skill-name>/           # Per-skill eval data
  auto-research/_sweep/                 # Sweep-level data and ecosystem scorecard
  health-ledger/observations.jsonl      # PM quality observations (append-only)
  research/<topic-slug>/                # Research skill cached findings
```

## Installation

1. Copy the portable core skills to your workspace's skills directory
2. Read blueprints/ for implementation guidance on each piece
3. Start with `--sweep --baseline-only` to measure before changing anything
