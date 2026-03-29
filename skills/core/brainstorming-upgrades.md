# Brainstorming Upgrades

Add these sections to the existing brainstorming SKILL.md.

---

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

---

## Question Protocol

1. **One question per message.** Never ask multiple questions in a single
   message. Prevents cognitive overload. Ensures focused answers.

2. **Prefer multiple-choice.** Present 2-3 options rather than open-ended
   questions. Easier to answer quickly (especially from a phone).

3. **Front-load the recommendation.** If you have a preferred option, list
   it first and mark it "(Recommended)" with a brief reason.

4. **Context before question.** One sentence explaining why you're asking
   before the question itself.

5. **Progressive depth.** Start broad → narrow → detail:
   - "What are we trying to accomplish?"
   - "Which of these three approaches fits best?"
   - "Should validation run on every save or on submit only?"

---

## Honesty Protocol for Proposals

Follow `skills/core/honesty-protocol.md`.

When presenting proposals or approaches, label each element:

- **EXTRACTED** — Directly from the user's stated requirements.
- **INFERRED** — An assumption brainstorming is making. Must flag and explain.

### Example

"Here's the approach I'm proposing:

| Element | Source | Detail |
|---------|--------|--------|
| Calendar integration | EXTRACTED | You said you need calendar sync |
| Google Calendar | INFERRED | You mentioned Google Workspace — assuming Google Calendar. Correct? |
| Real-time sync | INFERRED | Most integrations are real-time. Want batch instead? |
| Read-only access | EXTRACTED | You said 'just need to see the schedule' |

Any assumptions marked INFERRED — let me know if I got them wrong."

This prevents silently adding scope or making decisions the user didn't ask for.

---

## Research Handoff

When your proposal includes any of these:
- A specific tool, library, or framework
- An MCP server or API integration
- A third-party service or platform
- A technical approach you haven't verified

**Do not present it as a recommendation.** Instead:

1. Present as a **candidate**: "One approach could be [tool X], but I haven't
   verified it meets our needs."
2. Ask: "Want me to have the research skill investigate before we commit?"
3. If yes → route to research skill via PM
4. Research returns verified findings → brainstorming evaluates with user
5. Only then → recommend an approach

### Skip the Handoff When:
- Tool/approach already installed and working in workspace
- User explicitly says they've already evaluated the option
- Approach uses only built-in Claude capabilities (no external deps)

### Example Flow

Brainstorming: "For calendar integration, we could use an MCP server. I've
seen references to options but haven't verified them. Want me to have
research investigate?"

User: "Yes."

→ PM → Research: "Find maintained MCP servers for Google Calendar. Need:
read access, works with Claude Code, actively maintained."

Research returns verified options.

Brainstorming: "Research found 3 options. Here's what's verified: [comparison].
Based on our requirements (EXTRACTED), Option 1 fits best because [rationale].
Proceed?"

---

## Design Capture

When the user approves an approach, document before handing off:

1. **Write design summary** to:
   - New skill: `skills/<skill-name>/design.md`
   - Workspace change: `outputs/designs/<topic-slug>.md`
   - Existing skill mod: skill's `reference/` directory

2. **Summary includes:**
   - Problem statement (EXTRACTED from user)
   - Chosen approach (with rationale)
   - Assumptions (all INFERRED items, approved by user)
   - Scope boundaries (included + explicitly NOT included)
   - Success criteria (how we'll know it works)
   - Dependencies (tools, skills, resources needed)

3. **Hand off to PM** with design referenced in SKILL RESULT.

The design doc is the contract between brainstorming and implementation.
Nothing gets lost between "we agreed" and "start building."
