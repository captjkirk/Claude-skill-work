# Subfolders as Core Infrastructure — Blueprint

This is a design doc. The next Claude Code session implements these additions
to the existing subfolders skill in the live Cowork workspace.

## Sources

- [Anthropic: Don't Build Agents, Build Skills](https://youtu.be/wqH1hTkA6qg)
  — Skills can include scripts/, reference/, templates/ subdirectories.
  Progressive disclosure keeps context lean.
- [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
  — Multi-skill architecture with data/, scripts/, templates/ directories.
  Master+Overrides pattern for hierarchical customization.

## Why Subfolders Is Core

As the system grows, structure needs to grow with it:

- Auto-research may recommend splitting a skill into progressive-disclosure
  pieces (SKILL.md + reference/ + scripts/ + templates/)
- PM may recommend new output directories for research caches, health ledger
  data, or integration test results
- Research may need to cache findings
- New skills added to the workspace need proper directory structure
- Dream's EVO pass may propose new subfolder organization

Subfolders gives the system the ability to self-organize — propose and create
structure as needed, always with user approval (Tier 2).

---

## Additions to Existing Subfolders Skill

### 1. Skill Directory Creation

When a new skill is being created (by skill-creator, or manually), subfolders
can create the standard skill directory structure:

```
skills/<skill-name>/
├── SKILL.md                    # Main skill definition
├── reference/                  # Reference documents (loaded on demand)
├── scripts/                    # Executable tools (Python, bash)
├── templates/                  # Output templates (strict, medium, flexible)
└── examples/                   # Usage examples (optional)
```

Not all subdirectories are required. Create only what the skill needs:
- `reference/` — if the skill needs domain docs, product docs, or reference data
- `scripts/` — if the skill produces structured output that benefits from validation
- `templates/` — if the skill has specific output formats
- `examples/` — if the skill is complex enough to benefit from sample inputs/outputs

### 2. Skill Split Support

When auto-research or PM recommends splitting a skill that's grown too large
(>500 lines), subfolders handles the restructuring:

1. Create the new subdirectories (reference/, scripts/, templates/)
2. PM verifies the split plan before execution
3. Content is moved from the monolithic SKILL.md into the new files
4. SKILL.md is updated to reference the new files
5. **Awareness propagation runs** (see below)

### 3. Output Directory Creation

For auto-research sweeps, research caches, health ledger data, and other
runtime outputs:

```
outputs/
├── auto-research/             # Per-skill eval data
│   ├── <skill-name>/
│   └── _sweep/
├── health-ledger/             # PM quality observations
├── research/                  # Research skill cached findings
│   └── <topic-slug>/
├── evo-proposals/             # Dream's EVO proposals
└── integration-tests/         # Cross-skill test results
```

### 4. Self-Organizing Recommendations

When PM or auto-research identifies a structural need, they can recommend
a subfolder creation via the health ledger:

```json
{
  "skill": "email-templates",
  "type": "missing-resource",
  "recommendation": "Create scripts/ directory for date validation script",
  "resource_type": "script"
}
```

PM surfaces this to the user as a Tier 2 recommendation. On approval,
subfolders creates the directory and awareness propagation runs.

---

## CRITICAL: Awareness Propagation

**The rule: No orphan folders.** Every new directory must be announced to every
file that maintains a map of the workspace.

When subfolders creates a new directory, PM must update ALL of the following
(as applicable):

### Always Updated

| File | What to Update |
|------|---------------|
| Root `CLAUDE.md` | Workspace structure map — add the new directory to the tree |
| `ACTIVITY-LOG.md` | Record the structural change with timestamp and reason |

### Updated If Applicable

| File | When to Update |
|------|---------------|
| Root `MEMORY.md` | If the folder represents a new knowledge area or capability |
| Subfolder `MEMORY.md` | If the new directory is inside an existing subfolder — add cross-reference |
| PM's routing table / skill catalog | If a new skill folder was created — PM needs to know about it for routing |
| Dream's file scan targets | If the new folder contains files dream should process during nightly consolidation |
| Memory-create's target list | If the new folder should be a valid target for memory writes |

### Propagation Checklist

Before PM marks any subfolder creation as complete, it must verify:

- [ ] Root CLAUDE.md structure map updated
- [ ] ACTIVITY-LOG.md entry written
- [ ] All relevant MEMORY.md files updated with cross-references
- [ ] PM routing table updated (if new skill)
- [ ] Dream scan targets updated (if new data folder)
- [ ] Memory-create targets updated (if new memory-eligible folder)
- [ ] No other file in the workspace references a directory structure that
      is now outdated

### Propagation as a Sub-Skill

The propagation logic should be a defined step within the subfolders skill,
not ad hoc. Every time subfolders runs, it follows this sequence:

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

---

## SKILL RESULT for Subfolders (Updated)

```
## SKILL RESULT: subfolders
Timestamp: [ISO 8601]
Customer: None
Actions taken: Created [N] directories. Updated [N] workspace files.

Findings:

  === DIRECTORIES CREATED ===
  | Path | Reason | Requested By |
  |------|--------|-------------|
  | skills/email-templates/scripts/ | Auto-research recommended validation script | auto-research |
  | outputs/research/calendar-mcp/ | Research skill needs cache directory | research |

  === FILES UPDATED (Awareness Propagation) ===
  | File | Change |
  |------|--------|
  | CLAUDE.md | Added skills/email-templates/scripts/ to structure map |
  | ACTIVITY-LOG.md | Logged structural change at [timestamp] |
  | skills/email-templates/SKILL.md | Added reference to scripts/ directory |

  === PROPAGATION VERIFICATION ===
  All [N] applicable files updated. No orphan references detected.

Confidence: High
Gaps/failures: None
Suggested next: [skill that requested the directory can now proceed]
Flags for Jared: None (structural change was pre-approved as Tier 2)
```

---

## Integration with the Portable Core

| Core Skill | How It Uses Subfolders |
|-----------|----------------------|
| **PM** | Requests output directories, triggers awareness propagation |
| **Auto-research** | Requests skill splits and reference/scripts/templates directories |
| **Brainstorming** | May recommend new project subfolders during design phase |
| **Research** | Requests cache directories for research outputs |
| **Honesty protocol** | No direct interaction, but benefits from organized reference docs |

The key principle: **the system proposes structural changes (Tier 2), the user
approves, subfolders executes, PM propagates awareness.** No silent
reorganization. No orphan folders.
