# Skill Architecture Audit Template

Run this checklist against every skill. Prioritize by customer-facing risk.

---

## Audit Checklist

### A. Size & Progressive Disclosure

- [ ] Line count under 500? (Over 500 → split. Over 800 → strongly split.)
- [ ] Frequently-loaded content under 200 words?
- [ ] Reference material in reference/ or embedded in SKILL.md?
  - Large tables, product docs, process descriptions → move to reference/
  - Pattern: CSV files + search scripts for reference-heavy skills

### B. Validation & Quality

- [ ] Produces structured output? → Should have `scripts/validate.py`
- [ ] Has feedback loop? (generate → validate → fix → re-validate → present)
- [ ] Pre-delivery checklist present? (honesty labels, format, confidence)

### C. Output Templates

- [ ] Templates extracted from prose into `templates/` files?
- [ ] Freedom level classified?
  - **Strict** — exact format (COM updates, Salesforce fields)
  - **Medium** — preferred structure (morning brief, dossier updates)
  - **Flexible** — guidance only (analysis, research findings)

### D. Frontmatter & Discovery

- [ ] Description under 250 characters?
- [ ] Starts with triggering conditions? ("Use when..." not "This skill...")
- [ ] Keywords match what users/PM would search for?
- [ ] Frontmatter options set? (allowed-tools, context: fork, paths, disable-model-invocation)

### E. Honesty Protocol

- [ ] References `skills/core/honesty-protocol.md`?
- [ ] Output includes EXTRACTED/INFERRED labels?
- [ ] BLANK fields have Flags table?
- [ ] Confidence calibrated to evidence quality?

### F. Cross-Skill Integration

- [ ] SKILL RESULT has all required fields?
- [ ] "Suggested next" references real skills by correct name?
- [ ] Tier 1/2 classification correct?
- [ ] Upstream format handled? (receives expected input)
- [ ] Downstream compatibility? (provides what next skill needs)

---

## Priority Order

### Priority 1: Customer-Facing Content (Highest Risk)

| # | Skill | Key Risks | Focus |
|---|-------|-----------|-------|
| 1 | email-templates | Fabricated dates, wrong commitments | Validation script, honesty protocol |
| 2 | com-update | Wrong Salesforce values visible to team | Validation against dossier |
| 3 | customer-dossier | Errors cascade to all customer work | Staleness detection, completeness |
| 4 | blackthorn-support | Product misinformation | Source attribution, confidence escalation |

### Priority 2: Daily Context (High Risk)

| # | Skill | Key Risks | Focus |
|---|-------|-----------|-------|
| 5 | day-prep-recap | Wrong meeting details, stale context | Honesty labels, calendar verification |
| 6 | fathom | AI summaries presented as fact | EXTRACTED vs INFERRED distinction |
| 7 | post-meeting-sweep | Missing action items | Cross-reference calendar + Fathom |

### Priority 3: Orchestration (Cascading Impact)

| # | Skill | Key Risks | Focus |
|---|-------|-----------|-------|
| 8 | project-manager | Wrong routing, missed signals | Routing accuracy, Tier 1/2 |
| 9 | morning-orchestrator | Missing events | Calendar extraction |

### Priority 4: Memory & Learning (Long-term)

| # | Skill | Focus |
|---|-------|-------|
| 10 | dream | Source attribution on writes, pruning evidence |
| 11 | memory-create | File routing, dedup, contradictions |
| 12 | memory-delete | Confirmation, evidence for deletion |
| 13 | process-mistakes | Accuracy of failure description |

### Priority 5: Specialized

| # | Skill | Focus |
|---|-------|-------|
| 14 | flagged-onboarding-sync | Same as com-update + format |
| 15 | product-feedback-poster | Dedup, customer attribution |
| 16 | kickoff-deck | Dossier verification |
| 17 | blackthorn-brand | Brand guidelines |

### Priority 6: Utility & Infrastructure

| # | Skill | Focus |
|---|-------|-------|
| 18-27 | subfolders, onboarding-process-sync, schedule, begin, docx, pdf, pptx, xlsx, brainstorming, skill-creator | Standard checklist |

---

## Per-Skill Audit Results

```markdown
## Skill: [name]

| Check | Status | Finding | Recommendation |
|-------|--------|---------|----------------|
| Line count | [ ] | [N] lines | [Split needed?] |
| Progressive disclosure | [ ] | [Separated?] | [What to move] |
| Validation script | [ ] | [Has/needs one?] | [What to validate] |
| Feedback loop | [ ] | [Present?] | [What to add] |
| Pre-delivery checklist | [ ] | [Present?] | [Add from honesty-protocol.md] |
| Templates | [ ] | [In prose or separate?] | [What to extract] |
| Description | [ ] | [Length, triggers] | [Rewrite?] |
| Frontmatter | [ ] | [Options set?] | [What to add] |
| Honesty protocol | [ ] | [Referenced?] | [What's missing] |
| SKILL RESULT | [ ] | [Fields present?] | [What's missing] |
| Cross-skill | [ ] | [Compatible?] | [What breaks] |

### Summary
- **Health:** [Good / Needs Work / Critical]
- **Top 3 fixes:**
  1. [Most impactful]
  2. [Second]
  3. [Third]
- **Effort:** [Quick fix / Moderate / Major rework]
```

---

## Usage

1. Start with Priority 1 — highest customer-facing risk
2. Fill in audit table per skill
3. Implement fixes for Priority 1 before moving to 2
4. Run auto-research after each fix to measure improvement
5. Log findings to health ledger
6. Repeat per tier

After initial pass, auto-research handles ongoing monitoring. The audit
establishes the baseline and identifies the biggest gaps.
