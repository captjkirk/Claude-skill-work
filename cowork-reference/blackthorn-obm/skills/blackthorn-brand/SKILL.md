---
name: blackthorn-brand
description: >
  Utility skill — may be invoked directly by PM or by other skills. Apply Blackthorn's brand
  voice, visual styling, and messaging guidelines to any content — presentations, documents,
  spreadsheets, marketing copy, emails, or social posts. Use when creating or reviewing ANY content
  for Blackthorn, including: presentations (.pptx), Word documents (.docx), spreadsheets (.xlsx),
  blog posts, landing pages, emails, social media, press releases, case studies, one-pagers,
  internal decks, or any writing that should sound like Blackthorn. Invoke when user asks to "make
  it on-brand," "apply brand guidelines," "use our colors," "write in our voice," or references
  Blackthorn styling, tone, or messaging.
---

# Blackthorn Brand Skill

This skill encodes Blackthorn's complete brand system — voice, messaging, visual identity, and style rules — so that every piece of content you create sounds, reads, and looks like Blackthorn.

Use this skill in two modes:

1. **Creating new content**: Apply brand voice, messaging, colors, fonts, and formatting from the start.
2. **Reviewing existing content**: Flag anything that's off-brand and suggest specific fixes.

When this skill is used alongside a document-creation skill (pptx, docx, xlsx), apply the visual identity rules (colors, fonts, spacing) to the output file directly. When creating written content (blog posts, emails, social, etc.), apply the voice and messaging guidelines.

---

## Logo Assets

Blackthorn logo files are bundled with this skill in `assets/logos/`. Use these actual image files when creating presentations, documents, or any content that needs the Blackthorn logo — don't just describe where the logo goes, embed the real file.

Files are organized into three folders:

**PNG/** — Use for presentations (.pptx), documents (.docx), and most digital use:

| File | Description | Use For |
|------|-------------|---------|
| `PNG/Blackthorn-LogoLockup-272727.png` | Logomark + wordmark, Charcoal (#272727) | Cover slides (on Spring bg), documents, everyday use |
| `PNG/Blackthorn-LogoLockup-FFFFFF.png` | Logomark + wordmark, White (#FFFFFF) | Closing slides (on Charcoal bg), dark backgrounds |
| `PNG/Blackthorn-Logomark-272727.png` | Flower icon only, Charcoal | Small spaces, content slide footers, social avatars |
| `PNG/Blackthorn-Logomark-FFFFFF.png` | Flower icon only, White | Dark backgrounds, footers |
| `PNG/Blackthorn-Logotype-272727.png` | "Blackthorn" text only, Charcoal | Email signatures, footers, text-heavy layouts |
| `PNG/Blackthorn-Logotype-FFFFFF.png` | "Blackthorn" text only, White | Dark backgrounds |

**SVG/** — Same six logos as scalable vectors. Use when resolution independence matters (web, large-format print):

| File | Description |
|------|-------------|
| `SVG/Blackthorn-LogoLockup-272727.svg` | Logo lockup, Charcoal |
| `SVG/Blackthorn-LogoLockup-FFFFFF.svg` | Logo lockup, White |
| `SVG/Blackthorn-Logomark-272727.svg` | Logomark, Charcoal |
| `SVG/Blackthorn-Logomark-FFFFFF.svg` | Logomark, White |
| `SVG/Blackthorn-Logotype-272727.svg` | Logotype, Charcoal |
| `SVG/Blackthorn-Logotype-FFFFFF.svg` | Logotype, White |

**Color-Backgrounds/** — Logo lockup pre-placed on brand-colored backgrounds (PNG + SVG):

| File | Description | Use For |
|------|-------------|---------|
| `Color-Backgrounds/Blackthorn-LogoLockup-Charcoal.png/.svg` | Charcoal logo on Charcoal background | Dark-themed hero areas |
| `Color-Backgrounds/Blackthorn-LogoLockup-Spring.png/.svg` | Charcoal logo on Spring background | Primary brand moments, cover slides |
| `Color-Backgrounds/Blackthorn-LogoLockup-White.png/.svg` | Charcoal logo on White background | Clean, everyday brand use |

When placing logos, always check the Logo Usage rules in `references/visual-identity.md` for correct colorway pairings and clear space requirements.

---

## Brand Voice

Blackthorn's voice persona is **"Your favorite coworker"** — the expert who knows the system inside and out, makes things happen fast, and earned their reputation through results rather than bragging. Smart, seasoned, and dedicated to helping users create events that people enjoy and that their businesses can learn from.

### Voice Attributes

Apply all five of these consistently:

**Friendly** — Approachable and easygoing. Never condescending, never cold. Put people at ease without sounding flippant.

**Natural** — Communicate like real people. Plain language, active voice, no filler, no jargon, no corporate cliches.

**Clear** — Get to the point. Make complexity understandable without overexplaining or dumbing down.

**Supportive** — Show up ready to collaborate. Anticipate needs, offer guidance, never make people feel bad for not knowing something.

**Fresh** — Professional but not stiff. Even when the subject is technical or dry, find ways to make it engaging and relevant.

### Competitive Voice Positioning

Blackthorn aims to sound distinct from competitors. For context:

| Competitor | Their tone | Blackthorn's contrast |
|-----------|-----------|----------------------|
| Cvent | Dry | Friendly |
| Eventspark | Cheesy | Natural |
| Swoogo | Pretentious | Clear |
| Eventbrite | Aggressive | Supportive |
| Fonteva | Boring | Fresh |

---

## Tone Rules

These rules ensure writing sounds like Blackthorn regardless of who's writing it.

**Do:**
- Use contractions (we'll, haven't, won't) — they make writing feel less uptight.
- Break things up with short paragraphs, bullet points, and clear headings to keep info scannable.
- Read it out loud. If it sounds awkward or robotic, revise for a conversational rhythm.

**Don't:**
- Be too casual. No puns, sarcasm, or pop culture references — Blackthorn is a global company with a diverse user base, so keep things accessible to everyone.
- Use jargon. Use simple, clear phrases a layperson can understand. If a niche term or acronym is unavoidable, define it on first reference.
- Rely on buzzwords, empty cliches, or hyperbole. Stick to concrete facts, tangible benefits, and outcomes rooted in reality.
- Overuse exclamation points. Limit them to direct customer interactions (like "Thank you!" in an email). Never scatter them across marketing pages.

---

## Words and Phrases to Avoid

These are overused in tech and often cliche. Never use them in Blackthorn content:

- Seamless
- Harness the power
- Streamline
- Transform
- Simplify
- Save time and money
- Integration (Blackthorn doesn't integrate with Salesforce — it's native to it)
- Alpha, Beta, MVP (use "limited availability" instead for pre-GA products)

---

## Style Rules

### Text Formatting

| Element | Rule | Example |
|---------|------|---------|
| Headlines | Sentence case. No end punctuation unless multi-sentence. No exclamations. Avoid questions except in FAQ sections. | "Powering events with your data" |
| Eyebrow headlines | Title case. No end punctuation. No exclamations or questions. | "Event Management Software" |
| Subheadlines | Sentence case. Complete sentences with end punctuation. | "Blackthorn turns your Salesforce CRM into event registration and management software." |
| Bulleted lists | Minimum three items. Consistent phrasing, formatting, and punctuation across items. Default to sentence case. Introductory text needs end punctuation. | See references/messaging.md for examples |

### Numbers and Punctuation

- **Oxford comma**: Always use it. "plan, manage, and measure events"
- **Numbers**: Spell out cardinal numbers and ordinals under 10 (one, two, first, second). Use numerals for 10+. Always use numerals in headlines and email subject lines.
- **Salesforce name**: Use "Salesforce" when referring to the company. Add ® when describing a specific Salesforce product or solution (e.g., "Salesforce® CRM"). Never use "Salesforce, Inc." — just "Salesforce."

---

## Messaging Quick Reference

Use these when writing about Blackthorn. For the full messaging architecture (value props, personas, company descriptions at various lengths), read `references/messaging.md`.

**One-sentence description**: Blackthorn turns any organization's Salesforce® CRM into event planning software powered by their connected data.

**Tagline**: Your events. Your data. All in Salesforce.

**Mission**: Blackthorn enables organizations to unlock the full potential of their Salesforce data to plan, manage, and measure events.

**Products**: Blackthorn Events, Blackthorn Payments, Blackthorn Messaging, Blackthorn Compliance (limited availability).

**Core value props** (use these as the backbone for any persuasive content):
1. Built specifically for Salesforce — no tricky, flimsy integrations
2. All events and business data connected in one place — no messy imports or data silos
3. Better attendee experiences through personalization, automations, and digital solutions
4. Richer analytics to prove event ROI in context of the full customer journey
5. Flexible for all kinds of organizations, from tiny nonprofits to global corporations
6. Maximizes the value of an org's existing Salesforce investment (including Agentforce)
7. Works alongside popular tools like Zoom, Stripe, and Sendgrid

**Key persona**: Jamie, The Event Planner — works at a medium-sized nonprofit, needs to plan and manage events in one place without moving data between tools or dealing with confusing integrations. For full persona details, read `references/messaging.md`.

---

## Visual Identity Quick Reference

For the complete visual specs (logo usage rules, gradient definitions, design elements, typesetting specs), read `references/visual-identity.md`.

### Color Palette

**Core Colors:**

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Spring | #34FF85 | 52, 225, 153 | Primary brand color. Use for hero areas, cover slides, branded banners. |
| Charcoal | #272727 | 39, 39, 39 | Primary text color and dark backgrounds. |
| White | #FFFFFF | 255, 255, 255 | Backgrounds, reversed text on dark surfaces. |

**Neutral Colors:**

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Slate | #475258 | 71, 82, 88 | Outlines, partner graphics. |
| Silver | #BCCED3 | 188, 206, 211 | Backgrounds for content sections. |
| Lavender | #EBEBFF | 235, 235, 255 | Light backgrounds, soft accent. |

**Functional Colors:**

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Violet | #7360FF | 115, 96, 255 | Accented hierarchy, UI highlights, marketing accents. |
| Hot Red | #FF5C5C | 255, 92, 92 | UI error messages only, or limited marketing accents. |

### Typography

| Role | Typeface | Weight | Notes |
|------|----------|--------|-------|
| Logo / situational marketing | Bricolage Grotesque | Semibold | Logo font only — don't use for body text. |
| Headlines | Manrope | Regular | Tracking: 2%, Leading: 120%, Sentence case. |
| Eyebrows | Manrope | ExtraBold | Tracking: 10%, Uppercase. |
| Body / paragraphs | Manrope | Regular | Tracking: 2%, Leading: 140%, Sentence case. |
| CTAs / buttons | Manrope | ExtraBold | Tracking: 5%, Title case. |

Both Manrope and Bricolage Grotesque are free Google Fonts, which means they render correctly in Google Slides and Google Docs without any extra installation. For .pptx or .docx files where Manrope may not be available on the recipient's system, embed the font or note that Manrope should be installed from Google Fonts.

### Type & Color Pairing

- Charcoal text (#272727) can be set on: Spring, White, Silver, Lavender backgrounds.
- White text (#FFFFFF) can be used on Charcoal backgrounds for CTA buttons, closing slides, and dark section dividers.
- Spring text (#34FF85) can be used on Slate (#475258) backgrounds for quote/key-finding slides — this is an approved high-contrast pairing.
- Never place Charcoal text on Charcoal, Slate, or Violet backgrounds.

### Logo Usage

- Logo comes in three forms: Logo Lockup (mark + wordmark), Logomark (icon only), Logotype (wordmark only).
- Only use the logo in Charcoal (#272727) or White (#FFFFFF). Never apply other colors, gradients, outlines, or rotations to the logo.
- Primary colorway is Charcoal logo on Spring background — use for high-impact brand moments (hero areas, cover slides, branded banners).
- Charcoal on White for everyday use (documents, invoices, presentations).
- White on Charcoal for dark-mode layouts (footers, backdrops, closing slides).
- Logo files are available in `assets/logos/` — always embed the actual image file rather than describing it.

---

## Applying the Brand by Content Type

### Presentations (Google Slides — primary format)

Blackthorn uses **Google Slides** as its primary presentation tool. The company template is available at: https://docs.google.com/presentation/d/1DHZXhbtYSbW-Vd2hq01N1jziSocZPylP3zzpcKi9Qno/edit

When creating a new deck, start from a copy of this template whenever possible. The template has Manrope pre-configured (it's a Google Font, so it renders natively in Slides without installation).

If the user needs a .pptx file instead of Google Slides, note that Manrope must be embedded or installed on the recipient's machine — otherwise it will fall back to a system font like Calibri. When generating .pptx programmatically, explicitly set the font to Manrope and consider embedding it.

**Slide design rules (apply whether in Google Slides or .pptx):**

Use Manrope for all text. Bricolage Grotesque only for the logo. Use the brand color palette strictly — no off-palette colors. Follow headline/eyebrow/subheadline formatting rules above.

**For the complete slide template catalog with 23 approved layouts, sequencing guidelines, and deck-type patterns, read `references/slide-templates.md`.**

#### Template Design Patterns (from the Blackthorn Company Template)

These patterns appear consistently across the template slides. Apply them to maintain visual consistency with the rest of the company's decks.

**Cover slide:**
- Spring (#34FF85) background with Charcoal text.
- Blackthorn logo lockup (Charcoal, use `assets/logos/PNG/Blackthorn-LogoLockup-272727.png`) in the top-left corner.
- Title in Manrope Regular, 40-44pt, positioned lower-left.
- "A Salesforce Partner since 2016" tagline in small text.
- Large, semi-transparent decorative logomark shapes in the background (overlapping, rotated at different angles) creating depth. These shapes use a slightly darker Spring tone or subtle opacity.

**Content slides — two-column layout (primary content pattern):**
- White background.
- Left column (~30-35% width): Spring (#34FF85) background block containing the slide heading in Charcoal, Manrope Regular, 28-32pt. This Spring block acts as a visual anchor and hierarchy signal.
- Dotted vertical divider line (Charcoal or Slate dots) separating left and right columns.
- Right column (~60-65% width): Body content in Charcoal on White — paragraphs, bullet points, or sub-sections.
- This two-column pattern with Spring heading block is the default content layout and should be used for most informational slides.

**Numbered items:**
- Numbers displayed inside Lavender (#EBEBFF) circles with thin Charcoal (#272727) outlines.
- Number text in Charcoal, Manrope Bold.
- Each numbered item has a title (Manrope Bold, Charcoal) and description (Manrope Regular, Charcoal or Slate) to the right of the circle.

**Section divider slides:**
- Spring (#34FF85) background.
- Large Charcoal heading centered.
- Decorative: multiple overlapping, semi-transparent logomark shapes in the background at varying sizes and rotations (the same motif as the cover slide).
- Dark variant: Charcoal background with White text and Spring accent underline.

**Quote / key finding slides:**
- Slate (#475258) background — this is the approved dark-but-not-Charcoal background for emphasis.
- Quote or key finding text in Spring (#34FF85), large, centered.
- Attribution or context in White or Silver below.
- This Slate + Spring colorway is reserved for high-impact callouts.

**Data and metrics slides:**
- Spring left panel (same two-column pattern) with the metric category or label.
- Large numbers in Violet (#7360FF), 48-60pt, on the right side.
- Dotted horizontal dividers between metric rows.
- Charts use brand palette in order: Spring, Charcoal, Violet, Slate, Silver, Lavender.
- Tables use Spring header row with alternating White/Lavender data rows.

**Team and icon slides:**
- Spring-to-White gradient on the header/top area of the slide, fading downward.
- Content (team photos, icons, descriptions) on the White portion below.
- Icons and feature labels use Spring or Violet accents.

**Closing slide:**
- Two variants in the template:
  1. Charcoal (#272727) background with White logo lockup centered (use `assets/logos/PNG/Blackthorn-LogoLockup-FFFFFF.png`), tagline "Your events. Your data. All in Salesforce." in White below.
  2. Spring (#34FF85) background with Charcoal logo lockup and CTA text — used for a more energetic, action-oriented close.

**Consistent footer (all content slides):**
- Small Blackthorn logo lockup (Charcoal) in the bottom-left corner.
- Page number in small text (Manrope Regular, 10-12pt, Slate) in the bottom-right corner.
- Footer area is minimal and unobtrusive — thin line or just whitespace separating it from content.

**Dotted dividers:**
- The template uses dotted lines (not solid) for visual separation — both vertical (between columns) and horizontal (between content sections or metric rows).
- Dots are small, evenly spaced, in Charcoal or Slate.
- This is a distinctive Blackthorn design element — use dotted dividers instead of solid rules wherever dividers are needed.

### Documents (.docx)
- Use Manrope for headings and body text.
- Heading 1: Manrope Regular, large size, Charcoal color.
- Body text: Manrope Regular, Charcoal.
- Accent color for borders, dividers, or highlights: Spring (#34FF85) or Violet (#7360FF).
- Include Blackthorn logo (use `assets/logos/PNG/Blackthorn-LogoLockup-272727.png` or `assets/logos/PNG/Blackthorn-Logotype-272727.png`) in the header or first page.

### Spreadsheets (.xlsx)
- Header row: Spring (#34FF85) background with Charcoal text, Manrope Bold.
- Data rows: alternating White and Lavender (#EBEBFF) for readability.
- Accent highlights: Violet (#7360FF) for key metrics or callouts.
- Chart colors: Follow the brand palette order — Spring, Charcoal, Violet, Slate, Silver, Lavender.

### Marketing Copy (blogs, emails, social, landing pages)
- Apply all voice and tone rules.
- Lead with value props relevant to the audience.
- Use the company description appropriate to the format length (see references/messaging.md for <150 char, <250 char, <50 word, and <100 word versions).
- Never use avoided words/phrases.
- For email subject lines, always use numerals for numbers.

---

## Brand Review Checklist

When reviewing existing content for brand consistency, check each of these:

1. **Voice**: Does it sound friendly, natural, clear, supportive, and fresh? Or does it sound dry, cheesy, pretentious, aggressive, or boring?
2. **Avoided words**: Any instances of "seamless," "harness the power," "streamline," "transform," "simplify," "save time and money," "integration," "alpha," "beta," or "MVP"?
3. **Style rules**: Headlines in sentence case? Oxford commas? Numbers formatted correctly? Salesforce® used properly?
4. **Messaging accuracy**: Are value props and descriptions consistent with the messaging architecture? Is Blackthorn described as Salesforce-native (not as an integration)?
5. **Visual identity** (for designed content): Correct colors, fonts, logo usage, and type/color pairings?
6. **Exclamation points**: Used sparingly and only in direct customer interactions?
7. **Jargon and buzzwords**: Is everything accessible to a layperson? Any terms that need defining?

When flagging issues, provide the specific off-brand text and a suggested on-brand replacement.
