# Research Skill — Blueprint

This is a design doc. The next Claude Code session creates this as a new skill
in the live Cowork workspace at `skills/research/SKILL.md`.

## Sources

- [Anthropic: Don't Build Agents, Build Skills](https://youtu.be/wqH1hTkA6qg)
  — Skills can include scripts, reference documents, and strategy docs.
  Research is the outward-facing complement to brainstorming (inward-facing).
- [The Honesty Gap](https://d-squared70.github.io/ChatGPT-and-Claude-Got-Smarter.-Not-More-Honest.)
  — Show the Source applied to external research. Every finding must be
  labeled EXTRACTED (confirmed in docs) or INFERRED (pattern-based suggestion).
- [ClaudeMem 3-layer pattern](https://github.com/thedotmack/claude-mem)
  — Progressive disclosure: scan → deep dive → verification. Controls token
  usage and prevents premature detail loading.

## Purpose

Brainstorming explores what you want (inward, through dialogue).
Research finds what exists (outward, through investigation).

They are companions:
1. Brainstorming defines the problem
2. Research finds real solutions
3. Brainstorming evaluates the options with you
4. You decide

Research is the system's bridge to the outside world — grounded in real data,
not guesses. It applies the honesty protocol more strictly than any other skill
because its outputs become the foundation for decisions.

---

## Frontmatter

```yaml
---
name: research
description: >
  Evidence-based research using web, docs, GitHub, and available resources.
  Finds real tools, integrations, APIs, MCP servers, and approaches. Labels
  all findings EXTRACTED or INFERRED with sources. Flags unverifiable claims
  as BLANK. Use when brainstorming needs validation, PM identifies a gap,
  or user asks "how could we do X?" or "what tools exist for Y?"
---
```

---

## When PM Routes to Research

- When any skill surfaces a resource gap: "we need a way to do X"
- When brainstorming proposes an approach needing real-world validation
- When user asks "how could we do X?" / "what tools exist for Y?"
- When auto-research recommends a resource type (script, reference, template)
  and PM wants to find the best existing option before building from scratch
- When a product question exceeds blackthorn-support's knowledge

---

## Research Process

### Stage 1: Quick Scan (Low Token Cost)

Surface-level search. Return a summary index without deep-diving into any
single option.

1. Parse the research question from the SKILL REQUEST
2. Identify the research domain (tool comparison, integration approach,
   API capability, process methodology, etc.)
3. Search available sources:
   - Web search for current tools, libraries, services
   - GitHub for repos, MCP servers, Claude skills
   - Documentation sites for specific products
   - Awesome-lists and curated directories
4. Return a **summary index** — one line per option found, with name and
   what it claims to do

**Output format for Stage 1:**
```
Found [N] potential options for [research question].

| # | Option | Category | Claimed Purpose | Source |
|---|--------|----------|-----------------|--------|
| 1 | Tool A | MCP server | Calendar integration | github.com/... |
| 2 | Tool B | API | Calendar + contacts | toolb.com/docs |
| 3 | Tool C | Library | Calendar sync | npmjs.com/... |

Proceeding to deep dive on top [3] candidates.
```

### Stage 2: Deep Dive (Medium Token Cost)

For the top candidates (3-5), read their actual documentation.

1. Fetch and read the README, docs, or product pages
2. Verify claimed features against documentation
3. Check for: last updated date, community adoption (stars, downloads),
   pricing model, maintenance status
4. Note any discrepancies between marketing claims and technical docs

### Stage 3: Verification (Highest Rigor)

Cross-reference claims against multiple sources. This is where the honesty
protocol applies most strictly.

For each finding, determine:
- **EXTRACTED** — directly confirmed in technical documentation, README,
  API reference, or verified source code
- **INFERRED** — suggested by marketing copy, community discussions, or
  related features but not explicitly confirmed in technical docs
- **BLANK** — claimed but could not be verified in available documentation

---

## SKILL RESULT Format

```
## SKILL RESULT: research
Timestamp: [ISO 8601]
Customer: [customer name if customer-specific, else None]
Actions taken: Researched [topic]. Scanned [N] sources. Deep-dived [N]
  candidates. Verified [N] claims.

Findings:

  === RECOMMENDATIONS ===
  | # | Option | What It Is | Why It Fits | Key Features | Source | Confidence | Verification |
  |---|--------|-----------|-------------|--------------|--------|------------|-------------|
  | 1 | [name] | [1-line description] | [why relevant to the question] | [verified features] | [URL] | High | EXTRACTED — confirmed in API docs |
  | 2 | [name] | [1-line description] | [why relevant] | [features] | [URL] | Medium | INFERRED — feature list suggests this, not explicitly documented |
  | 3 | [name] | [1-line description] | [why relevant] | — BLANK | [URL] | Low | Could not verify claimed feature in technical docs |

  === COMPARISON ===
  | Dimension | Option 1 | Option 2 | Option 3 |
  |-----------|----------|----------|----------|
  | Pricing | Free/OSS (EXTRACTED) | $X/mo (EXTRACTED) | Unknown (BLANK) |
  | Last Updated | [date] (EXTRACTED) | [date] (EXTRACTED) | [date] (EXTRACTED) |
  | Community | [N] stars (EXTRACTED) | [N] downloads (EXTRACTED) | — |
  | Maintenance | Active (EXTRACTED) | Stale — last commit 6mo ago (EXTRACTED) | — |
  | Our Use Case Fit | [assessment] (INFERRED) | [assessment] (INFERRED) | — |

  === FLAGS ===
  | Item | Reason |
  |------|--------|
  | Option 3 feature X | Claimed on marketing page but not in API reference |
  | Option 1 pricing | "Free tier" mentioned but limits not documented |

  === VERIFY YOURSELF ===
  - [ ] Test Option 1's [specific feature] — I confirmed the API exists but
        couldn't verify the response format matches our needs
  - [ ] Check Option 2's pricing page — may have changed since my last data
  - [ ] Confirm Option 3 is still maintained — last commit was [date]

  === SOURCES CONSULTED ===
  | Source | Type | Access | Notes |
  |--------|------|--------|-------|
  | [URL] | README | Full | Primary documentation |
  | [URL] | API docs | Full | Feature verification |
  | [URL] | Pricing page | Full | Cost comparison |
  | [URL] | GitHub issues | Partial | Checked open issues for known problems |

Confidence: [High if majority EXTRACTED with multiple source verification;
  Medium if mix of EXTRACTED and INFERRED; Low if mostly INFERRED or BLANK]
Gaps/failures: [What couldn't be researched — paywalled docs, unavailable
  APIs, rate-limited searches, results too old]
Suggested next: [brainstorming to evaluate options | PM to route to
  implementation | specific skill to test integration]
Flags for Jared: [Any recommendations requiring purchase, account signup,
  API key setup, or infrastructure changes — all Tier 2]
```

---

## Honesty Protocol — Strictest Application

Research applies the honesty protocol more strictly than other skills because
its outputs inform decisions:

1. **Every claim needs a source URL.** No "Tool X can do Y" without a link
   to where that capability is documented.

2. **Marketing copy ≠ verified feature.** If a capability is only mentioned
   on marketing pages but not in technical docs, label it INFERRED and flag it.

3. **Version-awareness.** If documentation doesn't specify which version
   supports a feature, note it. Features may exist in paid tiers only.

4. **Recency matters.** Always note when the source was last updated. A README
   from 2024 might describe deprecated features.

5. **"I don't know" is a valid finding.** If research cannot determine whether
   a tool meets a requirement, that's a BLANK with an explanation — not a guess.

---

## Integration with Other Core Skills

### Research ← Brainstorming
Brainstorming says: "We could use an MCP server for calendar integration."
Research goes and finds: which MCP servers exist, what they do, whether
they're maintained, whether they fit the use case.

### Research ← PM
PM identifies a gap: "email-templates needs a validation script."
Research finds: are there existing validation patterns, scripts, or tools
that could be adapted instead of building from scratch?

### Research ← Auto-Research
Auto-research recommends: "blackthorn-support would improve with updated
product docs."
Research finds: where are the latest docs, what format, how to integrate them.

### Research → PM (SKILL RESULT)
All research returns to PM via standard SKILL RESULT. PM evaluates and either:
- Routes recommendations to brainstorming for evaluation
- Presents directly to user for decision
- Flags as Tier 2 if action requires purchases or account setup

---

## Caching and Deduplication

Research should check if the same or similar question has been researched before:

**Check first:** `outputs/research/` for previous research results on the
same topic. If recent (<30 days) and the landscape hasn't changed significantly,
reference the previous research and note what's new.

**Cache results:** Save research outputs to `outputs/research/<topic-slug>/`
with timestamp. Future research on the same topic starts from the previous
findings rather than from scratch.

**Deduplication:** If PM requests research on "calendar MCP servers" and a
previous research run covered "MCP servers for scheduling," note the overlap
and build on the prior work.
