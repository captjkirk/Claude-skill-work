# Opportunity Schema

Opportunities are the Sales record that precede every onboarding. For Jared, the Opportunity is primarily a reference — not something he works in day-to-day — but it contains critical context for understanding what a customer purchased and what they were told during the sales process.

**Naming convention:** `[ACRONYM] Account Name - App - Type`
Example: `[HAF] Hindu American Foundation - Events - Initial`

**Type values:** Initial, Expansion, Renewal

---

## How Jared Uses Opportunities

1. **Notes & Attachments** — The signed contract lives here as an uploaded file. This is the fastest way to confirm exactly what the customer purchased (license counts, registration limits, specific terms) when taking over a new account.

2. **Key Fields tab** — Commercial details: ARR, registration counts, dates, app purchased, contact assignments.

3. **Qualifying tab** — Discovery context: why they bought, what they were using before, pain points, feature requirements, and deal risk. Critical for managing expectations during onboarding — especially if there's a mismatch between what was sold and what the product actually does. The **Sales to CS Notes** and **Closed Won Analysis** (Momentum fields at the bottom of this tab) are the richest handoff content — read both before a kickoff call.

---

## Key Fields Tab

### Opportunity Information
| Field | Notes |
|-------|-------|
| Opportunity Name | [ACRONYM] Account - App - Type |
| Account Name | Linked Account |
| Type | Initial / Expansion / Renewal |
| Stage | Closed Won (for onboarding customers) |
| App | Events, Payments, Messaging, etc. |
| ACV / ARR | Annual recurring revenue |
| Amount / TCV | Total contract value |
| Registrations Per Year | Licensed registration volume |
| Registration or User Based? | Blended, User-Based, Registration-Based |
| App Value | Apps included |
| Close Date | Date deal closed |
| Start Date | Contract start date |
| End Date | Contract end date |
| Renewal Term (Months) | Contract length (typically 24) |
| Multi Product? | Whether multiple apps are included |
| Opportunity Owner | AE who closed the deal |
| Qualified By | Person who qualified the lead |

### Contact Assignments
| Field | Notes |
|-------|-------|
| Stakeholder Contact | Primary business contact |
| Technical User Contact | Person handling technical setup |
| Billing Contact | Finance/AP contact |
| Accounts Payable | AP contact |

### Contract Information
| Field | Notes |
|-------|-------|
| Auto-Renewal | Yes / No |
| MSA Version | Master Service Agreement version |
| Contract Uplift % | Annual price increase (default 10%) |
| Has Special Terms & Conditions? | Flags non-standard contract terms |

### Alliances Notes
| Field | Notes |
|-------|-------|
| Partner | SI or implementation partner (e.g. Huron, Attain) |
| Partner Point of Contact | Partner contact name |
| Salesforce Rep | Customer's Salesforce AE |

---

## Qualifying Tab

This is the most useful tab for onboarding context. Captures what the AE learned during discovery.

### Situation
| Field | Notes |
|-------|-------|
| AE Disco Notes | Full AE discovery call notes — current tools, goals, integration needs |
| Pre Demo Notes | Notes from before the demo |
| Salesforce | Whether they're a Salesforce customer (Yes/No) |
| RFI/RFP | Whether a formal procurement process was involved |

### Pain
| Field | Notes |
|-------|-------|
| Use Case | What types of events/registrations they run |
| Current Process | What tools they use today and how they manage events |
| Pain Points | What's broken or frustrating about their current setup |
| Feature Requirements | Specific features they said they need |
| Competitors Considered | Other platforms they evaluated |
| BT Missing Features | Features they wanted that Blackthorn doesn't have — flag for managing expectations |

### Impact
| Field | Notes |
|-------|-------|
| ROI / Success Metric | How they'll measure success |

### Critical Event
| Field | Notes |
|-------|-------|
| Timeline to Purchase? | What drove their timing (e.g. contract expiring, event coming up) |
| Ideal Launch Date | When they wanted to go live |

### Decision Process
| Field | Notes |
|-------|-------|
| Deal Risk | AE's notes on what could have derailed the deal |
| Business User Contact | Who uses the product day-to-day |
| Economic Buyer Contact | Decision-maker / budget holder |
| Technical User Contact | Technical contact |

### Event Insights
| Field | Notes |
|-------|-------|
| Events Free or Paid | Both, Free only, Paid only |
| Registrations Per Year | Volume committed |
| Registration or User Based? | Blended, User-Based, Registration-Based |
| Total Event Users | Number of licensed event users |

### Account Insights
General account context captured during the sales process.

| Field | Notes |
|-------|-------|
| Account Industry | e.g. Nonprofit, Higher Education, Healthcare |
| Nonprofit? | Checkbox |
| Stakeholder Contact | Business sponsor (also in Key Fields) |
| Technical User Contact | Hands-on technical contact (also in Key Fields) |
| Partner | SI or implementation partner, if any |
| Partner Tier | Partner tier level |
| Partner Rep Notes | Notes from the partner's rep |
| Source | Lead source (e.g. Website - Sales) |
| Influenced By (First) | First-touch attribution |
| Last Touch Campaign Source | Last campaign before close |
| Current Gateway / Payment Processor(s) | Their current payment setup — important for Payments onboarding |
| Salesforce Rep | Customer's Salesforce AE |

### Momentum Fields (Post-Close Analysis)
These are filled in by Momentum (sales intelligence tool) after the deal closes. **These are among the most valuable fields for onboarding.** Check all four before a kickoff call.

| Field | Notes |
|-------|-------|
| Closed Won Analysis - Momentum | Detailed SPICED analysis of why the deal closed — winning conditions, buyer context, pain drivers, rep behaviors, competitive displacement. Long-form. Read before kickoff to understand what the customer was sold on. |
| Closed Lost Analysis - Momentum | Populated only for churned/lost deals. Explains why they didn't renew or left. |
| Sales to CS Notes - Momentum | **The most important handoff field.** Written by the AE at close. Covers: stakeholders & risk factors, planned usage & use cases, event types, success criteria, known concerns/objections, feature gaps, assumptions to validate, change-management considerations, implementation notes, immediate next steps, and items likely to delay launch. Read this before every first call with a customer. |
| Deal Summary - Momentum | Short-form summary (often blank). |

---

## Related Lists (Relevant to Onboarding)

| Related List | Notes |
|-------------|-------|
| Notes & Attachments | **Contract PDF lives here** — check this first when onboarding a new customer |
| Contact Roles | All contacts associated with the deal and their roles |
| Products | Line items purchased |
| Opportunity Team | AE, SDR, SE who worked the deal |

---

## Notes

- Fathom call summaries from onboarding calls sometimes get auto-attached as Notes on the Opportunity — check here if notes aren't showing up on the COM record
- The Opportunity Owner (AE) is distinct from the Onboarding Manager — Lauren Orscheln, Jason Gannon, Damon Menapace are examples of AEs who may have owned deals that Jared onboards
