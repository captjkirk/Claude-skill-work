# Onboarding Process

This folder caches the official Blackthorn onboarding process docs from Google Drive,
and holds personal process notes and decision logs.

---

## Shared Drive Folder

All official process documents live in Google Drive:

**[2026 Onboarding Process Docs](https://drive.google.com/drive/folders/1L-zC-wWBHR2VQxYKMYNjiSoUyRqQRQXa)**
(folder ID: `1L-zC-wWBHR2VQxYKMYNjiSoUyRqQRQXa`)

Current tracked docs:
- `1-onboarding-process-summary.md` — Master reference; resource inventory across Drive, Gmail, and Slack
- `10-meeting-structure.md` — Synthesized 10-meeting framework (March 2026)
- `risk-assessment-flagging-process.md` — When and how to flag accounts
- `sales-to-onboarding-handoff.md` — Steps from closed-won through OBM kickoff

These are local cached copies. Run `sync onboarding docs` to pull any updates from Drive.

---

## Keeping Docs in Sync

The `onboarding-process-sync` skill handles everything:
- Checks Drive for documents newer than the local cache
- Fetches updated content and overwrites the local file
- Updates `manifest.json` with the latest sync timestamps
- Reports exactly what changed

**To sync manually:** say "sync onboarding docs" or "check for onboarding process updates"

**To sync on a schedule:** say "sync onboarding docs weekly" — the skill will set up an
automatic Monday morning check via the schedule skill.

The `manifest.json` file in this folder is the source of truth for what's been synced
and when. Don't edit it manually.

---

## What Goes Here Locally

- Cached Drive docs (auto-managed by the sync skill — don't edit these manually)
- `manifest.json` — sync state (auto-managed)
- Personal process notes that don't belong in the shared Drive (edge cases, your own observations)
- Decision logs for non-standard onboarding situations
- Draft SOPs you're working on before they're ready to share

Do NOT manually duplicate Drive content here outside of the synced cache files.

---

## MEMORY SYSTEM

This folder contains a file called MEMORY.md. Read it before responding in this folder.
Write to it when the user asks to remember something. Entries are persistent until removed.
