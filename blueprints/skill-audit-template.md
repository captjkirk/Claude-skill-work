# Skill Architecture Audit Template — Blueprint

This is a design doc. The next Claude Code session uses this template to audit
each skill in the live Cowork workspace, prioritized by customer-facing risk.

## Sources

- [Anthropic: Don't Build Agents, Build Skills](https://youtu.be/wqH1hTkA6qg)
  — Progressive disclosure, scripts as tools, reference documents, templates,
  frontmatter tuning. Keep SKILL.md under 500 lines.
- [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
  — CSV-as-database with search scripts, reasoning rules as data,
  pre-delivery checklists, Master+Overrides pattern.
- [Superpowers](https://github.com/obra/superpowers) — Skill descriptions
  should describe triggering conditions ("Use when..."), not process summaries.
  Keep frequently-loaded skills under 200 words.

---

## Audit Checklist (Per Skill)

Run this checklist against every skill. Record findings in the audit table.

### A. Size & Progressive Disclosure

- [ ] **Line count under 500?** Count the lines in SKILL.md.
  - If over 500 → recommend split into SKILL.md + reference/ files
  - If over 800 → strongly recommend split — performance degrades
  - Rule: SKILL.md contains core instructions. Reference/ contains domain
    knowledge, detailed examples, lookup tables, and context that's only
    needed for specific scenarios.

- [ ] **Frequently-loaded content under 200 words?** The description and
  any content that loads on every invocation should be concise.

- [ ] **Reference material separated?** Large lookup tables, product docs,
  process descriptions — are they in reference/ or embedded in SKILL.md?
  - Pattern from UI/UX Pro Max: Move data to CSV files + search scripts
    for reference-heavy skills (blackthorn-support product docs, email
    template catalog, brand guidelines)

### B. Validation & Quality Assurance

- [ ] **Produces structured output?** (tables, field/value pairs, COM updates,
  email drafts, dossier entries)
  - If yes → should have `scripts/validate.py` or equivalent
  - Validation script checks output before presenting:
    dates are real, names match dossier, required fields present,
    no fabricated details

- [ ] **Has feedback loop?** For skills that produce output requiring
  verification:
  ```
  Generate output → Run validate.py → Fix if errors → Re-validate → Present
  ```
  This "make-check-fix-recheck" pattern (from Anthropic talk) catches errors
  before they reach the user.

- [ ] **Pre-delivery checklist present?** For content-producing skills:
  - [ ] All values labeled EXTRACTED/INFERRED (honesty protocol)
  - [ ] All BLANK fields have Flags entries
  - [ ] Format matches expected template
  - [ ] Required fields present
  - [ ] Confidence calibrated to evidence quality

### C. Output Templates

- [ ] **Templates extracted from prose?** If the skill has specific output
  formats, are they in standalone `templates/` files or embedded in the
  SKILL.md prose?
  - Extract to `templates/` for reusability and clarity

- [ ] **Template freedom level classified?**
  | Level | When to Use | Example |
  |-------|------------|---------|
  | **Strict** (exact format) | Fragile operations, external-facing content, COM updates | COM field update table must match Salesforce schema exactly |
  | **Medium** (preferred structure) | Internal reports, dossier updates | Morning brief has preferred sections but can adapt |
  | **Flexible** (guidance only) | Analysis, brainstorming output | Research findings can be structured as fits the content |

### D. Frontmatter & Discovery

- [ ] **Description under 250 characters?** Longer descriptions get truncated
  and hurt discovery.

- [ ] **Description starts with triggering conditions?** Not "This skill
  processes..." but "Use when [trigger]. Handles [capability]."
  (From Superpowers skill-writing framework)

- [ ] **Keywords for discovery?** Does the description include the terms
  users and PM would use when looking for this capability?

- [ ] **Frontmatter options set?**
  | Option | When to Set |
  |--------|------------|
  | `allowed-tools` | If the skill needs specific tools pre-authorized |
  | `context: fork` | If the skill is heavy and should run in an isolated subagent |
  | `paths` | If the skill should auto-activate on specific file patterns |
  | `disable-model-invocation: true` | If the skill has side effects and should only run when explicitly invoked |

### E. Honesty Protocol

- [ ] **Honesty protocol referenced?** Does the skill include:
  ```markdown
  ## Honesty Protocol
  Read and follow `skills/core/honesty-protocol.md` for all outputs.
  ```

- [ ] **Source labels in output?** Does the SKILL RESULT include
  EXTRACTED/INFERRED labels on values?

- [ ] **Flags table for blanks?** When the skill can't determine a value,
  does it leave it BLANK with an explanation?

- [ ] **Confidence calibrated?** Does the skill's confidence assessment
  match the evidence quality guidelines from the honesty protocol?

### F. Cross-Skill Integration

- [ ] **SKILL RESULT format correct?** All required fields present
  (Timestamp, Customer, Actions taken, Findings, Confidence, Gaps/failures,
  Suggested next, Flags for Jared)?

- [ ] **"Suggested next" references real skills?** By correct name?

- [ ] **Tier 1/2 classification correct?** External sends and irreversible
  actions are Tier 2? Internal operations are Tier 1?

- [ ] **Upstream compatibility?** If this skill receives input from another
  skill's output, does it handle the expected format?

- [ ] **Downstream compatibility?** Does this skill's output contain
  everything downstream skills need?

---

## Priority Order

Audit skills in this order, based on customer-facing risk and frequency of use.

### Priority 1: Customer-Facing Content (Highest Risk)

These skills produce output that customers or colleagues may see. Wrong
information here has the highest blast radius.

| # | Skill | Key Risks | Audit Focus |
|---|-------|-----------|-------------|
| 1 | **email-templates** | Fabricated dates, wrong commitments, tone mismatch | Validation script for dates/names, honesty protocol, voice template |
| 2 | **com-update** | Wrong Salesforce field values visible to whole team | Validation against dossier, strict output template, honesty labels |
| 3 | **customer-dossier** | Foundation for all customer work — errors cascade | Staleness detection, field completeness, honesty protocol |
| 4 | **blackthorn-support** | Product misinformation to customers | Source attribution, confidence escalation, reference doc freshness |

### Priority 2: Daily Context (High Risk)

These skills set the context for the day's work. Wrong context leads to
wrong decisions across every subsequent interaction.

| # | Skill | Key Risks | Audit Focus |
|---|-------|-----------|-------------|
| 5 | **day-prep-recap** | Morning brief with wrong meeting details or stale context | Honesty labels on all prep data, calendar verification |
| 6 | **fathom** | Meeting outcomes presented as fact when they're AI summaries | EXTRACTED (transcript quotes) vs INFERRED (AI summaries), cache freshness |
| 7 | **post-meeting-sweep** | Missing action items, wrong customer attribution | Cross-reference against calendar, Fathom verification |

### Priority 3: Orchestration Hub (Cascading Impact)

PM routing errors affect every downstream skill.

| # | Skill | Key Risks | Audit Focus |
|---|-------|-----------|-------------|
| 8 | **project-manager** | Wrong routing, missed signals, premature presentation | Routing table accuracy, signal detection, parallel buffering, Tier 1/2 |
| 9 | **morning-orchestrator** | Missing calendar events, wrong customer identification | Calendar API reliability, customer name extraction |

### Priority 4: Memory & Learning (Long-term Impact)

Errors in memory skills persist and compound over time.

| # | Skill | Key Risks | Audit Focus |
|---|-------|-----------|-------------|
| 10 | **dream** | Writing wrong facts to dossiers, over-pruning, EVO false positives | Source attribution on all writes, pruning evidence, EVO quality |
| 11 | **memory-create** | Wrong target file, duplicate entries, contradictions | File routing, dedup check, contradiction detection |
| 12 | **memory-delete** | Deleting valid entries, wrong file targeting | Confirmation requirement, evidence for deletion |
| 13 | **process-mistakes** | Logging wrong lessons that skew future behavior | Accuracy of failure description and corrected approach |

### Priority 5: Specialized Skills (Lower Frequency)

| # | Skill | Key Risks | Audit Focus |
|---|-------|-----------|-------------|
| 14 | **flagged-onboarding-sync** | Wrong COM updates for flagged accounts | Same as com-update, plus Emily/Ashley format requirements |
| 15 | **product-feedback-poster** | Duplicate Slack posts, wrong customer context | PFQE log dedup, customer attribution, Tier 2 enforcement |
| 16 | **kickoff-deck** | Wrong customer details in deck, outdated template | Dossier verification, template freshness |
| 17 | **blackthorn-brand** | Off-brand content reaching customers | Brand guidelines as reference doc, voice profile verification |

### Priority 6: Utility & Infrastructure (Lowest Risk)

| # | Skill | Audit Focus |
|---|-------|-------------|
| 18 | **subfolders** | Awareness propagation (new addition from blueprints) |
| 19 | **onboarding-process-sync** | Drive sync reliability |
| 20 | **schedule** | Cron format accuracy, task execution |
| 21 | **begin** | One-time setup — verify still current |
| 22-26 | **docx, pdf, pptx, xlsx, brainstorming** | Standard audit checklist |
| 27 | **skill-creator** | Meta — audit last since it creates other skills |

---

## Audit Results Table

For each skill, fill in this table during the audit:

```markdown
## Skill: [name]

| Check | Status | Finding | Recommendation |
|-------|--------|---------|----------------|
| Line count | [ ] | [N] lines | [Split needed? Y/N] |
| Progressive disclosure | [ ] | [Reference material separated?] | [What to move] |
| Validation script | [ ] | [Has one? Needs one?] | [What to validate] |
| Feedback loop | [ ] | [Present?] | [What to add] |
| Pre-delivery checklist | [ ] | [Present?] | [What to add] |
| Templates extracted | [ ] | [In prose or separate?] | [What to extract] |
| Description quality | [ ] | [Length, triggers, keywords] | [Rewrite needed?] |
| Frontmatter options | [ ] | [What's set?] | [What to add] |
| Honesty protocol | [ ] | [Referenced? Implemented?] | [What's missing] |
| SKILL RESULT format | [ ] | [All fields present?] | [What's missing] |
| Cross-skill compat | [ ] | [Upstream/downstream OK?] | [What breaks] |

### Summary
- **Overall health:** [Good / Needs Work / Critical]
- **Top 3 fixes (prioritized):**
  1. [Most impactful fix]
  2. [Second most impactful]
  3. [Third most impactful]
- **Estimated effort:** [Quick fix / Moderate / Major rework]
```

---

## How to Use This Audit

1. **Start with Priority 1 skills** — highest customer-facing risk
2. **Fill in the audit table** for each skill
3. **Implement fixes** for Priority 1 before moving to Priority 2
4. **Run auto-research** after fixing each skill to measure improvement
5. **Log findings** to PM's health ledger for tracking
6. **Repeat** for each priority tier

The audit is not a one-time event. After the initial pass, auto-research
handles ongoing monitoring. But the initial audit establishes the baseline
and identifies the biggest gaps that auto-research should target first.
