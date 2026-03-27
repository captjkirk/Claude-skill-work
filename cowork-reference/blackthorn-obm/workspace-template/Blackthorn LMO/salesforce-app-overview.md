# Blackthorn LMO — Salesforce App Overview

**Org URL:** https://blackthornio.lightning.force.com
**App:** Customer Onboarding Management
**API prefix:** `sfLma__` (licenses), `EduGuide__` (EduGuide objects), `conference360__` (Events objects)

---

## Navigation Tabs

| Tab | Object API Name | Purpose |
|-----|----------------|---------|
| Customer Onboarding Management | `Customer_Onboarding_Management__c` | Active and historical onboarding projects |
| Content | `EduGuide__Content_edu__c` | EduGuide learning hub content and adoption guides |
| Learning Studio | (EduGuide app) | EduGuide authoring/management interface |
| Engagements | `EduGuide__Engagement_edu__c` | Customer engagement with EduGuide content |
| Assignments | `EduGuide__Assignment_edu__c` | EduGuide adoption guides assigned to contacts |
| Onboarding Schedule Templates | `Onboarding_Schedule_Template__c` | Standard activity sequences per onboarding type |
| Typeform Responses | `Typeform_Response__c` | Mapped survey responses from customers |

---

## Home Dashboard

Key widgets on the Onboarding Dashboard:
- **Open Onboardings** — count of active COM records
- **My Active Onboardings by Milestone** — Jared's current accounts by milestone stage
- **(Calendly) Office Hours Report** — tracks office hours activity via Calendly
- **Accounts that have used...** — adoption/usage signal
- **CX Time Tracking Today** — quick-log widget: "What account did you meet with?" — prompts time entry directly from the home page

---

## Key Buttons on COM Records

| Button | What it does |
|--------|-------------|
| Edit | Standard record edit |
| Delete | Delete the COM record |
| Create CX Escalation | Logs a CX escalation related object |
| Milestone Progress Report | Generates a progress report snapshot |

---

## Notes

- The "Log Into Subscriber Console" button on License records allows direct login to the customer's Salesforce org — useful for verifying installs and configurations
- The app is entirely custom-built by Jared Kirk (started Nov 2023, last major update May 2024 based on template timestamps)
- This is the main Blackthorn org — it handles both license management (sfLma) and the full CX/onboarding workflow
