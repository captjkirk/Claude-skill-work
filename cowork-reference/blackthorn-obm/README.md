# Blackthorn Plugin

The complete Claude workspace for Blackthorn team members. Core tools work for anyone at Blackthorn — OBM-specific workflows activate automatically based on your department.

## What This Plugin Does

Installs 20 skills and a full workspace structure covering: day prep and meeting recaps, Fathom call research, email drafting, Blackthorn product support, memory management, and workspace organization. OBM team members also get PM-orchestrated workflows, kickoff deck building, COM updates, flagged account syncs, and customer dossier management. Document creation (docx, pdf, pptx, xlsx) and skill management (skill-creator) are handled by global Cowork skills — not bundled here to avoid duplication.

## First-Time Setup

After installing the plugin, run:

> "Set up my workspace" (or "run begin")

The setup skill will:
1. Verify your `@blackthorn.io` identity
2. Ask about your department — OBM-specific steps activate if you're on the Onboarding team
3. Walk through your personal preferences (communication style, working style)
4. Create the full folder structure and seed your memory with the Blackthorn team roster
5. Connect Calendly, email templates, Slack briefing channel, and Fathom
6. Capture your current priorities

Everything uses pick-list questions — minimal typing required.

## Skills Included

### Universal (all Blackthorn team members)

| Skill | What it does |
|-------|-------------|
| **begin** | One-time workspace setup — interactive, picklist-driven |
| **memory-create** | Write entries to MEMORY.md across sessions |
| **memory-delete** | Remove or clear memory entries |
| **subfolders** | Create new project subfolders with CLAUDE.md + MEMORY.md |
| **day-prep-recap** | Morning prep brief and end-of-day recap |
| **fathom** | Search Fathom Video for meeting recordings and transcripts |
| **email-templates** | Fetch and customize email templates or build a voice profile |
| **blackthorn-support** | Blackthorn product expert — Events, Payments, Messaging |
| **blackthorn-brand** | Apply Blackthorn brand voice and visual identity |
| **product-feedback-poster** | Post structured feedback to #product-feedback-questions-everything |
| **onboarding-process-sync** | Sync local process doc cache with the shared Google Drive folder; schedulable |
| **process-mistakes** | Log and surface workflow lessons learned |
| **dream** | Nightly memory consolidation — routes session facts to the right files |

### OBM-Specific (Onboarding & Enablement team)

| Skill | What it does |
|-------|-------------|
| **project-manager** | Orchestration hub — routes all tasks through PM before presenting to user |
| **morning-orchestrator** | Runs daily at 7 AM — reads calendar, schedules sweeps, produces morning brief |
| **post-meeting-sweep** | Fires 15 min after each meeting — pulls Fathom + Gmail and routes findings through PM |
| **customer-dossier** | Read, create, and update customer account files |
| **com-update** | Prepare Salesforce COM field updates after any customer touchpoint |
| **kickoff-deck** | Build customized onboarding intro decks from the Blackthorn template |
| **flagged-onboarding-sync** | Prep COM records for the bi-weekly flagged sync with Emily + Ashley |

These skills are available to all users but are only configured during setup for OBM team members.

## Prerequisites (OBM team only)

Before using kickoff-deck, you'll need:
1. The Blackthorn Onboarding Intro template .pptx in `reference/kickoff-deck-template/`
   (the setup skill links directly to it — File > Make a copy > Download as .pptx)
2. Your own headshot in `reference/team-headshots/` named `firstname-lastname.ext`
   (the full team headshot library ships with the plugin)

## Connections Required

- Gmail MCP — required for most workflows
- Slack MCP — required for day prep, product feedback posting
- Google Drive MCP — required for kickoff deck upload, email templates
- Calendly MCP — required for meeting link lookups
- Fathom MCP — required for meeting research (setup instructions included in begin skill)
- Google Calendar MCP — required for day prep

## Companion Plugins

These add additional capabilities. The OBM plugin no longer requires Cowork OS —
`memory-create`, `memory-delete`, and `subfolders` are now bundled.

| Plugin | Why you might want it | Get it |
|--------|----------------------|--------|
| **slack-by-salesforce** | Powers Slack search in day prep, COM research, product feedback, and dossiers | Search "Slack" in the Cowork plugin marketplace |
| **productivity** | TASKS.md dashboard and task management commands | Search "Productivity" in the marketplace |

Skill management (creating, editing, and packaging skills) is handled by the global **skill-creator** Cowork skill — no separate plugin needed.

## Credits & Inspiration

This plugin draws on ideas and work from people worth naming:

- **[Paul J Lipsky](https://www.youtube.com/@PaulJLipsky)** — the workspace architecture (CLAUDE.md / MEMORY.md / subfolder structure, the `begin` setup flow, `memory-create`, `memory-delete`, `subfolders`) is adapted directly from his [Cowork OS plugin](https://www.youtube.com/@PaulJLipsky). The bundled versions of those skills are based on his work.
- **Dustin** — the `product-feedback-poster` skill concept came from his approach to routing customer questions through a structured Slack channel rather than letting them get lost in email or ad-hoc DMs.

---

## Version

**2.2.1 — March 2026**
- PM: added Active Improvement Scan — PM watches for cross-skill contradictions, routing gaps, repeated low-confidence returns, and judgment calls not covered by routing rules; logs to PROCESS-LESSONS.md immediately and surfaces a one-line note in consolidated output; queues EVO task in TASKS.md for significant patterns
- Dream EVO Pass: expanded scan criteria to include cross-skill contradictions, skills with schema drift vs. PM's expected SKILL RESULT format, routing gaps (natural follow-on skill not triggered), skills with no SKILL RESULT block, stale EVO proposals that were never applied, and PM judgment calls that should become routing rules
- Workspace template: added 4 LMO reference files to Blackthorn LMO/ folder (com-object-schema.md, onboarding-templates.md, opportunity-schema.md, salesforce-app-overview.md) — LMO structure now travels with the plugin for all new installs

**2.2.0 — March 2026**
- PM intake: added context pre-load step — customer-dossier invoked first when context is sparse, before downstream skills are selected
- Activity log: newest entries now at top within each day (INSERT after header, not append); ACTIVITY-LOG.md creation handled if file doesn't exist
- Dream architecture: dream now proposes all memory writes and returns SKILL RESULT to PM; PM executes all Tier 1 writes (MEMORY.md, dossiers, EVO proposals) rather than dream writing directly
- Kickoff-deck: added PM Handoff / SKILL RESULT block; output now routes through PM before presentation
- blackthorn-brand: removed INTERNAL prefix — utility skill, may be invoked directly by PM or other skills
- product-feedback-poster: removed AskUserQuestion from Steps 3 and 5; skill now packages answer and draft in SKILL RESULT with Tier 2 flag; PM presents and gets Jared's approval before posting
- com-update and flagged-onboarding-sync: task sync is now autonomous (Tier 1) — writes to TASKS.md without confirmation, reports in SKILL RESULT
- 5 utility skills (memory-create, memory-delete, subfolders, onboarding-process-sync, process-mistakes): added SKILL RESULT blocks; PM now receives confirmation of all utility operations for ACTIVITY-LOG.md and chaining
- memory-create: added explicit note that PM invocations are equivalent to user triggers — no confirmation needed

**2.1.0 — March 2026**
- PM orchestration enforced: 12 specialist skills marked INTERNAL — invoked by PM only
- Added PM Gate section to CLAUDE.md — hard rule requiring PM intake before any skill fires in manual sessions
- Added 3 missing OBM skills to README: project-manager, morning-orchestrator, post-meeting-sweep
- Excluded document creation skills (docx, pdf, pptx, xlsx, brainstorming) — already available as global Cowork skills; bundling caused duplicates
- Corrected skill count in README: 20
- Excluded skill-creator and schedule — identical to global Cowork versions, no OBM-specific customization
- Added LMO routing to PM: org ID, license, package version, subscriber status signals now route to Blackthorn LMO/ folder
- Added LMO CLAUDE.md to workspace-template — was missing, so new users got the folder but no context
- PM Skill Catalog added: per-skill reference covering all 20 packaged skills — when to invoke, what to request, expected output, deepen/re-route triggers
- PM routing table expanded: added blackthorn-brand, kickoff-deck, memory-create, memory-delete, onboarding-process-sync, process-mistakes, subfolders
- Added Step 10b to begin skill: walks new users through scheduling morning-orchestrator, dream, and explains the post-meeting sweep daily habit
- Removed cowork-plugin-management from companion plugins — skill-creator (bundled) covers all skill management needs

**0.1.0 — March 2026**
- Added department-aware setup (not OBM-only anymore)
- Added personal preferences interview
- Added interactive team roster customization + OBM priorities capture
- Replaced text input with picklist questions throughout setup
- Bundled memory-create, memory-delete, subfolders (Cowork OS no longer required)
- Updated kickoff deck template link and output folder
