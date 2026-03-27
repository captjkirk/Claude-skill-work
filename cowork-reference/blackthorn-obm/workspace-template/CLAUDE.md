# Blackthorn OBM Workspace — [OBM_NAME]

This is your Claude Cowork hub for onboarding and customer success work at Blackthorn — email, meeting prep, CRM updates, and anything worth automating.

---

## Folder Structure

```
Cowork-OS/
├── CLAUDE.md                  ← this file
├── MEMORY.md                  ← persistent memory across sessions
├── PROCESS-LESSONS.md         ← workflow mistake log (always read at session start)
├── customers/                 ← all customer context (dossiers + meeting caches)
│   └── acme/                  ← one folder per customer (kebab-case)
│       ├── CLAUDE.md          ← operative context (auto-derived; read this first)
│       ├── acme.md            ← full dossier (source of truth)
│       └── meetings/          ← Fathom meeting summaries (YYYY-MM-DD-title.md)
├── Blackthorn LMO/            ← LMO navigation, license data, org reference
├── onboarding-process/        ← SOPs, process docs, decision log
├── personal-growth/           ← career development, resume, learning goals
├── Daily Prep/                ← day prep and recap docs only
├── outputs/                   ← all deliverables, organized by customer or category
├── reference/                 ← Blackthorn product and reference docs
│   └── team-headshots/        ← headshot images, named firstname-lastname.ext
├── Productivity/              ← task tracking (TASKS.md)
├── emails/                    ← email brand voice, contacts CRM, session context
├── fathom-mcp/                ← Fathom MCP config (if applicable)
└── calendly/                  ← Calendly meeting catalog + lookup logic
```

---

## Output Organization Rules

| What | Where |
|------|-------|
| Customer operative context | `customers/<name>/CLAUDE.md` (auto-derived; read first) |
| Customer dossiers | `customers/<name>/<name>.md` (full source of truth) |
| Fathom meeting cache | `customers/<name>/meetings/` (one `.md` per call) |
| Day prep / recap docs | `Daily Prep/` |
| Blackthorn product/reference docs | `reference/` |
| Email brand voice, contacts CRM | `emails/` |
| Calendly meeting links and catalog | `calendly/` |
| Everything else (deliverables, reports) | `outputs/<CustomerName or category>/` |

**Nothing goes in root** except CLAUDE.md, MEMORY.md, and PROCESS-LESSONS.md.

---

## MEMORY SYSTEM

MEMORY.md is your external memory across sessions. Read it at the start of every session. Write to it proactively when something is worth keeping long-term. Customer-specific facts go in the relevant dossier, not root memory.

---

## MEMORY HIERARCHY

Always read at session start:
1. `CLAUDE.md` (this file)
2. `MEMORY.md`
3. `PROCESS-LESSONS.md` — scan for lessons relevant to the current task before starting.

When work shifts into a subfolder, also read that subfolder's CLAUDE.md and MEMORY.md.

---

## GLOBAL STANDARDS

### Mistake Logging
Any time a workflow fails or a correction is made mid-task: log it to `PROCESS-LESSONS.md` immediately.

### Pre-Flight Check
Before starting any workflow that touches known error-prone areas — skill updates, COM records, MEMORY.md edits, packaging, Salesforce config — read `PROCESS-LESSONS.md` and surface any relevant lesson.

### Hyperlinks
Always use inline hyperlinks — link text embedded naturally in sentences, never bare URLs or a "Resources" section appended at the end.

### Customer Context
Any time a named customer appears in a task, load context in this order:
1. `customers/<name>/CLAUDE.md` — operative context (phase, blockers, open items, recent activity)
2. `customers/<name>/<name>.md` — full dossier
3. `customers/<name>/meetings/` — Fathom cache

### Cross-Skill Coordination
After any task that surfaces new customer info, flag it for dossier update. After any customer interaction, offer a COM update. After any product question that couldn't be fully answered, offer a PFQE post.

### Meeting Links — Always Check the Calendly Catalog First
Any time a Calendly meeting link is needed — in an email, Slack message, COM update, or kickoff deck — read `calendly/CLAUDE.md` and follow the lookup chain before doing anything else. Never provide a meeting link from memory.

### Email Drafting — Always Invoke the Email Skill First
Before drafting any email, always invoke the **email-templates** skill first. Never draft freehand and check after.

### Gmail Drafts — Always Validate Before Creating
**Never create a Gmail draft without first presenting the full email in the chat for approval.** Draft in conversation first. Only call `gmail_create_draft` after explicit approval.
