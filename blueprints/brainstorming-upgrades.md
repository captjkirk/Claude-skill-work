# Brainstorming Upgrades — Blueprint

This is a design doc. The next Claude Code session modifies the existing
brainstorming skill in the live Cowork workspace with these additions.

## Sources

- [Superpowers](https://github.com/obra/superpowers) — Hard gate on
  implementation, single-question discipline, Socratic brainstorming approach.
  122K stars. The brainstorming skill in Superpowers enforces design-before-code
  as a non-negotiable rule.
- [The Honesty Gap](https://d-squared70.github.io/ChatGPT-and-Claude-Got-Smarter.-Not-More-Honest.)
  — EXTRACTED vs INFERRED labeling applied to proposals and assumptions.

---

## Upgrade 1: Hard Gate on Implementation

The most important addition. Adapted from Superpowers' brainstorming skill.

### Add to Brainstorming SKILL.md — Core Rule

```markdown
## Hard Rule: No Implementation Without Design Approval

Do NOT invoke any implementation skill, write any code, create any files,
scaffold any project, or take any implementation action until:

1. You have presented a design/approach to the user
2. The user has explicitly approved it

This applies to ALL tasks, including ones that seem "simple" or "obvious."
Simple tasks are the highest risk — they skip design because they seem
straightforward, then compound into complex problems.

If the user says "just do it" or "skip the brainstorming" — that IS approval.
But the default is always: explore first, build second.
```

### Why This Matters for the Portable Core

Brainstorming is the "think first" gate. If it doesn't enforce the gate,
the system skips straight to implementation and misses opportunities to:
- Catch misunderstandings before they become wasted work
- Identify that a similar solution already exists (research handoff)
- Consider multiple approaches before committing to one
- Surface assumptions that need validation

---

## Upgrade 2: Single-Question Discipline

Adapted from Superpowers' brainstorming skill. Prevents cognitive overload
and ensures each question gets a thoughtful answer.

### Add to Brainstorming SKILL.md — Question Protocol

```markdown
## Question Protocol

When exploring requirements with the user:

1. **One question per message.** Never ask multiple questions in a single
   message. This prevents cognitive overload and ensures each question gets
   a focused answer.

2. **Prefer multiple-choice.** When possible, present 2-3 options rather
   than open-ended questions. This makes it easier for the user to respond
   quickly (especially from a phone).

3. **Front-load the recommendation.** If you have a preferred option, list
   it first and mark it "(Recommended)" with a brief reason why.

4. **Context before question.** Give a one-sentence explanation of why
   you're asking before the question itself. Don't ask "Which database?"
   without first explaining "We need to decide on a storage approach because
   the data volume affects the architecture."

5. **Progressive depth.** Start broad ("What are we trying to accomplish?"),
   then narrow ("Which of these three approaches fits best?"), then detail
   ("Should the validation run on every save or on submit only?").
```

---

## Upgrade 3: Honesty Labeling on Proposals

Every proposal brainstorming presents must be transparent about what came
from the user vs. what brainstorming assumed.

### Add to Brainstorming SKILL.md — Proposal Honesty

```markdown
## Honesty Protocol for Proposals

When presenting proposals or approaches, label each element:

- **EXTRACTED** — Directly from the user's stated requirements. The user
  said this explicitly.
- **INFERRED** — An assumption brainstorming is making about what the user
  wants. Must be flagged and explained so the user can correct it.

### Example

"Here's the approach I'm proposing:

| Element | Source | Detail |
|---------|--------|--------|
| Calendar integration | EXTRACTED | You said you need calendar sync |
| Google Calendar specifically | INFERRED | You mentioned Google Workspace earlier — assuming Google Calendar. Correct? |
| Real-time sync | INFERRED | Most calendar integrations are real-time. Want batch sync instead? |
| Read-only access | EXTRACTED | You said 'just need to see the schedule' |

Any assumptions I've marked INFERRED — let me know if I got them wrong."

This prevents brainstorming from silently adding scope or making decisions
the user didn't ask for. Every assumption is visible and correctable.
```

### Why This Matters

Without honesty labeling, brainstorming can:
- Add features the user didn't ask for ("while we're at it, let's also...")
- Assume a technology choice without asking ("we'll use React for this")
- Scope-creep a simple request into a complex project
- Present its assumptions as the user's requirements

The EXTRACTED/INFERRED labeling makes every assumption visible.

---

## Upgrade 4: Research Handoff

When brainstorming surfaces an approach that depends on external tools,
libraries, or integrations, it should validate before recommending.

### Add to Brainstorming SKILL.md — Research Integration

```markdown
## Research Handoff

When your proposal includes any of these:
- A specific tool, library, or framework
- An MCP server or API integration
- A third-party service or platform
- A technical approach you haven't verified

**Do not present it as a recommendation.** Instead:

1. Present it as a **candidate** — "One approach could be [tool X], but I
   haven't verified it meets our specific needs."
2. Ask the user: "Want me to have the research skill investigate this before
   we commit to it?"
3. If yes → route to research skill via PM with the specific question
4. Research returns verified findings → brainstorming evaluates the options
   with the user
5. Only then → recommend an approach

### When to Skip the Handoff

You can skip the research handoff when:
- The tool/approach is already installed and working in the workspace
- The user explicitly says they've already evaluated the option
- The approach uses only built-in Claude capabilities (no external deps)

### Example Flow

Brainstorming: "For calendar integration, we could use an MCP server.
I've seen references to a few options but haven't verified which ones are
maintained or fit our setup. Want me to have research investigate?"

User: "Yes, go ahead."

Brainstorming → PM → Research: "Find maintained MCP servers for Google
Calendar integration. Need: read access to events, works with Claude Code,
actively maintained (commits in last 3 months)."

Research returns: Verified options with EXTRACTED/INFERRED labels.

Brainstorming: "Research found 3 options. Here's what's verified: [presents
comparison]. Based on our requirements (EXTRACTED from our earlier discussion),
Option 1 fits best because [rationale]. Shall we proceed with this approach?"
```

---

## Upgrade 5: Design Documentation

When brainstorming reaches a design the user approves, capture it before
moving to implementation.

### Add to Brainstorming SKILL.md — Design Capture

```markdown
## Design Capture

When the user approves an approach, document it before handing off:

1. **Write a design summary** to the appropriate location:
   - For new skills: `skills/<skill-name>/design.md`
   - For workspace changes: `outputs/designs/<topic-slug>.md`
   - For existing skill modifications: append to the skill's reference/ dir

2. **Design summary includes:**
   - Problem statement (EXTRACTED from user)
   - Chosen approach (with rationale)
   - Assumptions made (all INFERRED items, approved by user)
   - Scope boundaries (what's included, what's explicitly NOT included)
   - Success criteria (how we'll know it works)
   - Dependencies (tools, skills, resources needed)

3. **Hand off to PM** with the design summary referenced in the SKILL RESULT.
   PM routes to the implementation skill with the design as context.

This ensures nothing gets lost between "we agreed on this approach" and
"start building." The design doc is the contract between brainstorming
and implementation.
```

---

## Integration Summary

| Upgrade | What It Does | Pattern Source |
|---------|-------------|---------------|
| Hard gate | Prevents implementation before design approval | Superpowers |
| Single-question | One question per message, prefer multiple-choice | Superpowers |
| Honesty labeling | Labels proposals EXTRACTED vs INFERRED | Honesty Gap |
| Research handoff | Validates external tools before recommending | Research skill + Honesty Gap |
| Design capture | Documents approved design before implementation | Superpowers |

These upgrades make brainstorming the reliable front door for all new work.
It thinks first, validates assumptions, checks with the outside world, and
documents the agreement before anything gets built.
