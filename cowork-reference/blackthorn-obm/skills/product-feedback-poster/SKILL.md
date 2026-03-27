---
name: product-feedback-poster
description: >
  INTERNAL — invoked by PM only. Do not trigger directly on user messages. Analyzes customer emails or
  Fathom recordings and either answers product questions using Blackthorn knowledge or escalates them
  as a structured post to #product-feedback-questions-everything. Invoke when a customer name +
  product question or PFQE signal is present; user references the PFQE channel; or user pastes a
  customer email with a question or complaint about Blackthorn behavior.
---

# Product Feedback Poster

Analyzes customer emails or Fathom meeting transcripts, attempts to answer the question using available Blackthorn product knowledge, then either copies the answer for use or drafts and posts a structured message to **#product-feedback-questions-everything** in Slack.

---

## Gotchas

Failure modes to check before drafting or posting anything.

- **Use `**double asterisks**` for bold in Slack, never `*single asterisks*`.** Single asterisks render as italic in standard markdown. The Slack MCP uses standard markdown, not Slack's native mrkdwn. Headers and field labels must use double asterisks.
- **Medium or Low confidence = post it, even if you have an answer.** A technically correct but incomplete answer is worse than surfacing the question. If you're not confident you've covered all options or edge cases, draft the Slack post and flag your confidence level. Don't let uncertainty become silence.
- **Multiple issues in one call/email = separate posts.** Never combine multiple distinct questions into a single post. Surface all of them, then work through one at a time with approval on each before moving to the next.
- **Customer field: full org name only.** No abbreviations (HAF, ERAU, etc.) in the Customer or Prospect Name field — use the complete organization name.
- **Question or Feedback is a single focused statement — no backstory.** Write it as what you'd say to a PM in a hallway. Background context goes in Business use case, not here.
- **The Slack MCP cannot submit Workflow Builder forms.** The post looks like a workflow submission but the "I got it!" button won't be present — that's a Slack-native interactive element that can't be replicated via API. This is expected behavior, not a bug.
- **Don't post if blackthorn-support gives a high-confidence, complete answer.** The skill's Step 3 options menu exists precisely for this. Only escalate to Slack if the answer is incomplete, uncertain, or the question genuinely warrants product team visibility.

---

## Step 1: Identify source and gather context

Users often trigger this skill with a short, casual reference — like "PFQE channel based on my call with No Labels" or "product feedback post for my emails with HAF." Don't ask for clarification upfront; instead, infer what you can and go fetch the context yourself.

**Inferring the source:**
- If the user says "call", "meeting", or "Fathom" → use the Fathom skill
- If the user says "email", "thread", or "inbox" → search Gmail for the thread
- If neither is specified but a customer name/org is given → try Fathom first (most recent call), then Gmail if nothing found
- If the user pastes content directly → use what they gave you

**Customer name / org shorthand:**
Users may use abbreviations (e.g. "HAF", "ERAU", "No Labels"). Search broadly — try the abbreviation as-is first, then expand if needed. Don't ask for the full name unless search comes up empty.

**If email (via Gmail):**
Search Gmail for the customer name/org and pull the most recent thread. Extract:
- The specific question, behavior observed, or feedback
- Any steps they described, what they expected, what actually happened
- Any urgency signals (go-live date, blocked, frustrated tone)

**If Fathom call:**
Use the Fathom skill to pull the summary for the most recent relevant call. Specifically, call
`fathom_get_summary` with the recording's `recording_id` — this returns a summary where every
bullet and section is hyperlinked to the exact timestamp in the recording. Focus on moments where:
- The customer described unexpected behavior
- They asked "is this how it's supposed to work?"
- They expressed frustration or mentioned a workaround
- A specific feature or limitation came up

Note the timestamp link for the specific moment the feedback was raised — you'll embed it inline
in the Slack post draft (see Step 4).

---

## Step 1.5: Duplicate Check

Before researching or drafting, verify this topic hasn't already been posted to #product-feedback-questions-everything.

**Check order:**

1. **Check `reference/pfqe-log.md` first** — this is the local post log maintained after every successful PFQE post. Read it and scan for any entry that covers the same feature, behavior, or question. If a match exists, include the log entry in the SKILL RESULT as a note: "PFQE post already on file for this topic ([date] — [topic]). Proceeding only if this is a meaningfully different angle." Let PM decide whether to continue or surface the log entry to Jared instead.

   ```bash
   find /sessions -path "*/mnt/Cowork-OS/reference/pfqe-log.md" 2>/dev/null | head -1
   ```

2. **If no match in pfqe-log.md** — optionally search Slack as a secondary check: `slack_search_public_and_private` in `#product-feedback-questions-everything` using the feature/behavior as the search term. Only do this if the local log is empty or sparse; skip if the log has clear coverage.

If clearly already covered → do not draft. Return a SKILL RESULT noting the duplicate with the relevant log/Slack link, and mark as resolved. PM surfaces this to Jared instead of a new post.

If not covered or uncertain → continue to Step 2.

---

## Step 2: Research an answer

**Priority order — work through these until you have a confident answer or exhaust options:**

1. **Blackthorn Support skill** — use it to look up the behavior, limitation, or configuration in question.

2. **Local Blackthorn docs** — if the skill isn't available, look for PDF or Markdown documentation in the user's folder (e.g., `Blackthorn Events - February 2026.pdf`, `User Docs - MD file format_Feb2026/`). Ask the user if they have a specific folder with their Blackthorn docs.

3. **Built-in product knowledge** — if no docs are available, fall back to Claude's training knowledge about Blackthorn Events, Payments, and Messaging. Be explicit when you're doing this: "I'm drawing on general product knowledge here, not a doc."

**You're looking for**: Is this expected behavior? Is it a known limitation? Is there a configuration workaround? Or is this genuinely unexpected / a potential bug?

**Research accuracy is critical.** Don't present partial information as the full picture. If you find one thing (e.g. "only two fields exist"), keep looking to make sure you're not missing others. A confident but incomplete answer is worse than saying "I'm not sure." When in doubt about whether more options or workarounds exist, say so explicitly rather than implying the list is exhaustive. Also look for workarounds — sometimes a question that seems unanswerable has a practical path forward that's worth surfacing.

---

## Step 3: Evaluate the answer

Format the answer internally:

```
ANSWER: [Written response to the customer's question]
Source: [Blackthorn Support skill / Blackthorn Events doc / general product knowledge]
Confidence: [High / Medium / Low — and why if not High]
Next steps: [What should happen after — send to customer, follow up, etc.]
```

**Routing decision (no user input needed):**
- **Confidence: High** → include the answer in SKILL RESULT Findings as resolved.
  PM presents to Jared. No Slack post needed.
- **Confidence: Medium or Low, OR question warrants product team visibility** →
  proceed directly to Step 4 and draft the Slack post. Include both the answer
  and the draft post in SKILL RESULT so PM can surface both to Jared.
- **No answer found** → proceed to Step 4.

When running under PM orchestration, never use AskUserQuestion here — route based
on confidence level and proceed. PM will present options to Jared in the consolidated
output if a choice is needed.

---

## Step 4: Draft the Product Feedback Form content

The channel uses a Slack Workflow Builder form called **Product Feedback Form** with exactly these fields:

| Field | Type | Notes |
|-------|------|-------|
| **Which App is this in reference to?** | Picklist | Events, Payments, or Messaging. If it spans multiple apps, choose Events. |
| **Customer or Prospect Name?** | Text | Full org name |
| **Question or Feedback** | Rich text | Keep it tight — one focused question or observation. No rambling, but don't sacrifice necessary context. |
| **Business use case** | Rich text | Why does this matter to the customer and their organization? |

**Important note on the workflow:** The Slack MCP cannot programmatically submit a Workflow Builder form. Instead, the skill posts a message formatted to look identical to a real workflow submission. The only difference is the "I got it!" interactive button won't be present — that's a Slack workflow-only feature that can't be replicated via the API.

### Filling in the fields

**Which App:** Use the exact option labels below — these include Slack user mentions that notify the right product owner automatically (same behavior as the workflow form):

| Option | Use when... |
|--------|-------------|
| `Events & Other <@U0644HDHLRJ>` | Anything related to event registration, attendees, checkout, sessions, capacity, kiosk, navigator, or features that span multiple apps |
| `Payments <@U02944WGXJ8>` | PayLink, Virtual Terminal, allocations, invoices, payment gateways, non-gateway transactions |
| `Messaging <@U02944WGXJ8>` | A2P, SMS, messaging compliance |
| `Compliance <@U02944WGXJ8>` | Compliance-specific questions |
| `Storefront <@U02944WGXJ8>` | Storefront-related features |

Default to `Events & Other <@U0644HDHLRJ>` when the topic spans multiple apps or is unclear.

**Customer or Prospect Name:** Use the full org name, not an abbreviation.

**Question or Feedback:** Write this as a single crisp statement of the question or issue — what you'd say to a PM in a hallway. Specific enough to be actionable, tight enough to read in 10 seconds. Include what was observed, what was expected, and (for bugs) enough to reproduce it. This is NOT the place for backstory — that goes in Business use case.

If the source was a Fathom call, hyperlink the most descriptive phrase in the statement to the
timestamp where the customer raised it — inline, naturally, so the text reads cleanly and the
link is the most relevant anchor. Don't add a separate URL or call it out as a link explicitly.

- ❌ "Customer had issues with waitlist"
- ✅ "[Waitlist auto-promotion not triggering on cancellation](https://fathom.video/share/TOKEN?tab=summary&timestamp=XXX) — capacity=200, waitlist enabled, cancellations are not moving the next waitlisted registrant to Registered status."

**Business use case:** Answer "why does this matter to *them*?" — real-world impact, not feature description. Cover: what they're trying to accomplish, what's blocked or at risk, any go-live date or renewal timeline, scale of impact. 2-4 sentences max.

### Present the draft

Show the draft formatted exactly as it will appear in Slack, so the user can approve what they'll see posted.

**Slack formatting note:** Use `**double asterisks**` for bold labels. The Slack MCP collapses blank lines (double newlines) during markdown processing — to preserve visual spacing between sections, place a **zero-width space character (U+200B)** on each blank line. This character is invisible but prevents the MCP from treating the line as empty and collapsing it. Do NOT include "Sent using @Claude" in the message — the MCP appends it automatically; including it causes duplication.

The title line (`**Product Feedback Form**`) has NO blank line before the first field. Zero-width space lines go between every subsequent section.

```
**Product Feedback Form**
**App(s) referenced:**
[exact option label including the user mention, e.g. "Events & Other <@U0644HDHLRJ>"]
​
**Customer or Prospect Name:**
[Full org name]
​
**Question or Feedback:**
[Tight, specific statement of the question or issue]
​
**Business use case:**
[Why it matters — impact, context, urgency, go-live risk]
​
**Submission from:**
<@USERID>
```

(Each ​ line above contains a zero-width space character U+200B — copy this template exactly when drafting.)

The `<@UXXXXXXXX>` mentions in the App field will ping the relevant product owner when the message is posted — this replicates the workflow's notification routing.

---

## Step 5: Package for PM approval

Do NOT post to Slack directly. Include the full draft in the SKILL RESULT as a Tier 2 flag.
PM presents it to Jared for approval. Only after Jared's explicit approval does PM call
`slack_send_message` to post to **#product-feedback-questions-everything**.

**After a successful post:** PM must append an entry to `reference/pfqe-log.md`:

```markdown
### YYYY-MM-DD — [Topic / Feature Area]
**Customer:** [Customer name]
**Question/Feedback:** [One-line summary from the post]
**Slack link:** [Link to the message if available, otherwise omit]
```

This entry is Tier 1 — PM writes it autonomously after the post is confirmed sent. It is the canonical local record that future duplicate checks rely on.

If multiple feedback items were found in the source, package each as a separate draft in
the SKILL RESULT. PM surfaces them one at a time for Jared's review.

Note: The post will look like a workflow submission but won't have the "I got it!" button — that's a Slack-only interactive element tied to the actual workflow form.

---

---

## Customer Dossier Integration

> This step only applies if the current user is @blackthorn.io domain. Verify with
> `gmail_get_profile` — if the email does not end with @blackthorn.io, skip this section entirely and do not
> mention dossiers.

**Before starting research:** Check for an existing dossier in
`*/mnt/Cowork-OS/customers/`. Convert the customer name to
kebab-case to find the file (e.g., `royal-college-of-psychiatrists.md`). If found, read it
before doing any other research — it will tell you the email domain (for Fathom/Gmail
searches), known contacts, open items, and recent interaction history. This saves significant
research time and surfaces context that external searches alone will not.

**After completing the workflow:** Update the dossier with anything new that surfaced —
new contacts, status changes, decisions made, action items, or a new interaction log entry.
Update the `Last Contact` field in the header. If no dossier exists yet, create one from the
template at `_TEMPLATE.md` in the same folder.
## Notes

- **Tone**: Write for the product team, not the customer. Direct, factual, enough context to act on without reading the whole email thread.
- **Don't over-summarize**: If the customer said something specific and vivid, quote them rather than paraphrasing.
- **Multiple pieces of feedback**: If the email/call has more than one distinct question or issue, always treat them as separate posts — one per item. Let the user know how many you found and work through them one at a time, getting approval on each before moving to the next.
- **Confidence matters**: Always surface your confidence level on the answer. A Medium or Low confidence answer should almost always result in a Slack post even if you technically have an answer — flag it clearly.

---

## PM Handoff — SKILL RESULT

When running under PM orchestration, do not surface output directly to the user.
Complete analysis and draft the post, then return a SKILL RESULT block to PM.

```
## SKILL RESULT: product-feedback-poster
Timestamp: [ISO 8601]
Customer: [customer name | None]
Actions taken: [source analyzed; blackthorn-support called; post drafted or question answered]
Findings: [if answerable: full answer with confidence level and doc links.
  if escalating: full draft Slack post for #product-feedback-questions-everything]
Confidence: [High if answered confidently; Medium/Low if escalating to Slack]
Gaps/failures: [topics that couldn't be answered; sources that returned nothing]
Suggested next: None
Flags for Jared: [ALWAYS flag Slack posts — external sends are Tier 2. Include the
  full draft post in the flag for Jared's review and approval before posting.
  If blackthorn-support gave a High-confidence answer, no flag needed — include the
  answer in Findings and mark as resolved.]
```
