# Calendly — Your Meeting Link Hub

This folder is the source of truth for all your Calendly event types. Use it any time a meeting link is needed.

---

## TRIGGER: Always Check This Folder First

**Any time a meeting link needs to be provided** — in an email, a Slack message, a COM update, a kickoff deck, or any other context — follow this lookup chain before doing anything else:

1. **Check `catalog.md`** — search by meeting type and co-host name
2. **If found and active** → return the scheduling URL (the link you share with customers)
3. **If found but inactive** → flag it, return the edit URL so you can reactivate it
4. **If not found in catalog** → query the Calendly API (`list_event_types` for your user URI stored in MEMORY.md under "Calendly Configuration")
5. **If not found in API either** → find the closest match in `catalog.md` by meeting type (kickoff → kickoff, handoff → handoff, etc.) and return its scheduling URL with the note: "This doesn't exist yet — clone this one to create it: [link]"

**Never skip this lookup.** Even if you think you know the link, verify against the catalog.

---

## Catalog Structure

`catalog.md` is organized by meeting type category. Each entry includes:

- **Name** — the event type name in Calendly
- **Co-host** — who the meeting is with (or "Solo" for solo events)
- **Duration**
- **Scheduling URL** — the link shared with invitees/customers
- **Edit URL** — direct link to edit in Calendly UI
- **Status** — Active or Inactive
- **Type** — Collective (co-hosted) or Solo

---

## Matching Logic for "Similar Meeting" Fallback

When a requested event doesn't exist, pick the closest fallback using this priority:

1. Same category (kickoff, handoff, sync, etc.)
2. Same duration
3. Active status preferred over inactive
4. Collective preferred over solo if the request implies a co-host

Suggest the clone link and note what needs to be changed (co-host, name).

---

## Known Calendly API Limitations (hardcoded — confirmed as of March 2026)

- **Collective event types cannot be created via API** — must use the Calendly UI clone workflow instead
- **Calendar invitation title/body and email notification workflows are NOT exposed via API** — must be set manually in Calendly UI after creating or cloning
- All event types are `kind: solo` at the API level; collective/co-hosted meetings use `pooling_type: collective`
- **Edit URL format:** `https://calendly.com/event_types/{UUID}/edit`
- UUID is the last segment of the event's API URI: `https://api.calendly.com/event_types/{UUID}`

---

## URL Formats

- **Scheduling URL** (share with invitees): as stored in catalog
- **Edit URL** (Calendly UI editor): `https://calendly.com/event_types/{UUID}/edit`

---

## Catalog Last Synced

Not yet synced. To build your catalog: ask Claude to "sync my Calendly catalog" — it will pull all your event types from the API and generate `catalog.md`.

---

## Your Calendly Configuration

See `MEMORY.md` under "Calendly Configuration" for your user URI and username.
To look up your user: call `users-get_current_user` via the Calendly API.
