---
name: com-update
description: >
  INTERNAL — invoked by PM only. Do not trigger directly on user messages. Recommend Salesforce COM
  (Customer Onboarding Management) field updates after any customer interaction — calls, emails,
  syncs, or any touchpoint. Outputs copy-paste-ready field values the user applies directly in
  Salesforce. Invoke whenever the user wants to update a COM record, log an interaction, or capture
  what happened in a recent call or email exchange. Also invoke proactively after any customer context
  surfaces during another workflow — if a customer name appears and there's interaction data worth
  logging, recommend updates without being asked. Trigger phrases: "update COM for [customer]", "log
  my interaction with [customer]", "update onboarding notes for [customer]", "what should I update
  after my call with [customer]", "COM update". Also trigger when day-prep-recap identifies a
  completed onboarding sync. Use flagged-onboarding-sync instead only when specifically prepping for
  the bi-weekly sync.
---

# COM Update Skill

## What This Skill Does

Recommends Salesforce COM field updates after any customer interaction and outputs copy-paste-ready
field values. Claude cannot update Salesforce directly — the output of this skill is a formatted
recommendations block the user applies in Salesforce themselves.

The goal is to keep COM records current so that anyone on the team — managers, CSMs, the onboarding
manager on a future date — can glance at a record and know exactly where things stand.

This is the workhorse COM updater. It runs after calls, email exchanges, or any meaningful touchpoint.
**Proactive mode:** any time another workflow (day-prep-recap, fathom, customer-dossier) surfaces
interaction context for an onboarding customer, offer COM field recommendations without waiting to
be asked. The flagged-onboarding-sync skill handles the bi-weekly leadership sync — this covers
everything else.

---

## Fields This Skill Updates

### Core Fields (update every interaction)

| Field | API Name | Type | Limit | What Goes Here |
|---|---|---|---|---|
| Last Interaction | `Last_Interaction__c` | Text Area | 255 chars, plain text | Date + one-liner summary of the most recent touchpoint |
| Steps to Next Stage | `Steps_to_Next_Stage__c` | Text Area | 255 chars, plain text | Current action items / what's needed before the customer can progress |
| Onboarding Notes | `Onboarding_Notes__c` | Rich Text Area | 50,000 chars | Comprehensive, current summary of the entire engagement |

### Update When New Info Surfaces

| Field | API Name | Type | Limit | What Goes Here |
|---|---|---|---|---|
| How are we being used? | `How_are_we_being_used__c` | Rich Text Area | 100,000 chars | Functional product usage — features, event types, integrations. Skip if nothing new. |

### Update When Relevant

| Field | API Name | Type | Limit | When to Update |
|---|---|---|---|---|
| Customer's Product Pain Points | `Onboarding_Pain_Points__c` | Rich Text Area | 32,768 chars | Customer hits product friction, makes feature requests, or reports bugs |
| Concerns | `Concerns__c` | Text Area | 255 chars | General worries that don't yet warrant flagging — a "micro flag" |
| Flagged | `Flagged__c` | Checkbox | — | Only when concern escalates to a real risk |
| Flagged Reason | `Flagged_Reason__c` | Long Text Area | 50,000 chars | Context for why the account was flagged |
| Flagged Category | `Flagged_Category__c` | Picklist | — | Category of the flag |

### Date Fields (conservative updates)

These three milestone dates each have three versions: Ideal, Planned, and Actual.

| Milestone | Ideal | Planned | Actual |
|---|---|---|---|
| Event Published | `Ideal_Event_Published_Date__c` | `Planned_Event_Published_Date__c` | `Actual_First_Event_Published_Date__c` |
| First Event | `Ideal_First_Event_Date__c` | `Planned_First_Event_Date__c` | `Actual_First_Event_Date__c` |
| CS Transition | `Ideal_CS_Transition_Date__c` | `Planned_CS_Transition_Date__c` | `Actual_CS_Transition_Date__c` |

**How these dates work:**

- **Ideal dates** are set once, early in onboarding, based on the customer's best-case scenario. Once set, they don't change. Only suggest setting these if they're currently empty and the customer has stated their ideal timeline.

- **Planned dates** start as copies of the ideal dates. As the onboarding project matures and reality sets in, planned dates shift. Only recommend updating these when the customer or onboarding manager explicitly acknowledges a timeline change — not based on speculation.

- **Actual dates** record when things concretely happened. Only set these when you have confirmation that registration opened, an event went live, or CS transition occurred. These are facts, not projections.

---

## Gotchas

Failure modes that have caused problems before — check these before writing or presenting any field update.

- **Never replace Onboarding Notes — always expand.** If the user provides existing Onboarding Notes content, incorporate everything still relevant. Do not erase history. Add to it, update stale sections, and preserve the running narrative.
- **255-character fields are easy to violate.** Always count characters before finalizing `Last_Interaction__c`, `Steps_to_Next_Stage__c`, and `Concerns__c`. These will be silently truncated in Salesforce if over limit.
- **`Onboarding_Stage_Picklist__c` is Flow-managed — never touch it.** This field is set automatically by a Salesforce Flow. Suggesting an update to it will either fail or break the automation.
- **Date fields: no speculation.** Only recommend updating Planned dates when the customer or OBM explicitly acknowledges a timeline shift. Only set Actual dates with confirmed evidence. "They seem behind" is not grounds for a date change.
- **Rich text fields: no raw HTML.** Write markdown (bold, bullets) that the user can paste directly into Salesforce's rich text editor. Raw HTML tags will appear as literal text.
- **Concerns are about implementation risk, not external delays.** Budget approvals, external partner timelines, or seasonal scheduling are not Concerns unless they directly impact the customer's ability to keep working with Blackthorn.
- **Only output fields you're actually changing.** Do not include a "Fields NOT Updated" section or list fields to say "no change." Output only the fields with new content.

---

## What the User Typically Provides

The user will usually provide one or more of:

- **Customer name** — so you know which account to research
- **Current COM field values** — pasted from Salesforce, so you can see what exists and what's stale
- **Context about what just happened** — "just had a kickoff call with them" or "got an email about their timeline changing"

If the user just gives a customer name with no other context, ask: "What just happened with them — a call, email, or something else?" before researching.

If the user provides current field values, use them as your baseline. For Onboarding Notes specifically, incorporate existing content — don't discard history, update it.

---

## Step 1 — Research Sources

Work through these in order. The depth of research depends on what the user has already provided — if they just had a call and can tell you what happened, you may not need to dig through every source.

### 1. Fathom (meeting recordings)

Invoke the Fathom skill by reading and following the fathom SKILL.md — find it at: `find /sessions -path "*/mnt/.skills/skills/fathom/SKILL.md" 2>/dev/null | head -1`

Pull recent call summaries and action items for the customer. If the user mentions a specific call ("my call this morning"), scope the search tightly. If this is a broader refresh, use the full research workflow.

For any high-stakes moments identified (churn signals, escalations, specific commitments made by
Blackthorn, product failures), call `fathom_get_summary` on that recording to get the
timestamp-linked summary. Embed those links inline within the COM field text — hyperlink the
relevant phrase rather than adding a separate URL. This gives anyone reviewing the COM record
a direct path to verify the moment in context.

Run this in parallel with Slack and Gmail research.

### 2. Gmail

Search for recent emails involving the customer (last 2-3 weeks unless the user specifies otherwise):
```
Tool: gmail_search_messages
- q: "Customer Name"
- maxResults: 25
```

Read actual email bodies for threads that look relevant — subject lines alone aren't enough. Focus on:
- Direct communication with customer contacts
- Internal threads about the account
- Action items or commitments made via email

### 3. Slack

Before searching, read the `slack-search` skill (find it at `find /sessions -path "*/mnt/.skills/skills/slack-search/SKILL.md" 2>/dev/null | head -1` — or the remote plugin path at `find /sessions -path "*plugin*/skills/slack-search/SKILL.md" 2>/dev/null | head -1`) and follow its search strategy and modifier guidance.

Search for the customer name in relevant channels. Look for:
- Recent mentions or discussions
- Swarm channel activity (if one exists — ask the user)
- Blockers, product issues, or timeline updates shared in Slack

### 4. Google Calendar

Check for recent and upcoming meetings with the customer. Note dates and frequency — meeting cadence is a signal of engagement health.

### 5. Jira (only if tickets are mentioned)

If the user or any source references a Jira ticket, look it up for current status.

---

## Step 2 — Write the Field Updates

### Last Interaction (`Last_Interaction__c`)

**255 character limit, plain text.** This is a glanceable signal for management — they should be able to see at a glance that the account is being actively worked.

Format: `[date] - [one or two sentence summary of what happened]`

Always include the date. Count characters carefully — must be ≤255.

**Example:**
> 3/16/26 - Kickoff call completed. Jacob (main contact) was absent; discussed event timeline and template survey with Sarah. Follow-up scheduled for 3/20.

### Steps to Next Stage (`Steps_to_Next_Stage__c`)

**255 character limit, plain text.** A short list of what needs to happen before the customer can progress. Think of this as the onboarding manager's personal checklist for this account.

Write it as a brief dash-separated list of concrete next actions. These should be specific and actionable, not vague.

**Example:**
> Need: - Recurring syncs scheduled - Template survey completed - Adoption guide assignees confirmed - Jacob to attend next call

### Onboarding Notes (`Onboarding_Notes__c`)

**Rich text, 50,000 char limit.** This is a full replacement each time — a comprehensive, running story of the entire onboarding journey from kickoff to now. The goal is that anyone — a new OBM, a CSM taking over, leadership — could read this field alone and fully understand where this customer has been, where they are, and what's at stake. Build it from the first interaction and keep adding to it.

If the user provides existing onboarding notes, incorporate everything still relevant. Don't erase history — expand and update it. If something is missing or unclear, note it so the user can fill the gap.

Use all of the following sections. Omit a section only if there is genuinely nothing to put in it yet (e.g., Architecture on day one of kickoff if requirements aren't known). As the relationship matures, every section should be populated.

---

**Outcome**
What does successful onboarding look like for this customer? Capture their specific definition — not a generic description. Include:
- What needs to be live, functional, or validated before they're done
- Whether they're running free or paid events, in-person/virtual/hybrid
- Any specific features, integrations, or automations required
- Scope inclusions and explicit exclusions (anything agreed to be out of scope)

This should read like a requirements definition — not a summary of what was said on a call.

---

**Architecture**
How is this customer's implementation classified? Choose one: OOTB, Configurable, Workaround-Based, Custom, or Unsupported functionality. Explain what that means for this customer specifically — what's standard, what requires configuration, where workarounds are in play, and where expectations may have bumped against product limits. Distinguish between "can't" and "not yet configured." Update this if the implementation scope evolves.

---

**Key Contacts**
Everyone on the customer side who matters to this project: name, title, role in the implementation, and engagement level. Note if someone is the decision-maker, the technical owner, or the day-to-day contact. Flag anyone who has gone dark, been replaced, or whose capacity is uncertain. Also note any SI/implementation partner involved.

---

**Readiness**
Assess the customer's demonstrated capability and preparedness — not assignment completion percentages, but what they've actually shown they can do. Examples: Have they successfully configured event templates? Did they pass the reverse demo? Can they operate the system independently? Are their internal stakeholders aligned? Is there a capable Salesforce admin involved? Call out specific gaps and what they mean for timeline or go-live quality.

---

**Momentum**
A snapshot of how the onboarding is actually progressing.

- **Current phase:** Discovery / Design / Launch / Transition
  - Discovery — closed won through sandbox install
  - Design — event template build through completed reverse demo in sandbox
  - Launch — production install through first event published for registration
  - Transition — first event publish through CS transition
- **Meeting cadence and engagement:** How often are you meeting? Is there progress between calls? Is the customer responsive and taking ownership?
- **Most advanced milestone completed** (with date if known)
- **Milestones completed to date:** kickoff, template reviews, reverse demo, production install, first event published, etc.
- **What's blocking advancement to the next phase** — be specific about unmet gates
- **Execution trend:** Improving / Flat / Declining — and why

---

**Timeline**
Key dates in the onboarding journey as a bullet list — one date per line. Never write this as a paragraph. Format: MM/DD/YY. Include kickoff, major milestones completed, planned event publish date, planned first event date, planned CS transition, and any revisions with cause.

Example:
- 10/23/25 — Kickoff
- 11/06/25 — Production install completed
- 03/19/26 — CS Handoff (actual)
- 03/31/26 — Target event published / registrations open
- Oct 2026 — First event
- 09/01/28 — Contract renewal

Add a note below the list for any timeline variance and its cause.

---

**Decision / Escalation Needed**
If there is a structural decision that's currently blocking progress or that requires input from outside the OBM, call it out explicitly here. Who needs to decide, what they need to decide, and by when. This section ensures that if someone glances at the notes, they don't miss an open escalation or a decision that's sitting unresolved.

---

**Feedback**
Capture what the customer has said about the product — both positive and negative. This is distinct from the Product Pain Points field (which is for structured blockers). This section is for the broader picture:
- Features or functionality they've responded positively to
- Enhancement requests with the reason/use case behind them
- Workarounds they've accepted and what problem each solves
- Workarounds they've rejected and why
- Recurring friction themes
- Anything that might be relevant to roadmap or scalability

---

**Risks / Watch Items**
Anything that could derail the onboarding, even if not yet flag-worthy. Stale engagement, unclear ownership, approaching deadlines with no progress, a key contact going dark, dependency on an unresponsive partner, etc. Be specific — vague risk notes aren't useful.

### How are we being used? (`How_are_we_being_used__c`)

**Rich text, 100,000 char limit.** This field is specifically about **functional product usage** — what Blackthorn features and capabilities the customer is actually using or plans to use. Keep it tight and practical. Don't put organizational context, licensing details, success criteria, or general business background here — that belongs in Onboarding Notes.

Focus on:
- Which Blackthorn features they use (Events, Payments, Messaging, check-in app, etc.)
- What types of events they hold (conferences, fundraisers, workshops, webinars, etc.)
- How many events per year, expected attendance numbers
- Whether and how they use payments (Stripe, gateway type, donation vs. ticket sales)
- Integration patterns (what connects to Blackthorn in their org)
- Any custom configurations or non-standard usage

**Example:**
> Using BT Events for 3 annual fundraising galas (~500 attendees each). Paid registration + donation collection via Stripe. Plan to use mobile check-in app at events. SMS communications via BT Messaging for attendee updates. Migrating from Eventbrite.

If nothing new about their product usage came up in the interaction, skip this field entirely.

### Customer's Product Pain Points (`Onboarding_Pain_Points__c`)

**Rich text, 32,768 char limit.** This field is scoped to **product-related friction only** — things the Blackthorn platform does or doesn't do that create challenges for the customer. It is not a place to log customer-side issues like bandwidth, staffing, or internal alignment (those belong in the Readiness and Risks sections of Onboarding Notes).

Covers:
- **Product gaps or limitations** — features that don't work the way the customer needs, missing functionality, workarounds in place
- **Platform boundaries** — things the product can't do and the customer has hit that wall
- **Open support cases** — unresolved technical issues that are blocking progress
- **Workarounds in place** — what the customer is doing instead, and whether it's acceptable to them

Each entry should use a **bold header** for the issue name, followed by a brief description: what it is, why it matters for this customer, and current status (resolved, workaround accepted, open, escalated). Only include issues that are meaningfully product-related — if the challenge is purely about the customer's internal capacity or process, leave it out of this field.

If there are no product-related challenges, skip this field entirely.

### Concerns (`Concerns__c`)

**255 character limit, plain text.** This is a micro-flag — something worth noting that hasn't risen to flag level.

Concerns are about things that threaten the customer's ability to continue working on the implementation. Examples: low engagement, missed meetings, unclear internal ownership, key contact leaving, staffing changes that reduce their capacity to implement. External delays like budget approvals or timeline shifts are **not** concerns unless they directly impact staffing or the customer's ability to keep working with Blackthorn.

If there are no concerns, skip this field entirely.

### Flagged Fields

Only recommend flagging when a concern has escalated to a real risk. Flagging is a deliberate escalation — it routes the account to the bi-weekly leadership sync. Don't recommend it lightly.

When recommending a flag, always suggest a **Flagged Category** from the following list:

- **Product Misalignment** — Customer expects the product to behave differently than it does. They're asking for many enhancements, or rejecting the solutions being offered to meet their requirements.
- **Miscommunication in the Onboarding Process** — Customer believed the process would go differently. Frustration over roles and responsibilities, hands-on expectations vs. what was scoped, or confusion about what Blackthorn delivers vs. what the customer owns.
- **Product Issues Blocking Go-Live** — Multiple open support cases directly threatening the go-live deadline.
- **Delayed Onboarding Timelines** — Customer has paused, stalled, or gone unresponsive for a significant period (generally 3+ months).
- **Lack of Skill or Resources** — Customer team lacks the Salesforce admin skills, technical capacity, or internal alignment needed to complete onboarding.
- **Partner Concerns** — An SI/implementation partner is blocking direct communication, unresponsive, or creating negative dynamics.
- **Contract Concerns** — Customer has raised issues with contract terms, attempted opt-out, or expressed desire to stop engaging with onboarding.

For each flag recommendation, include:
- The suggested Flagged Category
- A proposed Flagged Reason (a concise explanation of why the flag is warranted and what the current situation is)
- Suggested next steps based on the category

### Date Fields

Only recommend date updates when:
- **Planned dates**: The customer or onboarding manager explicitly acknowledges a timeline shift. Include the source (e.g., "Per 3/16 call, customer pushed event to November due to internal staffing changes").
- **Actual dates**: You have confirmation something concretely happened. Include evidence.

Never recommend date changes based on speculation or "it seems like they might be behind."

---

## Step 3 — Present the Updates

Present all proposed updates in a clear format the user can review before entering into Salesforce.

For each field:
1. Show the field name and API name
2. Show the proposed value
3. If existing content was provided, briefly note what changed and why

**Only include fields you're actually updating.** If a field has no new information, omit it entirely from the output. Do not include a "Fields NOT Updated" section or list fields just to say "no change recommended" — that's noise the user has to read past. The output should contain only the fields that are changing and why. Nothing else.

---

## Step 3.5 — Task Sync

After presenting the COM updates and before wrapping up, reconcile TASKS.md with what the research surfaced. This keeps the task list current after every customer interaction.

**TASKS.md location:** `*/mnt/Cowork-OS/Productivity/TASKS.md`

Find and read it:
```bash
find /sessions -path "*/mnt/Cowork-OS/Productivity/TASKS.md" 2>/dev/null | head -1
```

Work through three passes:

**Pass 1 — Mark Complete:** Check Active and Waiting On for any task related to this customer. If the interaction just resolved one (e.g., you sent the follow-up email, a support case was confirmed closed, a meeting happened), mark it done with today's date and move to Done.

**Pass 2 — Update Existing:** If a task exists for this customer but wasn't resolved, update its context line to reflect current status.

**Pass 3 — Add New:** Surface tasks that aren't already tracked. Pull from:
- Items in `Steps_to_Next_Stage__c` that represent commitments you made
- Open Concerns or flagged issues requiring a follow-up action
- Any tabled or deferred items from the interaction
- New support cases or escalations referenced

**Format for new tasks:**
- Active: `- [ ] **[Task title]** - [context], for [customer], due [date if known]`
- Waiting On: `- [ ] **Waiting: [what]** - from [customer/contact], since [today's date]`

Write to TASKS.md autonomously — this is Tier 1 work, no confirmation needed.
Report what was changed in the SKILL RESULT (Actions taken field). If there's nothing
to update, skip silently.

---

## Step 4 — Format Check

Before presenting:
- `Last_Interaction__c`: count characters, must be ≤255
- `Steps_to_Next_Stage__c`: count characters, must be ≤255
- `Concerns__c`: count characters, must be ≤255
- Date fields: use MM/DD/YYYY format to match Salesforce display

**Rich text field formatting standard** (applies to Onboarding Notes, How Are We Being Used, Product Pain Points):
- Use **bold** for all section headers
- Use bullet points for any list of items — contacts, action items, milestones, risks, workarounds, etc.
- Keep prose paragraphs short; prefer bullets over run-on sentences
- Timeline must always be a bullet list (one date per line), never a paragraph
- Product Pain Points entries should each have a **bold header** followed by a short description
- The goal is scannability — someone glancing at the field should immediately see what's important without reading every word
- Do not use raw HTML tags — render as markdown bold/bullets in the response so the user can select and copy directly into Salesforce's rich text editor

---

## Step 5 — Present Recommendations

Present the output as a clearly labeled recommendations block:

```
**COM Field Recommendations — [Customer Name]**
_Copy-paste each value directly into Salesforce. Rich text fields accept markdown bold/bullets._

**Last Interaction** (≤255 chars)
[value]

**Steps to Next Stage** (≤255 chars)
[value]

**Onboarding Notes** (rich text — paste into Salesforce rich text editor)
[full content]

[any additional fields with updates]
```

If any field was not updated (no new information to add), omit it from the output entirely.
Do not include a "no change" note — only include fields with actual recommended updates.

---

## Blackthorn Support Integration

When any Blackthorn product question, unexpected behavior, or configuration issue surfaces
during research or context-gathering — invoke the `blackthorn-support` skill before logging
it as a pain point or leaving it unresolved.

- **High-confidence answer:** Include the answer and a relevant Learning Hub or doc link
  inline in the COM field (e.g., in Product Pain Points or Onboarding Notes). No escalation.
- **Medium/Low confidence:** Include your best answer, flag the confidence level in the field,
  and offer to draft a PFQE post via the `product-feedback-poster` skill.
- **No answer found:** Log as a product pain point and offer a PFQE post.

A documented answer — even a partial one — is more useful than a raw unanswered question
sitting in a COM field.

---

## Integration with Day Prep/Recap

This skill should be invoked after any completed onboarding sync identified during a day recap. If the day-prep-recap skill surfaces that an onboarding call happened, the natural next step is "update the COM record." The user may trigger this explicitly or it may be suggested as a follow-up.

---

---

## Customer Dossier Integration

> This step only applies if the current user is @blackthorn.io domain. Verify with
> `gmail_get_profile` — if the email does not end with @blackthorn.io, skip this section entirely and do not
> mention dossiers.

**Before starting research:** Check for an existing dossier in
`*/mnt/Cowork-OS/customers/`. Convert the customer name to
kebab-case to find the file (e.g., `royal-college-of-psychiatrists.md`). If found, read it
before doing any other research — it will tell you the email domain (for Fathom/Gmail
searches), known contacts, open items, and recent interaction history. This saves significant
research time and surfaces context that external searches alone will not.

**After completing the workflow:** Update the dossier with anything new that surfaced —
new contacts, status changes, decisions made, action items, or a new interaction log entry.
Update the `Last Contact` field in the header. If no dossier exists yet, create one from the
template at `_TEMPLATE.md` in the same folder.
## COM Field Reference (Complete)

For reference, the full COM object has ~170+ fields. The fields above are the ones updated from
interaction context. Other notable fields on the object that are NOT typically updated by this skill
(because they're set once, auto-calculated, or managed by flows):

- `Onboarding_Stage_Picklist__c` — managed by Salesforce flow, don't touch
- Formula fields (`Customer_Account__c`, `Customer_Date__c`, etc.) — read-only
- Roll-up summaries (`Onboarding_Events_Time_Summary__c`, etc.) — auto-calculated
- Lookup fields (`Account__c`, `Opportunity__c`, etc.) — set at creation
- Technical fields (`Production_Org_ID__c`, `Sandbox_Org_ID__c`) — set during setup
- Milestone checkboxes (`App_Installed_into_Production__c`, etc.) — typically updated by the onboarding manager directly or via automation

---

## PM Handoff — SKILL RESULT

When running under PM orchestration, do not surface output directly to the user.
Complete all work, then return a SKILL RESULT block to PM for evaluation:

```
## SKILL RESULT: com-update
Timestamp: [ISO 8601]
Customer: [customer name]
Actions taken: [research sources checked; fields prepared; task sync status]
Findings: [full COM field recommendations block — copy-paste-ready content for all updated fields]
Confidence: [High | Medium | Low]
Gaps/failures: [sources that returned nothing; fields that couldn't be populated; data gaps]
Suggested next: customer-dossier to sync interaction log with what was captured;
  email-templates if a follow-up email to the customer is warranted
Flags for Jared: [any Tier 2 items — note that Salesforce updates require Jared to apply manually;
  flag any flag/escalation recommendations for Jared's review before applying]
```

PM presents the COM recommendations to Jared in consolidated output. Jared applies
the field values to Salesforce directly — Claude cannot write to Salesforce.
