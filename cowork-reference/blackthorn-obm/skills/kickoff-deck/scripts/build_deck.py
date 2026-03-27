#!/usr/bin/env python3
"""
build_deck.py — Builds a customized Blackthorn onboarding kickoff deck.

Usage:
    python3 build_deck.py \
        --customer "Parker Institute" \
        --csm "Ellie Silverstein" \
        --ae "Michael Disraeli" \
        --date "March 24, 2026" \
        --workspace /path/to/Cowork-OS \
        --output /path/to/output.pptx

Slide 3 layout (3-person, evenly spaced):
  - Left  (CSM): role sp=220, name sp=223, photo pic=226 rId=rId3 -> image11.png
  - Center (OBM = Jared Kirk): role sp=231, name sp=232, photo pic=233 rId=rId7 -> image8.png
  - Right  (AE): role sp=222, name sp=225, photo pic=228 rId=rId5 -> image7.jpg
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from PIL import Image
    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False

try:
    import cv2
    import numpy as np
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False


def find_headshot(workspace: Path, person_name: str) -> Path | None:
    """Find a headshot file by person name (firstname-lastname, case-insensitive)."""
    parts = person_name.strip().lower().split()
    if len(parts) < 2:
        return None
    slug = f"{parts[0]}-{parts[-1]}"
    headshots_dir = workspace / "reference" / "team-headshots"
    for f in headshots_dir.iterdir():
        if f.stem.lower() == slug:
            return f
    return None


def _detect_face(img_path: Path):
    """Return (fx, fy, fw, fh) of the largest detected face, or None."""
    if not HAS_CV2:
        return None
    img_cv = cv2.imread(str(img_path))
    if img_cv is None:
        return None
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if not len(faces):
        faces = cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3, minSize=(20, 20))
    if not len(faces):
        return None
    return max(faces, key=lambda f: f[2] * f[3])


def copy_headshot(src: Path, dest: Path):
    """Copy a headshot to dest with smart face-centered cropping.

    Uses OpenCV face detection to determine the right center point:
      - Headshot (face > 20% of image height): center on nose
      - Full body (face <= 20% of image height): center on belly button
      - No face detected: center of image

    Crops a square around that center, then saves with format conversion if needed.
    The template srcRect offsets are cleared separately in slide XML — this function
    only handles the image file itself.
    """
    if not HAS_PILLOW:
        shutil.copy2(src, dest)
        return

    img = Image.open(src).convert("RGB")
    w, h = img.size
    size = min(w, h)

    face = _detect_face(src)
    if face is not None:
        fx, fy, fw, fh = face
        cx = fx + fw // 2
        if fh / h > 0.20:
            # Headshot — center on nose (middle of face bbox)
            cy = fy + fh // 2
        else:
            # Full body — center on belly button (~2.5 face-heights below chin)
            cy = fy + fh + int(2.5 * fh)
    else:
        cx, cy = w // 2, h // 2

    x0 = max(0, min(cx - size // 2, w - size))
    y0 = max(0, min(cy - size // 2, h - size))
    img = img.crop((x0, y0, x0 + size, y0 + size))

    dest_ext = dest.suffix.lower()
    fmt_map = {".jpg": "JPEG", ".jpeg": "JPEG", ".png": "PNG"}
    fmt = fmt_map.get(dest_ext, dest_ext.lstrip(".").upper())
    img.save(dest, format=fmt, quality=95)



def _para(text: str, spc_before: int = 600, spc_after: int = 600) -> str:
    """Build a centered, no-bullet paragraph XML node at 1000pt with Manrope."""
    return (
        f'<a:p><a:pPr indent="0" lvl="0" marL="0" rtl="0" algn="ctr">'
        f'<a:spcBef><a:spcPts val="{spc_before}"/></a:spcBef>'
        f'<a:spcAft><a:spcPts val="{spc_after}"/></a:spcAft>'
        f'<a:buNone/></a:pPr>'
        f'<a:r><a:rPr lang="en" sz="1000"/><a:t>{text}</a:t></a:r>'
        f'<a:endParaRPr sz="1000"/></a:p>'
    )


def patch_slide4(slide_xml: str, args) -> str:
    """Populate slide 4 (Your License) with customer-specific values.

    Template placeholders (from Blackthorn-Onboarding-Intro-Template.pptx):
      - "Your License (Template)"            → "Your License"
      - "Registration-based"                 → args.license_type
      - Entitlements block (Events/Payments + Messaging paragraphs)
                                             → dynamically built per purchased app
                                               (Events, Payments, Messaging — only if arg provided)
      - "Unlimited"                          → blended: "X Full Users / Y Light Users"; else args.users
      - "Blackthorn Premium Support"         → args.support
    """
    s = slide_xml

    # 1. Strip "(Template)" from title
    s = s.replace("Your License (Template)", "Your License")

    # 2. License type
    s = s.replace("Registration-based", args.license_type)

    # 3. Entitlements box — replace the ENTIRE two-paragraph template block with
    #    one paragraph per purchased app (Events, Payments, Messaging).
    #    Any app whose arg is omitted is excluded entirely — no "N/A" rows.
    #
    #    Template block being replaced (exact strings from template XML):
    #      <a:p>...<a:t>Events/Payments: 20k Free &amp; Paid registrations</a:t>...</a:p>
    #      <a:p>...<a:t>Messaging: 1,000 messages &amp; 1 phone number</a:t>...</a:p>
    #
    #    Note: in the template, the Events/Payments paragraph has spcAft=0 (tight spacing
    #    to the next line) while the Messaging paragraph has spcAft=600 (bottom padding).
    #    We replicate that pattern: all-but-last have spcAft=0, last has spcAft=600.

    TEMPLATE_ENTITLEMENTS = (
        '<a:p><a:pPr indent="0" lvl="0" marL="0" rtl="0" algn="ctr">'
        '<a:spcBef><a:spcPts val="600"/></a:spcBef>'
        '<a:spcAft><a:spcPts val="0"/></a:spcAft>'
        '<a:buNone/></a:pPr>'
        '<a:r><a:rPr lang="en" sz="1000"/>'
        '<a:t>Events/Payments: 20k Free &amp; Paid registrations</a:t></a:r>'
        '<a:endParaRPr sz="1000"/></a:p>'
        '<a:p><a:pPr indent="0" lvl="0" marL="0" rtl="0" algn="ctr">'
        '<a:spcBef><a:spcPts val="600"/></a:spcBef>'
        '<a:spcAft><a:spcPts val="600"/></a:spcAft>'
        '<a:buNone/></a:pPr>'
        '<a:r><a:rPr lang="en" sz="1000"/>'
        '<a:t>Messaging: 1,000 messages &amp; 1 phone number</a:t></a:r>'
        '<a:endParaRPr sz="1000"/></a:p>'
    )

    app_lines = []
    if args.events:
        app_lines.append(args.events.replace("&", "&amp;"))
    if args.payments:
        app_lines.append(args.payments.replace("&", "&amp;"))
    if args.messaging:
        app_lines.append(args.messaging.replace("&", "&amp;"))

    if app_lines:
        new_entitlements = ""
        for i, line in enumerate(app_lines):
            is_last = (i == len(app_lines) - 1)
            new_entitlements += _para(line, spc_before=600, spc_after=600 if is_last else 0)
        if TEMPLATE_ENTITLEMENTS in s:
            s = s.replace(TEMPLATE_ENTITLEMENTS, new_entitlements)
        else:
            # Fallback: replace individual text nodes
            s = s.replace(
                "Events/Payments: 20k Free &amp; Paid registrations",
                app_lines[0] if app_lines else "",
            )

    # 4. Users box
    # Template has a single paragraph: <a:t>Unlimited</a:t>
    # The surrounding paragraph block is what we replace.
    old_users_para = (
        '<a:p><a:pPr indent="0" lvl="0" marL="0" rtl="0" algn="ctr">'
        '<a:spcBef><a:spcPts val="600"/></a:spcBef>'
        '<a:spcAft><a:spcPts val="600"/></a:spcAft>'
        '<a:buNone/></a:pPr>'
        '<a:r><a:rPr lang="en" sz="1000"/><a:t>Unlimited</a:t></a:r>'
        '<a:endParaRPr sz="1000"/></a:p>'
    )
    if args.full_users is not None and args.light_users is not None:
        new_users = (
            _para(f"{args.full_users} Full Users", spc_before=400, spc_after=0)
            + _para(f"{args.light_users} Light Users", spc_before=0, spc_after=400)
        )
    else:
        new_users = _para(args.users or "Unlimited")

    if old_users_para in s:
        s = s.replace(old_users_para, new_users)
    else:
        # Fallback: plain text replace
        s = s.replace("<a:t>Unlimited</a:t>", f"<a:t>{args.users or 'Unlimited'}</a:t>")

    # 5. Support tier
    s = s.replace("Blackthorn Premium Support", args.support)

    return s


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--customer",      required=True,  help="Customer/company name")
    parser.add_argument("--csm",           required=True,  help="CSM full name")
    parser.add_argument("--ae",            required=True,  help="AE full name")
    parser.add_argument("--obm",           required=True,  help="OBM full name (current user)")
    parser.add_argument("--date",          required=True,  help="Date string e.g. 'March 24, 2026'")
    parser.add_argument("--workspace",     required=True,  help="Path to Cowork-OS workspace")
    parser.add_argument("--output",        required=True,  help="Output .pptx path")
    # Slide 4 — license data (provide args only for purchased apps; omitted apps are excluded entirely)
    parser.add_argument("--license-type",  default="Registration-based",
                        help="License type label (default: Registration-based)")
    parser.add_argument("--events",        default=None,
                        help="Events entitlement text, e.g. '1,100 registrations/year'. "
                             "Omit if customer did not purchase Events.")
    parser.add_argument("--payments",      default=None,
                        help="Payments entitlement text, e.g. 'PayLink included'. "
                             "Omit if customer did not purchase Payments.")
    parser.add_argument("--messaging",     default=None,
                        help="Messaging entitlement text, e.g. '10,000 messages/month, 1 phone number'. "
                             "Omit if customer did not purchase Messaging.")
    parser.add_argument("--full-users",    type=int, default=None,
                        help="Number of full users (blended license). Triggers two-line user display.")
    parser.add_argument("--light-users",   type=int, default=None,
                        help="Number of light users (blended license). Must be paired with --full-users.")
    parser.add_argument("--users",         default=None,
                        help="Flat user count/label for non-blended licenses (e.g. 'Unlimited').")
    parser.add_argument("--support",       default="Blackthorn Premium Support",
                        help="Support tier label (default: Blackthorn Premium Support)")
    args = parser.parse_args()

    # Validate blended user args
    if (args.full_users is None) != (args.light_users is None):
        parser.error("--full-users and --light-users must both be provided together.")
    if args.full_users is not None and args.users is not None:
        parser.error("Provide either --full-users/--light-users (blended) or --users (flat), not both.")

    workspace = Path(args.workspace)
    baseline = workspace / "reference" / "kickoff-deck-template" / "Blackthorn-Onboarding-Intro-Template.pptx"
    headshots_dir = workspace / "reference" / "team-headshots"
    scripts_dir = Path(__file__).parent

    # --- Headshot lookup ---
    people = {
        "CSM": args.csm,
        "OBM": args.obm,
        "AE": args.ae,
    }
    missing = []
    headshot_paths = {}
    for role, name in people.items():
        path = find_headshot(workspace, name)
        if path is None:
            missing.append(f"{name} ({role})")
        else:
            headshot_paths[role] = path

    if missing:
        print("ERROR: Missing headshots for:")
        for m in missing:
            print(f"  - {m}")
        print(f"\nAdd headshots to: {headshots_dir}")
        print("Filename format: firstname-lastname.ext (e.g., john-smith.jpg)")
        sys.exit(2)

    # --- Set up working directory ---
    with tempfile.TemporaryDirectory(prefix="kickoff-deck-") as tmpdir:
        tmpdir = Path(tmpdir)
        working_pptx = tmpdir / "deck.pptx"
        unpacked = tmpdir / "unpacked"

        shutil.copy2(baseline, working_pptx)

        # Find unpack/pack scripts (relative to this skill's scripts dir, or from .skills)
        unpack_script = None
        pack_script = None
        for search_root in [scripts_dir.parent.parent, workspace.parent / ".skills" / "skills" / "pptx"]:
            u = search_root / "scripts" / "office" / "unpack.py"
            p = search_root / "scripts" / "office" / "pack.py"
            if u.exists():
                unpack_script = u
                pack_script = p
                break

        if unpack_script is None:
            # Fallback: use zipfile directly
            unpack_script = None

        if unpack_script:
            subprocess.run([sys.executable, str(unpack_script), str(working_pptx), str(unpacked)], check=True)
        else:
            import zipfile
            unpacked.mkdir()
            with zipfile.ZipFile(working_pptx, 'r') as z:
                z.extractall(unpacked)

        slides_dir = unpacked / "ppt" / "slides"
        media_dir = unpacked / "ppt" / "media"

        # --- Swap headshots ---
        # CSM: rId3 -> image11.png
        copy_headshot(headshot_paths["CSM"], media_dir / "image11.png")
        # OBM: rId7 -> image8.png
        copy_headshot(headshot_paths["OBM"], media_dir / "image8.png")
        # AE: rId5 -> image7.jpg
        copy_headshot(headshot_paths["AE"], media_dir / "image7.jpg")
        print(f"  Headshots swapped: {args.csm}, {args.obm}, {args.ae}")

        # --- Update slide 3 names ---
        # Template placeholder names (from Blackthorn-Onboarding-Intro-Template.pptx):
        #   CSM slot: "Lexi Wachtell"
        #   OBM slot: "Noah Merrikan"
        #   AE slot:  "Lauren Orscheln"
        # Simple string replace — same approach as Company Name / date, avoids
        # fragile XML regex that misfires on Google-Slides-generated XML.
        slide3_path = slides_dir / "slide3.xml"
        with open(slide3_path) as f:
            slide3 = f.read()

        slide3 = slide3.replace("Lexi Wachtell", args.csm)
        slide3 = slide3.replace("Noah Merrikan", args.obm)
        slide3 = slide3.replace("Lauren Orscheln", args.ae)

        # --- Zero out srcRect offsets for all headshot slots ---
        # The template has srcRect values calibrated for the original placeholder headshots.
        # After swapping images those offsets crop the new photos incorrectly — reset them.
        for rid in ["rId3", "rId5", "rId7"]:
            slide3 = re.sub(
                rf'(r:embed="{rid}".*?)<a:srcRect[^/]*/>',
                r'\1<a:srcRect b="0" l="0" r="0" t="0"/>',
                slide3, count=1, flags=re.DOTALL
            )

        with open(slide3_path, 'w') as f:
            f.write(slide3)
        print(f"  Slide 3 names updated, srcRect offsets cleared")

        # --- Replace placeholders on all slides ---
        for slide_file in sorted(slides_dir.glob("slide*.xml")):
            with open(slide_file) as f:
                content = f.read()

            if "Company Name" in content:
                content = content.replace("Company Name", args.customer)
                print(f"  Replaced 'Company Name' in {slide_file.name}")

            if "Month DD, YYYY" in content:
                content = content.replace("Month DD, YYYY", args.date)
                print(f"  Replaced date placeholder in {slide_file.name}")

            with open(slide_file, 'w') as f:
                f.write(content)

        # --- Populate slide 4 (license/support table) ---
        if any([args.events, args.payments, args.messaging]):
            slide4_path = slides_dir / "slide4.xml"
            with open(slide4_path) as f:
                slide4 = f.read()
            slide4 = patch_slide4(slide4, args)
            with open(slide4_path, 'w') as f:
                f.write(slide4)
            apps = [a for a in [
                f"Events({args.events})" if args.events else None,
                f"Payments({args.payments})" if args.payments else None,
                f"Messaging({args.messaging})" if args.messaging else None,
            ] if a]
            user_display = (
                f"{args.full_users} Full / {args.light_users} Light"
                if args.full_users is not None
                else (args.users or "Unlimited")
            )
            print(f"  Slide 4 populated: {args.license_type} | {', '.join(apps)} | Users: {user_display} | {args.support}")

        # --- Repack ---
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if pack_script:
            subprocess.run([sys.executable, str(pack_script), str(unpacked), str(output_path)], check=True)
        else:
            import zipfile
            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as z:
                for file in unpacked.rglob("*"):
                    if file.is_file():
                        z.write(file, file.relative_to(unpacked))

        print(f"\nDeck saved to: {output_path}")


if __name__ == "__main__":
    main()
