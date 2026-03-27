# Onboarding Schedule Templates

**Object API Name:** `Onboarding_Schedule_Template__c`
**Related activities object:** `Onboarding_Activities__r` (child relationship)

Templates define the standard sequence of activities for each onboarding type. When a COM record is created, the matching template auto-generates Onboarding Events in sequence.

---

## 5 Templates

1. Premier Onboarding
2. Dedicated Onboarding
3. Messaging Onboarding
4. Standard Onboarding
5. Self-Onboarding

---

## Activity Fields

Each activity has:
- **Onboarding Activity Name** — what the task is
- **Milestone** — which phase it belongs to
- **Task Owner** — OBM, Customer, CSM & OBM, or Support & OBM
- **Meeting Sequence** — numeric order (increments of 5–10; gaps allow inserting ad-hoc items)

---

## Milestones (in order)

1. Discovery
2. Sandbox Build
3. Review/Iterate
4. Learn/Test
5. Go Live
6. Hyper Care

> These are the **current active milestone system** — distinct from Emily's aspirational 10-meeting framework. The milestones here drive the Onboarding Stage (New) field on COM records.

---

## Premier Onboarding — Full Activity List (31 items)

| # | Activity | Milestone | Owner | Seq |
|---|----------|-----------|-------|-----|
| 1 | Initial Welcome Email | Discovery | OBM | 5 |
| 2 | Sales Handoff Call | Discovery | OBM | 10 |
| 3 | Create Customer Journey Presentation | Discovery | OBM | 30 |
| 4 | Share Pre-Onboarding Survey & Event Setup Surveys with the Customer | Discovery | OBM | 40 |
| 5 | Send Kickoff Invitation to the Customer | Discovery | OBM | 50 |
| 6 | Kickoff Project with Implementation Team | Discovery | CSM & OBM | 60 |
| 7 | Kickoff Follow up Email | Discovery | CSM & OBM | 65 |
| 8 | Confirm Core and Admin Users for Adoption Guides | Discovery | OBM | 66 |
| 9 | Assign Adoption Guides | Discovery | OBM | 67 |
| 10 | Sign off on Discovery Phase | Discovery | CSM & OBM | 70 |
| 11 | Blackthorn Installation into Sandbox | Sandbox Build | Support & OBM | 80 |
| 12 | Build all three Event Templates | Sandbox Build | OBM | 90 |
| 13 | Review Event Templates from Support | Sandbox Build | OBM | 95 |
| 14 | Send event templates to the customer for review | Sandbox Build | OBM | 100 |
| 15 | Receive Customer feedback on Event Templates | Review/Iterate | OBM | 110 |
| 16 | Update the three Events | Review/Iterate | OBM | 120 |
| 17 | Create Event Template Overview video to show updates in Sandbox | Review/Iterate | OBM | 130 |
| 18 | Iterate event templates as needed | Review/Iterate | OBM | 140 |
| 19 | Customer Team Event Template Sign Off | Review/Iterate | Customer | 150 |
| 20 | Core Users Complete Foundational Training | Learn/Test | Customer | 170 |
| 21 | Customer UAT | Learn/Test | Customer | 180 |
| 22 | Admins Complete Admin Training | Learn/Test | Customer | 190 |
| 23 | Admins Pass Admin Exam | Learn/Test | Customer | 200 |
| 24 | Customer/BT meet to sign off on milestone | Learn/Test | CSM & OBM | 210 |
| 25 | Customer team Installs Blackthorn into production | Go Live | Customer | 220 |
| 26 | Complete All Production Install and Configuration Steps | Go Live | Customer | 230 |
| 27 | Customer Event Build | Go Live | Customer | 240 |
| 28 | Blackthorn Reviews Org | Go Live | OBM | 250 |
| 29 | Team can activate and go-live with Events | Go Live | Customer | 270 |
| 30 | OBM - Reactive Event Setup Support | Hyper Care | OBM | 280 |
| 31 | Handoff Call Back to CSM | Hyper Care | OBM | 290 |
