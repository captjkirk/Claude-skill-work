# COM Object Schema

**Object API Name:** `Customer_Onboarding_Management__c`
**Built by:** Jared Kirk (replaced an external system)

---

## Header Fields

| Field | Notes |
|-------|-------|
| Account | Lookup to Account |
| Opportunity | Lookup to Opportunity (the originating sale) |
| Onboarding Start Date | When onboarding formally began |
| Planned First Event Published Date | Target go-live date for first event |
| Renewal Date | Contract renewal date |

---

## Stage Progress Bar

Five sequential stages displayed as a progress path at the top of the record:

`Pre-Onboarding` → `Install & Tech Review` → `Self-Learning in the Hub` → `Pending First Event` → `Completed`

Advance stages using the "Mark Onboarding Stage as Complete" button.

---

## Project Information Section

| Field | Notes |
|-------|-------|
| Owner | Record owner (User) |
| Onboarding Manager | Assigned OBM |
| Customer Onboarding Management Project | Display name for the project |
| Record Type | Premier Onboarding, Standard Onboarding, Self-Onboarding, Dedicated Onboarding |
| Contract ARR | Annual recurring revenue |
| Planned First Event Published Date | Target first event go-live |
| What did you purchase? | License/product details (e.g. "Events – 2,000 regs, 3 Full Users, 3 Lite Users") |
| Onboarding Status | On Track / Late / etc. |
| Onboarding Document | URL to customer's Google Drive kickoff deck |
| Org Login Info | Sandbox and Production org URLs, usernames, temp passwords for Blackthorn access |
| How are we being used? | Customer use case context |
| Onboarding Key Dates | Notable dates from the customer |

---

## System Information Section

| Field | Notes |
|-------|-------|
| Production Org ID | 15-char Salesforce org ID for production |
| Sandbox Org ID | 15-char Salesforce org ID for sandbox |
| Starting in Sandbox? | Checkbox — whether onboarding starts in sandbox |
| Payment Gateway | Payment processor (Stripe, TouchNet, etc.) |
| Other Known Integrations | Non-standard integrations to be aware of |
| Previously Used Solution | What they used before Blackthorn |
| Apps Purchased | Products purchased (Events, Payments, Messaging, etc.) |

---

## Project Overview Panel (Right Side)

| Field | Notes |
|-------|-------|
| Onboarding Stage (New) | Current milestone: Discovery, Sandbox Build, Review/Iterate, Learn/Test, Go Live, Hyper Care, Post-Onboarding |
| Last Interaction | Free text — most recent interaction notes |
| Steps to Next Stage | Free text — what needs to happen to advance |
| Concerns | Free text — active concerns or risks |
| Flagged | Checkbox — marks account as at-risk |
| Flagged Category | Product Misalignment, Miscommunication, Product Issues Blocking Go-Live, Delayed Timelines, Lack of Skill/Resources, Partner Concerns, Contract Concerns |
| Flagged Reason? | Rich text — detailed description of the flag, product gaps, risk factors, and context |

> **Note:** Onboarding Stage (New) is the active milestone system. The Stage Progress Bar is a separate higher-level tracker. These are two distinct fields.

---

## Project Dates Panel (Right Side)

Three tiers of dates — Ideal (system-calculated), Planned (target), Actual (what happened):

| Field | Tier |
|-------|------|
| Onboarding Start Date | Actual |
| Project Start Date | Planned |
| Ideal Event Published Date | Ideal |
| Ideal First Event Date | Ideal |
| Ideal CS Transition Date | Ideal |
| Planned First Event Published Date | Planned |
| Planned First Event Date | Planned |
| Planned CS Transition Date | Planned |
| Actual First Event Published Date | Actual |
| Actual First Event Date | Actual |

Dates are based on: **Planned GO Live Date**

---

## Tabs

| Tab | Purpose |
|-----|---------|
| Details | All fields above |
| Onboarding Events | Screen flow to log events + related list of logged events |
| Chatter | Internal notes and feed |
| Project Snapshot | Summary view |

---

## Related Lists

| Related List | Object | Notes |
|-------------|--------|-------|
| Onboarding Events | `Onboarding_Event__c` | All logged meetings and activities |
| Licenses | `sfLma__License__c` | Production and sandbox package licenses |
| Assignments | `EduGuide__Assignment_edu__c` | Adoption guides assigned to customer contacts |
| Cases | `Case` | Support tickets filed under the customer account. **Important:** Cases filed by a SI/partner go under the *partner's* account, not the customer's — they won't appear here. Use the License related to the case as a signal to identify the actual customer. |
| CX Escalations | Custom | Formal escalations |
| Engagements | `EduGuide__Engagement_edu__c` | EduGuide content engagement tracking |
| CX Time Tracking (COM) | Custom | Time logs created alongside Onboarding Events |
| Typeform Responses | `Typeform_Response__c` | Mapped survey responses (pre-onboarding, event template, etc.) |
| Notes & Attachments | Attachment | File attachments |
| Customer Onboarding Management History | Field History | Audit trail of field changes |

---

## Onboarding Events — Log Form Fields

Accessed via the "Onboarding Events" tab. Screen flow creates the event record and a CX Time Tracking record simultaneously.

| Field | Required | Notes |
|-------|----------|-------|
| Onboarding Event Name | Yes | |
| Meeting Type | Yes | See picklist below |
| Account | Yes | Pre-filled |
| Meeting Date | Yes | Defaults to today |
| Meeting Length (In Hours) | Yes | Defaults to 0.50 |
| Meeting Description | Yes | |
| Public Recording Link | No | Customer-visible (e.g. Fathom public link) |
| Public Meeting Notes | No | Customer-visible notes |
| Internal Recording Link | No | Internal only |
| Private Meeting Notes | No | Rich text, internal only |

**Meeting Type picklist values:**
Ad-Hoc Meeting, Advisement Session, Churn Risk, CS Handoff/CSM Intro, Customer Re-Sync, Customer Sync, Expansion - Handoff to Sales, Feature Review, Intro Call, Kickoff Call, Office Hours, Partner Advisement, Product Meeting, Renewal Conversation, Reverse Demo, Sales Handoff, Strategic Account Update, Tech Audit (Meetings & Prep), Typical Onboarding, Working Session

The screen flow auto-sequences the new event after the most recently completed event in the schedule.

---

## Onboarding Event Record — Full Field Reference

What a completed event record looks like when you open it directly (beyond the log form).

**Record title (Salesforce Name field):** Displays the Milestone name (e.g., "Review/Iterate"), not the event name. The descriptive name lives in the separate "Onboarding Event Name" field.

**Header summary bar:** Customer Onboarding Management (link), Date Completed, Onboarding Event Type, Days from Start.

### Details Section (left side)

| Field | Notes |
|-------|-------|
| Onboarding Event Name | Descriptive name (e.g., "Onboarding Sync") |
| Customer Onboarding Management | Lookup to COM record |
| Meeting Date | Scheduled or actual meeting date |
| Meeting Length (In Hours) | Duration |
| Category | Auto-mapped from Meeting Type (e.g., "Customer Sync") |
| Date Completed | Date the event was logged |
| Days from Start | Auto-calculated days since onboarding start |
| Days since Last Progress | Auto-calculated gap since prior event |
| Milestone | Which milestone this event belongs to (e.g., Review/Iterate) |
| Onboarding Event Type | Meeting or Task |
| Task Owner | Who owns this item (OBM, CSM & OBM, Support & OBM, etc.) |
| Public Recording Link | Customer-visible Fathom link |
| Internal Recording Link | Internal-only recording link |

### Meeting Description & Notes Section

| Field | Notes |
|-------|-------|
| Description | Brief purpose statement (e.g., "Sync on Onboarding Progress, Timeline, Next Steps, and Q&A.") |
| Public Meeting Notes | Full Fathom AI summary — **plain text format**. Customer-visible. |
| Private Meeting Notes | Full Fathom AI summary — **rich text format** with headers, bullet points, blue hyperlinks. Internal only. |

Both notes fields typically contain the same Fathom-generated content in different formats. Standard Fathom note structure includes: Meeting Purpose, Contacts on Call (Non-Blackthorn), Customer Sentiment, Progress Since Last Sync, Issues & Tickets (per issue: Context / Status / Concerns-Challenges-Blockers / Ideas and Explanations / Decisions and Next Steps / Current Objective), Product Feedback, Blackthorn Promised Actions/Deliverables, Plans Between Now and Next Call, Other & Incidental Topics, and Action Items with timestamped Fathom video links.

### Customer Use Information Panel (right side)

Captures new use case information surfaced during the meeting. Usually blank — fill in when something notable comes up.

| Field | Notes |
|-------|-------|
| Any New Standard Use Case Information? | New standard use cases discovered |
| Any New Custom Use Case Information | Custom/unique use cases discovered |
| Any New Business Impact Information? | Business impact or ROI signals |

### System Information Section

| Field | Notes |
|-------|-------|
| Meeting Sequence | Auto-assigned sequence number (e.g., 112) — determines order in the event log |
| Logged | Checkbox — checked when the event has been logged/completed |
| Created By / Last Modified By | Audit fields |

---

## License Records — Key Fields

**Object API Name:** `sfLma__License__c`

| Field | Notes |
|-------|-------|
| Package Name | Events, Payments, Messaging (Textey), PayLink, Base |
| Package Version Number | Current installed version |
| License Type | Editable, Site License |
| Licensed Seats / Seats / Used Licenses | Seat allocation and current usage |
| Expiration Date | "Does not expire" for most active licenses |
| Subscriber Org ID | 15-char org ID (matches Production/Sandbox Org ID on COM) |
| Subscriber Org Is Sandbox | Checkbox distinguishing prod vs. sandbox |
| BT Connected User | Primary connected user in the customer org |
| Org Edition | Enterprise Edition, Professional, etc. |
| Org Status Formula | ACTIVE, INACTIVE, etc. |
| ARR / ARR Normalized | Revenue figures |
| Technical Contact Email | Primary technical contact |
| Log Into Subscriber Console | Button — opens direct login to customer's Salesforce org |

**Product Usage (related panel):** Monthly records showing registration counts by period (Start Date, End Date, Number of Registrations). Key signal for actual product adoption.

**License History (related panel):** Tracks changes to Used Licenses over time — useful for seeing adoption growth.

---

## Typeform Responses

**Object API Name:** `Typeform_Response__c`

Responses from customers filling out Blackthorn's Typeform surveys are automatically mapped into Salesforce records. Each response links to an Account, COM record, and a Typeform Form Mapping record (MAP-XXXXXX) that defines the field mapping.

**Key fields:**
- Typeform Form Answered — which form was submitted
- Record Type — determines the layout and field mapping
- Response Mapped — checkbox confirming data was successfully mapped
- Contact People section — project/stakeholder and technical contact details
- Onboarding Information tab — dates, tech stack, previous tools, feature intentions, org IDs

**Known form types / record types:**

| Form Name | Record Type | Linked to COM? | Notes |
|-----------|------------|----------------|-------|
| Pre-Onboarding Information 3.0 | Pre-Onboarding Survey | Yes | Captures: contacts, key dates, previous tools, sandbox/prod org IDs, feature interests (paid events, AttendeeLink, mobile check-in, email tool) |
| Event Template Questionnaire | (Event Template) | Yes | Customer fills this out to specify the events they want Blackthorn to build in their org during onboarding. Tied to a specific Template Event Name. |
| Daily Office Hours | Daily Office Hours | No | Auto-sent after an office hours session to collect feedback on how it went. Not tied to a COM — captures any customer. |
| Blackthorn Events Certified Administrator | (Certification) | No | Records results of the Blackthorn admin certification quiz. Includes "Quiz Passed?" field. Note: certification quiz is currently not functioning correctly. |

**Additional Typeform Response fields visible in the All list view:**
- Response Mapped — whether the data was successfully mapped to Salesforce fields
- Quiz Passed? — relevant for certification form responses
- Typeform Response Timestamp

---

## Assignments (EduGuide)

**Object API Name:** `EduGuide__Assignment_edu__c`

EduGuide adoption guide courses proactively assigned to customer contacts by the OBM. Sorted by Overall Progress (%).

| Field | Notes |
|-------|-------|
| Assignment Number | A-XXXX |
| Contact | Who the assignment is for |
| Assignment Name | Which adoption plan (e.g. "Event Manager Adoption Plan", "Event Administrator Adoption Plan") |
| Overall Progress | % complete |
| Assignment Link | Direct URL to the course in community.blackthorn.io |

Customers access assigned content via community.blackthorn.io.
