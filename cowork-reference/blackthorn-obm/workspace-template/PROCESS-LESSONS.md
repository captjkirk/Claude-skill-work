# Process Lessons

_Maintained by the process-mistakes skill. Read at the start of any workflow involving COM records, skill updates, Gmail drafting, kickoff deck builds, or packaging._

---

### Learning Hub Links — Always Grep the Bundled CSV First
**Date logged:** 2026-03-24 (Jared Kirk — added to plugin 2026-03-25)
**Affected workflows:** Any email or resource that includes Blackthorn Learning Hub links
**What went wrong:** Used web search to hunt for community.blackthorn.io module URLs when a complete catalog already exists locally.
**Correct approach:** Before searching the web for any Learning Hub URL, grep `reference/BlackthornLearningHubContent.csv` by topic keyword. The CSV has content names and direct shareable links for every published module. Find it dynamically: `find /sessions -path "*/mnt/*/reference/BlackthornLearningHubContent.csv" 2>/dev/null | head -1`

---

### Gmail Drafts — Always Preview in Chat Before Creating
**Date logged:** 2026-03-23 (Jared Kirk — added to plugin 2026-03-25)
**Affected workflows:** All email drafting — email-templates, day-prep-recap follow-ups, customer replies, any customer email
**What went wrong:** Draft was created in Gmail before the user had a chance to review or approve the content. No `gmail_delete_draft` tool exists, so fixing a bad draft requires the user to manually delete it.
**Correct approach:** Always present the full email — subject, recipients, body — in the conversation first. Only call `gmail_create_draft` after explicit user approval (via AskUserQuestion or typed confirmation). No exceptions, even for short or obvious emails.

---

### Use AskUserQuestion for Every Approval and Directional Choice
**Date logged:** 2026-03-23 (Jared Kirk — added to plugin 2026-03-25)
**Affected workflows:** All workflows — any time a decision, approval, or yes/no is needed
**What went wrong:** Asked for feedback or approval as plain prose, requiring the user to type a response when a structured pick would be faster and clearer.
**Correct approach:** Whenever asking the user to approve something, choose between options, or confirm a direction — always use `AskUserQuestion` with a pick list. Applies across the board: email approvals, next-step choices, confirmation prompts, "does this look right?" moments.

---

### PPTX Template — Zero Out srcRect Crop Values After Headshot Swaps
**Date logged:** 2026-03-24 (Jared Kirk — added to plugin 2026-03-25)
**Affected workflows:** kickoff-deck build, any workflow that swaps images in a PPTX
**What went wrong:** The Blackthorn onboarding template has `<a:srcRect>` values in slide3.xml calibrated for the original placeholder headshots. Swapping in new photos without clearing these offsets causes zoomed-in or miscentered results that are invisible in the XML unless explicitly inspected.
**Correct approach:** After any headshot swap, zero out all srcRect values for the affected pic elements: `<a:srcRect b="0" l="0" r="0" t="0"/>`. The `build_deck.py` script does this automatically for rId3, rId5, and rId7 — do not bypass that script for manual edits.

---

### Google Drive Upload via Chrome File_Upload Tool Fails
**Date logged:** 2026-03-24 (Jared Kirk — added to plugin 2026-03-25)
**Affected workflows:** kickoff-deck skill, any workflow uploading files to Drive via Chrome automation
**What went wrong:** `mcp__Claude_in_Chrome__file_upload` returns `{"code":-32000,"message":"Not allowed"}` for all local file paths. The Chrome extension blocks local filesystem access for uploads.
**Correct approach:** Upload to Drive manually. Provide the user with a `computer://` link to the file and direct them to use New → File upload in Drive. After upload, open in Slides and do File > Save as Google Slides to convert to native format and eliminate rendering skew.

---

### Skill Updates — Direct Writes to .skills/ Always Fail
**Date logged:** 2026-03-21 (Jared Kirk — added to plugin 2026-03-25)
**Affected workflows:** skill-creator, any skill patching or update task
**What went wrong:** Attempted direct edits to the `.skills/` runtime directory via `sed -i`, `cp`, or Python file writes. The directory is read-only — all such attempts fail silently or with a permissions error.
**Correct approach:**
1. `cp -r /sessions/*/mnt/.skills/skills/<skill-name> /tmp/<unique-dir>/`
2. `chmod -R u+w /tmp/<unique-dir>/`
3. Edit files from `/tmp/<unique-dir>/`
4. Package: `cd /sessions/*/mnt/.skills/skills/skill-creator && python3 -m scripts.package_skill /tmp/<unique-dir> /tmp/<output-dir>`
5. Copy `.skill` to `outputs/skill-updates/` and present via `present_files`
Note: Use a fresh unique `/tmp/` subdirectory each time — do not reuse a previously-used path.

---

### Product Feedback — Validate Before Flagging as New PFQE Candidate
**Date logged:** 2026-03-23 (Jared Kirk — added to plugin 2026-03-25)
**Affected workflows:** day-prep-recap, com-update, any workflow surfacing product feedback signals
**What went wrong:** Flagged a product issue as "worth posting to PFQE" without first checking whether a post had already been made on that topic.
**Correct approach:** Before surfacing any product feedback as a new PFQE candidate, search #product-feedback-questions-everything in Slack for the topic. Only flag as "worth posting" if no existing post covers it. Log when a post is made in the customer dossier to prevent re-flagging.

---

### Skill Description Length — Must Be Under 1024 Characters
**Date logged:** 2026-03-23 (Jared Kirk — added to plugin 2026-03-25)
**Affected workflows:** skill-creator, any skill packaging task
**What went wrong:** Packager rejected a skill with a description over 1024 characters.
**Correct approach:** Before packaging, check description length:
```python
python3 -c "
import re
f = open('/tmp/.../SKILL.md').read()
m = re.search(r'description: >(.*?)---', f, re.DOTALL)
print(len(' '.join(m.group(1).strip().split())))
"
```
Must be under 1024 characters. Trim if over.
