---
name: flagged-onboarding-sync
description: >
  INTERNAL — invoked by PM only. Do not trigger directly on user messages. Use this skill to prepare
  Salesforce COM (Customer Onboarding Management) field updates for flagged customers ahead of a
  flagged onboarding sync meeting. Invoke this skill whenever the user asks to update COM records for
  a flagged customer, prep for a red flag sync, research a flagged onboarding account, or compile
  onboarding notes for Emily and Ashley's review. Trigger phrases include: "update COM for
  [customer]", "flagged onboarding sync", "red flag update", "prep flagged customer records", "COM
  update", "onboarding notes for [customer]", or any time the user pastes in current Salesforce COM
  data and asks what needs updating. Also trigger when the user mentions preparing for a Monday sync
  with Emily and Ashley, or updating flagged reason / onboarding notes / product pain points for any
  customer account.
---

# Flagged Onboarding Sync — COM Update Skill

## What This Skill Does

Prepares updated content for four specific Salesforce COM fields for flagged onboarding customers, ahead of the bi-weekly flagged onboarding sync with Emily Powers and Ashley Wagner. The goal of these updates is to give Emily and Ashley enough context to focus the meeting on **action steps and decisions** — not background.

Emily's exact framing: *"I'm assuming if you flagged it, it's so we can talk through what to do next, not how we got here."*

---

## The Four Fields

Always update all four fields. Each has a specific type and purpose:

| Field | Type | Limit | Purpose |
|---|---|---|---|
| Last Interaction | Text Area | 255 chars, plain text | Most recent touchpoint with date |
| Flagged Reason | Long Text Area | 50,000 chars, plain text | Why the project is flagged — history, gaps, risk |
| Customer Product Pain Points | Rich Text Area | 32,768 chars | Specific product limitations the customer has hit |
| Onboarding Notes | Rich Text Area | 50,000 chars | Forward-looking: status, options, questions for the meeting |

**Rich Text fields** should use bold headers and paragraph breaks — not raw HTML tags. Plain text fields are plain text only.

Every field must include a date.

---

## Gotchas

Failure modes specific to this workflow — check before writing any of the four fields.

- **Flagged Reason is plain text only.** No markdown bold, headers, or bullets will render in this field. Write in plain paragraphs. Bullets are acceptable if they genuinely improve readability (e.g., timeline lists), but no `**bold**` or `##` headers.
- **Onboarding Notes must be forward-looking, not a history log.** Emily's explicit framing: *"I'm assuming if you flagged it, it's so we can talk through what to do next, not how we got here."* Status, Action Plan, and Questions for Monday — not a timeline recap.
- **Questions for Monday must require Emily or Ashley's input.** Don't write questions Jared can answer himself. If a question doesn't need leadership authority or roadmap knowledge, it doesn't belong here.
- **Never include Fathom sentiment scores.** Ratings like "40/100" or "customer sentiment: medium" are speculative AI outputs. Exclude them entirely. Only include factual claims from primary sources or clearly attributed high-signal observations.
- **Every field must include a date.** Stale-looking fields undermine the sync. If you can't confirm a recent date, flag it explicitly rather than leaving the field undated.
- **Don't start research without COM data.** If the user hasn't shared the current COM record, ask for it before doing anything. Research without the baseline wastes time and leads to gaps.
- **255-char limit on Last Interaction.** Count characters before finalizing — this field is easily over-run.

---

## What the User Typically Provides

Understanding what the user has already gathered helps you know what to research vs. what to just synthesize. Common inputs:

- **COM Project Overview** — the user copies and pastes the relevant sections from the Salesforce COM record (stage, flagged category, existing field content). This is the baseline.
- **Fathom Deal Summary** — a copy/paste of Fathom's AI-generated summary for the account. Useful for surfacing context from recorded calls, but needs careful handling (see Step 2, item 5).
- **Call transcripts** — occasionally the user will paste in a specific transcript excerpt when a Fathom claim is uncertain or needs verification. These are authoritative.

If the user hasn't shared COM data yet, ask for it before researching.

## Step 1 — Review the Current COM Data

When the user shares the COM record, review it carefully:
- What stage is the customer in?
- What's the flagged category?
- How stale is the existing content?
- Are there product pain points already captured, or is that field empty?

---

## Step 2 — Research Sources

Work through these sources in order. Stop when you have enough to write all four fields.

### 1. Slack Swarm Thread (if one exists)
Before searching, read the `slack-search` skill (find it at `find /sessions -path "*/mnt/.skills/skills/slack-search/SKILL.md" 2>/dev/null | head -1` — or the remote plugin path at `find /sessions -path "*plugin*/skills/slack-search/SKILL.md" 2>/dev/null | head -1`) and follow its search strategy and modifier guidance.

Ask the user if there's a swarm channel. If yes, search it by channel ID. Read the full channel — look for: current blockers, product ticket numbers, churn risk flags, go-live decisions, timeline changes, anything posted in the last 3 weeks.

If no swarm exists, search Slack more broadly (customer name in #obms-and-pms or other relevant channels) for any recent mentions.

### 2. Gmail
Search for emails involving the customer in the last 3 weeks. Look for:
- Email threads with customer contacts
- Internal follow-up threads
- Meeting recaps or follow-up notes

Read the actual email bodies — subject lines alone aren't enough. If a thread is very long, focus on the most recent messages.

### 3. Google Calendar
Search calendar events for the customer name in the last 3 weeks. For any meetings found, note: date, attendees, and meeting title. If there's a recording or Fathom recap linked, note it.

### 4. Google Drive
Check for any relevant docs — onboarding plans, risk assessments, kickoff notes, or product feedback documents. Read them if recent or directly relevant.

### 5. Jira (if tickets are mentioned)
If the user references a Jira ticket number (e.g., ATT-14), search for it to get current status, priority, assignee, and any recent activity. Include the ticket number, status, and any relevant timeline details in the Pain Points and Flagged Reason fields. If a ticket is unresolved and blocking go-live, that's a primary flag signal worth surfacing in Onboarding Notes.

### 6. Fathom (live API lookup — use proactively, do not wait for user to provide)

Invoke the Fathom skill directly by reading and following the instructions in the `fathom` skill.
Do not wait for the user to paste in a Fathom summary — pull it yourself.

Run this in parallel with Slack and Gmail research. At minimum, pull summaries and action items.
Only fetch full transcripts when you need to verify a specific claim.

For high-stakes moments (churn signals, competitor mentions, hard deadlines, escalations), call
`fathom_get_summary` on that recording to get the timestamp-linked version. Embed those links
inline within the COM field text — hyperlink the relevant phrase so Emily and Ashley (or anyone
reviewing the record) can jump directly to the moment. Don't add separate URL lines; the link
should live naturally within the sentence it references.

To invoke: read the fathom SKILL.md, load the API key, then run the layered search strategy
using the customer account name and domain. Ask for domain if not known.

Apply these rules to Fathom data when writing COM fields:

**Always exclude:** Sentiment scores, star ratings, and vague satisfaction assessments (e.g.,
"customer sentiment 40/100"). These are speculative and not reliable enough for fields Emily and
Ashley will act on.

**Include directly** if confirmed from primary sources (email, Slack, transcript): factual claims
like event dates, feature timelines, attendee counts, competitor mentions.

**Include with attribution** for high-signal claims you can't verify but that are decision-relevant —
e.g., "Customer mentioned considering Cvent as an alternative (per Fathom)." Churn signals and
hard deadlines are worth flagging even unverified.

**When a Fathom claim is uncertain and high-stakes**, use the transcript fetch (Layer 4 in the
Fathom skill) to verify directly rather than asking the user to dig it up. If the transcript
doesn't resolve it, draft specific Ask Fathom questions for the user:

Example Ask Fathom questions:
- "For [Customer Name]: In the [Month DD, YYYY] onboarding meeting, did [Contact Name] mention [competitor/alternative] as an alternative? If so, what were the exact concerns they raised and who raised them?"
- "For [Customer Name]: Was a specific event date or go-live target mentioned in any call? If so, what was the date and what event was it for?"
- "For [Customer Name]: Did anyone from the customer side mention the number of events they run per year, or the expected number of registrations? If so, what were the figures and who provided them?"

---

## Step 3 — Write the Four Fields

### Last Interaction (255 chars, plain text)
One or two sentences covering the most recent touchpoint. Always include the date. Stay within 255 characters — count carefully.

Good example:
> 3/12/26 - Seetha Aiyar (Tithee OOO) asked re: attendees report & form submission answers for 3 upcoming events. OBM provided guidance; items tabled until Tithee returns 3/16. Mobile check-in confirmed resolved.

---

### Flagged Reason (plain text)
This is the "how we got here" field — Emily and Ashley use it to understand the situation before the meeting. Include:
- The flag category and a one-sentence summary of why
- The core gaps or blockers, with specifics (ticket numbers, feature names, dates)
- A timeline of key events with dates
- Current status as of today
- Risk factors (renewal pressure, churn signals, competitor mentions, budget strain)

Write in plain paragraphs with labeled sections. Use bullet points when they improve scannability — for timelines, risk factors, and lists of blockers, bullets are often clearer than prose.

---

### Customer Product Pain Points (rich text)
Document specific product limitations the customer has encountered. Each pain point should be a numbered bold header with a paragraph explaining: what the gap is, why it matters to this customer, any workarounds in place, and current status/resolution.

Include only real product gaps — not process issues, access problems, or configuration items. If there are no product pain points yet (e.g., customer is stalled before product evaluation), say so explicitly.

---

### Onboarding Notes (rich text)
This is the most important field for the meeting. Emily doesn't want a history log here — she wants to know **what to do next**. Structure it like this:

**Status as of [date]**
Two to four sentences on where things stand right now.

**Action Plan Ideas / Options**
Concrete options for moving forward. If there's a decision to be made, lay out the choices. If there's a concession to consider, name it. If the customer needs a difficult conversation, say who should have it.

**Questions for Monday**
Specific questions the onboarding manager wants to bring to Emily and Ashley. These should be things that require their input, authority, or roadmap knowledge — not things the onboarding manager can answer themselves. Make them sharp and specific, not generic.

For each question, include a brief anticipatory note where possible — specifically, a question Emily or Ashley is likely to ask the onboarding manager in response. Keep these concise (one sentence). This helps the onboarding manager walk in prepared rather than caught off guard.

---

## Step 4 — Format Check

Before presenting the output:
- Last Interaction: count characters, must be ≤255
- Flagged Reason: plain text only, no markdown symbols that won't render
- Onboarding Notes and Pain Points: use **bold** for headers, paragraph breaks between sections — no raw HTML

---

## Step 5 — Task Sync

After presenting the four fields, reconcile TASKS.md with what the research surfaced for this flagged customer.

**TASKS.md location:** `*/mnt/Cowork-OS/Productivity/TASKS.md`

Find and read it:
```bash
find /sessions -path "*/mnt/Cowork-OS/Productivity/TASKS.md" 2>/dev/null | head -1
```

Work through three passes:

**Pass 1 — Mark Complete:** Check Active and Waiting On for any task related to this customer. If research shows the item was resolved (an escalation was sent, a case was closed, a decision was reached), mark it done with today's date and move to Done.

**Pass 2 — Update Existing:** If a task for this customer exists but wasn't resolved, update the context line to reflect current status and the date you last touched it.

**Pass 3 — Add New:** Surface tasks from the COM prep that aren't already tracked. Pull from:
- "Questions for Monday" from the Onboarding Notes field — each one is a potential task or escalation to track
- Action Plan items that require a follow-up between now and the sync
- Escalations waiting on a response (product team, Emily, Ashley)
- Any explicit commitment made to the customer that isn't already logged

**Format for new tasks:**
- Active: `- [ ] **[Task title]** - [context], for [customer], due [date if known]`
- Waiting On: `- [ ] **Waiting: [what]** - from [person/team], since [today's date]`

Write to TASKS.md autonomously — this is Tier 1 work, no confirmation needed.
Report what was changed in the SKILL RESULT (Actions taken field). If there's nothing
to update, skip silently.

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
---

## Blackthorn Support Integration

When any Blackthorn product question, unexpected behavior, or configuration issue surfaces
during this workflow — invoke the `blackthorn-support` skill before logging it as a pain
point, leaving it unanswered, or escalating to PFQE.

- **High-confidence answer:** Document it inline (in the dossier, COM field, or email draft)
  with a relevant Learning Hub or doc link. No further escalation needed.
- **Medium/Low confidence:** Include your best answer, flag the confidence level, and offer
  to draft a PFQE post via the `product-feedback-poster` skill.
- **No answer found:** Log as an open question or product pain point and offer a PFQE post.

A documented answer — even partial — is more useful than an unanswered question.

---

## Context: The Flagged Onboarding Sync

This is a bi-weekly meeting between the OBM (you) and Emily Powers + Ashley Wagner (leadership). Customers are flagged when they have: product issues blocking go-live, skill/resource gaps on the implementation team, misaligned expectations from the sales process, or unresponsive/stalled accounts.

Emily's goal: read the COM fields before the meeting so discussion time is spent on what to do, not what happened. If a customer's record is stale or light on detail, the meeting derails into background instead of decisions.

The four fields map to that goal:
- **Last Interaction** = what's the latest signal?
- **Flagged Reason** = why are we here?
- **Pain Points** = what does the product need to fix?
- **Onboarding Notes** = what do we do next, and what do we need from you?

---

## PM Handoff — SKILL RESULT

When running under PM orchestration, do not surface output directly to the user.
Complete all research and field preparation, then return a SKILL RESULT block to PM.

PM may ask clarifying questions for high-stakes decisions — but only after completing
all Tier 1 work. PM will escalate to Jared only if: (a) the answer would materially
change what gets recommended, or (b) the situation could result in a damaging interaction
with a customer or coworker. All other decisions PM handles autonomously.

```
## SKILL RESULT: flagged-onboarding-sync
Timestamp: [ISO 8601]
Customer: [customer name]
Actions taken: [sources researched; four fields prepared; character counts verified]
Findings: [all four COM fields fully prepared — Last Interaction, Flagged Reason,
  Customer Product Pain Points, Onboarding Notes — formatted and ready for Salesforce]
Confidence: [High | Medium | Low]
Gaps/failures: [data gaps; sources that returned nothing; fields that needed assumptions]
Suggested next: None — COM field recommendations ready for Jared to apply in Salesforce.
  customer-dossier update if new info surfaced during research.
Flags for Jared: [high-stakes decisions that need human judgment — contract concerns,
  escalation language from customer, decisions about flag category or next-step framing
  where the choice could affect the customer relationship; present these AFTER all fields
  are prepared, not mid-workflow]
```
