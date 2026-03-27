---
name: onboarding-process-sync
description: >
  INTERNAL — invoked by PM only. Do not trigger directly on user messages. Sync the local
  onboarding-process/ folder with the shared Google Drive process docs. Checks the Drive folder for
  updated documents, compares to locally cached versions, and fetches and saves any docs that have
  changed since the last sync. Trigger phrases include: "check for onboarding process updates", "sync
  onboarding docs", "are the process docs up to date", "check Drive for process doc changes", "has
  Emily updated the process docs", or any time the user wants to verify their local copy matches
  Drive.
---

# Onboarding Process Sync

Keeps the local `onboarding-process/` folder in sync with the shared Google Drive folder
where the team's official process docs live. Safe to run any time — it only writes files
when Drive has a newer version.

---

## Step 1 — Find the Workspace and Manifest

Locate the workspace:
```bash
WORKSPACE=$(find /sessions/*/mnt -maxdepth 1 -name "CLAUDE.md" 2>/dev/null | head -1 | xargs dirname)
PROCESS_DIR="$WORKSPACE/onboarding-process"
MANIFEST="$PROCESS_DIR/manifest.json"
```

Read `manifest.json` if it exists. If it doesn't exist, create it with the default
document list (see Step 5).

---

## Step 2 — Check Drive for Current Doc State

Call `google_drive_search` with:
```
api_query: '1L-zC-wWBHR2VQxYKMYNjiSoUyRqQRQXa' in parents
```

For each result, capture:
- `uri` — the file ID
- `title` — document name
- `modified_time` — when it was last changed in Drive

If the Drive search fails or returns empty, tell the user:
> "Couldn't reach the Drive folder. Check that Google Drive MCP is connected and try again."

Stop.

---

## Step 3 — Compare to Manifest

For each doc returned from Drive:

1. Look up the doc's `uri` in the manifest's `docs` dictionary
2. Compare the Drive `modified_time` to the manifest's `last_synced` for that doc

**Needs update if:** `modified_time > last_synced` OR `last_synced` is null/missing

**Up to date if:** `modified_time <= last_synced`

Also note any docs in Drive that aren't in the manifest — these are new additions and
should be fetched and added.

Build two lists:
- `NEEDS_UPDATE` — docs that are newer in Drive or missing locally
- `UP_TO_DATE` — docs where local cache is current

If `NEEDS_UPDATE` is empty, tell the user:
> "All onboarding process docs are up to date. Last checked: [today's date]."

Update `last_checked` in the manifest and stop.

---

## Step 4 — Fetch and Save Updated Docs

For each doc in `NEEDS_UPDATE`:

1. Call `google_drive_fetch` with `document_ids: ["<doc_uri>"]`
2. Extract the text content from the response
3. Determine the local filename from the manifest (or generate a kebab-case name from
   the title if it's a new doc not yet in the manifest)
4. Write the content to `$PROCESS_DIR/<local_filename>.md` with this header:
   ```markdown
   # [Doc Title]

   _Synced from Google Drive — [Drive modified date]_
   _Source: https://docs.google.com/document/d/[doc_id]/edit_

   ---

   [doc content]
   ```
5. Update the manifest entry for that doc:
   - Set `last_synced` to Drive's `modified_time`
   - Set `local_file` to the filename used

For new docs not yet in the manifest, add a new entry with:
```json
"<uri>": {
  "name": "<title from Drive>",
  "local_file": "<kebab-case-name>.md",
  "last_synced": "<modified_time from Drive>"
}
```

---

## Step 5 — Update Manifest

Write the updated manifest back to `$PROCESS_DIR/manifest.json`:

```json
{
  "folder_id": "1L-zC-wWBHR2VQxYKMYNjiSoUyRqQRQXa",
  "folder_url": "https://drive.google.com/drive/folders/1L-zC-wWBHR2VQxYKMYNjiSoUyRqQRQXa",
  "last_checked": "[TODAY_ISO]",
  "docs": {
    "1H1FKnBbBP5_hyawV6ykPGwUZgZMKEdsiCd2tA7wxGdI": {
      "name": "1. Onboarding Process Summary",
      "local_file": "1-onboarding-process-summary.md",
      "last_synced": "[value]"
    },
    "17ugm1iklwiYXm7nDJf3XBK59goYdfV24LCMjkh8B_3M": {
      "name": "Onboarding Risk Assessment & Flagging Process",
      "local_file": "risk-assessment-flagging-process.md",
      "last_synced": "[value]"
    },
    "1QQMuR0xAqMhIRDakFPgoEkadMc2Hu90iY_3vVZ6z7Hw": {
      "name": "New Sales to Onboarding Handoff Process",
      "local_file": "sales-to-onboarding-handoff.md",
      "last_synced": "[value]"
    },
    "1FWecoKZwLHeDqDEJ3cVmbEmYqLPdmJoEC2JUZ0G1CeY": {
      "name": "Onboarding 10-Meeting Structure",
      "local_file": "10-meeting-structure.md",
      "last_synced": "[value]"
    }
  }
}
```

Replace `[value]` with the actual `last_synced` timestamp for each doc (or null if
not yet synced). Replace `[TODAY_ISO]` with today's date in ISO 8601 format.

---

## Step 6 — Report

Tell the user what happened:

> "Onboarding process docs synced. Here's what changed:
>
> ✅ Updated: [list of doc names that were fetched]
> ⏩ Already current: [list of doc names that were up to date]
>
> New docs added to your local folder: [list, if any]
>
> Next sync: run 'sync onboarding docs' any time, or [if scheduled] it runs automatically
> every [frequency]."

---

## Scheduling

If the user asks to run this on a schedule (e.g., "check for updates weekly"), use the
`schedule` skill to create a recurring task. Suggested frequency: weekly on Monday morning,
so docs are current before the OBM sync.

Trigger phrase to use in the scheduled task: `"sync my onboarding process docs"`

---

## PM Handoff — SKILL RESULT

When running under PM orchestration, complete the sync and return:

```
## SKILL RESULT: onboarding-process-sync
Timestamp: [ISO 8601]
Customer: None
Actions taken: Checked Drive folder. Compared [N] docs to local manifest.
Findings:
  Updated: [list of doc names fetched from Drive]
  Already current: [list of doc names unchanged]
  New docs added: [list, or "none"]
  All current: [if no updates were needed]
Confidence: High (if Drive accessible); Low (if Drive unreachable)
Gaps/failures: [Drive API unavailable; specific docs that failed to fetch]
Suggested next: If a specific process question is in scope — read the relevant
  doc from onboarding-process/ to answer after sync completes.
Flags for Jared: None
```
