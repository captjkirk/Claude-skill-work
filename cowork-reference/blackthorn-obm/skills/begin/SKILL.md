---
name: begin
description: >
  Initialize a Blackthorn team workspace for a new user. Run once when first setting up
  the plugin. Creates the full folder structure, seeds MEMORY.md with the Blackthorn team
  roster, configures Calendly integration, sets up email templates, and creates the Slack
  briefing channel. Trigger phrases include: "set up my workspace", "initialize my workspace",
  "first time setup", "run begin", "set up the plugin", or any time a new team member
  installs this plugin and needs to get configured.
---

# Begin — Blackthorn Team Workspace Setup

One-time setup that configures the full workspace for a new Blackthorn team member. Safe
to re-run if something needs to be reset or reconfigured.

---

## Before You Start

Tell the user:
> "Let's get your workspace set up. I'll walk through this step by step — most choices are
> just a click, and you can skip or come back to anything. It takes about 5–10 minutes."

---

## Step -1 — Personal Preferences

Check your current personal preferences context:

- **If detailed preferences exist** (name, role, communication style, tools clearly described):
  Use `AskUserQuestion`:
  - Question: "I already have your preferences on file. Want to review or update anything before we start?"
  - Options:
    - "No — looks good, let's go"
    - "Yes — update my communication style"
    - "Yes — something else to update"

  If they want to update: ask in chat what's changed. Then generate an updated preferences
  block (see format at end of this skill) and say:
  > "Here's your updated preferences block — copy everything between the lines and paste it
  > into Claude Settings → Personal Preferences."

  Then `AskUserQuestion`: "Done — ready to continue" / "I'll do it later"

- **If preferences are blank or sparse**: Run the quick interview below, one question at a time.

### Quick Preferences Interview

**1. Communication style** — `AskUserQuestion`:
> "How do you like your responses?"
- 📌 Short and direct — get to the point, no fluff
- 📋 Detailed with context — explain the thinking, full picture
- 🔀 Depends on the task — match length to what's needed

**2. Working style** — `AskUserQuestion` (multiSelect):
> "How should I work with you? Pick as many as feel right."
- 🔔 Proactively flag things I should know — don't wait for me to ask
- ✋ Always ask before sending, posting, or drafting anything on my behalf
- 🔁 Push back when I'm about to do something inefficient
- ⚡ Anticipate my next step without being asked

**3. Anything else** — ask in chat:
> "Anything else you'd want me to always keep in mind?"

### Generate Preferences Block

After the interview, generate a preferences block using the format below. Say:
> "Here are your personal preferences — copy everything between the lines and paste it into
> Claude Settings → Personal Preferences."

Show the block. Then `AskUserQuestion`:
- "Done — I've pasted it in"
- "Skip for now — I'll set it up later"

Continue regardless of which they pick.

---

## Personal Preferences Format

```
## My AI Assistant
My assistant's name is Claude. [1-2 sentences describing personality based on their choices.
Written as instructions to Claude.]

## About Me
My name is [USER_FULL]. I work at Blackthorn as [ROLE/DEPT]. [1-2 sentences about their
work context based on what came up in the interview or department selection.]

## My Preferred Tools
Salesforce, Gmail, Slack, Fathom, Calendly

## How to Work With Me
[1-2 sentences covering communication style and behavioral preferences from steps 1-3.
Concrete and specific — not generic.]

## Behavior Rules — Always Follow These
**Stay in character.** You have a name and a personality — own it at all times.

**Read MEMORY.md at the start of every Cowork session.** When working inside a Cowork
folder, read MEMORY.md before responding. Use what you find to inform your work —
don't announce it, just be informed by it.

**Memory is proactive when substantive.** Write to MEMORY.md without being asked when:
(1) it's not already on file, (2) it would clearly be useful across sessions, (3) it's not
already covered by personal preferences. Announce it briefly when doing so proactively.
Always write immediately when the user explicitly asks using phrases like "remember this,"
"make a note," "save this," "log this," or "don't forget."

**Flag contradictions.** If asked to remember something conflicting with an existing
memory or preference, flag it rather than silently overwriting. Ask how to reconcile.
```

---

## Step 0 — Identify the User

Call `gmail_get_profile` to get the current user's name and email address.

Verify the email ends with `@blackthorn.io`. If not, stop and say:
> "This plugin is designed for Blackthorn team members. It looks like you're signed in as
> [email]. If that's wrong, check your Gmail MCP connection and try again."

Extract:
- `USER_FIRST` — first name (lowercase for channel naming, title case for display)
- `USER_LAST` — last name
- `USER_EMAIL` — full email address
- `USER_FULL` — full name (title case)

---

## Step 0b — Detect Operating System

Infer the host OS from the workspace path.

```bash
find /sessions/*/mnt -maxdepth 2 -type d 2>/dev/null | head -5
```

- If the path contains `/mnt/c/` or `/mnt/[a-z]/` → `OS = "windows"`
- If the path contains `/Users/` or resembles a Mac iCloud path → `OS = "mac"`
- If uncertain, use `AskUserQuestion`:
  - Question: "What type of computer are you setting this up on?"
  - Options: "Mac", "Windows"

Store `OS` for use throughout this skill. Reference it when providing Fathom MCP config
paths, terminal instructions, or any OS-specific guidance.

---

## Step 0c — Department

Use `AskUserQuestion`:
- Question: "This plugin includes Blackthorn Onboarding team-specific skills — kickoff
  decks, COM updates, flagged account syncs, and customer dossier management. Are you on
  the Onboarding team, or from a different department?"
- Options:
  - "Onboarding & Enablement"
  - "Customer Success"
  - "Sales"
  - "Product"
  - "Other — I'll specify"

Store as `DEPT`.

If "Other — I'll specify": ask in chat: "What department or team are you on?"
Update `DEPT` with their answer.

If DEPT is not "Onboarding & Enablement":
  Say:
  > "Got it. The core tools — Fathom, email, Slack, Calendly, Blackthorn Support — all apply
  > to you. The OBM-specific skills (kickoff decks, COM updates, flagged syncs) are in the
  > plugin and available if you ever need them, but we'll skip the OBM-specific setup steps."

Set `OBM_MODE = false`. For all steps marked **[OBM only]** below, skip unless the user
explicitly asks.

If DEPT = "Onboarding & Enablement": set `OBM_MODE = true` and proceed with full setup.

---

## Step 1 — Find the Workspace

Find the mounted workspace:

```bash
find /sessions/*/mnt -maxdepth 1 -type d 2>/dev/null | grep -v "^\." | head -5
```

If multiple candidates exist, pick the one most likely to be the user's folder (look for
an existing CLAUDE.md or a folder name containing "Cowork"). If uncertain, use
`AskUserQuestion` to confirm which folder is their workspace.

Store as `WORKSPACE`.

---

## Step 2 — Review + Create Folder Structure

Before creating anything, show the user what will be created and let them customize it.

Present this list in chat:

> "Here's the folder structure I'll create for your workspace. Each one has a purpose —
> let me know if you want to add or remove anything."
>
> | Folder | What it's for |
> |--------|--------------|
> | `customers/` | Customer dossiers, meeting caches, and account history |
> | `emails/` | Email templates, brand voice profile, and contact context |
> | `calendly/` | Your Calendly meeting links catalog and lookup logic |
> | `onboarding-process/` | SOPs, process notes, and links to the shared Google Drive process docs |
> | `Blackthorn LMO/` | License management org — navigation notes and license data |
> | `Daily Prep/` | Day prep briefs and end-of-day recaps |
> | `outputs/` | All deliverables, organized by customer or category |
> | `reference/` | Blackthorn product docs, Learning Hub CSV, team headshots, XML schemas |
> | `personal-growth/` | Career goals, learning notes, and development tracking |
> | `Productivity/` | TASKS.md and task tracking |

Then use `AskUserQuestion`:
- Question: "Want to make any changes to this folder structure before I create it?"
- Options:
  - "Looks good — create them all"
  - "Remove a folder I won't use"
  - "Add a custom folder"
  - "Both — add some and remove some"

**If "Remove a folder":** Use `AskUserQuestion` (multiSelect):
- Question: "Which folders do you want to skip? (You can always create them manually later.)"
- Options: list each folder name from the table above
- Store the selected names as `SKIP_FOLDERS`

**If "Add a custom folder":** Ask in chat:
> "What should the folder be called, and what will you use it for?"
Store each addition as `CUSTOM_FOLDERS` (name + purpose). These get created with a basic CLAUDE.md.

**If "Both":** Run the remove step first, then the add step.

**After customization is settled**, create all non-skipped folders:

```bash
# Default folders (create if not in SKIP_FOLDERS)
mkdir -p "$WORKSPACE/customers"
mkdir -p "$WORKSPACE/emails"
mkdir -p "$WORKSPACE/calendly"
mkdir -p "$WORKSPACE/onboarding-process"
mkdir -p "$WORKSPACE/Blackthorn LMO"
mkdir -p "$WORKSPACE/Daily Prep"
mkdir -p "$WORKSPACE/outputs/skill-updates"
mkdir -p "$WORKSPACE/reference/team-headshots"
mkdir -p "$WORKSPACE/personal-growth"
mkdir -p "$WORKSPACE/Productivity"
```

For any `CUSTOM_FOLDERS`, create the folder and write a minimal CLAUDE.md:
```markdown
# [Folder Name]

[Purpose as described by user]

---

**MEMORY SYSTEM**

This folder contains a file called MEMORY.md. Read it before responding in this folder.
Write to it when the user asks to remember something. Entries are persistent until removed.
```
Also create an empty MEMORY.md in each custom folder.

---

## Step 3 — Copy Workspace Templates

Locate the plugin root:
```bash
PLUGIN_ROOT=$(find /sessions -path "*/blackthorn-obm/workspace-template" -type d 2>/dev/null | head -1 | sed 's|/workspace-template||')
TEMPLATE_DIR="$PLUGIN_ROOT/workspace-template"
```

**For each file in `workspace-template/`, copy to the workspace if not already present.**
Do NOT overwrite existing files:

```bash
for f in "$TEMPLATE_DIR"/CLAUDE.md "$TEMPLATE_DIR"/MEMORY.md "$TEMPLATE_DIR"/PROCESS-LESSONS.md; do
  fname=$(basename "$f")
  if [ ! -f "$WORKSPACE/$fname" ]; then
    cp "$f" "$WORKSPACE/$fname"
  fi
done
```

Do the same for each subfolder template file (calendly/, emails/, customers/, Productivity/, onboarding-process/).

This includes copying `onboarding-process/manifest.json` — the sync skill depends on it.

**After copying CLAUDE.md:** Replace the `[OBM_NAME]` placeholder with the user's full name:
```bash
sed -i "s/\[OBM_NAME\]/$USER_FULL/g" "$WORKSPACE/CLAUDE.md"
```

---

## Step 4 — Seed MEMORY.md + Team Roster

Check if MEMORY.md is empty or newly created:
```bash
wc -l "$WORKSPACE/MEMORY.md"
```

If empty or just the template header, write the default team roster block below.

```markdown
# Memory

_Last updated: [TODAY]_

## User Setup

- **Name:** [USER_FULL]
- **Email:** [USER_EMAIL]
- **Department:** [DEPT]
- **OS:** [OS]

---

## Blackthorn Team

**Onboarding team:**
- Emily Powers — Director of Onboarding
- Ashley Wagner — VP of Customer Experience
- Nathan Gonzalez — Onboarding & Enablement Manager
- Noah Merrikin — Onboarding & Enablement Manager
- Dustin Morris — Onboarding & Enablement Manager

**Customer Success team:**
- Barb Watkins — Director of Customer Success
- Grace Boboye — Customer Success Manager
- Carly Blair — Customer Success Manager
- Ellie Silverstein — Customer Success Manager
- Lexi Wachtell — Customer Success Manager
- Nicole Roth — Senior Customer Success Manager

**Sales:**
- Dylan Dunn — Account Executive
- Jason Gannen — Account Executive
- Lauren Orscheln — Account Executive
- Michael Disraeli — Account Executive
- Ted Caito — Account Executive

## Recurring Meetings
- **Flagged Onboarding Sync** — Every other Monday, internal review of at-risk accounts
- **OBM Sync** — Mondays at 1 PM MT, internal team sync
- **Office Hours** — Daily round-robin rotation; open to any Blackthorn customer
- **Monthly CS/OBM 1:1s** — Meet with each CS manager once a month

## Known Constraints & Workflows

### Updating Skills — Correct Process
The `.skills/` runtime directory is **read-only**. Direct edits via `sed -i`, `cp`, or Python
file writes will always fail.

The correct process every time:
1. `cp -r /sessions/*/mnt/.skills/skills/<skill-name> /tmp/skill-patches/<skill-name>`
2. `chmod -R u+w /tmp/skill-patches/`
3. Edit from `/tmp/skill-patches/`
4. Package: `cd /sessions/*/mnt/.skills/skills/skill-creator && python3 -m scripts.package_skill /tmp/skill-patches/<skill-name> /tmp/skill-output`
5. Copy `.skill` files to `outputs/skill-updates/` and present with `present_files`
6. Update the `Skills/` human-readable copies

### Gmail Draft Workflow — Validate Before Creating
**Never create a Gmail draft without first presenting the full email content in the chat
for the user to review and approve.** Draft in conversation first. Only call
`gmail_create_draft` after explicit approval.

### Inline Hyperlink Standard
Always use inline hyperlinks — link text embedded naturally in sentences, never bare URLs
or a "Resources" section at the end.
```

Replace `[TODAY]`, `[USER_FULL]`, `[USER_EMAIL]`, `[DEPT]`, and `[OS]` with actual values.

### Roster Confirmation Loop

After writing the roster, use `AskUserQuestion`:
- Question: "The default Blackthorn team roster has been loaded into your memory. Want to make any changes?"
- Options:
  - "Looks good — move on"
  - "Add a team member or note"
  - "Remove or edit someone"
  - "I'll update it manually later"

**If "Add a team member or note":**
Ask in chat:
> "Who should I add? Give me their name, role, and any context (e.g., 'Jordan Smith —
> Senior AE, handles enterprise accounts' or 'Brian Jones — IT contact for ACME Corp')."

Write the entry to the appropriate section in MEMORY.md. Then loop:
`AskUserQuestion`:
- "Yes — add another person"
- "That's everyone — move on"

**If "Remove or edit someone":**
Ask in chat: "Who should I remove or edit, and what should change?"
Make the change, confirm it, then ask: "Anything else to change?"

Continue the roster loop until the user says "move on" or "looks good."

---

## Step 4b — OBM Priorities **[OBM only]**

*Skip if `OBM_MODE = false`.*

Use `AskUserQuestion` (multiSelect):
- Question: "What are your top priorities as an OBM right now? I'll use these to tailor your daily prep briefs and proactively surface relevant info."
- Options:
  - 🎯 Getting active customers to first live event
  - 🚨 Managing flagged or at-risk accounts
  - 📋 Building and refining the onboarding process
  - 🤝 Strengthening CS team handoffs and collaboration
  - 📚 Learning Blackthorn products deeper
  - ⚡ Reducing admin overhead (emails, COM updates, notes)
  - 📅 Managing office hours and unassigned customer questions

Write their selections to MEMORY.md under a "Current Focus" section:
```markdown
## Current Focus

Priorities as of [TODAY]:
- [selected item 1]
- [selected item 2]
...
```

---

## Step 5 — Calendly Setup

Use `AskUserQuestion`:
- Question: "Let's set up your Calendly. Where are you with it?"
- Options:
  - "I have Calendly connected — let's configure it"
  - "I haven't connected Calendly yet — skip for now"
  - "What's Calendly used for here?"

**If configuring:**
Call `users-get_current_user` to get their Calendly user URI. Store it in MEMORY.md:
```markdown
### Calendly Configuration
- **User URI:** [API URI from response]
- **Catalog last synced:** Not yet — run the Calendly catalog sync to build your meeting link catalog
```

Also write `calendly/CLAUDE.md` using the template from `workspace-template/calendly/CLAUDE.md`,
replacing `[CALENDLY_USER_URI]` with their URI.

Say: "Connected! Run 'sync my Calendly catalog' any time to build your full meeting link library."

**If skip:** Add to TASKS.md:
```
- [ ] **Set up Calendly integration** — re-run the begin skill and choose "configure it"
```

**If "what's it used for":**
Explain: "Calendly is how you share meeting links with customers — the plugin auto-looks up
the right link for any email or message so you don't have to hunt for it. Once connected,
run 'sync my Calendly catalog' and it'll catalog all your meeting types."
Then ask the question again.

---

## Step 6 — Email Templates

Use `AskUserQuestion`:
- Question: "For customer emails — how do you want to handle templates?"
- Options:
  - "Use the shared Blackthorn OBM template doc"
  - "I have my own Google Doc — I'll provide the ID"
  - "Build my email voice from my sent mail (no templates yet)"
  - "Skip email setup for now"

**If shared templates:** store `TEMPLATES_DOC_ID = "1Mu2k-5y4RsvoxRl0gTUjLk9L3D5gPFZQtFkoY_Lecw0"` in `emails/CLAUDE.md` and MEMORY.md.

**If own doc:** ask in chat for their Google Doc ID. Store it.

**If build from sent mail:**
1. Search Gmail: `gmail_search_messages` with `in:sent after:[60-days-ago]`, limit 40
2. Read bodies of 50 representative emails — prioritize customer-facing, vary by thread length and recency
3. Analyze for: greeting style, sign-off, sentence length, formality, recurring phrases
4. Write `emails/brand-voice.md` as behavioral guidance Claude can apply when drafting
5. Say: "I've drafted an email voice profile from your last 60 days of sent mail. Check `emails/brand-voice.md` — edit anything that feels off."
6. Store `TEMPLATES_DOC_ID = "none"` in MEMORY.md

**If skip:** Add to TASKS.md:
```
- [ ] **Set up email templates** — re-run begin and choose an email template option
```

Write to `emails/CLAUDE.md` replacing `[TEMPLATES_DOC_ID]` with the actual ID (or "none").

---

## Step 7 — Slack Briefing Channel

Search for a channel named `[USER_FIRST]-briefing` using `slack_search_channels`.

If it doesn't exist:
> "Create a private Slack channel called `[USER_FIRST]-briefing` and star it — that's where
> your daily prep briefs will be posted."

If it already exists: confirm the channel ID and store it in MEMORY.md.

---

## Step 8 — Customer Dossier System

Copy customer template files from the plugin if not already present:

```bash
for f in _TEMPLATE.md generate_customer_claude.py CLAUDE.md MEMORY.md; do
  if [ ! -f "$WORKSPACE/customers/$f" ]; then
    cp "$TEMPLATE_DIR/customers/$f" "$WORKSPACE/customers/$f"
  fi
done
```

---

## Step 8b — Copy Reference Library

Copy silently — no announcement unless something fails:

```bash
PLUGIN_REF="$TEMPLATE_DIR/reference"
WORKSPACE_REF="$WORKSPACE/reference"
mkdir -p "$WORKSPACE_REF"

for item in "$PLUGIN_REF"/BlackthornLearningHubContent.csv \
            "$PLUGIN_REF/product-docs" \
            "$PLUGIN_REF/articles" \
            "$PLUGIN_REF/xml schema files"; do
  name=$(basename "$item")
  if [ ! -e "$WORKSPACE_REF/$name" ]; then
    cp -r "$item" "$WORKSPACE_REF/$name"
  fi
done
```

What's included:
- `BlackthornLearningHubContent.csv` — full Learning Hub catalog with shareable links. Always grep this before searching the web for any Learning Hub URL.
- `product-docs/` — official Blackthorn documentation (Events, Payments, Messaging — Feb 2026). Required for the blackthorn-support skill.
- `articles/` — 650 supplementary knowledge base articles (~Oct 2024).
- `xml schema files/` — Salesforce object schemas for Events, Payments, and SMS.

### Onboarding Process Docs — Initial Sync Offer

After copying reference files, use `AskUserQuestion`:
- Question: "Want me to do an initial sync of the onboarding process docs from Google Drive? This pulls down the latest versions of the team's official process documents into your local folder."
- Options:
  - "Yes — sync them now"
  - "Skip for now — I'll sync manually later"
  - "Set up a weekly auto-sync instead"

**If "sync now":** Run the `onboarding-process-sync` skill immediately.

**If "set up weekly auto-sync":** Use the `schedule` skill to create a recurring Monday
morning task with trigger phrase `"sync my onboarding process docs"`. Then run the sync
skill once immediately to populate the initial cache.

**If "skip":** Add to TASKS.md:
```
- [ ] **Sync onboarding process docs** — say "sync onboarding docs" to pull the latest from Drive
```

---

## Step 9 — Kickoff Deck Setup **[OBM only]**

*Skip if `OBM_MODE = false`.*

Use `AskUserQuestion`:
- Question: "Do you have the Blackthorn Onboarding Intro template for kickoff decks?"
- Options:
  - "Yes — it's already in my workspace"
  - "No — show me how to get it"
  - "Skip this for now"

**If yes:** Verify at `$WORKSPACE/reference/kickoff-deck-template/Blackthorn-Onboarding-Intro-Template.pptx`. Confirm if found; note the path if missing.

**If no:**
> "Open [the Blackthorn Onboarding Intro template](https://docs.google.com/presentation/d/1oB2yZgEAWn1mdFh3_DonpJZ6XQ13D871QX-fnLkByIM/edit),
> make a copy (File > Make a copy), download it as .pptx (File > Download > Microsoft PowerPoint),
> and drop it into `reference/kickoff-deck-template/` named `Blackthorn-Onboarding-Intro-Template.pptx`."

**If skip:** Add to TASKS.md.

### Headshots Setup

The plugin ships with the full Blackthorn team headshot library. Copy it silently:
```bash
if [ ! -d "$WORKSPACE/reference/team-headshots" ] || [ -z "$(ls -A $WORKSPACE/reference/team-headshots)" ]; then
  cp -r "$TEMPLATE_DIR/reference/team-headshots/." "$WORKSPACE/reference/team-headshots/"
fi
```

**Your own headshot** — ask separately using `AskUserQuestion`:
- Question: "Do you have a headshot of yourself to add? It'll appear on slide 3 of every kickoff deck."
- Options:
  - "Yes — I'll paste a Drive link now"
  - "Skip — add to my tasks"

If they provide a link, download and save as `[firstname]-[lastname].ext`.
If skip: add to TASKS.md.

---

## Step 9b — Fathom MCP Setup Check

Use `AskUserQuestion`:
- Question: "Is Fathom connected in your Claude Desktop?"
- Options:
  - "Yes — it's working"
  - "No — help me set it up"
  - "Not sure — test it"

**If "yes" or "not sure":** Call `fathom_list_teams`. If it responds, confirm: "Fathom is connected." If it fails, fall through to instructions.

**If "no" or fathom_list_teams fails:** provide OS-specific setup instructions based on `OS`:

**Mac:**
> **Fathom MCP Setup — Mac**
> 1. Verify Node.js: open Terminal → `node --version`. If missing, install from [nodejs.org](https://nodejs.org) (LTS).
> 2. Claude Desktop → Settings → Developer → Edit Config
> 3. Add inside `"mcpServers"`:
>    ```json
>    "fathom": {
>      "command": "npx",
>      "args": ["-y", "@fathomhq/mcp-server"],
>      "env": { "FATHOM_API_KEY": "your-api-key-here" }
>    }
>    ```
> 4. Get API key: Fathom → Settings → Integrations → API → Create key
> 5. Save and restart Claude Desktop

**Windows:**
> **Fathom MCP Setup — Windows**
> 1. Install Node.js from [nodejs.org](https://nodejs.org) — check "Add to PATH" during install
> 2. Open PowerShell **as Administrator**: `npm install -g @fathomhq/mcp-server`
> 3. Config file: paste `%APPDATA%\Claude\claude_desktop_config.json` in File Explorer (create if missing)
> 4. Add the Fathom server block (same JSON as above)
> 5. Get API key and save → restart Claude Desktop
>
> **Common issues:** `npx` not found → reinstall Node with PATH checked. PowerShell script error → run `Set-ExecutionPolicy RemoteSigned` as admin. Config missing → create `{ "mcpServers": {} }` manually.

---

## Step 10 — TASKS.md

Create `Productivity/TASKS.md` if it doesn't exist:

```markdown
# TASKS.md — [USER_FULL]

_Last updated: [TODAY]_

## Active
<!-- Current tasks with owners and due dates -->

## Waiting On
<!-- Items blocked on someone else -->

## Done
<!-- Completed tasks — move here with completion date -->
```

---

## Step 10b — Automated Workflows

This plugin includes three automation features. Walk through each one now so the user
can get them running before they close this session.

Say:
> "There are three automated workflows built into this plugin — here's how they work and
> how to turn them on."

---

### Automation 1: Morning Brief (runs daily at 7 AM)

Explain:
> "Every weekday morning at 7 AM, the morning orchestrator checks your calendar, scans
> Gmail and Slack for anything flagged on your active accounts, and delivers a briefing
> to your `[USER_FIRST]-briefing` Slack channel. It covers who you're meeting with, what's
> open on each account, and what needs attention before your first call."

Use `AskUserQuestion`:
- Question: "Want me to schedule the morning brief to run automatically at 7 AM on weekdays?"
- Options:
  - "Yes — schedule it now"
  - "Skip — I'll trigger it manually"

**If yes:** Use the `schedule` skill to create a weekday task at 7:00 AM with trigger
phrase `"run morning prep"`. Confirm once created.

**If skip:** Add to TASKS.md:
```
- [ ] **Schedule morning brief** — say "schedule morning orchestrator at 7am weekdays" when ready
```

---

### Automation 2: Post-Meeting Sweep (15 min after each meeting)

Explain — this one has a manual step involved:
> "After each meeting, the post-meeting sweep automatically pulls the Fathom recording,
> checks Gmail for related threads, and routes everything through PM — COM update suggestions,
> dossier updates, PFQE posts if there's a product question, follow-up email drafts. It fires
> 15 minutes after a meeting ends so the summary is ready before your next call."
>
> "There's one catch: the sweep fires are created from your calendar each morning, but they
> have to be created in a regular session — not inside the scheduled task that runs the morning
> brief. So the morning brief ends with a reminder: **open a new session and say 'create today's
> sweep tasks.'** That takes about 10 seconds and sets up automatic post-call processing for the
> whole day."

Use `AskUserQuestion`:
- Question: "Got it — does the post-meeting sweep sound useful for your workflow?"
- Options:
  - "Yes — I'll run 'create today's sweep tasks' each morning after my brief"
  - "Not sure yet — I'll decide later"

**If yes:** Confirm the daily habit:
> "Perfect. Each morning after your brief lands in Slack, open a new session and say
> 'create today's sweep tasks'. That's it — sweeps will fire automatically after each call."

Add a note to MEMORY.md under "Known Constraints & Workflows":
```markdown
### Post-Meeting Sweep — Daily Manual Step Required
After the morning brief each day, open a new session and say "create today's sweep tasks."
This creates the 15-min-after-meeting fireAt tasks for that day's calendar. Cannot be done
inside the scheduled morning brief session — must be a fresh manual session.
```

**If "not sure":** Add to TASKS.md:
```
- [ ] **Enable post-meeting sweep** — once set up, say "create today's sweep tasks" each
      morning to get automatic post-call processing (Fathom + COM + PFQE + follow-up drafts)
```

---

### Automation 3: Dream (nightly memory consolidation)

Explain:
> "Dream runs at the end of each day and reviews what happened — routes new facts to the
> right customer dossiers, prunes anything stale from memory, and flags any workflow patterns
> worth improving. It's how the system stays current without you having to maintain it manually."

Use `AskUserQuestion`:
- Question: "Want to schedule Dream to run automatically each night?"
- Options:
  - "Yes — schedule it nightly"
  - "I'd rather run it manually when I feel like it"

**If yes:** Use the `schedule` skill to create a daily task at 11:00 PM with trigger
phrase `"dream"`. Confirm once created.

**If manual:** Say:
> "No problem — just say 'dream' at the end of any session where you want to consolidate
> what happened. Especially useful after a busy day or a long session with a lot of new info."

---

## Step 11 — Report

Provide a summary when complete:

> "Your workspace is ready, [USER_FIRST]. Here's what was set up:
> ✅ Folder structure created
> ✅ Team roster loaded into memory
> ✅ Department: [DEPT]
> ✅ Calendly — [configured / pending]
> ✅ Email templates — [shared / your doc / voice profile / pending]
> ✅ Slack briefing channel — [found / needs to be created]
> [if OBM] ✅ Kickoff deck template — [ready / pending]
> [if OBM] ✅ OBM priorities captured
> ✅ Morning brief — [scheduled at 7 AM weekdays / manual]
> ✅ Post-meeting sweep — [enabled / pending]
> ✅ Dream — [scheduled nightly / manual]
>
> **Daily habit:** After your morning brief lands in Slack, open a new session and say
> 'create today's sweep tasks' — that activates post-call processing for the day.
>
> **Get started:** Try 'prep me for today' for a day brief, or [if OBM] 'I have a new customer' to kick off an onboarding."

For anything skipped, add a single line:
> "A few items were skipped — they're in your TASKS.md when you're ready."
