---
name: kickoff-deck
description: >
  INTERNAL — invoked by PM only. Do not trigger directly on user messages. Build a customized
  Blackthorn onboarding kickoff deck for a new customer. Invoke when: Jared asks to build a kickoff
  deck; Jared dumps customer data (pre-onboarding survey, Salesforce opportunity, Chatter post, email
  thread) signaling a new account assignment; or a morning brief surfaces a new OBM assignment.
  Extracts customer name, CSM, and AE from context and runs the full workflow through to Drive.
---

# Kickoff Deck Builder

Builds a customized `[Customer] Blackthorn Onboarding Intro` deck from the local baseline
template. This is the deck used on the kickoff call — it introduces the team, covers the
onboarding journey, and sets expectations.

---

## Intake — extracting inputs from context

Jared typically starts a new onboarding session by dumping in data — pre-onboarding survey
responses, a Salesforce opportunity screenshot, a Chatter notification, an email thread, or
some combination. He may not explicitly say "build the kickoff deck." Recognize the pattern
and proceed.

**Extract the required inputs before asking for anything.** Parse whatever was provided for:

| Field | What to look for in the dump |
|-------|------------------------------|
| `customer_name` | Account/company name on the opportunity or Chatter post |
| `csm_name` | "CSM", "Customer Success Manager", or "assigned to" field |
| `ae_name` | "AE", "Account Executive", "closed by", or "opportunity owner" |
| `kickoff_date` | Any date mentioned — defaults to today if not found |

OBM is the current user — call `gmail_get_profile` to get their full name if not already known.

After extracting, confirm the values with the user before proceeding:
> "Got it — here's what I pulled from your dump:
> - Customer: [name]
> - CSM: [name]
> - AE: [name]
> - Date: [date]
>
> Does that look right, or do any of these need adjusting?"

If a field can't be confidently extracted, use `AskUserQuestion` to get just that one piece.
Don't ask for things that are clearly present in the context.

---

## Step 1: Check headshots

Before building, verify headshots exist for the CSM and AE (the current OBM's should be in the team-headshots folder):

```python
workspace / "reference" / "team-headshots" / f"{firstname}-{lastname}.ext"
```

If a headshot is missing, **stop and tell the user**:
> "I need a headshot for [Name] before I can build the deck. Drop it in
> `reference/team-headshots/` named `firstname-lastname.ext` and I'll take it from there."

Do not proceed until all headshots are available.

---

## Step 2: Template sync check

The local baseline lives at:
```
reference/kickoff-deck-template/Blackthorn-Onboarding-Intro-Template.pptx
```

Last synced from Drive: check the file mtime at runtime. Drive source: `[Template - Jan 2026] Blackthorn Onboarding Intro`

Check the Drive version (note: Google Slides files may not appear in Drive search API — if
search returns nothing, skip and proceed with local copy):
1. Search Drive: `name contains 'Blackthorn Onboarding Intro' and name contains 'Template'`
2. Compare `modified_time` to local `mtime`
3. If Drive is newer, flag it and ask the user whether to re-sync first

A monthly scheduled task also runs this check automatically (see "Monthly Sync Check" below).

---

## Step 3: Customer dossier

Check for `customers/<customer-kebab>/CLAUDE.md`. If it doesn't exist, offer to create one
via the `customer-dossier` skill — but don't block deck creation on this.

---

## Step 3b: Extract license data (slide 4)

Before building, identify **which Blackthorn apps the customer purchased** and gather
entitlement details for each. Only purchased apps appear on slide 4 — omitted args are
excluded entirely. Never pass "N/A" as a value.

**Step 1 — identify purchased apps from the data dump:**

| App | Signals to look for |
|-----|---------------------|
| Events | "Events", registration volume, event management use case |
| Payments | "Payments", "PayLink", paid registration processing |
| Messaging | "Messaging", SMS, message credits, phone numbers |

**Step 2 — extract per-app entitlement details:**

| Arg | App | What to look for | Example value |
|-----|-----|-----------------|---------------|
| `--events` | Events | Registrations/year, contracted volume | `"1,100 registrations/year"` |
| `--payments` | Payments | Transaction volume, PayLink scope | `"PayLink included"` |
| `--messaging` | Messaging | Message credits + phone numbers | `"10,000 messages/month, 1 phone number"` |
| `--license-type` | All | License model | `"Registration-based"` |
| `--full-users` | All | Full/admin user seats | `4` (integer) |
| `--light-users` | All | Light/view-only user seats | `4` (integer) |
| `--users` | All | Flat label when not blended | `"Unlimited"` |
| `--support` | All | Support tier | `"Standard Support"` |

**Blended user rule:** If the contract notes a blended model (mix of full + light users),
you MUST have both `full_users` and `light_users` before building. If either is missing, ask:
> "This looks like a blended license — how many full users and light users does [Customer] have?"

Do not default to "Unlimited" for blended accounts. Ask first.

**Per-app rule:** Provide args ONLY for purchased apps. Any arg omitted = that row is removed
from slide 4. The script handles this automatically — never pass "N/A" as a value.

---

## Step 3c: Standard Support vs. Premium Support

Check whether the customer is **Standard Support** (rare, but it changes the deck and process):

Standard support entitlements:
- Kickoff call (included)
- Blackthorn adoption guides / I&C guides (provided; customer self-installs)
- 3 office hours/month
- No Blackthorn-assisted install & configure
- No event template building by Blackthorn

**If Standard Support:**
- Slide 4: use `--support "Standard Support"`
- Slide 14 (Discovery checklist): the I&C bullet should read
  "Customer completes self-guided install & configure using Blackthorn I&C adoption guides"
  — NOT "Customer completes Blackthorn install & configure in sandbox"
- Do NOT include event template bullets in slide 14 — they're not in scope

**If Premium Support** (default): use `--support "Blackthorn Premium Support"` (or omit, it's
the default). Standard slide 14 bullets apply.

---

## Step 4: Build the deck

```bash
python3 <skill_dir>/scripts/build_deck.py \
  --customer "<customer_name>" \
  --csm "<csm_name>" \
  --ae "<ae_name>" \
  --obm "<obm_full_name>" \
  --date "<Month DD, YYYY>" \
  --workspace "<workspace_path>" \
  --output "<workspace_path>/customers/<customer-kebab>/<CustomerSlug>-Blackthorn-Onboarding-Intro.pptx" \
  --license-type "<license_type>" \
  [--events "<X registrations/year>"]         # omit if Events not purchased \
  [--payments "<entitlement text>"]           # omit if Payments not purchased \
  [--messaging "<X messages/month, N phones>"] # omit if Messaging not purchased \
  [--full-users X --light-users Y]            # blended: both required together \
  [--users "Unlimited"]                       # non-blended flat label \
  --support "<Standard Support | Blackthorn Premium Support>"
```

**Locate paths at runtime:**
```python
import glob
skill_dir   = glob.glob("/sessions/*/mnt/.skills/skills/kickoff-deck/")[0]
workspace   = glob.glob("/sessions/*/mnt/Cowork-OS/")[0].rstrip("/")
```

**Output path convention:**
- Save to `customers/<customer-kebab>/`
- Filename: `<CustomerSlug>-Blackthorn-Onboarding-Intro.pptx`
- Example: `customers/parker-institute/PICI-Blackthorn-Onboarding-Intro.pptx`

Create the customer folder if it doesn't exist.

The script handles:
- Headshot swaps for CSM, OBM (Jared), AE on slide 3
- Name updates on slide 3
- "Company Name" → customer name on slide 1
- "Month DD, YYYY" → kickoff date on slide 1
- Slide 4 license table: license type, registrations, users (blended or flat), messaging (or removal), support tier

---

## Step 5: Upload to Google Drive

**Target folder ID:** `1fH6IdprLJimI-sK5NZDW4Ocausn2LRat`

Since the Drive MCP is read-only, upload via Chrome:
1. Navigate to `https://drive.google.com/drive/folders/1fH6IdprLJimI-sK5NZDW4Ocausn2LRat`
2. Upload: `mcp__Claude_in_Chrome__file_upload` with the output PPTX path
3. After upload, open the file in Drive → File > Save as Google Slides (eliminates PPTX rendering skew)
4. Return the sharing link

If Chrome upload fails, provide the local `computer://` link and ask the user to upload manually.

---

## Step 6: Return SKILL RESULT to PM

Complete all build and upload steps, then return a SKILL RESULT to PM.
Do not surface output directly to Jared — PM presents the consolidated output.

```
## SKILL RESULT: kickoff-deck
Timestamp: [ISO 8601]
Customer: [customer name]
Actions taken: Extracted inputs; built deck from template; uploaded to Drive.
  [Or: Chrome upload failed — local file available at computer:// link]
Findings:
  Customer: [name]
  CSM: [name]
  AE: [name]
  OBM: [name]
  Kickoff Date: [date]
  Products: [Events / Payments / Messaging]
  Support tier: [Standard | Premium]
  Deck link: [Google Drive sharing link | local computer:// link if upload failed]
  Local path: customers/<customer-kebab>/[slug]-Blackthorn-Onboarding-Intro.pptx
Confidence: [High if deck built and uploaded; Medium if upload failed or a headshot was
  substituted; Low if required inputs were missing or script errored]
Gaps/failures: [missing headshots used as substitutes; Drive upload failure; template
  sync warning if Drive version is newer than local baseline]
Suggested next: customer-dossier — create or update with kickoff deck note and initial
  customer context extracted from the data dump
Flags for Jared: [headshot missing and placeholder was used — flag with "provide headshot
  for [name] before the kickoff call"; Drive upload failed — link to local file with
  instruction to upload manually; template may be outdated — flag if Drive is newer]
```

---

## Monthly Sync Check

A scheduled task runs monthly to check whether the Drive template has been updated. If it
has, it posts a Slack DM to the current user flagging the change so the local baseline can be re-synced
before the next deck is built.

Scheduled task name: `kickoff-template-sync-check`
See `reference/kickoff-deck-template/` for the baseline and sync date.

To re-sync the baseline manually: download the current Drive template to Downloads, then tell
Jared you're running a re-sync, and repeat the Brian-removal + 3-person rebalancing process
documented in MEMORY.md → "Kickoff Deck Skill" before saving as the new baseline.

---

## Slide 3 Technical Reference

Baseline template element IDs:

| Role | Name SP | Role SP | Photo PIC | rId | Media file |
|------|---------|---------|-----------|-----|-----------|
| CSM (left) | 223 | 220 | 226 | rId3 | image11.png |
| OBM/Jared (center) | 232 | 231 | 233 | rId7 | image8.png |
| AE (right) | 225 | 222 | 228 | rId5 | image7.jpg |

Photo positions (EMU): CSM x=573700 · OBM x=3727200 · AE x=6880750

---

## Headshots library

`reference/team-headshots/`, named `firstname-lastname.ext`:

| Person | File | Role |
|--------|------|------|
| Carly Blair | carly-blair.jpeg | CSM |
| Ellie Silverstein | ellie-silverstein.jpg | CSM |
| Grace Boboye | grace-boboye.png | CSM |
| Lexi Wachtell | lexi-wachtell.png | CSM |
| Nicole Roth | nicole-roth.png | Senior CSM |
| Jared Kirk | jared-kirk.png | OBM |
| Dylan Dunn | dylan-dunn.jpg | AE |
| Jason Gannen | jason-gannen.jpg | AE |
| Lauren Orscheln | lauren-orscheln.jpg | AE |
| Michael Disraeli | michael-disraeli.png | AE |
| Ted Caito | ted-caito.jpg | AE |
| Brian Russe | brian-russe.jpg | (Renewals — not used on slide 3) |
