# Subfolders — Core Infrastructure Additions

These additions promote subfolders from a utility skill to a core piece of
the portable skill operating system. Add these sections to the existing
subfolders SKILL.md.

---

## Skill Directory Creation

When creating a new skill, use the standard structure:

```
skills/<skill-name>/
├── SKILL.md                    # Main skill definition (required)
├── reference/                  # Reference documents (loaded on demand)
├── scripts/                    # Executable tools (Python, bash)
├── templates/                  # Output templates
└── examples/                   # Usage examples (optional)
```

Create only what the skill needs. Not all subdirectories are required:
- `reference/` — skill needs domain docs, product docs, or reference data
- `scripts/` — skill produces structured output benefiting from validation
- `templates/` — skill has specific output formats
- `examples/` — skill is complex enough for sample inputs/outputs

---

## Skill Split Support

When auto-research or PM recommends splitting a skill (>500 lines):

1. Create the new subdirectories (reference/, scripts/, templates/)
2. PM verifies the split plan before execution (Tier 2)
3. Content moves from monolithic SKILL.md into new files
4. SKILL.md updated to reference the new files
5. **Awareness propagation runs** (see below)

---

## Output Directory Creation

Runtime output directories:

```
outputs/
├── auto-research/<skill-name>/    # Per-skill eval data
├── auto-research/_sweep/          # Sweep-level data
├── health-ledger/                 # PM quality observations
├── research/<topic-slug>/         # Research skill cached findings
├── evo-proposals/                 # Dream's EVO proposals
└── integration-tests/             # Cross-skill test results
```

---

## Awareness Propagation

**Rule: No orphan folders.** Every new directory must be announced to every
file that maintains a map of the workspace.

### Always Updated

| File | Update |
|------|--------|
| Root `CLAUDE.md` | Add new directory to workspace structure map |
| `ACTIVITY-LOG.md` | Record structural change with timestamp and reason |

### Updated When Applicable

| File | When |
|------|------|
| Root `MEMORY.md` | New folder represents a new knowledge area |
| Subfolder `MEMORY.md` | New directory inside existing subfolder — add cross-reference |
| PM routing table / skill catalog | New skill folder created |
| Dream's file scan targets | New folder contains files dream should process |
| Memory-create's target list | New folder is valid target for memory writes |

### Propagation Sequence

Every time subfolders runs:

```
1. Create the directory/directories
2. Read the propagation checklist
3. For each applicable file:
   a. Read current content
   b. Add the new directory reference
   c. Write updated content
4. Verify all references are consistent
5. Return SKILL RESULT confirming what was created AND what was updated
```

### Propagation Checklist (verify before marking complete)

- [ ] Root CLAUDE.md structure map updated
- [ ] ACTIVITY-LOG.md entry written
- [ ] All relevant MEMORY.md files updated
- [ ] PM routing table updated (if new skill)
- [ ] Dream scan targets updated (if new data folder)
- [ ] Memory-create targets updated (if new memory-eligible folder)
- [ ] No workspace file references an outdated directory structure

---

## SKILL RESULT Format

```
## SKILL RESULT: subfolders
Timestamp: [ISO 8601]
Customer: None
Actions taken: Created [N] directories. Updated [N] workspace files.

Findings:

  === DIRECTORIES CREATED ===
  | Path | Reason | Requested By |
  |------|--------|-------------|
  | skills/email-templates/scripts/ | Validation script needed | auto-research |
  | outputs/research/calendar-mcp/ | Research cache directory | research |

  === FILES UPDATED (Awareness Propagation) ===
  | File | Change |
  |------|--------|
  | CLAUDE.md | Added new paths to structure map |
  | ACTIVITY-LOG.md | Logged structural change |
  | skills/email-templates/SKILL.md | Added reference to scripts/ |

  === PROPAGATION VERIFICATION ===
  All [N] applicable files updated. No orphan references.

Confidence: High
Gaps/failures: None
Suggested next: [skill that requested the directory can now proceed]
Flags for Jared: None (structural change pre-approved as Tier 2)
```

---

## Who Invokes Subfolders

| Core Skill | Why |
|-----------|-----|
| **PM** | New output directories, structural recommendations |
| **Auto-research** | Skill splits, reference/scripts/templates directories |
| **Brainstorming** | New project subfolders during design phase |
| **Research** | Cache directories for research outputs |
| **Skill-creator** | New skill directory structure |

All structural changes require user approval (Tier 2). The system proposes,
the user decides, subfolders executes, PM propagates awareness.
