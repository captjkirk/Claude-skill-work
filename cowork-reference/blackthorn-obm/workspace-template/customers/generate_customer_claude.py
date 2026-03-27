#!/usr/bin/env python3
"""
Generate CLAUDE.md operative context files for each customer folder.
Parses the customer dossier (.md) and extracts key operative fields.
Run this any time a dossier is updated significantly.
"""

import os
import re
from datetime import date

# Dynamic path discovery
import glob as _glob
_paths = _glob.glob("/sessions/*/mnt/*/customers")
CUSTOMERS_DIR = _paths[0] if _paths else os.path.join(os.path.expanduser("~"), "Cowork-OS", "customers")
TODAY = date.today().isoformat()

def extract_header_field(text, field):
    """Extract a value from the bold header fields at the top of the dossier."""
    pattern = rf"\*\*{re.escape(field)}:\*\*\s*(.+)"
    m = re.search(pattern, text)
    return m.group(1).strip() if m else "—"

def extract_section(text, heading, stop_headings=None):
    """
    Extract content under a markdown heading (## or ###).
    Stops at the next heading of the same or higher level, or at any stop_headings.
    """
    # Match ## or ### heading — use {{}} to escape braces in f-string
    pattern = r"^#{1,3} " + re.escape(heading) + r"\s*$"
    m = re.search(pattern, text, re.MULTILINE)
    if not m:
        return ""
    start = m.end()
    # Find next heading at same or higher level
    level = len(re.match(r"(#+)", m.group(0)).group(1))
    next_heading = re.search(r"^#{1," + str(level) + r"} ", text[start:], re.MULTILINE)
    if next_heading:
        end = start + next_heading.start()
    else:
        end = len(text)
    return text[start:end].strip()

def extract_contacts(text):
    """Extract key contacts table rows."""
    section = extract_section(text, "Key Contacts")
    rows = []
    for line in section.split("\n"):
        # Table data rows (not header or separator)
        if line.startswith("|") and not re.match(r"\|[\s\-|]+\|", line):
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) >= 3 and parts[0] and parts[0] not in ["Name", "---"]:
                name = parts[0]
                title = parts[1] if len(parts) > 1 else ""
                role = parts[3] if len(parts) > 3 else ""
                if name and "Unknown" not in name and "not yet" not in name.lower():
                    entry = f"- **{name}**"
                    if title:
                        entry += f" — {title}"
                    if role:
                        entry += f" ({role})"
                    rows.append(entry)
    return "\n".join(rows) if rows else "- Not yet captured"

def extract_onboarding_status(text):
    """Extract the structured Onboarding Status section."""
    section = extract_section(text, "Onboarding Status")
    if not section:
        return {"phase": "—", "situation": "—", "blockers": "—", "next_steps": "—"}

    phase_m = re.search(r"\*\*Current phase:\*\*\s*(.+)", section)
    phase = phase_m.group(1).strip() if phase_m else "—"

    stands_m = re.search(r"\*\*Where things stand:\*\*\s*([\s\S]+?)(?=\*\*|\Z)", section)
    situation = stands_m.group(1).strip() if stands_m else "—"

    blockers_m = re.search(r"\*\*Blockers:\*\*\s*([\s\S]+?)(?=\*\*|\Z)", section)
    blockers_raw = blockers_m.group(1).strip() if blockers_m else "—"
    # Preserve ALL blocker bullet lines — no truncation
    blockers_lines = [l for l in blockers_raw.split("\n") if l.strip() and l.strip() != "-"]
    blockers = "\n".join(blockers_lines) if blockers_lines else "None identified"

    next_m = re.search(r"\*\*Next steps:\*\*\s*([\s\S]+?)(?=\*\*|\Z)", section)
    next_raw = next_m.group(1).strip() if next_m else "—"
    next_lines = [l for l in next_raw.split("\n") if l.strip() and l.strip() != "-"]
    next_steps = "\n".join(next_lines) if next_lines else "—"

    return {
        "phase": phase,
        "situation": situation,
        "blockers": blockers,
        "next_steps": next_steps
    }


def extract_recent_activity(text):
    """Extract the most recent entry from the Interaction Log."""
    section = extract_section(text, "Interaction Log")
    if not section:
        return "—"
    # Find first ### entry (most recent — log is most-recent-first)
    m = re.search(r"^### (.+)", section, re.MULTILINE)
    if not m:
        return "—"
    entry_start = m.start()
    next_entry = re.search(r"^### ", section[m.end():], re.MULTILINE)
    entry_end = m.end() + next_entry.start() if next_entry else len(section)
    entry = section[entry_start:entry_end].strip()
    # Pull just the heading + Key takeaways (first 3 bullets max)
    heading = m.group(1).strip()
    takeaways_m = re.search(r"\*\*Key takeaways:\*\*\s*([\s\S]+?)(?=\*\*|\Z)", entry)
    if takeaways_m:
        bullets = re.findall(r"- (.+)", takeaways_m.group(1))[:3]
        bullets_str = "\n".join(f"  - {b}" for b in bullets)
        return f"**{heading}**\n{bullets_str}" if bullets else f"**{heading}**"
    return f"**{heading}**"


def extract_blockers_with_context(text):
    """
    Build enriched blocker entries by cross-referencing the Onboarding Status blockers
    with matching Watch Items (which often have more context + resolution notes).
    Returns a list of enriched blocker strings.
    """
    status = extract_onboarding_status(text)
    blockers_raw = status["blockers"]
    if blockers_raw in ("—", "None identified"):
        return blockers_raw

    watch_section = extract_section(text, "Watch Items / Flags")
    watch_items = {}
    if watch_section:
        # Watch items use **Bold title** — description format
        for item in re.finditer(r"\*\*([^*]+)\*\*\s*[—–-]\s*([^\n]+(?:\n(?![-*#\*]).*)*)", watch_section):
            key = item.group(1).strip().lower()
            watch_items[key] = item.group(0).strip()

    enriched = []
    for line in blockers_raw.split("\n"):
        if not line.strip():
            continue
        # Try to match this blocker to a watch item for richer context
        line_lower = line.lower()
        matched_watch = None
        for wkey, wval in watch_items.items():
            # Match on shared keywords (3+ chars)
            wwords = set(w for w in wkey.split() if len(w) > 3)
            lwords = set(w for w in re.findall(r'\w+', line_lower) if len(w) > 3)
            if wwords & lwords:
                matched_watch = wval
                break
        if matched_watch:
            # Use the watch item's richer description, trimmed
            if len(matched_watch) > 200:
                matched_watch = matched_watch[:197] + "..."
            enriched.append(matched_watch)
        else:
            enriched.append(line)

    return "\n\n".join(enriched) if enriched else "None identified"

def extract_jareds_open_items(text):
    """Extract open (unchecked) items from Open Items > Jared's to-do."""
    section = extract_section(text, "Open Items")
    if not section:
        return "None"
    # Get everything before "Watching" subsection
    jared_section = re.split(r"\*\*Watching", section)[0]
    items = re.findall(r"- \[ \] (.+)", jared_section)
    return "\n".join(f"- [ ] {i}" for i in items) if items else "None"

def extract_watch_items(text):
    """Extract Watch Items / Flags section."""
    section = extract_section(text, "Watch Items / Flags")
    if not section:
        return "None"
    lines = [l for l in section.split("\n") if l.strip() and l.strip() != "-"]
    # Truncate long entries to keep CLAUDE.md tight
    condensed = []
    for line in lines[:5]:  # max 5 watch items
        if len(line) > 120:
            line = line[:117] + "..."
        condensed.append(line)
    return "\n".join(condensed) if condensed else "None"

def extract_comm_notes(text):
    """Extract 2-3 bullets from Communication Notes."""
    section = extract_section(text, "Communication Notes")
    if not section or "not yet captured" in section.lower():
        return "Not yet captured"
    lands_m = re.search(r"\*\*What lands well:\*\*\s*([\s\S]+?)(?=\*\*What to avoid|\Z)", section)
    avoid_m = re.search(r"\*\*What to avoid[^:]*:\*\*\s*([\s\S]+)", section)
    notes = []
    if lands_m:
        items = re.findall(r"- (.+)", lands_m.group(1))
        for item in items[:2]:
            if "not yet captured" not in item.lower():
                notes.append(f"✅ {item}")
    if avoid_m:
        items = re.findall(r"- (.+)", avoid_m.group(1))
        for item in items[:2]:
            if "not yet captured" not in item.lower():
                notes.append(f"⚠️ {item}")
    return "\n".join(f"- {n}" for n in notes) if notes else "Not yet captured"

def get_csm(text):
    """Try to find CSM from contacts or account status."""
    # Look for CSM in contacts table
    m = re.search(r"\|\s*([^|]+)\s*\|\s*[^|]*CSM[^|]*\|", text, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    # Look in account status for CS handoff reference
    status = extract_header_field(text, "Account Status")
    if "Grace" in status:
        return "Grace Boboye"
    if "Barb" in status or "Barbara" in status:
        return "Barb Watkins"
    return "—"

def generate_claude_md(customer_name, dossier_text, data_depth):
    """Generate the CLAUDE.md content for a customer folder."""
    status = extract_header_field(dossier_text, "Account Status")
    health = extract_header_field(dossier_text, "Onboarding Health")
    products = extract_header_field(dossier_text, "Product(s)")
    last_contact = extract_header_field(dossier_text, "Last Contact")
    flagged = extract_header_field(dossier_text, "Flagged")
    contract_renewal = extract_header_field(dossier_text, "Contract Renewal")
    si_partner = extract_header_field(dossier_text, "SI Partner(s)")
    csm = get_csm(dossier_text)

    contacts = extract_contacts(dossier_text)
    onboarding = extract_onboarding_status(dossier_text)
    blockers_enriched = extract_blockers_with_context(dossier_text)
    open_items = extract_jareds_open_items(dossier_text)
    recent_activity = extract_recent_activity(dossier_text)
    comm_notes = extract_comm_notes(dossier_text)

    depth_note = ""
    if "⚪" in data_depth or "Sparse" in data_depth:
        depth_note = "\n> ⚪ **Sparse dossier** — limited context available. Check Fathom and Gmail before any customer work.\n"

    content = f"""# {customer_name} — Active Context

> Auto-derived from dossier — last refreshed {TODAY}. Do not edit manually.
> To update: revise the dossier first, then re-run `generate_customer_claude.py` or ask Claude to refresh this file.
{depth_note}
## At a Glance

| Field | Value |
|-------|-------|
| Status | {status} |
| Health | {health} |
| Phase | {onboarding['phase']} |
| Products | {products} |
| Flagged | {flagged} |
| Last Contact | {last_contact} |
| Contract Renewal | {contract_renewal} |
| SI Partner | {si_partner} |
| CSM | {csm} |

## Primary Contacts

{contacts}

## Current Situation

{onboarding['situation']}

## Active Blockers

> Each blocker includes context and resolution path where available.

{blockers_enriched}

## Next Steps (Resolution Path)

{onboarding['next_steps']}

## Open Items

{open_items}

## Recent Activity

{recent_activity}

## Communication Notes

{comm_notes}
"""
    return content.strip() + "\n"


def refresh_one(folder_name):
    """Regenerate CLAUDE.md for a single customer folder (by kebab-case folder name)."""
    folder_path = os.path.join(CUSTOMERS_DIR, folder_name)
    dossier_path = os.path.join(folder_path, f"{folder_name}.md")

    if not os.path.exists(dossier_path):
        print(f"⚠️  No dossier found at {dossier_path}")
        return False

    with open(dossier_path, "r", encoding="utf-8") as f:
        dossier_text = f.read()

    name_m = re.match(r"# (.+)", dossier_text)
    customer_name = name_m.group(1).strip() if name_m else folder_name.replace("-", " ").title()
    data_depth = extract_header_field(dossier_text, "Data Depth")

    claude_md_content = generate_claude_md(customer_name, dossier_text, data_depth)
    claude_md_path = os.path.join(folder_path, "CLAUDE.md")

    with open(claude_md_path, "w", encoding="utf-8") as f:
        f.write(claude_md_content)

    print(f"✅ Refreshed CLAUDE.md for {customer_name}")
    return True


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate customer CLAUDE.md files from dossiers.")
    parser.add_argument("--customer", metavar="FOLDER", help="Regenerate only this customer (kebab-case folder name)")
    args = parser.parse_args()

    if args.customer:
        refresh_one(args.customer)
        return

    customers_path = CUSTOMERS_DIR
    folders = [
        f for f in os.listdir(customers_path)
        if os.path.isdir(os.path.join(customers_path, f))
        and not f.startswith("_") and f != "CLAUDE.md" and f != "MEMORY.md" and f != "README.md"
    ]

    generated = []
    skipped = []

    for folder in sorted(folders):
        folder_path = os.path.join(customers_path, folder)
        dossier_path = os.path.join(folder_path, f"{folder}.md")

        if not os.path.exists(dossier_path):
            skipped.append(f"{folder} — no dossier found")
            continue

        with open(dossier_path, "r", encoding="utf-8") as f:
            dossier_text = f.read()

        name_m = re.match(r"# (.+)", dossier_text)
        customer_name = name_m.group(1).strip() if name_m else folder.replace("-", " ").title()
        data_depth = extract_header_field(dossier_text, "Data Depth")

        claude_md_content = generate_claude_md(customer_name, dossier_text, data_depth)
        claude_md_path = os.path.join(folder_path, "CLAUDE.md")

        with open(claude_md_path, "w", encoding="utf-8") as f:
            f.write(claude_md_content)

        generated.append(f"✅ {customer_name}")

    print(f"\n=== Customer CLAUDE.md Generation Complete ===")
    print(f"\nGenerated ({len(generated)}):")
    for g in generated:
        print(f"  {g}")
    if skipped:
        print(f"\nSkipped ({len(skipped)}):")
        for s in skipped:
            print(f"  ⚠️  {s}")


if __name__ == "__main__":
    main()
