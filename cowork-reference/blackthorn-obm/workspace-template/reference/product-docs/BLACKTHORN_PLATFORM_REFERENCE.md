# Blackthorn Platform Reference

> A comprehensive guide to the four Salesforce packages that make up the Blackthorn Events platform.
> Written for developers building applications that integrate with or extend these codebases.

---

## Table of Contents

1. [Platform Overview](#platform-overview)
2. [How It All Fits Together](#how-it-all-fits-together)
3. [Blackthorn Base (bt_base)](#blackthorn-base-bt_base)
4. [Blackthorn Payments (bt_stripe)](#blackthorn-payments-bt_stripe)
5. [Blackthorn Events (conference360)](#blackthorn-events-conference360)
6. [Events Webapp](#events-webapp)
7. [Cross-Package Data Flows](#cross-package-data-flows)
8. [Key Integration Patterns](#key-integration-patterns)

---

## Platform Overview

Blackthorn is an event management platform built on Salesforce. It consists of four repositories that work together:

| Repository | Namespace | Type | Purpose |
|-----------|-----------|------|---------|
| **Base** | `bt_base__` | Salesforce managed package | Foundation layer: platform events, portal roles, logistics, exhibit spaces, email blasts, asset management |
| **Payments** | `bt_stripe__` | Salesforce managed package | Payment processing: Stripe integration, transactions, subscriptions, invoices, virtual terminal |
| **Events** | `conference360__` | Salesforce managed package | Core event management: events, sessions, attendees, tickets, speakers, sponsors, forms, registration checkout |
| **Events Webapp** | N/A | Angular + Express.js app | Public-facing registration portal: event pages, session browsing, ticket purchase, checkout UI |

**Salesforce is always the system of record.** External apps (the webapp, Planner UI) read/write via Salesforce APIs and never persist PII locally.

### Installation Order

```
1. Blackthorn Base (bt_base)           ← no dependencies
2. Blackthorn Payments (bt_stripe)     ← no package dependencies (standalone)
3. Blackthorn Events (conference360)   ← depends on Base v1.46+ AND Payments v6.48+
4. Events Webapp                       ← connects to a Salesforce org with all three packages installed
```

---

## How It All Fits Together

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                        PUBLIC INTERNET                              │
│                                                                     │
│  ┌──────────────────────┐    ┌──────────────────────────────────┐  │
│  │   Events Webapp      │    │   Planner UI (Next.js)           │  │
│  │   (Angular + Express)│    │   (Admin portal - separate repo) │  │
│  │   Public registration│    │   Event planning & management    │  │
│  └──────────┬───────────┘    └──────────────┬───────────────────┘  │
│             │                                │                      │
│             │  REST APIs / Webhooks          │  REST APIs / OAuth   │
│             │  Stripe.js (client-side)       │                      │
└─────────────┼────────────────────────────────┼──────────────────────┘
              │                                │
┌─────────────┼────────────────────────────────┼──────────────────────┐
│             ▼                                ▼                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                    SALESFORCE ORG                             │  │
│  │                                                              │  │
│  │  ┌────────────────────────────────────────────────────────┐  │  │
│  │  │  Blackthorn Events (conference360__)                   │  │  │
│  │  │  - Events, Sessions, Attendees, Tickets, Speakers      │  │  │
│  │  │  - Registration checkout (REST API)                    │  │  │
│  │  │  - Forms, Email Templates, Campaign Sync               │  │  │
│  │  │  - 730+ Apex classes, 159 LWCs, 51 triggers            │  │  │
│  │  └──────────────────┬───────────────┬─────────────────────┘  │  │
│  │                     │               │                        │  │
│  │          ┌──────────▼──┐    ┌───────▼───────────┐           │  │
│  │          │ Base        │    │ Payments           │           │  │
│  │          │ (bt_base__) │    │ (bt_stripe__)      │           │  │
│  │          │             │    │                    │           │  │
│  │          │ - Platform  │    │ - Stripe API       │           │  │
│  │          │   Events    │    │ - Transactions     │           │  │
│  │          │ - Portal    │    │ - Subscriptions    │           │  │
│  │          │   Roles     │    │ - Invoices         │           │  │
│  │          │ - Logistics │    │ - Webhooks         │           │  │
│  │          │ - Exhibits  │    │ - Payment Methods  │           │  │
│  │          │ - Assets    │    │ - Virtual Terminal  │           │  │
│  │          └─────────────┘    └────────┬──────────┘           │  │
│  │                                      │                       │  │
│  │                                      ▼                       │  │
│  │                              ┌───────────────┐               │  │
│  │                              │  Stripe API   │               │  │
│  │                              │  (External)   │               │  │
│  │                              └───────────────┘               │  │
│  └──────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────┘
```

### Data Flow: Event Registration (End-to-End)

```
1. Attendee visits Events Webapp → browses events
2. Selects tickets, fills form → webapp calls REST API
3. Events package validates capacity, promo codes, duplicates
4. Events calls Payments → creates Sales Document + Transaction
5. Payments calls Stripe API → processes charge
6. Stripe webhook → Payments webhook endpoint → updates Transaction status
7. Events creates Attendee records + Event Item Purchases
8. Base publishes Platform Event → triggers async notification to Planner UI
9. Planner UI receives notification → triggers confirmation email via SendGrid
```

### Package Dependency Chain

```
Events (conference360__)
  ├── depends on → Base (bt_base__) v1.46+
  │     └── Provides: platform events, portal roles, logistics objects
  └── depends on → Payments (bt_stripe__) v6.48+
        └── Provides: transactions, sales documents, line items, payment gateways
```

---

## Blackthorn Base (bt_base)

### Purpose

Foundation layer providing infrastructure for the Blackthorn platform. Bridges Salesforce with external applications (Planner UI) via platform events and async HTTP callouts. Also provides operational objects for logistics, exhibits, portal access, and sponsor benefits.

### Namespace: `bt_base__`

### Custom Objects (8)

| Object | Purpose | Key Relationships |
|--------|---------|-------------------|
| `Email_Blast__c` | Outbound email campaign tracking | → Event; stores delivery metrics (sent/opened/clicked/bounced/failed) |
| `Exhibit_Space__c` | Booth/floor inventory | → Event; size, type (10x10, Island, Corner), pricing, availability |
| `Exhibit_Assignment__c` | Sponsor-to-booth mapping | → Sponsor, → Exhibit_Space; status workflow (Pending → Confirmed → Cancelled) |
| `Logistics_Entry__c` | Task/checklist items | → Event; pillar (Venue, Catering, AV, Staffing, etc.); status (Ready/At Risk/Blocked) |
| `Logistics_Pillar_Status__c` | Aggregate readiness rollup | → Event; count fields (Ready, At Risk, Blocked), computed score (%) |
| `Portal_Contact_Role__c` | Portal access control | → Contact, → Sponsor, → Event; role-based access (Program, AV, Sponsorship, Registration) |
| `Event_Asset__c` | File/collateral with approval workflow | → Speaker or Sponsor; approval states (Draft → Submitted → In Review → Approved); stores ContentDocument IDs |
| `Sponsor_Benefit__c` | Contractual sponsor deliverables | → Sponsor; type (Table, Email List, Sponsored Talk, Ad); fulfillment status tracking |

### Key Apex Classes

| Class | Purpose |
|-------|---------|
| `PlannerRegistrationNotifier` | Monitors Attendee and Session_Attendee changes; publishes platform events for registration state changes (new reg, waitlist promotion, cancellation, attendance) |
| `PlannerRegistrationTriggerQueueable` | Consumes platform events; makes async HTTP POST to Planner UI `/api/email/triggers`; chunks into 50-item batches; chains remaining items |
| `PlannerSettings` | Hierarchy custom setting guard; org/profile/user-level kill switch for all triggers |
| `PlannerHealthController` | REST endpoint `POST /Planner/health`; validates event configuration (capacity, waitlist, campaign status) |

### Triggers (5)

1. `Attendee_PlannerNotifier` on `conference360__Attendee__c` (after insert/update)
2. `SessionAttendee_PlannerNotifier` on `conference360__Session_Attendee__c` (after insert/update)
3. `PlannerRegistrationNotificationTrigger` on platform event (after insert)
4. `Event_PlannerLifecycleNotifier` on `conference360__Event__c`
5. `PlannerLifecycleNotificationTrigger` on lifecycle platform event

### Platform Event: `Planner_Registration_Notification__e`

| Field | Purpose |
|-------|---------|
| `Attendee_Id__c` | Attendee record ID |
| `Event_Id__c` | Event record ID |
| `Change_Type__c` | Enum: ATTENDEE_REG, ATTENDEE_WAITLIST_PROMO, ATTENDEE_CANCEL, ATTENDEE_ATTENDANCE, SESSION_REG, SESSION_WAITLIST_PROMO, SESSION_CANCEL, SESSION_ATTENDANCE |
| `Hash__c` | SHA-256 deduplication hash |
| `Primary_Email__c` | Contact email (for lookup) |
| `Registration_Status__c` | Current status |

### Configuration

| Metadata | Purpose |
|----------|---------|
| `Planner_Trigger_Settings__mdt` | Master config: endpoint URL, tenant ID, worker token, named credential, template ID |
| `Planner_UI_Settings__c` (hierarchy) | Kill switch per user/profile/org; also stores OAuth state |
| `Blackthorn_Base_Settings__c` (hierarchy) | Feature flags: advanced visibility, Gen2 cache, contact trigger disable |

### REST API

- `POST /services/apexrest/Planner/health` — Event health check (capacity, remaining, attendee count, waitlist, campaign status)

### Outbound Integration

- `POST {Endpoint_URL}/api/email/triggers` — Async notification to Planner UI when registration events occur
  - Auth: Bearer token from `Worker_Token__c`
  - Payload: `{ tenantId, eventId, triggerType, attendees[], metadata }`

### Augmentations to Other Package Objects

Base adds fields to objects owned by Events and Payments:

- `conference360__Attendee_Data_Message__c`: +9 fields (Speaker, Sponsor, Session, Asset lookups; Channel, Delivery_Status picklists)
- `conference360__Event_Item__c`: +3 FMV fields (FMV_Amount, FMV_Computed, FMV_Percent)
- `conference360__Sponsor__c`: +8 fields (Complimentary quotas, Partner_Type, Payment_Method, Portal signup)
- `bt_stripe__Line_Item__c`: +1 field (FMV_Computed)
- `bt_stripe__Sales_Document__c`: +1 field (FMV_Computed)

---

## Blackthorn Payments (bt_stripe)

### Purpose

Comprehensive payment processing within Salesforce. Integrates Stripe (primary), Authorize.Net, and PayPal. Handles charges, refunds, subscriptions, invoices, disputes, Stripe Connect, and virtual terminal entry.

### Namespace: `bt_stripe__`

### Core Objects

| Object | Purpose | Key Fields |
|--------|---------|-----------|
| `Transaction__c` | Primary payment record (123+ fields) | Amount, Currency, Transaction_Status (Open/Process/Completed/Failed), Payment_Status (Pending/Authorized/Captured/Refunded), Key (Stripe charge ID), Error fields |
| `Payment_Method__c` | Customer payment instruments | Stripe_Payment_Method_ID, Type (Card/ACH), masked card/bank details, Default flag, Verified status |
| `Payment_Gateway__c` | Processor configuration | Provider (Stripe/AuthNet/PayPal), API keys, Webhook config, Balance, Livemode flag |
| `Stripe_Customer__c` | Stripe customer ↔ Salesforce Contact/Account | Stripe Customer ID, Contact/Account lookups |
| `Payment_Intent__c` | SCA (3D Secure) flows | Stripe Payment Intent ID, status |
| `Sales_Document__c` | Invoices/orders | Stripe Invoice ID, Status, Total, Due Date, Line Items |
| `Line_Item__c` | Invoice/order line items | Item name, quantity, unit price, total |

### Subscription & Billing Objects

| Object | Purpose |
|--------|---------|
| `Subscription2__c` | Recurring subscriptions (plan, method, status, billing interval, Stripe sub ID) |
| `Subscription_Item__c` | Individual items on subscriptions |
| `Subscription_Schedule__c` | Scheduled subscription phases |
| `Plan2__c` | Billing plans (interval, amount, Stripe plan ID) |
| `Gateway_SKU__c` | Product SKUs linked to Stripe products |
| `Usage__c` | Usage-based billing records |

### Stripe Connect Objects

| Object | Purpose |
|--------|---------|
| `Connected_Account__c` | Platform partner/merchant accounts |
| `Connected_Account_Owner__c` | Account owner records |
| `Stripe_Application_Fee__c` | Application fees on transfers |

### Supporting Objects

`Dispute__c`, `Dispute_Evidence__c`, `Webhook_Event__c`, `Checkout_Submission__c`, `Code__c` (promo codes), `Coupon2__c`, `Fee__c`, `Allocation__c`, `Virtual_Terminal_Settings__c`

### Key Apex Classes

**Transaction Processing:**

| Class | Purpose |
|-------|---------|
| `TransactionService` | Main service for transaction operations |
| `TransStripe` / `TransactionStripeQueueable` | Stripe-specific charge processing (async via Queueable) |
| `TransactionStripePayoutService` | Payout processing |
| `TransactionStripeTransferService` | Stripe Connect transfer handling |

**Stripe API Client:**

| Class | Purpose |
|-------|---------|
| `StripeAPI` | Primary REST client for all Stripe endpoints |
| `Stripe` | Data model classes (POJOs) for API deserialization — Customer, Charge, Card, BankAccount, Refund, PaymentIntent, Invoice, Subscription, Plan, Product, Transfer, Payout, Dispute |

**Billing:**

| Class | Purpose |
|-------|---------|
| `StripeInvoiceService` | Invoice CRUD |
| `StripePlanService` / `StripeProductService` | Plan and product management |
| `Subscription2Service` | Subscription lifecycle |

**Webhook Processing:**

| Class | Purpose |
|-------|---------|
| `REST_Webhook2` | REST endpoint for Stripe/AuthNet webhooks; HMAC signature verification |
| `WebhookService` | Event routing and processing |

### Stripe API Endpoints Used

```
Customers:       POST/GET/PUT/DELETE https://api.stripe.com/v1/customers
Charges:         POST/GET            https://api.stripe.com/v1/charges
Payment Intents: POST/GET/PUT        https://api.stripe.com/v1/payment_intents
Payment Methods: POST/GET/PUT        https://api.stripe.com/v1/payment_methods
Subscriptions:   POST/GET/PUT/DELETE https://api.stripe.com/v1/subscriptions
Invoices:        POST/GET/PUT        https://api.stripe.com/v1/invoices
Products:        POST/GET/PUT        https://api.stripe.com/v1/products
Plans:           POST/GET/PUT        https://api.stripe.com/v1/plans
Payouts:         POST/GET            https://api.stripe.com/v1/payouts
Transfers:       POST/GET            https://api.stripe.com/v1/transfers
Accounts:        POST/GET/PUT        https://api.stripe.com/v1/accounts
Disputes:        POST/GET/PUT        https://api.stripe.com/v1/disputes
```

### Charge Processing Flow

```
1. Create Transaction__c (Charge record type)
   Set: Amount, Payment_Method, Payment_Gateway, Authorize_Only or Capture
2. Trigger fires → TransactionStripeQueueable (async)
3. Queueable calls StripeAPI.charge() or StripeAPI.authorize()
4. Stripe response → update Transaction (Key, status, fees)
5. Transaction_RollupUpdatedBalance trigger → updates Payment_Gateway balance
6. Stripe sends webhook (charge.succeeded) → REST_Webhook2 → confirms status
```

### Refund Flow

```
1. Set Refund__c = true on original Transaction (or create child refund record)
2. Trigger → TransactionStripeQueueable → StripeAPI.refund()
3. Parent Transaction status → Partially Refunded or Refunded
4. Net amounts recalculated; balance rollups propagate
```

### Webhook Endpoint

- `POST /services/apexrest/bt_stripe/webhook/{label}`
- Signature verification: HMAC-SHA256 (Stripe) or HMAC-SHA512 (Authorize.Net)
- Creates `Webhook_Event__c` for audit trail
- Routes events to appropriate handlers (charge.succeeded, charge.failed, invoice.paid, etc.)

### LWC Components (20+)

- `blackthornVirtualTerminal` — Manual payment entry UI
- `createPaymentMethod` — Add card/bank account form
- `manageSubscription` suite (8 components) — Subscription dashboard
- `dataDictionaryEdit` — Field mapping editor
- `customLookup` / `customMultiObjectLookup` — Reusable lookups

### Permission Sets (7)

- `payment360_Adminv2` — Full admin access
- `payment360_Managerv2` — Manager-level
- `payment360_Userv2` — Standard user
- `Stripe_Billing` — Subscription/invoice features
- `Blackthorn_Payments_Community_User` — Portal access
- `Blackthorn_Payments_Lite_User` — Read-only
- `Blackthorn_Payments_Webhook_Event_Admin` — Webhook management

### Configuration

| Metadata | Purpose |
|----------|---------|
| `Stripe_Settings__c` (org defaults) | Enable SCA, Enable Billing, Livemode, API Version |
| `Stripe_Platform_Credential__mdt` | Platform-level credentials |
| `Protected_Key__mdt` | Encrypted API keys |
| `Webhook_Secret__mdt` | Webhook signing secrets (label → secret) |
| `Stripe_Currency_Setting__mdt` | Currency support and minimum amounts |
| `Stripe_Metadata_Mapping__mdt` | Field mappings between SF and Stripe |

---

## Blackthorn Events (conference360)

### Purpose

Core event management package. Provides the full lifecycle: event creation, session scheduling, speaker management, attendee registration, ticket sales, forms, email communications, campaign sync, and reporting. This is the largest and most complex package.

### Namespace: `conference360__`

### Dependencies

- Blackthorn Base (`bt_base__`) v1.46+
- Blackthorn Payments (`bt_stripe__`) v6.48+

### Core Objects

| Object | Purpose | Key Fields |
|--------|---------|-----------|
| `Event__c` | Master event record (199 fields) | Name, Status, Start/End Date, Attendee Limit, Currency, Campaign Link, Custom CSS, Timezone, Email Templates |
| `Session__c` | Sessions within events (70+ fields) | Event, Start/End DateTime GMT, Max Registrants, Remaining Seats, Join URL (virtual), Track |
| `Attendee__c` | Event attendees (100+ fields) | Event, Contact/Lead, Email, Registration Status, Attendance Status, Event Item (ticket), Dietary Preference |
| `Session_Attendee__c` | Junction: Session ↔ Attendee | Session, Attendee, Registration Status, Attendance Status |
| `Event_Item__c` | Ticket types/offerings | Event, Name, Price, Quantity, Remaining, Waitlist capacity, linked Form |
| `Event_Item_Purchase__c` | Ticket purchase records | Attendee, Event Item, Quantity, Price, Sales Document |
| `Speaker__c` | Speakers/presenters | Name, Bio, Image URL, Keywords |
| `Session_Speaker__c` | Junction: Session ↔ Speaker | Session, Speaker, Role/Title |
| `Sponsor__c` | Event sponsors | Name, Account, Image, Sponsorship Level |

### Form Objects

| Object | Purpose |
|--------|---------|
| `Form__c` | Registration/survey form definitions |
| `Form_Element__c` | Individual form questions (type, required, order, conditional logic) |
| `Form_Submission__c` | Submission instances |
| `Form_Submission_Answer__c` | Individual question answers |
| `Form_Big_List_Group__c` / `Form_Big_List_Option__c` | Large picklist storage (1000+ options) |

### Supporting Objects

| Object | Purpose |
|--------|---------|
| `Event_Registration_Submission__c` (ERS) | Checkout cart/session draft; stores full cart payload as JSON |
| `Track__c` / `Track_Session__c` / `Track_Attendee__c` | Event tracks/agendas |
| `Attendee_Group__c` | Team registrations |
| `Waitlist__c` | Waitlist records |
| `Table__c` / `Seat__c` | Physical seating |
| `Email_Template__c` | Custom email templates (Bee builder integration) |
| `Event_Content__c` | Event page content blocks |
| `Event_FAQ__c` | FAQ entries |
| `Event_Group__c` / `Event_Group_Association__c` | Multi-event groups |
| `Budget_Expense__c` / `Expense_Entry__c` | Budget tracking |
| `Hotel_Room_Block__c` / `Hotel_Room__c` / `Flight__c` | Travel/accommodation |
| `Recurring_Events__c` | Recurring event series templates |
| `Badge_Printing_Configuration__c` | Badge printing setup |
| `Mobile_Check_In_Submission__c` | Mobile check-in records |

### Key Apex Classes

**Registration & Checkout:**

| Class | Purpose |
|-------|---------|
| `CheckoutAPI` | Main checkout orchestrator: validates ERS payloads, calculates pricing, applies discounts, manages duplicate detection, calls Payments |
| `Checkout` | Serializable data model for checkout payloads |
| `CheckoutSubmission_ProcessAttendees` | Queueable: creates Attendee records + Event Item Purchases after checkout |
| `REST_Events` | REST endpoint `/eventRegistrationSubmission` — accepts checkout payloads |

**Selectors & Services:**

| Class | Purpose |
|-------|---------|
| `EventSelector2` / `AttendeeSelector` / `SessionSelector` | Query builders (fflib-inspired selector pattern) |
| `SessionService` | Session business logic: rollup counts, capacity, timezone adjustments |
| `RecurringEventService` | Recurring event series creation and cloning |
| `BudgetExpenseService` | Budget tracking and expense rollups |

**Email & Communication:**

| Class | Purpose |
|-------|---------|
| `EmailTemplateHelper` | Template management, merge field validation, Bee builder integration |
| `SendMassEmailBatch` | Batch job for mass email sends |
| `FetchEmailStatsBatch` | Retrieves SendGrid email statistics |

**External Integrations:**

| Class | Purpose |
|-------|---------|
| `ZoomAPI` / `WAWebex` | Webinar creation and attendee sync |
| `AttendeeAddToWebinarBatch` | Syncs attendees to Zoom/Webex/GoToWebinar |
| `CacheDataSyncBatch` | Syncs event data to external Capacity Service |
| `NotifyPlaformToRefreshCacheQueueable` | Cache invalidation for external platforms |

### Triggers (51)

Organized by domain:

- **Event lifecycle:** Event_Trigger, EventContent_Trigger, EventFAQ_Trigger, EventSettings_Trigger, EventGroupAssociation_Trigger, RecurringEvent_Trigger
- **Attendee/Registration:** Attendee_Trigger, SessionAttendee, Waitlist_Trigger, AttendeeDataMessage_Trigger
- **Forms:** Form, FormElement, FormElementCondition, FormSubmission_Trigger, FormBigListGroup, FormBigListOption
- **Checkout/Payment:** CheckoutSubmission_Trigger, CodeEligibility_Trigger, PaymentGateway_Trigger, Fee_Trigger
- **Sessions/Speakers:** Session_Trigger, SessionSpeaker_Trigger, SessionKeyword_Trigger, Speaker_Trigger
- **Campaign sync:** Campaign_Trigger, CampaignMember_Trigger
- **Other:** Contact_Trigger, Lead_Trigger, User_Trigger, EmailTemplateTrigger, DataDictionaryEntry_Trigger, etc.

### Flows (8)

| Flow | Purpose |
|------|---------|
| `Send_Blackthorn_Event_confirmation_email` | Confirmation on registration |
| `Send_Blackthorn_Event_invite_email` | Attendee invitations |
| `Send_Blackthorn_Event_Reminder_email` | Pre-event reminders |
| `Send_the_Waitlisted_Email` | Waitlist notification |
| `Send_the_removed_from_the_Waitlist_Email` | Waitlist promotion |
| `Send_Cancelled_Registration_Email` | Cancellation notices |
| `Blackthorn_Events_ERS_Failed` | Failed checkout error notification |
| `Blackthorn_Events_WebinarService_Failed` | Webinar sync error handling |

### REST API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/eventRegistrationSubmission` | POST | Main checkout (accepts ERS payload, returns Sales Document with pricing) |
| `/sessionRegistration` | POST | Session-specific registration |
| `/formSubmission` | POST | Form submission |
| `/sessionAttendee` | GET/POST | Session attendee operations |
| `/events` | GET/POST | Event CRUD |
| `/mobileCheckIn` | POST | Mobile app check-in |

### Registration Checkout Flow (Detail)

```
1. REST_Events.onPost receives ERS payload
     └─ Contains: attendee data, contact info, ticket selections, form answers, promo code

2. CheckoutAPI.validateERS()
     ├─ Duplicate email detection
     ├─ Capacity validation (per ticket type)
     ├─ Promo code validation (bt_stripe__Code__c eligibility)
     └─ Calls Payments checkout → creates bt_stripe__Sales_Document__c + bt_stripe__Transaction__c

3. Event_Registration_Submission__c upsert (status: Draft)

4. User confirms → ERS status = "To Process"

5. CheckoutSubmission_Trigger fires
     └─ Enqueues CheckoutSubmission_ProcessAttendees (Queueable)

6. CheckoutSubmission_ProcessAttendees:
     ├─ Creates conference360__Attendee__c records
     ├─ Creates conference360__Event_Item_Purchase__c records
     ├─ Links Contact (creates new if email not found)
     ├─ Fires email automation flows
     └─ ERS status = "Completed"

7. Attendee_PlannerNotifier trigger (from Base) → publishes platform event
     └─ PlannerRegistrationTriggerQueueable → HTTP POST to Planner UI
```

### LWC Components (159)

Major component groups:
- **Event Builder Wizard** (`ebWizard*` suite, ~30 components) — Step-by-step event creation
- **Email** (`emailTemplateCreationForm`, `emailPreview`, `emailComponentLibrary`)
- **Forms** (`attendeeForm`, `customQuestion`, `formSubmission`)
- **Tables & Lists** (`attendeePreviewTable`, `eventTableView`, `eventDetailsCard`)
- **Utilities** (`customLookup`, `comboboxAutocomplete`, `confirmModal`)

### Permission Sets (7)

- `Blackthorn_Events_Admin` — Full access
- `Blackthorn_Event_Organizer` — Event management
- `Blackthorn_Events_Lite_User` — Limited organizer
- `Blackthorn_Events_ReadOnly` — Read-only
- `Blackthorn_Events_Limited_Access` — External users
- `Blackthorn_Events_Community_Guest_User` — Experience Cloud guest
- `Blackthorn_Events_Community_Platform_User` — Experience Cloud authenticated

### Third-Party Integrations

| Service | Purpose |
|---------|---------|
| **Zoom** | Webinar creation, registrant sync |
| **Webex** | Webinar creation, attendee sync |
| **GoToWebinar** | Webinar integration |
| **Auth0** | SSO/identity provider for portals |
| **Cloudinary** | Image hosting and optimization |
| **SendGrid** | Email delivery and statistics |
| **Slack / Microsoft Teams** | Auto-create chat channels for events/sessions |
| **Capacity Service** | External capacity/inventory state cache |

---

## Events Webapp

### Purpose

Public-facing event registration and ticketing portal. Attendees use this to browse events, view sessions, select tickets, fill registration forms, and complete payment checkout.

### Tech Stack

| Layer | Technology |
|-------|-----------|
| **Client** | Angular 16.2.12, TypeScript, Angular Material, SCSS |
| **Server** | Express.js 4.19, TypeScript, Nunjucks templates |
| **Worker** | BullMQ 5.1 (background job queue) |
| **Cache** | Redis (ioredis 5.3) with Redlock for distributed locks |
| **Payments** | Stripe.js (client-side), stripe v16.8 (server-side) |
| **Auth** | Passport.js, AWS JWT Verify, simple-oauth2 |
| **Schema** | Connect360 (@blackthornio/schema-migrate) |
| **Package Manager** | pnpm 10.24 |
| **Testing** | Jest, Cypress, Playwright |

### URL Structure

```
https://events.blackthorn.io/{compactOrgId}/{eventNameSlug}-{compactEventId}
```

### Routes

| Route | Purpose |
|-------|---------|
| `/g/:groupslug` | Event group landing page (event listing) |
| `/g/:groupslug/:eventslug` | Individual event details |
| `/c` or `/d/:groupslug` | Calendar view |
| `/s/:surveyId` | Post-event survey |
| `/a/:code` | Attendee secure link (ticket view) |
| `/preview` | Event preview mode |

### Event Details Sub-Routes

Session browsing → Ticket selection → Pre-checkout form (attendee info) → Cart review → Checkout → Payment → Confirmation

### Salesforce Integration

- **Primary:** Salesforce Composite API, UI API, REST API
- **Schema Management:** Connect360 (schema migration framework)
- **Real-time Sync:** Webhook-based cache refresh

**Data Flow:**
1. Salesforce changes trigger webhook to webapp
2. Webhook validates org ID and payload
3. Creates cache refresh job via BullMQ
4. Worker updates event cache in Redis/memory
5. Client fetches fresh data on next request

### Payment Integration

**Stripe (primary):**
- Client-side: Stripe Elements for PCI-compliant card entry
- Server-side: stripe v16.8 for tokenization and charge creation
- Components: `StripeCheckoutComponent` (modal) + `StripeFormComponent` (embedded)
- Multi-currency support

**Legacy:**
- Touchnet/CashNet via SOAP integration

### Form Rendering

**Supported question types:**
- text, long-text, email, url, number, date
- checkbox, select, multi-select, picklist
- file upload, hidden, parameter, divider
- big list group (grouped selection for large datasets)

**Features:**
- Conditional visibility rules (show/hide based on conditions)
- Dynamic field loading based on ticket selection
- Real-time validation
- Internationalization (multi-language labels)

### Theming System

- `BtThemeService` — Injectable, RxJS-based theme service
- CSS custom properties injected at runtime (~50+ variables)
- Per-event branding: primary/accent colors, logo, custom CSS, font selection
- Responsive breakpoints observable (mobile-sm < 400px, mobile < 600px, tablet 600-959px, desktop 960px+)
- Dark mode support via `prefers-color-scheme`

### Multi-Language Support

- 30+ languages via `SUPPORTED_LANGUAGES`
- ICU Message Formatting for complex pluralization
- Locale detection: URL → document.lang → browser preference
- Dynamic dictionary loading per locale
- Angular locale data for date/number/currency formatting

### Key Services

| Service | Purpose |
|---------|---------|
| `EventService` | Event CRUD, caching, filtering |
| `ShoppingCartService` | Cart state management |
| `CheckoutService` / `CheckoutV2Service` | Checkout orchestration |
| `BillingService` | Payment processing, price calculation |
| `PeopleService` | Attendee validation, profiles |
| `LanguageService` | i18n, locale detection |
| `BtThemeService` | Dynamic theming, responsive breakpoints |
| `TicketService` | Ticket availability, capacity |
| `TrackingService` | GA, LinkedIn, Twitter event tracking |

### Performance

- Lazy-loaded Angular modules by feature
- Virtual scrolling for large lists
- Image lazy loading (lazysizes)
- Redis caching for Salesforce metadata
- BullMQ job prioritization for cache refresh
- Code splitting via Webpack

### Embed Options

The webapp can be embedded in external sites:
- Direct link (standalone page)
- Iframe embed (`docs/embed-iframe.md`)
- Programmatic embed API (`docs/embed-api.md`)

---

## Cross-Package Data Flows

### 1. Charge Creation (Events → Payments → Stripe)

```
Events: CheckoutAPI validates cart
  → Payments: Creates Sales_Document__c + Line_Item__c records
  → Payments: Creates Transaction__c (Charge)
  → Payments: TransactionStripeQueueable → StripeAPI.charge()
  → Stripe: Processes charge, returns response
  → Payments: Updates Transaction status + fees
  → Payments: Stripe webhook confirms (charge.succeeded)
  → Events: Links Sales Document to ERS and Attendee records
```

### 2. Registration Notification (Events → Base → Planner UI)

```
Events: Attendee__c created/updated
  → Base: Attendee_PlannerNotifier trigger fires
  → Base: PlannerRegistrationNotifier detects state change
  → Base: Publishes Planner_Registration_Notification__e platform event
  → Base: PlannerRegistrationTriggerQueueable HTTP POST
  → Planner UI: /api/email/triggers receives notification
  → Planner UI: Triggers confirmation email via SendGrid
```

### 3. Promo Code Validation (Events ↔ Payments)

```
Events: CheckoutAPI receives promo code in cart
  → Payments: Validates bt_stripe__Code__c eligibility rules
  → Payments: Calculates discount amount
  → Events: Applies discount to pricing; stores in Sales Document
```

### 4. Webhook Round-Trip (Stripe → Payments → Events)

```
Stripe: Sends charge.succeeded webhook
  → Payments: REST_Webhook2 verifies HMAC signature
  → Payments: WebhookService routes event
  → Payments: Updates Transaction__c status
  → Events: (via trigger rollups) Updates ERS status if applicable
```

### 5. Campaign Sync (Events ↔ Salesforce Standard)

```
Salesforce: Campaign record linked to Event
  → Events: CampaignSyncWithEventController orchestrates
  → Events: AttendeeImportToEventBatch imports CampaignMembers as Attendees
  → Events: CampaignMemberStatusSyncBatch syncs attendance back to CampaignMembers
```

### 6. Webapp ↔ Salesforce (Events Webapp → Events Package)

```
Webapp: User selects tickets, fills form, submits
  → Express server: Validates, calls Salesforce REST API
  → Events: REST_Events.onPost processes ERS
  → Events: CheckoutAPI validates and prices
  → Payments: Creates Sales Document + Transaction
  → Stripe: Processes payment
  → Events: Creates Attendee records
  → Webapp: Receives confirmation, displays to user
```

---

## Key Integration Patterns

### Pattern 1: Declarative Trigger Processing (Payments)

Payments uses "declarative checkboxes" on Transaction__c. Setting `Capture__c = true` triggers the `Transaction_TriggerDeclarativeProcessing` trigger, which enqueues the Stripe API call. This lets admins process payments by simply updating a checkbox field.

### Pattern 2: Platform Events for Decoupling (Base)

Base uses Salesforce Platform Events to decouple event detection from processing. The Attendee trigger publishes an event, and a separate trigger on the platform event channel consumes it and makes the HTTP callout. This avoids mixed DML and governor limit issues.

### Pattern 3: ERS as Durable Cart (Events)

The Event Registration Submission (ERS) record stores the entire checkout cart as JSON. This enables:
- Cart persistence across sessions
- Retry on processing failure (status: Failed → reprocess)
- Audit trail of what was submitted
- Decoupled validation (validate first, process later)

### Pattern 4: Webhook-Driven Cache Refresh (Webapp)

The webapp doesn't poll Salesforce. Instead, Salesforce sends webhooks on data changes, which queue BullMQ jobs to refresh the Redis cache. The webapp always reads from cache, ensuring fast response times.

### Pattern 5: Queueable Chaining (Base, Payments)

Both Base and Payments use Queueable chaining for processing large batches. Items are chunked (50 per batch), processed, and remaining items are enqueued into a new Queueable. This respects Salesforce governor limits while ensuring all items are processed.

### Pattern 6: Feature Gating via Hierarchy Settings

Both Base (`Planner_UI_Settings__c`) and Payments (`Stripe_Settings__c`) use hierarchy custom settings for feature flags. This allows kill switches at org, profile, or user level without code deployment.

### Pattern 7: Selector Pattern for Queries

Events uses a selector pattern (`EventSelector2`, `AttendeeSelector`, `SessionSelector`) that encapsulates SOQL queries and field lists. This centralizes query logic, makes it testable, and prevents field list drift across the codebase.

---

## Object Relationship Map

```
conference360__Event__c (MASTER)
│
├── conference360__Session__c (many)
│   ├── conference360__Session_Speaker__c → Speaker__c
│   ├── conference360__Session_Attendee__c → Attendee__c
│   ├── conference360__Track_Session__c → Track__c
│   └── Form__c (session registration form)
│
├── conference360__Event_Item__c (tickets, many)
│   ├── conference360__Event_Item_Purchase__c → Attendee__c
│   └── Form__c (ticket registration form)
│
├── conference360__Attendee__c (many)
│   ├── → Contact / Lead (Salesforce standard)
│   ├── → Event_Item__c (ticket type)
│   ├── → Attendee_Group__c
│   ├── conference360__Form_Submission__c → Form_Submission_Answer__c
│   └── bt_stripe__Sales_Document__c → bt_stripe__Transaction__c
│
├── conference360__Speaker__c (many)
│   └── bt_base__Event_Asset__c (presentations, etc.)
│
├── conference360__Sponsor__c (many)
│   ├── bt_base__Exhibit_Assignment__c → bt_base__Exhibit_Space__c
│   ├── bt_base__Sponsor_Benefit__c
│   ├── bt_base__Event_Asset__c (logos, documents)
│   └── bt_base__Portal_Contact_Role__c → Contact
│
├── conference360__Form__c (many)
│   └── conference360__Form_Element__c (questions)
│
├── conference360__Email_Template__c (many)
│
├── conference360__Event_Registration_Submission__c (many)
│   └── → bt_stripe__Sales_Document__c
│
├── bt_base__Logistics_Entry__c (many)
│   └── bt_base__Logistics_Pillar_Status__c (aggregation)
│
├── bt_base__Exhibit_Space__c (many)
│
├── bt_base__Email_Blast__c (many)
│
├── conference360__Budget_Expense__c (many)
│   └── conference360__Expense_Entry__c
│
├── conference360__Event_Group_Association__c → Event_Group__c
│
└── Campaign (standard, optional link)
    └── CampaignMember ↔ Attendee (bidirectional sync)
```

---

## Quick Reference: API Names

### Events Package (conference360__)
- `conference360__Event__c`
- `conference360__Session__c`
- `conference360__Attendee__c`
- `conference360__Session_Attendee__c`
- `conference360__Event_Item__c`
- `conference360__Event_Item_Purchase__c`
- `conference360__Speaker__c`
- `conference360__Session_Speaker__c`
- `conference360__Sponsor__c`
- `conference360__Form__c`
- `conference360__Form_Element__c`
- `conference360__Form_Submission__c`
- `conference360__Form_Submission_Answer__c`
- `conference360__Event_Registration_Submission__c`
- `conference360__Email_Template__c`
- `conference360__Track__c`
- `conference360__Waitlist__c`
- `conference360__Attendee_Group__c`

### Payments Package (bt_stripe__)
- `bt_stripe__Transaction__c`
- `bt_stripe__Payment_Method__c`
- `bt_stripe__Payment_Gateway__c`
- `bt_stripe__Stripe_Customer__c`
- `bt_stripe__Sales_Document__c`
- `bt_stripe__Line_Item__c`
- `bt_stripe__Subscription2__c`
- `bt_stripe__Plan2__c`
- `bt_stripe__Code__c`
- `bt_stripe__Dispute__c`
- `bt_stripe__Connected_Account__c`
- `bt_stripe__Webhook_Event__c`

### Base Package (bt_base__)
- `bt_base__Email_Blast__c`
- `bt_base__Exhibit_Space__c`
- `bt_base__Exhibit_Assignment__c`
- `bt_base__Logistics_Entry__c`
- `bt_base__Logistics_Pillar_Status__c`
- `bt_base__Portal_Contact_Role__c`
- `bt_base__Event_Asset__c`
- `bt_base__Sponsor_Benefit__c`

### Platform Events
- `bt_base__Planner_Registration_Notification__e`

---

## Appendix: Schema Data Model Reference

> Derived from the XML schema files in `xml schemas/`. These schemas define the Salesforce metadata for all custom objects across the platform.
>
> This appendix describes the **data model shape and relationships** — enough for an LLM or developer to understand how objects relate and what each package manages. For exact field definitions, consult the schema XMLs directly.

---

### Schema: Blackthorn Base (`bt_base`) — 23 Objects

**Active Objects:**

| Object | Field Count | Purpose | Key Relationships |
|--------|-------------|---------|-------------------|
| `Branding_Setting__c` | 17 | Store/webapp theming: logo, colors, language selector, custom footer links/URLs, theme selection | Standalone config record |
| `Rule__c` | 10 | Visibility/access rules with AND/OR/Custom logic, active flag, account-level extension | Parent of Rule_Condition__c |
| `Rule_Condition__c` | 5 | Individual rule criteria: field, operator (11 comparison types), value, evaluation order | MasterDetail → Rule__c |
| `Translation__c` | 1 | Multi-language support (50+ language picklist) | Standalone |
| `SCH_Schedule__c` | 16 | Smart Scheduler: base/related object targeting, offset (before/after by days/hours/minutes), status lifecycle | Parent of Actions, Executions, Delta Requests |
| `SCH_Schedule_Action__c` | 16 | Email and SMS actions on schedules (template IDs, from addresses, HTML body, SMS message) | MasterDetail → Schedule |
| `Schedule_Execution__c` | 11 | Execution instances with status tracking | MasterDetail → Schedule |
| `Schedule_Execution_Log__c` | 16 | Per-action execution logs (email/SMS delivery SIDs, status) | MasterDetail → Schedule Action + Execution |
| `Schedule_Delta_Request__c` | 5 | Failed sync retry queue (Create/Re-calculate/Archived request types) | MasterDetail → Schedule |
| `Blackthorn_Feature_Toggle__c` | 3 | Feature flags with activation/deactivation datetime windows | Standalone |
| `Protected_Key__c` | 2 | API key storage (protected visibility — only Blackthorn can view/edit) | Standalone |
| `BT_Keyword__c` | 2 | Categorized keywords (Association, City, Department, Industry, Interest, Location, State, Type) | Standalone |
| `Form_Question_Map_To_Object__c` | 1 | Object API name for form field mapping targets | Standalone |

**Custom Settings (Hierarchy):**

| Setting | Fields | Purpose |
|---------|--------|---------|
| `Blackthorn_Base_Settings__c` | 4 | OAuth state tracking, contact trigger disable |
| `Blackthorn_Base_Settings_Protected__c` | 5 | Data persistence config, advanced visibility toggle, Gen2 cache |
| `Blackthorn_Schedule_Config__c` | 8 | Smart Scheduler: API keys, URL, SendGrid key, delta sync chunk size, OrgWide Email |

**Deprecated** (7 objects — moved to Events package): Form, Form Element, Form Element Condition, Form Submission, Form Submission Answer, Form Big List Group, Form Big List Option. These share the same field shapes as their Events counterparts (question types, map-to-object/field, conditional logic).

---

### Schema: Blackthorn Payments (`bt_stripe`) — 57 Objects

#### Core Data Model Concepts

The Payments package models a standard payment processing pipeline:

- **Gateway** → configures which payment processor to use and stores credentials
- **Customer** → links a Salesforce Contact/Account/Lead to a payment processor customer
- **Payment Method** → stores tokenized card/bank details (never raw card numbers)
- **Transaction** → the central record for charges, refunds, payouts, and transfers
- **Invoice (Sales Document)** → line-item-level billing with payment tracking
- **Subscription** → recurring billing tied to a plan/price

#### Key Object Shapes

**Transaction__c** (~122 fields) — Central payment record. Contains:
- Amount fields (amount, net, retained revenue, application fee) with currency ISO
- Status lifecycle: Open → Process → Completed/Failed, with separate Payment Status (Authorized → Captured → Refunded)
- Declarative processing via checkboxes (Authorize, Capture, Refund) that trigger Stripe API calls
- Self-referential lookups for refund→parent and reversal→original chains
- Relationships to: Payment Method, Payment Gateway, Invoice, Connected Account, Payment Intent, Payment Schedule, Customer, Checkout Submission
- Stripe integration fields: charge/intent ID, customer ID, card ID, transfer group
- Error tracking: code, message, type, param
- Scheduling: Date_To_Process for deferred charges, reattempt flag for retries
- Source tracking: where the transaction originated (UI, Virtual Terminal, API, Event, Subscription, etc.)

**Payment_Method__c** (~62 fields) — Tokenized payment instruments. Contains:
- Stripe Payment Method ID (never raw card data)
- Type (card, ACH, various alternative methods), brand, status lifecycle
- Masked card details (last 4 only), expiry, cardholder name
- Bank account fields for ACH (masked, routing number, holder type, verification status)
- Links to: Customer, Gateway, Account, Contact

**Payment_Gateway__c** (~54 fields) — Processor configuration. Contains:
- Provider selection, API credentials (access token, publishable key)
- Webhook configuration (label, secret)
- Balance tracking (available, pending, total)
- Currency defaults and accepted payment method multiselects
- Test mode flag

**Sales_Document__c / Invoice** (~92 fields) — Full invoicing. Contains:
- Document type (Invoice, Quote, Order, Sales Receipt, Credit Note)
- Status lifecycle and payment status tracking
- Payment terms (Net 7 through Net 90)
- Full Bill To/Ship To address sets
- Links to: Account, Contact, Gateway, Payment Method, Subscription
- Stripe invoice ID sync

**Line_Item__c** (~39 fields) — Invoice line items with: unit price, quantity, discount amount, tax amount, total, balance due. Links to Invoice, Product, Plan/Price, Code, Subscription.

**Subscription2__c** (~53 fields) — Recurring billing with: status lifecycle (Trialing → Active → Past Due → Canceled), billing method (auto-charge vs send-invoice), period tracking, cancellation scheduling. Links to Customer, Plan, Payment Method.

**Code__c** (10 fields) — Promo/discount codes with: type (Discount, Access-Promo, Source), discount amount/percentage, quantity tracking (available/claimed/remaining formula), validity dates.

**Connected_Account__c** (~51 fields) — Stripe Connect marketplace accounts with: account type (Standard/Express/Custom), entity type, charges/payouts enabled flags, balance tracking, verification status.

**Other Notable Objects:**

| Object | Purpose |
|--------|---------|
| `Payment_Intent__c` (~10 fields) | SCA/3D Secure flows with status lifecycle and capture method |
| `Stripe_Customer__c` (~35 fields) | Gateway customer records linking SF Account/Contact/Lead with full address sets |
| `Plan2__c / Stripe_Price__c` (~18 fields) | Pricing plans: interval, billing scheme (per-unit/tiered), usage type (licensed/metered) |
| `Dispute__c` (~18 fields) | Payment disputes with reason categories and status lifecycle |
| `Dispute_Evidence__c` (~34 fields) | Evidence documents for dispute resolution |
| `Webhook_Event__c` (~22 fields) | Incoming webhook audit trail with links to affected records |
| `Fee__c` (4 fields) | Tax and processing fee definitions |
| `Checkout_Submission__c` (7 fields) | Cart state for checkout API (JSON payload, status) |
| `Payment_Schedule__c` (~30 fields) | Scheduled/recurring payment definitions |
| `Allocation__c` (5 fields) | Fund allocation tracking |
| `Stripe_Coupon__c` (~15 fields) | Coupon management (amount/percent off, duration, redemption limits) |

**Configuration Layer:**
- Hierarchy custom settings for trigger enable/disable (~83 flags), retry config, mobile config, relationship defaults
- Custom metadata for currency settings, Connect country specs, field mappings, webhook secrets, encrypted credentials

---

### Schema: Blackthorn Events (`conference360`) — 64 Objects

#### Core Data Model Concepts

The Events package models a complete event management lifecycle:

- **Event** → master record with capacity, dates, branding, budget, and email config
- **Session** → time-slotted activities within an event with independent capacity
- **Attendee** → registration records linking Contact/Lead to an Event via a Ticket
- **Event Item (Ticket)** → purchasable offerings with pricing, quantity, and visibility rules
- **Form** → configurable question sets for registration, surveys, and custom data collection
- **Speaker / Sponsor** → event stakeholder records with profile data
- **ERS (Event Registration Submission)** → durable checkout cart storing the full JSON payload

#### Key Object Shapes

**Event__c** (~194 fields) — The master record. Key field categories:
- **Identity:** name, status lifecycle (Draft → Published → Active → Completed → Canceled), type (In Person/Online/Hybrid), category
- **Dates/Time:** start/end date and time, timezone (IANA), cancellation deadlines
- **Capacity:** attendee limit with buffer, waitlist toggle, capacity threshold
- **Rollup Counts:** registered, attended, waitlisted, invited, canceled, no-show, pending, remaining (formula)
- **Branding:** custom CSS URL, image/logo URLs, primary color, theme selection, display density
- **Forms:** pre-registration, post-registration, and post-event survey form lookups; attendee constraint JSON (Optional/Required/Hide per field)
- **Email:** template lookups for confirmation, invite, cancellation, waitlist; contact email
- **Financial:** currency, discount, budget with category breakdowns (AV, catering, decor, etc.), budget variance formula
- **Relationships:** Campaign (standard), Event Group, Payment Gateway (2: primary + donations), Recurring Event template, Event Settings

**Session__c** (~66 fields) — Contains: MasterDetail to Event, GMT date/times, capacity with remaining seats formula, room/location, virtual join URL, main stage flag, form lookup, track lookup, attendee count rollups matching Event pattern.

**Attendee__c** (~104 fields) — Contains: Event and Contact/Lead lookups, ticket (Event Item) link, email, name fields with full name formula, registration status lifecycle (Registered/Pending/Waitlisted/Invited/Canceled/Declined/Checked In/Transferred/No Show), attendance type and status, dietary preference, full address, encrypted ID for secure links, marketing opt-in, contact sync control.

**Event_Item__c** (~68 fields) — Tickets. Contains: MasterDetail to Event, price, quantity with remaining formula, waitlist capacity, type (Guest/Donation/Product/Custom), status, visibility (Public/Private/Hidden), min/max quantity per order, form lookup, session link for session-specific tickets, attendee constraint fields matching Event pattern.

**Event_Settings__c** (~116 fields) — Per-event configuration covering: payment gateway and accepted methods, email automation (from address, templates, send toggles), registration rules (waitlist, approval, group registration, max tickets), checkout options (order summary, promo codes, donations, terms & conditions), attendee constraints (~15 field-level Optional/Required/Hide controls).

**Form__c** (~10 fields) + **Form_Element__c** (~21 fields) — Configurable forms with: question text, type (14 types including text, picklist, multi-select, file upload, big list group, checkbox, date, divider, hidden, parameter), required flag, sort order, picklist values, default values, hint/placeholder, map-to-object and map-to-field for Salesforce writeback, supplemental rich text (terms & conditions). Conditional logic via Form_Element_Condition__c (Contains/Equals operators, controlling/next element lookups).

**Event_Registration_Submission__c** (~11 fields) — Durable checkout cart: Event lookup, Contact lookup, status (Draft/To Process/Completed/Failed), Form_JSON (131KB LongTextArea storing full cart payload), Sales Document and Transaction lookups to Payments objects, indexed Key field, error field.

**Speaker__c** (~29 fields), **Sponsor__c** (~13 fields) — Profile records with: name, bio, image URL, contact/account links, social media URLs, sponsorship level (for sponsors), sort order.

**Email_Template__c** (4 fields) — Event email templates with: Event lookup, Bee email builder JSON payload (split across two 131KB LongTextArea fields), indexed key.

**Session_Attendee__c** (~27 fields) — Junction record with: MasterDetail to Session, Attendee lookup, independent registration and attendance status, Event Item link, check-in datetime.

**Waitlist__c** (~8 fields) — Waitlist tracking with: Attendee and Event Item lookups, status (Active/Promoted/Expired/Canceled), join and promoted dates, position number.

**Other Notable Objects:**

| Object | Purpose |
|--------|---------|
| `Track__c` / `Track_Session__c` / `Track_Attendee__c` | Event agendas/tracks with session and attendee junction tables |
| `Event_Item_Session__c` | Ticket-to-session mapping (which sessions a ticket grants access to) |
| `Event_Group__c` / `Event_Group_Association__c` | Multi-event bundles with branding and slug |
| `Attendee_Group__c` | Team/group registration containers |
| `Event_Content__c` | Event page content blocks |
| `Event_FAQ__c` | FAQ entries with question/answer, sort order, categories |
| `Event_Keyword__c` | Event/session tagging |
| `Event_Ad__c` | Sponsor ad placements |
| `Budget_Expense__c` / `Expense_Entry__c` | Budget tracking with category-level line items |
| `Hotel_Room_Block__c` / `Hotel_Booking__c` | Hotel accommodation management |
| `Table__c` / `Seat__c` | Physical seating layout |
| `Recurring_Events__c` | Recurring event series templates |
| `Badge_Printing_Configuration__c` + `Detail__c` | Badge template design |
| `Staff__c` / `Session_Staff__c` | Event staff assignments |
| `Mobile_Check_In_Submission__c` | Mobile app check-in records |
| `Event_Attendee_Data__c` | Enriched attendee data snapshots |
| `Attendee_Data_Message__c` | Attendee communication records |
| `Event_User_Identity__c` | Attendee auth/identity (Auth0 integration) |
| `Form_Big_List_Group__c` / `Form_Big_List_Option__c` | Large picklist storage (1000+ options) |
| `Form_Submission__c` / `Form_Submission_Answer__c` | Form response storage |
| `Webinar_Account__c` | Zoom/Webex account configuration |
| `Data_Sync_Retry__c` | Failed data sync retry queue |

**Configuration Layer:**
- Hierarchy custom settings: org defaults (~32 fields: attendee constraints, form settings, display prefs), protected settings (~10 fields: external service URLs/keys), email settings (~6 fields: batch size, from address), per-user preferences
- Custom metadata: email builder (Bee) credentials, image hosting (Cloudinary) credentials, domain whitelist for embedding
