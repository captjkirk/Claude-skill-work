# Criteria Templates — Domain-Specific Heuristics

When auto-research generates evaluation criteria for a target skill, it starts
with the skill's domain classification and draws from the heuristics below.
These are starting points — always adapt based on the specific skill's analysis,
PROCESS-LESSONS.md entries, and EVO proposals.

Never use these templates verbatim. They exist to ensure you don't miss
important quality dimensions for each domain.

---

## Universal Criteria (Apply to Every Skill)

These criteria apply regardless of domain. Include at least one in every
evaluation set.

### SKILL RESULT Schema Compliance
**What to check:** Does the output contain all fields PM expects?
- `Timestamp` (ISO 8601)
- `Customer` (name or "None")
- `Actions taken` (summary)
- `Findings` (substantive output)
- `Confidence` (High / Medium / Low)
- `Gaps/failures` (what the skill couldn't do)
- `Suggested next` (what should run next, if anything)
- `Flags for Jared` (Tier 2 items only)

**Evaluation prompt:** "Does the output contain a properly formatted SKILL
RESULT block with all required fields (Timestamp, Customer, Actions taken,
Findings, Confidence, Gaps/failures, Suggested next, Flags for Jared)?
Answer PASS or FAIL with one sentence justification."

### Tier 1/2 Classification Accuracy
**What to check:** Does the skill correctly distinguish between autonomous
actions (Tier 1) and actions requiring user approval (Tier 2)?

**Tier 1 (autonomous):** File writes, memory updates, dossier updates, running
additional skills, drafting recommendations, internal analysis.

**Tier 2 (flag to user):** External sends (email, Slack), applying skill
patches, irreversible actions, anything visible to customers/colleagues,
high-stakes customer risk signals.

**Evaluation prompt:** "Does the output correctly classify all actions as
Tier 1 (autonomous) or Tier 2 (flag to user)? Specifically: are any external
sends or irreversible actions treated as Tier 1 (wrong), or are any internal
file writes treated as Tier 2 (unnecessarily cautious)? Answer PASS or FAIL."

### Honesty Protocol Compliance (MANDATORY)
This criterion MUST be included in every evaluation. It cannot be removed or
skipped regardless of domain. Source: `skills/core/honesty-protocol.md`

**What to check:** Does the output follow all three honesty rules?
1. Force Blank — are ambiguous/missing values BLANK with Flags entries?
2. Penalize Guessing — are there any confident assertions without evidence?
3. Show the Source — are all values labeled EXTRACTED or INFERRED with evidence?

**Evaluation prompt:** "Check the output against the honesty protocol.
(1) Are all values labeled EXTRACTED or INFERRED? (2) Do all INFERRED values
have evidence trails? (3) Are ambiguous/missing values BLANK with Flags
entries? (4) Are there any confident assertions without sources? (5) Does the
Confidence level match evidence quality? Any violation is a FAIL. Answer PASS
or FAIL with specific examples of the violation."

### Confidence Calibration
**What to check:** Does the stated confidence accurately reflect the evidence?
- High = mostly EXTRACTED, minimal blanks, recent data
- Medium = mix of EXTRACTED/INFERRED, some blanks, data 30-90 days old
- Low = mostly INFERRED or BLANK, stale data, missing key sources

**Evaluation prompt:** "Compare the stated Confidence level against the evidence.
Is it accurately calibrated? Overconfidence on thin evidence is a FAIL.
Underconfidence on strong evidence is also a FAIL. Answer PASS or FAIL."

### Cross-Skill Reference Accuracy
**What to check:** When the skill references other skills (by name, in
"Suggested next", or in routing logic), are the names correct and do the
referenced skills actually exist?

**Evaluation prompt:** "Does the output reference other skills by their correct
names? Does 'Suggested next' point to a real skill that makes sense as a
follow-up? Answer PASS or FAIL."

---

## Orchestration Skills

**Examples:** project-manager, morning-orchestrator

Orchestration skills route work to other skills and synthesize results. They
don't produce substantive output themselves — they decide *what runs* and
*in what order*.

### Routing Correctness
Does the skill identify the right downstream skills for the given input? Does
it match PM's routing table?

**Evaluation prompt:** "Given the input signals, does the output invoke the
correct skills in the correct order? Cross-reference against PM's routing
table. Answer PASS or FAIL."

### Signal Detection Completeness
Does the skill detect all actionable signals in the input? A missed signal
means a skill that should have run doesn't.

**Evaluation prompt:** "Are there any actionable signals in the input that
the output fails to detect or route? A missed customer name, an undetected
risk signal, an ignored calendar event? Answer PASS or FAIL."

### Parallel vs. Sequential Handling
When multiple skills need to run, does the orchestrator correctly identify
which can run in parallel and which must be sequential?

**Evaluation prompt:** "Does the output correctly handle parallel vs. sequential
skill invocations? Skills with dependencies should be sequential; independent
skills should be parallel. Answer PASS or FAIL."

### Consolidated Output (No Premature Presentation)
Does the orchestrator wait for all skills to complete before presenting to the
user? Partial output while work is pending is a failure.

**Evaluation prompt:** "Does the output present consolidated results only after
all skill work is complete? Any partial presentation or premature surfacing of
results is a FAIL. Answer PASS or FAIL."

---

## Customer Research Skills

**Examples:** customer-dossier, fathom, flagged-onboarding-sync

These skills gather, synthesize, and present customer context.

### Customer Identification
Does the skill correctly identify which customer is being referenced and load
the right dossier?

**Evaluation prompt:** "Does the output correctly identify the customer and
reference the right dossier data? Any misattribution or wrong customer context
is a FAIL. Answer PASS or FAIL."

### Field Completeness
Does the output populate all expected fields? Missing fields force PM to
deepen or re-route unnecessarily.

**Evaluation prompt:** "Does the output populate all fields expected for this
skill's SKILL RESULT? Check against PM's catalog entry for this skill. Any
missing required fields are a FAIL. Answer PASS or FAIL."

### Confidence Calibration
Does the stated confidence level accurately reflect the data quality?
High confidence on sparse data is worse than Medium confidence — it
prevents PM from deepening when it should.

**Evaluation prompt:** "Does the stated Confidence level (High/Medium/Low)
accurately reflect the underlying data quality? High confidence requires rich,
recent data. Medium or Low should trigger PM to deepen. Miscalibrated
confidence is a FAIL. Answer PASS or FAIL."

### Staleness Detection
Does the skill flag stale data rather than presenting it as current?

**Evaluation prompt:** "If any of the data used is potentially stale (old
dates, outdated status), does the output flag this? Presenting stale data
without a caveat is a FAIL. Answer PASS or FAIL."

---

## Content Generation Skills

**Examples:** email-templates, com-update, kickoff-deck, blackthorn-brand

These skills produce content for human review or external delivery.

### Format Compliance
Does the output match the expected format exactly? Email skills should produce
HTML with subject/to/cc/body. COM skills should produce field-value pairs.

**Evaluation prompt:** "Does the output match the expected format for this
skill type? Check structure, required sections, and formatting conventions.
Any missing structure is a FAIL. Answer PASS or FAIL."

### Voice and Tone Match
For customer-facing content, does the output match the expected voice?
Blackthorn brand voice, Jared's personal communication style, or the
appropriate email template tone.

**Evaluation prompt:** "Does the output match the expected voice and tone?
Check against brand guidelines or the user's established communication style.
Obvious mismatches in formality, terminology, or personality are a FAIL.
Answer PASS or FAIL."

### No Hallucinated Details
Content skills must never fabricate customer details, dates, meeting outcomes,
or commitments that aren't in the input context.

**Evaluation prompt:** "Does the output contain any details (customer facts,
dates, commitments, meeting outcomes) not present in or directly inferable
from the input context? Any fabricated detail is a FAIL. Answer PASS or FAIL."

### Required Fields Present
Does the output include all fields the downstream consumer expects?
COM updates need specific Salesforce fields. Emails need subject + recipients + body.

**Evaluation prompt:** "Does the output include all required fields for its
type? Check against the skill's specified output format. Any missing required
field is a FAIL. Answer PASS or FAIL."

---

## Memory Management Skills

**Examples:** dream, memory-create, memory-delete

These skills read and write to MEMORY.md files, customer dossiers, and other
persistent storage.

### Correct Routing to Target File
Does the fact get written to the right file? Customer facts should go to the
customer dossier, not root MEMORY.md. Subfolder-specific context should go
to that subfolder's MEMORY.md.

**Evaluation prompt:** "Does each proposed write target the correct file?
Customer-specific facts should target `customers/<name>/<name>.md`, subfolder
facts should target `<subfolder>/MEMORY.md`, and general facts should target
root `MEMORY.md`. Any misrouted write is a FAIL. Answer PASS or FAIL."

### No Duplicate Entries
Does the skill check for existing entries before writing? Adding a fact that's
already captured wastes memory budget.

**Evaluation prompt:** "Does the output check for and avoid duplicate entries?
If a fact is already present in the target file, writing it again is a FAIL.
Answer PASS or FAIL."

### No Overwrites of Good Data
The skill should never silently overwrite existing, correct data. Updates
should be explicit (replace X with Y) and pruning should flag for review.

**Evaluation prompt:** "Does the output preserve existing correct data? Any
silent overwrite of a valid entry without explicit justification is a FAIL.
Answer PASS or FAIL."

### Appropriate Pruning
Stale or contradicted entries should be flagged for removal, but uncertain
entries should be left alone. Over-pruning is as bad as under-pruning.

**Evaluation prompt:** "Does the output appropriately flag stale or contradicted
entries for pruning while leaving uncertain entries alone? Over-pruning or
pruning without strong evidence is a FAIL. Answer PASS or FAIL."

---

## Product Knowledge Skills

**Examples:** blackthorn-support, product-feedback-poster

These skills answer product questions or route them for further research.

### Answer Accuracy
Is the answer factually correct based on available product documentation?

**Evaluation prompt:** "Is the answer factually accurate based on available
Blackthorn product documentation? Any incorrect fact about product features,
configuration, or behavior is a FAIL. Answer PASS or FAIL."

### Confidence-Appropriate Escalation
When the skill isn't confident, does it escalate correctly?
blackthorn-support at Medium/Low should route to product-feedback-poster.

**Evaluation prompt:** "When the answer confidence is Medium or Low, does the
output include appropriate escalation (e.g., suggesting product-feedback-poster
or flagging for manual research)? Confident presentation of uncertain answers
is a FAIL. Answer PASS or FAIL."

### Source Attribution
Does the skill indicate where its answer came from? Answers grounded in
specific docs or articles are more trustworthy than unsourced assertions.

**Evaluation prompt:** "Does the output attribute its answer to a specific
source (article, doc, feature description)? Unsourced assertions on technical
questions are a FAIL. Answer PASS or FAIL."

---

## Utility Skills

**Examples:** subfolders, process-mistakes, onboarding-process-sync, schedule

These skills perform discrete, well-defined operations.

### Idempotency
Running the skill twice with the same input should not produce duplicate
results or errors.

**Evaluation prompt:** "Would running this skill again with the same input
produce a clean result without duplicates or errors? Any indication of
non-idempotent behavior is a FAIL. Answer PASS or FAIL."

### Correct File Targeting
Does the skill write to or read from the correct filesystem path?

**Evaluation prompt:** "Does the output target the correct file paths for
reads and writes? Any wrong path or missing path validation is a FAIL.
Answer PASS or FAIL."

### Confirmation in SKILL RESULT
Utility skills should confirm exactly what they did — which files were
written, what was changed, what was deleted.

**Evaluation prompt:** "Does the SKILL RESULT confirm exactly what actions
were taken (files written, entries added/removed, paths created)? Vague
confirmations without specifics are a FAIL. Answer PASS or FAIL."

---

## Cross-Skill Integration (Sweep Mode)

These criteria evaluate how skills work **together** — the handoffs, routing
decisions, and collective behavior across multi-skill chains. Used in Stage 3
of sweep mode. Individual skill criteria (above) test skills in isolation;
integration criteria test the boundaries between them.

Never use these for single-skill evaluation. They only apply when evaluating
a chain of 2+ skills passing data through PM.

### IC1: SKILL RESULT → SKILL REQUEST Compatibility

When Skill A's output flows through PM to become Skill B's input, does the
handoff work? Does Skill A's SKILL RESULT contain all fields that Skill B
needs in its SKILL REQUEST?

**Known critical handoffs:**
- `morning-orchestrator` → `customer-dossier`: Must pass customer names extracted from calendar
- `customer-dossier` → `day-prep-recap`: Must pass phase, open items, contacts, risk flags
- `customer-dossier` → `com-update`: Must pass current COM field values for comparison
- `post-meeting-sweep` → `fathom`: Must pass meeting name + time for lookup
- `fathom` → `com-update`: Must pass action items, key outcomes, risk signals
- `blackthorn-support` → `product-feedback-poster`: Must pass exact question + confidence + customer context
- `email-templates` → `blackthorn-brand`: Must pass draft content + content type + audience
- `dream` → `memory-create`: Must pass fact text + target file + section

**Evaluation prompt:** "Does Skill A's SKILL RESULT contain all data fields that
Skill B needs to construct a valid SKILL REQUEST? Check each field the downstream
skill expects against what the upstream skill actually provides. Any missing
field that would force PM to fabricate data or skip the downstream skill is a
FAIL. Answer PASS or FAIL."

### IC2: Dependency Ordering

Does the chain execute in the correct sequence? Hard dependencies must be
respected.

**Hard dependency rules:**
- `customer-dossier` MUST complete before any task-specific skill when a customer is named
- `email-templates` MUST be checked before drafting any email from scratch
- `blackthorn-support` MUST return before deciding whether to route to `product-feedback-poster`
- `morning-orchestrator` MUST complete before `day-prep-recap` receives its input
- `post-meeting-sweep` findings MUST be available before `com-update` runs

**Evaluation prompt:** "Does the chain execute skills in the correct dependency
order? Specifically: does customer-dossier run before task-specific skills? Does
email-templates get checked before freehand drafting? Are hard sequential
dependencies respected? Any out-of-order execution is a FAIL. Answer PASS or FAIL."

### IC3: Parallel Buffering

When multiple skills run in parallel, PM must buffer all results before
presenting to the user or routing downstream. No premature partial output.

**Parallel patterns to test:**
- Multiple `customer-dossier` calls for different customers (all must complete before presentation)
- `fathom` + Gmail searches running simultaneously (both must return before synthesis)
- Multiple SKILL RESULTs from different skills (all buffered, presented as consolidated block)

**Evaluation prompt:** "When multiple skills run in parallel, does PM wait for
ALL results before presenting or routing downstream? Any partial output while
other skills are still pending is a FAIL. Answer PASS or FAIL."

### IC4: Confidence-Based Routing

When a skill returns Medium or Low confidence, PM should either deepen
(re-request with more context) or re-route (send to a different skill).

**Expected routing decisions:**
- `fathom` Medium/Low → PM requests transcript pull (deepen)
- `fathom` + high-stakes signal → ALWAYS transcript pull regardless of confidence
- `blackthorn-support` Medium/Low → route to `product-feedback-poster` (re-route)
- `customer-dossier` Low (stale) → PM requests dossier regeneration (deepen)
- Any skill with gaps → PM checks if another skill can fill them

**Evaluation prompt:** "When a skill returns Medium or Low confidence, does PM
take the correct action (deepen with more context, or re-route to a different
skill)? Accepting Medium/Low confidence without deepening on customer-impacting
questions is a FAIL. Answer PASS or FAIL."

### IC5: Tier 1/2 Segregation Across Chain

Across the complete chain, all Tier 1 actions should execute autonomously and
all Tier 2 items should be collected into a single block presented at the end.
No Tier 2 action should execute mid-chain.

**Tier 1 (autonomous):** File writes, memory updates, dossier updates, running
additional skills, drafting to outputs/, routing decisions, writing EVO proposals.

**Tier 2 (flag to user):** External sends (email, Slack), applying skill patches,
irreversible actions, anything visible to customers/colleagues, high-stakes
customer risk signals.

**The "Act First, Flag Last" pattern:**
```
DO all Tier 1 work → COLLECT Tier 2 flags → PRESENT consolidated output + flags
```

**Evaluation prompt:** "Across the complete chain, are all Tier 1 actions executed
autonomously while all Tier 2 items are collected and presented as a single block
at the end? Any Tier 2 action executed mid-chain, or any Tier 2 flag presented
before all Tier 1 work completes, is a FAIL. Answer PASS or FAIL."

### IC6: High-Stakes Signal Propagation

When any skill in the chain detects a high-stakes signal, it must propagate to
PM regardless of confidence level and trigger the correct escalation.

**High-stakes signals:** "cancel", "opt out", "not renewing", "considering
alternatives", "frustrated", "this isn't working", "evaluate other platforms",
"talk to legal", "issue a refund", threats to leave or reduce scope.

**Expected behavior:** Any high-stakes signal → fathom transcript pull (if
meeting-sourced) + Tier 2 flag + customer-dossier risk update.

**Evaluation prompt:** "When a high-stakes signal appears anywhere in the chain
(in fathom output, email content, meeting notes, etc.), does it propagate to PM
and trigger escalation (transcript pull + Tier 2 flag)? A high-stakes signal
that goes undetected or unescalated is a FAIL. Answer PASS or FAIL."

### IC7: No Circular Handoffs

The chain must terminate. No skill should trigger a loop back to itself or to
an earlier skill in the chain.

**Known risk patterns:**
- `dream` → `memory-create` must not re-trigger `dream`
- `product-feedback-poster` must not loop back to `blackthorn-support`
- `com-update` after `fathom` must not re-trigger `fathom`
- PM deepening on low confidence must have a max depth (don't deepen forever)

**Evaluation prompt:** "Does the chain terminate cleanly without circular
handoffs? Does any skill's output trigger a loop back to itself or an earlier
skill? Any circular reference or infinite loop potential is a FAIL.
Answer PASS or FAIL."

### IC8: Schema Consistency

All skills in the chain should use the same SKILL RESULT schema — same field
names, same confidence scale (High/Medium/Low), same timestamp format (ISO 8601).

**Evaluation prompt:** "Do all SKILL RESULTs in the chain use consistent schema —
same field names, same confidence scale (High/Medium/Low), same timestamp format
(ISO 8601)? Any schema drift (different field names for the same concept,
numeric vs. text confidence) is a FAIL. Answer PASS or FAIL."

### IC9: Graceful Degradation

When one skill in the chain fails or returns empty results, the chain should
continue with reduced context rather than halting entirely.

**Expected behavior:**
- Missing fathom data → proceed with Gmail-only context, note the gap
- Empty dossier → create dossier, then proceed
- Failed API call → log to TASKS.md, continue with available data
- Skill timeout → skip, note in Gaps/failures field

**Evaluation prompt:** "When one skill in the chain returns empty results or
fails, does the chain continue with reduced context? Does PM log the gap in
Gaps/failures? A complete chain halt due to one skill's failure is a FAIL.
Answer PASS or FAIL."

### IC10: Memory Routing Consistency

When multiple skills in a chain propose memory writes, the writes should target
the correct files without conflicts or duplicates.

**Routing rules:**
- Customer-specific facts → `customers/<name>/<name>.md`
- Subfolder-specific facts → `<subfolder>/MEMORY.md`
- General facts → root `/Cowork-OS/MEMORY.md`
- Feature explanations → `reference/feature-explanations.md`
- Never duplicate the same fact to multiple locations

**Evaluation prompt:** "When multiple skills propose memory writes, do they
target the correct files following the routing rules? Are there any conflicts
(two skills writing contradictory data to the same file) or duplicates (same
fact written to multiple locations)? Any routing error is a FAIL.
Answer PASS or FAIL."
