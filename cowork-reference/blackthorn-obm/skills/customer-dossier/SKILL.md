---
name: customer-dossier
description: >
  INTERNAL — invoked by PM only. Do not trigger directly on user messages. Read, update, and create
  customer account dossiers stored as markdown files in the customers/ folder of Jared's workspace.
  Use this skill proactively whenever a customer name appears in any workflow — morning prep, COM
  updates, Fathom research, email drafting, flagged syncs, product feedback posts, or any
  customer-facing task. The dossiers are the fastest way to build context on an account without
  re-researching from scratch. Trigger phrases include: "update the dossier for [customer]", "what do
  we know about [customer]", "create a profile for [customer]", "check the dossier for [customer]",
  "who haven't I heard from recently", "which customers are overdue for follow-up", or any time a
  named customer account is the subject of work and context would be useful. Also invoke automatically
  at the end of any workflow where new information about a customer was surfaced.
---

# Customer Dossier Skill

Customer dossiers are markdown files that accumulate everything known about an account —
contacts, personality notes, onboarding status, product configuration, open items, support
cases, a full interaction log, and a chronological timeline. Reading one before any customer
workflow saves time and improves the quality of every output. Updating one after any customer
workflow ensures the context compounds over time.

---

## Dossier Location

All dossiers live in the `customers/` folder inside Jared's workspace — the mounted Claude
folder on his computer. Use the Glob tool to find it if the path isn't immediately obvious:

```
glob: customers/*/*.md
```

Files live inside their own folder: `customers/royal-college-of-psychiatrists/royal-college-of-psychiatrists.md`, `customers/acme-corp/acme-corp.md`.

The template for new dossiers is `customers/_TEMPLATE.md`. When creating a new dossier, create the folder first: `customers/<kebab-name>/`, then save the dossier as `customers/<kebab-name>/<kebab-name>.md`.

---

## Step 0 — Scan for All Customer Mentions (Multi-Customer Contexts)

Before doing anything else, determine whether the current context involves one customer or
several. Many workflows — 1:1s with Emily, team meetings, daily prep, flagged syncs — touch
multiple accounts in a single conversation or transcript.

If the context involves multiple customers (e.g., a 1:1 recap, a team meeting summary, a
Fathom transcript where several accounts came up), identify **all** of them before proceeding.
Don't stop at the first customer name you recognize.

For each customer identified:
1. Check for an existing dossier
2. Extract any details that surfaced about that customer in this context
3. Update (or create) their dossier with what's relevant

The bar for updating is low — even a single sentence about an account ("Emily mentioned APT
Travel is at risk of churning") is worth a dated Internal Notes or Interaction Log entry. You
don't need a full conversation about a customer to justify updating their file.

---

## Step 1 — Find the Right File

Given a customer name, locate the dossier:

1. Convert the org name to kebab-case (lowercase, spaces and special chars → hyphens)
2. Look for an exact match in the customers folder
3. If no exact match, look for a close match (partial name, common abbreviation, acronym)
4. If nothing close exists, the customer has no dossier yet — proceed to **Create** mode

Examples:
- "Royal College of Psychiatrists" → `customers/royal-college-of-psychiatrists/royal-college-of-psychiatrists.md`
- "RCPsych" → `customers/royal-college-of-psychiatrists/royal-college-of-psychiatrists.md` (match on known abbreviation)
- "Acme" → `customers/acme-corp/acme-corp.md` (partial match)

---

## Step 2 — Read Mode (Loading Context)

**Start with CLAUDE.md.** Every customer folder contains a `CLAUDE.md` with a compact
operative summary — current phase, contacts, blockers, next steps, open items, recent
activity. Read it first. It loads fast and covers 80% of what you need for most tasks.
Only read the full dossier when you need deeper context (personality notes, full timeline,
product configuration detail, etc.).

When loading the full dossier to inform a task, focus on these sections:

| Task | Sections to prioritize |
|------|----------------------|
| Morning prep / meeting briefing | Onboarding Status, Open Items, Upcoming Events, Communication Notes, last 2 Interaction Log entries |
| COM update | Onboarding Status, Open Items, Support Cases, last Interaction Log entry |
| Drafting an email | Communication Notes, Key Contacts, last Interaction Log entry |
| Fathom research | Key Contacts (for names/domains), Product Context |
| Flagged sync prep | Everything — read the full file |
| "What do I know about X?" | Everything |

After reading, extract:
- **Email domain** (from the Domain field in the header) — use for Fathom and Gmail searches
- **Known contacts and their roles** — so you can filter search results to the right people
- **Open items and blockers** — so you can flag what's still unresolved
- **Last contact date** — so you know how fresh the relationship is

---

## Step 3 — Update Mode (Writing Back)

After any workflow that surfaced new customer information, update the dossier. Not all sections
update the same way — factual sections are always additive, but interpretive sections require
re-synthesis across the full history.

### Linking to Fathom moments

The goal is for the dossier to be self-contained — if a piece of information came from a call,
the dossier should link directly to that moment so there's no need to go back to Fathom to find
it. This saves time and keeps the dossier as the single source of truth.

**Whenever you're writing content that came from a Fathom recording**, call `fathom_get_summary`
on that recording to get the timestamp-linked version, then embed the link inline — hyperlink the
most descriptive phrase in the sentence. This applies across all sections:

- Watch Items, Open Items, blockers — link to the call where the issue surfaced
- Onboarding Status narrative — link to the moment that defined the current state
- Personality & Relationship Notes — link to behavioral observations, not just notable quotes
- Product feedback, pain points, workarounds mentioned — link to where they were raised
- Any specific commitment, decision, or concern documented in any section

The pattern is always the same: hyperlink the relevant phrase inline, don't add a separate URL
line. If you don't yet have the `fathom_get_summary` result for the recording, fetch it — the
timestamp links are worth the extra call.

### Two types of updates

**Factual sections — always additive.** Never overwrite or remove entries. Just append.
These are sections where each entry is a discrete record:
- Interaction Log
- Timeline
- Support Cases
- Open Items (check off completed, add new ones)

**Interpretive sections — re-synthesize, don't just patch.** Before updating these, re-read
the existing content AND factor in the new information together. The goal is a balanced,
cumulative portrait — not a snapshot of the most recent interaction. One difficult call
doesn't make someone difficult. One enthusiastic email doesn't make someone a champion.
Look for patterns across multiple touchpoints before updating a characterization.
These sections require judgment:
- Personality & Relationship Notes
- Communication Notes
- Onboarding Status (the narrative "where things stand" summary)
- Watch Items
- Internal Notes (one person's frustration in a 1:1 is not the whole picture)

When updating interpretive sections, ask: does this new signal change the overall picture,
or is it a one-off? If it's a genuine shift in pattern, update the characterization. If it's
an outlier, note it in the Interaction Log but don't let it rewrite the profile. The dossier
should reflect who someone consistently is, not who they were on their worst or best day.

### Personality & Relationship Notes — quality standard

This section has two modes depending on how much source material exists. The template
reflects both. The key rule: **never fill a thin profile with plausible-sounding guesses.**
A sparse entry that's honest is more useful than a rich-looking entry that was fabricated
from a job title and one email.

**RICH format** — use when you have Fathom transcripts, real email threads, or multiple
interactions to draw from. Write in full sentences. Use behavioral evidence — what you've
actually observed — not adjective labels. "Responsive" and "strategic-level" tell Jared
nothing useful. "When asked about SF access, she replied '@Shane can you update here?' and
stepped back" tells him exactly how she operates.

What good rich entries include:
- **Communication style:** How they actually write and speak. Long or short? Fast or slow
  to respond? Do they escalate or absorb tension? Formal or casual?
- **Decision-making:** Do they own decisions or need to loop others in? Who do they defer
  to? Who defers to them? What does it take to get them to commit?
- **Technical level:** Not just a label — what does it mean practically? What can they do
  themselves vs. what do they need Jared for?
- **Patterns:** What do they reliably do across multiple touchpoints? What tends to slip?
  What triggers re-engagement when things go quiet?
- **Relationship health:** More than a one-word label — what's the evidence behind it?
- **Notable quotes:** Direct quotes are the most reliable signal. Capture them when you
  have them — and always include a Fathom link to the specific moment when one is available.
  Format: `"[quote]" — [Name], [date] ([Fathom link](url))`. If you have a playback URL
  with a timestamp (e.g., from action items or transcript analysis), link directly to that
  moment. If you only have the share URL, link to that. Example:
  `"THIS IS VITAL..." — Tithee, 3/4/26 ([Fathom](https://fathom.video/calls/123?timestamp=240))`
- **Recent activity:** Most recent observation — what did they do or say, and when?
- **Flags:** Anything Jared needs to route around or watch for (e.g., "She holds the
  limitations list but tends to go MIA — use Jillian for delivery instead").

**SPARSE format** — use when the dossier was seeded from a handoff doc, CSV, or a single
brief interaction. State the known facts and be explicit that depth is limited:

```
**[Contact Name]** ([Title] — [role])
- Known facts: [Title, email, how they came up]
- Signal so far: [One sentence on any behavioral observation, or "No direct interaction to date."]
- ⚪ *Limited depth — not enough source material for a full profile. Update after first substantive interaction.*
```

This makes the absence of information legible rather than hiding it behind placeholder text.
A ⚪ marker signals to Jared that this contact needs a real interaction before the profile
can be trusted.

### Auto-Refresh CLAUDE.md After Every Dossier Update

Every customer folder contains a `CLAUDE.md` — a lightweight operative context file
auto-derived from the dossier. It holds the at-a-glance status, contacts, blockers,
next steps, open items, and recent activity in a compact form that every skill reads
first before touching the full dossier.

**After writing any changes to a dossier, always regenerate the customer's CLAUDE.md
automatically — no need to ask Jared.** Run:

```bash
python3 $(find /sessions -path "*/mnt/*/customers/generate_customer_claude.py" 2>/dev/null | head -1) --customer <kebab-folder-name>
```

Where `<kebab-folder-name>` is the customer's folder name (e.g., `bystronic`,
`royal-college-of-psychiatrists`, `clutch-solutions`).

This must happen silently as part of every dossier update — not as an optional step.
The CLAUDE.md should always reflect the current state of the dossier immediately after
any write. Do not announce this to Jared unless the regeneration fails.

---

### What to update and when

**After every customer touchpoint (call, email, Slack exchange):**
- Add a new entry to the **Interaction Log** (most recent first)
- Add a row to the **Timeline**
- Update **Last Contact** in the header
- Update or check off items in **Open Items**
- Update **Onboarding Status** if anything has changed
- **Regenerate CLAUDE.md** (see above — always, automatically)
- If the account status or primary POC changed, check whether `emails/contacts-crm.md` needs
  a light update too (status in the Quick Status Dashboard, or a relationship note on the contact).
  The CRM is a derived view of the dossiers — it will drift, and that's expected — but major
  changes like graduation, flag status shifts, or contact changes are worth propagating.

**When new contacts surface:**
- Add to **Key Contacts** table
- Add a **Personality & Relationship Notes** entry — use the rich format if you have source
  material (Fathom transcripts, email threads, multiple interactions); use the sparse format
  if you don't. See the Personality Notes standard below for what each format looks like.
- If the contact is likely to appear in email workflows (a primary POC, a decision-maker, or
  anyone Jared emails regularly), also add them to `emails/contacts-crm.md` under the account's
  section. Keep the CRM entry light — name, title, email, one-line relationship note. The dossier
  holds the full depth; the CRM is just the fast-access index.

**When health changes:**
- Update **Onboarding Health** in the header
- Add a `Health Shift` row to the Timeline (format: `🟢→🟡 — reason`)

**When new issues surface:**
- Add to **Support Cases** table if it's a filed case
- Add to **Open Items** if it's an action item
- Add to **Watch Items** if it needs monitoring

**When an event is mentioned:**
- Add or update a row in **Upcoming Events**

**When contract/renewal info comes up in conversation or email:**
- Update **Contract Start** and **Contract Renewal** in the header

**When a customer is no longer on the active onboarding tracker (dropped off a CSV export,
explicitly handed off, or confirmed graduated):**
- Keep the dossier — never delete it. It's a permanent reference.
- Update **Account Status** in the header. Use context to infer the right status — don't
  wait for Jared to spell it out. Signals to look for:
  - Recent notes mention a handoff call, CS transition, or scorecard completion → 🎓 **Graduated**
  - Notes reference a reassignment or a different CSM taking over → 🔄 **Transferred** (note who)
  - Account was stalled, unresponsive, or otherwise inactive with no clear resolution → 🗄️ **Archived** (note why)
- Add a Timeline entry capturing the transition: date, type (`Milestone`), and what happened
- Exclude these accounts from active onboarding workflows — flagged syncs, "who needs
  follow-up" summaries, and proactive outreach queues. They're not Jared's active
  responsibility right now.
- But don't treat them as gone. If one of these customers comes up in any context —
  an email thread, a Fathom call, a day-prep question — pull their dossier and use it
  normally. Graduated doesn't mean irrelevant; it just means they're not being actively
  onboarded at this moment.

**When a customer is 🤝 Contact Only (not Jared's onboarding account):**
This covers anyone Jared has meaningful contact with but doesn't own — customers met at
office hours, accounts being onboarded by another CSM, or anyone where the relationship
exists but the project doesn't belong to Jared.
- Keep contact details, personality notes, and interaction log — these are worth having
- Skip or mark N/A all onboarding-specific sections: Onboarding Status, Onboarding Health,
  Upcoming Events, Open Items (unless they're Jared's to action), and Watch Items related
  to onboarding progress
- Never include in active onboarding workflows, follow-up queues, or flagged syncs
- If this person or account comes up in a future context, use the dossier for relationship
  context only — not as a project record

**When seeding a dossier from the Onboarding Tracker CSV or any automated export:**
- The `Flagged` checkbox is the source of truth for flag status. If `Flagged = false` (unchecked),
  treat any related fields — flagged reason, flagged category, flag notes — as stale data left
  over from a previous flag that was cleared. Omit them entirely; don't carry them into the
  dossier. The Onboarding Tracker doesn't always clear these fields when the flag is removed.

**When internal Blackthorn context surfaces (1:1s, team meetings, internal Slack):**
- Add a dated entry to **Internal Notes** with the source (e.g., "Emily 1:1", "Team Meeting", "Slack — #rcpsych")
- Keep this section clearly separate from customer-facing interactions — it captures the internal view of the account, not what the customer said or did

**Proactively search internal Slack for customer context.** When building or updating a dossier,
search Slack for internal discussions about the customer — not just customer-facing channels.
Before searching, read the `slack-search` skill (find it at `find /sessions -path "*/mnt/.skills/skills/slack-search/SKILL.md" 2>/dev/null | head -1` — or the remote plugin path at `find /sessions -path "*plugin*/skills/slack-search/SKILL.md" 2>/dev/null | head -1`) and follow its search strategy and modifier guidance.
Useful things to look for:
- A dedicated internal channel for the account (e.g., `#rcpsych`, `#acme-onboarding`)
- Threads where teammates have flagged concerns, asked questions, or shared observations about the account
- Open internal questions that haven't been asked to the customer yet
- Any internal decisions or positions taken about how to handle the account

Content from these searches belongs in **Internal Notes**, not the Interaction Log. The
distinction matters: Internal Notes is the internal view of the account; the Interaction Log
is the record of what actually happened in customer-facing touchpoints.

### Product Context — structure and categorization

The Product Context section has four sub-sections. Populate them as information becomes available — not all will apply to every customer from day one.

**Blackthorn Features in Use (Out-of-the-Box)**
A table of native Blackthorn capabilities the customer is actively using. This distinction matters: anyone reading the dossier should immediately understand what's vanilla Blackthorn vs. what's custom-built. Common features to capture: Event Builder, Dynamic Event Pages, Smart Scheduler, Event Items, Event Groups/Keywords, Mobile Check-in App, Deep Clone, iFrame Embed, BT-Campaign Member Sync.

**Custom / Partner-Built**
A table of custom Salesforce work — flows, screen flows, automations, integrations — built on top of Blackthorn by the customer, their SI partner, or a third party. If the customer's primary end-user workflow bypasses standard Blackthorn UI entirely (e.g., volunteer leaders never touch the Event Builder because event creation goes through a custom EC screen flow), call that out explicitly. Whoever reads the dossier next shouldn't assume standard BT behavior applies when it doesn't.

**Pain Points**
Categorize by root cause rather than listing everything in one flat list. The goal is to make it immediately clear who owns the problem and whether a solution exists. Default categories — use what fits, add others as needed:

- **Internal / organizational** — the customer's own coordination gaps, process complexity, or structural issues (e.g., multiple stakeholders who don't communicate, a third party holding credentials, event types that are structurally incompatible). Jared can't fix these; he can only manage around them.
- **Salesforce platform constraints** — things SF architecture is causing, not Blackthorn (e.g., EC community license types don't qualify as full SF users for mobile check-in). Useful for product conversations so BT doesn't absorb blame for Salesforce's limitations.
- **Blackthorn limitations — addressed or workaround in place** — BT doesn't do it natively, but there's a working solution the customer has accepted. Always note what the workaround is — "accepted as interim" tells Jared it's not a live blocker.
- **Blackthorn limitations — no current solution** — BT gap with no workaround; the customer just lives with it. These are the most important items for product feedback because there's nothing to offer right now.
- Add others if something doesn't fit cleanly: "SI partner coordination gaps", "data migration complexity", "third-party integration friction", "volume / scale concerns", etc.

**Feature Requests / Product Feedback**
The "ideal fix" layer — what they'd want if Blackthorn built it properly. Keep this distinct from Pain Points: Pain Points = what's painful today. Feature Requests = what would make it stop being painful. A pain point with no solution often maps 1:1 to a feature request.

### Open Items — three-tier structure

Not all open items are Jared's responsibility or even visible to him. A flat list makes it too easy for third-party coordination items to masquerade as overdue Jared action items. Use three tiers:

**Jared's to-do** — things Jared owns and should act on. Keep this short and honest. If there are more than 4-5 items here, something is probably in the wrong bucket.

**Watching — [owner]'s** — items owned by the customer or their SI partner where Jared would reasonably be looped in on the outcome. He's not actioning these, but he'd know if they closed or stalled. Worth tracking so he can follow up if they surface on a call.

**Third-party coordination — no Jared visibility** — items between the customer and their SI partner (or other third parties) where Jared has no natural visibility and wouldn't necessarily be told when completed. Stripe access grants between a customer and their SI are the canonical example. Don't surface these as open Jared action items — they may already be resolved, and he can't action them anyway. Note the last known status and when it was last mentioned. If one comes up on a call, move it to the appropriate bucket at that point.

### Interaction Log entry format

```markdown
### [Month DD, YYYY] — [Call / Email / Slack / COM Update / Support Case]
**Attendees / participants:** [names, roles — or "—" if async]
**Key takeaways:**
- [signal only — what actually matters]
**Decisions made:**
- [anything that was agreed on or resolved]
**Action items from this:**
- [ ] [Item — owner]
```

When the source is a Fathom call, call `fathom_get_summary` on the recording to get the
timestamp-linked summary. For high-stakes moments in the key takeaways (churn signals,
escalations, specific commitments, product failures, strong sentiment), embed the timestamp
link inline — hyperlink the most descriptive phrase rather than adding a separate URL.

Example key takeaway with a link:
- [Customer said they'd consider not renewing if the waitlist issue isn't resolved](https://fathom.video/share/TOKEN?tab=summary&timestamp=XXX)

### Timeline row format

```
| [Month DD, YYYY] | [Type] | [Brief description] |
```

Types: `Sale / Contract`, `Kickoff`, `Milestone`, `Health Shift`, `Bug`, `Enhancement`,
`Sync`, `Email`, `Go-Live`, `Escalation`, `Post-Launch`

---

## Step 4 — Auto-Create for New Customers

If no dossier exists for a customer, **create one automatically** — don't wait to be asked.
Any meaningful interaction with a customer is enough reason to start a dossier. The goal is
that no customer ever slips through the cracks just because a file hasn't been created yet.

1. Copy the structure from `_TEMPLATE.md`
2. Fill in everything available from the current context — name, contacts, emails, product, use case, any details from the interaction that triggered this
3. Leave unknown fields as `Unknown — not yet captured` rather than blank or omitted
4. Save as `customers/[kebab-case-org-name]/[kebab-case-org-name].md` (create the folder first if it does not exist)
5. Add the first Timeline entry capturing how/when this customer was first encountered (e.g., `| [date] | Milestone | First dossier created — context: [brief description of triggering interaction] |`)
6. Mention to Jared that a new dossier was created and where it lives

The bar for creating a dossier is low: if you're doing any research on a customer, pulling
Fathom data, reading their emails, or preparing for a call with them, that's enough. A
partially-filled dossier is far more useful than no dossier at all — it will fill in over time.

---

## Quick Reference — Header Fields

The header of every dossier has two fields that together determine how much external research
is needed before starting any customer workflow:

**Last Contact** — when the dossier was last updated from a real interaction. Updated after
every touchpoint. Use this to answer "who haven't I heard from in a while?" by scanning just
the first ~15 lines of each dossier file.

**Data Depth** — how complete and reliable the dossier's background context is:
- 🔵 **Comprehensive** — contacts, personality notes, product context, communication preferences,
  contract info, and history are all well-documented. Trust this as the primary source for
  background context. Only check live sources (Gmail, Slack, Fathom) for activity that may
  have occurred *since* the Last Contact date.
- 🟡 **Partial** — some sections are well-filled, others are sparse or missing. Use the dossier
  for what's there but supplement with targeted live research to fill gaps.
- ⚪ **Sparse** — dossier was recently created or is missing most context. Treat it as a
  starting point only and do full research as normal.

### How to use these fields together

| Data Depth | Last Contact | Approach |
|------------|-------------|----------|
| 🔵 Comprehensive | Recent (within ~2 weeks) | Use dossier as primary context. Only check live sources for new activity since Last Contact date. |
| 🔵 Comprehensive | Older (2+ weeks) | Use dossier for background. Do a targeted live search for recent activity — emails, Slack, new Fathom calls. |
| 🟡 Partial | Any | Use dossier for what's documented. Research the gaps. |
| ⚪ Sparse | Any | Do full research. Use dossier only as a skeleton to fill in. |

### Updating Data Depth

Reassess Data Depth whenever you update a dossier. Promote to 🔵 Comprehensive when all of
these are true:
- Key contacts identified with roles
- Personality notes for main contacts are in **rich format** (behavioral evidence, not just
  labels) — contacts with no real interactions yet may use sparse format, but the primary
  POC should have a full rich entry
- Product context and configuration documented
- Communication notes present
- Open items and blockers current
- Timeline has meaningful history

Demote to 🟡 Partial if a section becomes clearly stale or a significant unknown surfaces.
Never demote just because time has passed — that's what Last Contact is for.

---

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

## Identity Check

This dossier system is personal to @blackthorn.io domain. Before integrating
dossier lookups in any shared skill workflow, verify the current user's email via
`gmail_get_profile`. Only proceed with dossier read/write if the email matches
`@blackthorn.io domain`. If it doesn't match, skip the dossier steps silently — don't
mention dossiers to other users.

---

## PM Handoff — SKILL RESULT

When running under PM orchestration, do not surface output directly to the user.
Complete all work, then return a SKILL RESULT block to PM for evaluation:

```
## SKILL RESULT: customer-dossier
Timestamp: [ISO 8601]
Customer: [customer name | multiple if multi-customer context]
Actions taken: [read mode / update mode / create mode; what was written]
Findings: [operative context loaded; what was updated; key signals from the dossier]
Confidence: [High if dossier is Comprehensive; Medium if Partial; Low if Sparse]
Gaps/failures: [dossier missing or couldn't be found; sections that couldn't be populated]
Suggested next: com-update if interaction data surfaced; email-templates if follow-up
  email is needed; fathom if recent calls haven't been cached yet
Flags for Jared: [none expected — dossier operations are Tier 1]
```

After any dossier write, CLAUDE.md must be regenerated automatically:
```bash
python3 $(find /sessions -path "*/mnt/*/customers/generate_customer_claude.py" 2>/dev/null | head -1) --customer <kebab-folder-name>
```
Do this silently. Do not announce to Jared unless regeneration fails.
