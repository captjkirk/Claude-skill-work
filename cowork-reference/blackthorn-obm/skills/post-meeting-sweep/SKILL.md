---
name: post-meeting-sweep
description: >
  INTERNAL — invoked by PM only. Do not trigger directly on user messages. Triggered automatically 15
  minutes after a meeting ends via fireAt scheduled tasks created by the morning-orchestrator. Pulls
  Fathom summary for the meeting, checks Gmail for related threads, and routes all findings through PM
  for evaluation. PM then decides: COM update needed? Dossier update? PFQE post? Follow-up email?
  Never invoke manually unless re-running a sweep that failed. PM handles all routing from the sweep
  results — this skill gathers and packages, PM decides and acts.
---

# Post-Meeting Sweep

Triggered 15 minutes after a meeting ends. Gathers meeting context from Fathom and
Gmail, packages it as a SKILL RESULT, and routes to PM for evaluation and routing.

This skill does not decide what to do with the data — PM does. This skill's job is
to gather quickly, package cleanly, and hand off.

---

## Step 0 — Identify the Meeting and Mode

The fireAt task prompt contains the meeting title, start time, and customer name (if known).
Parse these from the task prompt. Classify the meeting into one of three modes:

**Mode A — Customer meeting:** External attendees present (non-blackthorn.io domain), or
customer name explicitly provided. Run full sweep with customer context.

**Mode B — Internal work meeting:** No external attendees, but a work meeting — includes
1:1s with manager (Emily), team syncs (OBM Sync, Flagged Onboarding Sync), peer 1:1s,
CS/OBM 1:1s, office hours debrief, or any meeting that could surface customer discussions,
action items, process decisions, or new assignments. Run full sweep without customer dossier.
Cache to `Daily Prep/YYYY-MM-DD-[meeting-title-kebab].md`.

**Mode C — Non-work event:** Personal calendar events, blocked focus time, OOO blocks,
lunch holds, or anything clearly unrelated to work. Exit cleanly:
```
[HH:MM] **POST-MEETING-SWEEP** — [Meeting title] at [time] — non-work event. Sweep skipped.
```

When in doubt between Mode B and Mode C, treat as Mode B. A false positive sweep is
far less costly than missing action items from a manager 1:1 or team sync.

Log start:
```bash
WORKSPACE=$(find /sessions/*/mnt/Cowork-OS -maxdepth 0 -type d 2>/dev/null | head -1)
```
```
[HH:MM] **POST-MEETING-SWEEP** — Sweep starting for: [meeting title] (Mode [A/B]).
```

---

## Step 1 — Load Context

**Mode A:** Load the customer dossier for fast context:
```bash
cat "$WORKSPACE/customers/<customer-kebab>/CLAUDE.md"
```
This gives: current phase, open items, recent interactions, known contacts. Use this
to filter and prioritize what comes back from Fathom and Gmail.

**Mode B:** No customer dossier. Use the meeting title and known attendees (Emily Powers,
Nathan, Noah, Dustin, etc.) to frame Fathom and Gmail searches. Look for: customer names
mentioned, new account assignments, action items for Jared, process decisions, escalations.

---

## Step 2 — Fathom Pull (Run in Parallel with Step 3)

Search Fathom for the meeting. Use a tight date window (today ± 1 day).

**Mode A — by customer domain:**
```
Tool: fathom_search_meetings
- customer_domains: ["[domain from dossier]"]
- created_after: "[today minus 1 day]T00:00:00Z"
- created_before: "[today plus 1 day]T00:00:00Z"
```

**Mode B — or any time domain search is unreliable — by title:**
```
Tool: fathom_search_meetings
- filter_title_contains: "[meeting title keywords]"
- created_after: "[today minus 1 day]T00:00:00Z"
- created_before: "[today plus 1 day]T00:00:00Z"
```

If recording found:
- Pull the summary: `fathom_get_summary` with the `recording_id`
- Extract: action items, key decisions, sentiment signals, anything PM should evaluate
- **Mode A:** Save to `customers/<customer-kebab>/meetings/YYYY-MM-DD-[title].md`
- **Mode B:** Save to `Daily Prep/YYYY-MM-DD-[meeting-title-kebab].md`

If no recording found (meeting wasn't recorded, Fathom hasn't processed it yet):
- Note in SKILL RESULT gaps — Fathom may still be processing (typical delay: 5–10 min after recording ends)
- PM may schedule a retry or flag for manual check

---

## Step 3 — Gmail Sweep (Run in Parallel with Step 2)

**Mode A:** Check for emails related to this customer:
```
Tool: gmail_search_messages
- q: "[customer name] after:[today in YYYY/MM/DD format]"
- maxResults: 10
```
Also check for pre-meeting threads that might reference it:
```
Tool: gmail_search_messages
- q: "[customer name]"
- maxResults: 15
```

**Mode B:** Check for emails involving key internal attendees (Emily, team members) that
may have triggered from or relate to this meeting:
```
Tool: gmail_search_messages
- q: "from:emily@blackthorn.io OR to:emily@blackthorn.io after:[today in YYYY/MM/DD format]"
- maxResults: 15
```

Extract:
- **Mode A:** New inbound from customer contacts; follow-up threads; outstanding threads needing reply
- **Mode B:** Action items sent or received; customer names mentioned; any decisions communicated via email after the meeting

---

## Step 4 — Package and Route to PM

Compile all findings and return to PM:

```
## SKILL RESULT: post-meeting-sweep
Timestamp: [ISO 8601]
Mode: [A — customer | B — internal]
Customer: [customer name, or "Internal — [meeting title]" for Mode B]
Actions taken: Pulled Fathom summary for [meeting title]. Checked Gmail for recent threads.
  Cached meeting to [customers/<customer-kebab>/meetings/ | Daily Prep/].
Findings:
  Meeting: [title] on [date], [start]–[end]
  Attendees: [names and orgs]

  Fathom Summary:
  [Summary content — key points, decisions, action items]

  Action Items (from Fathom):
  - [item] (assigned: [name] | user_generated: [true/false])

  Customers Discussed (Mode B only):
  - [customer name] — [what was discussed, any directives or risk signals]

  Gmail — New/Relevant Threads:
  - [thread subject] — [brief description of content]
  - [or: "No new threads since meeting."]

  Signals for PM evaluation:
  - [Any high-stakes language, risk signals, or escalation indicators — quoted directly]
  - [Any open questions that might need a PFQE post]
  - [Any commitments made that should be tracked]
  - [Mode B: Any new account assignments or portfolio changes]

Confidence: [High | Medium | Low — based on whether Fathom recording was found]
Gaps/failures: [if Fathom recording not found; if Gmail returned nothing; etc.]
Suggested next:
  Mode A: com-update; customer-dossier; email-templates if follow-up needed; product-feedback-poster if PFQE signal
  Mode B: customer-dossier for any customer mentioned; TASKS.md updates for action items; com-update if customer status changed
Flags for Jared: [high-stakes signals, new assignments, escalation language — Tier 2 only]
```

PM evaluates this and routes to the appropriate skills. The sweep does not make
decisions — it gathers, packages, and hands off.

---

## Error Handling

- **Fathom recording not found:** Note in gaps. PM will decide whether to retry later
  or flag for manual check. Do not halt — still complete Gmail sweep and route findings.
- **Fathom still processing:** If meeting ended < 20 min ago and no recording exists,
  note it as "likely still processing" rather than "not found." PM may schedule a retry.
- **Gmail returns no results:** Note in gaps. Not a failure — some meetings just don't
  have related email threads.
- **No customer identified (internal meeting):** Run as Mode B — do not exit. Only exit
  for confirmed non-work events (Mode C). When in doubt, run the sweep.
- **Meeting cache write fails:** Log the error. Still route the SKILL RESULT to PM —
  the cache is a convenience, not a blocker.
