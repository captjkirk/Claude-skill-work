# Blackthorn LMO

This folder is a reference and navigation guide for Blackthorn's License Management Org (LMO) at lmo.blackthorn.io — the Salesforce org where customer package licenses are managed.

---

## What the LMO Is

Blackthorn is a Salesforce ISV (Independent Software Vendor). When customers buy Blackthorn products (Events, Payments, Messaging), their licenses are tracked in Blackthorn's License Management Org. The LMO is a special Salesforce org that lets the Blackthorn team see which customers have which packages installed, in which orgs, with how many licenses.

---

## What Jared Uses It For

- Verifying a customer's Production and Sandbox org IDs (`Production_Org_ID__c`, `Sandbox_Org_ID__c`)
- Checking license counts and types for a customer account
- Confirming which package version a customer has installed
- Diagnosing issues that require knowing the customer's org state (e.g., package not installed, wrong version, license limit hit)
- Cross-referencing subscriber org data with the COM record in the onboarding Salesforce org

---

## Key Concepts to Document Here

As Jared builds out this folder, useful things to capture include:
- Where to find specific data in the LMO (which object, which field, which view)
- How to interpret subscriber status or license states
- Common LMO lookups that come up during onboarding
- Any quirks or non-obvious navigation patterns in the org

---

## MEMORY SYSTEM

This folder contains a file called MEMORY.md. It is your external memory for this workspace — use it to bridge the gap between sessions.

**At the start of every session:** Read MEMORY.md before responding. Use what you find to inform your work — don't announce it, just be informed by it.

**Memory is proactive when substantive.** Write to MEMORY.md without being asked when all three apply: (1) it's not already on file, (2) it would clearly be useful across future sessions, (3) it's not already covered by personal preferences. When writing proactively, announce it briefly — one line, e.g. "Adding [X] to memory." For anything ambiguous or uncertain, don't write it — instead add a task to TASKS.md flagged for the next daily prep brief. Customer-specific facts belong in the relevant customer dossier, not MEMORY.md — route them there directly. Always write immediately when the user explicitly asks using phrases like "remember this," "make a note," "save this," "log this," or "don't forget."

**All memories are persistent.** Entries stay in MEMORY.md until the user explicitly asks to remove or change them. Do not auto-delete or expire entries.

**Flag contradictions.** If the user asks you to remember something that conflicts with an existing memory, don't silently overwrite it. Flag the conflict and ask how to reconcile it.
