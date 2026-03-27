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
