---
name: day-prep-recap
description: >
  INTERNAL — invoked by PM only. Do not trigger directly on user messages. Day preparation and meeting
  recap assistant for the Blackthorn team. Use this skill whenever the user asks to prep for their
  day, recap their day, prepare for a specific meeting or call, or review what's coming up. Trigger
  phrases include: "prep me for today", "morning prep", "end of day recap", "recap my day", "prepare
  for my call with [customer]", "what do I have today", "help me get ready for [meeting]", "office
  hours prep", "what happened today", and any request to review upcoming meetings or summarize a
  completed day. Also trigger when the user asks about a specific customer meeting, QBR, account
  review, or implementation call. This skill should be used proactively — if the user mentions
  meetings, calendar, customer calls, or wanting to be prepared for anything on their schedule, invoke
  it.
---

# Day Prep & Recap

This skill helps Blackthorn team members prepare for or recap their workday — pulling calendar
events, finding relevant email and Slack context, triaging the inbox, surfacing stale drafts and
unanswered questions, and generating meeting briefings that go beyond the obvious. It infers the
business need behind what customers are asking, not just summarizing what they said.

The full brief is delivered as a Slack DM and archived as an HTML file — so it's accessible on
mobile, between meetings, and for future reference.

---

## Step 0: Identify the User

This skill is designed to work for anyone — nothing is hardcoded to a specific person.

1. **Get the user's identity**: Call `gmail_get_profile` to get their name and email address. Use their first name (lowercased) throughout the output and for channel naming.
2. **Find their briefing channel**: Search Slack for a channel named `{firstname}-briefing` (e.g., `jared-briefing`, `dustin-briefing`). Use `slack_search_channels` with that name. If found, store the channel ID — this is where the full brief will be posted. If not found, tell the user: *"I couldn't find a `{firstname}-briefing` channel in Slack. Create a private channel with that name, star it for easy access, and I'll post your daily brief there."* Then skip the Slack delivery step for this run.
3. **Determine their team**: Call `slack_read_user_profile` with the user's Slack ID and check their **Title** field. If the title contains "onboarding" (case-insensitive), they are on the Onboarding team — include the COM Portfolio Snapshot (Step 6). If not, skip Step 6 but offer the **Subscribed Report** alternative (see Step 6 notes).
4. **Determine their workspace path**: Use the current session's workspace path for saving the HTML archive (e.g., the `Claude/` directory accessible to the user).
5. **Post a start notification**: If the briefing channel was found, immediately post a single line to it: `🔄 Daily prep running — brief incoming shortly.` This ensures there is always a signal in the channel even if the session gets interrupted before the full brief is ready.

All Blackthorn-specific context below (support skill, Learning Hub, industry context) applies to everyone using this skill.

---

## Completion Gate — Non-Negotiable

**Do not engage with any specific email thread, draft any replies, investigate any individual customer issue, or have any interactive conversation with the user until Steps 9 and 10 are both complete** (HTML saved, full brief posted to Slack).

During the research phase, you will surface "Reply Needed" items, overdue drafts, and open customer threads. These are for the brief — not for immediate action. If the user tries to engage with a specific item before the brief is posted, acknowledge it briefly and defer: *"I'll get to that right after the brief is posted — almost there."* Then finish.

The Slack post is the deliverable. Everything else is follow-up. Complete the deliverable first.

---

## Step 0.5: Read TASKS.md

Before doing any research, read the current task list. This gives you a baseline of what's already tracked so you can cross-reference it against what you find — and avoid duplicating work or missing updates.

**Find and read TASKS.md:**
```bash
find /sessions -path "*/mnt/Cowork-OS/Productivity/TASKS.md" 2>/dev/null | head -1
```

From the Active and Waiting On sections, extract:
- Tasks due today (any with today's date or "due today")
- Overdue tasks (past due dates)
- Tasks related to customers who have meetings today
- Tasks that look like they may have been completed based on what you'll find in research (e.g., "send follow-up to X" — if a sent email to X shows up later, mark it resolved)
- **Undated active tasks** — open tasks in Active with no due date (no 📅 marker and no "due" text). These are candidates for the Suggested Work section in the brief. Cap at 3-5 to avoid overwhelming — prioritize by customer urgency or time sensitivity if you can infer it.

Keep this in working memory. You'll use it in two ways:
1. **In Step 6** — when building the Client Snapshot, cross-reference Needs Attention accounts with open tasks. If a task already exists for that account, note it so the user knows it's being tracked.
2. **In Step 11** — after posting the brief, reconcile what you found with TASKS.md: close out completed items, update stale ones, and add anything new that surfaced.

**Skip this step in Single-meeting mode** — TASKS.md integration only applies in full Prep and Recap modes.

---

## Step 1: Determine Mode and Scope

### Mode
- **Prep** — Morning or pre-day overview of what's coming up. Forward-looking. What to expect, what questions might come up, how to be ready. Includes full inbox triage, draft queue, and awaiting-reply scan.
- **Recap** — End-of-day summary of what happened. Focus on open action items and follow-ups, carefully distinguishing what's already been handled from what hasn't.
- **Single-meeting** — User asks about "next call", "my 2pm", or a specific customer. Scope tightly to just that meeting. Skip inbox triage, draft queue, and awaiting-reply sections.

### Scope rule
If the user asks about a specific meeting or "next call", treat it as Single-meeting mode and only cover that one. Don't expand to a full day overview unless explicitly asked.

---

## Step 2: Pull Today's Calendar

Use Google Calendar to get the relevant events.

- **Prep**: all upcoming events today (or from now forward if mid-morning)
- **Recap**: all events that have ended today
- **Single-meeting**: find the specific meeting or the next upcoming one

Filter out blocks with no attendees (focus blocks, OOO, reminders). Keep customer calls, internal meetings with other people, Office Hours, and recurring syncs.

---

## Step 3: Classify Each Meeting

Assign a tier to each meeting. This drives how deeply to research it.

### Tier 1 — Deep Dive (6-month email + full Slack lookback)
Apply when:
- It's an internal meeting where a specific customer is being reviewed (e.g., "Acme account review")
- Title/description signals strategic depth: QBR, business review, account strategy, deep dive, implementation review, use case analysis

Be comprehensive — this is a research-heavy briefing.

### Tier 2 — Standard (7-day email + Slack lookback)
Most customer-facing calls: Office Hours, onboarding syncs, check-ins, demos, general follow-ups.

### Tier 2.5 — One-on-One Internal (person-scoped, 30-day AI recap lookback)
Apply when **all** of the following are true:
- Exactly 2 attendees (you + one other person)
- Both attendees share the same email domain (i.e., both internal/Blackthorn)
- It is not a customer call

Common title patterns that signal this tier: `[Name]/[Name]`, `1:1 with [Name]`, `Weekly sync with [Name]`, `[Name] check-in`, `[Name] <> [Name]`.

- Search email and Slack for the last **7 days** scoped to that specific person
- Search for AI notetaker recap emails from the **last 30 days** scoped to that person — track themes and conversations over time
- See dedicated output format in Step 8

### Tier 3 — Lightweight (quick Slack/email scan)
Internal-only meetings that are not 1:1s: group meetings (3+ attendees), all-hands, standups, or brief syncs where the agenda is fully clear from the calendar description and no research is needed.

### Office Hours / Explicit Questions → Always apply 6-part analysis
If a meeting is "Office Hours" or similar, or if the calendar description or recent emails contain specific customer questions — always apply the **Question Analysis Framework** (see Step 7), regardless of tier. This is the highest-value signal: when you know what the customer is asking, go deep on it.

---

## Step 4: Pull Context

### Email (Gmail)

**For customer meetings (Tier 1 and 2):**
Search for emails involving attendees from the customer's company and any identified implementation partners.

- General email context: last 7 days
- **AI notetaker recap emails: last 30 days** — these can be 2+ weeks old and are among the richest sources of prior call context. Search explicitly: `"Fathom" OR "Coworker" OR "Otter" [customer/person name]` with a 30-day window.

For 6-month Tier 1 lookbacks, extend the general window to 6 months as well.

Implementation partners are typically contracted implementation partners — identify them by their presence on email threads or calls with the customer.

**Prior commitments — extract for any recurring customer sync:**
If a prior AI notetaker recap exists for this customer (regardless of meeting title format — don't rely on naming conventions), treat this as a recurring sync and explicitly extract what each party committed to before the next call. This is one of the highest-value prep inputs: it tells you what the customer expects you to have done, and what they were supposed to do. Pull it explicitly and surface it in the output.

- **Their homework**: action items the customer or their implementation partner committed to (e.g., DKIM setup with IT, building a test event, distributing access links to their team, completing learning assignments, testing a configuration)
- **Your homework**: items you committed to (e.g., testing a behavior, filing a product enhancement request, sending a follow-up email, forwarding documentation, asking the product team a question)
- **Tabled items**: anything explicitly deferred to the next call

Once extracted, cross-reference each item against recent email and Slack to determine whether it was completed — same "already handled" logic used in recap mode. The goal is walking into the call knowing exactly what's done and what isn't, so you can address gaps proactively rather than discovering them live.

If no prior recap exists for this customer (first call, or none in the 30-day window), skip this section entirely.

**For 1:1 internal meetings (Tier 2.5):**
- Scope all email and Slack searches to the specific person's email address and name
- AI notetaker recaps: last 30 days scoped to that person — find the most recent 1:1 recap with them to surface prior action items and themes

### Slack

**Full sweep first — this is required, not optional.**

Before doing any targeted customer or meeting searches, run a broad sweep of all Slack activity since the last prep run. This is the step that catches signals targeted searches miss: teammate requests in internal channels, direct messages from colleagues, customer mentions buried in channels you aren't actively monitoring, and new threads that haven't been linked to any specific task yet.

**How to run the sweep:**

1. Determine the cutoff date — use yesterday's date (or the date of the last day-prep run if known). Format: `YYYY-MM-DD`.
2. Call `slack_search_public_and_private` with query `after:YYYY-MM-DD` — this sweeps all channels and DMs you are a member of.
3. **Page through all results.** Don't stop at the first page. Keep paginating until the full window is covered. Missing the second page means missing real signals.
4. For any message that has replies, read the full thread — a short opener can hide a complex request or decision chain underneath.

**What to surface from the sweep:**

- Direct messages from teammates with requests, questions, or time-sensitive items
- Mentions (@you) with any ask or action attached
- Messages in internal channels (onboarding team, product, CX, CS) where your accounts or open items are discussed
- New threads touching accounts in your portfolio that you haven't seen yet
- Anything where someone is clearly waiting for a response or action from you
- Signals from AEs or teammates about incoming accounts (pre-kickoff context, license provisioning requests, etc.)
- Teammate questions in shared channels (e.g., #onboarding-team) where you might have relevant context to contribute

**What to skip:**

- Pure FYI threads with no action signal
- Channels with only routine automated notifications (bot alerts, system messages)
- Threads fully resolved before the cutoff date

After completing the sweep, store the signals. They feed into:
1. **Inbox Triage** — Slack items needing replies or action go alongside email items here
2. **Slack Signals section** in the brief — a dedicated section for notable Slack activity that doesn't fit neatly into a specific meeting prep (see output format in Step 8)
3. **Step 11 Task Sync** — new tasks surfaced from Slack get added to TASKS.md

**Then run targeted searches** for each meeting's customers, attendees, and topics — same as before. The full sweep is additive, not a replacement for meeting-specific searches.

For 1:1s, scope the targeted search to direct messages and threads exchanged with that specific person.

For recap mode, also check messages you sent *after* each meeting end time — these often confirm what follow-ups were already handled.

### What to surface (and what to skip)

When reviewing email and Slack for the day overview sections (not meeting-specific context), apply this filter:

**Include:**
- Emails or threads where action is needed or overdue
- Things you said you'd do and haven't done yet (follow-ups you committed to)
- Urgent or time-sensitive items
- Replies from customers or partners that need a response

**Skip:**
- Unread count summaries
- Promotional emails, marketing, conference invites
- System error alerts unless someone specifically replied about them
- Slack channels with only archival/old content not relevant to today

The goal is a clean action-oriented picture, not an inbox audit.

### Fathom Meeting History

For any Tier 1 or Tier 2 customer meeting, invoke the Fathom skill to pull recorded meeting
context for that customer. Read the fathom SKILL.md and follow its layered search strategy.

Run in parallel with Gmail research. Use summaries and action items by default. This is
especially valuable for:
- Single-meeting prep: surface what was discussed in the last 1–3 calls with this customer,
  what action items were left open, and any patterns across meetings
- Tier 1 deep dives: get a full picture of the relationship history from recorded calls
- Any meeting where prior commitments need to be tracked (Fathom action items complement the
  AI notetaker recap emails you pull from Gmail)

For internal-only meetings (Tier 3) and 1:1s (Tier 2.5), skip Fathom unless the meeting topic
is specifically about a customer account.

When surfacing high-stakes moments from Fathom calls (prior commitments, escalations, churn
signals, open blockers), call `fathom_get_summary` on the relevant recording to get the
timestamp-linked version. Embed those links inline in the prep brief — hyperlink the relevant
phrase so Jared can jump directly to the moment before walking into the meeting.

---

### Blackthorn Reference Files

Use this lookup order — local first, Google Drive as fallback only if local files are not found.

**Step 1 — Check local files first:**
```bash
find /sessions -path "*/mnt/Cowork-OS/reference/product-docs" -type d 2>/dev/null | head -1
```
If this returns a path, the reference folder is available locally. Use it. Local reads are fast and always current.

Key files in `reference/product-docs/`:
- `Blackthorn Events - February 2026.md` — primary reference for all Events questions
- `Blackthorn Payments - February 2026.md`, `Blackthorn Messaging - February 2026.md` — other products
- `Blackthorn Compliance - February 2026.md`, `Blackthorn Badge Generation - February 2026.md`, `Blackthorn Smart Capture - February 2026.md`
- `BLACKTHORN_PLATFORM_REFERENCE.md` — cross-product platform reference, API names, object schema

Learning Hub CSV (for Resources section):
```bash
find /sessions -path "*/mnt/Cowork-OS/reference/BlackthornLearningHubContent.csv" 2>/dev/null | head -1
```

**Step 2 — Fall back to Google Drive only if local files are missing:**
Root folder ID: `1Wl3gOxlineFdKgekvxgHtIzvVyIYzGZG` | Docs folder ID: `1YgABQJOsZc8w1FA5BeY374EPI7VYQLDG`

Use `google_drive_search` to find files by name, then `google_drive_fetch` to read content (requires files to be in Google Docs format in Drive).

**When to consult either source:**
- Meeting has product/feature/configuration questions
- Email context contains a bug, error, or implementation issue
- Office Hours with submitted questions
- Any Tier 1 or Tier 2 customer meeting where Blackthorn product topics are likely

**When not to:** Internal 1:1s, general business reviews, or meetings with no product signal.

### Blackthorn Product Support Skill
For any Tier 1 or Tier 2 customer meeting, invoke the `blackthorn-support` skill for **every open question, issue, or known product topic** identified during research — not just complex ones. This is the mechanism that populates the Resources / Mitigation options section of the output. If you've surfaced a customer question from an email, a prior recap, a tabled item, or a known bug, look it up before writing the prep. The goal is to walk into the call with an answer (or at least a clear path) already prepared, rather than having to look things up live.

Invoke it for:
- Any specific question the customer has raised (in email, prior recap, or Office Hours)
- Any open bug or error they've mentioned
- Any configuration or architecture question that came up in the prior call and was left open
- Any topic you know will come up based on where they are in onboarding

It follows the same local-first / Drive-fallback pattern.

---

## Step 5: Inbox Triage (Prep mode only)

In Prep mode, scan the inbox (last 48 hours) and categorize each email into one of these triage labels. This creates a structured picture of what needs attention today.

### Triage labels

| Label | Description | Detail level in report |
|---|---|---|
| **Reply Needed** | Someone is waiting on your response — a direct question, a request, a decision needed | **High** — include who's asking, what they need, and any deadline or urgency signal |
| **Action Required** | Not a reply, but something you need to do — a task, a document to review, a form to fill | **High** — include what the action is, who assigned it, and when it's due |
| **Meeting** | Calendar-related — agenda, prep materials, rescheduling, confirmation | **Medium** — note which meeting and any action needed (confirm, prep, reschedule) |
| **Waiting** | You already replied or acted — ball is in someone else's court | **Low** — one-liner: who you're waiting on and what for |
| **FYI** | Informational only — announcements, newsletters, updates, CC'd threads | **Minimal** — subject line and sender only, skip if obviously irrelevant |
| **Provisioning** | Account setup, license assignments, access requests, environment provisioning | **Medium** — note the customer/org and what's needed |
| **Marketing** | Promotional content, event invitations, vendor outreach | **Skip** — don't include in the report unless something is genuinely relevant |
| **Draft** | Handled by the Draft Queue section below — don't duplicate here | **Skip** |

The goal: someone scanning the report should immediately know what needs their attention (Reply Needed / Action Required at the top with full context) and can safely ignore the rest. Don't bury important items in a wall of FYI noise.

---

## Step 5b: Draft Queue (Prep mode only)

Pull all current drafts via `gmail_list_drafts`. For each draft:
- Identify the recipient and subject
- Flag any draft older than 24 hours as **overdue** — these are easy to forget and often represent dropped balls
- Note briefly what the draft appears to be about (from subject/recipient context)

This section surfaces half-finished work that might otherwise slip through the cracks.

---

## Step 5c: Sent & Awaiting Reply (Prep mode only)

Search sent emails from the last 5 days and contextually identify ones where a response is reasonably expected but hasn't arrived. This is NOT a list of all unreplied sent emails — most sent emails don't need a response.

### What qualifies as "awaiting reply"

Surface a sent email only if it meets one or more of these criteria:
- **You asked a direct question** — the email contains a question directed at the recipient
- **You requested an action** — you asked someone to do something and there's no evidence they did it
- **You sent a scheduling link or meeting request** — and no meeting has appeared on your calendar with that person (cross-reference Google Calendar to verify)
- **You're in an active back-and-forth** — the thread had rapid exchanges and then went silent on their end
- **You set a deadline or follow-up date** — and that date is approaching or passed

### What does NOT qualify
- Confirmation emails ("Thanks, got it!")
- FYI forwards with no question
- Auto-responses or system notifications you replied to
- Emails where the thread context makes clear no response was expected

For each surfaced item, note: who you're waiting on, what the open question/request was, and how many days it's been.

---

## Step 6: Portfolio Snapshot (Prep mode only)

This section provides a scannable, visual portfolio overview of the user's accounts. For Onboarding team members, this is the **COM Portfolio Snapshot** built from the Salesforce COM report. For everyone else, this section adapts to whatever subscribed Salesforce report the user provides.

### Who gets this section

- **Onboarding team** (detected in Step 0 via Slack title containing "onboarding"): Full COM Portfolio Snapshot with the interpretation guidance, health indicators, and Needs Attention logic described below.
- **Non-onboarding team**: If this is the user's first run, ask: *"Do you have a Salesforce subscribed report that tracks your accounts or pipeline? If so, what's the report name? I'll pull it from your email each morning and include a snapshot in your brief. If not, I'll skip this section."* Store their answer for future runs. If they provide a report name, pull and display it as a simple table with whatever columns the CSV contains — no COM-specific interpretation logic.

### Getting the data

Search Gmail for the Salesforce subscribed report by its specific name. The user may have multiple subscribed reports, so searching generically for "Salesforce report" is unreliable. Instead, search by the report's known name — e.g., `"Current Onboarding Tracker"` — within the last 24 hours. The email typically arrives on workdays around 8am and includes a CSV attachment. Read the email, download the CSV attachment, and parse it.

If the report name isn't known, ask the user: *"What's the name of your Salesforce report? I'll search for it by name so I grab the right one."*

If no report email is found today, silently skip this entire section — don't prompt the user about it.

### COM report fields

The CSV contains these key columns (field names may vary slightly):
- **Customer Onboarding Management Project** — the account name
- **Onboarding Stage** — where they are structurally (Discovery, Design, Build, Pending First Event, Hyper Care, etc.)
- **Onboarding Status** — health signal (On Track, Late, etc.)
- **Onboarding Stage (New)** — the more current stage classification
- **Next Onboarding Step** — the next structural milestone in their onboarding (not necessarily happening today)
- **Last Interaction** — most recent touchpoint notes
- **Flagged** — whether the account is flagged (1 = yes, 0 = no)
- **Flagged Reason?** / **Flagged Category** — why it's flagged
- **Concerns** — open concerns
- **Onboarding Notes** — detailed status notes
- **Customer's Product Pain Points** — known product issues
- **Days Elapsed** — how long they've been in onboarding
- **Ideal/Planned/Actual dates** — milestone timeline fields
- **Apps Purchased** — which Blackthorn products they have
- **Renewal Date** — contract renewal date

### How to interpret the data

Some important context for reading COM data correctly:
- **"Late" status is common and not an emergency.** Many customers end up Late simply due to their own timelines. It's an awareness signal, not an alarm.
- **Flagged accounts can stay flagged for a while.** A flag persists until explicitly removed — it doesn't mean something is actively on fire right now. Treat it as "keep an eye on this."
- **Days Elapsed varies wildly.** Some customers onboard in 20 days, others take 6+ months. High days elapsed alone is not a problem — it's contextual.
- **Next Onboarding Step** is structural, not temporal. It describes _what_ happens next in the onboarding journey, not _when_.

### What to surface

Cross-reference the COM data with today's calendar, this week's calendar, recent email, and Fathom to build the snapshot:

1. **Customers with meetings today or this week** — pull their COM row and surface: stage, status, next step, last interaction, any concerns or flags. This context feeds directly into the meeting prep sections.

2. **Needs Attention** — customers that warrant a callout. Apply these filters:
   - Flagged accounts — note the flagged reason/category
   - Accounts with upcoming milestone dates (Ideal/Planned dates) in the next 14 days
   - Accounts where **Last Interaction** is stale — cross-reference with email and calendar to identify customers you haven't interacted with in 2+ weeks. This is one of the highest-value signals: accounts quietly going cold.
   - Accounts where a scheduling link was sent but no meeting is on the calendar (cross-ref with Sent & Awaiting Reply)
   - Renewal dates approaching in the next 60 days

3. **All Clear** — everyone else. Just list them by name so the user knows their full portfolio was reviewed.

### Output format — Client Snapshot

This section should be highly visual and scannable — use color indicators and a compact table format. In the Slack DM (mrkdwn) and HTML report, render it like this:

**In HTML (for the saved report):**
Use a styled table with colored health indicators:
- 🟢 On Track (green)
- 🟡 At Risk / Late (yellow) — for accounts that are Late or have concerns
- 🔴 Flagged (red) — for actively flagged accounts
- 🟣 New (purple) — for accounts less than 7 days in

**In Slack:**
Use bold headers, emoji health indicators, and a **code block table** for the portfolio grid. The Slack MCP connector uses **standard markdown** — use `**bold**` (double asterisks) for bold, `_italic_` for italic. Do NOT use Slack's native mrkdwn single-asterisk bold — it won't render correctly through the connector.

The Client Snapshot table should be inside a code block (triple backticks) for alignment. Emoji renders inside Slack code blocks. Use fixed-width columns so names, stages, and health indicators line up cleanly. Pad shorter names/stages with spaces to keep columns aligned.

Example:
````
**📊 Client Snapshot — [Date]**

```
Client                     Stage            Health      Next Mtg      Days
─────────────────────────  ───────────────  ──────────  ────────────  ────
[Name]                     [Stage]          🟢 On Time  [date]         [n]
[Name]                     [Stage]          🟡 Late     [date]         [n]
[Name]                     [Stage]          🔴 Flagged  TBD            [n]
```

**⚠️ Needs Attention**
• **🟡 [Customer]** — [Why: e.g., "Late, no interaction since 3/1, renewal in 45 days"]
• **🔴 [Customer]** — [Why: e.g., "Flagged: engagement issues. No reply from contact since 3/12."]

**✅ All Clear**
[Customer], [Customer], [Customer], [Customer]
````

Keep the Needs Attention and All Clear sections **outside** the code block so bold and emoji formatting render with full richness.

**Next Mtg** = the next calendar event found with this customer. If none found in the next 21 days, show "TBD" — and if they're more than 7 days in with no meeting, that's a "Needs Attention" signal.

The Needs Attention section should include enough context to be actionable without clicking into anything else. The All Clear section is just names — a quick confirmation that the rest of the portfolio was reviewed and nothing stood out.

---

## Step 7: Apply the Question Analysis Framework

When you have specific questions or concerns from the customer (from calendar description, email, or Office Hours submission), analyze each one using this framework. Do not just paraphrase — infer the business or operational need beneath the question and explain your reasoning briefly.

**For each customer question or concern:**

- **Surface ask** — What they literally said or asked
- **Underlying need** — What they are trying to achieve, avoid, prove, or decide
- **Trigger** — What likely prompted this question now (timing, recent event, pain point)
- **Category** — Pick one: bug, configuration gap, skill gap, unsupported architecture, process confusion, expectation mismatch, or strategic/product need
- **Urgency** — What happens if this is not addressed (business impact, timeline, user trust)
- **Recommended response posture** — Pick one: educate, troubleshoot, reset expectations, propose workaround, escalate internally, or push for customer decision

---

## Step 8: Generate Output

### Output Format — Standard Prep

In Slack, use bold section labels and emoji to make each meeting block easy to scan. The Slack MCP connector uses **standard markdown** — use `**bold**` (double asterisks), not single-asterisk mrkdwn:

```
**📅 [Meeting Title] — [Time]**
[2-3 sentence summary: what this meeting is, who it's with, what to expect]

**Attendees:** [list, noting company/role where known]
**Recent context:** [what's top of mind for this customer — specific email threads, Slack signals, AI recap highlights]

**Since last call** _(only if a prior recap was found — skip entirely if this is a first call or no prior recap exists)_:
• _Their homework:_ [what they committed to — with status: ✅ done / ⚠️ unclear / ❌ not done]
• _Your homework:_ [what you committed to — with status: ✅ done / ⚠️ unclear / ❌ not done]
• _Tabled:_ [anything explicitly deferred to this call, if any]

**Prep / What to know:** [specific things to be ready for, talking points, background]
**Resources / Mitigation options:** [answers, workarounds, or Learning Hub links sourced from the `blackthorn-support` skill for each open question or issue identified — one entry per question/issue]

[If questions exist — apply Question Analysis Framework for each one]

**[Question or topic]**
• _Surface ask:_ ...
• _Underlying need:_ ...
• _Trigger:_ ...
• _Category:_ ...
• _Urgency:_ ...
• _Recommended response posture:_ ...
```

**For single-meeting mode**: same format, scoped to just that one meeting. No other meetings, no inbox triage, no draft queue.

---

### Output Format — Recap

```
## [Meeting Title] — [Time]
[2-3 sentence summary of what the meeting was and key outcome]

- **What happened**: [brief note on outcome if inferable from emails/Slack post-meeting]
- **Follow-ups still open**: [action items with no evidence of resolution]
- **Already handled**: [items addressed — e.g., "Sent follow-up email at 12:30pm", "Replied in Slack thread about permissions"]
```

At the end, a **Day Summary** section:
- Any urgent items from email or Slack that need attention (not already covered in meeting follow-ups)
- Only items that are actionable — not a general inbox summary

---

### Output Format — 1:1 Internal Prep (Tier 2.5)

```
## 1:1 with [Name] — [Time]
[1-2 sentence framing: cadence and general purpose of these 1:1s]

### Last 1:1 recap
[Key points from the most recent AI notetaker recap with this person — what was discussed, what was decided]

- **Open action items from last session:**
  - [Item you committed to] — [done / still open]
  - [Item they committed to] — [done / still open]

### What you've been working on
[Brief summary of your recent activity over the past week — from sent emails, Slack messages, and calendar. Captures themes: what you've been focused on, what you've shipped, resolved, or driven. This is your memory anchor for the conversation.]

### What they've been working on
[Based on their recent emails and Slack to you and any shared threads — what's on their plate, what they've been driving]

### Things to raise
- **Issues / escalations**: [any problems that have surfaced recently — from email, Slack, or customer patterns]
- **Problem accounts or situations**: [anything showing stress signals in recent context]
- **Blockers / asks**: [things you need from this person — decisions, unblocking, approvals]

### Wins to share
[Accomplishments since the last 1:1 worth calling out — shipped things, resolved issues, positive outcomes, customer feedback]

### Friction signals
[Optional — only include if relevant: recurring themes, unresolved tensions, or patterns in recent threads worth being aware of going in]
```

---

### Output Format — Inbox Triage Section (Prep mode only)

This section appears before the meeting prep sections in the full brief. Use bold headers and visual separators throughout — the user should be able to scan this in seconds. The Slack MCP connector uses **standard markdown** — use `**bold**` (double asterisks) for bold text.

```
**📬 Inbox Triage**

**Reply Needed**
• **[Sender]** — [Subject]: [What they need from you. Any deadline or urgency signal.]
• **[Sender]** — [Subject]: [Context and what's being asked.]

**Action Required**
• **[Sender/Source]** — [Subject]: [What needs to be done, who assigned it, when it's due.]

———

**📝 Draft Queue**
• **To: [Recipient]** — [Subject] — started [date] **⚠️ OVERDUE**
• **To: [Recipient]** — [Subject] — started [date]

———

**⏳ Sent & Awaiting Reply**
• **[Recipient]** — [Subject] — sent [date]: [What you're waiting on]
• **[Recipient]** — [Subject] — sent [date]: [Scheduling link sent, no booking yet]

———

**Meeting-Related**
• [one-liner per item: which meeting, any action needed]

**Waiting On Others**
• [one-liner: who and what]

**Provisioning**
• [customer/org and what's needed]

**FYI**
• [subject line and sender — minimal, only if worth noting]
```

---

### Output Format — Slack Signals Section (Prep mode only)

This section appears after Inbox Triage in the full brief. It surfaces everything notable from the full Slack sweep that didn't get absorbed into a specific meeting prep block. The goal is a clean list of Slack-sourced signals the user needs to be aware of today — not a log of everything posted.

Only include this section if the sweep surfaced something worth acting on or knowing. If the sweep was clean, skip it silently — don't write "no Slack signals."

```
**💬 Slack Signals**

**Action / Reply Needed**
• **@[Person] in #[channel]**: [What they asked or need — one line with enough context to act on it]
• **DM from [Person]**: [What they said and what's needed from you]

**Heads Up (FYI)**
• **[Person] in #[channel]**: [Brief summary of what's worth knowing — no action required]

**Account Mentions**
• **[Customer name]** mentioned in #[channel] by [Person]: [What was said — surface if it's new context or changes the picture]
```

Only include sub-headers that have content. If there were no "Heads Up" items, omit that header entirely rather than leaving it empty.

---

### Output Format — Suggested Work Section (Prep mode only)

This section appears at the end of the brief, after Slack Signals and meeting prep blocks. It surfaces open active tasks that have no due date — tasks that are tracked but could slip indefinitely without a nudge. The goal is to prompt Jared to either tackle one today or assign a date so it doesn't stay open forever.

Only include this section if there are undated active tasks from Step 0.5. If all active tasks have dates, skip it silently.

```
**🗂 Open — No Due Date**
These are tracked but undated. Worth tackling today or assigning a deadline:

• **[Task title]** — [one-line context on what it is and why it matters now]
• **[Task title]** — [one-line context]
• **[Task title]** — [one-line context]
```

Keep the list to 3-5 items max. If there are more undated tasks than that, surface the ones most likely to matter today based on customer urgency, recency, or dependencies. Don't list every undated task — be selective.

---

### Email exchange summaries (for single-meeting or Tier 1 deep dives)

When summarizing an email thread, present it as a brief **conversation summary** — a combined view of the back-and-forth, not split by sender. Use a few bullet points to capture the arc of the conversation, then a separate **Open topics** section for anything unresolved from either side.

```
**Conversation summary:**
- [brief bullet covering key topics/decisions in the thread]
- [next key exchange or development]

**Open topics:**
- [unresolved question or item from customer]
- [item you were going to get back to them on]
```

---

### Recap mode: detecting already-handled items

For each potential follow-up, check:
1. Sent emails after the meeting end time mentioning the topic or customer
2. Slack messages sent after the meeting end time

If evidence exists it was addressed, mark it as **Already handled** with a brief note. The goal is an accurate action list — not a guilt list of things already done.

---

## Step 9: Save HTML Report

After generating the full brief, save it as a dated HTML file for archival and easy reference.

**File location:** Save to a `Daily Prep/` folder inside the user's workspace directory.
- Path pattern: `<workspace>/Daily Prep/YYYY-MM-DD-day-prep.html`
- Create the `Daily Prep/` folder if it doesn't exist.

**HTML formatting:**
- Clean, readable HTML with inline CSS (no external dependencies)
- Use a professional but simple design — light background, clear section headers, readable fonts
- Color-code triage labels (e.g., red/orange for Reply Needed/Action Required, gray for FYI)
- Mark overdue drafts with a visible warning indicator
- The HTML should be fully self-contained and look good when opened in any browser
- Include the user's name and the date at the top

---

## Step 10: Post to Briefing Channel

Post the **full brief** to the user's `{firstname}-briefing` Slack channel (resolved in Step 0). This is the primary delivery mechanism — not a summary, not a pointer to a file. The user should be able to read the entire brief from Slack, on any device. The channel won't trigger a notification (Slack doesn't notify for messages posted as yourself), so users should star the channel for quick access.

**Formatting for Slack:**
- Use **standard markdown** formatting — the Slack MCP connector translates `**bold**` (double asterisks) into Slack bold. Do NOT use Slack's native mrkdwn single-asterisk `*bold*` — it renders as italic through the connector.
- **Make it scannable.** The user should be able to skim the brief in under 60 seconds and know where to focus.
- Use **bold headers** generously — every section and subsection should have a bold header line (e.g., `**📬 Inbox Triage**`, `**📝 Draft Queue**`, `**📊 Client Snapshot**`, `**📅 Meeting Prep**`)
- Use bold for key names, labels, and statuses within sections too (e.g., `**Reply Needed**`, `**⚠️ OVERDUE**`, `**🔴 Flagged**`)
- Use divider lines (`———`) between major sections for visual separation
- Bullet points for list items, but keep them tight — no paragraph-length bullets
- The brief should include ALL sections: Inbox Triage, Draft Queue, Sent & Awaiting Reply, Slack Signals (if anything was found), COM Portfolio Snapshot, and Meeting Prep — in that order
- At the bottom, include a note: `Full HTML version saved to Daily Prep/YYYY-MM-DD-day-prep.html`
- **Always include this line at the very end of the brief** (Prep mode only): `🔔 **Post-meeting sweeps:** Open a new Cowork session and say "create today's sweep tasks" to schedule automated post-call summaries for today's meetings.`

**If the Slack message exceeds 5000 characters** (Slack's limit per message), split it into multiple messages posted sequentially to the same channel. Use logical section breaks — e.g., one message for Inbox Triage + Draft Queue + Awaiting Reply, one for COM Snapshot, one per meeting prep or grouped meetings.

If the briefing channel wasn't found in Step 0, skip the Slack post and let the user know: *"I couldn't find your briefing channel. Create a private channel called `{firstname}-briefing` in Slack and I'll post there next time. The full brief is saved as an HTML file in the meantime."*

---

## Step 11: Task Sync

After the brief is posted, reconcile TASKS.md with what the research surfaced. This is the step that keeps the task list current without requiring manual updates.

**TASKS.md location:** `*/mnt/Cowork-OS/Productivity/TASKS.md`

Work through three passes:

### Pass 1 — Mark Complete

Review Active and Waiting On tasks from Step 0.5. For any task where research produced clear evidence of completion (sent email found, meeting happened, question was answered, follow-up was logged), mark it done:
- Change `[ ]` to `[x]`
- Add strikethrough: `~~task~~`
- Add today's date
- Move to Done section

Only mark complete if the evidence is clear — don't infer completion from ambiguous signals.

### Pass 2 — Update Existing

For tasks that were not completed but have new status information (e.g., a waiting item got a partial response, a stale account had a touchpoint), update the context line to reflect what's current. Don't rewrite the task — just add a brief status note and update the date.

### Pass 3 — Add New

Surface tasks from the brief that aren't already tracked. Pull from:
- **Awaiting-reply items past 5 days** — if not already in Waiting On
- **Needs Attention accounts** — if no task exists for that account, add one with context from the brief (e.g., "Follow up with Blue Meridian — no interaction since 2/18, first event status unknown")
- **"Your homework" items** from meeting prep — action items you committed to from prior call recaps (e.g., "Send Jill Calendly link for Jess call — RCP")
- **Explicit action items** surfaced in research (e.g., "Chase Emily re: HAF Group Ticketing escalation — sent 3/11, 8 days no response")

**Format for new tasks:**
- Active: `- [ ] **[Task title]** - [context], for [customer/person], due [date if known]`
- Waiting On: `- [ ] **Waiting: [what]** - [from whom], since [date]`

### Presentation and Confirmation

Present all proposed changes as a single batch before writing:

```
**Task Sync — Proposed Updates**

✅ Mark complete: [task title] — [evidence]
🔄 Update: [task title] — [what changed]
➕ Add (Active): [new task]
➕ Add (Waiting): [new waiting item]
```

Write to TASKS.md after the user confirms. If no changes are needed, skip silently — don't announce that nothing changed.

---

## Step 12: Post-Brief Email Draft Offers

After Steps 9, 10, and 11 are complete, proactively offer to draft replies for any **Reply Needed** items from the inbox triage — in priority order. This is the point where it's appropriate to engage with specific threads.

**How to surface it:**

Present a numbered list of the "Reply Needed" items from the brief, with a one-line summary of what's needed for each:

```
**Ready to help with follow-ups. Want me to draft any of these?**

1. **[Sender] — [Subject]**: [What's being asked / what a reply needs to address]
2. **[Sender] — [Subject]**: [What's being asked]
3. ...
```

Let the user pick which ones to tackle. Don't draft anything without being asked — just surface the options clearly so they can direct the next step.

**For overdue drafts** (flagged in Step 5b), surface those too with a separate prompt:

```
**You also have [N] overdue draft(s):**
• **To: [Recipient]** — [Subject] — started [date]: [What it was about / what still needs to happen]
```

If there are no Reply Needed items and no overdue drafts, skip this step silently.

---

## Customer Dossier Integration

> This step only applies if the current user is the current user (@blackthorn.io domain). Verify with
> `gmail_get_profile` — if the email does not match, skip this section entirely and do not
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
## Tips

- Lead with what matters. If context is sparse, say so — don't pad.
- AI notetaker recap emails are often the richest source of prior call context. Go back 30 days for these — they are worth it. For 1:1s, a full month of recaps surfaces conversation themes that a single recap won't.
- When inferring underlying needs, be specific about the business logic. "They want to improve registration" is not useful. "They need to prevent double-registration across event time slots and are hitting a configuration gap in their current setup" is.
- For Office Hours: treat each submitted question as a separate item with full framework analysis.
- For Tier 1 deep-dive meetings: volume of context matters. Be comprehensive.
- Resources / mitigation options: this section is populated by the `blackthorn-support` skill — run it for every open question or issue before writing this section. Think about what you'd actually send someone: a Learning Hub article, a known workaround, a config step. One entry per identified question/issue, not a generic list.
- For 1:1s: the "What you've been working on" section is a deliberate memory aid — surface enough detail to walk into the conversation well-grounded.
- The inbox triage in Prep mode is meant to give you a quick handle on email before meetings start. If the inbox is clean, say so and move on — don't manufacture triage items.
- For the Sent & Awaiting Reply section, when in doubt about whether a response is expected, err on the side of excluding it. A shorter, high-signal list is more useful than a noisy one.

---

## PM Handoff — SKILL RESULT

When running under PM orchestration (including when triggered by the morning-orchestrator),
complete all steps through HTML file save and Slack post delivery, then return a SKILL
RESULT block to PM. The brief is the deliverable — PM does not re-route before delivery.
PM receives the result to log, route any follow-up actions, and surface Tier 2 flags.

```
## SKILL RESULT: day-prep-recap
Timestamp: [ISO 8601]
Customer: None (day-level briefing)
Actions taken: [calendar read; inbox triage; COM portfolio snapshot; brief posted to Slack;
  HTML archived to Daily Prep/]
Findings: [summary of the brief — key meetings today, follow-up triggers, tasks due,
  inbox highlights. Full brief is in the HTML file and Slack channel.]
Confidence: High
Gaps/failures: [any calendar errors, Slack post failures, inbox search issues]
Suggested next: For any "Reply Needed" email surfaced in the brief: email-templates if
  a draft is warranted.
Flags for Jared: [any externally-visible items from the triage — emails that need
  sending, calendar invites, anything requiring Jared's action today]
```
