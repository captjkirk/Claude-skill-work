---
name: morning-orchestrator
description: >
  Runs at 7:00 AM on weekdays via cron. Reads Google Calendar, checks all customer
  dossiers for follow-up triggers, sweeps Slack and Gmail for flagged accounts before
  surfacing them, and routes everything through PM (including structured meeting data)
  to produce the day's morning brief via day-prep-recap. Post-meeting sweep tasks are
  created by day-prep-recap at the end of its run. Also invoked manually: "run morning
  prep", "morning orchestrator", "set up my day". This is the entry point for the
  automated daily workflow — PM handles all routing from here. Never invoke
  day-prep-recap directly for scheduled morning runs; use this.
---

# Morning Orchestrator

Runs at 7:00 AM weekdays. Bootstraps the day: reads the calendar, checks dossier health,
and routes through PM to produce the morning brief. Meeting data is passed to day-prep-recap
so it can create post-meeting sweep tasks at the end of its run.

This is the first thing that runs each day. PM receives all output and synthesizes the
brief — the orchestrator's job is to gather and route, not to present.

---

## Step 0 — Log Start

Append to ACTIVITY-LOG.md:
```
[HH:MM] **MORNING-ORCHESTRATOR** — Starting daily run for [YYYY-MM-DD].
```

Find the log:
```bash
WORKSPACE=$(find /sessions/*/mnt/Cowork-OS -maxdepth 0 -type d 2>/dev/null | head -1)
LOG_FILE="$WORKSPACE/ACTIVITY-LOG.md"
```

---

## Step 1 — Read Today's Calendar

```
Tool: gcal_list_events
- date: [today in YYYY-MM-DD format]
```

From the results, extract for each event:
- Title
- Start time (ISO 8601)
- End time (ISO 8601)
- Attendees (names / emails)
- Customer name (if identifiable from title or attendees)

Filter out: focus blocks, OOO entries, reminders, events with no attendees.
Keep: customer calls, internal meetings, Office Hours, recurring syncs.

If calendar returns no events: log it, proceed to Step 2 with an empty meeting list.

---

## Step 2 — Dossier Staleness Check

Find all customer dossier folders:
```bash
WORKSPACE=$(find /sessions/*/mnt/Cowork-OS -maxdepth 0 -type d 2>/dev/null | head -1)
ls "$WORKSPACE/customers/"
```

For each customer folder (skip `_TEMPLATE.md`, `README.md`, `CLAUDE.md`, `generate_customer_claude.py`):

1. Read `customers/<name>/CLAUDE.md` (fast — operative context)
2. Check for follow-up trigger using this priority order:

| Field to check | Location | Action |
|---|---|---|
| `Next Follow-up Date` | Header | If date ≤ today → flag |
| `Next Scheduled Touch` | Header | If date ≤ today → flag |
| `Follow-up Cadence` + `Last Contact` | Header | Calculate next due date; if ≤ today → flag |
| Neither field present | — | If `Last Contact` > 7 days ago → flag |

**Before flagging any account:** Run a quick activity sweep — search Slack and Gmail
for any activity with that customer in the last 72 hours:

```
Tool: gmail_search_messages
- q: "[customer name]"
- maxResults: 5
```

```
Tool: mcp__f5990e36-1dc1-4097-a832-dced201af2dd__slack_search_public_and_private
- query: "[customer name]"
```

If recent activity found → update dossier `Last Contact` field, do not flag.
If no recent activity found → add to the follow-up list for the brief.

Skip accounts with `Account Status` of: 🎓 Graduated, 🔄 Transferred, 🗄️ Archived,
🤝 Contact Only. These are not active onboarding accounts.

Log completion:
```
[HH:MM] **MORNING-ORCHESTRATOR** — Dossier staleness check complete. [N] accounts flagged for follow-up.
```

---

## Step 3 — Route to PM

Package all findings as a SKILL RESULT block and route to PM:

```
## SKILL RESULT: morning-orchestrator
Timestamp: [ISO 8601]
Customer: None
Actions taken: Read calendar ([N] events). Checked [N] dossiers.
Findings:
  Calendar — Meeting List (pass to day-prep-recap for sweep task creation):
  - [Meeting 1]: title="[title]", start=[ISO 8601], end=[ISO 8601], customer="[name or unknown]", attendees=[list]
  - [Meeting 2]: title="[title]", start=[ISO 8601], end=[ISO 8601], customer="[name or unknown]", attendees=[list]
  - (none) ← if calendar was empty

  Follow-up triggers ([N] accounts):
  - [Customer name] — [reason: Next Follow-up Date was [date] / [N] days since last contact]
  - ...

  No-flag accounts: [N] accounts current, no action needed.

Confidence: High
Gaps/failures: [any calendar errors, Slack/Gmail API issues, dossiers that couldn't be read]
Suggested next: day-prep-recap — pass the full meeting list above so it can build the
  brief and create post-meeting sweep tasks at the end of its run
Flags for Jared: [any Tier 2 items — none expected in standard run]
```

PM receives this, invokes `day-prep-recap` with the meeting list in context, which builds
the full brief (Slack + HTML) and creates fireAt sweep tasks at the end of its run.

---

## Scheduling Note

This skill runs as a cron-scheduled task:
- `cronExpression`: `0 7 * * 1-5` (7:00 AM, Monday–Friday)
- Created via the `schedule` skill

If the scheduled task misfires or fails to run, PM should surface this on the next
manual session start: "Morning orchestrator didn't run today — want me to run it now?"
Check `ACTIVITY-LOG.md` — if no entry exists for today's morning run, the task misfired.

---

## Error Handling

- **Calendar API unavailable:** Log the failure, proceed to Step 2 with empty meeting list. Note in brief. Day-prep-recap will re-read the calendar independently.
- **No events on calendar:** Pass empty meeting list to PM. Still run Step 2.
- **Dossier unreadable:** Log the error, skip that account, continue with others.
- **Slack/Gmail sweep fails for a specific customer:** Flag the account as needing review rather than suppressing it. Better to over-flag than to miss a stale account.
- **All APIs down:** Log the failure, surface to Jared at next session: "Morning orchestrator couldn't complete — API issues at [time]. Run manually?"
