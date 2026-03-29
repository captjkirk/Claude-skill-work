---
name: research
description: >
  Evidence-based research using web, docs, GitHub, and available resources.
  Finds real tools, integrations, APIs, MCP servers, and approaches. Labels
  all findings EXTRACTED or INFERRED with sources. Flags unverifiable claims
  as BLANK. Use when brainstorming needs validation, PM identifies a gap,
  or user asks "how could we do X?" or "what tools exist for Y?"
---

# Research — Evidence-Based Investigation

Brainstorming explores what you want (inward, through dialogue).
Research finds what exists (outward, through investigation).

Research is the system's bridge to the outside world — grounded in real data,
not guesses. It applies the honesty protocol more strictly than any other skill.

---

## Honesty Protocol
Follow `skills/core/honesty-protocol.md` for all outputs.
Label all findings EXTRACTED or INFERRED with evidence and source URLs.
Leave unverifiable claims BLANK with Flags entry.
A wrong answer is 3x worse than a blank.

**Additional research-specific rules:**
- Every claim needs a source URL. No "Tool X can do Y" without a link.
- Marketing copy is NOT verified documentation. Label it INFERRED and flag it.
- Note when source was last updated. A 2024 README may describe deprecated features.
- Version-awareness: features may exist in paid tiers only — note it.
- "I don't know" is a valid finding. BLANK with explanation, not a guess.

---

## When PM Routes Here

- Any skill surfaces a resource gap: "we need a way to do X"
- Brainstorming proposes an approach needing real-world validation
- User asks "how could we do X?" / "what tools exist for Y?"
- Auto-research recommends a resource (script, reference, template) and PM
  wants to find existing options before building from scratch
- Product question exceeds blackthorn-support's knowledge

---

## Research Process

### Stage 1: Quick Scan

Surface-level search. Return a summary index without deep-diving.

1. Parse the research question from the SKILL REQUEST
2. Identify the research domain (tool comparison, integration, API, methodology)
3. Search available sources:
   - Web search for current tools, libraries, services
   - GitHub for repos, MCP servers, Claude skills
   - Documentation sites for specific products
   - Curated directories and awesome-lists
4. Return summary index — one line per option with name and claimed purpose

**Stage 1 output:**
```
Found [N] potential options for [research question].

| # | Option | Category | Claimed Purpose | Source |
|---|--------|----------|-----------------|--------|
| 1 | Tool A | MCP server | Calendar integration | github.com/... |
| 2 | Tool B | API | Calendar + contacts | toolb.com/docs |
| 3 | Tool C | Library | Calendar sync | npmjs.com/... |

Proceeding to deep dive on top [3] candidates.
```

### Stage 2: Deep Dive

For top 3-5 candidates, read actual documentation.

1. Fetch and read README, docs, or product pages
2. Verify claimed features against documentation
3. Check: last updated, community adoption (stars, downloads), pricing,
   maintenance status
4. Note discrepancies between marketing claims and technical docs

### Stage 3: Verification

Cross-reference claims against multiple sources.

For each finding:
- **EXTRACTED** — confirmed in technical docs, README, API reference, or source code
- **INFERRED** — suggested by marketing, community discussions, or related features
- **BLANK** — claimed but could not be verified in available documentation

---

## SKILL RESULT Format

```
## SKILL RESULT: research
Timestamp: [ISO 8601]
Customer: [customer name if relevant, else None]
Actions taken: Researched [topic]. Scanned [N] sources. Deep-dived [N]
  candidates. Verified [N] claims.

Findings:

  === RECOMMENDATIONS ===
  | # | Option | What It Is | Why It Fits | Source | Confidence | Verification |
  |---|--------|-----------|-------------|--------|------------|-------------|
  | 1 | [name] | [description] | [rationale] | [URL] | High | EXTRACTED — confirmed in API docs |
  | 2 | [name] | [description] | [rationale] | [URL] | Medium | INFERRED — feature list suggests this |
  | 3 | [name] | [description] | [rationale] | [URL] | Low | BLANK — could not verify in docs |

  === COMPARISON ===
  | Dimension | Option 1 | Option 2 | Option 3 |
  |-----------|----------|----------|----------|
  | Pricing | Free/OSS (EXTRACTED) | $X/mo (EXTRACTED) | Unknown (BLANK) |
  | Last Updated | [date] (EXTRACTED) | [date] (EXTRACTED) | [date] (EXTRACTED) |
  | Community | [N] stars (EXTRACTED) | [N] downloads (EXTRACTED) | — |
  | Maintenance | Active (EXTRACTED) | Stale (EXTRACTED) | — |
  | Use Case Fit | [assessment] (INFERRED) | [assessment] (INFERRED) | — |

  === FLAGS ===
  | Item | Reason |
  |------|--------|
  | [what couldn't be verified] | [why] |

  === VERIFY YOURSELF ===
  - [ ] [Things the user should manually check before committing]

  === SOURCES CONSULTED ===
  | Source | Type | Access | Notes |
  |--------|------|--------|-------|
  | [URL] | README | Full | Primary documentation |
  | [URL] | API docs | Full | Feature verification |

Confidence: [High if majority EXTRACTED with multi-source verification;
  Medium if mix; Low if mostly INFERRED or BLANK]
Gaps/failures: [Paywalled docs, unavailable APIs, rate-limited searches]
Suggested next: [brainstorming to evaluate | PM to route to implementation]
Flags for Jared: [Recommendations requiring purchase, signup, or config — Tier 2]
```

---

## Caching and Deduplication

### Check Before Researching
Look in `outputs/research/` for previous results on the same topic.
If recent (<30 days) and landscape hasn't changed, reference previous
research and note what's new.

### Cache Results
Save outputs to `outputs/research/<topic-slug>/` with timestamp.
Future research on the same topic builds on prior findings.

### Deduplication
If PM requests research on "calendar MCP servers" and a previous run
covered "MCP servers for scheduling," note the overlap and build on it.

---

## Integration with Core Skills

### Research ← Brainstorming
Brainstorming says "we could use tool X." Research verifies whether tool X
exists, is maintained, and fits the use case.

### Research ← PM
PM identifies a gap. Research finds existing solutions before building
from scratch.

### Research ← Auto-Research
Auto-research recommends a resource type. Research finds the best option.

### Research → PM (SKILL RESULT)
All results return to PM. PM routes to brainstorming for evaluation,
presents to user for decision, or flags as Tier 2 if action requires
purchases or account setup.
