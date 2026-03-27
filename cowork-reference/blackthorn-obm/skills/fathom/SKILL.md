---
name: fathom
description: >
  INTERNAL — invoked by PM only. Do not trigger directly on user messages. Search Fathom Video for
  meeting recordings, transcripts, summaries, and action items related to a specific customer. Use
  this skill whenever you need meeting context for a customer — including when preparing COM record
  updates, flagged onboarding syncs, day prep, account reviews, or any task where knowing what was
  discussed in recent calls would be valuable. Trigger phrases include: "pull Fathom for [customer]",
  "what do we know from calls with [customer]", "check Fathom for [customer]", "look up meetings with
  [customer]", "get meeting context for [customer]", "what did we discuss with [customer]". Also
  invoke proactively when another skill (flagged-onboarding-sync, day-prep-recap) is gathering
  customer context — Fathom data should be treated as a primary research source alongside Slack and
  Gmail, not a last resort.
---

# Fathom Meeting Research Skill

This skill searches Fathom Video for recorded meetings related to a customer account. The
primary workflow is Gmail-first: use a broad email search to build an intelligence picture of
the customer (domains, contacts, SI partners, timeline), then use that to run precise, targeted
Fathom searches. This approach consistently outperforms going straight to Fathom because Gmail
surfaces context that makes every downstream search smarter.

Meetings are frequently recorded by teammates other than the user — sales reps, CSMs, directors.
The search strategy must account for this by casting a wide net across domains and titles rather
than assuming the user recorded every call.

---

## Step 0 — Check MCP Availability (ALWAYS DO THIS FIRST)

Before doing anything else, check whether the Fathom MCP tools are available in this session.
Look for `fathom_search_meetings` in the list of available tools.

**If `fathom_search_meetings` IS available:** proceed directly to the search strategy. Do not
mention setup to the user. Just do the work.

**If `fathom_search_meetings` is NOT available:** the MCP server needs to be set up on this
person's machine. This is a one-time process — once done, it never needs to be repeated.
Walk through the setup guide below, then stop. The user will need to restart their conversation
after completing setup before Fathom searches will work.

---

## One-Time Setup Guide (only shown when MCP tools are missing)

Tell the user:

> "To connect Claude to Fathom, I need to set up a small background server on your machine.
> This is a one-time process — once done, it works automatically every session."

### Option A — Setup script (easiest, if they have a `setup.sh` from a teammate)

If the user has access to a `setup.sh` file (shared by a teammate or in a shared folder):
1. Open Terminal
2. Navigate to the folder containing `setup.sh`
3. Run: `bash setup.sh`
4. Follow the printed instructions to add the server to Claude settings
5. Start a new conversation and test with: *"Use fathom_list_teams to test my Fathom connection."*

### Option B — From scratch (no shared folder needed)

**Step 1 — Check Python**
Ask: *"Do you have Python installed? Check by opening Terminal and running `python3 --version`."*
If not: https://www.python.org/downloads/ (install Python 3.9+)

**Step 2 — Run this single Terminal command**
```bash
mkdir -p ~/fathom-mcp && pip3 install mcp requests --quiet && curl -fsSL https://raw.githubusercontent.com/anthropics/fathom-mcp/main/server.py -o ~/fathom-mcp/server.py 2>/dev/null || python3 -c "
import urllib.request
urllib.request.urlretrieve('https://raw.githubusercontent.com/anthropics/fathom-mcp/main/server.py', '/Users/' + __import__('os').getenv('USER') + '/fathom-mcp/server.py')
print('Done')
"
```

**Step 3 — Add to Claude settings**

For **Cowork**: Settings (gear icon) → MCP Servers → Add new:
- Name: `fathom`
- Command: `python3`
- Args: `/Users/THEIR_USERNAME/fathom-mcp/server.py`
- Environment: `FATHOM_API_KEY` = their API key

For **Claude Code**, add to `~/.claude/settings.json`:
```json
"fathom": {
  "command": "python3",
  "args": ["/Users/THEIR_USERNAME/fathom-mcp/server.py"],
  "env": { "FATHOM_API_KEY": "their-key-here" }
}
```

**Step 4 — Get an API key (if needed)**
Fathom → Settings → API Keys → Generate Key. Each person needs their own.

**Step 5 — Verify**
Start a new conversation and ask: *"Use fathom_list_teams to test my Fathom connection."*
If it returns team names, setup is complete.

---

## Step 0.5 — Check Local Meeting Cache (ALWAYS DO THIS SECOND)

Before making any Fathom API calls, check whether meeting files already exist locally for this
customer. Local files are the fastest source of truth and eliminate redundant API calls.

**Find the workspace and check for cached meetings:**
```bash
WORKSPACE=$(find /sessions/*/mnt/Cowork-OS -maxdepth 0 -type d 2>/dev/null | head -1)
CUSTOMER_KEBAB="<customer-name-in-kebab-case>"
ls "$WORKSPACE/customers/$CUSTOMER_KEBAB/meetings/" 2>/dev/null
```

Each file is named `YYYY-MM-DD-Meeting-Title.md` and contains the Fathom summary, action
items, and a direct Fathom URL for that meeting.

**If local files exist:**
- Read any relevant ones — they load instantly with no API call
- Note the date of the most recent cached file — that's your "last synced" date
- When you later build the full meeting list (Step 2), only fetch summaries from Fathom for
  meetings newer than the most recent cached file, or any meetings not in the cache
- A meeting is "cached" if a local file exists with a matching date and a similar title (fuzzy
  match is fine — don't be overly strict about exact title formatting)

**If no local files exist:**
- Proceed with the full research workflow as normal
- You'll save everything to local files in Step 7 at the end

---

## Single-Call Lookup (use when context makes the call obvious)

If the user is asking about one specific recent call — e.g., "what did we cover in my call with
Acme this morning?" or "pull the summary from yesterday's HAF sync" — skip the full research
workflow. Just run a domain search scoped to the last 1–3 days and pull that recording directly.
Don't over-engineer it when the ask is simple.

---

## Day Recap (use for "recap my day" or "what calls did I have today?")

When the user wants a recap of their day's calls, pull everything they personally recorded that
day — with full transcripts, not just summaries. This is one of the few cases where `recorded_by`
and tight date filters are the right tool: you know the user, you know the date, and you want
only their calls.

**Before searching:** call `gmail_get_profile` to get the current user's email address if not
already known. Use that email for the `recorded_by` filter below.

```
Tool: fathom_search_meetings
- recorded_by: ["<current user's email from gmail_get_profile>"]
- created_after: "<today>T00:00:00Z"
- created_before: "<today+1>T00:00:00Z"
```

For each result, pull the full transcript:
```
Tool: fathom_get_transcript
- recording_id: <id from search results>
```

Use the transcripts (not just summaries) to build the recap — they capture nuance, commitments,
and tone that summaries flatten. Present results chronologically with key takeaways, action items,
and anything that needs follow-up.

If the user says "yesterday" or a specific past date, adjust the date window accordingly. If they
say "this week," expand to Monday–today.

---

## Full Research Workflow

Use this when building a complete picture of a customer relationship, preparing for an account
review, updating COM records, or any task requiring historical context.

The search strategy follows a deliberate sequence — each step casts a different kind of net.
Domain searches catch calls with external attendees. Broad title searches catch internal calls.
Fine-tuned searches catch anything that slipped through. Skipping steps or narrowing too early
means missing calls.

---

### Step 1 — Gmail Intelligence Gathering

Start here, not in Fathom. A broad Gmail search surfaces the customer's email domain(s),
identifies contacts and their roles, reveals SI/implementation partners, and establishes a real
onboarding start date — all before making a single Fathom API call. This makes every downstream
search more targeted and avoids the common failure mode of guessing the wrong domain.

**Run a broad search:**
```
Tool: gmail_search_messages
- q: "Customer Account Name"
- maxResults: 50
```

If the customer has a known abbreviation (e.g., "HAF" for Hindu American Foundation), run a
second search for that too and merge results.

**From the results, extract:**
- **Email domains** — look at From/To/CC addresses across the threads, not just subject lines.
  A customer's operational domain often differs from their public name (especially nonprofits).
  Note every distinct external domain — some orgs have multiple (e.g., a branded short domain
  plus their org name domain).
- **SI/implementation partners** — consultants or third-party firms CC'd on threads, mentioned
  in email bodies, or appearing in intro emails. Note their company and domain.
- **Contact names and roles** — who from the customer side appears most? What are their titles?
- **Onboarding start date** — the earliest relevant email gives you a real lower bound.
- **Account themes** — even quick subject line scanning can surface things like escalations,
  feature requests, or open issues before you've looked at a single call.

**Caveat:** If customer contacts use personal email addresses (gmail.com, outlook.com, etc.)
rather than a company domain, domain-based Fathom searching won't work. Note this and rely
more heavily on title search or the Fathom recap email inventory below.

---

### Step 2 — Fathom Recap Email Inventory

Before running Fathom API searches, build a complete call inventory from the user's Fathom
recap emails. This tells you exactly how many calls exist and provides critical metadata
(titles, dates, internal vs. external) that guides every subsequent search.

```
Tool: gmail_search_messages
- q: from:fathom "Customer Account Name"
```

The email subject format tells you the call type and which search strategy will find it:

| Email subject | What it means | How to find it |
|---|---|---|
| "Recap of your meeting with [customer-domain]" | Recording with recognized external attendees | Domain search (Step 3) |
| "Recap for '[Meeting Title]'" | Internal recording — no external domain recognized | Broad or fine-tuned title search (Steps 4–5) |
| "Recap of your meeting with Blackthorn" | External attendees present but on a domain Fathom didn't recognize as external, OR a teammate's recording shared to you | Try domain search first; if not found, use title search |

This inventory is your checklist. After each subsequent search step, compare what the API
returned against this list. Any gaps tell you which calls still need to be found and which
search strategy to try next.

**Key insight:** "Recap for '[Title]'" format is a strong signal the call is internal-only.
These will never appear in domain searches — they require title-based searching (Steps 4–5).
Note the exact title and date from the email; you'll use both later if needed.

**Note:** Fathom recap email URLs use a `/calls/ID` or `/share/TOKEN` format that does NOT
map to the `recording_id` used by `fathom_get_summary` and `fathom_get_transcript`. Never
pass a URL call ID directly to those tools.

---

### Step 3 — Fathom Domain Searches

With domains confirmed from Step 1, run domain searches to find calls with external attendees.
This is the broadest net — it catches calls regardless of who on the Blackthorn team recorded
them or what the meeting was titled.

**Search each customer domain separately:**
```
Tool: fathom_search_meetings
- customer_domains: ["acme.com"]   ← must be a JSON array, not a string
```

**Then search each SI/implementation partner domain:**
```
Tool: fathom_search_meetings
- customer_domains: ["sipartnerdomain.com"]
```

Do not add a `filter_title_contains` here — SI partner meetings are often titled generically
("Weekly Sync", "Implementation Check-in") with no mention of the customer name. Instead,
pull all results for the partner domain and review the summaries to determine which calls
pertain to this customer. SI partners typically work multiple accounts, so not every result
will be relevant — use the summary content (customer names, topics discussed) to filter
manually.

**Important notes:**
- **Do not use `created_after` on initial searches.** Keeping the date window wide ensures you
  don't accidentally exclude early calls due to timezone offsets or date discrepancies. Only
  add date filters later (Step 5) if you need to reduce pagination depth for a targeted search.
- **Do not use `recorded_by` in domain searches.** Domain search already casts a wide net
  across all recorders — adding `recorded_by` here would exclude calls recorded by teammates.
  Reserve `recorded_by` for Step 4.5, where it's the right tool for recovering internal calls.
- Do not pass `include_summary` or `include_action_items` — they default to `true` and throw
  a validation error when passed explicitly.
- After getting results, check `_filter_applied` in the response. If it says `"none"`, the
  domain filter silently failed and results are unfiltered. Try a different domain variation.
- If multiple customer domains were found in Step 1, run a separate search for each and
  deduplicate results by `recording_id`.
- **Paginate fully.** If `next_cursor` is present, keep paging until you've collected all results.

After this step, compare results against the recap email inventory from Step 2. Note which
calls are still missing — those are your targets for Steps 4 and 5.

---

### Step 4 — Broad Title Searches

Domain searches only find calls where an external attendee was present. Internal calls — sales
handoffs, internal syncs, strategy discussions about the customer — won't appear. These calls
are often critical context (e.g., a sales handoff reveals what was promised; an internal sync
reveals risk flags).

Run broad title searches using short customer identifiers:
```
Tool: fathom_search_meetings
- filter_title_contains: "Customer Account Name"
```

Also search for common abbreviations or short names the customer is known by:
```
Tool: fathom_search_meetings
- filter_title_contains: "ABBREV"
```

For example, if the customer is "Hindu American Foundation", search for both
"Hindu American Foundation" and "HAF".

**Why no date filter here:** The `filter_title_contains` parameter is applied client-side per
page of results, and the API returns results in reverse chronological order. Without a date
filter, you may need to paginate through multiple pages to reach older calls. This is intentional —
keeping the window wide ensures you don't miss anything. If pagination becomes excessive (many
pages with zero matches), only then consider adding `created_after` to reduce the search space.

**What this catches that domain searches miss:**
- Sales handoffs (internal, no customer attendees)
- Internal strategy syncs about the customer
- Calls where external attendees used a domain Fathom didn't index
- Calls recorded by teammates on other teams

After this step, compare against the recap email inventory again. If all calls are accounted
for, you're done searching. If gaps remain — especially if the missing calls are confirmed
internal-only (their Fathom recap email subjects used the "Recap for '[Title]'" format) or
if you have a known call count from the user that isn't matching up — proceed to Step 4.5
before Step 5.

---

### Step 4.5 — Calendar-Assisted `recorded_by` Search (for internal calls title search can't find)

Title search fails for internal calls when you don't know the exact title Fathom used, or
when the call title contains no customer-identifiable keywords. This happens most often with
sales handoffs, internal strategy syncs, and ad-hoc working sessions where the calendar
invite title was something generic.

The key insight: if you know a call happened on a specific date (from the user's memory, a
gap in the call count, or context from Gmail), you can look up who was on that call in
Google Calendar — and then use `recorded_by` with a tight date window to find the recording
directly, without needing to know the title at all.

**Step 1 — Check Google Calendar for the date in question:**
```
Tool: gcal_list_events
- date: <the date the call is believed to have occurred>
```

Look for events that match the expected call (timing, duration, attendees). The calendar
event tells you who was invited, which tells you who likely recorded it.

**Step 2 — Search Fathom by recorder + date window:**
```
Tool: fathom_search_meetings
- recorded_by: ["<recorder-email@blackthorn.io>"]
- created_after: "<date minus 1 day>T00:00:00Z"
- created_before: "<date plus 1 day>T00:00:00Z"
```

Keep the date window tight (±1 day) to minimize results — you're looking for one specific
call. Review what comes back and identify the recording by matching the date, duration,
and any recognizable attendees.

**Who to try for `recorded_by`:**

| Call type | Who likely recorded it |
|---|---|
| Sales handoff (internal) | `dylan@blackthorn.io`, `ellie@blackthorn.io` |
| CS-recorded kickoff | `lexi.wachtell@blackthorn.io` |
| Jared's working sessions | `@blackthorn.io domain` |
| Other internal syncs | Check the calendar event; use whoever hosted the meeting |

**When the customer didn't join the calendar invite:** Some calls are recorded with external
attendees who joined a Zoom link directly without being on the original calendar invite.
In this case, `calendar_invitees` in the Fathom result may only show internal attendees even
though the customer was on the call. The `recorded_by` + date window approach still works —
just confirm the match by checking the recording duration and title against your expectations.

**Known call count as a target:** If the user tells you how many calls they've had (e.g.,
"I've had 7 calls with this customer"), use that as your target number. Don't stop searching
until you've found all of them or exhausted all reasonable strategies. A gap between what
domain + title searches found and what the user knows exists is a strong signal that
Step 4.5 is needed.

After this step, compare against your target count. If calls are still missing, proceed to Step 5.

---

### Step 5 — Fine-Tuned Searches (for known missing calls)

If specific calls from the Gmail recap inventory (Step 2) are still missing after Steps 3–4,
use the precise information from the recap email to target them directly.

You know the exact title from the email subject and the approximate date. Use both to bracket
the search into a tight window — ±2 days from the known date:
```
Tool: fathom_search_meetings
- filter_title_contains: "Exact Meeting Title From Email"
- created_after: <known date minus 2 days, ISO 8601 format>
- created_before: <known date plus 2 days, ISO 8601 format>
```

**Example:** For a call you know happened on January 5, 2026, titled "Acme Corp Sales Handoff":
```
Tool: fathom_search_meetings
- filter_title_contains: "Acme Corp Sales Handoff"
- created_after: "2026-01-03T00:00:00Z"
- created_before: "2026-01-07T00:00:00Z"
```

The ±2 day buffer accounts for timezone offsets or minor date discrepancies between Gmail
and Fathom, while keeping the search window tight enough to minimize pagination (typically
resolves in 1–3 pages).

**Why this works:** Using `created_before` + `created_after` together dramatically reduces
pagination depth. A search that might require dozens of pages without date filters often
resolves in 1–3 pages when the date window is tight. This is why date bracketing is saved
for this step — it's a precision tool for known targets, not a default filter.

**Confirming internal calls:** The `calendar_invitees_domains_type` field on results is useful
for confirming call type. A value of `"only_internal"` confirms the call had no external
attendees, which explains why domain searches didn't find it.

If fine-tuned searches still fail, the call may be in a teammate's Fathom workspace that the
API key doesn't have access to. In that case, the Gmail recap email content is the best
available source — read the full email body via `gmail_read_message` to extract the summary.

---

### Step 6 — Transcripts

Transcripts are speaker-labeled with timestamps. They're large (a 30-min call can be 5,000+
lines), so the approach depends on how many calls you're working with.

**When to pull transcripts automatically (~10 or fewer calls):**
If the result set is roughly 10 or fewer recordings — which covers day recaps, single-customer
deep dives, and most focused research — pull full transcripts for every call. This is a loose
guideline, not a hard cutoff — if there are 11 or 12, just pull them all. Transcripts capture
nuance, commitments, and tone that summaries flatten. For day recaps and deep dives, this is
the default behavior, not an opt-in.

```
Tool: fathom_get_transcript
- recording_id: <id from fathom_search_meetings results>
```

**When to be selective (significantly more than 10 calls):**
For larger result sets, pull summaries first and use them to triage. Read through the summaries
to identify which calls are most likely to contain high-value context — churn signals, a
customer threatening to switch platforms, exec escalation, specific commitments or promises
made by Blackthorn, legal or contract language, product failures, or whatever is most relevant
to the task at hand. Then pull transcripts for those calls. Summaries are reliable for general
context but can miss the moments that matter most, so use them as a screening layer rather
than an endpoint.

**Always pull a transcript when:**
- You need to verify a specific claim or find an exact quote
- A summary surfaces something high-stakes that needs the full picture
- The user explicitly asks for transcript-level detail

---

### Step 7 — Save to Local Cache

After completing research for any customer, save each meeting's data to the local cache.
This prevents redundant API calls in future sessions and gives you a permanent local record
with timestamped Fathom links even if API access changes.

**Only save meetings for which you actually retrieved summary data from the API.** Don't
create placeholder files for meetings identified in Gmail but not retrievable from Fathom.
Skip any meeting already in the cache (matching date + similar title).

**Create the folder if it doesn't exist:**
```bash
WORKSPACE=$(find /sessions/*/mnt/Cowork-OS -maxdepth 0 -type d 2>/dev/null | head -1)
mkdir -p "$WORKSPACE/customers/<customer-kebab>/meetings/"
```

**File naming:** `YYYY-MM-DD-Meeting-Title.md`
- Date from `recording_start_time` or `created_at`
- Title slugified: lowercase, spaces to hyphens, special chars removed
- Example: `2026-01-15-acme-kickoff-call.md`

**File format:**
```markdown
---
recording_id: <id>
date: YYYY-MM-DD
title: Full Meeting Title
fathom_url: https://fathom.video/share/TOKEN
participants: Name (Company), Name (Company)
---

# Full Meeting Title

**Date:** YYYY-MM-DD
**Participants:** Name (Company), Name (Company)
**Fathom Link:** [View Recording](https://fathom.video/share/TOKEN)

## Summary

[Full summary from Fathom — include timestamp links where present]

## Action Items

- [item] (assigned: name | status: open/complete | user_generated: true/false)
```

**For the Fathom URL:** use the link from `fathom_get_summary` if you called it (it contains
the share token). If you only have the search result, use the `recording_id` to construct:
`https://fathom.video/calls/<recording_id>` as a fallback — the share link is preferred.

---

## Fathom API Reference

### Available Parameters for `fathom_search_meetings`

| Parameter | Type | Purpose | When to use |
|---|---|---|---|
| `customer_domains` | JSON array | Filter by attendee email domain | Steps 3 (domain searches) |
| `filter_title_contains` | string | Client-side title substring match | Steps 4–5 (title searches) |
| `created_after` | ISO 8601 string | Only return recordings after this date | Step 5 only (fine-tuned) |
| `created_before` | ISO 8601 string | Only return recordings before this date | Step 5 only (fine-tuned) |
| `cursor` | string | Pagination cursor from previous response | Any search with `next_cursor` |

### Parameters to use with caution

| Parameter | Guidance |
|---|---|
| `recorded_by` | Use in **two specific situations only**: (1) Day Recap — filter to the user's own recordings; (2) Step 4.5 — recover internal calls by targeting a specific recorder + tight date window. Do not use in domain searches (Step 3) — it would exclude calls recorded by teammates. |
| `include_summary` | Defaults to `true`; passing it explicitly throws a validation error — always omit |
| `include_action_items` | Same as above — always omit |

### Pagination

The API returns results in reverse chronological order (newest first), with a default page
size of 10. If `next_cursor` is present in the response, more results exist. Pass the cursor
value to the next call to continue paginating.

Title filters (`filter_title_contains`) are applied client-side per page, meaning a page can
return 0 matching results while still having a `next_cursor` pointing to more pages. Keep
paginating until `next_cursor` is empty.

### Useful Response Fields

| Field | Purpose |
|---|---|
| `recording_id` | Use with `fathom_get_summary` and `fathom_get_transcript` |
| `calendar_invitees_domains_type` | `"only_internal"` = no external attendees (internal call) |
| `recorded_by` | Shows who recorded the call (name, email, team) |
| `_filter_applied` | Confirms which filter was used; `"none"` means the filter silently failed |
| `recording_start_time` / `created_at` | Actual recording date (use these, not `recording_started_at` which may be null) |

---

## Interpreting Results

**AI Summaries** (`default_summary.markdown_formatted`) are generally reliable for topics,
decisions, and sentiment. Treat as a strong signal but verify high-stakes moments in transcripts.

**Timestamp Links** — `fathom_get_summary` returns summaries with hyperlinks to specific moments
embedded in every bullet, section header, and key statement. The link format is:
`https://fathom.video/share/{token}?tab=summary&timestamp={seconds}`. The summary returned by
`fathom_search_meetings` may not contain these links — call `fathom_get_summary` with the
`recording_id` when you need a clickable link to a specific moment. Do this selectively — it's
most valuable for recordings containing high-stakes moments worth calling out directly.

**Surface timestamp links when you identify:**
- Churn signals or competitor mentions
- Specific commitments made by Blackthorn
- Product failures, blockers, or escalations
- Customer frustration or strong sentiment moments
- Moments a downstream workflow (COM update, product feedback post) would want to reference directly

Embed timestamp links inline — hyperlink the most relevant phrase in the surrounding sentence
rather than adding a separate URL. Example: "Customer said [they'd consider switching platforms](https://fathom.video/share/TOKEN?tab=summary&timestamp=XXX) if the feature gap isn't addressed."

**Action Items** are AI-extracted unless `user_generated: true` (manually added by a participant).
Note which type when surfacing them.

**Attendees** — `is_external: false` = Blackthorn team member. Use this to understand who was
in the room from each side.

**Recording dates** — use `recording_start_time` or `created_at` fields. The `recording_started_at`
field may be null in some records.

---

## Output Format

Always open with an Account Context section that synthesizes the Gmail intelligence from Step 1.
This is often as valuable as the call summaries themselves — especially contacts, SI partners,
and the account timeline — and it came from a source the Fathom API can't see.

```
## [Customer Name] — Account Context
*Relationship since: [earliest email date] | [N] calls found via API | [M] additional calls identified via Gmail*

**Key Contacts:** [name, title, email domain]
**SI / Implementation Partner:** [company, domain — or "none identified"]
**Account Themes (from email):** [recurring topics, escalations, open issues]

---

## Recorded Calls
*[newest first]*

### [Date] — [Meeting Title]
**Attendees:** [names and companies]
**Summary:** [Fathom AI summary]
**Action Items:**
- [item] (assigned: [name] | status: open/complete)

---

[repeat for each call]

---

## Calls Identified in Gmail But Not Retrievable via API
- [date] — [title] — [reason: internal recording / teammate's workspace]

---

## Themes Across Calls
[recurring topics, unresolved issues, patterns observed across meetings]

## Open Action Items
- [item] — from [date]

## Notes
[Caveats: missing attendees, unverified claims, high-stakes moments flagged for transcript review]

```

*When high-stakes moments are identified (churn signals, escalations, specific commitments,
product failures): call `fathom_get_summary` on the relevant recording to get the
timestamp-linked summary. Embed the link inline within the relevant text — hyperlink the
most descriptive phrase, not a separate "click here" line. Example:*

*"Customer mentioned [they're evaluating Cvent as an alternative](https://fathom.video/share/TOKEN?tab=summary&timestamp=XXX) due to the waitlist limitation."*

---

---

## Customer Dossier Integration

> This step only applies if the current user is @blackthorn.io domain. Verify with
> `gmail_get_profile` — if the email does not end with @blackthorn.io, skip this section entirely and do not
> mention dossiers.

**Before starting research:** Check for an existing dossier in the customers/ folder.
Find it with:
```bash
WORKSPACE=$(find /sessions/*/mnt/Cowork-OS -maxdepth 0 -type d 2>/dev/null | head -1)
ls "$WORKSPACE/customers/"
```
Convert the customer name to kebab-case to find the file (e.g., `royal-college-of-psychiatrists.md`).
If found, read it before doing any other research — it will tell you the email domain (for Fathom/Gmail
searches), known contacts, open items, and recent interaction history. This saves significant
research time and surfaces context that external searches alone will not.

**After completing the workflow:** Update the dossier with anything new that surfaced —
new contacts, status changes, decisions made, action items, or a new interaction log entry.
Update the `Last Contact` field in the header. If no dossier exists yet, create one from the
template at `_TEMPLATE.md` in the same folder.
## Rate Limits

60 API requests per 60 seconds. Most customer lookups use 3–6 requests. Be mindful when
paginating large result sets or running multiple domain searches in parallel.

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

## PM Handoff — SKILL RESULT

When running under PM orchestration, do not surface output directly to the user.
Complete all work, then return a SKILL RESULT block to PM for evaluation:

```
## SKILL RESULT: fathom
Timestamp: [ISO 8601]
Customer: [customer name | None]
Actions taken: [brief — what searches ran, how many recordings found, whether transcripts pulled]
Findings: [full account context output — Gmail intelligence, call summaries, action items, themes]
Confidence: [High | Medium | Low — Low if Fathom returned nothing or summaries lacked action items]
Gaps/failures: [calls identified in Gmail but not retrievable; API errors; recordings still processing]
Suggested next: com-update with meeting findings; customer-dossier to update interaction log
  and cache meetings; product-feedback-poster if PFQE-worthy signals found
Flags for Jared: [high-stakes signals — opt-out language, contract concerns, escalation threats;
  always escalate these to Tier 2 regardless of summary confidence]
```

PM evaluates this block. If Confidence is Low or a high-stakes signal is detected, PM
will send a SKILL REQUEST back asking for a transcript pull on a specific recording.
Execute that request and return a new SKILL RESULT.
