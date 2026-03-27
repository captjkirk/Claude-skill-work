---
name: email-templates
description: "INTERNAL — invoked by PM only. Do not trigger directly on user messages. Draft and customize customer emails using the team's standard templates in Google Docs. Invoked whenever any workflow results in needing to draft a customer email — always check for a matching template before drafting from scratch. Covers: kickoff emails, follow-ups, post-call emails, reverse demo prep, graduation, and any onboarding-context customer email."
---

# Email Templates Skill

This skill fetches the team's living email templates from Google Docs and customizes them for a specific customer and situation.

All email drafts, whether an applicable template is identified or not should always create Gmail drafts using contentType: text/html

## Source of Truth

The canonical templates live in a Google Doc. The Document ID is stored in your workspace memory — check `MEMORY.md` under "Email Templates Configuration" or `emails/CLAUDE.md` for the Document ID.

**Finding the templates doc ID:**
```bash
WORKSPACE=$(find /sessions/*/mnt -maxdepth 2 -name "MEMORY.md" 2>/dev/null | grep -v ".skills" | head -1 | xargs dirname)
grep -A2 "Templates Doc ID\|TEMPLATES_DOC_ID\|templates_doc" "$WORKSPACE/MEMORY.md" 2>/dev/null | head -5
grep -A2 "Templates Doc\|templates doc\|Google Doc" "$WORKSPACE/emails/CLAUDE.md" 2>/dev/null | head -5
```

If no doc ID is configured yet, ask the user:
> "I don't see an email templates doc configured. Do you have a Google Doc with your email
> templates? If so, share the document ID (the long string in the URL). Or run the begin
> skill to configure it."

Default team shared templates doc (use if user hasn't configured their own):
- **Document ID:** `1Mu2k-5y4RsvoxRl0gTUjLk9L3D5gPFZQtFkoY_Lecw0`
- **Direct link:** https://docs.google.com/document/d/1Mu2k-5y4RsvoxRl0gTUjLk9L3D5gPFZQtFkoY_Lecw0/edit

Use `google_drive_fetch` with the document ID to pull the latest version. Never rely on a cached or previously-seen version — always fetch live.

If the user asks for the link to their templates doc, or wants to add a new template, share the direct link above (or their configured doc link if different).

## Template Selection

After fetching the Google Doc, review the available templates and determine whether any match the situation. Templates are organized by type (e.g., "Post-Kickoff call follow-up", "Closed/Won - Welcome Email"). If a template closely matches the intent of the email, use it as the starting point. If nothing fits — for example, the user needs a check-in email, a re-engagement nudge, or something situational that doesn't map to any existing template — draft from scratch using available customer context. Don't force a template where one doesn't apply.

## How to Use the Templates

The templates are starting points, not rigid forms. Every customer is different, and the email should reflect what actually happened on the call and what the customer actually needs. Here's how to think about customization:

### Gather Context First

Before drafting, pull together everything relevant about the customer:

1. **Customer dossier** — Check `customers/<account-kebab>/<account-kebab>.md` first. It has current contacts, communication notes, relationship health, and recent interaction history. This is the authoritative source — faster and richer than re-researching from scratch.
2. **Meeting / email thread context** — Pay attention to what the user says. If they reference a call ("follow up from my call with X"), pull the meeting from Fathom. If they reference an email thread ("help me reply to this chain"), read the thread via Gmail. If both are relevant, pull both. Don't default to one over the other — just follow the cue.
3. **Opportunity data** — If the user has pasted or previously shared Salesforce opportunity data, use it for account details, contacts, products, partner info, etc.
4. **Conversation history** — The current chat may already contain relevant context from earlier in the session.

### Customize Intelligently

With context in hand, adapt the template:

- **Reorder sections** to match what makes the most logical sense for this customer's situation. The template order is a sensible default, but if a customer's biggest next step is scheduling the sync (not community access), lead with that.
- **Remove sections** that don't apply. If the customer already provided org IDs, installed the app, or completed a survey — don't ask for those things again. Acknowledging what they've already done (briefly) is better than re-asking.
- **Add sections** for things that came up on the call but aren't in the standard template. Open questions, customer-specific clarifications, unique asks.
- **Modify language** to reflect the actual conversation. If specific people were named, use their names. If a specific timeline was discussed, reference it. Generic placeholders should be replaced with real details.
- **Collapse related items** when it reduces noise. If two template sections are really about the same thing for this customer, combine them.

### Links and Resources

The Google Doc contains the canonical links (community access, surveys, etc.). Always pull these from the doc rather than hardcoding them — they may be updated over time.

For links NOT in the template (scheduling links, slide decks, etc.), ask the user to provide them or check if they've already been shared in the conversation.

### Tone

**Always check `emails/brand-voice.md`** before drafting — it's the definitive guide to the OBM's email voice, built from their actual sent email corpus. Key conventions covered there:

- Greeting style by context (Hey vs. Hi, group vs. 1:1, familiar vs. first contact)
- What to do vs. never do (no "Please find attached", no "I hope this email finds you well")
- Structural patterns for short replies, long multi-topic emails, and re-engagement
- The "Receipts" principle: always hyperlink docs.blackthorn.io, community.blackthorn.io, or Loom to back up technical answers
- Good news / bad news sequencing (lead with what IS possible)
- Status/checklist format for technical diagnoses
- Subject line format: `[Topic] - [Company Name]` in Title Case with hyphen

Short version: direct, warm, practical. But don't rely on that alone — the full guide has the specifics that make emails sound natural and professional.

### Output

### Subject Line Format

Always follow the subject line convention when creating a draft:

- **All emails:** Title Case with a hyphen separating topic from company name — [Topic] - [Company Name or Abbreviation]
  - e.g., "Blackthorn Kickoff Follow Up - Sam Houston State Univ." or "Additional Call - RCP"

Present the drafted email in the conversation so the user can review and request changes before sending. Include a note about any links or details that still need to be filled in.

**Never create a Gmail draft without first presenting the full email content in the conversation for the user to review and approve.** Only call `gmail_create_draft` after explicit approval.

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
## SKILL RESULT: email-templates
Timestamp: [ISO 8601]
Customer: [customer name]
Actions taken: [template fetched; template selected or drafted from scratch; customized]
Findings: [full email draft — subject line, recipients, complete body]
Confidence: [High | Medium | Low — confidence in template match and customization accuracy]
Gaps/failures: [template doc unavailable; links that need manual fill-in; missing contact info]
Suggested next: [Tier 2] Present draft to Jared for approval before creating Gmail draft
Flags for Jared: [ALWAYS flag email drafts — external sends are Tier 2. Include the full
  draft in the flag so Jared can review and approve in one step. After approval,
  call gmail_create_draft with contentType: text/html. Never create the draft before approval.]
```

Email drafts are ALWAYS Tier 2. PM will present the draft to Jared for approval.
Only after explicit approval does PM call gmail_create_draft.
