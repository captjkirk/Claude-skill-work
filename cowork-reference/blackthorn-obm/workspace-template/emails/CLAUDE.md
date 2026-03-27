# Emails Subfolder — Your Email Workspace

This subfolder handles all email-related work: drafting, replying, researching contacts, and maintaining your mini CRM.

---

## Folder Contents

```
emails/
├── CLAUDE.md              ← this file
├── MEMORY.md              ← session notes and running email context
├── contacts-crm.md        ← mini CRM: top contacts organized by account
└── brand-voice.md         ← your email writing style and conventions
```

---

## Email Templates Doc

**Document ID:** [TEMPLATES_DOC_ID]
**Direct link:** https://docs.google.com/document/d/[TEMPLATES_DOC_ID]/edit

Always fetch live — update this if you create your own templates doc.

---

## How to Use This Subfolder

### When drafting or replying to an email:
1. Check `contacts-crm.md` first — primary contact per account, their role, relationship notes
2. Check `brand-voice.md` for tone, greeting conventions, subject line format
3. Consult the **email-templates skill** — always check for a template match before drafting from scratch
4. All Gmail drafts must use `contentType: text/html`
5. **Never create a Gmail draft without first presenting the full email in the chat for approval**

### Subject Line Convention

**Format:** `[Topic] - [Company Name or Abbreviation]`
- Title Case throughout
- Hyphen (not em-dash) separating topic from company
- Examples: `Blackthorn Kickoff Follow Up - Acme Corp` / `Additional Call - RCP`

---

## Live Data Connection — `customers/` is the authoritative source

`emails/contacts-crm.md` is a fast-access index, not the source of truth. The real data lives in `customers/<account-name>/<account-name>.md` dossiers. The CRM will drift from dossiers over time — that's expected. Its purpose is a quick cross-account view.

- Before drafting any email: check the dossier for current contacts and relationship health
- After any email that surfaces new contact info: update the dossier first

---

## Parent Context

This subfolder inherits all context from root `CLAUDE.md` and `MEMORY.md`. Nothing here overrides root context — it adds to it.
