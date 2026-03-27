# Customers — Operative Context

This folder contains one subfolder per customer account. Each subfolder has:

- `CLAUDE.md` — compact operative context (current phase, contacts, blockers, next steps). Read this first.
- `<customer-name>.md` — full dossier (source of truth, full history)
- `meetings/` — Fathom call cache (YYYY-MM-DD-title.md)

## How to Use

Before any customer-facing task, load context in this order:
1. `customers/<name>/CLAUDE.md` (fast path — covers 80% of what you need)
2. `customers/<name>/<name>.md` (full depth when needed)
3. `customers/<name>/meetings/` (Fathom cache — check before calling API)

## Creating a New Dossier

Copy `_TEMPLATE.md` to `customers/<kebab-name>/<kebab-name>.md` and fill in what you know.
After any update, regenerate `CLAUDE.md`:

```bash
python3 $(find /sessions -path "*/mnt/*/customers/generate_customer_claude.py" 2>/dev/null | head -1) --customer <kebab-folder-name>
```
