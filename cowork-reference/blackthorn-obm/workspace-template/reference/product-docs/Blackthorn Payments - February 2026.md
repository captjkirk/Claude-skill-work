# Blackthorn Payments - February 2026

Table of contents

## Welcome to Blackthorn Payments


Welcome to Blackthorn Payments
PCI Compliance
Important Technical Information for Admins
6

## Payments Quick Start Guide


Overview
Install Payments
Provide Users Access
9

### Payment Gateway Setup


Instructions
12

#### Connect to Stripe


Connect to Stripe in Test Mode
Test Your Stripe Payment Gateway
Set Up and Con gure Stripe Webhooks
17

#### Connect to Authorize.net


Create an Authorize.net Sandbox Account
Connect to Authorize.net in Test Mode
De ne the Gateway User ID
Test Your Authorize.net Payment Gateway
Set Up and Con gure Authorize.net Webhooks
Test Your Webhook Connection
29

#### Connect to Spreedly


Connect to Spreedly in Test Mode
Update Your Payment Gateway Page Layout
Create a Spreedly Payment Gateway
Test Your Spreedly Payment Gateway
35

### PayLink


Overview
Provide User Access
Con gure PayLink
SCA (Stripe, Required for European Customers)
40

#### Enable Stripe Checkout (Optional)


Instructions
Con gure the Payment Gateway
Add Permissions to Access Encrypted Data
Assign the Page Layout to the Corresponding Record Type
Con gure PayLink
45

## Payments Quick Start Guide


Virtual Terminal
46

### DocumentLink


Overview
Con gure DocumentLink Templates
Add the “Create Invoice” Button to the Opportunity Page Layout (Optional)
50

### Move Historical Data to Blackthorn


Start Here
51

#### Stripe


Overview
Instructions
Customers
Payment Methods
Charges / Refunds
Payouts
57

#### Authorize.net


Instructions
Automatically Move Historical Data
Manually Sync Your Data
60

#### Dataload Historical Transactions into Blackthorn


Instructions
Transactions
Payment Methods
Recreating Records
64

### FSL Extension Package (Optional)


FSL Overview
65

#### FSL Install & Setup


Installation
Setup
Create FSL Records
70

### Go Live in Production


Checklist
72

##### Stripe


Connect to Stripe in Live Mode
Stripe Webhooks, Live Mode
74

##### Authorize.net


Connect to Authorize.net in Live Mode
Authorize.net Webhooks, Live Mode
78

##### Spreedly


Connect to Spreedly in Live Mode
Create a Spreedly Payment Gateway
83

### Use Cases


PayLink: Automated PayLink with Opportunities
Transaction Reattempt Noti cations
Virtual Terminal
92

## Payments: Objects


Payments: Objects
93

### Allocations


Overview
Automate the Allocation Creation for Event Checkout
Scenarios for Payment and Refund Types
96

#### Write-Off Allocations


Overview
Scenarios
99

### Allocations


Allocation Fields
100

## Payments: Objects


Blackthorn Logs
Company Info
Disputes
Invoices
Line Items
Payment Gateway
Payment Gateway Customer
Payment Methods
Payment Schedules
Transactions
Webhook Events
136

## Payments: Features


Payments: Features
Authorize.net
Blackthorn | Payments Admin
Communities & Billing Portal
Custom Metadata Types
Custom Settings
Dashboard
Default Payment Method
152

### DocumentLink


DocumentLink Overview
DocumentLink Template
Authorize DocumentLink
Update DocumentLink Fields
158

#### Multilingual Support for DocumentLink


DocumentLink Multilingual Support Overview
Select a Method - DocumentLink
160

### DocumentLink


Invoice Payment
162

## Payments: Features


Transaction Email Receipts
163

### Field Service Lightning Payments


FSL Overview
FSL Extension Package Setup
Create FSL Records
Additional Con guration
FSL Extension Package Release Notes
174

### Flow Screen Charge Component


Flow Screen Charge Component
Translate Custom Labels
179

## Payments: Features


FSL Mobile Actions (without our iOS/Android app)
High Volume Batch Processing
Historical Sync
Level 3 Processing
Matching and Duplication
Multi-Currency
187

### PayLink


Introduction
Setup & Con guration
189

#### How It Works


How It Works
Card
ACH
193

#### Upgrade


Upgrade
Update Existing Transactions
196

### PayLink


FAQ
Use Cases
198

#### Multilingual Support for PayLink


PayLink Multilingual Support Overview
Select a Method - PayLink
205

### PayLink


AuthLink
Release Notes
209

## Payments: Features


Permission Sets
Plaid
Process Scheduled Transactions and Reattempt Logic
Recurring Charges and Subscription Options
Reports
Salesforce Shield / Platform Encryption with all Blackthorn apps
SCA and MOTO
Scheduled Batch Jobs
Spreedly
Stripe
229

### Stripe Billing


Overview
Step-by-Step Instructions
234

#### Settings


Settings
Blackthorn | Payments Admin
Permission Sets
Blackthorn | Scheduled Jobs
238

#### Features


Features
Account Subscription Data
Batch Apex Callouts to Stripe
Creating Subscriptions from Opportunities
Migrating Subscriptions
Stripe Billing Object and Stripe API Interaction
244

#### Objects & Stripe Modeling


Gateway SKU's
Invoices
Products
Stripe Coupons
Stripe Gateway Orders
Stripe Prices & Tiers
Subscriptions & Subscription Items
Subscription Schedules
Usage
255

## Payments: Features


Stripe Checkout
Stripe Metadata
Stripe Radar Integration
Test Data
262

### Virtual Terminal


Overview
267

#### Setup


Setup
Lightning Record Pages
Custom Aura Component (Advanced)
Custom Component Scenario
LWC Experience Cloud (Beta)
LWC Lightning Record Page
LWC Screen Flow Component
274

##### User Interface Con guration


User Interface Con guration
Manage Virtual Terminal Custom Settings
Add or Remove Virtual Terminal Fields
278

#### Additional Customization


ACH Direct Debit Mandate
279


##### Pre-Populate Fields


Pre-Populate Fields
Navigate to Custom Metadata Types
Virtual Terminal Transaction Con guration
New Record Screen
283

#### Additional Customization


Custom Labels
284

### Virtual Terminal


Available Actions
Payment Process Type
286

## Payments: Features


Webhooks
287

## Mobile Payments App


Overview
Supported Devices
Install & Setup
Con guration Options
Testing
Navigation
Check 21 Integration
Of ine for Mobile
Payment Intents and Stripe Payment Methods
Tap to Pay
307

### Mobile Payments App Release Notes


Mobile Payments Android Releases
Mobile Payments iOS Releases
311

## Payments: Troubleshooting and FAQ


Payments Error Codes
Payments FAQ
Payments Troubleshooting
DocumentLink Error Codes and Messages
320

## Payments: Release Notes & Webinar Recordings


Payments: Release Notes & Webinar Recordings
February 2026 - Version 6.57
January 2026 - Version 6.52
November 2025 - Version 6.49
October 2025
September 2025 - Version 6.48
August 2025 - Version 6.44
July 2025 - Version 6.42
June 2025 - Version 6.40
May 2025 - Version 6.37
April 2025 - Version 6.32
March 2025 - Version 6.3
February 2025 - Version 6.29
January 2025 - Version 6.28
335

### 2024


December 2024 - Version 6.27
November 2024 - Version 6.26
October 2024 - Version 6.25
September 2024 - Version 6.23
August 2024 - Version 6.22
July 2024 - Version 6.20
June 2024 - Version 6.19
May 2024 - Version 6.18
April 2024 - Version 6.17
March 2024 - Version 6.16
February 2024 - Version 6.13
January 2024 - Version 6.11
347

### 2023


December 2023 - Version 6.8
November 2023 - Version 6.6
October 2023 - Version 6.4.1
September 2023 - Version 6.3
August 2023 - Version 6.0.1
July 2023 - Version 5.108.2
June 2023 - Version 5.106
May 2023 - Version 5.103
April 2023 - Version 5.99.1
March 2023 - Version 5.95
February 2023 - Version 5.93
January 2023 - Version 5.91
359

### 2022


December 2022 - Version 5.85
October 2022 - Version 5.76
September 2022 - Version 5.71.2
August 2022 - Version 5.70
July 2022 - Version 5.66
June 2022 - Version 5.63
April 2022 - Version 5.58
March 2022 - Version 5.53
February 2022 - Version 5.49
368

### 2021


December 2021 - Version 5.46
November 2021 - Version 5.41
October 2021 - Version 5.34
September 2021 - Version 5.33
August 2021 - Version 5.31
July 2021 - Version 5.29
June 2021 - Version 5.24
May 2021 - Version 5.22
April 2021 - Version 5.20
March 2021 - Version 5.17
February 2021 - Version 5.15
January 2021 - Version 5.14
384


Welcome to Blackthorn Payments
Blackthorn Payments offers simple, Salesforce-native payment processing for every industry. Centralize and modernize your online, subscription, or mobile payment process. Whether one-time or recurring subscriptions, Blackthorn Payments streamlines every step of the process while giving your team access to critical nancial data.


Important Features
Connect your Payment Gateway in a matter of minutes with our Setup Wizard.
Process payments by phone with our Virtual Terminal.
Send web-based Invoices with our DocumentLink feature.
Con gure self-service payment options within the Experience Cloud by using the LWC Virtual Terminal or ChargeFlow component.
Set up recurring payments that will be automatically captured via payment schedules. Set it and forget it.
Process mobile payments with our iOS and Android mobile apps.
Send payment requests with our PayLink feature.
Stay PCI-Compliant using certain features of our app (see PCI Compliance for more information).
Connect multiple Payment Gateways.
Process payments in any currency that Stripe supports.
Sync historical data.
Automatically update expired cards.
Payments can originate in your gateway or in Salesforce. If it is from your gateway, be sure to set up webhooks so the data ows from your gateway to Salesforce.
Salesforceeditions supported: Enterprise, Unlimited, Performance, Developer, Force.com (App Cloud).
Blackthorn Payments is not supported in Salesforce Professional Edition orgs.


Popular Con guration Resources
Auto-Process and Reattempt Logic
DocumentLink
Historical Sync
Migrating Records
Mobile Payments
PayLink
Payment Schedules
PCI Compliance
Setup Wizard
Virtual Terminal
Webhooks


Performance and Scale Testing

Performance and Scale testing must be pre-approved by both Salesforce and Blackthorn. Please complete the steps below.


1. Follow the guidance provided by Salesforce and seek Salesforce approval.
2. Once you obtain Salesforce approval, submit a case to Blackthorn with your plan and detailed testing scenarios. You will be able to upload attachments after your ticket has been opened.
3. If approved, Blackthorn will work with you to determine an optimal date and time to run your tests.

Please read Performance and Scale of Your Experience Cloud Site for additional resources.


PCI Compliance

Introduction
PCI Compliance Guide:

The Payment Card Industry Data Security Standard (PCI DSS) is a set of requirements designed to ensure that ALL companies that process, store or transmit credit card information maintain a secure environment.


Processing, transmitting, and storing credit card data requires an organization to be in compliance with the PCI Data Security Standards (PCI DSS). PCI compliance decreases the footprint of where a Cardholder's data is located throughout an organization.

Stripe makes it easy to be in compliance. Using the Payments app with the Virtual Terminal or PayLink features reduces your PCI compliance scope even more. Your next step is to take a PCI DSS Self-Assessment Questionnaire to become fully PCI compliant.


Blackthorn does NOT offer this information as legal advice.

If you do seek complete PCI compliance, we recommend hiring a PCI compliance auditor to audit your practices. The information here is for guideline purposes only and is not to be used as legal advice.


Blackthorn | Payments
Salesforce has stringent security standards and Stripe is PCI Level 1 Service Provider - the most stringent level of certi cation available in the payments industry. To help maintain compliance, Blackthorn Payments does not store card or ACH details, it only stores the Card I D , which is a unique ID generated by Stripe.

Blackthorn Payments also complies with Stripe's usage requirements of utilizing TLS (Transport Layer Security) with either Checkout or Stripe.js. Click here for additional information.


Additional Information
If you need to provide someone else with an Attestation of Compliance (AOC), and/or you are asked to ll in a PCI DSS Self-Assessment Questionnaire (SAQ), Stripe already has you covered!


1. Log into your Stripe account.
2. Go to your security settings.
3. Click “View completed document.” Stripe will have the pre- lled documents for you.


Important Technical Information for Admins
Below is a list of important articles that review critical technical features and processes. Please read through them. They will help you understand how to con gure and maintain the Payments app.


Blackthorn Logs
Scheduled Jobs
Relationship Settings
Custom Settings
Custom Metadata
~Stripe Only~ Metadata Matching
~Stripe/PSD2 Regulation Only~ SCA


Overview
This Payments Quick Start Guide (QSG) will teach you how to download and install the Payments app and set up a Payment Gateway.

In this QSG, you will learn how to:

Download and install the Payments app.
Assign Licenses (if in production).
Assign Permission Sets.
Setup your Payment Gateway(s).
Stripe
Authorize.net
Spreedly
Set up PayLink, Virtual Terminal, and DocumentLink.
Move historical data to Blackthorn.
Set up FSL (optional).
Go live in production.


Install Payments
Blackthorn Payments can be installed in a Production or Sandbox org. Once installed, the Blackthorn team will be noti ed and will update your license.


Pre-requisites
Before you install the Events and/or Payments apps, you must complete the following steps.


1. Enable the following objects in your org. They handle le uploads (Event banners, Event Content, Speaker/Sponsor images, etc.), and without them, the Blackthorn packages will experience an error during installation.
Content Version (ContentVersion)
Content Document (ContentDocument)
Content Distribution (ContentDistribution)
2. Enable Chatter for Base and Events installs.


Install Payments
Note: You must have the Salesforce Administrator pro le to complete the tasks below.

1. Go to the Candy Shop.
2. Click Install Blackthorn Payments - Click Here for Details.
3. Click the Log In to Install button
4. Log into your Salesforce org.
5. Select “Install for Admins Only”.
6. Once the installation process is complete, you will receive an email from Salesforce.


Review Salesforce Connected App Changes
Salesforce recently announced a change to its security policy around Connected Apps, effective August 28th. As a result, Blackthorn recommends verifying that these Connected Apps are installed in your Salesforce orgs.

Blackthorn | Connected App - required to use Blackthorn Events and Blackthorn Payments
Mobile Check-in App - required for using Blackthorn Mobile Check-in
Blackthorn | Mobile Connected App - required for using Blackthorn Mobile Payments
Blackthorn Message - required for using Blackthorn Messaging

Please review the attached pdf for instructions to check that the required Connected Apps are installed and connected correctly.

Your browser does not support PDF. Click here to download.


Provide Users Access
It’s time to grant your users access to Blackthorn Payments.


Assign Licenses
You will need to assign the Blackthorn Payments license to all users who need access. To assign licenses, perform the following steps:

1. Click the Gear icon in the upper right-hand corner.
2. Click Setup.


3. Type and click “Installed Packages” in the Quick Find box.


4. Click Manage Licenses next to the package you need to assign. (Payments and Events licenses are separate.)


5. Click Add Users.


6. Check the box next to the Available Users that you need to assign a license to.


7. Click Add.


8. Repeat Steps 5-8 for any additional package licenses you need to assign.

If you purchased unlimited users, you can skip this step.


Assign Permission Sets
Next, you will need to add the appropriate Permission Sets to your users. This will grant them the ability to see all of the Blackthorn objects/records within Salesforce. For a breakdown of what each permission set does, please read this documentation.

You can assign one or more users to a permission set by assigning a user to a permission set. Or you can assign one or more permission sets to your users by assigning a permission set to a user.


Assign a User to a Permission Set
1. Click the Gear Icon in the upper right-hand corner.
2. Click Setup.


3. Type “Permission Sets” in the Quick Find box.
4. Click Permission Sets.


5. Click the permission set you need to manage.


6. Click Manage Assignments.
7. Click Add Assignment to assign users to the permission set.


8. Add your users and click Assign.


Assign a Permission Set to a User
1. Go to Setup.
2. Search for the user.
3. Click the user’s name.
4. Click Edit Assignments.
5. Click “Blackthorn | Payments (Admin)” in the Available Permission Sets box.
6. Click Add.
To remove a permission set, highlight it in the Enabled Permission Sets box, click the left Remove arrow, and click Save.
7. Click Save.


Manager vs. User

Manager and User are essentially the same with the exception that Managers can delete payment records.


Instructions
In Blackthorn Payments, a Payment Gateway record is synonymous with a gateway (i.e. Stripe, Authorize.net, etc.) account. Each Payment Gateway record you create connects your Salesforce org to one gateway account, in either test or live mode.

To start, we suggest connecting to your Payment Gateway in test mode. When you are ready to go live, then you can create another Payment Gateway record connecting to your Payment Gateway in live mode.


** Note About Payment Gateway Records**

Do not change your Payment Gateway record from Test to Live mode or vice versa by clicking Connect to Gateway or checking/unchecking the Test Mode checkbox. Instead, create a new record for the other mode you wish to enable.


Blackthorn supports several gateway providers. The primary gateway providers are Stripe, Authorize.net, and Spreedly.

Please click on the link below for your gateway and follow the instructions to connect your Payment Gateway in Salesforce.


Connect to Stripe

Connect to Authorize.net

Connect to Spreedly


Connect to Stripe in Test Mode

No Stripe Account?
If you don't have a Stripe Account, that is okay! Stripe allows you to skip the account form and connect to their test account until yours is ready.


Follow the steps below to complete the Payments Setup Wizard process.


1. Click the App Launcher.


2. Type “Admin”.


3. Click "Blackthorn | Payments (Admin)".


4. Click the Blackthorn | Payments Setup Wizard tab.


5. Watch the Overview Video and then click Let's get started.


6. Set Select Provider to "Stripe".


7. Set Select Your Gateway Mode to "Test".


8. Click Connect.
9. You will be redirected to the Stripe login page.
10. Click Skip. You can also log into your Stripe account if you have one already.
11. If you plan to use ACH, select “Yes” and click Make Magic Happen. This will deploy the ACH record type for the Payment Method object.


12. Permission Sets - Select No and click Next. You have already assigned permission sets.


13. Relationship Settings - MOST IMPORTANT SETTING. When a business charges a customer in Salesforce, there is an object that represents what's being sold, typically Opportunity, Quote, or similar. By default, we associate Opportunities, Contacts, Accounts, and Invoices with Transactions. If you need to associate Transactions to a different object,
please select that object from the drop-down.


14. Watch the Virtual Terminal Overview video or click Continue.


15. That’s it! Click Show me my rst transaction, and you’ve completed the Payment Wizard.


Test Your Stripe Payment Gateway

The next step is to test your Payment Gateway using either the test Stripe card or the test Stripe ACH bank account.


Test a Stripe Card

Warning
Actual card and bank account information cannot be used in Test Mode.


1. Con rm that the Payment Gateway has T est Mo de set to "TRUE".


2. Go to the Payment Method tab and click New.
3. Select "Card" and click Next.


4. Using the information provided below, complete the following elds.
Ho lder's Name = use any name
Number = “4242424242424242”
Ex piratio n Mo nth = use any month
Ex piratio n Y ear = use any year
CV V = use any 3-digit number
P o stal Co de = use any 5-digit number
P ay ment Gateway = the Payment Gateway you just set up
5. Click Save.

This Payment Method is now valid and can be used to capture and refund Transactions.

NOTE: Additional card numbers can be found in Stripe's testing documentation.


Test a Stripe ACH Bank Account

Warning
Real card and bank account information cannot be used in Test Mode.


1. Con rm that the Payment Gateway has T est Mo de set to “TRUE”.


2. Go to the Payment Method tab and click New.
3. Select "ACH" and click Next.


4. Use the data below to test either a successful or failed payment.
Successful Payment Method
Ho lder’s Name = Use any name
A c c o unt Number = “000123456789”
Ro uting Number = “110000000”
A c c o unt Ho lder T y pe = Choose either option
Currenc y I SO = “USD”
Co untry I SO = “US”
Failed Payment Method
Ho lder’s Name = Use any name
A c c o unt Number = 000111111116
Ro uting Number = 110000000
A c c o unt Ho lder T y pe = Choose either option
Currenc y I SO = “USD”
Co untry I SO = “US”
5. Click Save.

This Payment Method is now valid and can be used to capture and refund Transactions.


Test for Speci c Responses and Errors
Use the test cards below to create a Payment Method that produces a speci c response.


Incorrect CVC Code Error
Use this number to create an error about an incorrect CV V . The error message will be in the Stripe data elds.

•   Number = 4000000000000127


Fail to Capture
This number will create a valid Payment Method, but when you capture a Transaction with the Payment Method, the Transaction will fail. The error message will be in the Stripe data elds.

• Number = 4000000000000341


Additional testing for speci c responses and errors can be found here.


Disputes
Use the card below in test mode to simulate a disputed Transaction. This number will create a valid Payment Method, but when you capture a Transaction with the Payment Method, a Dispute record will be created.


Number = "4000000000000259"


Test Winning a Dispute

Enter the words "winning_evidence" in the A dditio nal I nf o rmatio n eld on the Dispute Evidence record to simulate the dispute being won and the funds being returned to your account as an adjustment Transaction.


Test Losing a Dispute

Enter the words "losing_evidence" in the A dditio nal I nf o rmatio n eld on the Dispute Evidence record to simulate the dispute being closed and marked as lost. (Your account will not be credited.)

Click here for more information about Disputes.


Delete Test Data
1. Navigate to your Stripe Dashboard.
2. Toggle "ON" the V iew test data switch. (left-hand column).
3. Click Business settings. (left-hand column)
4. Select "Data".
5. Next to Test data, click Delete all test data.
6. Click Delete Now.


Salesforce
Whether you are in a Production or Sandbox Org, you will need to temporarily deactivate all triggers so that you can delete Transaction, Payment Method, and Payment Gateway Customer records.

1. Navigate to Custom Settings.
2. Click Manage next to Blackthorn - Pay Trigger Settings.
3. Click Edit.
4. Check the Disable A ll T riggers checkbox.
5. Click Save.
6. Delete all of your test data.
7. Navigate back to Custom Settings and UNCHECK Disable A ll T riggers .


Set Up and Con gure Stripe Webhooks

Once you are connected to Stripe, it’s time to con gure webhooks, which automatically send speci c data from Stripe to Salesforce.

What are some bene ts of using webhooks?


Update a card on le with recent changes to the credit card information.
Send Payouts to Salesforce (reconciliation).
Create Disputes in Salesforce after capturing Transactions.
Send updates about deleted Payment Gateway Customers or Payment Methods.
Maintain consistency across all records by sending data from Stripe to Salesforce.


Prerequisite
You must have Salesforce administrator access to Salesforce and Stripe to complete the following instructions.


Create a Force.com Domain
1. Go to Setup.
2. In the Quick Find box, enter “Sites and Domains.”
3. Click “Sites.”
4. Enter a value for your Force.com domain.
5. Click Check Availability.
6. Review and accept the Site terms of use.
7. Click Register My Force.com Domain.


Con gure Your Site
1. Go to Setup.
2. In the Quick Find box, enter “Sites and Domains.”
3. Click “Sites.”
4. Click New.


5. Enter a Site Label , Site Name , and a Def ault W eb A ddress . (We suggest using "webhook" or "stripe" for the Site Label and Site Name .)
6. Set A c tiv e = "TRUE" (checked).
7. For the A c tiv e Site Ho me P age eld, click the Lookup icon and select "InMaintenance". (The page is not visible. It's just a placeholder because a value is required).
8. Click Save.


Change the Default Record Owner for Webhook Events
1. Go to Setup.
2. in the Quick Find box, enter and click “Sites.”
3. Click Edit next to your webhook site.
4. Change the Def ault Rec o rd Owner to a user of your choice.
5. Click Save.


Assign the Site Guest User Permission Set
1. Navigate back to the Site you created.
2. Click Public Access Settings.


3. Click the View Users or Assign Users button.
4. Click the link for the site guest user.


5. Add the Blackthorn | Payments (Site Guest User) permission set to this user's record.


6. Click Save.


Con gure Webhooks in Stripe
In this section, you will gather the different components that will make up the URL before adding it to Stripe.


The URL will have the following format: https://SITE_DOMAIN_NAME/SITE_PATH/services/apexrest/bt_stripe/webhook/WEBHOOK_LABEL


SITE_DOMAIN_NAME = The Salesforce Do main Name for the Site you set up
SITE_PATH = The P ath for the Site
WEBHOOK_LABEL = The value in the Payment Gateway W ebho o k Label eld
“services/apexrest/bt_stripe/webhook” remains the same


Create a Salesforce Webhook Site URL
1. Go to Setup.
2. In the Quick Find box, enter “Sites and Domains.”
3. Click “Sites.”
4. Locate the site you just created and click the URL.
5. Copy the URL.
6. Replace “SITE_DOMAIN_NAME/SITE_PATH” with the copied URL.
7. Leave “services/apexrest/bt_stripe/webhook” as is.
8. Open the related Payment Gateway record.
9. Copy the value in the W ebho o k Label eld.
10. Replace “WEBHOOK_LABEL” with the copied value from the W ebho o k Label eld.
11. To verify that the new URL works, open a new browser tab and paste the URL. You will see the following message.


Con gure the URL in Stripe
1. Go to your Stripe dashboard. When you create a Webhook URL for your Stripe account in test mode, ensure the "Viewing test data" switch is enabled.
2. Click the Developers tab at the bottom-left side of the screen.
3. Click Webhooks.
4. Click + Add destination to add a destination.


5. Click Your account.
6. Click into the Account section.
7. Check the Selec t all A c c o unt ev ents option.


8. Scroll down to and click into the Charge section.
9. Click the Selec t all Charge ev ents option.


10. Click into the Checkout section.
11. Check the options that are relevant to your use case.


12. Scroll down to the Invoice section.
13. Check the Selec t all I nv o ic e ev ents option.


14. Scroll down to the Payment Method section.
15. Check the Selec t all P ay ment Metho d ev ents option.


16. Scroll down to the Refund section.
17. Check the Selec t all Ref und ev ents option.


18. Click Continue.
19. Select “Webhook endpoint.”


20. Click Continue.


21. Enter a Destinatio n name .
22. Enter the URL you created in the Endpo int U RL eld.
23. Click Create destination.
24. To test the new Webhook Event, create a new charge Transaction, capture it, and charge it. A new Webhook Event will be created for the Transaction.

In Stripe, click the Events tab to see the newly created charge. The new Stripe Ev ent I D will match the Webhook Event Ev ent I D .


Create an Authorize.net Sandbox Account

The Setup Wizard's rst step is to connect to a Payment Gateway. Before that, you'll need to create an Authorize.net sandbox account to test.

1. Go to this link.
2. Fill out the form.


3. Click Submit.


4. Click Test Environment.


5. Log in to your account.


6. See your test account with Authorize.net.


Connect to Authorize.net in Test Mode

1. Click the App Launcher.


2. Type “Admin”.


3. Click "Blackthorn | Payments (Admin)".


4. Click "Blackthorn | Payments Setup Wizard".


5. Watch the Overview Video then Click "Let's get started".


6. Set Select Provider to "Authorize.net".


7. Set Select Your Gateway Mode to "Test".
8. Click Connect.
9. Log in to your test Authorize.net account.
10. If you plan to use ACH, select “Yes” and click Make Magic Happen. This will deploy the ACH record type for the Payment Method object.


11. Permission Sets - Select No and click Next. You have already assigned permission sets.


12. Relationship Settings - MOST IMPORTANT SETTING - When a business charges a customer in Salesforce, there is an object that represents what's being sold, typically Opportunity, Quote, or similar. By default, we associate Opportunities, Contacts, Accounts, and Invoices with Transactions. If you need to associate Transactions to a different object, please
select that object from the drop-down.


13. Watch the Virtual Terminal Overview vieo or click Continue.


14. That’s it! Click Show me my rst transaction, and you’ve completed the Payment Wizard.


De ne the Gateway User ID

Now that you are connected to your Payment Gateway, you need to manually copy the “API Login ID” from your Authorize.net account and paste it into the Payment Gateway Gateway U ser I D eld.


1. Log into your Authorize.net account.
2. Click Account and then API Credentials and Keys.


3. Copy the “API Login ID”.


4. Enter the “API Login ID” in the Gateway U ser I D eld.


5. Click Save.


Test Your Authorize.net Payment Gateway
The next step is to test your Payment Gateway using either the test Authorize.net card or the test Authorize.net ACH bank account.


Test an Authorize.net Card

Warning
Actual card and bank account information cannot be used in Test Mode.


1. Con rm that the Payment Gateway has T est Mo de set to “TRUE”.


2. Go to the Payment Method tab and click New.
3. Select Card and click Next.


4. Using the information provided below, complete the following elds.
a. Ho lder’s Name = use any name
b. Number = “4111111111111111”
c. Ex piratio n Mo nth = use any month
d. Ex piratio n Y ear = use any year
e. CV V = use any 3-digit number
f. P o stal Co de = use any 5-digit number
g. P ay ment Gateway = the Payment Gateway you just set up
5. Check the Payment Gateway’s Enable A utho rize.Net CCV Filter eld if you want to require users to re-enter the CVV code for the card they are using.
6. Click Save.


This Payment Method is now valid and can be used to capture and refund Transactions.

For more information about testing Authorize.net Payment Gateways, click here.

NOTE: Additional card numbers can be found in Authorize.net's testing documentation.


Test an Authorize.net ACH Bank Account

Warning
Real card and bank account information cannot be used in Test Mode.


1. Con rm that the Payment Gateway has T est Mo de set to “TRUE”.


2. Go to the Payment Method tab and click New.
3. Select A CH and click Next.


4. Using the information provided below, complete the following elds.
a. Ho lder’s Name = use any name
b. A c c o unt Number = “000123456789”
c. Routing Number = “122105812”
d. A c c o unt Ho lder T y pe = either option
e. Currenc y I SO = “USD”
f. Co untry I SO = “US”
5. Click Save.

This Payment Method is now valid and can be used to capture and refund Transactions.

NOTE: For testing purposes, eCheck.Net transactions under $100 will be accepted. To generate a decline, submit a Transaction over $100. A monthly limit of $5000 is also con gured in the sandbox. If you exceed this amount, your eCheck Transactions will fail with a "This transaction has been declined." error message.


Test for Speci c Responses and Errors

Cards
Create a Payment Method using the following postal codes to generate a declined Transaction.

* P o stal Co de = "46282" - This Transaction will be declined.

* P o stal Co de = "46205" - The Transaction will be declined because of an AVS mismatch. The address provided does not match the cardholder's billing address.


ACH
To generate a decline using an ACH bank account, submit a Transaction over $100.


Duplicate Payment Methods
Create two Payment Methods with the same name and email address to generate "A duplicate record with ID [auth.net id] already exists error" for the second Payment Method.


Set Up and Con gure Authorize.net Webhooks

Once you are connected to Authorize.net, it’s time to con gure webhooks. What does a webhook do? It automatically sends speci c data from Authorize.net to Salesforce.

If you have created a Customer Pro le in Authorize.net, webhooks can update Salesforce and add the new Payment Gateway Customer and Payment Method records.


Prerequisites
You must have Salesforce administrator access and Authorize.net access to complete the following instructions.

Due to a limited number of available elds in Authorize.net, the Payment Pro le information in Authorize.net is used to populate the following Salesforce records.

Payment Method
Payment Gateway Customer
Example: Payment Pro le Name from Authorize.net = Payment Gateway Customer Name .


Create a Force.com Domain
1. Go to Setup.
2. In the Quick Find box, enter “Sites and Domains.”
3. Click “Sites.”
4. Enter a value for your Force.com domain.
5. Click Check Availability.
6. Review and accept the Site terms of use.
7. Click Register My Force.com Domain.


Con gure Your Site
1. Go to Setup.
2. In the Quick Find box, enter “Sites and Domains.”
3. Click “Sites.”
4. Click New.


5. Enter a Site Label , Site Name , and a Def ault W eb A ddress . (We suggest using "webhook" or "stripe" for the Site Label and Site Name .)
6. Set A c tiv e = "TRUE" (checked).
7. For the A c tiv e Site Ho me P age eld, click the Lookup icon and select "InMaintenance". (The page is not visible. It's just a placeholder because a value is required).
8. Click Save.


Assign the Site Guest User Permission Set
1. Navigate back to the Site you created.
2. Click Public Access Settings.


3. Click the View Users or Assign Users button.
4. Click the link for the site guest user.


5. Add the Blackthorn | Payments (Site Guest User) permission set to this user's record.


6. Click Save.


Con gure Webhooks in Authorize.net
In this section, you will gather the different components that will make up the URL before adding it to Authorize.net.

The URL will have the following format: https://SITE_DOMAIN_NAME/SITE_PATH/services/apexrest/bt_stripe/webhook/WEBHOOK_LABEL

SITE_DOMAIN_NAME = The Salesforce Do main Name for the Site you set up
SITE_PATH = The P ath for the Site
WEBHOOK_LABEL = The value in the Payment Gateway W ebho o k Label eld
“services/apexrest/bt_stripe/webhook” remains the same


Create a Salesforce Webhook Site URL


1. Go to Setup.
2. In the Quick Find box, enter “Sites and Domains.”
3. Click “Sites.”
4. Locate the site you just created and click the URL.
5. Copy the URL.
6. Replace “SITE_DOMAIN_NAME/SITE_PATH” with the copied URL.
7. Leave “services/apexrest/bt_stripe/webhook” as is.
8. Open the related Payment Gateway record.
9. Copy the value in the W ebho o k Label eld.
10. Replace “WEBHOOK_LABEL” with the copied value from the W ebho o k Label eld.
11. To verify that the new URL works, open a new browser tab and paste the URL. You will see the following message.


Con gure the URL in Authorize.net
1. Go to your connected Authorize.net account dashboard.
2. Click the Account tab.
3. Click Settings.
4. Click Webhooks.


5. Click Add endpoint.


6. De ne a Name .
7. In the Endpo int U RL eld, enter the Salesforce webhook Site URL you created.
8. Set Status = "Active".
9. Under Select Events, check "All Events."
10. Click Save.

If you have multiple Authorize.net accounts connected to your Salesforce org and want to create a Webhook Endpoint for each in Authorize.net, you can use the same Salesforce Site. Change the WEBHOOK_LABEL part of the URL to the Webhook Label value on the Payment Gateway record you want to use.


Test Your Webhook Connection

1. Click on the Account tab > Settings > Webhooks.
2. Edit the Endpoint and set the Status to "Inactive."
3. Click Save.

You will see a Test Webhook button as shown in the screenshot below.


If you received a "Ping successful" message at the top, then webhooks are set up correctly!


Connect to Spreedly in Test Mode

Limitation
Currently, you can't connect to Spreedly from the Setup Wizard. Please click the Skip button under the Connect to Gateway instructions.


1. Click on the App Launcher and type “admin”.


2. Click on "Blackthorn | Payments (Admin)".


3. Click on "Blackthorn | Payments Setup Wizard".


4. Watch the Overview Video then Click on "Let's get started".


5. Currently, you can't connect to Spreedly from the Setup Wizard. Please click the Skip button under the Connect to Gateway instructions.
6. If you plan to use ACH, select “Yes” and click Make Magic Happen. This will deploy the ACH record type for the Payment Method object.


7. Permission Sets - Select No and click Next. You have already assigned permission sets.


8. Relationship Settings - MOST IMPORTANT SETTING. When a business charges a customer in Salesforce, there is an object that represents what's being sold, typically Opportunity, Quote, or similar. By default, we associate Opportunities, Contacts, Accounts, and Invoices to Transactions. If you need to associate transactions to a different object, please
select that object from the drop-down.


9. Watch the Virtual Terminal Overview video or click Continue.


10. That’s it! Click Show me my rst transaction, and you’ve completed the Payment Wizard.


Update Your Payment Gateway Page Layout

Payment Gateway Customer Record Update
Since Spreedly does not have an equivalent record (e.g., user id) for customers, a Payment Gateway Customer record will not be created in Salesforce.


1. Click the Gear icon in the upper right-hand corner.
2. Click Setup.
3. Click the Object Manager tab.
4. Locate the Payment Gateway object.
5. Click the Field & Relationships tab.
6. Locate the P ro v ider eld.
7. In the Values section, click New.
8. Enter “Spreedly” and click Save.
9. Click the Page Layouts tab.
10. Click Payment Gateway Layout.
11. Add the following elds to your Payment Gateway page layout:
Spreedly Env iro nment Key
Spreedly Co nf igured Gateway
Gateway T o k en
Spreedly P riv ate Key (use with iframed components)

Spreedly Certif ic ate T o k en (use with iframed components)
12. Click on the Buttons section.
13. Drag and drop the Create Spreedly Gateway button to the Custom Buttons section.
14. Click on the Mobile & Lightning Actions section.
15. Drag and drop the Create Spreedly Gateway button to the Salesforce Mobile and Lightning Experience Actions section.
16. Click Save.


Create a Spreedly Payment Gateway

Authorize.net and Stripe Users

When setting up a Payment Gateway using Spreedly, the option to add Authorize.net and Stripe as a Payment Gateway has been removed. Authorize.net and Stripe function as stand-alone Payment Gateways.


When setting up Blackthorn Payments, we suggest you connect your Payment Gateway in test mode so that you can create test Transactions, Payment Methods, and Customers.

1. Contact Blackthorn Support to obtain a Spreedly Environment Key.
2. Navigate to the Payment Gateway object.
3. Click New.


4. Enter a P ay ment Gateway Name .


5. Set P ro v ider = “Spreedly”.


6. Check the T est Mo de checkbox if you are setting this up in your sandbox for testing. Do not check the box if this is a live Payment Gateway in production.


7. Populate the Def ault Currenc y and Def ault Co untry     elds.


8. Enter the key provided by Blackthorn Support in the Spreedly Env iro nment Key    eld.


9. Click Save.


10. Click the Create Spreedly Gateway button.
11. Select the Payment Gateway you want to connect (e.g. CardConnect; EBANX). For test mode, select "Spreedly Test".
12. If prompted, add additional information from the selected gateway.
13. Click Create.


14. The Spreedly Co nf igured Gateway and Gateway T o k en elds will be populated automatically.


Test Your Spreedly Payment Gateway
The next step is to test your Payment Gateway using either the test Spreedly card or the test Spreedly ACH bank account.


Test a Spreedly Card

Warning
Real card and bank account information cannot be used in Test Mode.


1. Con rm that the Payment Gateway has T est Mo de set to “TRUE”.


2. Go to the Payment Method tab and click New.
3. Select Card and click Next.


4. Using the information provided below, complete the following elds.
Ho lder’s Name = use any name
Number = “4111111111111111”
Ex piratio n Mo nth = use any month
Ex piratio n Y ear = use any year
CV V = use any 3-digit number
P o stal Co de = use any 5-digit number
P ay ment Gateway = use the Payment Gateway you just set up
5. Click Save.


This Payment Method is now valid and can be used to capture and refund Transactions.

For more information about testing Spreedly Payment Gateways, click here.


Spreedly and ACH Bank Account Limitation

Blackthorn does not support webhook callbacks for gateways that are con gured through Spreedly. As a result, Blackthorn does not recommend submitting ACH payments via Spreedly.

If an ACH payment is submitted via Spreedly, users must check their gateway to see if the payment is complete. Users cannot con rm if the payment was successful by going to Salesforce.

If you do use ACH payments with Spreedly, please proceed with caution.


Test a Spreedly ACH Bank Account

Warning
Real card and bank account information cannot be used in Test Mode.


1. Con rm that the Payment Gateway has T est Mo de set to “TRUE”.


2. Go to the Payment Method tab and click New.
3. Select A CH and click Next.


4. Using the information provided below, complete the following elds.
Ho lder’s Name = use any name
A c c o unt Number = “9876543210”
Ro uting Number = “021000021”
A c c o unt Ho lder T y pe = either option
Currenc y I SO = “USD”
Co untry I SO = “US”
5. Click Save.

This Payment Method is now valid and can be used to capture and refund Transactions.

For more information about testing Spreedly Payment Gateways, click here.


Overview

For Government Cloud Users

Government Cloud users who want to use PayLink need to reach out to Blackthorn Support to have instanceUrl added to their PayLink license.


Do I need to install PayLink?

PayLink does not need to be installed separately. It was already installed via the Candy Shop.


PayLink is our beautiful, mobile-responsive payment request, paid add-on. For every Transaction that's created, a unique link (PayLink) is created.

The link can be rolled up to your Transaction's parent record, such as an Opportunity record. The link can also be automatically emailed to your customer so they can make an immediate payment.


Check out this quick 2-minute video to see it in action! Blackthorn Payments - PayLink Overview

Quick Tip: You can create multiple PayLink con gurations to change the look and feel of payment requests!


Provide User Access

Does your user have a Payments license?

Users must have a Payments license before they can be given access to PayLink.


Assign PayLink Licenses
You will need to assign the Blackthorn PayLink license to all users who need access. To assign users a PayLink license, complete the following steps.

1. Click the Gear icon in the upper right-hand corner.
2. Click Setup.
3. Type “Installed Packages” in the Quick Find box.
4. Click Installed Packages.
5. Click Manage Licenses next to Blackthorn | PayLink.
6. Click Add Users.
7. Check the box next to the Available Users that you need to assign licenses to.
8. Click Add.


Assign Permission Sets
Next, you will need to add the appropriate Permission Sets to your users. This will grant them the ability to see the necessary Blackthorn objects/records within Salesforce.

Administrative users will need the Blackthorn | PayLink (Admin) permission set while Managers and End Users will need the Blackthorn | PayLink (User) permission set.

You can assign one or more users to a permission set by Assigning a User to a Permission Set. Or you can assign one or more permission sets to your users by Assigning a Permission Set to a User.


Assign a User to a Permission Set
1. Click the Gear Icon in the upper right-hand corner.
2. Click Setup.
3. Type “Permission Sets” in the Quick Find box.
4. Click Permission Sets.
5. Click the permission set you need to manage.
6. Click Manage Assignments.
7. Click Add Assignment to assign users to the permission set.
8. Add your users and click Assign.


Assign a Permission Set to a User
1. Go to Setup.
2. Search for the user.
3. Click the user’s name.
4. Click Edit Assignments.
5. Click either Blackthorn | PayLink (Admin) or Blackthorn | PayLink (User) in the Available Permission Sets box.
6. Click Add.
7. To remove a permission set, highlight it in the Enabled Permission Sets box, click the left Remove arrow, and click Save.
8. Click Save.


Con gure PayLink
Follow the steps below to con gure PayLink.


1. Navigate to the Blackthorn PayLink app.
2. Click the PayLink Con guration tab.
3. Click New.
4. Enter the Name (required).
5. Add information to additional elds, as needed.
6. Add the A c c eptanc e Language , if using.
7. Add the T erms and Co nditio ns URL, if using.
8. Click Save.


Acceptance Language and Terms & Conditions Functionality

Pre-requisite

The A c c eptanc e Language eld must be lled.


If the A c c eptanc e Language eld has a value, the following will occur.


A checkbox will appear on the PayLink checkout.
The text entered in the A c c eptanc e Language eld will be the checkbox label.


If the A c c eptanc e Language eld has a value AND the T erms and Co nditio ns eld contains a URL, then the checkbox label will be hyperlinked with the URL.

BUT if the A c c eptanc e Language eld is empty, the checkbox and the accompanying hyperlinked text WILL NOT be visible.


Image Size Considerations
When using the Bac k gro und I mage (U RL) eld to add a background image to PayLink, consider the following.


We recommend using an image le no larger than 1MB.
The image you use will cover the whole page.
All images have a certain ratio (height and width). You may need to adjust your image outside of Salesforce based on the viewport of the devices being used.
If your image includes text, make sure it won’t be cropped on different devices (desktop, tablet, or mobile). You may need to edit your image outside of Salesforce to reorient the text.


Additional Con guration
We've added a few elds that allow users to further customize their PayLink. The following elds can be added to the PayLink Con guration object's page layout.

Due Date Label : This overrides the Transaction Due Date eld.
A mo unt Due Label : This overrides the Transaction A mo unt eld.
Requested By Label : This overrides the Requested By label when a value is added to the Transaction A c c o unt eld.


SCA (Stripe, Required for European Customers)
The requirements for SCA affect our customers in Europe where the PSD2 regulation is being implemented. It's quick and easy to enable SCA with Blackthorn.

Click here for instructions on enabling SCA.


Instructions
Stripe Checkout is a prebuilt, hosted payment page that easily and securely accepts payments online. Payment options include ApplePay and GooglePay.

Complete the following steps to enable Stripe Checkout.

1. Con gure the Payment Gateway.
2. Add Permissions to Access Encrypted Data.
3. Assign the Proper Page Layout to the Corresponding Record Type.
4. Con gure PayLink.Stripe Checkout is a prebuilt, hosted payment page that easily and securely accepts payments online. Payment options include ApplePay and GooglePay.


Con gure the Payment Gateway

Update Your Page Layout
1. Navigate to the Payment Gateway object in Setup.
2. Click the Page Layouts tab.
3. Click the Payment Gateway Layout link.
4. Add the A c c epted Chec k o ut P ay ment Metho ds eld to the Page Layout.
5. Click Save.


Set Values on the Payment Gateway Object
1. Navigate to the Stripe Payment Gateway that will be used for Stripe Checkout.
2. Select your required values for the following elds.
Def ault Currenc y
Def ault Co untry
3. Edit the A c c epted Chec k o ut P ay ment Metho ds eld to include the Payment Method to be used for Stripe Checkout. The supported payment method types for Stripe Checkout are here.

NOTE: Stripe updates this list periodically.

Payment Method Limitations: Certain payment methods like Sepa Debit only work with certain currencies (EUR). Check out this payment method fact sheet to review the limitations of each payment method type.


Add Permissions to Access Encrypted Data

1. Go to Permission Sets in Setup.
2. Click New.
3. Enter "Access Encrypted Data" in the Label eld.
4. Click Save.
5. Navigate to System Permissions.
6. Click Edit.
7. Check the V iew Enc ry pted Data checkbox.
8. Save the permission set.
9. Navigate to the user record in Setup for the person who authenticated the PayLink app. This is the person who clicked the Authenticate button while running the PayLink setup wizard.
10. Add the new permission set to their user record.


Assign the Page Layout to the Corresponding Record Type

1. Navigate to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, enter and click "Payment Method."
4. Click the Page Layouts tab.
5. Click Page Layout Assignment.
6. Click Edit Assignment.
7. Set the P age Lay o ut to U se to "Other" and con rm that the "Other" column lists "Other" for each relevant pro le.
8. Click Save.


Con gure PayLink
Add Stripe Checkout to the PayLink Con guration Object
1. Navigate to the PayLink Con guration object in Setup.
2. Click the Fields and Relationships tab.
3. Click the link for the A llo wed P ay ment Metho ds eld.
4. Go to the Values section.
5. Click New.
6. Add "Stripe Checkout" to the text box.
7. Click Save.


Set the Value on the Paylink Con guration Record
1. Navigate to the Paylink Con guration record that you will use for your Stripe Checkout Transactions.
2. Click Edit (the pencil icon) next to the A llo wed P ay ment Metho ds eld.
3. Move "Stripe Checkout" to the Chosen column.
4. Click Save.


Virtual Terminal
The LWC Virtual Terminal feature gives users the ability to collect payments from almost anywhere including:

Lightning Experience Sidebar
Lightning Experience Utility Bar
Salesforce Classic
Salesforce1 Mobile App

Check out this overview video to learn how to use the Virtual Terminal.


Set Up the Virtual Terminal in Salesforce Lightning
Before you can test the LWC Virtual Terminal component, you need to add it to your Salesforce org.

There are several places you can add this component. If you want to take a payment from an Opportunity, add the LWC Virtual Terminal to the Opportunity page layout. Or if you want to take payment from the Invoice object, add it to the Invoice page layout.

Complete the steps below to set up the LWC Virtual Terminal in Salesforce Lightning.

1. Navigate to the record where you want to place the LWC Virtual Terminal.
2. Click the Gear icon.
3. Click Edit Page.
4. On the left-hand side, select the BT Payments Virtual Terminal Visualforce component and drag and drop it into the Related column.
5. Set the V irtualf o rc e P age Name = "Virtual Terminal".
6. Set the Height (in pix els) = “660”.
7. Click Save.

To add the Virtual Terminal to any page layout, the Salesforce Mobile App, the Lightning Utility Bar, or your Experience Cloud, click here.


Customize the Virtual Terminal
Now that the LWC Virtual Terminal is added to your page layout, you can perform customizations that will make it even more powerful.

There are two types of customizations you can perform.

Click here to learn about pre- lling the elds.
Click here to learn about setting default values/actions for each eld.


Allowlist your Domain for the Aura Virtual Terminal
When using the Legacy Aura Virtual Terminal, you are required to allowlist any custom domains you are using. This allows Salesforce to enable your domain for Visualforce Inline Frames.

1. Click the Gear icon.
2. Click Setup.
3. In the Quick Find box, search for and click "Session Setting".
4. Under the Trusted Domains for Inline Frames section, click Add Domain.
5. Enter "https://.lightning.force.com".
(Example: if your domain-instance-name is "blackthornio", the new domain will be https://blackthornio.lightning.force.com)
6. Click Save.


Overview

Is DocumentLink a paid add-on?

No, the DocumentLink feature is included in your Payments package.


DocumentLink renders streamlined, mobile-responsive, and payable invoices on the web that can easily be shared via a link. Itemized Invoices can be paid using Blackthorn Payments while remaining PCI Compliant.


Check out our overview of DocumentLink here!


Authorize
To send Invoices from Salesforce via DocumentLink, you need to authorize DocumentLink with Blackthorn's Connect App.


Oauth Link

For the authorization to work properly, you can only be logged into one Salesforce org.


Production Org
Please click the oauth link to complete the DocumentLink setup.


Sandbox Org
1. Click the oauth link to complete the DocumentLink setup.
2. Click Allow to allow access.


3. If the authorization is successful, you will see a success message.


Did you receive an error?

If you receive an error, view the DocumentLink Error Codes And Messages.


Con gure DocumentLink Templates
With DocumentLink authorized in your org, it's time to set up your templates. This will allow you to add in Acceptance Language, Terms & Conditions, etc.

The DocumentLink Template object stores elds that allow users to con gure the presentation of a DocumentLink.


De ne Custom Acceptance Language
Using the A c c eptanc e Language - A CH , A c c eptanc e Language - Card , and T erms and Co nditio ns elds allows users to create their own custom messaging or link to their own custom terms and conditions.


Credit Card DocumentLink Checkout Example:


Bank DocumentLink Checkout Example:


Add a Company Logo and Details to DocumentLink
To add a logo and company details to your DocumentLink Invoice, complete the following steps.

1. From the App Launcher, navigate to the Company Info object.
2. Click New to create a new record.
3. Complete the following elds.
Co mpany I nf o Name (required)
Email (required)
Lo go - enter a URL to your logo.
NOTE: Use the Documents object in the Classic UI to store images. From there, right-click the image, select "Copy Image Address," and add it to the Lo go eld.
4. Add any additional details such as a website and address.
5. Click Save.
6. Add the Company Info record to either the DocumentLink Template record or directly on the Invoice record.

Click Company Info for more information about the Company Info object.


Add Custom Fields and Footer
Use the following elds to customize an Invoice when it is created with DocumentLink.

Do c umentLink Field 1 (Label)
Do c umentLink Field 1
Do c umentLink Field 2 (Label)
Do c umentLink Field 2
Fo o ter


Automatically Apply DocumentLink Template to Invoices


1. Create a simple process (Process Builder, Flow, etc).
2. In your automated process, set the Do c umentLink eld on the Invoice Record.
3. Set the process to ll in the DocumentLink Template any time an Invoice is created.


Deprecated Fields
If you upgraded your Blackthorn Payments package and noticed that some elds on the DocumentLink Template object have the ability to be deleted, feel free to take advantage of this to clean your org.

Otherwise, if a eld has the ability to be deleted and can no longer be added to your page layout that means we no longer support it. You'll need to go to Setup in the Classic UI to see the option to delete.

Fields that Blackthorn No Longer Supports

Background Color
Button Color
Card Color Theme
Logo
Due Date Label
Requested by label
Amount due label
Documentation


Add the “Create Invoice” Button to the Opportunity Page Layout (Optional)
Use the Create Invoice button to easily create one-off Invoices directly from an Opportunity. By simply adding information to the necessary elds, you can create a beautiful Create Invoice with the click of a button.


Add the Create Invoice Button
1. Click the Gear icon.
2. Click Setup.
3. Click the Object Manager tab.
4. In the Quick Find box, enter "Opportunity" and click the link for Opportunity.
5. Click Page Layouts.
6. Click Opportunity Layout.


7. Click Buttons.


8. Click and drag the Create Invoice button to the Opportunity Detail section.


9. Click Save.
10. Go back to your Opportunity record and refresh the page. In the drop-down in the right-hand corner, click Create Invoice.


11. Click Create.


You need to have the following items to successfully create and review an Invoice:

Have at least one Product related to the Opportunity.
Add the Invoices Related List to your page layout.


Auto-convert Opportunities to Invoices
You can convert an existing Opportunity object to an Invoice. The Opportunity Products will be converted to Line Items in the Invoice. The newly created Invoice will be linked to the originating Opportunity using the Oppo rtunity lookup eld.

The Opportunity Product Line I tem lookup eld will facilitate mapping the Invoice Line Item directly with the Opportunity Product Line Item. When an Invoice is created from Opportunities using the Create Invoice button, you can self-map additional Opportunity Line Item elds to the Invoice using a process builder.


Start Here
If you need to move any historical data from your current gateway or different objects, into Blackthorn Objects - look no further.


Stripe
Authorize.net
Dataload Historical Transactions into Blackthorn


Overview

Are webhooks active?

Before you start this task, webhooks need to be inactive. If webhooks are on, all the data will sync into Salesforce the minute it is loaded into your Stripe Account.


The rst step is to move any historical data from your existing gateway account over to your new Stripe account. Once that is complete, you will need to sync customer, payment method, transaction, and payout data from Stripe to Salesforce.

Click the links below for more information about each step.

1. Instructions
2. Customers
3. Payment Methods
4. Charges / Refunds
5. Payouts


Move Data from a Non-Stripe Account to Your New Stripe Account
Is your data located somewhere other than at Stripe?

If your data is with a different gateway and you want to move it to Stripe, Stripe provides a way to move your Customer and Payment Method records from your old/current payment gateway.

To start the process, reach out to Stripe Support.


Instructions
Before you start...

There are several ways to match data that syncs into Salesforce. Before you begin, con rm that your custom data, matching logic, or metadata is set up correctly. If you need help or want to chat, go to the Community where Support and Onboarding are available to help.

Review the instructions below and move through each of the following sections.

1. Sync your Stripe records in this order.
a. Customers - wait until this job is done before proceeding.
b. Payment Methods - wait until this job is done before proceeding.
c. Charges/Refunds - wait until this job is done before proceeding.
d. Payouts
2. Start with a small date range.
Select a small date range for a few Customer records to bring into Salesforce. This way you can con rm that everything looks correct and has related correctly before syncing everything.
3. Review how the emails match.
During the sync, if the Payment Gateway Customer's Email matches a Salesforce Contact's Email , the matching Contact will be populated on the Payment Gateway Customer's Co ntac t lookup eld.
BUT, if the Payment Gateway Customer's Email matches with more than one Contact record's Email , then the Payment Gateway Customer's Co ntac t lookup eld will not be populated.


Customers

Warning
When using this function, there are no "undo" calls. Be careful when clicking any of the buttons. If you want to make sure everything comes over correctly, sync a small number of records before syncing all of them.


1. Navigate to the Payment Gateway object.
2. Select the "View All" option.
3. Click the Payment Gateway record you want to sync.
4. Click the Sync with Stripe button.
5. Select either the Core, Billing, or Connect tab.


6. In the Fro m: and T o : elds, choose a date/time range for the data sync, if applicable.


7. Click the Customers button.


8. A message will appear telling you that the process has started.


Suggestion
If you have a large number lot of records (10,000+), click the Sync button and let the process run all night.


Payment Methods

Warning
When using this function, there are no "undo" calls. Be careful when clicking any of the buttons. If you want to make sure everything comes over correctly, sync a small number of records before syncing all of them.


1. Navigate to the Payment Gateway object.
2. Select the "View All" option.
3. Click the Payment Gateway record you want to sync.
4. Click the Sync with Stripe button.
5. Select either the Core, Billing, or Connect tab.


6. In the Fro m: and T o : elds, choose a date/time range for the data sync, if applicable.


7. Click the Payment Methods button.


8. A message will appear telling you that the process has started.


Suggestion
If you have a large number lot of records (10,000+), click the Sync button and let the process run all night.


Charges / Refunds

Warning
When using this function, there are no "undo" calls. Be careful when clicking any of the buttons. If you want to make sure everything comes over correctly, sync a small number of records before syncing all of them.


1. Navigate to the Payment Gateway object.
2. Select the "View All" option.
3. Click the Payment Gateway record you want to sync.
4. Click the Sync with Stripe button.
5. Select either the Core, Billing, or Connect tab.


6. In the Fro m: and T o : elds, choose a date/time range for the data sync, if applicable.


7. Click the Charges/Refund button.


8. A message will appear telling you that the process has started.


Suggestion
If you have a large number lot of records (10,000+), click the Sync button and let the process run all night.


Payouts

Warning
When using this function, there are no "undo" calls. Be careful when clicking any of the buttons. If you want to make sure everything comes over correctly, sync a small number of records before syncing all of them.


1. Navigate to the Payment Gateway object.
2. Select the "View All" option.
3. Click the Payment Gateway record you want to sync.
4. Click the Sync with Stripe button.
5. Select either the Core, Billing, or Connect tab.


6. In the Fro m: and T o : elds, choose a date/time range for the data sync, if applicable.


7. Click the Payouts button.


8. A message will appear telling you that the process has started.


Suggestion
If you have a large number lot of records (10,000+), click the Sync button and let the process run all night.


Instructions
Select one of the following paths to move your existing Authorize.net data.


Option 1
Automatically sync the data from your existing gateway account to Salesforce via Authorize.net.


Option 2
Perform the following two steps to manually sync your data.


1. Sync the data from your existing gateway account to Authorize.net.
2. Sync your data from Authorize.net to Salesforce.


Automatically Move Historical Data

Are webhooks active?

Before you begin, you must enable webhooks. If webhooks are on, your data will automatically sync from Authorize.net to Salesforce.


Before you move any historical data from your existing gateway account to Authorize.net, complete the following steps. Your data will be automatically synced to Salesforce once it's created in Authorize.net.

1. Enable webhooks. When webhooks are enabled, the data will automatically sync from Authorize.net to Salesforce.
2. Con rm that your matching logic is set up correctly. Matching logic determines how this data will relate to your Contacts/Accounts.

Once those steps are complete, reach out to Authorize.net to start the next step.


Manually Sync Your Data
If you do not have an existing Authorize.net gateway account, complete the following steps to move your data to Authorize.net.

1. Set your webhooks to inactive . If webhooks are turned on, your data will automatically sync from Authorize.net to Salesforce.
2. Reach out to Authorize.net to start the next step.
3. Once your Authorize.net gateway account is active, go to the next step.


Before you execute this task...

Con rm that your matching logic is set up correctly. Matching logic determines how this data will relate to your Contacts/Accounts.


Migrate Payment Methods and Customers
If you were an Authorize.net customer before coming to Blackthorn or you recently migrated your data to Authorize.net, you can manually sync your Authorize.net customers (Customer Pro le), Payment Methods (Payment Pro les), and Transactions to Salesforce.

This guide will help you understand our object model so you can easily sync the information using the Data Loader tool. Start by reviewing the tables below.


Customer Field Map
Salesforce Field Name                                                                                                                                                          Authorize.net Label
Payment Gateway Customer                                                                                                                                                                       Payment Pro le
Email                                                                                                                                                                                          Email
Name                                                                                                                                                                                           First Name + Last Name
Customer ID                                                                                                                                                                                    Customer Pro le ID
Description                                                                                                                                                                                    Description
Billing City (Optional)                                                                                                                                                                        City
Company                                                                                                                                                                                        Company
Postal Code(optional)                                                                                                                                                                          ZipPostal Code
Billing Street 1 (Optional)                                                                                                                                                                    Address
Billing State (Optional)                                                                                                                                                                       StateProvince
Billing Country                                                                                                                                                                                Country
Phone                                                                                                                                                                                          Phone


Payment Field Map
Salesforce Field Name                                                                                                                                                           Authorize.net Label
Payment Method                                                                                                                                                          Payment Pro le
Holder’s Name                                                                                                                                                           First Name + Last Name
Email (Optional)                                                                                                                                                        Email
Card ID                                                                                                                                                                 Payment Pro le ID
Customer ID                                                                                                                                                             Customer Pro le ID
Record Type(Card/ACH)                                                                                                                                                   Payment Type (CreditCard/Bank Account)
Street(Optional)                                                                                                                                                        Address
City(Optional)                                                                                                                                                          City
State (Optional)                                                                                                                                                        StateProvince
Country (Optional)                                                                                                                                                      Country
Last 4 Digits                                                                                                                                                           CardNumber (last 4 digits)
Payment Gateway (lookup)                                                                                                                                                Hardcode the PG id
Payment Gateway Customer(lookup)                                                                                                                                        Fetch id from SF
Payment Method Status                                                                                                                                                   Valid

1. Create a Payment Gateway in Salesforce and connect it to your Authorize.net account.
2. Export your customers and cards information from the Authorize.net gateway to an Excel document.
3. Convert the le to a CSV-type le.
4. The information in the CSV le will be mapped to the Payment Gateway Customer and Payment Method Salesforce objects. Prepare a second excel spreadsheet with the customer information mapping to respective elds on the Payment Gateway Customer/Payment Method objects.
5. In Salesforce, go to Custom Settings > Blackthorn | Payment Triggers > Edit > Disable all triggers.
6. Contact Blackthorn Support to disable CVV and Postal Code checks. (If you have information about the postal code, we can skip disabling this for you.)
7. Download the CSV le and import it into the Payment Gateway Customer using the Data Loader.
8. Export the new Payment Gateway Customer list from Salesforce and locate the Record ID.
9. Map the record ID in your Excel spreadsheet to the Payment Gateway Customer lookup eld on the Payment Method before importing.
10. Import the Payment Methods into Salesforce.
11. Go to Custom Settings to “Enable all triggers”.


Migrate Contacts and/or Accounts
To link the Contacts and/or Accounts to the Payment Gateway Customer or Payment Method records, complete the following steps.

1. Create a report in Salesforce for Contacts with the First Name , Last Name , Email , and Rec o rd I D elds.
2. Export them to a CSV le.
3. Create and export a report of all Payment Gateway Customer records with Name , Email , and Rec o rd I D elds.
4. In Sheet B, create a new column "Contact" and add the formula to match the contacts to the Payment Gateway Customer via email.
5. Download to CSV, and then import them back into Salesforce with size 1.
6. Once the Co ntac t lookup is set on the Payment Gateway Customer, it will auto-update the related Account as well as update all associated Payment Methods with the set Contact and Account.

This sync process only migrates your records from that moment backward. Syncing Authorize.net with Salesforce going forward can be done through webhooks, but you should not originate records outside of Salesforce.


Do you need to create a Contact record?

You can do so by creating a Process Builder that creates a Salesforce Contact record when the Authorize.net Customer record is created in Salesforce.


Instructions
If you have Transactional data outside of Authorize.net or Stripe and want it in Blackthorn, complete the following sections.

Transactions
Payment Methods
Recreating Records


Do you need to turn off callouts and Apex validations?

To temporarily turn off Stripe callouts and Apex validations, update the applicable custom settings under Blackthorn Pay - Trigger Settings.


Transactions
Source: CSV
Turn off all Transaction-related custom settings or check the Blackthorn Pay - Trigger Settings' custom setting Disable A ll T riggers checkbox.


Double Check Your Mapping

Map your org's Charge Record Type ID value, not the word "Charge". This can be found by navigating to the object's Record Type listing, clicking Charge, and pulling the ID from the URL.


Required Fields

Rec o rd T y pe = "Charge"
A mo unt
Currenc y I SO
T ransac tio n Status = "Completed"
P ay ment Status = "Captured"
No n-Gateway = "True"


Suggested Fields

A c c o unt
Co ntac t
P ro c essed Date (map a date eld if a date/time eld isn't available)


Suggested Fields if Records Originated from a Stripe Account

P ay ment Gateway
T ransac tio n I D
Custo mer I D

Upon completion, the So urc e eld on each Transaction will be set to "Sync".


Payment Methods
Source: Raw credit card data
Turn off all Payment Method-related custom settings or check the Blackthorn Pay - Trigger Settings' custom setting Disable A ll T riggers checkbox.


Double Check Your Mapping

Map your org's Record Type ID value, not the text word. This can be found by navigating to the object's RT listing, clicking Charge Card or ACH, and pulling the ID from the URL.


Required Fields

Rec o rd T y pe = "Charge Card" or "ACH"
Co ntac t


Suggested Fields

A c c o unt
Email
Address elds


1. Using the Data Loader, set your Batch Size to "1".
2. Stripe export with Card IDs & Customer IDs.


Map these Fields:

Last 4 Digits
Currenc y I SO
Co untry I SO
P ay ment Metho d Status = "Valid"


Recreating Records
Records that exist in Stripe but not in Salesforce can be recreated in Salesforce from the Stripe IDs.

Here's an example of recreating a charge so the refund can be conducted within Salesforce.

1. Log into the Stripe dashboard to see the relevant IDs.
Gather the following IDs:
Card ID
Customer ID
Transaction ID
2. Create a new Transaction in Salesforce.
a. Go to Setup > Custom Settings > Blackthorn Pay - Trigger Settings.
b. Click Manage and disable relevant triggers to manipulate records.
c. Fill in the following elds:
Rec o rd T y pe = "Charge"
A mo unt = Stripe Dashboard Charge amount
Currenc y I SO
T ransac tio n Status = "Completed"
P ay ment Status = "Captured"
Set the P ay ment Metho d lookup to the correct Payment Method that matches the Card ID from Step 1.
3. Click Refund in Salesforce.


FSL Overview

Use the Field Service Lightning (FSL) extension package to automate the creation of Transactions related to Work Orders. Work Order Line Items and Product Consumed objects automatically create and update the amount of money that needs to be collected from a job. That information can be used in the FSL extension package with our Mobile Payments app to
collect mobile payments.


Installing the Blackthorn FSL extension package allows customers to:

Create/Update an open Transaction automatically from a new/updated Product Consumed and Work Order Line Item.
Allows users to launch the Mobile Payments app right from the Work Order in the Field Service Mobile or from the Transaction in the Field Service Mobile.
Sets the Work Order object to be a "Transaction Parent" within the core Blackthorn Payments app.

Learn more about our Mobile Payments app here: Blackthorn | Mobile Payments.


Installation
The rst step is to install the latest extension packages and complete the setup process.


Enable the Field Service Package
1. Navigate to Setup > Field Service Settings.
2. Click Enable.


3. If you update any of the settings, click Save.


Install the SF Field Service Managed Package
If you haven't installed the Field Service Managed Packaged yet, install it now. (You can install the managed package in a production or sandbox org).

Click SF Field Service Managed Package and follow the prompts to install the managed package in your org.


Install the BT FSL Mobile Pay Extension
Prerequisite: To install the latest FSL Extension package, you must have Payments Version 5.31 or higher.

Install the latest Blackthorn Payments Mobile FSL Extension Package.


Setup

Con gure the Transaction Object
1. Click the Gear icon.
2. Click Setup.
3. Click the Object Manager tab.
4. In the Quick Find box, enter and click "Transaction."
5. Click the Page Layout tab.
6. Click the FSL Charge Transaction Layout.
7. Drag and drop the W o rk Order eld on the page layout.
8. Click Save.


1. Navigate to the Transaction object in Setup.
2. Click Edit on the Page Layout.
3. Add the W o rk Order lookup to the page layout.


Con gure the Work Order Object
1. Click the Gear icon.
2. Click Setup.
3. Click the Object Manager tab.
4. In the Quick Find box, enter and click "Work Order."
5. Click the Page Layout tab.
6. Click FSL Work Order Layout.
7. Click Related Lists.
8. Drag and drop the Transactions Related List to the page layout.


9. Click Fields.
10. Drag and drop the Mo bile P ay , Balanc e P aid , and Balanc e Due elds on the page layout.
11. Click Save.


Assign Permission Sets
1. Identify the users that will be using the Blackthorn FSL Extension Package.
2. Assign the Blackthorn | Payments FSL permission set to those users.


Add Field Service Permissions
1. From the App Launcher, type "Field Service Settings" and navigate to the app.
2. From the Getting Started step, click the Permission Sets tab.
3. Click Create Permissions for all the Roles.
4. Click Save.


Add Field Service Territory, Work Type, and Service Resource
1. Click the Getting Started tab.
2. Click Go to Guided Setup.


3. Create a Service Territory, Work Type, and Service Resource.


4. Click the Create Dispatchers and Agents step and click Add.
5. Choose users from Assign Service Territories to Select User.
6. Select the Service Territory.
7. Click Assign Service Territory.


Create FSL Records
Once you have installed and set up the FSL Extension, it's time to create FSL records.


Create a Work Order
1. Navigate to the Work Order object.
2. Click New to create a new Work Order record.
3. Add the required elds.
4. Make sure to de ne the P ric e Bo o k when creating the Work Order.
5. Click Save.


Create a Work Order Line Item
1. From the Work Order Line Item Related List on the Work Order you just created, click New to add a new Work Order Line Item record.
2. Add the required elds.
3. Be sure to set the P ro duc t and Quantity .
4. Click Save.


The Magic of the Blackthorn FSL Extension

When a Work Order Line Item is added to the Work Order and the Work Order's T o tal P ric e > 0 or the T o tal P ric e changes, a Transaction with T ransac tio n Status = "Open" is automatically created. If a Transaction with T ransac tio n Status = "Open" already exists, it will be updated to re ect the Work Order's Balanc e Due amount.


Create a Service Appointment

Service Appointments

If W o rk T y pe = "Auto-Create Service Appointment" on a Work Order or Work Order Line Item record, a child service appointment will be created. Review the Salesforce documentation about creating Service Appointments for more information.


1. Navigate to the Service Appointment object in the Related List on the Work Order that was created.


2. Click New to add a record.
3. Add the required elds.
4. Click Save.


Add a Service Resource
Adding a Service Resource lets you see your Work Order and related records in the FSL mobile app.


1. Go to the Service Resource Related List on the newly created Service Appointment record.
2. Click New to create a new Service Resource record.
3. Set a value for the U ser and Lo c atio n elds.
4. Set A c tiv e = "TRUE".
5. Click Save.


View Records in the FSL Mobile App
1. Go to the Field Service app on your mobile device.
2. Click the Service Appointment record that you have assigned to yourself (or to the user logged into the FSL Mobile app). Clicking the Service Appointment opens the Work Order.
3. Complete the payment process by either using the Mobile Pay option from Actions or by navigating to the Details tab and clicking Pay in the Mo bile P ay   eld.


Checklist
Blackthorn Payments allows you to accept payments within minutes of installing the app. However, certain steps need to be completed before going live.

The checklist below lists those steps in detail.

[ ] Create a live mode Payment Gateway record.
When creating the Payment Gateway record, set the Def ault checkbox to "True". This ensures that all live Transactions, Payment Methods, and Customers are created and captured correctly.


Stripe Payment Gateway

Do not change your Payment Gateway record from Test to Live mode by clicking Connect to Gateway. Instead, create a new record for your Payment Gateway in live mode. Review the instructions here.


[ ] Create a live Webhook URL in Stripe.
If you con gured webhooks while testing, there is one more step to complete. The last step is to create a Webhook URL for your Stripe account in live mode. Copy your test Webhook URL and update it with the live mode Payment Gateway's W ebho o k Label value. Then verify that the Webhook URL works correctly.

[ ] Enable the correct Blackthorn Payments permission sets for your team.
There are three Payments permission sets - Blackthorn | Payments (Admin), Blackthorn | Payments (Manager), and Blackthorn | Payments (User) - that you can assign to your team members. Each permission set provides a level of access to the Blackthorn Payments app. You can also clone any of the permission sets to personalize the access based on your
company's requirements.

[ ] Update your Account, Contact, and other parent objects' page layouts to include the Transaction, Payment Method, Payment Gateway Customer, and Payment Schedule objects as Related Lists.
You'll notice that all the payment processing objects give you the option to relate the record to an existing Account, Contact, and/or other de ned parent objects. Adding these objects as Related Lists gives you better visibility on payments for that particular Account, Contact, or Opportunity parent record.

[ ] Historical Sync of Stripe or Authorize.net Data.
Whether you were a new or existing Stripe or Authorize.net customer before installing Blackthorn Payments, there is an Historical Sync process for you to use to move your data to Salesforce.

[ ] Verify Customizations.
Verify that work ow rules, approval processes, email alerts, process builders, etc. are working correctly before going live.


Connect to Stripe in Live Mode

Are you ready to go live?

You cannot update the existing test Payment Gateway to live. This will result in an error. Please create a new Payment Gateway.


If you have refreshed a partial or full sandbox from Production, please create a template that does not include the Payment Gateway object. Otherwise, scheduled Transactions in production will be recaptured in the sandbox.

It's time to connect to your Stripe Account in live mode and create a new Payment Gateway to capture real Transactions.

This gateway should be marked as the default gateway instead of the test mode gateway.

1. Go to the Payments Setup Wizard.
2. Click Let's get started.


3. Set Select Provider = "Stripe" and Gateway Mode = "Live".


4. Click Connect.
5. Log into your production Stripe account and click Connect.


Troubleshooting
Q: I think I de ned the wrong object during the Relationship step. What do I do?

A: Complete the following steps to remove the relationship.

1. Go to Setup.
2. In the Quick Find box, enter and click "Custom Settings."
3. Click Manage next to "Blackthorn Pay - Transaction Parents."
4. Find the object/ eld you want to remove.
5. Click Del (Delete) next to the object/ eld.
6. Go to the Object Manager tab.
7. In the Quick Find box, enter and click "Transaction."
8. Open the relevant Transaction page layout.
9. Delete the lookup eld to the object you removed in Step 5.
10. Click Save.


Stripe Webhooks, Live Mode

Important

To use the following instructions, you must have Salesforce administrator access to Salesforce and Stripe.


Once you have connected to Stripe, it's time to con gure webhooks. Webhooks automatically send speci ed data from Stripe to Salesforce.

1. Go to Setup.
2. Type “Sites” in the Quick Find box.
3. Click Sites.
4. If a Force.com domain has not been set up, continue with the instructions. Otherwise, navigate to the steps for Site Con guration.
5. Enter your Force.com domain.
6. Click Check Availability.
7. Review and accept the Site terms of use.
8. Click Register My Force.com Domain.


9. Click New next to Sites.


10. Set Site Label = "Webhook".


11. The Site Name will auto-populate.
12. Click Default Web Address and enter the name you used for the Site Label .
13. Set A c tiv e = “TRUE”.
14. Click the Active Site Home Page lookup. (This will open a new window.)
15. Click InMaintenance.


16. Click Save.


17. Click the newly created Site Label.


18. Click Public Access Settings.


19. Click Assigned Users.


20. Click "Site Guest User, Webhook".


21. Add the Blackthorn | Payments (Site Guest User) permission set to this user's record.
For users looking to set up Webhooks with a Payments package older than v5.6, you will need to add the Blackthorn | Payments (Webhooks) permission set. Additionally, you will need to add a Sharing Rule to allow the Site Guest User to access the Payment Gateway object.
The Blackthorn | Payments (Site Guest User) permission set is now a dual-purpose permission set with packages v5.6 and beyond. This permission set will be used for webhook setup and REST API setup.


22. Go to Stripe and log into your test or production account.
23. Type "developers" and select “Developers > Webhooks”.


24. Click Add an endpoint.


25. Copy and paste the URL below into the Endpo int U RL eld. “https://SITE_DOMAIN_NAME/SITE_PATH/services/apexrest/bt_stripe/webhook/WEBHOOK_LABEL”


26. Without closing Stripe, go back to Salesforce and copy the Site URL you just created.


27. Replace https://SITE_DOMAIN_NAME/SITE_PATH with your Site URL.


28. Without closing Stripe, go back to Salesforce and click the App Launcher.


29. Select Blackthorn | Payments (Admin).


30. Click the Payment Gateways tab.


31. Go to the Payment Gateway you want to connect to webhooks and copy the value you placed in the W ebho o k Label .


32. Replace WEBHOOK_LABEL with the value from your Payment Gateway.


33. In the V ersio n eld, select the latest API version.


34. Click on Select events under “Select events to listen to.”


35. Check Selec t all ev ents .


36. Click Add events.


37. Click Add endpoint.


You now have successfully set up your Stripe Webhook!

Test the webhook connection by creating test Transactions, Subscriptions, or any other general payment processing tasks. You should see successful Webhook Events in your Stripe Dashboard.


Connect to Authorize.net in Live Mode

Are you ready to go live?

You cannot update the existing test Payment Gateway to live. This will result in an error. Please create a new Payment Gateway.


If you have refreshed a partial or full sandbox from Production, please create a template that does not include the Payment Gateway object. Otherwise, scheduled Transactions in production will be recaptured in the sandbox.

It's time to connect to your Authorize.net account! Follow the steps below to con gure you live Authorize.net gateway.

1. Click the App Launcher.


2. Type "Payment Gateways".


3. Click "Payment Gateways".
4. Click New.
5. Enter a P ay ment Gateway Name .
6. Set P ro v ider = “Authorize.net”.


7. Click Save.


8. Click the Connect to Gateway button.


9. Authorize.net's login page will launch in a new tab.
10. Enter your Username & Password.


11. Click LOG IN.


12. Click Allow.


The page will redirect back to Salesforce and you're all set!


Troubleshooting
Q: I think I de ned the wrong object during the Relationship step. What do I do?

A: Complete the following steps to remove the relationship.


1. Go to Setup.
2. In the Quick Find box, enter and click "Custom Settings."
3. Click Manage next to "Blackthorn Pay - Transaction Parents."
4. Find the object/ eld you want to remove.
5. Click Del (Delete) next to the object/ eld.
6. Go to the Object Manager tab.
7. In the Quick Find box, enter and click "Transaction."
8. Open the relevant Transaction page layout.
9. Delete the lookup eld to the object you removed in Step 5.
10. Click Save.


Authorize.net Webhooks, Live Mode

Important

To use the following instructions, you must have Salesforce administrator access to Salesforce and Authorize.net.


Once you have connected to Authorize.net, it's time to con gure webhooks. Webhooks automatically send speci ed data from Authorize.net to Salesforce.

1. Go to Setup.
2. Type “Sites” in the Quick Find box.
3. Click Sites.
4. If a Force.com domain has not been set up, follow the instructions to create one. If have have a Force.com domain, go to the next step.


Con gure your Site
1. Enter a value for your Force.com domain.
2. Click Check Availability.
3. Review and accept the Site terms of use.
4. Click Register My Force.com Domain.


5. Click New next to Sites.


6. Set Site Label = "Webhook".


7. The Site Name eld will auto populate.


8. In Def ault W eb A ddress , type in the same name you used for the Site Label .


9. Set A c tiv e = “True”.


10. Click the Active Site Home Page lookup. This will open a new window.
11. Click InMaintenance.


12. Click Save.


13. Click the newly created Site Label .


14. Click Public Access Settings.


15. Click Assigned Users.


16. Click Site Guest User, Webhook.


17. Add the Blackthorn | Payments (Site Guest User) permission set to this user's record.
For users who want to set up webhooks with a Payments package older than v5.6, you will need to add the Blackthorn | Payments (Webhooks) permission set. You will also need to add a Sharing Rule to allow the Site Guest User to access the Payment Gateway object.
For packages v5.6 and later, the Blackthorn | Payments (Site Guest User) permission set is now a dual-purpose permission set. This permission set will be used for webhook setup and REST API setup.


Go to Authorize.net
1. Log into your test or production account.
2. Click ACCOUNT.


3. Click Webhooks.


4. Click Add Endpoint.


5. De ne a Name for the endpoint.


6. Copy and paste the URL below into the Endpo int U RL eld.
"https://SITE_DOMAIN_NAME/SITE_PATH/services/apexrest/bt_stripe/webhook/WEBHOOK_LABEL"


7. Without closing Authorize.net, go back to Salesforce and copy the Site URL for the Site you created.


8. Replace “https://SITE_DOMAIN_NAME/SITE_PATH” with your Site URL.


9. Without closing Authorize.net, go back to Salesforce and click the App Launcher.


10. Select Blackthorn | Payments (Admin).


11. Click the Payment Gateways tab.


12. Go to the Payment Gateway record you want to connect to webhooks and copy the value you placed in the W ebho o k Label eld.


13. Replace “WEBHOOK_LABEL” with the value from your Payment Gateway.


14. Set Status = “Active”.


15. Check A ll Ev ents .


16. Click Save.

You have successfully setup your Authorize.net webhook!


Connect to Spreedly in Live Mode

Was the wrong object de ned during the Relationship step?

1. Navigate to Custom Settings from Setup.
2. Click Manage next to the Transaction parent custom setting.
3. Click Remove next to the object.
4. Navigate to the Transaction object and delete the lookup eld to that object.


It's time to connect to your Payment Gateway through Spreedly! The setup process is the same as for test mode, but this time it’s in live mode.

1. Click on the App Launcher and type "admin".


2. Click on "Blackthorn | Payments (Admin)".


3. Click on "Blackthorn | Payments Setup Wizard".


4. Watch the Overview Video then click Let's get started.


5. Currently, you can't connect to Spreedly from the Setup Wizard. Please select the Skip button under the connect to gateway instructions.
6. If you plan to use ACH, select “Yes” and click Make Magic Happen. This will deploy the ACH record type for the Payment Method object.


7. Permission Sets - Select "No" and click Next. You have already assigned permission sets.


8. Relationship Settings - MOST IMPORTANT SETTING.
When a business charges a customer in Salesforce, there is an object that represents what's being sold, typically Opportunity, Quote, or similar. By default, we associate Opportunities, Contacts, Accounts, and Invoices to Transactions. If you need to associate Transactions to a different object, please select that object from the drop-down.


9. Watch the Virtual Terminal Overview video or click Continue.


10. That’s it! Click Show me my rst transaction, and you’ve completed the Payment Wizard.


Create a Spreedly Payment Gateway
1. Contact Blackthorn Support to obtain a live mode Spreedly Environment Key. The live mode key is different than the test mode key.
2. Navigate to the Payment Gateway object.
3. Click New.


4. Enter a P ay ment Gateway Name .


5. Set P ro v ider = “Spreedly”.


6. Leave the T est Mo de checkbox unchecked for a live Payment Gateway in production.


7. Populate the Def ault Currenc y and Def ault Co untry      elds.


8. Enter the live mode key provided by Blackthorn Support in the Spreedly Env iro nment Key        eld.


9. Click Save.


10. Click the Create Spreedly Gateway button.
11. Select the Payment Gateway you want to connect (Ex. CardConnect; EBANX).
12. If prompted, add additional information from the selected gateway.
13. Click Create.
14. The Spreedly Co nf igured Gateway and Gateway T o k en elds will be populated automatically.


Add a CyberSource Payment Gateway
1. Contact Blackthorn Support to obtain a Spreedly Environment Key.
2. Navigate to the Payment Gateway object.
3. Click New.
4. Enter a P ay ment Gateway Name .
5. Set P ro v ider = “Spreedly”.
6. Leave the T est Mo de checkbox blank. Only check if you are setting this up in your sandbox for testing.
7. Populate the Def ault Currenc y and Def ault Co untry      elds.
8. Enter the key provided by Blackthorn Support in the Spreedly Env iro nment Key       eld.


9. Click Save.
10. Click the Create Spreedly Gateway button.
11. Select the CyberSource Payment Gateway.
12. Enter the Transaction Key and Username.
Use the SOAP toolkit key you created in Cybersource as the Transaction Key.
Use the Merchant ID from CyberSource as the Username. (Where do I nd the Merchant ID?)
13. Click Create.
14. The Spreedly Co nf igured Gateway and Gateway T o k en elds will be populated automatically.


PayLink: Automated PayLink with Opportunities

Scenario
A common use case is that a salesperson will close an Opportunity and send the customer a link to the payment request.

To do this, you can build three things without using code.

A Process Builder process to automatically create a Transaction record when the Opportunity Stage = "Closed Won".
A Process Builder process to automatically roll-up the PayLink on to the Opportunity record.
A Work ow Rule with an Email Alert to automatically email the PayLink to the customer.


Instructions

Step One
1. Create a custom URL type eld on the Opportunity object called P ay Link .
2. Create a lookup type eld on the Opportunity object called Billing Co ntac t that looks to the Contact object and is ltered by the Account record on the Opportunity. This is for sending a Work ow email all from one object (Opportunity).
3. Alternatively, roll-up a related Opportunity Contact Role record from the Opportunity to populate this value too.


Step Two
Auto-create the Blackthorn Payments Transaction from the "Closed Won" Opportunity.

1. Create a new Process Builder.
2. Set T he pro c ess starts when to "A record changes".
3. Click + Add Object.
4. Type in "Opportunity", and select "when a record is created or edited".
5. Click Save.
6. Click + Add Criteria.
7. Enter a Criteria Name and select "Conditions are met" for Criteria f o r Ex ec uting A c tio ns .
8. Under Field , nd the Opportunity Stage , set Operato r to "Equals", and pick "Closed Won" for the V alue .
9. Under IMMEDIATE ACTIONS, click + Add Action.
10. A c tio n T y pe = "Create a Record"
11. Ender an A c tio n Name and set Rec o rd T y pe to "Transaction".
12. Under Set Field Values, enter the following information.

Field                                                                                      Type                                                                                                                                    Value
Amount                                                                                  Formula                                                                                          [Opportunity].Amount
Opportunity                                                                             Field Reference                                                                                  [Opportunity].Id
Description                                                                             Formula                                                                                          [Opportunity].Description
Due Date                                                                                Formula                                                                                          [Opportunity].CloseDate
Contact                                                                                 Field Reference                                                                                  [Opportunity].Billing_Contact

13. Activate the Process Builder.

As an alternative to the Co ntac t eld, you can populate the A c c o unt lookup eld on the Transaction object with the Opportunity A c c o unt Name eld. However, if you want both lookup elds on the Transaction, the A c c o unt lookup will supersede the A c c o unt Name lookup when viewing the PayLink form.


Step Three
Auto roll-up the PayLink from Transaction to Opportunity. This will allow you to use the PayLink in the Email Alert.

1. Create a new Process Builder.
2. Set T he pro c ess starts when to "A record changes".
3. Click + Add Object, type in "Transaction", and select "only when a record is created".
4. Click Save.
5. Click + Add Criteria, name your criteria and select " Conditions are met".
6. Under eld, nd Transaction Oppo rtunity , set operator to "IS NULL", type to "Boolean" and pick "False" for the value.
This criteria tells the process to only re when the Transaction has a related Opportunity.
7. Under Immediate Actions, click + Add Action.
8. A c tio n T y pe = Update Records, enter your A c tio n Name and set Rec o rd T y pe = "Opportunity".
9. No criteria-just update the records!


10. Field = P ay Link ; Type = Formula; Value = "[bt_stripeTransactionc].bt_paylinkPayLinkc".
11. Activate the Process Builder.


Step Four
Create a Work ow Rule with an Email Alert to automatically email the PayLink to the customer.

1. Create the Email Template.
Here is an example Email Template.


2. Create the Work ow Rule and Email Alert. This will email your customer when the Opportunity Stage = "Closed Won", and there is a P ay Link value.


Here is an example Work ow Rule and Email Alert.


When P ayLink eld is not empty and the Opportunity Stage = "Closed Won" then send PayLink to customer.


Boom! Done.


Additional Use Cases
If you have any suggestions for a use case with Blackthorn Payments please contact Blackthorn Support and provide details on your use case. We always appreciate hearing the solutions our customers create and love sharing that with our other customers!


Transaction Reattempt Noti cations

Failed Transaction Follow Up Automation
When Transactions fail and are reattempted, it is a good practice to follow up with the customer to notify them and update their card or bank account information if the Transaction continues to fail.


For the use case below, we will be creating a Process in Process Builder to send out an automated Email Alert to the customer on the second reattempt and then notify the Transaction owner via a Chatter Post on the third reattempt.


Step One - Create an Email Template and an Email Alert
These two records will be referenced later in Process Builder.


Create an Email Template
1. From Setup, navigate to:
Lightning: Email > Classic Email Templates
Classic: Administration Setup > Communication Templates > Classic Email Templates
2. Click New Template
3. Under "Choose the type of email template you would like to create," select "Text".
4. Click Next.
5. Under "Available Merge Fields" set Selec t Field T y pe = "Transaction Fields".


Be sure to only use merge elds from the Transaction object for this template. Merged elds from other objects will not populate.


6. Select the folder where you want to store your Email Template.
7. A v ailable Fo r U se checkbox should be checked
8. Enter an Email T emplate Name and T emplate U nique Name .
9. Enter a Desc riptio n .
10. Enter a Subjec t and an Email Bo dy using a combination of text and Transaction merge elds


Create an Email Alert
1. From Setup, navigate to:
Lightning: Process Automation > Work ow Actions > Email Alerts
Classic: Create > Work ow & Approvals > Email Alerts
2. Click New Email A lert .
3. Enter a Desc riptio n and U nique Name .
4. For Objec t , select "Transaction".
5. For Email T emplate , nd and select your template from the prior step.


If you cannot locate your Email Template, please go back to the Template and make sure Available for Use is checked.


6. For Rec ipient T y pe , select "Email Field".
7. In the A v ailable Rec ipients column, select "Email Field: Payment Method Billing Email" and use the Add/Remove buttons to move the value into the Selec ted Rec ipients column.
8. If desired, enter any A dditio nal Emails .
9. Select the correct Fro m Email A ddress .
10. Click Save.


Step Two: Build the Process Using Process Builder
Create a Process with the Process Builder to automatically send out an Email Alert to notify the Customer of a second reattempt, as well as post to Chatter to notify the Transaction owner after the third reattempt.


Create a New Process
1. From Setup, navigate to:
Lightning: Process Automation > Process Builder
Classic: Create > Work ow & Approvals > Process Builder
2. Click New.
3. Enter the P ro c ess Name , A P I Name , and Desc riptio n .
4. Set T he pro c ess starts when to "A record changes."


Select the Object for the Process
1. On the canvas, click Add Object.
2. For the Objec t eld, select "Transaction".
3. Under Start the P ro c es , select "when a record is created or edited".
4. Click Save.


De ne the Criteria that Triggers the Process and De ne your Actions

Second Reattempt Criteria

1. On the canvas, click + Add Criteria.
2. Enter the Criteria Name .
3. Set Criteria f o r Ex ec uting A c tio ns to"Conditions are met".
4. Under Set Conditions, complete the following elds.
Field = "Reattempt Number"
Operato r = "Equals"
T y pe = "Number"
V alue = "2"
5. Set Co nditio ns to "All of the conditions are met (AND)".
6. Click Save.


Second Reattempt Action 1

1. On the canvas under IMMEDIATE ACTIONS, click + Add Action.
2. For A c tio n T y pe , select "Email Alerts".
3. Enter an A c tio n Name .
4. Enter the Email Alert created in Step One in the Email A lert eld.
5. Click Save.


Third Reattempt Criteria

1. Under your last element on the canvas, click + Add Criteria.
2. Enter the Criteria Name .
3. Under Criteria f o r Ex ec uting A c tio ns , select "Conditions are Met".
4. Under Set Conditions, complete the following elds
Field = "Reattempt Number"
Operato r = "Equals"
T y pe = "Number"
V alue = "3"
5. Set Co nditio ns to "All of the conditions are met (AND)".
6. Click Save.


Third Reattempt Action 1

1. On the canvas under IMMEDIATE ACTIONS, click + Add Action.
2. For A c tio n T y pe , select "Post to Chatter".
3. Enter an A c tio n Name .
4. Under P o st to , select "This Record".


Feed Tracking

The "Post to Chatter" option is only visible if the feed for Transaction object is enabled. Setup > Search for Feed Tracking > Select Transaction > Enable Feed Tracking > Save.


5. In the Message eld, enter your custom message.
Example Message: @[{![bt_stripe__Transaction__c].OwnerId}] Contact the customer on this Transaction. Their Payment Method is incorrect and needs to be updated in order for the Transaction to process. An email has already been sent with a PayLink to update their Payment Method.
6. Click Save.
7. Click Activate.


On the third reattempt, a Chatter post will automatically be created and the Transaction owner noti ed.


Additional Use Cases
If you have any suggestions for a use case with Blackthorn Payments please contact Blackthorn Support and provide details on your use case. We always appreciate hearing the solutions our customers create and love sharing that with our other customers!


Virtual Terminal

Prepopulating Examples

Related To Field: Opportunity.Account -> Transaction.Account


Currency ISO Field
1. Create a custom picklist eld called Currenc y I SO on your Opportunity parent object.
2. Insert the same values as the Currenc y I SO eld from the Transaction. Only include the Currency ISO values that you need.
3. Set a default value for this custom eld, ie "USD".
4. Create a new custom metadata type record.
Name: Opp_Currency_ISO
Label: Opp->Trans Currency
Screen: Single Transaction
Source Object: Opportunity
Source Field: Currency ISO
Target Object: Transaction
Target Field: Currency ISO
5. Click Save.


Description Field: Opportunity.Description -> Transaction.Description


Custom Field: Lead.Lead Source -> Transaction. Lead Source


Additional Use Cases
If you have any suggestions for a use case with Blackthorn Payments please contact Blackthorn Support and provide details on your use case. We always appreciate hearing the solutions our customers create and love sharing that with our other customers!


Payments: Objects
These custom objects are the bread and butter of Blackthorn Payments.


Allocations
The Allocation object allows you to allocate funds to multiple Line Items on the same Invoice from a single Transaction. For example, when a payment is made for four Invoices using the same Transaction, Allocations help to split the funds across those four Invoices.


Blackthorn Logs
Blackthorn Log records store application errors captured in our code as well as some batch job information.


Company Info
The Company Info object houses information regarding your company or companies.


Custom Metadata Types
This Metadata Type automatically installs metadata records into your org.


Disputes
The Dispute object receives disputes and allows you to submit evidence and upload les in defense.


Line Items
Line Items store price and quantity information for items related to an Invoice. A Stripe Line Item Record Type is used to create Invoice Items for an Invoice in Stripe Billing.


Payment Gateway
The Payment Gateway object connects your Stripe account to Salesforce.


Payment Gateway Customer
The Payment Gateway Customer object connects your Salesforce customers (Accounts and/or Contacts) with your Customer accounts in Stripe.


Payment Methods
The Payment Method object stores the methods by which you charge your customers.


Payment Schedules
The Payment Schedule object allows you to create a variety of forward-looking, scheduled (recurring) Transactions.


Invoices
An Invoice Record Type Invoice can be used to invoice a customer and apply charge Transactions to record a payment. A Stripe Invoice Record Type is used to create an Transaction in Stripe Billing.


Transactions
The Transaction object is used to capture, authorize, and refund Transactions, create payouts to external accounts, transfer funds between Stripe accounts and provide adjustment Transactions from Stripe.


Webhook Events
The Webhook Event object captures data from Stripe that needs to be dispersed in Salesforce.


Overview
Allocations allow you to distribute funds from a single Transaction to either multiple Invoices or multiple Line Items on one Invoice. For example, when a payment is made for four Invoices using the same Transaction, Allocations help to split the funds across those four Invoices.


Use Cases
1. You receive a bulk payment and distribute the payment across multiple Invoices. For example, one $10,000 payment can be applied from one Transaction across multiple Line Items on the same Invoice.
2. Auto-create an Allocation record for each Line Item as part of a paid Event checkout.
3. Manually create full or partial refund Allocations between a Transaction and one or more Line Items.


Write-Off Allocation Feature
This feature empowers users to de ne the process for creating write-off Transactions based on their unique requirements. Admins have the exibility to implement Allocations using a variety of tools including Screen ows, Approval Processes, and other custom work ows to generate write-off Transactions.

Write-off Transactions also provide a way to deduct amounts from an Invoice while maintaining an accurate, individual record of the Transaction. This provides granular level control of how amounts (payments/refunds/write offs) are allocated and recorded for reporting purposes.


How It Works
The Allocation object now supports a Transaction with T ransac tio n T y pe = “Write Off”. When an Allocation record is created, it's related to an Invoice, a Line Item, and a Transaction. The Allocation record represents the allocation of a partial amount of the total Transaction A mo unt to a particular Line Item on an Invoice.

The Invoice object also includes the W rite Of f A mo unt eld which automatically adds up all the write-off Transactions associated with each Invoice. The write-off total is also considered when calculating the Invoice roll-up eld values in the Totals and Financials section of the Invoice page layout.


New Fields
Invoice object: W rite Of f A mo unt eld
Field Label: W rite Of f A mo unt
API Name: bt_stripe__Write_Off_Amount__c
Description: If write-off Transactions are related, then this eld is automatically populated. If no write-off Transactions are present, then this eld will be blank.
Line Item object: A mo unt W ritten Of f eld
Field Label: A mo unt W ritten Of f
API Name: bt_stripe__Amount_Written_Off__c
Description: Auto-populates when a write off Allocation is related to Line Item.


Parent Object Relationship
Allocations are related to Invoice, Line Item, and Transaction objects. The Allocation's I nv o ic e lookup eld is automatically populated by the Line Item's I nv o ic e eld. This connection relates the Allocation record to the Line Item, Invoice, and the Transaction that paid for the Invoice.

With the addition of the write-off Allocation, the following updates will be made when an Allocation record is created.

The related Line Item elds will be updated.
A mo unt W ritten Of f
Balanc e Due = T o tal - (Balanc e P aid + A mo unt W ritten Of f )
The related Invoice eld will be updated.
A llo c atio n Ro llup eld = Line Item Balanc e P aid - (Line Item A mo unt Ref unded + Line Item A mo unt W ritten Of f )
The Line Item’s Balanc e Due eld updates to re ect changes to Line Item elds, including U nit P ric e , Quantity , and W rite Of f A mo unt .


Allocation Rollup Calculations
The following calculations include write-off amounts and the new elds on the Invoice and Line Item records.


Balance Paid
When Allocation T y pe = "Payment" is associated with a Line Item object, the value is automatically rolled up to the Line Item’s Balanc e P aid .


Amount Refunded
When Allocation T y pe = "Refund" is associated with a Line Item object, the value is automatically rolled up to the Line Item’s A mo unt Ref unded .


Amount Written Off
When Allocation T y pe = "Write Off" is associated with a Line Item object, the value automatically rolled up to the Line Item’s A mo unt W ritten Of f .


Balance Due
Line Item Balanc e Due = Line Item T o tal - (Line Item Balanc e P aid + Line Item A mo unt W ritten Of f )


Retained Amount
Line Item Retained A mo unt = Line Item Balanc e P aid - (Line Item A mo unt Ref unded )


Total
Line Item T o tal = Line Item Net + Line Item T ax - Line Item W rite Of f A mo unt


Allocation Rollup
Invoice A llo c atio n Ro llup = (the sum of all Allocation T y pe = “Payment”) – (The sum of all Allocation T y pe = “Refund” + the sum of all Allocation T y pe = “Write off”)


Automate the Allocation Creation for Event Checkout
You can automate the Allocation creation for Event checkouts.

1. Navigate to Blackthorn | Payment Trigger Settings (Setup > Custom Settings).


2. Click Manage.


3. Set the A uto matic ally Create A llo c atio n = "True".


4. Click Save.

When this setting is enabled and an Invoice is created by the checkout process, the Allocations are automatically created for the Line Items and Invoice.


Scenarios for Payment and Refund Types

Pre-requisite
Determine the A mo unt that you will use for the allocation before you begin the process. You cannot allocate more than the amount that is submitted.


Allocate Funds to Multiple Line Items on One Invoice
1. Navigate to the Allocation object.
Lightning: Click the App Launcher > Search for and click Allocations.
Classic: Click "All Tabs" ("+" icon in the top right) > Click Allocation.


2. Click New.
3. Enter information in the following elds.
A mo unt : The amount to allocate to the related Invoice or Line Item.
T ransac tio n : The Transaction that paid for the Line Item.
Line I tem : The Line Item the Allocation is associated with.
I nv o ic e (optional): Automatically populates if the Line I tem eld is set. Populate this eld only if the Allocation is not associated with a Line Item.
T y pe : Set this eld to either "Payment" or "Refund" depending on the type of Allocation. The default setting is "Payment."
4. Click Save.


Allocate Funds to Multiple Invoices
1. Navigate to the Allocation object.
Lightning: Click the App Launcher > Search for and click Allocations.
Classic: Click "All Tabs" ("+" icon in the top right) > Click Allocation.


2. Click New.
3. Enter information in the following elds.
A mo unt : The amount to allocate to the related Invoice or Line Item.
T ransac tio n : The Transaction that paid for the Line Item.
I nv o ic e : This eld determines which Invoice this Allocation is associated with.
T y pe : Set this eld to either "Payment" or "Refund" depending on the type of Allocation. The default setting is "Payment."
4. Click Save.


Use Allocation to show Refunds on Line Item and Invoice
You can use Allocations to handle refunds against the Line Items or the Invoice.


1. Create an Allocation record.
2. Set Allocation type = "Refund."
3. Set the Line I tem /I nv o ic e lookup eld. Setting a Line I tem lookup will auto-populate the I nv o ic e .
4. Select the refund T ransac tio n for the Allocation.
5. Click Save.


Overview
When an Allocation with T y pe = “Write Off” is created, then the related Invoice’s W rite Of f A mo unt eld will include - “the sum of all the amounts in the Invoice’s related Line Item’s A mo unt W ritten Of f elds.”

The Invoice’s Balanc e Due should be reduced by the Invoice’s W rite Of f A mo unt . (Invoice Balanc e Due = Invoice T o tal A mo unt - (Invoice Balanc e P aid + Invoice W rite Of f A mo unt ))

If a Transaction with T ransac tio n T y pe = “Write Off” is created, then an Allocation with T y pe = “Write Off” will be created.

When a Transaction with T ransac tio n T y pe = “Write Off” and an A mo unt less than the Invoice’s Balanc e Due is created, then a related Allocation record with T y pe = “Write Off” will be created.

If a Transaction with T ransac tio n T y pe = “Write Off” or T ransac tio n T y pe = “Charge” is created and the Transaction A mo unt = Invoice’s Balanc e Due , then an Allocation with T y pe = “Write Off” will be created and the Transaction with T ransac tio n T y pe = “Charge” will have Transaction’s P ay ment Status = “Captured”.

When the Invoice’s Balanc e Due = ”0”, then the Invoice Status = “Completed” and the Transaction’s P ay ment Status = “Paid”.


Create a Write-off Allocation
1. Go to Custom Setting > Blackthorn Pay – Trigger Settings.
2. Set A uto matic ally Create A llo c atio n = “True” (checked).
3. Create an Invoice with one or more Line Items that have a Balanc e Due .
4. Create a Transaction with T ransac tio n T y pe = “Write Off”.
5. Verify a related Allocation record was created.
6. Create a new Transaction with Rec o rd T y pe = “Charge”
a. Enter an A mo unt .
b. Change the T ransac tio n T y pe to “Write Off”.
c. Change T ransac tio n Status to “Complete”.
7. The Invoice’s W rite Of f A mo unt = “the sum of all the amounts in the Invoice’s related Line Item’s A mo unt W ritten Of f elds.”
8. Invoice’s Balanc e Due = Invoice T o tal A mo unt - Invoice W rite Of f A mo unt
9. TheInvoice’s Status should change to “Completed” when the Balanc e Due = “0”.
10. The P ay ment Status will update to “Partially Paid` once the Balanc e Due is less than the T o tal A mo unt . The P ay ment Status will update to “Paid” once the Balanc e Due = “0”.


Rollup Allocation Amounts and the Invoice Payment Status
When an Invoice is manually charged through a Transaction with T ransac tio n T y pe = “Write Off”, the following is true.

The Invoice W rite Of f A mo unt value is the same as the Allocation’s A mo unt eld.
An Allocation record with T y pe = “Write Off” is created.
The Line Item A mo unt W ritten Of f value is the same as the Allocation’s A mo unt eld.

When an Invoice is manually captured, the following in true.

The Line Item Balanc e P aid is the same as the Allocation (T y pe = “Payment”)’s A mo unt eld.

When an Invoice with the P ay ment Status set to “Paid” or “Partially Paid” is refunded, the following is true.

The Line Item A mo unt Ref unded is the same as the Allocation (T y pe = “Payment”)’s A mo unt eld.


Scenarios

When the write off is less than the full balance of single Line Item
1. Create an Invoice with a Line Item.
2. Manually create a write-off Transaction for an amount less than the Balanc e Due .
3. Verify that an Allocation with T y pe = "Write Off" was created.
a. The Line I tem , I nv o ic e , and T ransac tio n lookups should be populated.
b. The A mo unt should equal the W rite Of f A mo unt .

When a Transaction with T ransac tio n T y pe = “Write Off” is created manually for an A mo unt that is less than the Invoice’s Balanc e Due , then the Allocation’s Line I tem , I nv o ic e , and T ransac tio n lookups will be populated, and the Allocation A mo unt will be equal to the Transaction's (T ransac tio n T y pe = “Write Off”) A mo unt .


When the write off is less than full balance of multiple Line Items
1. Create an Invoice with multiple Line Items.
2. Manually create a write-off Transaction for an amount more than the Balanc e Due on line 1 but less than the total Invoice's Balanc e Due .
3. Verify that an Allocation with T y pe = "Write Off" was created.
a. The Line I tem , I nv o ic e , and T ransac tio n lookups should be populated.
b. The rst Allocation should equal the full Balanc e Due for line 1.
c. The second Allocation should be for the remainder of the W rite Of f A mo unt .

When a Transaction with T ransac tio n T y pe = “Write Off” is created manually for an A mo unt that is less than the Invoice’s Balanc e Due , then the Allocation’s Line I tem , I nv o ic e , and T ransac tio n lookups will be populated.

The rst Allocation A mo unt will be equal to the rst Line Item’s Balanc e Due . The second Allocation A mo unt will include the remainder of the write-off Transaction A mo unt .


When the write-off balance is part of a partially paid Invoice
1. Create an Invoice with one or more Line Items.
2. Process a partial payment for less than the Invoice's Balanc e Due .
3. Create a write-off Transaction for the remaining balance on the Invoice.
4. Verify that Allocations with T y pe = "Write Off" was created correctly based on the Line Items you created. The Allocation should be applied only to lines with a Balanc e Due .

When a Transaction with T ransac tio n T y pe = “Write Off” is created manually for a partially paid Invoice with multiple Line Items, the write-off Allocations will only be applied to the Line Item(s) with a Balanc e Due .

The Allocation’s Line I tem , I nv o ic e , and T ransac tio n look-up elds will also be populated.


Allocation Fields
Field Label                                  Field Name                         Data Type                                                                   Description
Allocation Name                 Name                                        Auto Number                       The automatically assigned name of the Allocation.
Amount                          bt_stripe__Amount__c                        Currency(16, 2)                   The amount to allocate to the related Invoice or Line Item.
Created By                      CreatedById                                 Lookup(User)
Invoice                         bt_stripe__Sales_Document__c                Lookup(Invoice)                   The related Invoice
Last Modi ed By                 LastModi edById                             Lookup(User)
Line Item                       bt_stripe__Line_Item__c                     Lookup(Line Item)                 The Line Item that the Allocation is related to.
Owner                           OwnerId                                     Lookup(User,Group)
Transaction                     bt_stripe__Transaction__c                   Lookup(Transaction)               The Transaction that the Allocation is related to.
Type                            bt_stripe__Type__c                          Picklist                          Select the type of Allocation - Payment, Refund, or Write Off


Blackthorn Logs
The Blackthorn Log object captures errors and performance issues related to Blackthorn Payments so that you can trace, report, and troubleshoot issues.

Records are automatically created and related to the records that threw an error.


Use Cases

Troubleshooting Event Registration Issues
Blackthorn Logs are instrumental in identifying why an Event Registration Submission (ERS) record might fail. This capability is crucial for ensuring Attendees receive con rmation emails and that their registration process is smooth


Preventing Data Loss
Blackthorn Logs play a vital role in preventing the loss of registration data or payments, which is essential for maintaining the integrity of the event registration process


Batch Processing of Records
In scenarios with high concurrent registrations, Blackthorn Logs can be used to monitor and manage batch processing of ERS records, ensuring that the registration process is ef cient and error-free


Blackthorn | Payments Log Record Cleanup
Blackthorn Logs older than 30 days are deleted by the Blackthorn | Payments Log Record Cleanup scheduled batch job.

All processed Webhook Events are also retained for 30 days but this can be customized by changing the Blackthorn Pay - Trigger Settings - Retain W ebho o k Rec o rds (f o r Day s) custom setting eld. The Blackthorn | Payments Webhook Record Cleanup scheduled job runs these deletes.


We don't start the scheduled jobs from the install handler. You need to schedule them to run from the Scheduled Jobs tab on the Blackthorn | Payments Admin screen.


Company Info

"Company Info" was previously known as "Legal Entity."

As of the Payments v4.169 release, the Legal Entity object has been renamed to Company Info. The API Name did not change.


The Company Info record contains information about your individual company or companies. This record can be used to relate multiple Payment Gateways under one Entity.

For example, if you have two separate Stripe accounts, both can be connected to one Company Info record. Thus, ensuring the monies are separated per Stripe account but under one Entity making, audits and tax information simple.

For Blackthorn Payments, enter as much or as little information as you would like to in the Company Info record.


Create a Company Info Record
1. From the App Launcher, enter and click “Company Info.”
2. Click New.


Company Information
Complete the following elds.

Co mpany I nf o Name – name of the company
EI N - Employer Identi cation Number
Registratio n Number – Company Registration Number; different than the EIN
V A T – Value Added Tax
Merc hant Catego ry Co de – classi es a business based on the goods or services they provide.
Go o gle T ag Manager I d - used on all Event webpages built in Blackthorn Events
Currenc y I SO – the currency the company uses to report its nancial information
FY Start Mo nth – the month the company’s scal year starts
Fav ic o n U RL – the URL to the Favicon icon/image used on the Events platform
U se Fo r A ll Ev ents - Check to use this Company Info record for all Event platform pages.


EIN vs Registration Number
You can add an Employer Identi cation Number (EI N ) or registration number (Registratio n Number ) to your Company Info record. The EI N or Registratio n Number will be visible below the company’s address on the DocumentLink Invoice.

The following logic explains when each number is used.

The EI N will be listed on the Invoice if the related Company Info record’s EI N eld or both the EI N and Registratio n Number elds have a value.
The Registration Number will be displayed when only the Registratio n Number eld has a value. The EI N eld must be blank.
"EIN" is the EI N eld’s default label on the Invoice. Customers can use the Data Dictionary to override the "EIN" label. For example, Australian customers might change the label to "ABN" instead.


Primary Contact Information
Complete the following elds.

P ho ne
Email
W ebsite
Desc riptio n
Street A ddress
City
State o r P ro v inc e
P o stal Co de
Co untry


PayLink/DocumentLink Branding
Complete the following eld.

Lo go – the logo that will be displayed on the company’s PayLink and DocumentLink


3. Click Save.

Instructions for the Company Info record and each add-on are in each feature’s documentation.


Disputes

What is a Dispute?

Introduction
A Dispute is a situation in which a customer questions the validity of a Transaction that was registered to their account.

If you are unfamiliar with how Disputes are received, the associated fees, or what to submit, please review Stripe's documentation.


Setup
Create a webhook between Stripe and Salesforce.


Testing Disputes
In order to test Disputes you will need to use a speci c test credit card created for a dispute simulation.


Receiving a Dispute
Navigate to the Dispute object.


Plaintext                                                                                                                                                                                                                                                                 Copy

* ***Lightning:** Navigate to app launcher > Under "All Items" select Dispute.*
* ***Classic:** Click "All Tabs" (The "+" icon in the top right corner) > select Dispute.*


A Dispute record is created through Webhook Events with the Status = "Needs Response."
The disputed Transaction's P ay ment Status changes from "Captured" to "Disputed" and a refund Transaction is created for the captured amount. The Stripe fee for the dispute will also be populated on the P ay ment Gateway Fee eld on the refund Transaction.


Disputed Transaction


If you notice that two refund Transactions are created when you receive a Dispute, this is because the old dispute logic operated in this manner. Please upgrade to the latest Payments package to see the most recent dispute logic.


When receiving a Dispute, you have until the Due By date to formally respond and submit all supporting evidence.
The Dispute Reaso n is what the cardholder de ned the disputed payment as. Dispute reasons
The Ref undable , Has Ev idenc e , and P ast Due elds track where the disputed record is in the process.These elds can be used as noti cation lters in a Work ow, Process Builder, or Reports to make sure Disputes are submitted before being past due.
After adding your Dispute Evidence and clicking Submit, the Submissio n Co unt = "1" and the Status = "Under Review". It has now been submitted to Stripe's nancial partner for review and no changes can be made.
If you won the Dispute, Status will update to "Won". If the card issuer won the Dispute, Status will update to "Lost". Once a Dispute has been "Won" or "Lost", Stripe will send out an email with the Dispute information.


Notes

Important note from Stripe: If you receive a Dispute, try contacting your customer and discuss it before you respond. It’s possible that they simply did not recognize or remember the Transaction when they viewed their statement.
Stripe will charge you a [
15.00 Dispute fee](https://stripe.com/docs/disputes#fees) (for users in the United States) by the card network. If you win the {{variable.Object_Dispute}}, the original amount will be refunded to you and a
15.00 adjustment Transaction will be created for you to cover the original Stripe fee.
ACH disputes cannot be contested. If you receive an ACH dispute the Dispute Status = "Lost" and the original Transaction's P ay ment Status will update to "Refunded".


Dispute Evidence
The purpose of the Dispute Evidence object is to submit evidence in defense of your Dispute that will push to Stripe. Review all evidence before clicking Submit, as you cannot update evidence once submitted.

There are four different Rec o rd T y pe s for Dispute Evidence. Rec o rd T y pe s are used because not all elds are relevant for all Dispute types (as is designed in the Stripe dashboard), however, if you do need access to other elds as part of the Dispute, you can add them to the Page Layout or update the same data set in the Stripe dashboard:

Basic Response
Physical Product
Digital Product or Service
Of ine Service


Creating a New Dispute Evidence Record


1. Navigate to the Dispute Evidence object.

Lightning/Classic: Navigate to the Dispute record > under Related Lists, click New for Dispute Evidence.

2. Select a Rec o rd T y pe and click Next.
3. P ro duc t Desc riptio n , Custo mer Name , Custo mer Email , Billing A ddress , and Custo mer I P A ddress are general elds for all Product Categories and should be lled out unless they are not applicable.
4. Stripe Data elds will populate automatically once the Dispute Evidence has been submitted.

Note

Enter as much information as you can into all sections of the Dispute Evidence record. Stripe provides best practice recommendations for preparing suitable responses. Click here.


Upload Documentation
Documentation can be uploaded through the Upload Files button under the Dispute Evidence Related List.


1. Click Upload Files.
2. Upload all relevant documentation.
3. Click the "Title" link of all uploaded le(s).
4. Click Go To Content Page (Classic UI - located in the top right of the page) or click Edit File Details (Lightning UI - pencil icon in the top right of the page).
Can't nd the Go To Content Page link? You might not have "Salesforce CRM Content User" enabled on your user record.


5. Under Content Details, click edit, and select Edit Content Details (Classic UI).
6. Click T y pe and select the available type for your uploaded documentation.Can't see the T ype eld in Lightning? Edit the Content Version Page Layout to include the T ype eld.
7. Click Save. Perform this process for each uploaded le.

Notes
* There is no limit to the number of les you can upload.
* Upload documents per T y pe , do not combine all documents into one le upload.
* Evidence cannot be added to Lost Disputes.

8. When you have uploaded and de ned the T y pe of your documentation you are ready to submit your evidence.


Submit Dispute Evidence


1. Navigate to your Dispute Evidence record.
2. Click the Submit button.
Once you click the Submit button, you can no longer edit, delete, or add anything to the record.

What happens when you submit evidence?

Evidence is submitted to Stripe's nancial partner.
No one can edit, delete, or add anything to the Dispute record.
Dispute Status = "Under Review".
Dispute Submissio n Co unt = "1".
Dispute Has Ev idenc e = "TRUE".

Then you wait...50-75 days for a response :)

Submitting Evidence in Stripe:

If you submit evidence in the Stripe Dashboard (as opposed to Salesforce), all evidence information will get created in Salesforce as Webhook Events.

The Dispute Evidence record will relate to the open Dispute.
File I D elds will populate with a Stripe Id if a document was uploaded for that particular T y pe .


NOTE:
Learn more about evidence submission.


Accept, Withdraw, and Refund Disputes

Accept
Closing the Dispute for a charge indicates that you do not have any evidence to submit and are dismissing the Dispute, or acknowledging it as lost. The disputed amount and $15 fee will not be reimbursed.

Steps to Accept a Dispute:

1. Navigate to the Dispute record.
2. Click Accept Dispute button.
3. The Status will be updated to "Lost".

Losing a Dispute will update the original Transaction's P ay ment Status to "Refunded".


Withdrawn
If your customer has created a Dispute in error and plans to withdraw it, you will need to submit proof in Dispute Evidence that the customer made a mistake.

When a Dispute is withdrawn:

The Dispute Status = "Won".
The original Transaction A mo unt will be refunded to you.
An adjustment Transaction for $15.00 will be created. This is Stripe reimbursing you for the Dispute fee.
P ay ment Status on the original Transaction will update to "Captured."


Refund
If you are refunding a customer that has withdrawn their Dispute, it can take up to 75 days to refund the payment because the disputed claim must close rst.

Trying to refund a Transaction before the Dispute is closed will result in a failed Transaction.

Steps for refunding a withdrawn Dispute:

1. Once the Dispute Status = "Won", navigate back to the original Transaction.
2. Click Refund at the top of the page (Classic UI) or click the drop-down arrow and select "Refund" (Lightning UI).

Additional information on refunding a withdrawn Dispute.


Troubleshooting
If you have received an error with Disputes or have a question, please view our Troubleshooting or FAQ page.


Invoices
There are two core objects: Invoice and Line Item. Line Items work as a related object to the Invoice.

You can send invoices to your customers for payment over the web using DocumentLink.


New Field

The Invoice record has a new eld called Dy namic Fee Name . The eld is populated only when an Invoice related to an Event with an associated tax Fee is created or updated. The eld’s value will then be used in DocumentLink’s Invoice to override the Tax column’s label. Click here for more information about using Fees with Events.


Before Creating an Invoice
Before you create Invoice, you should create a Company Info record with your logo and company information and complete the Payments Setup Wizard.

1. Complete the Payments Setup Wizard
2. Create a Company Info record. (The address, name, and logo that you enter here are rendered on the Invoice.)
3. Create a DocumentLink Template record. Set the lookups to the Payment Gateway and Company Info. When you create your Invoice, set the lookup to the Do c umentLink T emplate to default your Invoice's con guration and merge elds.
4. Authorize DocumentLink.


Is the date format on your Invoice incorrect?

Check your browser's location setting. All date elds on an Invoice will re ect the appropriate date format based on your browser's location setting.


Invoice Calculations

Gross Amount
Gro ss A mo unt (bt_stripe__Net_Amount__c): The sum or total amount across all Line Item records before anything is deducted.


Discount
Disc o unt (bt_stripe__Discount_Amount__c): The sum or total amount of all Line Item Disc o unt and Line Item Co de Disc o unt A mo unt values for all related Line Items.


Net Amount
Net A mo unt (bt_stripe__Subtotal_Amount__c):

= Invoice Gro ss A mo unt - Invoice Disc o unt

OR

= the sum or total amount of all Invoice Net A mo unt values for all related Line Items


Tax Amount (for Events only)
T ax A mo unt (bt_stripe__Tax_Amount__c): the sum or total amount of all Invoice T ax A mo unt values for all related Line Items.


Fee Amount (for Events only)
Fee A mo unt (bt_stripe__Fee_Amount__c):


= the total amount due (without fees) * Event P ay ment P ro c essing Fee

OR

= the sum or total amount of all Invoice Fee A mo unt values for all related Line Items


Total Amount
T o tal A mo unt (bt_stripe__Total_Amount__c) = Net A mo unt + T ax A mo unt + Fee A mo unt


Create an Invoice
1. In the app launcher eld, search for and click "Invoice" (the Blackthorn Custom Object, not the SF Standard Object).
2. Click New in the top-right corner.
3. Select either the "Stripe Invoice" or "Invoice" record type.
4. Set the values for:
Name
The Name eld is automatically generated with an "INV" pre x and an ordered numeric string. For example, your rst Invoice will be named "INV-1". This can be edited for any custom needs. This value will be rendered beneath the word "Invoice" on the DocumentLink document. This value is also written to the Desc riptio n eld of the related
Transaction record(s).
Subjec t
P O Number
P ay ment T erm
Due Date
P ay ment Gateway
De ning the Payment Gateway tells the system which Stripe account the money should go to.
Enabled P ay ment Metho ds
De ne how you would like to be paid for the Invoice - Card, ACH or both. Keep in mind that ACH transactions have a $5.00 capped fee which is an inexpensive fee compared to cards which have a percentage based fee.
Co mpany I nf o
Disc o unt Co de
If a discount Code has been created, de ne the record here.
Co ntac t (Bill T o ) The Email and P ho ne elds will automatically pull in the related Contact's email and phone values.
A c c o unt (Bill T o )
The address elds will automatically pull in the related Account's billing address.
A c c o unt (Ship T o )
The address elds will automatically pull in the related Account's shipping address.
Do c umentLink T emplate
The DocumentLink elds will automatically pull in the related DocumentLink Template elds.
T ax A mo unt
The T ax A mo unt eld can be manually de ned to calculate the percentage of taxes you want added to a Transaction.
W rite Of f A mo unt
If write-off Transactions are related, the W rite Of f A mo unt eld is automatically populated. If there are no write-off Transactions present, then the eld will be blank.
5. The Currenc y I SO , Status and P ay ment Status elds are automatically de ned with default values.
Currenc y I SO = "USD"
Status = "Draft"
P ay ment Status = "Unpaid" (only on Invoices)
6. The Do c umentLink eld is automatically generated with a random alphanumeric link. This link is used to render the Invoice online.


7. Click Save.


8. Click the Do c umentLink link.


Once your Invoice is completed, you are ready to view the Invoice through the web-based and mobile responsive DocumentLink.


Additional Field Worth Noting

A llo c atio n Ro llup : Sum of all Allocations for this Invoice.


Auto-convert Opportunities to Invoices

Add the Create Invoice Button

If the Create Invoice button isn't already on the Opportunity page layout, you must add it before proceeding.


You can convert an existing Opportunity to an Invoice by clicking the Create Invoice button. All Opportunity Line Items will also be converted to Line Items on the Invoice.

The newly created Invoice will be linked to the original Opportunity via the Invoice's Oppo rtunity lookup eld. Since an Opportunity can be related to many Invoices, the Oppo rtunity   eld is needed.

The Line I tem lookup eld on the Opportunity Product (OpportunityLineItem) facilitates mapping between the Invoice's Line Item and the Opportunity Product's Line Item.

This allows you to self-map additional Opportunity Product Line Item elds, such as the custom tax eld, to the Invoice using a process builder when an Invoice is created from an Opportunity.


Can I receive a noti cation when the Invoice's Status changes?

Yes, you can. Create a process builder that noti es the record owner when the Invoice's Status updates to accepted or rejected.


Invoice Payment
Once the Transaction related to the Invoice has been captured (manually or with DocumentLink) and if the Invoice Balanc e Due = "0", then the related Invoice P ay ment Status = "Paid", the Status = "Completed", and P aid I n Full = the current date/time.


Refunds
Sometimes you need to refund an Invoice. A refund can be either a full or partial refund. Refunding part or all of an Invoice won’t trigger a change to the original Invoice. The Invoice’s P ay ment Status will show "Paid" and the Balanc e P aid will show the amount of the original Transaction. The Invoice’s Balanc e P aid eld is not changed after a refund occurs
because refund & adjustment transactions are not considered in rollups.

A new Transaction will be created with the A mo unt equal to the refund amount, showing that part or all of the original Transaction was refunded.


Please be aware of the following functionality.

If changes are made to the Invoice before the Webhook Events related to the refunded Transaction are processed, the Invoice's P ay ment Status , Balanc e P aid , and Balanc e Due elds will revert to their original values.

To avoid this, please make any manual adjustments to the Invoice record’s refunded Line Item after the Webhook Events related to the refund Transaction have been processed.

The Webhook Event processing job runs every ve minutes, so the waiting time after refunding the Transaction is usually up to ve minutes. You will be able to see the Webhook Event records from the refunded Transaction on the Transaction’s Webhook Events Related List.


Rollup Fields
The logic used for refunds on an Invoice also impacts the rollup elds in the Event record’s nancial summary.

If you want the Event’s Balanc e P aid , Gro ss , Net , and T o tal elds to be updated when a registered Attendee receives a full or partial refund, use the Blackthorn Pay - Trigger Settings custom settings’ I nc lude ref unds in ro llup c alc ulatio ns (Include_Refunds_in_Rollup_Calculations__c) eld. The eld is unchecked (disabled) by default.


Full Refund
If an Event Organizer checks the I nc lude ref unds in ro llup c alc ulatio ns eld and processes a full refund, the refunded Transactions will be re ected on the Invoice record, and the Event’s Balanc e P aid eld will be updated to “P aid - Ref und ” or zero.


Partial Refund
For partial refunds, the refunded Transactions are re ected on the Invoice record, the related Event’s Balanc e P aid eld is updated to “P aid - Ref und ”, and the Gro ss , Net , and T o tal elds are updated.


Examples
Background: An Attendee registers for a paid Event and pays the $100 due. An Invoice is then generated for the Transaction.

Scenario 1: Full Refunds/Custom Setting Enabled
The Blackthorn Pay - Trigger Settings' I nc lude ref unds in ro llup c alc ulatio ns eld is checked (enabled), and a full refund is processed; the Event’s nancial summaries will re ect a full refund.

Ex. When an Attendee receives a full refund ($100), the Event record’s Balanc e P aid eld will be updated to “0.”

Scenario 2: Partial Refund/Custom Setting Enabled
The Blackthorn Pay - Trigger Settings' I nc lude ref unds in ro llup c alc ulatio ns eld is checked (enabled). When a partial refund is processed, the Event’s nancial summaries will re ect a partial refund.

Ex. When an Attendee receives a partial refund of $50, the Event record’s nancial summary elds will update as follows.

The Balanc e P aid eld will be updated to “$50.”
The Gro ss eld will be updated to “$50.”
The Net eld will be updated to “$50.”
The T o tal eld will be updated to “$50.”

Scenario 3: Custom Setting Disabled
If the Blackthorn Pay - Trigger Settings I nc lude ref unds in ro llup c alc ulatio ns eld is unchecked (disabled), and a full or partial refund is processed, the following will occur:

The Invoice will not be updated with new totals.
Only the initial payment Transaction amounts should be shown.


Line Items
A Line Item record stores price and quantity information for items related to an Invoice. You can create a one-off Line Item or create one that references Event Items or Salesforce Products and Price Books.

Line Item records can also be created automatically as part of the Event checkout process.


Will you be using standard Salesforce objects?

We suggest using the P ro duc t and P ric e Bo o k elds if you are going to create Invoices from standard Salesforce objects like Opportunities or Orders as those records already relate to Products.


Important Fields & Calculations

Fields
If any of the following elds are not on the Line Item page layout, please add them manually.

Field Label                                            API Name                                                                                                                                                                 Description
Unit Price                           bt_stripe__Unit_Price__c                                        The price for each unit of the Line Item
Quantity                             bt_stripe__Quantity__c                                          The quantity selected for a Line Item
Tax Rate                             bt_stripe__Tax_Rate__c                                          The tax rate for this Line Item. Set by the associated Event T ax Fee . Automatically set to 0 if the Event Item’s T ax -Ex empt is set to “True” (checked).
Discount Code                        bt_stripe__Code__c                                              The lookup for the associated discount Code record
Discount                             bt_stripe__Discount_Amount__c                                   The discount amount for this Line Item


Calculations

Code Discount Amount
Co de Disc o unt A mo unt (bt_stripe__Code_Discount_Amount__c): The calculated Disc o unt (bt_stripe__Discount_Amount__c) related to the discount Code applied.


Gross
Gro ss (bt_stripe__Net_Amount__c) = U nit P ric e * Quantity


Net
Net (bt_stripe__Subtotal_Amount__c) = Gro ss (bt_stripe__Net_Amount__c) - Disc o unt (bt_stripe__Discount_Amount__c)


Tax
T ax (bt_stripe__Tax_Amount__c) = Net (bt_stripe__Subtotal_Amount__c) * T ax Rate (bt_stripe__Tax_Rate__c)


Total
T o tal (bt_stripe__Total_Amount__c) = Net (bt_stripe__Subtotal_Amount__c) + T ax (bt_stripe__Tax_Amount__c)


Add Line Items to your Order or Invoice
1. Navigate to your Order or Invoice record.
2. Click New next to the Line Item Related List, .
3. Set the values for the following elds.
I tem Name
Serv ic e Start Date
Serv ic e End Date
I nv o ic e
P ro duc t
P ric e Bo o k
U nit P ric e
Quantity - If the left blank, the default value is "1."
Co de Disc o unt A mo unt
Ev ent
Ev ent I tem
Desc riptio n (Limit of 60 characters.)
T ax Rate
Disc o unt Co de
4. A dditio nal Disc o unt A mo unt and A dditio nal Disc o unt P erc entage
You can de ne these elds manually, or they will automatically be de ned when setting a Disc o unt Co de . For example,
if you de ne a Disc o unt Co de that provides $10.00 off, the A dditio nal Disc o unt A mo unt eld will show $10.00.
if a Disc o unt Co de is not de ned, you can manually enter a one-off discount in either eld.
5. Click Save.

Repeat the above process for all Line Items.


Now that you have added all Line Item to your Order or Invoice, click here to learn how DocumentLink works so that you can send this Invoice to your customer.


Use Salesforce Products and Price Books
Setting the P ro duc t and P ric e Bo o k elds on a Line Item automatically copies the values on those records to the Line Item elds when the record is saved.

The P ro duc t and P ric e Bo o k are optional. If a P ro duc t is set on the Line Item but not a P ric e Bo o k , the logic will set the Standard Pricebook in the P ric e Bo o k eld.

When a Line Item record is saved:

Values are pulled from the related Product and set on I tem Name , Co de and Desc riptio n elds if the corresponding Line Item eld is blank.
Values are pulled from the Pricebook Entry (based on the related Price Book and Product) and set on List U nit P ric e and U nit P ric e elds if the Line Item eld is blank.

Once the elds are set, none of the Line Item elds listed in the section above will be updated by the related Product or Pricebook.

This allows you to easily create Invoice Line Items from objects that use Salesforce Product and Price Book while also providing the exibility to set Line Item elds manually or from some other custom process.

Initial Setup: If the P ro duc t , P ric e Bo o k , and List U nit P ric e elds are not on your Line Item page layout, please add them.

Lightning -> Navigate to setup > search for "Object Manager" > type in and select "Line Items" > edit the Page Layout and add the three elds.

Classic -> Navigate to setup > search for "Objects" > type in and select "Line Items" > edit the Page Layout and add the three elds.


Payment Gateway

The following elds were added to the Payment Gateway object.

Field Name: TouchNet uPay Site ID
API Name: bt_stripe__TouchNet_uPay_Site_ID__c
Data Type: Text(15)
Field Name: TouchNet uPay Site URL
API Name: bt_stripe__TouchNet_uPay_Site_URL__c
Text(255)


In Blackthorn Payments, a Payment Gateway record is synonymous with a gateway account (i.e. Stripe, Authorize.net etc.) account. Each Payment Gateway record you create connects your Salesforce org to one gateway account, in either test or live mode. To have your gateway account in both test and live mode, create two Payment Gateway records. There is no
limit on the number of Payment Gateway accounts you can connect to your org.


Note on Payment Gateway Records

Do not change your Payment Gateway record from test mode to live mode or vice versa by clicking Connect to Gateway or checking/unchecking the T est Mo de checkbox. Instead, create a new record for the other mode you wish to enable.


Supported Payment Gateway Providers
Blackthorn supports several Payment Gateway providers. The primary Payment Gateway providers are Stripe, Authorize.net, and Spreedly. Blackthorn also supports the providers below via one of the primary providers.


Stripe
Plaintext                                                                                                                                                                                                                                                                                                                                                  Copy

* Apple Pay
* Google Pay
* Alipay
* Bacs Direct Debit
* Bancontact
* EPS
* iDEAL
* Plaid (must be set up in Stripe)
* SEPA Direct Debit


Cybersource
via Spreedly - fully tested


Spreedly
The following Spreedly processors are used by Blackthorn customers.


Braintree
Cardconnect
Elavon
eWAY
Fat Zebra
Litle
Orbital
Pay ow Pro
Paypal
Sage


What is the fee per transaction when using PayPal as a payment gateway?

The fee per transaction when using PayPal as a payment gateway is 3.49% + a at fee depending on the country. The at fee for the USA is 0.49 USD (standard rate).


Events and Catalog Checkout
Blackthorn also supports two Payment Gateway providers that only work with Events checkout.

TouchNet
CashNet


First Payment Gateway Record
Your rst Payment Gateway record, named "primary" was created automatically during the Setup Wizard. Follow the steps below to locate it.

1. Open the Blackthorn | Payments (Admin) app.
2. Click the Payment Gateways tab.
3. Select All from the list of List Views.
4. Click on the record named "primary".

If you connected to your gateway account in test mode, the T est Mo de      eld will be checked.

The primary Payment Gateway record includes the following.

The Def ault eld is checked.
Objects with a P ayme nt Gate w ay lookup eld (such as a Transaction and Payment Method) will default to the Payment Gateway record with the De f ault eld checked if the P ayme nt Gate w ay eld is blank.
The Gateway Information section provides all the connection details.
If these elds are blank, the data in Salesforce will not process in the gateway. Do not copy your Stripe API keys and insert them here as these keys are different than your Stripe keys (they are OAuth keys). You can only get them by clicking the Connect to Gateway button.


Create Payment Gateway Records (for Stripe)
Instructions for Authorize.net


Create a Payment Gateway for Stripe
Each Stripe account mode (test and live) needs its own Payment Gateway record. This is to ensure that your data is separated from "Live" and "Test".

If you connected to your account in T est Mo de during setup, create a new Stripe Payment Gateway record for live mode.


1. Open the Blackthorn | Payments (Admin) app.
2. Click the Payment Gateways tab.
3. Click New.
4. Populate the following elds:
P ay ment Gateway Name (required)
P ro v ider (required)
W ebho o k Label = Name for the webhook URL. This is needed to con gure webhooks.
Def ault = Check this eld if you want this as your default Payment Gateway.


If you have multiple Stripe Payment Gateways, you can change which one is the default.
T est Mo de = Check this eld if you are connecting to your Stripe account in test mode.
5. Click Save.
6. Click Connect to Gateway.
7. Enter your Stripe credentials.

Once you sign in, all elds under the "Gateway Information" section in the Payment Gateway record will be lled out.


Syncing Stripe Data to Salesforce

There won't be data in the Related Lists section. Connecting to your Stripe Account does not automatically sync existing data to Salesforce. If you have data in your Stripe Account that needs to be moved to Salesforce, review the Historical Sync documentation.


Available and Pending Balances
The Payment Gateway object allows you to track an compare your available and pending balances for both Salesforce and Stripe.


Stripe
Stripe Balanc e A v ailable and Stripe Balanc e P ending
These elds are updated via the Stripe's Balance.Available or Account.Updated Webhook Events.

Stripe Balanc e Last U pdated
This date and time eld is updated when the balances are updated, giving you an insight as to when the two balances were last updated.

Held in Reserv e
This eld shows the funds held in reserve due to negative balances on Connected Accounts. Stripe automatically updates this eld via a webhook.


Salesforce
Calc ulate Salesf o rc e Balanc es Fro m
This eld is for calculating historical transactions that were processed through Stripe before the balance elds were packaged.

Salesf o rc e Balanc e A v ailable and Salesf o rc e Balanc e P ending
These elds are automatically calculated based on the related Transactions.

If the related Transaction's Balanc e Status = "Available," then the Retained Net A mo unt is rolled up to the Salesf o rc e Balanc e A v ailable .
If the Transaction's Balanc e Status is "Pending," then the Retained Net A mo unt is rolled up to the Salesf o rc e Balanc e P ending .

Stripe Balanc e Last U pdated
This date and time eld that is updated when the balances are updated.

Balanc e(s) I nc o rrec t
When this eld is checked, it means the Stripe Balanc e A v ailable and Salesf o rc e Balanc e A v ailable elds, and the Stripe Balanc e P ending and Salesf o rc e Balanc e P ending elds do not match. Often, they don't match because the timing of the Stripe webhook and the Salesforce batch process doesn't line up.

Update Balance Button
Clicking this button forces a daily apex job to update the Salesforce and Stripe available and pending balances immediately.


IMPORTANT

If you have a high Transaction volume, don't click the Update Balance button. You will run into a query limit error.


Scheduled Apex Job
The Blackthorn | Payments Balance Update scheduled job runs daily. It updates the Stripe Balanc e A v ailable , Stripe Balanc e P ending , Salesf o rc e Balanc e A v ailable , and Salesf o rc e Balanc e P ending elds on the Payment Gateway record(s).

1. Navigate to Setup.
2. In the Quick Find box, enter and click "Scheduled Jobs."


Block Amex Payment Methods
Some providers, like Stripe, charge higher fees to use an American Express payment method. To help customers mitigate the extra fees, we added the Blo c k A mex T ransac tio ns I n Rest A P I eld to the Payment Gateway object to block Transactions from the REST API that attempt to charge a payment with an American Express card. This eld can be used with
the following.

PayLink
DocumentLink
REST API requests (custom front-end code)

Remember to add this eld to your Payment Gateway page layout if you want to use it.

Here's what a customer may see if the Blo c k A mex T ransac tio ns I n Rest A P I checkbox = "True" (checked).


Payment Gateway Owner - Known Limitation
If you have con gured a Sharing Rule for the Payment Gateway object, there is a known limitation in Salesforce. If the Payment Gateway Owner = "Automated Process User", Sharing Rules won't be applied. The work around is to update the Owner eld to re ect another user in your org such as the System Administrator. Read more about this here.


Delete a Payment Gateway
Before you can delete a Payment Gateway, you must rst delete any related Payment Gateway Customers and Payment Methods from the Payment Gateway.

1. Open the Payment Gateway record and review the Payment Gateway Customer and Payment Method Related Lists.


2. Open a Payment Gateway Customer record.
3. In the navigation menu, click Remove From Gateway.


4. The Deleted Fro m P ay ment Gateway         eld will be checked.


5. Repeat the process for any other related Payment Gateway Customer records.
6. Open a Payment Method record.
7. Click Remove From Gateway.


8. Go back to the Payment Gateway record.
9. In the record’s navigation, click Delete.


The Payment Gateway record is now deleted.


Troubleshooting
If you have received an error with your Payment Gateway or have a question, please view our Troubleshooting or FAQ page.


Payment Gateway Customer

Matching Rule Update

Users upgrading Payments will need to manually deactivate the current Payment Gateway Customer Dup Rule matching rule and activate the new Payment_Gateway_Customer_Matching_Rule2 matching rule. The new matching rule will be installed automatically for new installations.


The Payment Gateway Customer object connects your Salesforce customers' (Accounts and/or Contacts) with your Stripe customers' accounts. Stripe maintains a single entity by which cards, payments, and all other Stripe records relate to (something like a Person Account in Salesforce). All Stripe related data ultimately relates back to a Payment Gateway
Customer record (except with Stripe Connect).

This object works mainly in the background and requires no user setup. For example, a new Payment Method will either trigger the creation of a new Payment Gateway Customer record or relate to an existing one based on the Payment Method's Email and related Payment Gateway.


Note on Account, Contact, and Lead Matching

Matching Payment Gateway Customers to Accounts, Contacts, or Leads when these lookup elds are blank now uses your active standard or custom Salesforce Duplicate Rules and their associated Matching Rules.

Click here to learn more about the criteria evaluated in the Salesforce Standard Matching rules.

Click here to learn more about creating custom matching rules and click here to learn how to use those matching rules in custom Duplicate Rules.


Matching, PGC Records, and the Mobile Payments App
To prevent duplicate Payment Gateway Customer (PGC) records from being created when using the Mobile Payments app and a card reader, the following changes were made.

If a payment is submitted and a Contact or Account is selected, the Contact/Account will be related so future payments are matched to the existing PGC, preventing duplicate PGC records from being generated.
If a PGC record can't be matched to an id, we will attempt to match the PGC record against the parent Contact/Account and use the parent’s PGC record instead of creating a new record. If we nd an exact match, we will reuse the existing PGC record.


Example
The following records exist: PGC 1 is related to Account 1 and Contact 3.

Scenario 1: If a new Transaction is created. It is related to only Contact 3. The Transaction would generate a new PGC record called PGC 2.
Scenario 2: A second Transaction is created. Transaction 2 is related to Account 1 and Contact 3. Transaction 2 will use PGC 1.
Scenario 3: A third Transaction is created. Transaction 3 is only related to Contact 3. Transaction 3 will use PGC 2.


About the Payment Gateway Customer Record


1. Click the App Launcher.
2. Enter and click "Payment Gateway Customer."
3. Click on the Name of a Payment Gateway Customer.
If you don't see any Payment Gateway Customer records, that means you have not created any Payment Methods or synced any data from Stripe.

Email and Desc riptio n are the only two elds on the record that will update between Stripe and Salesforce when Webhooks is con gured.
The "Related To" elds A c c o unt and Co ntac t are lookup type elds to the standard Account and Contact objects.
They are automatically lled in from the related Payment Method's Co ntac t and/or Ac c o unt values.
A c c o unt Balanc e : The customer's current balance.
Co upo n : When de ned, the customer will have a discount applied on all recurring charges.
I nv o ic e P ref ix : The pre x for the customer used to generate unique invoice numbers.
Billing P o stal Co de

Note
Place the Payment Gateway Customer object on your Account and Contact page layouts as a Related List if you have multiple Payment Gateways. Since there can only be one Payment Gateway Customer to one Payment Gateway, you will be able to tell which Accounts and/or Contacts are on more than one Payment Gateway.


Create a Payment Gateway Customer


Option 1
1. Click the App Launcher.
2. Enter and click "Payment Gateway Customer."
3. Click New.
4. Populate the Name , P ay ment Gateway , Email , and Desc riptio n elds.
5. If you want to relate this Payment Gateway Customer to an existing Account and/or Contact, add the existing record(s) under the "Related To" section.
6. Click Save.

This record will sync with your Payment Gateway and the Custo mer I D and Created I n Gateway             elds will auto-populate.


Option 2


1. Add the Account’s billing and shipping addresses.


2. Create and set a Contact to be the Primary Stripe Contact.


3. On the Account click the Create Stripe Customer button.


4. Con rm that a Payment Gateway Customer was created and related to the Account.


Option 3
1. Add the Push To Gateway button to your Payment Gateway Customer page layout.
2. Navigate to Custom Settings > Blackthorn Pay - Trigger Settings > Manage > Edit > Enable Disable Creating a Stripe Customer .

3. Navigate to the Payment Gateway Customer object.
4. Click New.
5. Populate the Name , P ay ment Gateway , Email , and Desc riptio n elds.
6. Click Save.
7. Click Push To Gateway.
8. Click the Push button on the Visualforce page.
9. After the success message displays and you return to the Payment Gateway Customer record, the Custo mer I D and Created I n Gateway   elds will auto-populate.


Updating a Payment Gateway Customer Record

Using Option 3 without performing Step 2 will also work if the initial trigger action never happened or if you are updating the Payment Gateway Customer record and you notice that the update did not make it to the Payment Gateway.


Linking a New Payment Method to a PGC
When a user creates a new Payment Method, one of the following scenarios will occur.


Scenario 1

A Contact exists on the Payment Method, and the Contact is associated with an Account.

If Salesforce nds a Payment Gateway Customer where both the Contact and Account match, then the new Payment Method will be linked to that Payment Gateway Customer.


Scenario 2
A Contact exists on the Payment Method. The related Account and Contact do not have a matching Payment Gateway Customer.

Salesforce searches for an existing Payment Gateway Customer with a billing email address that matches the email address associated with the Payment Method.

If the resulting Payment Gateway Customer has the same Account, then the Payment Method will be linked to that Payment Gateway Customer.


Scenario 3
A Contact exists on the Payment Method, and the Contact is associated with an Account.

Salesforce cannot nd a matching Payment Gateway Customer by searching Contact and Account records, nor by searching by the billing email address.

Therefore, Salesforce creates a new Payment Gateway Customer for the Payment Method.

A new Payment Gateway Customer will be created even if another Payment Gateway Customer is related to the Account that is associated with the Payment Method. If they do not match, they will not be associated.


Remove a Payment Gateway Customer
Once a Payment Gateway Customer record in Salesforce has synced to the Stripe Payment Gateway, you are unable to delete the record. If you need to remove a Payment Gateway Customer for any reason, that can be done by clicking the Remove From Gateway button or checking the Remo v e Fro m Gateway checkbox. This functionality was created so
historical information can be kept while ceasing all ways to capture transactions.


1. Navigate to the Payment Gateway Customer's object.

Lightning: Click on the app launcher > Under "All Items" > Click on Payment Gateway Customers.

Classic: Click on "All Tabs" ("+" icon in the top right) > Click on Payment Gateway Customers.

Related List on your Account or Contact page layout.

Click on the record you want to remove from Stripe.
Click Remove From Gateway button or check the Remo v e Fro m Gateway         eld.
Clicking this button will invalidate any related Payment Method's on le.
The Deleted Fro m P ay ment Gateway       eld will be checked, letting you know this Payment Gateway Customer is no longer valid.

Notes
If the Payment Gateway Customer had any related Transactions that were captured, those records will still be in the Stripe Payment Gateway and the Customer account will show an alert, "This customer account has been permanently closed".

If you have any "Open" Transactions that are set to Auto-Process and related to this Payment Gateway Customer record, they will fail. Verify all related "Open" Transactions have been deleted once you click the Remove From Gateway button.


Troubleshooting
If you have received an error with your Payment Gateway Customer or have a question, please view our Troubleshooting or FAQ page.


Payment Methods

Introduction
The purpose of the Payment Method object is to store the method by which you charge your customers. Payment Method types are segmented by Rec o rd T y pe and can be related to Accounts, Contacts, and/or other objects.

Blackthorn Payments is built with PCI compliance in mind, we never store sensitive Payment Method details. Click here for information on PCI compliance.


Obtain Payment Methods
To capture card or bank account information from a customer, there are multiple, PCI compliant, options using Blackthorn Payments.


Phone
If you are not recording your phone calls (if you are, this goes against the tenants of PCI compliance)...

Payment Method Object
Manually enter the Payment Method through the Card or ACH Rec o rd T y pe . A real-time API call sends the record to Stripe/Authorize.net to tokenize the Payment Method information. A card can be veri ed within seconds, where for Stripe ACH Payment Methods, it takes 4-5 days to be veri ed.
Virtual Terminal
Manually enter the Payment Method through a popup, embedded Visualforce Page, or LWC component. The Virtual Terminal supports credit card, debit card, and ACH Payment Method types.


Web
PayLink feature.
Public web page as part of your website.
Salesforce Experience Cloud
Within a Salesforce Experience Cloud, you can display the native objects to enter Payment Method information with the default user interface (UI), or you can create a custom Experience Cloud user interface.


In-Person
Create your own custom page as part of a web app and access it via your mobile device.
Use the Virtual Terminal in Salesforce.


Initial Setup

Setup Wizard
When you click Grant Access in the Payments Setup Wizard, a Payment Method with Rec o rd T y pe = "Card" is created. If you select "Yes" for ACH payments, a Payment Method with Rec o rd T y pe = "ACH" is also created. These record types live on the Payment Method object and relate to two different Payment Method page layouts and used to collect
necessary card or bank account information.


If you need to add ACH payments, navigate back to the Blackthorn | Payments Setup Wizard tab, click on the "Record Types" step, select "Yes" for ACH payments, then click Make magic happen.


Card Payment Method


1. Navigate to the Payment Method object.

Lightning: Click on the App Launcher > Under "All Items" > Click on Payment Methods.

Classic: Click on "All Tabs" ("+" icon in the top right) > Click on Payment Methods.

2. Click New.
3. Select "Card" for the Rec o rd T y pe .
4. Required card details to enter
Ho lder's Name (required)
Number
Ex piratio n Mo nth (required)
Ex piratio n Y ear (required)
CV V
P o stal Co de (required)
Email
While this is not a required eld, we recommend you require it as we use email for Payment Gateway Customer matching logic in Salesforce.
For example, if you already have an existing Stripe/Authorize.net Payment Gateway Customer in Salesforce with a Payment Method and a new Payment Method with the same email is added, it directly relates to the existing Payment Gateway Customer record.
P ay ment Gateway
If a P ay ment Gateway is not selected, the default gateway will be used.


Related To Fields
If you add additional objects to the "Relationships" step in the Setup Wizard, meaning you want additional objects as the Transaction parent, those related objects will show up in this section as a "Lookup Field" along with the A c c o unt and Co ntac t lookup elds. We recommend entering an A c c o unt and Co ntac t for all Payment Method
records.
Street - This eld can be used for additional veri cation for the Payment Method.
The Payment Gateway Data section is data created for error logging and storing the tokenized card details on the Payment Method.
Fingerprint is not available with Authorize.net gateway.


When using External Accounts as part of Stripe Connect, the Custo mer I D will not be populated on the Payment Method.
When a Payment Method with P ay ment Metho d Status = "Valid" is created, the Card I D , Custo mer I D , and Fingerprint elds are populated.


5. Click Save.

What happens after clicking Save?

The card information is sent to Stripe/Authorize.net. The sensitive card information is removed from the Salesforce record and the gateway sends back a token for the Payment Method. This keeps us PCI compliant. No card information is ever saved in Salesforce.


How do I change the Postal Code to not required?

The default setting for the P o stal Co de eld is required. If you need to change the default setting to not required, contact Blackthorn Support, and they will change the setting.


Card Status

When saving the Payment Method record, the P ay ment Metho d Status will update to either "Valid" or "Invalid."

When P ay ment Metho d Status = "Valid", the record can be used to process immediate or scheduled Transactions.
When P ay ment Metho d Status = "Invalid", the record cannot be used.

There are two error elds on the Payment Method record's page layout, Erro r Message and Erro r T y pe , that provide information on why the Payment Method's P ay ment Metho d Status is "Invalid".


Blocking AMEX Transactions

Need a way to block American Express Card charges? Read more here.


ACH Payment Method

For Stripe


Micro-Deposit Veri cation
Before attempting to create an ACH Payment Method, it may be helpful to con rm that a Salesforce Contact record exists for the bank account holder. This will help ensure that Transaction data will be recorded for the intended person. Many organizations request a voided check to ensure the accuracy of the data to be entered.

Stripe Fingerprint
The Fingerprint is automatically added to an ACH Payment Method once it has been saved and validated. This ID is used to uniquely identify bank accounts.

Users can opt out of using the ngerprint matching logic by using one of our Custom Settings:

1. Navigate to Custom Settings in Setup.
2. Click Blackthorn Pay - Trigger Settings.
3. Click Manage.
4. Click Edit.
5. Find "Disable Fingerprint Matching (ACH)" and mark it as "TRUE".

Following the above steps will bypass the Stripe ngerprint matching logic and defer to Blackthorn's legacy ACH matching logic which uses an ACH key and Customer ID.


Add ACH Payment Methods with Non-USD Currencies
To add ACH Payment Methods with non-USD Currenc y I SO values to Stripe accounts, you need to update the ACH Rec o rd T y pe on the Payment Method object.

1. Go to Setup.
2. Click the Object Manager tab.
3. Go to the Payment Method object.


4. Click the Record Types tab in the left navigation bar.


5. Click ACH.


6. Click Edit next to Currenc y I SO .


7. In the Picklist Values’ Available Values Column, select the currency ISO code you want to use.


8. Click Add.


9. Click Save.


Create an ACH Payment Method


1. Navigate to the Payment Method object.

Lightning: Click on the App Launcher > Under "All Items" > Click on Payment Methods.

Classic: Click on "All Tabs" ("+" icon in the top right) > Click on Payment Methods.

2. Click New.
3. Set Rec o rd T y pe = "ACH".
4. Required ACH details to enter:
Ho lder's Name
A c c o unt Number
Ro uting Number
A c c o unt Ho lder T y pe
The elds on the right-hand side of the Payment Method detail section will be automatically populated from Stripe.
5. Bank account veri cation elds: Mic ro -Depo sit One and Mic ro -Depo sit T wo Your customer will receive two veri cation amounts in their bank account. They will need to provide you with those two amounts to make their Payment Method "Veri ed". Only enter the amounts (such as 35 and 42, there is no need for 0.xx or a decimal).
Email (Optional)
The Email eld is not a required eld; however, we highly recommend requiring it as we use email for Payment Gateway Customer matching logic in Salesforce.For example, if you already have an existing Payment Gateway Customer in Salesforce with a Payment Method and a new Payment Method with the same email is added, it directly
relates to the existing Payment Gateway Customer record.
Related To Fields
If you add additional objects to the "Relationships" step in the Setup Wizard, meaning you want additional objects as the Transaction parent, those related objects would show up in this section as a "Lookup Field" along with the A c c o unt and Co ntac t lookup elds.We recommend entering a contact and/or account for all Payment Method
records.
Optional Fields
Street can be used for additional veri cation for the Payment Method and is only required if you enable it in your Stripe Dashboard.
The Payment Gateway Data section is data created by Stripe. When a "Valid" Payment Method is created the Card I D , Custo mer I D , and Fingerprint elds are populated.When using External Accounts as part of Stripe Connect, Custo me r ID will not be populated on the Payment Method.
6. Click Save.


What happens when you click save?

The bank information is sent to Stripe. The sensitive bank account information is removed from the Salesforce record and Stripe sends back a token for the Payment Method. This keeps us PCI compliant. No bank account information is ever saved in Salesforce.


ACH Status
The P ay ment Metho d Status will update to "Pending" when the bank information has been entered and the record has been saved. If there is anything wrong with the A c c o unt Number or Ro uting Number you will receive an error message.

When you enter the micro-deposit numbers (this may take a few days to capture) and save the record, the P ay ment Metho d Status updates to "Veri ed". At this point, you are able to capture Transactions. Keep in mind that Transactions generally take 4-5 days to show up as a "Pending" amount in your Stripe account or External Account if Stripe Connect is
enabled.

If the micro-deposit numbers are incorrect, the P ay ment Metho d Status will update to "Veri cation Failed". Once the correct micro-deposits are entered, the P ay ment Metho d Status will update to "Veri ed".

If a Transfer sent to this bank account fails, the P ay ment Metho d Status updates to "Errored" and will not continue to send Transfers until the bank details are updated.

There are two error elds on the Payment Method record's page layout, Erro r T y pe and Erro r Message , that provide information about why the Payment Method is "Invalid".


For Authorize.net

1. Navigate to the Payment Method object.

Lightning: Click on the App Launcher > Under "All Items" > Click on Payment Methods.

Classic: Click on "All Tabs" ("+" icon in the top right) > Click on Payment Methods.

2. Click New.
3. Set Rec o rd T y pe = "ACH".
4. Required ACH details to enter:
Ho lder's Name
A c c o unt Number
Ro uting Number
A c c o unt Ho lder T y pe
5. Set the EChec k T y pe (CCD, PPD, WEB).
Visit Authorize.net to know the more about echecks.
6. Set the Bank A c c o unt T y pe (Optional).
7. Set the Bank Name (Optional).

For ACH test Payment Methods, a valid Routing Number is required.


You can set the Customer Lookup eld if you don't want to create a new customer.


8. Click Save.


What happens when you click save?

The bank information is sent to Authorize.net. The sensitive bank account information is removed from the Salesforce record and Authorize.net sends back a token for the Payment Method. This keeps us PCI compliant. No bank account information is ever saved in Salesforce.


Email (Optional)
Email is not a required eld, however, we highly recommend requiring it as we use email for Payment Gateway Customer matching logic in Salesforce.
For example, if you already have an existing Payment Gateway Customer in Salesforce with a Payment Method and a new Payment Method with the same email is added, it directly relates to the existing Payment Gateway Customer record.
Related To Fields
If you add additional objects to the "Relationships" step in the Setup Wizard, meaning you want additional objects as the Transaction parent, those related objects would show up in this section as a "Lookup Field" along with the A c c o unt and Co ntac t lookup elds.
We recommend entering a Ac c o unt and/or Co ntac t for all Payment Method records.
Optional Fields
Street can be used for additional veri cation for the Payment Method.


The Payment Gateway Data section is data created for error logging and storing the tokenized ID's in Salesforce.
When a "Valid" Payment Method is created the Card I D , Custo mer I D .

ACH Status

The P ay ment Metho d Status will update to "Valid" when the bank information has been entered and the record has been saved. If there is anything wrong with the A c c o unt Number or Ro uting Number you will receive an error message.

There are two error elds on the Payment Method record's page layout, Erro r T y pe and Erro r Message , that provide information about why the Payment Method is "Invalid".

Please note that ACH transactions with EChe c k T ype = "WEB" can't be refunded. You will see a validation error message if a WEB Transaction is attempted to Refund.

Kindly visit Authorize.net to know the more about eCheck Type Requirements


Card and ACH notes

When entering the CV V and information in the billing elds, there is an AVS (address veri cation) check and the three elds: CV V Chec k , Street Chec k , and P o stal Co de Chec k will automatically update with an "Unavailable", "Pass" or "Fail" status.

If you have more than one Payment Gateway set up, manually enter in the P ay ment Gateway lookup eld to make your selection otherwise, if left "Blank", the default Payment Gateway will be used.


Non-Gateway Payment Methods
You can create records which represent a Payment Method, but they are not actually sent to the Payment Gateway. This means that any Transaction linked to these records are symbolic, i.e. not sent to the gateway.

In order to create a Non-Gateway Payment Method:

1. Create a new Payment Method record.
2. Uncheck the Send to Gateway checkbox.
3. Populate all the required elds.
4. Click Save.


Remove the Payment Method
Once a Payment Method record in Salesforce has synced to the Payment Gateway (Stripe/Authorize.net), you are unable to delete the record. If you need to remove the Payment Method for any reason, that can be done by clicking the Remove From Gateway button or checking the Remo v e Fro m Gateway checkbox. This functionality was created so historical
information can be kept while ceasing all ways to capture transactions.

1. Navigate to the Payment Method object.
Lightning: Click on the app launcher > Under "All Items" > Click on Payment Methods.
Classic: Click on "All Tabs" ("+" icon in the top right) > Click on Payment Methods.
2. Click on the record you want to remove from Stripe.
3. Click the Remove From Gateway button or check the Remo v e Fro m Gateway checkbox.

The P ay ment Metho d Status will update to "Deleted from Payment Gateway".


Related Contact, Account, and Lead Logic
1. When de ning the Co ntac t and/or A c c o unt elds on a Payment Method for a new customer, the Payment Gateway Customer record will inherit the same Contact and Account as well.
2. If you set the Co ntac t eld on a Payment Method where the Contact is related to an Account, the Account will automatically be added to the Payment Method A c c o unt eld.
3. When the Co ntac t , A c c o unt , or Lead elds are set on the Payment Gateway Customer record, the newly created Payment Method will inherit the same Contact, Account, and Lead as well.


Remove the Payment Method Parent Object
1. Navigate to Setup.
2. In the Quick Find, type in and search for "Custom Settings".
3. Click Manage next to Payment Method Parents.
4. Click Delete next to the object you want to remove.
5. Delete the lookup elds on both the Payment Method object and your object.


Update an Existing Payment Method

Need to update an existing Payment Method?

Sometimes Payment Methods expire, but retain the same card details like card number. When this happens you can edit the expiration date. See instructions below:


1. Search for the existing Payment Method that requires the update.
2. Click Edit.
3. Type in the new 2 digit month value in the Ex piratio n Mo nth eld.
4. Type in the new 4 digit year value in the Ex piratio n Y ear eld.
5. Click Save.

The updated Ex piratio n Mo nth and Ex piratio n Y ear elds will be sent to Stripe for the edited Payment Method.


Troubleshooting
If you have received an error with your Payment Method or have a question, please view our Troubleshooting or FAQ page.


Payment Schedules

Introduction
Payment Schedules allow you to create a series of forward-looking, scheduled Transactions based on criteria you de ne through our EZ preset or advanced elds. You can:

Relate the Payment Schedule to any object (standard/custom).
Auto capture payments.
Capture a valid Payment Method through the terminal that updates all related Transactions.
Automatically request payment through PayLink.
Create an advanced Payment Schedule for unique due dates.


Parent Object Relationship
Payment Schedules are related to the parent object(s) you de ned in the Blackthorn | Payments Setup Wizard. Each parent object has a lookup eld automatically created and placed on the Payment Schedule's page layout. This allows you to relate your parent object(s) to your Payment Schedule and to add the Payment Schedules Related List to your parent
object(s).

Payment Schedules out-of-the-box have lookups (relationships) to both the Account and Contact objects. Just add the Payment Schedule Related List to your Account and/or Contact page layouts.


Create an EZ Preset Payment Schedule
The EZ Preset process is used for creating simple Payment Schedules.


1. Navigate to our Payment Schedule object.
Lightning: Click the App Launcher > In the search box enter and click Payment Schedules.
Classic: Click on "All Tabs" ("+" icon in the top right) > Click Payment Schedules.
2. Click New.
3. Populate required and optional elds.


The best feature of our Payment Schedule object is the ability to mix and match the elds you enter for generating scheduled Transactions. There are certain required elds (not marked required on the page layout) that need to be lled in when creating an "EZ Preset" Payment Schedule.


Required Fields
EZ P reset : This eld determines the frequency of each Transaction with its Due Date .
Start Date : This date determines when the Payment Schedule should start. This date can be the rst Transaction's Due Date , or the subsequent Transaction's Due Date if the rst Transaction was captured immediately.
End Date or Co unt : Either of these elds will determine the number of Transactions that need to be created.
Eac h A mo unt or T o tal A mo unt : Either of these elds will determine the amount of each Transaction.
Currenc y


Optional Fields
I nitial A mo unt : The rst Transaction's A mo unt (for example, initial fee + monthly amount) may be different than the other recurring payments.
If you use this eld, only enter Eac h Amo unt OR T o tal Amo unt , not both.
P ay ment Metho d : Add the customer's related Payment Method if you want to automatically process the generated Transactions based on its Due Date . You can also use our PayLink feature. Then you would leave the P ay ment Metho d eld blank and request payment through one of the Transaction's PayLinks. Once the customer pays through their
link, ALL related open Transactions and the Payment Schedule's P ay ment Metho d will be updated.
A c c o unt and Co ntac t : If these elds are left blank and the related Payment Method's A c c o unt and Co ntac t elds have a value, they will automatically populate the Payment Schedule and associated Transactions.
Sc hedule Status : "Draft" and "Generate" need to be set manually (or defaulted). The remaining picklist values are automatically set based on the status of the related Transactions. To generate the Transactions for your Payment Schedule, the Sc hedule Status must be set to "Generate". That triggers the system to create all Transactions based on your
Payment Schedule's EZ Preset and/or advanced elds. You can also generate the Payment Schedule by clicking Generate, located in the upper right corner of the Payment Schedule record page.
P ay ment Status : This eld is updated automatically. Do not change.
Balanc e P aid , Balanc e Due , and Nex t P ay ment Due : These elds are roll-up elds that are automatically set from the related Transactions.
Capture First T ransac tio n No w : If there is a related Payment Method and the Sc hedule Status = "Generate", the rst Transaction will be captured immediately through a real-time API call to Stripe.
A uto -P ro c ess T ransac tio ns : This eld is checked by default. Once related Transactions are created, each one will auto-process based on their Due Date .
A valid Payment Method is needed in order to auto-process the Transaction. See our Transaction documentation for more information.

4. Click Save.


Create an Advanced Payment Schedule
There are additional use cases where the Payment Schedule's frequency needs to be more complex than what is provided in the "EZ Preset" elds. For those use cases, you should use the advanced elds.


First, enter all of the required and optional elds listed above with the exception of the EZ Preset eld. That eld will be replaced by the advanced schedule elds.

For example, if your Payment Schedule needs to capture a payment once every three weeks, you would use our advanced schedule elds.

Repeats = "Weekly"
Frequenc y = "3"

The result will show that each Transaction's Due Date will be three weeks apart.

As you can see in the below images, a Payment Schedule was created using the advanced elds Repeats and Frequenc y instead of the EZ Preset eld since a payment needed to be captured every three weeks.


Keep in mind, if you did not add a valid Payment Method or requested a payment through PayLink, the related Transactions will NOT capture a payment from your customer.


Open-ended Payment Schedules
Open-Ended Payment Schedules are single amounts captured over and over again, with no ending date de ned. The Payment Schedule will continue until you close it.

The Rec urrenc e Metho d eld de nes the type of open-ended Payment Schedule you want.

Blank Field = The Payment Schedule is not open-ended and will end after the number of completed Transactions matches the Co unt .
"Keep One Open" = After one Transaction is completed, another open Transaction is generated on the same frequency.
"Auto-Renew" = After all initial Transactions are completed, the Payment Schedule will generate the full Co unt again. For example, if there were 12 original Transactions, there will be 12 new future Transactions.


Default the number of initial transactions created...


There is a custom setting that allows you to de ne the default number of Transactions to be created for "Keep One Open" and "Auto-Renew" options. The current default is 12 Transactions.

Navigate to Custom Settings > click Manage next to Blackthorn Pay - Trigger Settings > update the default "Payment Schedule Transaction Count".


Keep One Open Example
EZ P reset : "Monthly"
Rec urrenc e Metho d : "Keep One Open"
Co unt : "2"

This means that there will always be two open Transactions.


Auto-Renew Example
EZ P reset : "Monthly"
Rec urrenc e Metho d : "Auto-Renew"
Co unt : "2"

This means that after the two Transactions are completed, two more will automatically generate.

**If you didn't set the Co unt , 12 Transactions would automatically be created based on the default custom setting.


Schedule and Payment Statuses

Schedule Status

Completed
The sum of all Transactions’ Retained A mo unt equals the Payment Schedule’s T o tal A mo unt , AND there are no open Transactions remaining.


Failed
There is a Transaction with T ransac tio n Status set to “Failed” that has no available reattempts.


Active
The related Transactions have at least one Transaction with the T ransac tio n Status set to “Open,” and no Transactions with the T ransac tio n Status set to “Canceled,” OR there are Transactions with a Due Date on or before today.


Future
There are Transactions with the T ransac tio n Status set to “Open,” and none of them have the Transaction P ay ment Status set to “Captured.”


Canceled and Refunded
All Transactions with T ransac tio n Status set to “Completed” are refunded, and the remaining Transactions with T ransac tio n Status = “Open” are canceled.


Canceled
All remaining Transactions have the T ransac tio n Status set to “Canceled,” and there is a Cancel button on the Payment Schedule record.


Payment Status

Failed to Collect
The Transaction failed, and there are no available reattempts or refunds. OR the Payment Schedule was canceled and had no Transactions with the T ransac tio n Status set to “Captured” or “Refunded.”


Scheduled
There are open Transactions. And there are no Transactions with the T ransac tio n Status set to “Open” or “Canceled” or the P ay ment Status set to “Captured” or “Refunded,” or an unpaid Transaction with a Due Date before the current date.


Overdue
An open Transaction has a Due Date in the past.


Partially Paid
The sum of all Transactions’ Retained A mo unt is greater than 0 and less than the Payment Schedule's T o tal A mo unt . There are no refunded or canceled Transactions or open Transactions left to be captured.


Refunded
The sum of the related Transactions' amount paid is zero (P aid = "0"), and there are no refunds or open Transactions left to be captured.


Partially Refunded
The sum of all Transactions’ Retained A mo unt is greater than 0 and less than the Payment Schedule's T o tal A mo unt . There is a refunded Transaction, but there are no open Transactions left to be captured.


Paid
The sum of all Transactions’ Retained A mo unt is greater than or equal to the Payment Schedule's T o tal A mo unt , and there are no open Transactions left to be captured.


Good Standing
There is at least one Transaction with P ay ment Status set to “Captured.”


Canceled
There are no Transactions with the T ransac tio n Status set to “Open” or P ay ment Status set to “Captured” or “Refunded,” but there is at least one Transaction with T ransac tio n Status set to “Canceled.”


Matrix
Once you have read through the de nitions above, review the Payment Schedule Status Matrix to see how the Sc hedule Status and P ay ment Status elds interact. Your browser does not support PDF. Click here to download.


Update a Payment Schedule
There are times when you might want to update your Payment Schedule. This may occur when a Payment Gateway has changed in your org or maybe you need to swap out a Payment Method for future "Open" Transactions.

1. Navigate to your existing Payment Schedule record.
2. Update the P ay ment Gateway       eld to the updated value.
3. Notice that the related Transactions with a T ransac tio n Status = "Open" are updated to include the new P ay ment Gateway value.

NOTE: An error message will pop up on save if you have already associated the Payment Schedule with a Payment Method from a different Payment Gateway. This ensures that the associated Transactions don't fail later due to Payment Gateway mismatches.


Can I pause a Payment Schedule?


No. Out of the box, we don't offer an option to pause a Payment Schedule. To stop the Payment Schedule, you must cancel or delete the Payment Schedule and redo it when you need to restart it.


Cancel a Payment Schedule
When a Payment Schedule is canceled, the status on the Payment Schedule will be set to "Canceled" and the T ransac tio n Status of all open and related Transactions will also be updated to "Canceled". Use any of the below options to cancel an active Payment Schedule.


Click the Cancel button to cancel the Payment Schedule.
There is a hidden (off the page layout) checkbox eld (label: Canc el P ay ment Sc hedule ) on the Payment Schedule object. Check this checkbox using automation logic (Work ow, Process Builder, or Flow) to cancel the Payment Schedule.


Delete a Payment Schedule
When deleting a Payment Schedule record, all related "Open" Transactions will also be deleted. Any Transactions with a T ransac tio n Status other than "Open" will not be deleted and will continue to be related to the parent record (ie Contact, Account, Custom Object, etc...)


Changes to Payment Schedules


There are only certain changes that will sync between Payment Schedules and the associated Transactions after the initial creation of Transaction records. Those changes are described in the Roll-up/Roll-down Features section below. If you need to make changes related to the Payment Schedule dates or amounts, we recommend canceling the current
Payment Schedule and creating a new one.


Roll-up/Roll-down Features

Payment Method

From the Payment Schedule
Updating the P ay ment Metho d updates all related Transactions with the T ransac tio n Status = "Open".

For example, if a customer wants to change their Payment Method at any time during the schedule, update the P ay ment Metho d eld and the remaining "Open" Transactions will be updated.


From the Related Transaction
Updates to the P ay ment Metho d on a Transaction with the T ransac tio n Status = "Open" are rolled up to the related Payment Schedule. They are then rolled down to all other related "Open" Transactions.

For example, if a customer updates their P ay ment Metho d through PayLink on one Transaction, all other related Transactions and the Payment Schedule's P ay ment Metho d will be updated. If you don't want this to occur, set the Transaction's Do n't A uto -U pdate P ay ment Metho d eld to "True".


Account and Contact Lookup Fields
From the Payment Schedule: If the A c c o unt and/or Co ntac t lookup elds are populated when the Payment Schedule was rst created or edited, all related "Open" Transaction's A c c o unt and/or Co ntac t will be populated or updated.


Troubleshooting
If you have received an error with your Payment Schedule or have a question, please contact Blackthorn Support.


Transactions

Introduction
The Transaction object is used to authorize, capture, and refund charges, as well as serve other functions (see below). There are four record types on the Transaction object:

"Charge" (formerly called "Stripe"): Charging a Payment Method, refunding a charge, or logging a "Non-Gateway" Transaction (monies that transferred outside of Stripe but you want to keep track of in Salesforce, such as a wire transfer).

"Payouts": Auto-created by Stripe webhooks for stand-alone accounts (ordinary/common accounts). These can be manually created and processed if you're using Stripe Connect to initiate the "paying out" of funds from a Stripe account to an External Account (bank account or debit card).

"Transfer" (Stripe Connect only): Moves funds between Stripe accounts.

"Adjustment": This Transaction type is used by Stripe to send money to your account or debit your account (such as with a dispute's fee).


Transactions can relate to any object de ned in the Blackthorn Payments Setup Wizard. A lookup relationship is automatically created between the Transaction object and the parent object(s) you select.

Transactions can also process in any currency that Stripe supports. Each currency has a record in Custom Metadata for the Transaction to reference based on the value from the Currenc y I SO eld.


Process Flow
With all four record types, the most important part of Transactions is understanding the process ow. There are two elds on this object that provide the most information, T ransac tio n Status and P ay ment Status . These elds have picklist options (the majority of them are set automatically) that provide insight into what your Transactions have done.

T ransac tio n Status               P ay ment Status                                                                                                                                                              Meaning
"Open"                              "null"                           A Transaction is created in Salesforce but is not processed to any gateways yet.
"Completed"                         "Authorized"                     The Transaction is authorized.
"Completed"                         "Captured"                       The payment is successfully captured.
"Completed"                         "Uncaptured"                     An authorized Transaction is released.
"Completed"                         "Refunded"                       The charged Transaction is refunded.
"Completed"                         "Partially Refunded"             The charged Transaction is partially refunded.
"Failed"                            "null"                           The Transaction failed to capture. The Erro r Co de and Erro r Message will be captured.
"Pending"                           "null"                           The Transaction has a related ACH Payment Method in a waiting period for 3-4 days. Or if your platform's account/connected account balance is suf ciently negative, then the refund Transaction is set to "Pending" status.
"Needs Review"                      "null"                           The Transaction is invalid for some reason; the Erro r Message will display the issue and the T o Fix eld will display the possible solution.
"Canceled"                          "null"                           Mainly used in Payment Schedules, when a schedule is canceled and the underlying unprocessed/pending Transactions are also canceled.


Transaction Status
"Open" (set automatically): A Transaction that has not yet been processed or authorized.

"Process" (set automatically): This is a technical eld that you will only see after capturing or authorizing a Transaction. Once you refresh your page, it will automatically change to the next status.

"Pending" (set automatically): This status is only shown when a Transaction has a related ACH Payment Method and is within the 3-4 day waiting period, or if your platform's account/connected account balance is suf ciently negative. Then the refund Transaction is set to a status of "Pending". ACH Transactions can take up to four days before reaching a
"Completed" or "Failed" status.

"Pending Payment Intent": This status my indicate that you need to enable Strong Customer Authentication or SCA. Review the Transaction in Stripe to con rm the speci c issue.

"Completed" (set automatically): When the Transaction is fully completed. Reference the P ay ment Status as the result of the completed Transaction.

"On-Hold" (set manually): A Transaction that's set to auto-process but is currently on hold. This will remove the Transaction from the daily auto capture job. Change the status back to "Open" when it should automatically process. Manually add the picklist value to the T ransac tio n Status eld in the "Charge" Re c o rd T ype .

"Canceled" (set manually): If the Transaction was created by mistake or needs to be canceled for any reason while still in the "Open" status, it can be manually switched to "Canceled". Transactions with a status other than "Open" cannot be switched to "Canceled" unless you disable the Transaction validations in Custom Settings.

"Needs Review" (set automatically): This status is shown when an error within Salesforce impacted the Transaction from completing successfully. View the Erro r Me ssage eld or Blackthorn Logs for additional information. The Transaction may need to be set back to "Open" and recaptured if it was not sent to Stripe.

"Failed" (set automatically): The Transaction tried to complete but failed. The reason why it failed to complete may be located in the T o Fix eld or a Stripe error message populated.


Payment Status
The P ay ment Status eld is automatically populated when the T ransac tio n Status = "Completed".

"Authorized": This status means the amount of the Transaction has been guaranteed by the card issuer and the amount is held for up to 7 days unless it's released early.

"Captured": The full A mo unt was captured and the funds were taken out from the associated Payment Method.

"Partially Captured": The original A mo unt was authorized, but then a lesser amount was captured.

"Refunded": The original A mo unt was fully refunded back to the associated Payment Method.

"Partially Refunded": Part of the original A mo unt was refunded back to the associated Payment Method.

"Disputed": The Transaction was captured but is now disputed by your customer. It will remain in this status until the Dispute has been won or lost. See more about Disputes. The Transaction will automatically update to this status if webhooks are enabled.

"Uncaptured": If an authorized Transaction has not been captured in 7 days or refunded, the Transaction will automatically update to this status if webhooks are enabled.


Charge Transaction Record Type
When creating a charge Transaction record, there are several elds that automatically update:

Retained A mo unt : When a Transaction has been successfully completed, this eld's amount is the same as the Transaction A mo unt . If any refunds are made against this Transaction, the Retained A mo unt will show the remaining amount.

T ransac tio n T y pe : "Normal" is the default value, but if there is a full refund or a negative balance, this type will automatically update to "Refund".

P ay Link : If you purchased this paid add-on, this is the link you can send out to customers for capturing the payment. For additional information, click here.

T o Fix : This eld automatically displays a message about the Transaction if it was not captured correctly. See the table below for more information.

Criteria                                                                                                                                                                             To Fix (Output)
A uto -P ro c ess is checked and Due Date and Date T o P ro c ess is blank                                                                                                                    If A uto -P ro c ess is checked, a Due Date or Date T o P ro c ess is needed to automatically capture this Transaction.
I nv alid P ay ment Metho d is checked                                                                                                                                                        The related Payment Method is not valid to capture this Transaction.
A uto -P ro c ess is checked and P ay ment Metho d is blank and Rec o rd T y pe = "Charge"                                                                                                    If A uto -P ro c ess is checked, a Payment Method is needed to automatically capture this Transaction.
A uto -P ro c ess is checked and Co nnec ted A c c o unt is blank and Rec o rd T y pe = "Transfer"                                                                                            If A uto -P ro c ess is checked, a Connected Account is needed to automatically process this Transaction.
A uto -P ro c ess is checked and Co nnec ted A c c o unt is blank and P ay o ut Metho d is blank and Rec o rd T y pe = "Payout"                                                               If A uto -P ro c ess is checked, a Connected Account / Payment Method is needed to automatically process this Transaction.

P ay ment Gateway : This eld is set automatically under a few scenarios.

If the eld is blank and a Payment Method is related, the P ay ment Gateway will automatically set to the value of the Payment Method's P ay ment Gateway after the Transaction processes.

If the eld is blank and a PayLink is sent to your customer, the Payment Gateway will automatically be set to your org's default Payment Gateway after the Transaction's T ransac tio n Status is set to "Completed." Alternatively, you can set the value of the P ay ment Gateway prior to processing (if there is no related Payment Method) to 'tell' PayLink which
Payment Gateway to process through.

Co ntac t and A c c o unt : If both of these elds are null and the related Payment Method's A c c o unt and Co ntac t have a value, the Transaction's A c c o unt and Co ntac t will be updated with those values.


P ay ment Metho d Billing Email : Will be set automatically from the related Payment Method's Email when a Payment Method is added to the record and saved.

The “Send Blackthorn | Payment Receipt” ow launches the Payments Receipt Email from the ow in the Payments package. The email receipt will be sent when the Transaction is completed/captured and will contain the Transaction’s Desc riptio n in a merge eld.

Use the steps below to test the ow.

1. Process a Transaction with the following values:
A mo unt
T ransac tio n T y pe = “Normal”
T ransac tio n Status = “Completed”
P ay ment Status = “Capture”
P ay ment Metho d Billing Email = the email address where you would like to receive the test
2. The email will be sent, and the email receipt will contain the Transaction's Desc riptio n .

Original T ransac tio n (I f Ref und) : If this is a refund type Transaction, this eld will automatically populate a lookup to the original Transaction.

Original T ransac tio n (I f Reattempt) : If this is the reattempted Transaction, this eld will automatically populate a lookup to the original "Failed" Transaction.

A v ailable On : This eld provides the date that this amount is available in your Stripe account.

Balanc e Status : This eld lets you know if the amount is part of your Pending or Available balance in Stripe.


Processing Transactions
Below are instructions for processing each type of Transaction.


Webhooks

In some cases like ACH processing you may need to enable webhooks so statuses can be asynchronously updated. Use our webhook documentation to complete the setup.


Authorized Transaction


1. Navigate to the Transaction object.
Lightning: Click on the App Launcher > Under "All Items" > Click Transactions.*
Classic: Click on "All Tabs" ("+" icon in the top right) > Click Transactions.*
2. Click New.
3. Select Rec o rd T y pe = "Charge".
4. Click Next.
5. Fill in the following required elds:
A mo unt : The Transaction amount.
Currenc y I SO : The currency to process this Transaction in.
P ay ment Metho d : The Payment Method used to process this Transaction.The Payment Method must be valid to authorize a Transaction.
6. Click Save.
7. Click Authorize.
Lightning: Click the down arrow (top right corner) > Click Authorize.
Classic: Click the Authorize button at the top.

If the Transaction was successful, the T ransac tio n Status will update to "Completed" and P ay ment Status will update to "Authorized".

If the Transaction is not captured within 7 days, the P ay ment Status will update to "Uncaptured" when webhooks are enabled.The Transaction can no longer be captured and you will need to clone this Transaction or create a new one.

If you'd like to capture or partially capture the A mo unt of the authorized Transaction, click the Capture button to charge the full A mo unt or update the A mo unt to a lesser amount then click Capture (see below for more information).


Captured Transaction


1. Navigate to the Transaction object.
Lightning: Click on the App Launcher > Under "All Items" > Click Transactions.
Classic: Click on "All Tabs" ("+" icon in the top right) > Click Transactions.
2. Click New.
3. Select Rec o rd T y pe = "Charge".
4. Click Next.
5. Fill in the following required elds:
A mo unt : The Transaction amount.
Currenc y I SO : The currency to process this Transaction in.
P ay ment Metho d : The Payment Method used to process this Transaction.The Payment Method must be valid to capture a Transaction.
6. Click Save.
7. Click Capture.
Lightning: Click the down arrow (top right corner) > Click Capture.
Classic: Click Capture at the top.

If the Transaction was successful, the T ransac tio n Status will update to "Completed" and P ay ment Status will update to "Captured".


Partially Captured Transaction


Once a Transaction has successfully authorized, and you decide to capture less than the original amount, the P ay ment Status updates to "Partially Captured."

1. Navigate to the Transaction object.
Lightning: Click the App Launcher > Under "All Items" > Click Transactions.
Classic: Click on "All Tabs" ("+" icon in the top right) > Click Transactions.
2. Select an existing Transaction with P ay ment Status = "Authorized.
3. Update the A mo unt eld to a lesser amount.
4. Fill in the following required elds:
Currenc y I SO : The currency to process this Transaction in.
P ay ment Metho d : The Payment Method used to process this Transaction.The Payment Method must be valid to capture a Transaction.
5. Click Save.


6. Click Capture.
Lightning: Click the down arrow (top right corner) > Click Capture.
Classic: Click Capture at the top.

If the Transaction was successful, the T ransac tio n Status will update to "Completed" and P ay ment Status will update to "Partially Captured".


Releasing Authorized Transactions
The U nc aptured Metho d eld shows if an authorized Transaction was released (refunded) before the 7 days.


"Manual": This means the authorized Transaction was manually released from the user.
"Automatic": This means the authorized Transaction was automatically released by Stripe after 7 days.

When you need to release an authorized Transaction before 7 days.

1. Navigate to the authorized Transaction
2. Click Refund.

The authorized Transaction has been released in Stripe and the P ay ment Status updates to "Refunded." This will not create a new Transaction, it will update the existing Transaction.

Follow the process above to release a Transaction from Stripe.


In Payments version 4.54 and later...

When you release an authorized transaction by clicking the Refund button, there are no refund transaction created and the Payment Status updates to "Uncaptured".


Non-Gateway Transaction
Recording a Non-Gateway Transaction is similar to creating a charge Transaction with the exception that a Non-Gateway Transaction is not subject to the validations and processes that a charge Transaction is subject to.

However, you can refund and partially refund Non-Gateway Transactions; you can use the Refund / Partial Refund buttons and checkboxes the same way you'd use it with normal Transactions.

1. Navigate to the Transaction object.
Lightning: Click the App Launcher > Under "All Items" > Click Transactions.
Classic: Click on "All Tabs" ("+" icon in the top right) > Click Transactions.
2. Select Rec o rd T y pe = "Charge".
3. Click Next.
4. Fill in the following required elds:
A mo unt : The Transaction amount.
Currenc y I SO : The currency of this Transaction.
No n-Gateway : Checking this eld indicates the Transaction is a "Non-Gateway Transaction" and you can manually set any of the elds. IE Transaction for cash or a mailed-in check.Non-Gateway Transactions are not processed or captured like charge Transactions.
5. Click Save.


Failed Transactions
Transactions that fail to process, such as for card declines, cannot be retried. The Transaction must be cloned then reattempted. The app is built this way because Stripe maintains IDs, even for failed Transactions.


Spreedly
If a Spreedly Transaction fails, the Transaction will contain the following information describing the reason for the failure.


If the response includes an error code, it will be stored in the Transaction’s Erro r Co de eld.
The Transaction’s token will be stored in the Transaction’s Spreedly T ransac tio n T o k en eld.
The date the Transaction was processed will be stored in the P ro c essed Date eld.


Stripe
When a Transaction with an ACH Payment Method using a Stripe gateway fails, a new Transaction is created. Its Rec o rd T y pe is set to “Refund,” T ransac tio n Status is set to “Failed,” P ay ment Status eld is blank, and the Stripe Fee related to the failure is recorded.


Deleting Transactions
By default, once a Transaction has any Stripe elds populated (such as the Erro r Message or T ransac tio n I D ), you will not be able to delete it. If you do need to delete a Transaction, you can disable the Transaction validations in custom settings. This is done because Blackthorn Payments is built to be a mirror of your Stripe database.


Refund Transactions

Refunds and Authorize.net Payment Gateways
Partial and full refunds can only be processed via Authorize.net once the original Transaction is fully settled.


There are 2 paths to create a refund Transaction.

Refund / Partial Refund buttons on a Transaction record
Creates a refund Transaction for either the exact amount or an amount selected by the user.
Process Scheduled Refund Transactions Now button on Blackthorn | Payments Admin – Batch Jobs tab runs the job at the exact moment the button is pushed. It will only process Transactions that meet the speci c criteria for manual refunds.


Refunded/Partially Refunded Transaction

Transactionn Page Layout Update

The So urc e eld is not included on the Charge Transaction Layout page layout by default. To add the So urc e eld, go to Setup > Object Manager > Transaction > Page Layout > Charge Transaction Layout.


To refund a Transaction in full, click the Refund button. To partially refund a Transaction, click on the Partial Refund button, enter the amount to be partially refunded and click Refund.

Both refunds and partial refunds will create Transactions related to the original, parent Transaction. The Retained A mo unt eld captures the amount of the Transaction left after all refund(s).

Ex. If the original Transaction Amo unt = "100" and two partial refunds of 35 each (70 total) were processed, the Re taine d Amo unt eld will be "30".

NOTE: The So urc e eld of a refund Transaction is set on record creation. For example, if the refund Transaction is created from a Webhook Event, the So urc e will specify “Webhook.” Or if the refund is processed from Salesforce, the So urc e eld will specify “Salesforce UI.”


You can also fully refund or partially refund Non-Gateway Transactions (see: Non-Gateway Transactions).


1. Navigate to the Transaction object.
Lightning: Click the App Launcher > Under "All Items" > Click Transactions.
Classic: Click on "All Tabs" ("+" icon in the top right) | Click on Transactions.
2. Select an existing "Captured", "Partially Captured" or "Partially Refunded" Transaction.
3. Click Refund or Partial Refund.
4. If performing a partial refund, enter the A mo unt .
5. Click Refund.

If the Transaction was a full refund, the T ransac tio n Status will update to "Completed" and P ay ment Status will update to "Refunded". If it was a partial refund, T ransac tio n Status will update to "Completed" and P ay ment Status will update to "Partial Refund".


Scheduled Refund Transactions Now
To use the Process Scheduled Refund Transactions Now button to process a refund Transaction, complete the following steps.

1. Create a new Transaction.
2. Set Rec o rd T y pe = "Charge".
3. Click Next.
4. Enter the A mo unt as “-x.xx”.
5. Set T ransac tio n T y pe = "Refund".
6. Set Due Date = a date that is less than or equal to today.
7. Set A uto -P ro c ess = “True”.
8. Set T ransac tio n Status = "Open".
9. Set Original T ransac tio n (I f Ref und) = the original Transaction.
10. Set P ay ment Metho d = Payment Method used for the original Transaction.
11. Click Save.
12. Go to the Blackthorn | Payments Admin tab.
13. On the Batch Jobs tab, click Process Scheduled Refund Transactions Now.
14. Go back to the Transaction that was just created. Once the job is complete, the T ransac tio n Status eld will say “Completed”.


Write-Off Transactions
The new picklist value “Write Off” for the T ransac tio n T y pe eld is designed to deduct amounts from an Invoice while maintaining accurate records for nancial reconciliation purposes. Users can de ne the process for creating write-off Transactions based on their unique requirements.

Admins can implement this using tools such as Screen ows, Approval Processes, or other custom work ows to generate write-off Transactions.

Complete the following steps to create a new write-off Transaction.

1. From an Invoice record page, click New on the Transactions Related List.
2. Set the Rec o rd T y pe to "Charge".
3. Click Next.
4. Add an amount to write off in the A mo unt eld.
5. Set T ransac tio n T y pe = "Write Off".
6. Check the No n-Gateway checkbox. This is required to create a write-off Transaction. An error message will be displayed if this eld is left blank.
7. Set T ransac tio n Status = "Completed". (This triggers the recalculation of Invoice totals).
8. Complete any other elds. (optional)
9. Click Save.

The Invoice elds of W rite Of f A mo unt , Balanc e P aid , and Balanc e Due now re ect the new values.


Auto-Process/Scheduled Transactions
Blackthorn Payments has separate running scheduled batch jobs to process the daily charge Transactions, authorized Transactions, payouts, transfers and refund Transactions.

Find details for each scheduled job here.

Need to con gure reattempt logic for your scheduled Transactions? If you would like a new Transaction automatically created and queued for auto-process when the original Transaction fails, click here.


Capture Multiple Transactions In List View


Transactions can be manually processed in batch, up to 200 at a time through a Salesforce list view.

To capture multiple Transactions at one time:

1. Click the Transaction object tab.
2. Click the "Scheduled for Auto-Process (Future)" packaged list view.
3. Use the checkboxes to select which records to process.
4. Click Capture. (If the Capture button is not available in your ListView, go to the Transaction object in Setup and add the button to your available List View buttons.)
5. On the next screen, verify which Transactions to process.
6. Click Capture.


Payout Transaction
Stripe makes deposits (payouts) from your available account balance into your bank account. This account balance is comprised of different types of transactions (e.g., payments, refunds, etc.).


Stripe Payouts will now automatically relate to the Charges and Transfers included within them. This helps reconcile which Charges are included in which bank transfers that you receive.


Payout Transactions are created in Salesforce via webhook by Stripe.
They cannot be manually created in Salesforce.

Once a Transaction with Rec o rd T y pe = "Payout" has been created with a P ay ment Status = "Paid", all charge Transactions are related to the Payout Transaction through the P ay o ut eld on the Charge Transactions via the daily charges batch job.


It is important that payouts relate to original charges, refunds, disputed refunds and transfers so that you can successfully prove and document that account balances are in agreement.


In addition to relating a Payout Transaction record to all original charges, refunds, and transfers we provide an out-of-the-box report on payouts and related Transactions.

Batch job process

All Payout Transactions with a Rec o rd T y pe = "Payout", T ransac tio n Status = "Completed" and P ay ment Status = "Paid".
The Payout Transaction record then sets the P ay o ut P ro c essed Date eld with a timestamp when the record was processed so the batch job will not process it again.

This batch job can also be triggered manually. Go to the Blackthorn | Payments Admin tab, click the Batch Jobs tab, and click Process Payout Balance History.


Adjustment Transaction
This Transaction is created via webhook by Stripe. It should not be manually created.


Parent Object Roll-up Fields
There are roll-up elds that get automatically created on the parent object(s) you de ne in the Blackthorn | Payments Setup Wizard on the Relationship(s) Step. Each time you create or edit a Transaction, an apex job called, "TransactionRollupToParentService" res to update these balances.


Charge Transaction Fields
Charge Transaction roll-up elds are automatically placed on the parent object's page layout through the install wizard.


If you upgrade your org, these elds will need to be added manually to your page layout.


The roll-up elds provide insight into all open, captured, refunded, retained, and non-gateway charges related to the parent object, like an Opportunity record.

1. Navigate to a parent object record, i.e. an Opportunity record.
Lightning: Click the App Launcher > Under "All Items" > Click Opportunity.
Classic: Click "All Tabs" ("+" icon in the top right) > Click Opportunity.
2. Scroll down to "Charge Totals".

This section provides the roll-up elds for a Transaction with Re c o rd T ype = "Charge".


Checkboxes for Declarative Automation
In addition to the Authorize, Refund, and Capture buttons to process Charge Transactions, we have provided checkbox elds that mirror the button functions.

These checkboxes allow you to process Transactions automatically without the button. When Auto-Process runs, if A utho rize or Ref und are checked, the Transaction will be authorized or refunded instead of being captured. Checking each checkbox will perform the same process as if you were clicking the Capture or Authorize button.

These elds are on the Transaction object but are not on the Rec o rd T y pe = "Charge" Transaction page layout.


Transaction Fees
There are several elds that calculate certain fees for Charge Transactions.

P ay ment Gateway Fee : This is the fee from your Payment Gateway for successful Transactions.
The fee amount is based on your plan with your Payment Gateway.
Ref unded P ay ment Gateway Fee : This is the refunded Payment Gateway fee amount if your Transaction was fully or partially refunded.
As of November 2017, Stripe stopped refunding fees for new customers.
New P ay ment Gateway Fee : This is the sum of the P ay ment Gateway Fee minus the Ref unded P ay ment Gateway Fee .
A pplic atio n Fee (Stripe Connect only): The platform's application fee for direct charges from a Stripe Connect account.
Ref unded A pplic atio n Fee (Stripe Connect only): This is the refunded application fee amount if your Transaction was fully or partially refunded.
New A pplic atio n Fee (Stripe Connect only): This is the sum of the A pplic atio n Fee minus the Ref unded A pplic atio n Fee .
New A mo unt : This is the amount you receive after subtracting P ay ment Gateway Fee and A pplic atio n Fee fees.
Retained Net A mo unt : This is the amount you receive after subtracting P ay ment Gateway Fee and A pplic atio n Fee fees and any refunds.
This amount may be negative if you performed a full refund and the Payment Gateway fees were not refunded.


Currency Conversion with Stripe
When processing Transactions in a different currency than your bank account settles in Stripe, you will see the exchange rate and converted amount populate on the Transaction records in dedicated elds.

There are two elds available to add to your page layout or include in reports

Ex c hange Rate
Currenc y Co nv ersio n P ay o ut A mo unt


Exchange Rate example:

1. My Stripe Payment Gateway is in USD.
2. My Transaction is in CAD.
3. The Ex c hange Rate will populate with "0.74".
0.74 is the current value of CAD to USD.


Currency Conversion Payout Amount example:

1. My Stripe Payment Gateway is in USD.
2. My Transaction is in CAD.
3. I charge a customer CAD 100.
4. The Ex c hange Rate will populate with "0.74".
5. I will receive "$74" in the Currenc y Co nv ersio n P ay o ut A mo unt eld.


Roll-up/Roll-down Features

Payment Method
When a Contact's or Account's default Payment Method (a lookup eld on each respective object) is updated, all "Open" Transactions' Payment Methods related to that customer will update automatically.

If you don't want a certain Transaction's P ay ment Metho d to change, check the Do n't A uto -U pdate P ay ment Metho d checkbox on the Transaction record. If you don't want any Transactions to automatically update, set the Custom Setting Disable U pdate P M Related T ransac tio ns = "True".


Contact and Account
When a P ay ment Metho d is de ned on a Transaction, the related Contact and/or Account from the Payment Method will be added to the Transaction unless the Transaction already had those elds de ned.


Removing the Transaction Parent Object


1. Navigate to Setup.
2. In the Quick nd box, type in and search for "Custom Settings."
3. Click "Manage" next to Transaction Parents.
4. Click delete next to the object you want to remove.
5. Delete the lookup elds on both the Transaction object and your object.


Troubleshooting
If you have received an error with your Transactions or have a question, please view our Troubleshooting or FAQ page.


Webhook Events

Introduction
Anytime records are updated (CRUD - created/updated/deleted) in Stripe, a Webhook Event record in Salesforce gets created. Each Webhook Event record contains the full Stripe JSON payload of what occurred, which is processed in Salesforce by an scheduled batch job that processes new records every 5 minutes. This batch job will parse the Webhook Event
details and use the data to insert or update the related record in Salesforce.

For example, if a Payment Method was updated in Stripe, a Webhook Event is created in Salesforce and the batch job will update the Payment Method record in Salesforce.

There are several elds in the Blackthorn | Payments Trigger Settings' custom settings that allow you to manage Webhook Event records.

Retain W ebho o k Rec o rds f o r (Day s) : This eld controls how long to keep processed records, which limits the number of records stored in your org. The default value is 30. If the value to blank, processed records won’t be deleted.
W ebho o k Batc h Delay Minutes : If this eld is set to a speci c amount of time by the system user, new incoming Webhook Events will process only after the previously set amount of time has passed. This prevents duplication of records when Webhook Events process prior to receiving API responses back from the payment gateway.

We suggest using Webhook Events for troubleshooting and/or tracking what records are created or have been updated in Salesforce. This object only captures data from Stripe, it does not send information back to Stripe. Updating or creating Webhook Events in Salesforce will not create and/or update records in Stripe.

Note: You must con gure webhooks before Webhook Events can be created.


Stripe Webhook
How to navigate to Webhook Events in Stripe.

Navigate to your Stripe dashboard.
On the left-hand side, click on "Events and Logs".
This is where you will see all Webhook Events.
Click on any record.
The event record is split into Event Details, Event Data, and Webhooks.


All of this information is pushed to Salesforce through Stripe's Webhook. Stripe pushes Webhook Events to Salesforce in random order, such as the Payment data may get pushed before the Customer data, so we place all of these records in the Webhook Event object to process as a batch to mitigate Stripe's unpredictable lack of chronological order. Technically,
you rst need a Stripe Customer, then a Payment Method, then a Transaction, thus the purpose of the Webhook Event (to mitigate this randomness and process in the order Salesforce needs).


Salesforce Webhook Event
How to navigate to the Webhook Event object in Salesforce.


Navigate to the Webhook Events object.

Lightning: Click on the App Launcher | Under "All Items" | Click on Webhook Events.

Classic: Click on "All Tabs" ("+" icon in the top right) | Click on Webhook Events.

Click on any record.


Manually Process a Webhook Event record
If you want to manually process the record...

Click the "Process" button at the top of the page (classic user interface) or click the down arrow in the upper right-hand corner and click "Process" (lightning user interface).

For example, if you are testing and need to process the data faster than every 5 minutes, you would want to manually "Process" the Webhook Event record.


Troubleshooting/FAQ
If you have received an error with any Webhook Event record or have a question, please view our Troubleshooting or FAQ page.


Payments: Features
Below is a list of all the features we support. Take a tour! If you have questions, you can always let us know by reaching out to customer support.

Authorize.net
Blackthorn | Payments Admin
Communities & Billing Portal
Custom Metadata Types
Custom Settings
Dashboard
Default Payment Method
DocumentLink
Email Receipts
Field Service Lightning Payments
Flow Screen Charge Component
FSL Mobile Actions (without our iOS/Android app)
Historical Sync
Level 3 Processing
Matching and Duplication
Multi-Currency
PayLink
Permission Sets
Plaid
Process Scheduled Transactions and Reattempt Logic
Recurring Charges and Subscription Options
Reports
Salesforce Shield / Platform Encryption with all Blackthorn apps
SCA and MOTO
Scheduled Batch Jobs
Spreedly
Stripe
Stripe Billing
Stripe Checkout
Stripe Metadata
Stripe Radar Integration
Virtual Terminal
Webhooks


Authorize.net

If you were an Authorize.net customer before coming to Blackthorn | Payments, you may want to sync your customers and Payment Methods from Authorize.net into Salesforce. Please refer the documentation below for instructions to migrate the historic customers and Payment Methods into Salesforce.


Overview
With Authorize.net, we support over 20 processors. The list of supported processors is here.

When setting up Authorize.net, you can either use Authorize.net as a processor or use any number of their supported processors. The pricing will vary.


Scope
The Authorize.net Payment Gateway is currently supported with PayLink, DocumentLink, and the Events checkout.


Instructions
If you do not have an Authorize.net account and need one, please ll out this form. If you have a contract with one of the supported 20+ processors and want to use Authorize.net as your Payment Gateway, you'll need an Authorize.net account. Use these account credentials to connect your Payment Gateway following the setup doc below.


Customer Information Manager

If you've had an Authorize.net account for a while (pre 2018) you'll want to ensure that you've enabled the Customer Information Manager. This will ensure you don't run into unexpected errors later. From your authorize.net account goto Tools > Customer Information Manager > Click "Sign up for Customer Information Manager (CIM) Now". Check out this
article for more information and screenshots.


Setup

Authorize.net Permission Requirements
The user who connects the payment gateway to Authorize.net must have the following permissions checked on their Account Owner Pro le.


Permissions Key
Irrevocable permission
Transaction Processing Permissions
Create charge transactions
Create refund transactions
Update unsettled transactions
Manage ARB subscriptions
Manage CIM pro les
Settings Permissions
Edit transaction format settings
Update transaction security settings
Edit basic fraud settings
Edit AFDS settings
Manage mobile devices
Account Level Permissions
Update business information
Manage account services
View account nances
View/download eCheck.Net NOC reports
User Management Permissions
Manage account users


Create a Payment Gateway

Multiple Currencies

If you are a customer that needs to support multiple currencies through your Authorize.net Payment Gateway you will need to create an Authorize.net gateway for each currency. This is a limitation for Authorize.net.

We do have a validation you can enable to make sure your Transaction record currencies match your Payment Gateway currencies. Check it out here.


To begin, you will need to create a Payment Gateway record to connect to your Authorize.net account. It can be done via the Payment Setup Wizard or the Payment Gateway tab.


Using the Blackthorn | Payment Setup Wizard

1. Navigate to Blackthorn | Payments (Admin) app and click the Blackthorn | Payments Admin tab.
2. Set P ro v ider = "Authorize.net".
3. Check "Test" if you want to connect to your Authorize.net sandbox.
If you don't have a sandbox account yet, create a sandbox for testing.
4. Click Connect to Gateway.
5. Complete the Payments Setup Wizard ow.


Once the Setup Wizard is completed, you'll notice that the Gateway User Email , Gateway Public Key and Payment Gateway Account Country          elds are auto-populated. This means that the Payment Gateway is successfully connected.


Using the App Launcher

1. Navigate to the App Launcher and select Blackthorn | Payments (Admin) app.
2. Navigate to the Payment Gateways tab and click New.
3. De ne the P ay ment Gateway Name .
4. Set P ro v ider = "Authorize.net".
5. Check "Test" if you want to connect to your Authorize.net sandbox.If you don't have a sandbox account yet, create a sandbox for testing.
6. Provide a W ebho o k Label , if webhooks are implemented (Optional).
7. Provide a valid currency code in Def ault Currenc y , a blank Def ault Currenc y is considered "USD".
8. Check the Enable A utho rize.Net CV V Filter eld if you want to require users to re-enter their CVV code for the card they are using.
9. Click Save.


9. Once the record is saved, click Connect to Gateway.


The Gateway User Email , Gateway Public Key and Payment Gateway Account Country will be auto-populated once the gateway is successfully connected.


De ne the Gateway User ID
Now that you are connected to your Payment Gateway, you need to manually copy the “API Login ID” from your Authorize.net account and paste it into the Payment Gateway Gateway U ser I D eld.

1. Log into your Authorize.net account.
2. Click Account and then API Credentials and Keys.


3. Copy the “API Login ID”.


4. Enter the “API Login ID” in the Gateway U ser I D eld.


5. Click Save.


Add a Payment Method
Follow the instructions below to set up Credit Card and ACH Payment Methods with Authorize.net.


Create a Transaction
1. Create a new Transaction record (Charge).
2. Set the P ay ment Metho d lookup eld to an Authorize.net related record.
3. Enter an A mo unt .
4. Enter a Desc riptio n (Optional).
5. Set the I nv o ic e Number (Optional) - You will need to add this eld to the page layout.
6. Click Save.
7. Click Capture or Authorize.

Refer to the Charge a Transaction guide for additional information.


Refund a Transaction

Refunds and Authorize.net Payment Gateways
Partial and full refunds can only be processed via Authorize.net once the original Transaction is fully settled.


Click Refund to refund a captured Transaction or to release an authorized Transaction.


Duplicate Transactions
To prevent incorrect duplicate Transactions when using Authorize.net, a new custom setting labeled “Duplicate window” was added to Blackthorn Pay - Trigger Settings. The new custom setting includes the following functionality.

The user is UNABLE to capture the duplicate Transaction when
the Transaction is within the time mentioned in the Duplicate window custom setting
the Duplicate window = “NULL” in Custom Settings
The user is ABLE to capture the duplicate Transaction when
the time is after the time set in the Duplicate window custom setting
running the Batch Job


Authorize.net Fraud Detection Settings

If the values in a captured Transaction match or exceed the Authorize.net fraud detection settings, the Transaction’s T ransac tio n Status eld will update to “On Hold.” The “On Hold” value prevents a reattempt Transaction from being created before the Transaction can be reviewed and approved or declined.

If an “On Hold” Transaction is voided or declined, the T ransac tio n Status will be updated to “Failed” and no reattempt Transaction will be created.
If the Transaction is approved, the T ransac tio n Status will be changed to “Completed.”

Transactions that fall outside the Authorize.net fraud detection settings and do not require a review will not have their T ransac tio n Status set to “On Hold.” Instead, a reattempt Transaction will be created.


Transaction Errors

An error code and message are provided in the Erro r Message and Erro r Co de elds when a Transaction fails.

Review the response codes to nd speci c details about the Erro r Co de (Response Codes).

To generate a failed Transaction for testing, visit Authorize.net Testing Guide.


Webhooks
Webhooks provide a mechanism where a server-side application (in this case Authorize.net) can notify a client-side application (in this case Payments) when a new event (like customer create, update, delete, charge capture, charge failed, etc) has occurred on the server.

Webhooks automatically send speci ed data to a destination (endpoint) from database events.

Follow our instruction guide here for setting up webhooks in Authorize.net.


Create a Customer in the Authorize.net Portal

If you have created a Customer Pro le in Authorize.net, webhooks can update Salesforce and add the new Payment Gateway Customer record and Payment Method record.

Considerations:

Payment Pro le information will used to populate the Payment Method record.
Customer Pro le in Authorize.net does not contain many elds. In order to populate the Payment Gateway Customer record, elds from the Payment Pro le may be used.
Example: Authorize.net Payment Pro le Name = Payment Gateway Customer Name .


Visa Checkout (Optional )

Get the Visa Key from Authorize.net

1. Login in your Authorize.net account.
2. Click Account tab > Digital Payment Solutions.
3. Click Signup next to "Visa Checkout".
4. Capture the "Visa Key" from the Visa Checkout API Key section.


Create a Salesforce Site (if not yet created)

1. Register with a site domain in Salesforce. Setup > Search for Sites > Sites > Register with a unique Domain > New.
2. Fill in the required information.
3. Set any page to A c tiv e Site Ho me P age = "True".
4. Click Save.
5. Capture the U RL and P ath . Ex. https://myurl-developer-edition.na91.force.com/mypath

The client-side HTML will call start () function to init (payload) . You have to use the "Visa Key" in the HTML. The same value will be stored in the Gateway P ublic Key             eld on the Payment Gateway.


Migrate Payment Methods and Customers
If you were an Authorize.net customer before coming to Blackthorn Payments, you may want to sync your Authorize.net customers (Customer Pro le), Payment Methods (Payment Pro les), and Transactions from Authorize.net into Salesforce.

This guide will help you understand our object model so you can easily sync the information using the Data Loader tool.

1. Create a Payment Gateway in Salesforce and connect to your Authorize.net account.
2. Export customers and cards information from Authorize.net gateway into an excel document. Please convert to CSV type le.
3. We have two objects in Salesforce - Payment Gateway Customers and Payment Methods where this information will be mapped. Prepare an excel spreadsheet with this customer information mapping to respective elds on the Payment Gateway Customer/Payment Method.
4. In Salesforce, go to Custom Settings > Blackthorn | Payment Triggers > Edit > Disable all triggers.
5. Contact Blackthorn Support to disable CVV and Postal Code checks. (If you have information about the postal code, we can skip disabling this for you.)
6. Download the CSV le and import into the Payment Gateway Customer in Salesforce using the Data Loader.
7. Export the Payment Gateway Customer list from Salesforce and locate the record ID. Map the record ID in your Excel spreadsheet to P ay ment Gateway Custo mer lookup eld on the Payment Method before importing.
8. Import the Payment Methods into Salesforce.
9. Visit Custom Settings to “Enable all triggers”.


Customer Field Map

Salesforce Field Name                                                                                                                                                                   Authorize.net Label
Payment Gateway Customer                                                                                                                                                                                 Payment Pro le
Email                                                                                                                                                                                                    Email
Name                                                                                                                                                                                                     First Name + Last Name
Customer ID                                                                                                                                                                                              Customer Pro le ID
Description                                                                                                                                                                                              Description
Billing City (Optional)                                                                                                                                                                                  City
Company                                                                                                                                                                                                  Company
Postal Code(optional)                                                                                                                                                                                    ZipPostal Code
Billing Street 1 (Optional)                                                                                                                                                                              Address
Billing State (Optional)                                                                                                                                                                                 StateProvince
Billing Country                                                                                                                                                                                          Country
Phone                                                                                                                                                                                                    Phone


Payment Field Map

Salesforce Field Name                                                                                                                                                                   Authorize.net Label
Payment Method                                                                                                                                                                   Payment Pro le
Holder’s Name                                                                                                                                                                    First Name + Last Name
Email (Optional)                                                                                                                                                                 Email
Card ID                                                                                                                                                                          Payment Pro le ID
Customer ID                                                                                                                                                                      Customer Pro le ID
Record Type(Card/ACH)                                                                                                                                                            Payment Type (CreditCard/Bank Account)
Street(Optional)                                                                                                                                                                 Address
City(Optional)                                                                                                                                                                   City
State (Optional)                                                                                                                                                                 StateProvince
Country (Optional)                                                                                                                                                               Country
Last 4 Digits                                                                                                                                                                    CardNumber (last 4 digits)
Payment Gateway (lookup)                                                                                                                                                         Hardcode the PG id
Payment Gateway Customer(lookup)                                                                                                                                                 Fetch id from SF
Payment Method Status                                                                                                                                                            Valid


Alternative Migrating Method
To link the Contacts and/or Accounts to the Payment Gateway Customer or Payment Method records, complete the following steps.

Create a report in Salesforce for Contacts with the First Name , Last Name , Email , and Rec o rd I D elds.
Export them to a CSV le.
Create and export a report of all Payment Gateway Customer records with Name , Email and Rec o rd I D elds.
In Sheet B, create a new column "Contact" and add the formula to match the contacts to the Payment Gateway Customer via email.
Download to CSV then import them back into Salesforce with size 1.
Once the Co ntac t lookup is set on the Payment Gateway Customer, it will auto-update the related Account as well as update all associated Payment Methods with the set Contact and Account.


Using a Process Builder

If you want a Contact record created, you can create a Process Builder to create a Salesforce Contact when the Authorize.net Customer record is created in Salesforce.


This sync process is only to migrate your records from that moment backwards. Syncing Authorize.net with Salesforce going forward can be done through webhooks, but you should not be originating records outside of Salesforce.


Testing data
Find the testing information for Authorize.net here.


Troubleshooting
If you have received an error with Authorize.net or have a question, please view our Troubleshooting page. If you still have Authorize.net questions, please contact Blackthorn Support. We're happy to help!


Blackthorn | Payments Admin
The Blackthorn | Payments Admin tab helps you manage the Payments app's settings. Each section below matches the corresponding tab.


Batch Jobs
Most of the batch jobs are scheduled to run nightly, but you can start any of the following Payments batch jobs immediatly by clicking the relevant button.


Rollup Transaction to Parent Button
Batch Job Name: Blackthorn | Payments Transaction Rollup To Parent
Runs every 30 minutes..
Updates a Transaction’s parent records with the (child) Transaction's summary. This includes Payouts, Captures, Transfers, Refunds, and the Total elds on the parent record.


Process Scheduled Charge Transactions Now Button
Clicking this button starts two different batch processes.

The Blackthorn | Payments Daily Captures batch job processes all Authorized Charges (P ay ment Status = “Authorized”) with T ransac tio n Status = “Open”, A uto -P ro c ess = “True”, Date T o P ro c ess = “Today”, and T ransac tio n T y pe = “Normal”.
The Blackthorn | Payments Daily Captures (Authorized) batch job processes all Charges with T ransac tio n Status = “Open”, A uto -P ro c ess = “True”, Date T o P ro c ess = “Today”, and T ransac tio n T y pe = “Normal”.

See Process Charge Scheduled Transactions and Reattempt Logic for more information.


Process Scheduled Refund Transactions Now Button
Batch Job Name: Blackthorn | Payments Daily Refunds
Clicking this button starts a batch job that processes all Charges with the following: a Payment Method, T ransac tio n Status = “Open”, A uto -P ro c ess = “True”, Date T o P ro c ess = “Today”, and T ransac tio n T y pe = “Refund”.


Process Payout Balance History Button
Batch Job Name: Blackthorn | Payments Set Payout
Connects all Payout records with related Charge and Transfer (Stripe Connect) records.


Update Balances Button
Batch Job Name: Blackthorn | Payments Balance Update
Update the Stripe balances for all Payment Gateways and Connect accounts.


Assign Default Payment Methods Button
Assign the Account/Contact's default Payment Method to all related Transactions with T ransac tio n Status = "Open".


Update Transaction Net Amount Button
Updates the New A mo unt eld on a Transaction record when Rec o rd T y pe = “Stripe”.


Update Invoices Button
Batch Job Name: Blackthorn | Payments Past Due Invoices Stripe Billing
Runs daily at 5:00 am.
Updates the Invoice's P ay ment Status = "Past Due" when the Due Date < Today and P ay ment Status = "Unpaid".


Scheduled Jobs

Schedule Recommended Payment Jobs Button
Clicking this button will schedule all of our recommended Payment batch jobs, including those that were manually unscheduled. You can see a list of our scheduled jobs at Setup > Jobs > Scheduled Jobs. All of our job names start with Blackthorn | Payments.


How do I change the scheduled job/apex job user?

Before making any changes, please ensure that the person scheduling the jobs has Admin (Blackthorn | Payments (Admin)) access to Payments. The steps below will delete the current scheduled jobs and user and reschedule the jobs to run under the user who clicks the button.

1. Go to the Blackthorn | Payments Admin tab.
2. Click the Scheduled Jobs tab.
3. Click Schedule Recommended Payment Jobs.


Schedule Transaction Rollup To Parent Job Button
Scheduled Job Name: Blackthorn | Payments Transaction Rollup To Parent
Runs every 30 minutes.
Updates a Transaction’s parent records with the (child) Transaction's summary. This includes Payouts, Captures, Transfers, Refunds, and the Total elds on the parent record.


Schedule Billing Jobs Button
Clicking this button will automatically schedule all billing-related jobs if they are not already scheduled. You can see a list of our scheduled jobs at Setup > Jobs > Scheduled Jobs. All of our job names start with Blackthorn | Payments.


Scheduled Jobs

Blackthorn | Payments Send Stripe Invoices
Runs daily at 6:00 am.
Sends an Invoice to a customer when Send I nv o ic e On Date = "TODAY".
Blackthorn | Payments Past Due Invoices
Runs daily at 5:00 am.
Updates the Invoice's P ay ment Status = "Past Due" when the Due Date < Today and P ay ment Status = "Unpaid".
The Update Invoices button is located on the Blackthorn | Payments Admin’s Batch Jobs tab


Batch Jobs

Re-calculate Account Revenue
Recalculates the Historic Account Values (from Transaction) and MRR/QRR/ARR (from Subscription).
Rollup Transactions to Sales Document (Invoice)
Rolls up Transactions to their related Invoice (Sales Document).


Schedule High Volume Transaction Job Button
Clicking the Schedule High Volume Transaction Job button will trigger the “Blackthorn | Payments Daily Captures – High Volume” scheduled job and schedule Transaction auto-charge batches using the batch size of 75.

The Schedule High Volume Transaction Job button is available when the auto charge batch size exceeds 1.
The Schedule Billing Jobs button is visible when Stripe Billing is enabled through a future date.
The Schedule High Volume Transaction Job button is hidden when the batch size resets to 1.
When the Schedule High Volume Transaction Job button is clicked, the Blackthorn | Payments Daily Captures - High Volume scheduled job will replace the Blackthorn | Payments Daily Captures job and will run at midnight.


Upgrade
We sometimes add metadata changes that are not updated when you upgrade to the latest Payments package. You can deploy the latest metadata with the click of a button.


Enable All Record Types Button
Clicking this button updates all Pro les so they have visibility and all Payments' objects so they have the correct default Record Type.


Add Virtual Terminal Button
Use this button to add the Virtual Terminal button to all parent objects that were con gured in the Setup Wizard.


Deploy Roll-up Fields Button
Clicking this button deploys summary elds onto your Transaction parent objects. For example, if you de ned the Opportunity object as your Transaction parent, the following group of summary elds will be created on the Opportunity object.

Captured Charge Co unt (Captured_Charge_Count__c)
Captured Charges (Captured_Charges__c)
Captured T ransf er Co unt (Captured_Transfer_Count__c)
Captured T ransf ers (Captured_Transfers__c)
Co mpleted P ay o ut Co unt (Completed_Payout_Count__c)
Co mpleted P ay o uts (Completed_Payouts__c)
Open Charge Co unt (Open_Charge_Count__c)
Open Charges (Open_Charges__c)
Open P ay o ut Co unt (Open_Payout_Count__c)
Open P ay o uts (Open_Payouts__c)
Open T ransf er Co unt (Open_Transfer_Count__c)
Open T ransf ers (Open_Transfers__c)
R ef unded Charge Co unt (Refunded_Charge_Count__c)
Ref unded Charges (Refunded_Charges__c)
Retained Charge Co unt (Retained_Charge_Count__c)
Retained Charges (Retained_Charges__c)
Retained T ransf er Co unt (Retained_Transfer_Count__c)
Retained T ransf ers (Retained_Tranfers__c)
Rev ersed T ransf er Co unt (Reversed_Transfer_Count__c)
Rev ersed T ransf ers (Reversed Transfers__c)


Enable Order to Invoice Button
This button will deploy an Order lookup on the Invoice object so you can easily create Invoices from Order records.


Add Payment Fields to Page Layouts Button
Use this button to make sure the recommended Payments elds are visible on all our page layouts. (Salesforce doesn't add new elds to page layouts when upgrading a package.)


Add Picklist Values Button
Click this button to ensure the recommended picklist values are visible for the following elds.
P ro v ider on Payment Gateway
P ay ment Status on Transaction
T ransac tio n Status on Transaction
So urc e on Transaction
Status on Invoice
P ay ment Status on Invoice
Status on Checkout Submission
P ay ment Metho d Status on Payment Method
P ro ratio n Behav io r on Subscription
Status on Subscription


Stripe Billing
The following jobs are only scheduled for customers who previously had Stripe Billing enabled for their org. (We do not support Stripe Billing for new customers.) To schedule each job individually, click the following buttons on the Blackthorn | Payments Admin Stripe Billing tab.


Deploy Stripe Billing Button
Use this button to deploy the necessary elds to use Stripe Billing in a Salesforce org.


Re-Calculate Account Revenue Button
Clicking this button will recalculate the Historic Account Values (from Transactions) and MRR/QRR/ARR (from Subscriptions).


Rollup Transaction to Invoice Button
Use this button to roll up Transactions to their related Invoice.

View our Stripe Billing documentation here.


If you have any questions regarding the con gurations/settings, please contact Blackthorn Support, and we'll help you out!


Communities & Billing Portal

Have you considered using the new BT Payments LWC Virtual Terminal?

Use the LWC Virtual Terminal on a publicly accessible Lightning Experience Cloud page. Guest users can access publicly available pages without any licensing or authentication. They can also create up to 100 sites for free without buying community licenses.


Blackthorn Payments works within Communities and is often used as a Billing Portal.


To set up the Payments app to work in Communities or to have the BT Payments Virtual Terminal show in Communities, complete the following steps:

1. Set up a Payment Gateway, if you haven't already done so.
2. You many also need to create the following records: Payment Gateway Customer, Account/Contact/Opportunity, and Payment Method.
3. Expose Invoices or a different object to represent what the customer is paying for. The Invoice Rec o rd T y pe can be set to Order or Invoice. You can also have an object(s) for Invoice, Order, Case, or other. If other, set the Transaction Parent as this object in the Setup Wizard (Payments Admin App has the tab).
4. Add the BT Payments Virtual Terminal Visualforce component to the layout. The BT Payments Virtual Terminal Visualforce component works in Classic and Lightning. It uses the Lightning Design System and functions as a Lightning Component does. See our BT Payments Virtual Terminal documentation for instructions to add it to your layout.
5. Enable the correct Audience to view the BT Payments Virtual Terminal. In the top right after adding the Visualforce page, assign the Audience and see the screen shot below for where to click.


6. Add the Blackthorn | Payments (Community/Platform User) permission set to the Communities User. (Setup > Users > Any Communities User > Assign the Permission Set). For large Communities, auto-assign the Permission Set to new users. Blackthorn also offers a Site-wide License so individual user licenses do not need to be assigned, and can advise
on company-wide pro le-based permissions to assign for all Community Users.
7. Set applicable elds to read-only and pre-populate elds such as A mo unt , Currenc y , Desc riptio n , Related T o , or any custom elds to the desired value. See the Virtual Terminal documentation for instructions.


Custom Metadata Types

Introduction
Custom Metadata Types are used in Blackthorn apps to automatically install metadata records into your org. Many packaged apex triggers use these records. The purpose of this documentation is a reference for these records' functions.

For example, we have a Custom Metadata Type called "Stripe Currency Setting" that stores all the Stripe currency information like the ISO code, minimum amount, supported bank accounts, etc. and is used to validate your Payment Methods and Transactions.


Custom Metadata Types
There are two Custom Metadata Type records: Stripe Connect Country Specs and Stripe Currency Setting.

1. Navigate to Custom Metadata Types.

Lightning: Setup > In the Quick Find, search and click "Custom Metadata Types."

2. Click "Manage Records" next to either Custom Metadata Type.

You can update the records by clicking Edit next to the record name.


Stripe Currency Setting


Stripe Connect Country Specs


Troubleshooting
If you have received an error with your Custom Metadata Types or have a question, please view our Troubleshooting or FAQ page.


Custom Settings

Introduction
Custom Settings are used in Blackthorn apps for multiple use cases, such as turning Apex-based features on and off, custom handling around scheduled processes, tracking the status of your onboarding in the setup wizard, and many more.


Blackthorn Pay - Reattempt Settings
Out-of-the-box, Blackthorn Payments automatically creates and enables a Reattempt Schedule for your failed Transactions.


1. Navigate to Custom Settings.

Lightning/Classic: Setup > In Quick Find, Search and Click: "Custom Settings."

2. Click Manage on Blackthorn Pay - Reattempt Settings.


3. Check Allow on Non-Auto Process if you want to reattempt failed Transactions that don't have auto-process checked.
If you don't want to reattempt Transactions unless they have the auto-process eld checked, then skip this step.
4. Enter a number (of days) for each Attempt     eld.
If you enter "1" in each eld, each attempt will occur that number of days after the previous attempt. By default, we have entered a "1" from the rst to fourth reattempt (reattempting each day for four days).


Disable Reattempt Logic

To disable the Reattempt Logic, uncheck the Enabled eld.


5. Click Save.


Blackthorn Pay - Trigger Settings
There are many Apex-based validation rules, enabled by default. The following custom settings are just a few that can disable them.

Retain W ebho o k Rec o rds f o r (Day s) : This eld controls how long to keep processed records, which limits the number of records stored in your org. The default value is 30. If the value to blank, processed records won’t be deleted.
W ebho o k Batc h Delay Minutes : If this eld is set to a speci c amount of time by the system user, new incoming Webhook Events will process only after the previously set amount of time has passed. This prevents duplication of records when Webhook Events process prior to receiving API responses back from the payment gateway.
Disable T rans Ro llup T o A c c o unt : This eld prevents failures by stopping the triggers that sum the total Transactions related to an Account and populate the Histo ric al A c c o unt V alue eld. The failure occurred during check and money order scans for Check 21 and Mobile Payments users when more than 50,000 Transactions were related to a
single Account.


To Enable
1. Navigate to Custom Settings.

Lightning/Classic: Setup | In Quick Find, Search and Click: "Custom Settings."

2. Click Manage next to Blackthorn Pay - Trigger Settings.


Example: Disable Transaction Account/Contact Lookup Setting
When you don't wish to de ne a Contact/Account on a Transaction, you can disable the related lookups from the Payment Method being populated on the Transaction using a Custom Setting.

To disable this, navigate to setup >Custom Settings >Blackthorn Pay - Trigger Settings > “Disable Transaction Related Lookups“. set to TRUE. This will turn off transaction account/contact based lookup settings.


Note About Disable Trans Rollup To Parent

This Custom Setting is set to TRUE in new orgs by default. Users will still see TransactionRollupToParentService in the Apex Jobs list, but the logic will not re. To ensure that Transaction rollups are being executed in your org be sure to uncheck this setting.


Blackthorn Pay - Transaction Parents
This Custom Setting correlates to the custom lookup eld (Transaction parent) created on the Transaction object.


Add a New Transaction Parent
Adding additional Transaction parents happen in the Setup Wizard under the "Relationships" step.

We do not advise manipulating these records manually.

The most common Transaction parent is Opportunity, but it can be any object or multiple objects. When the object is selected, it creates a Custom Setting record here.
You can go back to the Setup Wizard at any time to add additional objects (Transaction parents).


Blackthorn Pay - Transaction Validations
This Custom Setting includes items that allow user to ne tune Transaction validation rules.

TR Validate Status Transition - Blocks invalid manual updates of Transaction Status or Payment Status.
TR Prevent Delete of Record with IDs - Blocks the deletion of Transactions if a Transaction ID is present.
TR Currency Validation - Blocks Transactions from being saved if the Currency on Transaction and Currency on the associated Authorize.net Payment Gateway do not match.


Blackthorn Pay – Features

Authorize.net: Track and Reconcile Payments
Customers can now track and reconcile payments processed through Authorize.net via the new “Blackthorn Pay – Features” custom setting. The custom setting will be created during package upgrades and new installations and can only be accessed via the LMO.

The Solution Id     eld will be populated with Blackthorn’s partner ID when Payments is installed/upgraded in production. A test value will be used in an Authorize.net sandbox. If a sandbox is created from production, the production value will be updated to the test value.


Once the Solution Id is populated, it will be included any time Blackthorn sends data to Authorize.net. If the Solution Id is not available, the data will be sent without the Transaction source information.


High-Volume Batch Processing
The introduction of high-volume batch processing resolves the issue of scalability with our batch processes. Previously, batch processes were limited to one record at a time to ensure that Payments was compliant with Salesforce's limits.

The new protected custom setting is located under the Blackthorn Pay – Features custom setting.


Field Label: A uto -Change Batc h Size
API Name: Auto_Charge_Batch_Size__c
Data Type: Number(3,0)
Description: Controls the batch size of the scheduled job. The default setting is 1. Currently, the maximum supported value is 75.


Next Steps
Learn more about our Auto-Process and Reattempt Logic.
Create a Payment Schedule.


Troubleshooting
If you have received an error with your Custom Settings or have a question, please view our Troubleshooting or FAQ page. If you still have Custom Setting questions, please contact Blackthorn Support. We're happy to help!


Dashboard

Introduction
We have created a basic Dashboard that will provide a starting template that you can modify to reach your desired metrics.

Navigate to Dashboards.

Lightning: Click on the app launcher | Under "All Items" | Click on Dashboards.

Classic: Click on "All Tabs" ("+" icon in the top right) | Click on Dashboards.

In the left-hand column, click on the "Blackthorn | Payments Dashboard" folder.


Out of the Box Dashboard
The below Dashboard components are provided by Blackthorn | Payments.

Revenue Forecast: The future estimated revenue per month.
Gross Revenue: The sum of revenue each month.
Captured this Month: The sum of retained revenue this month by speci c segment ranges.


Next Steps
Use our "out of the box" Reports to create a list of your records.


Troubleshooting
If you have received an error with our Dashboard or have a question, please view our Troubleshooting or FAQ page. If you still have questions about our Dashboard, please contact Blackthorn Support. We're happy to help!


Default Payment Method

Feature Overview
Have the ability to de ne your Default Payment Method for any given Contact and/or Account Record.
Automatically set the latest default payment method on all related "Open" Transactions.
For example: If a customer has updated their payment method, all un-processed transactions will automatically update with the newest Payment Method.
Update default Payment Methods in Stripe and they will sync back to Salesforce with the setup of Webhooks.


Scope
Default payment method is supported for both Card and ACH payment methods types.
Ability to automatically default the Payment Method lookup eld on a Transaction record is coming soon.


Prerequisite
1. Install our latest Blackthorn | Payments App.
2. Update your Contact, Transaction, and Payment Method Layouts to include below-highlighted elds and related lists.

Object: Contact*

Fields                                                                                                                           Related Lists
Default Payment Method                                                                                                                                                      Payment Method
Default Payment Gateway                                                                                                                                                     Payment Gateway Customers
Transactions

*Including the related lists for Contact/Account will provide insights into your Contact/Account’s related Stripe Customers, Transactions, and Payment Methods records.


Object: Account*

Fields                                                                                                                           Related Lists
Default Payment Method                                                                                                                                                   Payment Method
Payment Gateway Customers
Transactions

*Including the related lists for Contact/Account will provide insights into your Contact/Account’s related Stripe Customers, Transactions, and Payment Methods records.


Object: Payment Method

Fields                                                                                                               Related Lists
Default Payment Method                                                                                                                                                                                  none


Object: Transaction

Fields                                                                                                                 Related Lists
Don’t Auto-Update Payment Method                                                                                                                                                                               none


When adding the Payment Method related list on your Contact and/or Account record, edit the related list settings to include the Default Payment Method Checkbox eld.


Setup

Create a Default Payment Method
1. Navigate to an existing Contact or Account record.
2. Create New Payment Method.
3. Select Card/ACH and enter the Payment Method details.
4. Click Save.


If this is the rst Payment Method for your Contact and/or Account, the Default Payment Method checkbox will be selected automatically.


If your Contact/Account has multiple Payment Method records, you will need to manually check the Default Payment Method eld to de ne your default Payment Method.


Auto-Update "Open" Transaction's Payment Method
Our default Payment Method logic automatically updates related "Open" Transactions to the latest default Payment Method.

1. Navigate to an existing Contact or Account record.
2. Click on the newest Payment Method.
3. Check Default Payment Method .

4. Navigate to all "Related To" Transactions.

You will see all "Open" Transactions have updated to the newest default Payment Method.

You are all set!


Don't wish to update all related Transactions to the latest default Payment Method?

Example scenario -If you have a customer paying for only one transaction where the Payment Method should not update to the default Payment Method.

You can do one of the below two things -

1. When creating a new Transaction or updating an existing Transaction, check the Don't Auto-Update Payment Method .

OR

2. Navigate to Custom Settings, select Manage next to Blackthorn | Payments triggers and select Disable Update PM Related Transactions checkbox.


This will disable updating the Payment Method on related transaction/s.


Update Existing Payment Method Records to set the Default Payment Method
If you have been using Blackthorn | Payments now is the time to update your records in Salesforce for this feature!

You can update records via Salesforce Data Loader.

1. Verify your Payment Method Records are related to an existing Contact and/or Account.
2. When you set the related Contact and/or Account, the Payment Gateway Customer record will also update with that related Contact and/or Account automatically.
3. Run a report of all Payment Gateway Customer records that have a related Payment Method record. From that list determine which Payment Method's should be marked as the "Default Payment Method".
4. Set those Payment Method records Default Payment Method checkbox eld=True.


If you don't want the related Transaction's Payment Method to update, disable this feature in Custom Settings while doing the initial update of historical records.


Next Steps
Understand how Transactions are processed.
Use Payment Schedules to create future looking Transactions in minutes.
Learn about our supported Payment Methods.


Troubleshooting
If you have received an error with your Default Payment Method Feature or have a question, please view our Troubleshooting or FAQ page. If you still have Default Payment Method questions, please contact Blackthorn Support. We're happy to help!


DocumentLink Overview
Send web-based Invoices through DocumentLink

DocumentLink renders beautiful, mobile responsive payable Invoices on the web that can be shared easily via a link. Invoices can be paid using Blackthorn Payments in a PCI-compliant fashion. No custom code is needed for setup or con guration.


DocumentLink Template
This DocumentLink Template object contains the elds that allow users to con gure the presentation of the DocumentLink.


De ne Custom Acceptance Language
Use the following elds to customize the acceptance language on your DocumentLink Template.

T erms and Co nditio ns : Use this eld to link your custom terms and conditions to the DocumentLink Template.

A c c eptanc e Language - A CH and A c c eptanc e Language - Card : Use these elds to craft custom messaging.


If these elds aren’t already included in the DocumentLink Template page layout, complete the following steps to add them.

1. Click the Gear icon.
2. Click Setup.
3. Click the Object Manager tab.
4. In the Quick Find box, enter and click “DocumentLink Template.”
5. Click the Page Layouts tab.
6. Click “Document Link Layout.”
7. Drag and drop each eld onto the page layout.
8. Click Save once all three elds have been added.


Examples

Credit Card DocumentLink Checkout


Bank DocumentLink Checkout


Is the date format on your DocumentLink Template incorrect?

Check your browser's location setting. All date elds on the DocumentLink Template are formatted based on your browser's location setting.


Add Company Logo and Details to DocumentLink
To add company details and a logo to your DocumentLink Invoice, complete the following steps.

1. From the App Launcher, navigate to the Company Info object.
2. Click New to create a new record.
3. Complete the following elds.
Co mpany I nf o Name (required)
Email (required)


Lo go - enter a URL to your logo.
NOTE: Use the Documents object in the Classic UI to store images. From there, right-click the image, select "Copy Image Address", and add it to the Lo go eld.
4. Add additional details such as a website and address.
5. Click Save.
6. Add the Company Info record to either the DocumentLink Template record or directly on the Invoice record.

Click Company Info for more information about the Company Info object.


Add Custom Fields and Footer
Use the following elds to customize the Invoice created by DocumentLink:

Do c umentLink Field 1 (Label)
Do c umentLink Field 1
Do c umentLink Field 2 (Label)
Do c umentLink Field 2
Fo o ter


What other changes can I make?

Additional customizations such as changes to the font, font size, and wording are not able to be made at this time.


Multilingual Support - In Progress
The DocumentLink Template object includes a new eld called Display Language . The eld contains a list of languages an Admin can choose from to display to the DocumentLink end user.

Field Name: Display Language
API Name: Display_Language__c
Data Type: picklist
Description: List of supported display languages for the DocumentLink. This eld is set to English by default.


Automatically Apply DocumentLink Template to Invoices
1. Create a simple process (Process Builder, Flow etc) to accomplish this.
2. In your automated process, you would set the Do c umentLink T emplate eld on the Invoice Record.
3. Set it to ll in the Do c umentLink T emplate any time an Invoice is created.


Deprecated Fields
If you are upgrading your Blackthorn Payments package and notice that some elds on the DocumentLink Template object have the ability to be deleted feel free to take advantage of this to clean your org.

Otherwise, if a eld has the ability to be deleted and can no longer be added to your page layout that means we no longer support it. You'll need to navigate to Setup in the classic UI to see the option to delete.

Fields No Longer Supported:

Bac k gro und Co lo r
Butto n Co lo r
Card Co lo r T heme
Lo go
Due Date Label
Requested by label
A mo unt due label
Do c umentatio n


Authorize DocumentLink
In order to view your Order or Invoice via DocumentLink, you must oauth with Blackthorn's Connect App.


Oauth Link

In order for the authorization to work properly, you can only be logged into one Salesforce org.


Production Org
Please click the oauth link to complete the DocumentLink setup. Once you authorize with the key above, you will be set.

Sandbox Org

1. Click the oauth link to complete the DocumentLink setup.
2. Click Allow to allow access.


3. If the authorization is successful, you will see a success message.


If you receive an error with DocumentLink, click to view Error Codes And Messages.


Update DocumentLink Fields
Complete the following steps to change the values in the A c c o unt Name (Bill T o ) , First Name (Bill T o ) , and Last Name (Bill T o ) elds, but keep the existing A c c o unt (Bill T o ) and Co ntac t (Bill T o ) eld values.

1. Open an Invoice record.
2. Click the Pencil icon next to the A c c o unt Name (Bill T o ) eld.
3. Enter a new name.
4. In the First Name (Bill T o ) eld, enter a new rst name.
5. In the Last Name (Bill T o ) eld, enter a new last name.
6. Click Save.
7. Click the Do c umentLink URL to view the changes.


DocumentLink Multilingual Support Overview
The Data Dictionary provides multilingual support, allowing Admins to establish a default language that serves as the primary language for all users. For example, you can override button labels and other static text on your web-based invoices.

Admins can also override the default language and customize users' language experiences when speci c prede ned criteria are met. For example, an Admin can change the language for users in a particular region.

Content will be presented in a user’s preferred language or default to English if a language isn’t pre-selected. Users won’t have to manually select their language each time they interact with the system, and they can change the displayed language according to their preferences.


New Fields

Data Dictionary Group
The Data Dic tio nary Gro up eld creates a link between the Data Dictionary Group and the DocumentLink Template object.
• Field Name: Data Dic tio nary Gro up
• API Name: bt_stripe__Data_Dictionary_Group__c
• Data Type: Lookup(Data Dictionary Group)
• Description: Select the appropriate Data Dictionary Group containing the translated override values (Data Dictionary Entries) for the chosen language.


Display Language
The Display Language contains a list of languages an Admin can choose from to display to the DocumentLink end user.
• Field Name: Display Language
• API Name: Display_Language__c
• Data Type: picklist
• Description: List of supported display languages for the DocumentLink. This eld is set to English by default.


Select a Method - DocumentLink

How It Works
The following logic describes how the Data Dictionary Group/Data Dictionary Entry records interact with the Display Language eld.

DocumentLink labels are displayed in English, the default language, when either of the following is true.
The DocumentLink Template’s Display Language and Data Dic tio nary Gro up elds are blank.
The Display Language eld is blank, and the Data Dic tio nary Gro up does not have a Data Dictionary Entry for the English language.
DocumentLink labels are displayed in the values given for the selected language in the Data Dic tio nary Gro up if the Data Dictionary Group has a Data Dictionary Entry record for the DocumentLink Template’s Display Language .
DocumentLink labels are displayed in the DocumentLink Template’s Display Language if the related Data Dictionary Group does not include a Data Dictionary Entry record for the selected Display Language .
DocumentLink labels are displayed in the values given for the English language in the Data Dictionary Group if the Data Dictionary Group includes a Data Dictionary Entry record for the English language, and the DocumentLink Template’s Display Language eld is blank.
When the Data Dic tio nary Gro up eld is blank, DocumentLink labels are displayed in the selected DocumentLink Template’s Display Language .


Data Dictionary

Required Licenses and Permission Sets
To use the Data Dictionary feature, you must have a Blackthorn Payments license, as well as access to the following elds:

Create/Read/Update - Data Dictionary Group
Create/Read/Update - Data Dictionary Entry


Supported Languages
We do not currently support all languages. The following is a list of the languages we support.

Arabic
Chinese (Simpli ed)
Chinese (Traditional)
Czech
Danish
Dutch
Finnish
French
German
Haitian Creole
Hindi
Hmong
Hungarian
Indonesian
Italian
Japanese
Korean
Norwegian
Polish
Portuguese
Romanian
Russian
Somali
Spanish
Swedish
Thai
Turkish
Vietnamese


One-to-One Relationships
A Data Dictionary Entry record contains three important elds: V alue , Key , and Language / Lo c ale . In each Data Dictionary Entry record, the elds interact as follows:


There can be only one value in the Language / Lo c ale eld.
Each Key is associated only with one V alue .

Creating a second line in the Data Dictionary Entry using the same Key as the rst line but with a different V alue will replace the rst V alue with the new one.

Example:

Line 1: Key = "LBL_CHECKOUT" and V alue = "Checkout"
Line 2: Key = "LBL_CHECKOUT" and V alue = “Proceed”
Result: The Attendee will see “Proceed.”


Create a Data Dictionary Group
If you want to override out-of-the-box values, the rst step is to create a Data Dictionary Group and populate it with Data Dictionary Entries.

1. In the App Launcher, enter and click “Data Dictionary Group”.
2. Click New.


3. Enter a Data Dic tio nary Gro up Name .
4. Click Save.


5. Click New next to Data Dictionary Entry.


6. The Data Dic tio nary V alues eld contains the Language / Lo c ale , Key , and V alue . Click the DocumentLink Data Dictionary (a Google document) for Key and V alue information.
7. Here are a few frequently used Data Dictionary values and their keys:
Key = "LBL_CHECKOUT" and V alue = "Checkout"
Key = "LBL_INVOICE" and V alue = "Invoice"
Key = "LBL_BALANCE_PAID" and V alue = "Balance Paid"
Key = "MSG_PROCESSING_TRANSACTION" and V alue = "Processing transaction…"
Key = "MSG_AUTHORIZE_CREDIT_CARD_WITH_NAME" and V alue = "I authorize [XYZ] to charge my credit card."
8. Select the Language / Lo c ale you'd like to change.
9. Enter a Key and V alue .


10. Click Back to return to the Data Dictionary Group record.


If you need to add additional keys to the Data Dictionary Entry, click the menu (upside down triangle) next to the Data Dictionary Entry. From there, click Add Row to add a new Key and V alue . When you are done, click Save and Back to return to the Data Dictionary Group.


USE CAPITAL LETTERS


In the Key   eld, use capital letters.


Example
In this example, we will set Language / Lo c ale = "German". Now, we can select any word or phrase to replace an action with. Set Key = “LBL_DUE_DATE“ and V alue = “Faelligkeitsdatum”. Make sure to use all capital letters for the Key .


Add a Data Dictionary Group to a DocumentLink Template
1. Open an existing DocumentLink Template or create a new one.
2. Click the Pencil icon next to the Data Dic tio nary Gro up eld.


3. Select a Data Dictionary Group.
4. Click Save.


Default Languages

Change the Default Language
The following functionality has been added.

DocumentLink checkout will be displayed in the language selected on the DocumentLink Template record.
Labels will default to English if the Display Language eld on the DocumentLink Template record is left blank.
The language on labels and buttons can be overwritten with a Data Dictionary Group record containing the matching Key and V alue .
The date will be formatted based on the language selected on the DocumentLink Template. If no language is selected, the date format will be based on the browser’s location.


Translate a DocumentLink Template
1. Go to an Invoice record.
2. Click an existing Do c umentLink T emplate or create a new one.


3. Select a Display Language .


4. Click Save.


Invoice Payment
When a customer receives an Invoice, they can immediately make a payment through DocumentLink.


Process Flow
1. The customer receives an email with the DocumentLink. This generated DocumentLink comes from an Invoice.
When they click on the link, they are brought to a mobile responsive page like the example below.


2. The customer clicks Pay.
3. Depending on the enabled Payment Methods, the customer can either pay with a card or ACH.
If this is a new Stripe customer, a Payment Method and Payment Gateway Customer record will be created automatically and related to the P repared Fo r eld.
If this is an existing Payment Gateway Customer (matches on email) a new Payment Method will be added to their record.
4. If they select Card, they will enter in their credit card information and click Pay.
If they select ACH, they will enter in their bank information and click Pay.
If the Payment Method is successful, they will receive a noti cation that tells the customer:
"Two small deposits will be made in your bank account. These deposits should appear in your bank account within the next few days. When they arrive, con rm your bank account by contacting us."

There will be an ACH Payment Method with the P ay ment Metho d Status = "Pending" and a related Transaction with T ransac tio n Status = "Open" in Salesforce.

When the customer contacts you, enter the two micro-deposits on the pending ACH Payment Method record. The Payment Method's P ay ment Metho d Status will automatically update to "Veri ed".

Then navigate to the related open Transaction and click the Capture button.

Once the Transaction has been captured and if the Invoice Balanc e Due is "0", the related Invoice P ay ment Status eld = "Paid", the Status eld = "Completed" and the P aid I n Full eld is set to the current date/time.

Voila! Your Invoice has been paid.


Transaction Email Receipts
Blackthorn | Payments allows you to send receipts from Salesforce using the “Send Blackthorn | Payment Receipt” ow or from Stripe.

If you choose to send from Salesforce, you will have full control over the Email Template (HTML or text) and who the email goes to (Email Alert). Emails from Stripe offer two options: successful payments and/or refunds.

NOTE: Please do not send receipts from both Blackthorn | Payments and Stripe. Your customers do not want to receive two emails with the same information about a Transaction.


Customize the Email Template
The information below provides instructions on customizing the Email Template for the automated Transaction email receipt.

The Email Template de nes what message will be sent to your customer and whether it is formatted (HTML) or not (Text).

For this example, we are working with the Receipt (HTML) template in the Classic Email Templates.

1. Go to Setup.
2. In the Quick Find box, enter “Email Templates.”
3. Select “Classic Email Templates.”
4. In the Folder drop-down, select “Blackthorn | Payments.”


5. Click "Receipt (HTML)" to select the template.


6. Click the Edit HTML Version button.


7. Update the email message.
For the Email Template, merge elds can only come from the Transaction object. If you need to use merge elds from a related object, you must create formula elds on the Transaction object rst. Review the section below for the steps to add custom elds.


8. Click Save.


Send from Blackthorn Payments
The Transaction ow used to send the Payments Receipt Email is the “Send Blackthorn | Payment Receipt” ow.
Users can launch the Transaction email receipt from the ow in the Payments package. The email receipt will be sent when the Transaction is completed/captured and will contain the Transaction’s Desc riptio n in a merge eld.

To test the ow, complete the steps below.

1. Process a Transaction with the following values:
A mo unt
T ransac tio n T y pe = “Normal”
T ransac tio n Status = “Completed”
P ay ment Status = “Capture”
P ay ment Metho d Billing Email = the email address where you would like to receive the test
2. The email will be sent, and the email receipt will contain the Transaction's Desc riptio n .

Note: The previous Transaction work ow rules, “Send Blackthorn | Payment Receipt (HTML) and “Send Blackthorn | Payment Receipt (Text),” used to send the Transaction email receipt were deprecated. The new “Send Blackthorn | Payment Receipt” ow replaces both.


Send from Stripe
1. Sign in to your Stripe account.
2. Go to Settings.
3. Select Emails.


4. Select "Successful Payments" and/or "Refunds."


Add Custom Merge Fields to the Email Template
To add custom merge elds from an Opportunity record to the Transaction's Email Template, you must create those elds in the Transaction object as formula-type elds and pull in the values from the related object before they can be added to the Email Template.

For the use case below, we will create a custom eld on the Transaction with a formula referencing the Oppo rtunity Name eld.


Step One: Create a custom formula eld on the Transaction object.
1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, enter and click “Transaction.”
4. Click the Fields & Relationships tab.
5. Click New.
6. Select "Formula."


7. Click Next.
8. Enter a Field Label .
9. Set the Fo rmula Return T y pe to “Text.”


10. Click Next.
11. Click the Advanced Formula tab.
12. Click the Insert Field button.


13. The rst column should be set to “Transaction >.”
14. In the second column, select “Opportunity >.”
15. In the third column, select “Opportunity Name.”
16. Click Insert in the fourth column.


17. Click Next.


18. Con rm the eld-level security.
19. Click Next.
20. Con rm which page layouts the eld will be added to.
21. Click Save.


NOTE: Some eld types need special handling. You may need to wrap the eld name in a Text( eldnamehere) OR Value( eldnamehere). Picklist elds need a value( eldname), and number elds need a text( eldname).


Step Two: Update the Blackthorn | Payments Email Receipt Template


1. Go to Setup
2. In the Quick Find box, enter “Email Templates.”
3. Select “Classic Email Templates.”
4. In the Folder drop-down, select “Blackthorn | Payments.”
5. Click "Receipt (HTML)" to select the template.
6. Click the Edit HTML Version button.
7. Complete the steps below to add the eld created in Step One.
a. In the Select Field Type column, select “Transaction Fields.”
b. In the Select Field column, select the “name of new eld.”
c. Copy the "Merge Field Value" from the third column and paste it into the message text (HTML Body).
8. Click Save.


Manually Send an Email Receipt
1. Open a Transaction record.
2. Go to the Activity History Related List.
3. Click the Email tab.
4. To change formatting type, click Switch to Text-Only or Switch to HTML.
5. Click Select Template and select the "Transaction Receipt" (HTML or Text).
6. Update the elds.
7. Click Send.


Troubleshooting
If you have received an error regarding email receipts or have a question, please view our Troubleshooting or FAQ page. If you still have Default Payment Method questions, please contact Blackthorn Support. We're happy to help!


FSL Overview

Use the Field Service Lightning (FSL) extension package to automate the creation of Transactions related to Work Orders. Work Order Line Items and Product Consumed objects automatically create and update the amount of money that needs to be collected from a job. That information can be used in the FSL extension package with our Mobile Payments app to
collect mobile payments.


Installing the Blackthorn FSL extension package allows customers to:

Create/Update an open Transaction automatically from a new/updated Product Consumed and Work Order Line Item.
Allows users to launch the Mobile Payments app right from the Work Order in the Field Service Mobile or from the Transaction in the Field Service Mobile.
Sets the Work Order object to be a "Transaction Parent" within the core Blackthorn Payments app.

Learn more about our Mobile Payments app here: Blackthorn | Mobile Payments.


FSL Extension Package Setup

Setup FSL and Blackthorn Payments Mobile FSL Extension Package
1. Navigate to Setup > Field Service Settings.
2. Click Enable.


Install the Field Service Managed Package
If you haven't installed the Field Service Managed Packaged yet, click https://fsl.secure.force.com/install and follow the prompts to install the managed package in your org. You can install it on a production or sandbox org.


Install the Blackthorn FSL Extension Package
Prerequisite: To install the latest FSL Extension package, you must have Payments Version 5.31 or higher.

Install the latest Blackthorn Payments Mobile FSL Extension Package.


Con gure the Transaction Object
1. Click the Gear icon.
2. Click Setup.
3. Click the Object Manager tab.
4. In the Quick Find box, enter and click "Transaction."
5. Click the Page Layout tab.
6. Click the FSL Charge Transaction Layout.
7. Drag and drop the W o rk Order eld on the page layout.
8. Click Save.


Con gure the Work Order Object
1. Click the Gear icon.
2. Click Setup.
3. Click the Object Manager tab.
4. In the Quick Find box, enter and click "Work Order."
5. Click the Page Layout tab.
6. Click FSL Work Order Layout.
7. Click Related Lists.
8. Drag and drop the Transactions Related List to the page layout.


9. Click Fields.
10. Drag and drop the Mo bile P ay , Balanc e P aid , and Balanc e Due elds on the page layout.
11. Click Save.


Assign Permission Sets
1. Identify the users that will be using the Blackthorn FSL Extension Package.
2. Assign the Blackthorn | Payments FSL permission set to those users.


Add Field Service Permissions
1. From the App Launcher, type "Field Service Settings" and navigate to the app.
2. From the Getting Started step, click the Permission Sets tab.
3. Click Create Permissions for all the Roles.
4. Click Save.


Add Field Service Territory, Work Type, and Service Resource
1. Click the Getting Started tab.
2. Click Go to Guided Setup.
3. Create a Service Territory, Work Type, and Service Resource.


4. Click the Create Dispatchers and Agents step and click Add.
5. Choose users from Assign Service Territories to Select User.
6. Select the Service Territory.
7. Click Assign Service Territory.


Create FSL Records

Create a Work Order
1. Navigate to the Work Order object.
2. Click New to create a new Work Order record.
3. Add the required elds.
4. Make sure to de ne the P ric e Bo o k when creating the Work Order.
5. Click Save.


Create a Work Order Line Item
1. From the Work Order Line Item Related List on the Work Order you just created, click New to add a new Work Order Line Item record.
2. Add the required elds.
3. Be sure to set the P ro duc t and Quantity .
4. Click Save.


The Magic of the Blackthorn FSL Extension

When a Work Order Line Item is added to the Work Order and the Work Order Total Price > 0 or Total Price changes, a new Open Transaction is automatically created. If an Open Transaction already existed, it is updated to re ect the Balance Due amount.


Create a Service Appointment

Service Appointments

If "Auto-Create Service Appointment" is selected on a work type, a child service appointment is created when a Work Order or Work Order Line Item lists that work type. Check out the Salesforce Documentation on creating Service Appointments.


1. Navigate to the Service Appointment object in the Related List on the Work Order that was created.
2. Click New to add a record.


3. Add the required elds.
4. Click Save.


Add a Service Resource
Adding a Service Resource lets you see your Work Order and related records in the FSL mobile app.

1. Go to the Service Resource Related List on the newly created Service Appointment record.
2. Click New to create a new Service Resource record.
3. Set a value for the U ser and Lo c atio n elds.
4. Set A c tiv e = "TRUE".
5. Click Save.


View Records in the FSL Mobile App
1. Go to the Field Service app on your mobile device.
2. Click the Service Appointment record that you have assigned to yourself (or to the user logged into the FSL Mobile app). Clicking the Service Appointment opens the Work Order.
3. Complete the payment process by either using the Mobile Pay option from Actions or by navigating to the Details tab and clicking Pay in the Mo bile P ay   eld.


Additional Con guration

Add Mobile Pay Action to Transaction Page Layout
The Mobile Pay action can be added to the Transaction page layout to link from the Field Service Lightning (FSL) Mobile app to the Blackthorn Mobile Payments app. This is useful for FSL Mobile app users that want to accept a mobile payment.

Complete the following setup steps to enable the feature.

1. In Salesforce go to Setup > Customize > Custom Objects.
2. Click on the Transaction object.
3. On the Transaction object, create a custom formula eld.
4. Give it any name you'd like, such as "Mobile Pay" and use this formula:


Text                                                                                                                                                                                                                                             Copy

HYPERLINK("btmobilepmt://mobilepayments.blackthorn.io/transaction?id=" & Id & "&orgid=" & $Organization.Id & "&app=fieldService","Mobile Pay")


5. Add the new eld to the Charge Transaction layout.
6. Click Save.
This will create a hyperlinked eld in your mobile app. You can use this approach and/or the App Extension below to launch Blackthorn Mobile Payments app from the FSL Mobile app.


Create an App Extension


Create an App Extension for each mobile app device type (iOS and/or Android) that you support. On iOS, this creates the blue lightning bolt button action for a single button click from the Work Order. It's a two-step con guration once our FSL extension package is installed.


1. Navigate to Field Service Mobile Settings in Setup.
2. In the section titled "App Extension," click the Add button.
3. Add the required elds. They will be similar to what is displayed in the screenshot below.


4. Copy/paste the text below into the Launc h V alue eld shown above.


Text                                                                                                                                                                                                                                                                               Copy


btmobilepmt://mobilepayments.blackthorn.io/transaction?id={!btfslmobileext__Open_Charge_Record_Id__c}&orgid=$Organization.Id&app=fieldService


5. Click Save to add the App Extension.

Once completed, the App Extension will show up in the FSL Mobile app. Be sure to clear your cached data for the button to appear. You may also have to log out and log in.


Disable the Creation of Transactions from a Work Order
To prevent the automatic creation of Transaction from a Work Order, the "Disable Transaction Create From WO" custom setting was added to the Blackthorn Payments | FSL Settings.

Follow the steps below to disable the automatic creation of Transaction from a Work Order.

1. Go to Custom Settings.
2. Click on Blackthorn Payments | FSL Settings.
3. Click New.
4. Set Disable T ransac tio n Create Fro m W O = “True”.
5. Click Save.


FSL Extension Package Release Notes

Package 1.67
Released 03 January 2024

Sandbox & Scratch Org: https://test.salesforce.com/packaging/installPackage.apexp?p0=04t4P000002Oy93QAC

Production & Dev Org: https://login.salesforce.com/packaging/installPackage.apexp?p0=04t4P000002Oy93QAC


Bug Fix
The Offline Mobile Pay URL      eld was removed from the Work Order page layout URLs section as the system only uses the eld to launch the Mobile Payments app.


Package 1.65
Released 25 April 2023

Production & Dev Org: https://login.salesforce.com/packaging/installPackage.apexp?p0=04t4P000002GJqm


Bug Fix
“Disable Transaction Create From WO,” a new custom setting, was added to the Blackthorn Payments | FSL Settings. When the setting is checked, the automation that creates a Transaction related to a Work Order will be disabled.


Package 1.64
Released 12 December 2022

Production & Dev Org: https://login.salesforce.com/packaging/installPackage.apexp?p0=04t4P000002GJlh


Enhancement
The Balance Due and Balance Paid         elds on a Work Order will update automatically when a Transaction with an amount less than the Balance Due on the Work Order is authorized. This change allows these elds to be used with authorized charges.


Package 1.63
Released 20 December 2022

Production & Dev Org: https://login.salesforce.com/packaging/installPackage.apexp?p0=04t4P000002GJIu


Bug Fixes
An error affecting Virtual Terminal users has been resolved for customers who previously used and uninstalled our Blackthorn FSL extension package.
When Work Order Line Items are deleted from a Work Order, the amount of the related Transaction record will update accordingly.


Enhancements
A new lookup eld, Payment Method , was added to the Work Order object. The new eld allows users to add a Payment Method to a Work Order in the Field Service Mobile extension package.
NOTE: Users must have the Blackthorn | Payments FSL and Blackthorn | Payments (User) permission set to access the eld.
Field Label: Payment Method

API Name: Payment_Method__c
Data Type: Lookup
An FSL user can add and authorize a payment or add a new Payment Method while connected to a Spreedly Payment Gateway. The authorized Transaction will be associated with an FSL Work Order to be used later.
To perform these tasks, two new elds -- Mobile Add Card and Mobile Authorize -- have been added to the Work Order object. The elds store links that launch the Mobile Payments app and take the user directly to the correct screen to complete the selected action. Both elds include the Blackthorn | Payments FSL permission set with Read

Access = “True”.

Field Label: Mobile Add Card

API Name: Mobile_AddCard__c
Description: Contains the URL that will launch the Mobile Payments app directly to the add card screen.
Field Label: Mobile Authorize
API Name: Mobile_Auth__c
Description: Contains the URL that will launch the Mobile Payments app directly to the authorize screen.
A Field Service Lightning (FSL) user can add and authorize a payment or add a new Payment Method while connected to a Spreedly Payment Gateway. The authorized Transaction or Payment Method will be associated with an FSL Work Order to be used later.


Flow Screen Charge Component

Coming in 2026: Deprecation of Aura Virtual Terminal Component

New Virtual Terminal con gurations should utilize our modern and feature-rich Lightning Web Component version. We plan to sunset the Aura Component and related Flow Screen Charge Component in 2026.


Don’t worry! Customers will receive advance notice of the sunset date to ensure a smooth transition.


The Flow Screen Charge component (PaymentChargeFlow) creates a Payment Method and charge Transaction with clicks, not code. This ow component can be con gured for internal or customer-facing scenarios and used with standard or custom objects.


Create a Flow
1. Before you begin, please determine the Parent object for the Transaction (Charge) object. (The Parent object was con gured in the Payments Setup Wizard.) For this example, we will use the Opportunity object as our Transaction Parent.
2. Click the Gear icon
3. Click Setup.
4. In the Quick Find box, search for and click "Flows."
5. Click New Flow.


6. Select "Screen Flow" and click Create.


Create a Get Records Element
1. Click the + symbol (Add Element) between the Start and End elements.


2. Under Data, select Get Records.
3. Fill in the following elds. This step quieries the Opportunity for the elds you want to pass into the PaymentChargeFlow component. If you unfamiliar con guring the Get Records step, please review the Flow Trailhead modules.
Label (required)
Objec t (required)
Field (required)


4. Review the additional options.
5. Close the Get Records window.


Create an "Enter Card" Screen Element
1. Click the + symbol (Add Element) between the Get Records and End elements.


2. Under Interaction, select Screen.
3. Enter a Label . (required) (In this example, we used “Enter Card.”)
4. Un-check the Sho w Header eld since the component already contains a header.
5. Review the footer con gurations.
6. Under the Components tab, locate the PaymentChargeFlow component and drag and drop it on the new screen.
7. Fill in the required elds.
A P I Name
I s Fo r Custo mer


8. Complete the optional elds as needed. To learn more about each eld, hover over each help icon. Values entered such as Currenc y = “USD” can be hard-coded. Or they can be mapped from elds such as {!opp_record.Amount} on the Transaction Parent (the Opportunity in this example). NOTE: Most elds may default to values if not set.


P ay ment Gateway I d
A mo unt T o Charge
Currenc y
Charge Desc riptio n
Charge P arent I d
A c c o unt I d
Co ntac t I d
I nput and Output - P ay ment Metho d I d
I nput and Output - T ransac tio n I d


Create a PaymentMethodId Field

1. Click the Fields tab.
2. Click in the Rec o rd V ariables eld and click + New Resource.
3. Fill in the following elds.
A P I Name = “PaymentMethodId” (required)
Data T y pe = “Text” (required)
A v ailable f o r input = “True” (checked)
A v ailable f o r o utput = “True” (checked)


4. Click Done.


Create a TransactionId Field

1. Click the Fields tab.
2. Click in the Rec o rd V ariables eld and click + New Resource.
3. Fill in the following elds.
A P I Name = “TransactionId” (required
Data T y pe = “Text” (required
A v ailable f o r input = “True” (checked
A v ailable f o r o utput = “True” (checked)


4. Click Done.


Con gure the Advanced Settings
1. Click the + symbol (Add Element) between the PaymentChargeFlow component and open the Advanced section.
2. Check the Manually A ssign V ariables checkbox.
3. Set I nput and Output - P ay ment Metho d I d = “{!PaymentMethodId]" and I nput and Output - T ransac tio n I d = “{!TransactionId}." You must enter values in these elds so the multi-step ow will know if the Payment Charge step has been completed when a user clicks the Previous button. Entering values in these elds now also makes it easy to
obtain the newly created P ay ment Metho d I D and T ransac tio n I D if you need either later in the ow.


4. Click Done.


Create a "Results" Screen Element
1. Click the + symbol (Add Element) between the Payment Flow screen and the End.
2. Enter a Label . (required) (In this example, we used “Results.”)
3. Un-check the Sho w Header eld since the component already contains a header.
4. Review the footer con gurations.


5. Click Done.


Save Your Flow
1. Click Save.


2. Enter a Flo w Label .
3. Click the Advanced section and set T y pe = “Screen Flow.”
4. Click Save.
5. Run, test, and activate the ow before using it.


Edit the Parent Object Page Layout
1. Open the Parent Object record. In this case, it’s the Opportunity.
2. Click Setup.
3. Click Edit Page.
4. Select the Flow component and drag and drop it to a narrow column on the page layout. If you have multiple Flows de ned in Salesforce, select the name of the Flow you just created in the Flo w eld.
5. Ensure the P ass rec o rd I D into this v ariable checkbox is checked.


6. Click Save.
7. Navigate back to the Parent Object (Opportunity) record and try it out. Depending on how you've con gured the PaymentChargeFlow component, it should look like one of the following images.
For customer-facing users


For internal Salesforce users


Authorize.net Payment Gateway Con guration

PREREQUISITE


You must be an Authorize.net user to use the following elds. Do not use these elds for any other scenarios. It will cause Transactions to fail.

This update is a work in progress, and support for CVV and address validation for other features will occur in future updates.


New Fields
Object: Payment Gateway
Field Label: Liv e V alidatio n Mo de (A utho rize.net)
API Name: Live_Validation_Mode__c
Data Type: checkbox
Default Value: False (unchecked)
Description:
If checked, the Payment Method will use the "liveMode" to submit a zero-dollar or one-cent Transaction (depending on the card type and the processor support) to con rm the card number belongs to an active credit or debit account.


If unchecked, the Payment Method will use the "testMode" to perform a Luhn mod-10 check on the card number, without further validation.
Component: PaymentChargeFlow
Field: Sho w A ddress
Description: When enabled, additional address elds (Street, City, State, and Country) will be visible and required. Click here for more information about adding elds.


Instructions
1. To enable CVV validations when using an Authorize.net gateway and the PaymentChargeFlow component, check the new Liv e V alidatio n Mo de (A utho rize.net) eld on the Payment Gateway record and add the Sho w A ddress eld to the PaymentChargeFlow component.
2. When both are enabled, additional address elds (Street, City, State, and Country) will be visible and required, and the validation process will occur.


Translate Custom Labels
Blackthorn Payments users can translate the labels the user sees (and override the Standard out-of-the-box values) when using the Flow Screen Charge component.


Pre-requisite Step
Before proceeding, you must enable Translations in your Salesforce org. Follow the steps below to con gure the Flow Screen Charge component custom labels.

1. Navigate to Setup.
2. In the Quick Find box, type "Custom Labels".
3. Click Custom Labels.
4. Find the Custom Labels in the "PaymentChargeFlow" category or the ones with "ChargeFlow" as a pre x. (See the chart above.)
5. Click the Label you would like to modify.
6. Click New Local Translations/ Overrides.
7. Select your Language .
8. Add the text for the label you would like to see displayed in the T ranslatio n T ex t eld.

The language displayed will depend on the Language con gured in the User Setting of the Salesforce user.


Custom Labels
The custom labels are as follows.

Custom Label Name                                                                                           API Name                        Standard Label (English)
ChargeFlow Account                                                                                                          ChargeFlow_Account                              Account
ChargeFlow Amount                                                                                                           ChargeFlow_Amount                               Amount
ChargeFlow Card Holder Name                                                                                                 ChargeFlow_Card_Holder_Name                     Card Holder Name
ChargeFlow Card Number                                                                                                      ChargeFlow_Card_Number                          Card Number
ChargeFlow Charge Card                                                                                                      ChargeFlow_Charge_Card                          Charge Card
ChargeFlow_Charge Description                                                                                               ChargeFlow_Charge_Description                   Charge Description
ChargeFlow_Contact                                                                                                          ChargeFlow_Contact                              Contact
ChargeFlow Currency                                                                                                         ChargeFlow_Currency                             Currency
ChargeFlow CVV                                                                                                              ChargeFlow_CVV                                  CVV
ChargeFlow Email                                                                                                            ChargeFlow_Email                                Email
ChargeFlow Exp Month                                                                                                        ChargeFlow_Exp_Month                            Exp Month
ChargeFlow Exp_Year                                                                                                         ChargeFlow_Exp_Year                             Exp Year
ChargeFlow Payment Details                                                                                                  ChargeFlow_Payment_Details                      Payment Details
ChargeFlow Payment Gateway                                                                                                  ChargeFlow_Payment_Gateway                      Payment Gateway
ChargeFlow_Please_Wait                                                                                                      ChargeFlow_Please_Wait                          Please Wait
ChargeFlow Postal Code                                                                                                      ChargeFlow_Postal_Code                          Postal Code
ChargeFlow Related To                                                                                                       ChargeFlow_Related_To                           Related To


FSL Mobile Actions (without our iOS/Android app)

This doc is for use without our iOS/Android apps. No card reader.

Use the below instructions if you want to use our native Salesforce Payments app within the FSL app. We packaged a few actions you can use for this. It's not as seamless as using our mobile apps, either with or without the card readers, but it allows you to process payments within FSL without an external app. If you're looking for our FSL & mobile app
integration, see the section in the navigation on our Mobile Payments add-on.


Simple Mobile Payments
We package two Lightning Actions - one on the Account object and the other our Payment Method object that can be used in the Salesforce Mobile or Field Service apps to quickly create a Card Payment Method and Charge the Card.


Add Card
Allows a mobile user to enter Credit Card info to create a Card - Payment Method record. Once the record is created in Salesforce, our Payments code will create a corresponding record in the processor's system. Check the Payment Method Status on the created record to make sure the Payment Method is valid.


Charge Card
Allows a mobile user to enter Charge info to create a Charge -Transaction and capture it. Once the record is created in Salesforce, our Payments code will create a corresponding record in the processor's system. Check the Transaction Status on the created record to make sure the charge was successful.


Typical Mobile Use Case
1. From an Account record, click the Add Card button. Enter Card elds and save.
2. Navigate to the Payment Method record and check the Payment Method Status eld to make sure it is "Valid". Then click the Charge Card button on the Payment Method, enter the Amount and Description and save. This creates a Charge Transaction that will be "Captured" in the processors's system and it copies over the Account, Contact, Payment
Method, and Payment Gateway elds. It also uses the default Currency de ned on the Charge Record Type.
3. Navigate to the Transaction and check that the Transaction Status = Completed.


Setup
To make these actions visible to Salesforce Mobile or Field Service app users, edit the Account Page layout for the user and drag the Add Card Mobile and Lightning Actions to the Salesforce Mobile and Lightning Experience Actions section at the top of the Page Layout and save.

The Charge Card action should already be on the Payment Method page layout. If it's not, follow the same instructions above to add it to the page layout.


Customize for Your Needs
If you need the "Add Card" action on some other custom or standard object, you can use the action we created as a template for a new one. Go to the Buttons, Links and Actions section of any object and click the New Action button. When creating the Action, look at how the "Add Card" Action is con gured on the Account. You can also use pre-populate some
elds using the Prede ned Field Values section that's available after you create the Action.


Authorize, Capture or Refund
Users can now authorize, capture, and partially refund transactions through the mobile app.


High Volume Batch Processing

Opt-In Process

High-volume batch processing is now available. If you want to enable the feature, please contact Blackthorn Support. There is no additional cost.

Support will guide you through testing in a sandbox before determining the nal value for the batch size setting. The value is based on the speci c customizations in your org.


High-volume batch processing enables the scalability of our batch processes. The new logic queries high volumes of Transactions, splits the results, and invokes concurrent batches. Previously, the batch processes were limited to one record at a time to ensure that Payments was compliant with Salesforce's limits.

The new protected custom setting, A uto -Charge Batc h Size (Auto_Charge_Batch_Size__c), controls the batch size of the scheduled job. The default setting is 1. Currently, the maximum supported value is 75.


About the Schedule High Volume Transaction Job Button
The Schedule High Volume Transaction Job button is located on the Blackthorn | Payments Admin page’s Scheduled Job tab.

The Schedule High Volume Transaction Job button is available when the auto charge batch size exceeds 1.
The Schedule Billing Jobs button is visible when Stripe Billing is enabled through a future date.
The Schedule High Volume Transaction Job button is hidden when the batch size resets to 1.
When the Schedule High Volume Transaction Job button is clicked, the Blackthorn | Payments Daily Captures - High Volume scheduled job will replace the Blackthorn | Payments Daily Captures job and will run at midnight.


Schedule the Blackthorn | Payments Daily Captures – High Volume Scheduled Job
Click the Schedule High Volume Transaction Job button to trigger the Blackthorn | Payments Daily Captures – High Volume scheduled job and schedule Transaction auto-charge batches using the batch size determined during testing.

You should see the “Success High Volume Transaction Job has been scheduled” success message.

To con rm that the scheduled job has been scheduled, complete the following steps.

1. Click the Gear icon.
2. Click Setup.
3. In the Quick Find box, enter and click “Scheduled Jobs.”
4. Verify that the Blackthorn | Payments Daily Captures scheduled job has been deleted and replaced with the Blackthorn | Payments Daily Captures - High Volume scheduled job.
5. Con rm that the Blackthorn | Payments Daily Captures - High Volume scheduled job is scheduled to run at midnight.


Historical Sync
If you were a Stripe customer before coming to Blackthorn Payments, you may want to sync your Payment Gateway Customers, Payment Methods (Cards and Bank Accounts), and Transactions (payments) from Stripe to Salesforce.

During the sync, if the Payment Gateway Customer email matches a Salesforce Contact's Email , the matching Contact will be populated on the Payment Gateway Customer's Contact lookup eld.

If the Payment Gateway Customer's email matches with more than one Contact record Email , the Payment Gateway Customer's Contact lookup eld will not be populated.

Blackthorn Payments has no Contact creation logic.


Related record matching on 4.163 and beyond

We no longer have hard-coded matching based on email and rst name. Matching is now handled using your active Salesforce Duplicate Rules. Click here for more information.


If you want a Contact record created, either create/update the Salesforce Contact record with the same email from Stripe. Do this before syncing/creating a Process Builder to create a Salesforce Contact when the Payment Gateway Customer record is created in Salesforce.

The sync process is only to migrate your records from that moment backward. Syncing Stripe with Salesforce going forward can be done through Webhooks, but you should not be originating records outside of Salesforce.


Sync Historical Data
You can easily transfer historical data or customers, Payment Methods, and Transactions from Stripe to Blackthorn Payments.

Before you start...

There are several ways to match data that syncs into Salesforce. Before you begin, con rm that your custom data, matching logic, or metadata is set up correctly. If you need help or want to chat, go to the Community where Support and Onboarding are available to help.

Review the instructions below and move through each of the following sections.

1. Sync your Stripe records in this order.
a. Customers - wait until this job is done before proceeding.
b. Payment Methods - wait until this job is done before proceeding.
c. Charges/Refunds - wait until this job is done before proceeding.
d. Payouts
2. Start with a small date range.
Select a small date range for a few Customer records to bring into Salesforce. This way you can con rm that everything looks correct and has related correctly before syncing everything.
3. Review how the emails match.
During the sync, if the Payment Gateway Customer's Email matches a Salesforce Contact's Email , the matching Contact will be populated on the Payment Gateway Customer's Co ntac t lookup eld.
BUT, if the Payment Gateway Customer's Email matches with more than one Contact record's Email , then the Payment Gateway Customer's Co ntac t lookup eld will not be populated.


Steps

When using this function, there are no "undo" calls, so be careful with your button click. If you want to make sure everything comes over correctly, sync a short amount of records before syncing them all.


1. Go to the Payment Gateway record you want to sync.
2. Click the upside-down carrot and then click Sync with Stripe.
3. There are three tabs: Core, Billing, and Connect. Core is for traditional Stripe, Billing is for Stripe Billing, and Connect is for Stripe Connect.


4. Select the Core tab.
5. Choose a date/time range for the data sync by entering values in the Fro m: and T o : elds, if applicable.


6. Click Customers to sync customers, Payment Methods for Payment Methods, or Charge/Refund for Transactions.


7. A message will appear letting you know the process has started.
When using this function, there are no "undo" calls, so be careful with your button click. If you want to make sure everything comes over correctly, sync a short amount of records before syncing them all.


Suggestion: If you have a lot of records (10,000+), click the relevant button and let it run all night.


Historical Apex Job
To monitor each Historical Sync, navigate to Apex Jobs.

Lightning/Classic: Setup > In Quick Find, Search and Click: "Apex Jobs".

The Apex Class is called "PaymentGateway_SyncBatchable".

Suggestion: Click Abort next to the "In Progress" job if you need to cancel the job.


Level 3 Processing
Blackthorn supports "level 3 processing" via Stripe as part of Blackthorn Payments. We have internal documentation for level 3 processing that we'll share with you upon request.

In short, level 3 gets you the best processing rate available by providing the gateway and processor full transaction details, such as you would see on an order. These include line-item level details, such as the quantity, product, and pricing details of each item that's part of the transaction.

Here are some requirements that Stripe calls out in their documentation:

Only Visa and Mastercard are supported.
You must provide the customer billing details—name, address, city, state, ZIP code—associated with the card. Assuming this means that the Payment Method used for the Transaction has all of these elds populated.
Only e-commerce is supported, not physical retail.
Total Amount Check - The sum of all the line items in the Level 3 data, including any discounts, taxes, and shipping costs, must exactly match the total amount collected. Attempting to collect more or less than the sum of all the line items will result in an error and a declined payment.


Salesforce Requirements
Any customer that wants to send Level 3 data to Stripe must:

Get Level 3 Charge Data enabled with Stripe
Check the Level 3 checkbox on their Stripe Payment Gateway record(s)
Generate an Invoice with Line Items and associate the Invoice to a Transaction before it’s captured.

Note: from Stripe, “Level 3 data cannot be modi ed after a charge is captured”.


Stripe Documentation
https://stripe.com/docs/level3
https://stripe.com/docs/api/payment_intents/create#create_payment_intent-level3
https://stripe.com/docs/api/charges/object#charge_object-level3


Matching and Duplication
Relationship Settings give you better control over Lead, Contact, and Account matching and creation. With this feature, you can de ne which records should be matched and created when a Payment Gateway Customer is created.


Before You Start
The following notes are important to review before you start.

Matching criteria are based on Matching and Duplication rules speci ed in Setup. The Account, Contact, and Lead objects are compared to either nd a match or create a new record.
Matching and Duplication rules are required for the Relationship Settings "Create New Record If No Match" and "Only Relate a Matched Record" options.
We recommend using the Standard Salesforce Matching and Duplication rules for Accounts, Contacts, and Leads. If you do not enable the Standard Salesforce Matching and Duplication rules, the Relationship Settings will not know which items to match when creating a new record.


How Does It Work?
The Relatio nship Settings eld is located on the Payment Gateway object. This eld controls how Payment Gateway Customers, Accounts, Contacts, and Leads are created on a Payment Gateway. To allow for a variety of scenarios, the Relatio nship Settings eld can be de ned differently for each Payment Gateway your organization uses.

Relationship Settings records de ne the matching and/or creation preferences for your org.

The logic starts with the Payment Gateway Customer and rolls down to the customer’s Payment Method. The following steps show the order of execution.

1. The new Payment Gateway Customer (PGC) record is added to Salesforce via API and webhooks.
2. The PGC record is compared to your active duplicate rules in conjunction with your Relationship Settings. (Duplicate rules determine what is or isn’t a match.)
3. The Relationship Settings determine how to match existing Accounts, Contacts, and Leads to the PGC record.
4. If your settings are con gured to do so, a new Account, Contact, and Lead record will be created.


Did you upgrade Payments?

Users upgrading Payments will need to manually deactivate the current “Payment Gateway Customer Dup Rule” matching rule and activate the new Payment_Gateway_Customer_Matching_Rule2 matching rule. The new matching rule will be installed automatically for new installations.


Con gure Your Relationship Settings
1. Click the App Launcher.
2. Type and click “Relationship Settings”.
3. Click New in the top-right-hand corner of the page.


4. Enter a Name . (required)
5. Select a Relatio nship Rule .
“Only Relate A Matched Record”: This setting updates existing records. It doesn’t create new records.
“Create New Record If No Match”: This setting creates a record if a match isn’t detected.
“Always Create A New Record”: This setting ignores duplication rules and creates a new record even if an existing record already exists.
“No Matching Or Record Creation”: This setting prevents matching and the creation of new records.
6. De ne a Create Rule . This eld selects the type of related record to be created.
7. Select an Account, Contact, or Lead record type, if using.
8. Click Save.




Default Relationship Settings
You can only mark one Relationship Setting record as the default setting for your org. A validation rule exists to prevent multiple records from being set to default.


Example
1. Set Relatio nship Rule = "Create a record if no match".


2. Set Create Rule = "Lead".
3. Create a customer in Stripe.
4. Wait for webhooks to process. Or manually process webhooks by navigating to your Payment Gateway, clicking Sync with Stripe , and clicking Sync Customers.

Once the sync is nished, your new Lead record and Payment Gateway Customer will be generated in Salesforce.


Additional Fields for Matching Logic Variations

Match Records
Some scenarios do not require matching on all three objects: Accounts, Contacts, and Leads. The Matc h Rec o rds eld is a multi-select picklist that allows users to select which object they want to use for matching.


Important

If you leave the Matc h Rec o rds eld blank and don't have active duplicate rules for Lead, Contact, and Account, you will receive an error in the Blackthorn Logs. Additionally, if this eld is blank your current matching logic will not continue to nd matches.


Match All Email Fields
If the Matc h A ll Email Fields eld is checked, the duplication logic will look for all email elds from the object selected in the Matc h Rec o rds eld and execute matching criteria based on the matching rules in Settings.


Requirement
You must create matching and duplication rules for each email address eld if you use the Matc h A ll Email Fields eld.


Use Case
Let's say you want to match the Email eld on a new Payment Gateway Customer to a custom eld named W o rk Email on the Contact object.

1. Create a matching and duplication rule from Setup for the W o rk Email eld on the Contact object.
2. Add your Relatio nship Settings to your Payment Gateway record.
3. Set Matc h Rec o rds so “Contact” is one of the values selected.
4. Check the Matc h A ll Email Fields checkbox.
5. Create a Contact record with W o rk Email populated.
6. Create a Payment Gateway Customer with the same value that was used for the Contact W o rk Email eld.
7. After clicking Save, notice the existing Contact record is populated in the Co ntac t lookup on Payment Gateway Customer.


Multi-Currency

Introduction
Blackthorn | Payments can process Transactions in any currency that Stripe supports. All supported currency records live as Custom Metadata Type records in Salesforce.

Processing Transactions in any currency does not require the Salesforce feature "Multi-Currency". Our amount elds are number elds, not currency elds, and thus the Salesforce Multi-Currency feature is not related to the Blackthorn | Payments' Multi-Currency feature.

Note
If you do use the Salesforce Multi-Currency feature, you may want to write a trigger whereby when the Transaction's Currency ISO eld is set, update the record's SFDC Currency, just make sure you don't have any picklist value con icts so it wouldn't block the Transaction record update.


How it works
The Transaction object has a picklist eld called Currency ISO . When the user selects their desired processing currency, such as "USD", the app references the "USD" currency record in Custom Metadata Types and veri es a few things against the Transaction.

For example, the minimum amount for USD currency is .50 cents, so if you try capturing a Transaction for the amount of .45 cents an Apex validation error will be thrown instructing you to increase the amount.


The validation has been disabled by default. To enable this validation, go to the Custom Setting, "Blackthorn | Payment Triggers" and check the "Enable Transaction Min Amount Validation."


Out-of-the-box all currency values are deployed and available under the Currency ISO           eld.
If you don't want users to see certain currencies, complete either option below.


Deactivate Currency Values
Navigate to the Transaction object.

Lightning: Setup | In the Quick Find, Search and Click: "Object Manager".

Classic: Setup | In the Quick Find, Search and Click: "Objects" under Create.

Click on the Transaction object.
Navigate to Fields & Relationships (Lightning) or Custom Fields & Relationships (Classic).
Click on the Currency ISO      eld.

Scroll down to "Values."
Click "Deactivate" next to the currency value(s) you don't want to be shown.


Remove Currency Values on Record Type
Navigate to the Transaction object.

Lightning: Setup | In the Quick Find, Search and Click: "Object Manager".

Classic: Setup | In the Quick Find, Search and Click: "Objects" under Create.

Click on the Transaction object.
Navigate to Record Types.
Click on the "Charge" Record Type.
Click "Edit" next to Currency ISO.
Move any currency values that you don't want to be shown from "Selected Values" to "Available Values".


Default Currency


Defaulting the Currency ISO     eld should happen per Record Type within the Transaction object. Follow the "Remove Currency Values on Record Type" instructions above and when you click "Edit" next to the Currency ISO       eld, set the Default   eld. Repeat this for any additional Record Types you use.


Next Steps
Setup a Default Payment Method for your Contact and Account Records.
Understand how Transactions are processed.
View all of our Custom Setting records.


Troubleshooting
If you have received an error with your Payment Schedule or have a question, please view our Troubleshooting or FAQ page. If you still have Default Payment Method questions, please contact Blackthorn Support. We're happy to help!


Introduction
PayLink is our beautiful, mobile-responsive payment request, add-on. For every Transaction that's created, a unique link (PayLink) is created. This link can be rolled up to the Transaction's parent, such as an Opportunity, as well as automatically emailed to your customer.


Supported Payment Methods
Cards
ACH (automated clearing house)

Payments can be processed in over 100+ currencies. List of Supported Currencies.

PayLink is mobile responsive, which means it automatically adjusts the sizing, layout, and proportions to display properly on any device.

If accepting ACH (Bank Account) for payment in PayLink, our system will detect an identical bank account that already exists in Salesforce for the customer and will re-use that ACH Payment Method instead of creating a new Payment Method record. This is done because Stripe does not allow duplicate bank accounts for a customer.


Getting Started

Follow our Payments quick start instructions and install PayLink from the Setup Wizard.


Setup & Con guration

For Government Cloud Users

Government Cloud users who want to use PayLink need to reach out to Blackthorn Support to have instanceUrl added to their PayLink license.


Install PayLink
1. Navigate to the Payments Setup Wizard to install PayLink.
2. Once the install has completed, go to the Blackthorn | PayLink Setup Wizard.


PayLink Setup Wizard


Con guration Video


Initial Con guration
1. Navigate to the Blackthorn PayLink app.
2. Click the PayLink Con guration tab.
3. Click New.


4. Enter a Name . (required)
5. Set Def ault = “True” (checked) if this record will be the default record.
6. Move accepted payment method types from the Available column to the Chosen column.
7. Set Currenc y Sy mbo l to “Symbol” or “ISO”. (The default setting is “Symbol”.)
Example for US dollars
Symbol = “$”
ISO = “USD”
8. Add the A c c eptanc e Language , if using.
9. Add the T erms and Co nditio ns URL, if using.
10. Use the following elds to con gure the PayLink’s appearance.
Lo go (U RL) (The URL must originate outside of Salesforce.)
Bac k gro und Co lo r (#)
Card Co lo r T heme
Bac k gro und I mage (U RL)
Butto n Co lo r (#)
Due Date Label (This eld overrides the Transaction Due Date eld.)


A mo unt Due Label (This overrides the Transaction A mo unt eld.)
Requested By Label (This overrides the Transaction A c c o unt eld.)
11. Click Save.


Acceptance Language and Terms & Conditions Functionality

Pre-requisite

The A c c eptanc e Language eld must be lled.


If the A c c eptanc e Language eld has a value, the following will occur.

A checkbox will appear on the PayLink checkout.
The text entered in the A c c eptanc e Language eld will be the checkbox label.


If the A c c eptanc e Language eld has a value AND the Terms and Conditions eld contains a URL, then the checkbox label will be hyperlinked with the URL.

BUT if the A c c eptanc e Language eld is Blank, the checkbox and the accompanying hyperlinked text WILL NOT be visible.


Image Size Considerations
When adding a background image to PayLink using the Bac k gro und I mage (U RL) eld, consider how the image will appear in PayLink.

We recommend using an image le no larger than 1MB.

Keep in Mind:

The image you provide will cover the whole page.
All images have a certain ratio (height and width). You may need to adjust your image outside of Salesforce based on the viewport of the devices being used.
If your image includes text, make sure it is not cropped on different devices (desktop, tablet, mobile). You may need to edit your image outside of Salesforce to reorient the text.


Please Read

For those using Government Cloud OR who have disallowed logins from "login.salesforce.com" in their org, please contact Blackthorn Support with your Salesforce org’s My Domain after installing PayLink. You can nd the My Domain at Setup > My Domain.


Now that your PayLink is customized, learn how it works.


How It Works

Existing PayLink Customers

If you used PayLink prior to the upgrade, click here.


Charge Transaction
When you create a Transaction, a unique PayLink is generated.
This link can be emailed manually or automatically to your customer for payment. See our Use Cases for speci c examples.

PayLink Configuration       eld
Either set manually or if you have a default PayLink con guration record, it will be set automatically.


There are ve elds that populate onto the PayLink Screen: Amount , Currency , Contact or Account , Due Date , and Description from the Transaction record.


Multiple Payment Gateways

Enter a value in Payment Gateway before saving.
PayLink will use the default Payment Gateway if that eld is empty.


Payment Process
When your customer receives the PayLink, they will:

Select "Pay" in the top right corner.
Enter their Payment Method and click Pay. (By default, a postal code is only required for users from the USA and Canada. It is optional for all other countries.)
Review and accept the Terms and Conditions.
Download their receipt (printer icon).
If you enabled Email Receipts, they will receive a receipt too.


Pay Button

Uses Stripe.js to collect card information from the user and stays PCI compliant. Learn more about Stripe.js


Next Steps
Completed Card Transaction
Completed ACH Payment


Card

Completed Transaction
The following Transaction elds are updated:

T ransac tio n Status = "Completed"
P ay ment Status = "Captured"
P ro c essed Date = date and time of submitted payment
P ay ment Metho d is added to the Transaction record.

A new Payment Method and Payment Gateway Customer record are created (if this is the rst payment) or a new Payment Method will be created and linked to the existing Payment Gateway Customer (based on email matching).


PayLink Link

The unique link always works, so if the customer needs to view the payment or print another receipt, they can reopen it anytime, but it can only be paid once.


ACH

Completed ACH Payment Method


A Payment Method will be created in Salesforce with a Status of Pending.
Two micro-deposits will be deposited into their Bank Account within the next 3-5 days.


Micro-Deposit with Stripe vs Authorize.net

This is with Stripe. If you're using Authorize.net with a merchant that does not require a micro-deposit, the micro-deposit veri cation is not needed and your Payment Method will be immediately Valid and available to use.


Enter the two micro-deposits on the Pending ACH Payment Method record


Payment Method Status updates to Veri ed
Refresh the page for the updated status.
Navigate to the related lists, Transactions
Manually capture all related Open Transactions


Enable the Skip ACH Validation Custom Setting
1. Go to Setup.
2. In the Quick Find box, search for and click “Custom Settings.”
3. Click Manage next to Blackthorn Pay - Trigger Settings.
4. Click Edit.
5. Set Sk ip A CH V alidatio n = “True” (checked).
6. Click Save.

To ensure the ACH Micro-Deposit Veri cation is fully waived, contact Stripe support to have ACH micro veri cation turned off for your account.


Upgrade
We made PayLink it's own app to give you more independence. In addition to a few internal process changes, you no longer have to rely on us to con gure your PayLink or reauthorize the connection.


Prerequisite
Before upgrading PayLink, please upgrade the Payments app to the most recent version.


Installing PayLink
1. Navigate to the Blackthorn Payments (Admin) app.
2. Select the Blackthorn | Payments Setup Wizard.
3. Click on the PayLink step.
4. Click the Install button.
5. If the existing PayLink breaks during the upgrade, reauthorize PayLink by completing the following steps.
a. Go to the PayLink Setup Wizard tab.
b. Click Authorize.
c. Click Grant Access.
6. If you had any processes (Process Builder, Flows, Triggers, Validations, etc) around the old PayLink eld, please update them to reference the new PayLink eld.
7. Once the PayLink package installed, navigate to the PayLink app, and click "Blackthorn | PayLink Setup Wizard"
8. Navigate to Permission Sets
9. Assign the user to PayLink (User) and Payments (User)
10. Navigate to the Charge Transaction Page Layout. The new PayLink eld will only work on the Charge Transaction record type.
11. Remove the old PayLink eld.


12. If you are not seeing the new "PayLink" section, edit the Transaction layout and mimic the below con guration.


It's now time to con gure your PayLink template.


PayLink Trial
When you install PayLink, you will be given a 14-day trial for all users in your organization. After the 14-day trial is complete, you must assign the enabled PayLink licenses to your users or contact Blackthorn Support to purchase PayLink.


Update Existing Transactions
If you need to update your existing Transactions with the new PayLink eld, please paste the below code and execute in the developer console.

This script will only update Transactions with a Charge Record Type and with a Transaction Status of Open. You'll need to keep executing this script in the Developer Console until you see, "ALL DONE - NO MORE RECORDS TO UPDATE" in the log.


Default PayLink

Before mass updating your Transactions with the new PayLink, make sure you have marked a con guration record as the default.


Plaintext                                                                                                                                                                                                                                       Copy

Map<String,Schema.RecordTypeInfo> transactionRecordTypes = Schema.SObjectType.bt_stripe__Transaction__c.getRecordTypeInfosByName();
Id chargeRtId = transactionRecordTypes.get('Charge').getRecordTypeId();

List<bt_stripe__Transaction__c> transactionsToTouch = [select Id from bt_stripe__Transaction__c where bt_paylink__PayLink__c = null
and RecordTypeId = :chargeRtId and bt_stripe__Transaction_Status__c = 'Open' limit 100];

if (transactionsToTouch.size() > 0) {
for (bt_stripe__Transaction__c t : transactionsToTouch) {
System.debug(LoggingLevel.INFO, 'touching record id = ' + t.Id);
}
update transactionsToTouch;
} else {
System.debug(LoggingLevel.INFO, 'ALL DONE - NO MORE RECORDS TO UPDATE');
}


FAQ
If you receive the error below from a user accessing PayLink, it is because they don't have the permission set assigned to them.

ERROR:


Plaintext                                                                                                                                                                                                                                             Copy

Error element myRule_1_A1 (FlowRecordCreate).
This error occurred when the flow tried to create records: CANNOT_INSERT_UPDATE_ACTIVATE_ENTITY: bt_paylink.TransactionTrigger: execution of AfterInsert caused by: bt_paylink.SObjectService.SObjectAccessException: Paylink: You do not have permission
to update this object: Transaction Class.bt_paylink.SObjectService: line 88, column 1 Class.bt_paylink.Transaction_GeneratePaylink: line 26, column 1 Class.bt_paylink.SObjectTrigger.handle: line 96, column 1 Class.bt_paylink.TriggerHandler.manage:
line 125, column 1 Trigger.bt_paylink.TransactionTrigger: line 2, column 1.


FIX: Assign user to the Blackthorn | PayLink (User) permission set.


Use Cases

Automated PayLink with Opportunities

Scenario
A common use case is that a salesperson will close an Opportunity and send the customer a link to the payment request.

To do this, you can build three things all without code:

A Process Builder process to automatically create a Transaction record when the Opportunity Stage = "Closed Won".
A Process Builder process to automatically roll-up the PayLink on to the Opportunity record.
A Work ow Rule with an Email Alert to automatically email the PayLink to the customer.


Instructions

Step One

Create a custom URL type eld on the Opportunity object called PayLink .

Create a lookup type eld on the Opportunity object called Billing Contact that looks to the Contact object and is ltered by the Account record on the Opportunity.
This is for sending a Work ow email all from one object (Opportunity). Alternatively, roll-up a related Contact Role record from the Opportunity to populate this value too.


Step Two
Auto-create the Blackthorn | Payments Transaction from the "Closed Won" Opportunity.


Create a new Process Builder.
The process starts when A record changes.
Click the "+ Add Object", type in "Opportunity", and select "when a record is created or edited".
Save.
Click the "+ Add Criteria", name your criteria and select " Conditions are met".
Under eld, nd Opportunity Stage , set to "Equals", and pick "Closed Won" for the value.

Under Immediate Actions, click "+ Add Action".
Action Type = Create a Record, name your action and Record Type = "Transaction".
Set Field Values for ve elds:


Plaintext                                                                                                                                                                             Copy

- Amount = Type: Formula, Value: Opportunity. Amount
- Opportunity = Type: Reference, Value: Opportunity. ID
- Description = Type: Formula, Value: Opportunity. Description
- Due Date = Type: Formula, Value: Opportunity.CloseDate
- Contact = Type: Reference, Value: Opportunity.Billing_Contact


Alternatively to the Contact   eld, you can populate the Account lookup onto the Transaction with the Opportunity Account . Just note, if you want both lookup elds on the Transaction, the Account lookup will supersede the Contact lookup when viewing the PayLink form.


Step Three

After the Immediate Action, select "Evaluate The Next Criteria".
Click the "+ Add Criteria", name your criteria "Amount is changed" and select " Conditions are met".
Set Condition: Opportunity Amount      eld, Is Changed, Boolean, True


Under Immediate Actions, click "+ Add Action".
Action Type: Update a Record, name your action: Update Transaction Amount
Select No criteria-just update the records!
Set the eld values:


Plaintext                                                                                                                                                                                                                                                                   Copy

- Amount: Type: Formula, Value: Opportunity. Amount


Activate the Process Builder.


Step Four
Auto roll-up the PayLink from Transaction to Opportunity. This will allow you to use the PayLink in the Email Alert.

Create a new Process Builder.


The process starts when A record changes.
Click the "+ Add Object", type in "Transaction", and select "only when a record is created".
Save.
Click the "+ Add Criteria", name your criteria and select " Conditions are met".
Under eld, nd Transaction Opportunity , set operator to "IS NULL", type to "Boolean" and pick "False" for the value.

This criteria is telling the process only to re when the Transaction has a related Opportunity.
Under Advanced, check "Yes".


Under Immediate Actions, click "+ Add Action".
Action Type = Update Records, name your action and select Record Type = "Opportunity".
No criteria-just update the records!
Field = PayLink , Type = Formula, Value = "bt_stripeTransactionc. bt_paylinkPayLinkc".
Activate the Process Builder.


Step Five
Create a Work ow Rule with an Email Alert to automatically email the PayLink to the customer.

Create the Email Template.
Here is an example Email Template.


Create the Work ow Rule and Email Alert. This will email your customer when the Opportunity is "Closed Won" and there is a PayLink value.
Here is an example Work ow Rule and Email Alert.


Boom! Done.


Transaction Reattempt Noti cations

Failed Transaction Follow Up
When Transactions fail and are reattempted, it is a good thing to follow up with the customer to notify them and update their card or bank account information if the Transaction continues to fail.

For the use case below, we will be creating a Process builder to send out an automated email noti cation to the customer after the second reattempt and then notify the sales rep on the third reattempt.


Step One
Create an Email Template and Email Alert
These two records will be referenced later in a Process Builder.


Example Email Template:


Example Email Alert:


Step Two

Create a Process Builder that will automatically send out the Email that we just created above and notify the Transaction owner.

Create a new Process Builder.
The process starts when A record changes.
Click the "+ Add Object," type in "Transactions," and select "when a record is created or edited."
Save.
Click the "+ Add Criteria," name your criteria and select " Conditions are met."
Under eld, nd Transaction Reattempt Number, set to "Equals," and value of "2".
Under Immediate Actions, click "+ Add Action".
Action Type = Email Alerts, name your action and Email Alert = The name of your Email Alert you created above.
Click "Save."
Under "False" click the "+ Add Criteria," name your criteria and select " Conditions are met."
Under eld, nd Transaction Reattempt Number, set to "Equals," and value of "3".
Under Immediate Actions, click "+ Add Action".
Action Type = Post to Chatter, Action Name: "Notify Transaction Owner", Post To: This record.
Message: Enter any custom message you would like.Example Message: @[{![bt_stripe__Transaction__c].OwnerId}] Contact the customer on this Transaction. Their Payment Method is incorrect and needs to be updated in order for the Transaction to process. An email has already been sent with a PayLink to update their Payment Method.
Click "Save."
Click "Activate."


On third reattempt, Chatter post will automatically get created and notify the Transaction owner.


PayLink Multilingual Support Overview
The Data Dictionary provides multilingual support, allowing Admins to establish a default language that serves as the primary language for all users. For example, you can override button labels and other static text on your PayLinks.

Admins can also override the default language and customize users' language experiences when speci c prede ned criteria are met. For example, an Admin can change the language for users in a particular region.

Content will be presented in a user’s preferred language or default to English if a language isn’t pre-selected. Users won’t have to manually select their language each time they interact with the system, and they can change the displayed language according to their preferences.


New Fields
The Transaction object now includes two new elds, the Data Dic tio nary Gro up eld and the P ay Link Display Language eld.


Data Dictionary Group
The Data Dic tio nary Gro up eld creates a link between the Data Dictionary Group and the Transaction records.

Field Name: Data Dic tio nary Gro up
API Name: bt_stripe__Data_Dictionary_Group__c
Data Type: Lookup(Data Dictionary Group)
Description: Select the appropriate Data Dictionary Group containing the translated override values (Data Dictionary Entries) for the chosen language.


PayLink Display Language
The P ay Link Display Language eld contains a list of languages that an Admin can choose from to display to the PayLink to the end user.

• Field Name: P ay Link Display Language
• API Name: PayLink_Display_Language__c
• Data Type: picklist
• Description: List of supported display languages for the PayLink. This eld is set to English by default.


Warning

Do not use the new Display Language (Display_Language__c) and Data Dic tio nary Gro up (bt_stripe__Data_Dictionary_Group__c) elds on the PayLink Con guration object. They are not functional.


How It Works
The following logic describes how the Data Dictionary Group / Data Dictionary Entry records interact with the P ay Link Display Language eld.

PayLink labels are displayed in English, the default language, when either of the following is true.
The Transaction’s P ay Link Display Language and Data Dic tio nary Gro up elds are blank.
The Transaction’s P ay Link Display Language eld is blank, and the Data Dic tio nary Gro up does not have a Data Dictionary Entry for English.
PayLink labels use a Data Dictionary Entry’s values if the attached Transaction’s Data Dic tio nary Gro up has a Data Dictionary Entry record that uses the same language as the Transaction’s P ay Link Display Language .
PayLink labels are displayed in the selected Transaction P ay Link Display Language if a Data Dictionary Group does not include a Data Dictionary Entry record for the selected P ay Link Display Language .
PayLink labels are displayed in English if a Data Dictionary Group has a Data Dictionary Entry record with Language / Lo c ale = “English,” and the Transaction’s P ay Link Display Language eld is blank.
PayLink labels are displayed in the selected Transaction’s P ay Link Display Language when the Transaction’s Data Dic tio nary Gro up eld does not have a value.


Select a Method - PayLink

Data Dictionary
The PayLink’s eld labels, button text, and checkout screen text will be written in the language selected in the P ay Link Display Language eld on the Transaction record. If the P ay Link Display Language eld is blank, the labels, button text, and text on the checkout screen will default to English.

The translations on the PayLink can also be overridden by using the Data Dictionary. Use the instructions below to create a Data Dictionary Group from the Transaction record.


Required Licenses and Permission Sets
To use the Data Dictionary feature, you must have a Blackthorn Payments license, as well as access to the following elds:

Create/Read/Update - Data Dictionary Group
Create/Read/Update - Data Dictionary Entry


Supported Languages
We do not currently support all languages. The following is a list of the languages we support.

Arabic
Chinese (Simpli ed)
Chinese (Traditional)
Czech
Danish
Dutch
Finnish
French
German
Haitian Creole
Hindi
Hmong
Hungarian
Indonesian
Italian
Japanese
Korean
Norwegian
Polish
Portuguese
Romanian
Russian
Somali
Spanish
Swedish
Thai
Turkish
Vietnamese


One-to-One Relationships
A Data Dictionary Entry record contains three important elds: V alue , Key , and Language / Lo c ale . In each Data Dictionary Entry record, the elds interact as follows:

There can be only one value in the Language / Lo c ale eld.
Each Key is associated only with one V alue .

Creating a second line in the Data Dictionary Entry using the same Key as the rst line but with a different V alue will replace the rst V alue with the new one.

Example:

Line 1: Key = "LBL_CHECKOUT" and V alue = "Checkout"
Line 2: Key = "LBL_CHECKOUT" and V alue = “Proceed”
Result: The Attendee will see “Proceed.”


Create a Data Dictionary Group
If you want to override out-of-the-box values, the rst step is to create a Data Dictionary Group and populate it with Data Dictionary Entries.

1. In the App Launcher, enter and click “Data Dictionary Group.”
2. Click New.


3. Enter a Data Dic tio nary Gro up Name .
4. Click Save.


5. Click New next to Data Dictionary Entry.


6. The Data Dic tio nary V alues eld contains the Language / Lo c ale , Key , and V alue . Click the PayLink Data Dictionary (a Google document) for Key and V alue information.
7. Here are few frequently used Data Dictionary values and their keys:
Key = "LBL_TOTAL" and V alue = "Total"
Key = "LBL_INVOICE" and V alue = "Invoice"
Key = "LBL_BALANCE_PAID" and V alue = "Balance Paid"
Key = "MSG_PROCESSING_TRANSACTION" and V alue = "Processing transaction..."
Key = "MSG_AUTHORIZE_CREDIT_CARD_WITH_NAME" and V alue = "I authorize (XYZ) to charge my credit card."
8. Select the Language / Lo c ale you'd like to change.
9. Enter a Key and V alue .
10. Click Add Row to add additional entries or click Save.
11. Click Back to return to the Data Dictionary Group record.


If you need to add additional keys to the Data Dictionary Entry, click the menu (upside down triangle) next to the Data Dictionary Entry. From there, click Add Row to add a new Key and V alue . When you are done, click Save and Back to return to the Data Dictionary Group.


USE CAPITAL LETTERS

In the Key   eld, use capital letters.


Example

For this example, we will set Language / Lo c ale = "German". Now, we can select any word or phrase to replace an action with. Set Key = “LBL_DUE_DATE“ and V alue = “Faelligkeitsdatum”. Make sure to use all capital letters for the Key .


Add a Data Dictionary Group to a PayLink Con guration
1. Open an existing PayLink Con guration record or create a new one.
2. Click the Pencil icon next to the Data Dic tio nary Gro up eld.
3. Select a Data Dictionary Group.
4. Click Save.


Default Language

Change the Default Language
The following functionality has been added.

PayLink checkout will be displayed in the language selected on the PayLink Con guration record.
Labels will default to English if the Display Language eld on the PayLink Con guration record is left blank.
The language on labels and buttons can be overwritten with a Data Dictionary Group record containing the matching Key and V alue .
The date will be formatted based on the language selected on the PayLink Con guration record. If no language is selected, the date format will be based on the browser’s location.


Translate a PayLink Con guration Record
1. Go to a Transaction record.
2. Click an existing P ay Link Co nf iguratio n or create a new one.
3. Select a Display Language .
4. Click Save.


Override a Speci c Key
If you are looking for a speci c Key you want to override but can't nd it, click the P ay Link URL eld, and swap the language in the domain with "debug". You will see the keys on a speci c PayLink, or in other words, the debugged version of the PayLink with each eld identi ed.

See the images below to see how swapping "https://dev.paylink.blackthorn.io" with "https://dev.paylink.blackthorn.io/debug/" shows the keys.


PayLink URL – Original


PayLink URL – Debug


AuthLink

Overview
Users can now send an authorization link (AuthLink) to customers to authorize the amount of a Transaction that was charged to the customer's Payment Method. This feature functions similarly to how PayLink functions, but with authorizations instead of charges.

Blackthorn supports AuthLink for Stripe, Authorize.net, and our supported Spreedly payment gateways.


Permission Set Requirement

Access to the AuthLink eld requires the Blackthorn | Payments (User) permission set.


Functionality
The A uthLink eld will be created and stored in the Transaction record after the Transaction is created.

Field Label: A uthLink
API Name: bt_paylink__AuthLink__c
Type: URL
Description: Unique AuthLink URL. *Paid add-on. Requires subscription.

The AuthLink is generated at the same time as the PayLink.

If an existing AuthLink is deleted and the record is saved, a new AuthLink will be generated.

When a user authorizes a payment via AuthLink, the Transaction’s P ay ment Status = “Authorized”.


Release Notes

Package v1.26
Released February 2024

https://login.salesforce.com/packaging/installPackage.apexp?p0=04t8W000003FY3TQAW


Enhancement
Users can now translate button labels and other static text on PayLinks. The Data Dictionary provides multilingual support, allowing Admins to establish a default language that serves as the primary language for all users. Admins can also override the default language and customize users' language experiences when speci c prede ned criteria are met.

The Transaction object now includes two new elds; the Data Dic tio nary Gro up eld and the P ay Link Display Language eld.

Field Name: Data Dic tio nary Gro up
API Name: bt_stripe__Data_Dictionary_Group__c
Data Type: Lookup(Data Dictionary Group)
Description: Select the Data Dictionary Group that contains the translated override values (Data Dictionary Entries) for the chosen Display Language.
Field Name: P ay Link Display Language
API Name: PayLink_Display_Language__c
Data Type: picklist
Description: List of supported display languages for PayLink. This eld is set to English by default.

The following logic describes how the Data Dictionary Group/Data Dictionary Entry records interact with the P ay Link Display Language eld.

PayLink labels are displayed in English, the default language, when either of the following is true.
The Transaction’s P ay Link Display Language and Data Dic tio nary Gro up elds are blank.
The Transaction’s P ay Link Display Language eld is blank, and the Data Dic tio nary Gro up does not have a Data Dictionary Entry for English.
PayLink labels use a Data Dictionary Entry’s values if the attached Transaction’s Data Dic tio nary Gro up has a Data Dictionary Entry record that uses the same language as the Transaction’s P ay Link Display Language .
PayLink labels are displayed in the selected Transaction P ay Link Display Language if a Data Dictionary Group does not include a Data Dictionary Entry record for the selected P ay Link Display Language .
PayLink labels are displayed in English if a Data Dictionary Group has a Data Dictionary Entry record with Language / Lo c ale = “English,” and the Transaction’s P ay Link Display Language eld is blank.
PayLink labels are displayed in the selected Transaction’s P ay Link Display Language when the Transaction’s Data Dic tio nary Gro up eld does not have a value.

Click here for more information about translating PayLinks.


Package v1.25
Released 12 December 2023

https://login.salesforce.com/packaging/installPackage.apexp?p0=3D04t8W000003VzX6


Enhancement
PayLink now includes a more ef cient method to reduce the number of API calls required to con rm the user license status.


Bug Fix
PayLink will display the currency based on the value in the Currency Display      eld on the Paylink Con guration record. Previously, the Currency Display        eld value did not impact how the currency was displayed.


Package v1.23
Released 22 August 2023

https://login.salesforce.com/packaging/installPackage.apexp?p0=04t8W000003Vrqf


Enhancement
Plaid users can now add a customer’s name and email to the Bank section of the PayLink form.


Bug Fixes
An error was resolved that occurred when using Authorize.net and PayLink which caused the Bank Account Type selector to appear inactive when a user tried to make an ACH payment.
After completing an ACH Transaction using a Stripe Payment Gateway via PayLink, the micro-deposit prompt will no longer be visible since Stripe waives micro-deposits.
Additional updates have been made to prevent the micro-deposit message from appearing when Stripe has waived the micro-deposit requirement, the Skip ACH Validation custom setting is enabled, and a Transaction with an ACH Payment Method is being processed via PayLink.

When a Stripe Payment Gateway that was set up with Plaid is used to complete a Transaction via PayLink, the Customer Name & Email will be captured correctly, populated on the Payment Gateway Customer record, and sent to Stripe.


Package v1.21
Released 26 May 2021

https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1I000003VrWd

Added the value "Stripe Checkout" to the eld Accepted Payment Methods on the Paylink Con guration object.


Package v1.20
Released 9 Feb 2021

https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1I000003VrLL

Updated verbiage and spacing in the PayLink Setup Wizard.


Package v1.19
Released 11 Nov 2020

https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1I000003Vqpu

Added error handling to triggers.
Updated redirect URLs.
Added dependency on Payments v5.6.


Package v1.17
Released 3 Sep 2020

https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1I000003B2fw

No code change, just modi ed the dependency on Payments to support version 4.170 and above.


Package v1.16
Released 7 Nov 2019

https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1I000003B2OA

Deprecated and deleted the Transaction__c.PayLink_Payment_Methods__c           eld.


Package v1.15
Released 4 Oct 2019

https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1I000003B2Fg

Fixed a broken link to our documentation in the PayLink setup wizard.


Package v1.14
Released 17 Sep 2019

https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1I000002yCBC

Added the ability to override the Amount Due , Due Date , and Requested By labels.


Package v1.13
Released 4 Jun 2019

https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1I000002yC9L

Added Support for Authorize.net.


Package v1.12
Released 21 May 2019

https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1I000002yBpY

Added a new eld to the PayLink Con guration called Terms and Conditions which can be used to render hyperlinked legal verbiage on the ACH checkout.


Package v1.11
Released 17 Apr 2019

https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1I000003ZGa9


Added a Next PayLink URL to the Payment Schedule object and rollup logic.


Package v1.10
Released 11 Feb 2019

https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1I000003ZGa4

Added support for Custom Settings.


Package v1.9
Released 25 Oct 2018

https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1I000003JV7h

Added Paylink Payment Method on the Transaction object.
Added a link to documentation in the Payments Setup Wizard.
Improved PayLink security.


Permission Sets

Prerequisites
The following is a list of required permissions that are NOT included in the Blackthorn Payments permission sets, BUT are required to use the Payments app.


Object                                                                                Read                     Write                     Delete                        View All               Comments


Account                                                                                ✅                        ✅                         ❌                               ❌


Contact                                                                                ✅                        ✅                         ❌                               ❌


Lead                                                                                   ✅                        ✅                         ❌                               ❌


Opportunity                                                                            ✅                        ✅                         ❌                               ❌


Opportunity Product                                                                    ✅                        ✅                         ❌                               ❌


Product                                                                                ✅                        ❌                         ❌                               ❌


Price Book Entry                                                                       ✅                        ❌                         ❌                               ❌                   A standard object that isn’t controlled by a permission set.


Content Version                                                                        ✅                        ❌                         ❌                               ❌                   A standard object that isn’t controlled by a permission set.


Content Document Link                                                                  ✅                        ❌                         ❌                               ❌                   A standard object that isn’t controlled by a permission set.


Packaged Permission Sets
There are six packaged permission sets that you can assign to users who need access to the Payments app.

All give at least Read, Create, and Edit permission to all custom objects and Read and Edit permission to all custom elds. This includes access to objects and elds for our Stripe Connect and Stripe Billing features.

The permission sets also give access to all VisualForce pages and Global Rest Apex classes. Any exceptions or additional permissions are listed below for each permission set.


Blackthorn | Payments (Admin)
The Payments Admin permission set is automatically given to Salesforce users with the System Administrator Pro le. Users with Payments Admin permissions are able to access the Payments (Admin) app, Setup Wizard, and Payment Settings tabs and perform view all, modify all, and delete records tasks for custom objects.


Blackthorn | Payments (User)
The Payments User permission set has Read permissions for Payment Gateway and Webhook Event objects and Read/Create permissions for the Blackthorn Log object. Users do not have Delete permissions on any custom objects.


Blackthorn | Payments (Manager)
The Payments Manager permission set is given to Salesforce users without a System Administrator pro le. Users with this permission set only have Read permissions for the Payment Gateway and Webhook Event objects. All other custom objects have Delete permissions.


Blackthorn | Payments (Community/Platform User)
The Payments Community/Platform User permission set is identical to the Blackthorn | Payments (User) permission set except that it does not have any of our Assigned Apps (a collection of tabs). This is because a permission set assigned to a Community user cannot have any Assigned Apps. Customers who want to give Community users access to Payments
should use this permission set.


Blackthorn | Payments (Site Guest User)
This permission set has all the permissions to create Webhook Events from Stripe. It should be assigned to the Site Guest User during the Webhook Site setup.


Blackthorn | Payments (Lite User)
The Blackthorn | Payments (Lite User) permission set has read-only access to all BT Payments objects and standard Salesforce functionality, such as reports and dashboards. Users cannot use packaged actions such as capturing Transactions, processing Refunds, etc.


Custom Permission Sets
Note: If you have custom permission sets you would like to use rather than using our Blackthorn permission sets you can view and add individual items by following the steps below:

1. Install the latest Blackthorn | Payments Salesforce AppExchange package in a sandbox.
2. Log in to the sandbox org as a System Admin.
3. Navigate to Setup -> Users -> Permission Sets.
4. Open up each individual "Blackthorn | Payments" permission set.
5. Review all permissions within each and compare them to the custom permission sets you have created. Ensure that all permissions granted by our out-of-the-box standard permission sets are recreated in your permission set.


Plaid

What is Plaid?
Plaid makes it faster and easier to set up bank payments through a ow designed with the user's experience and security in mind. Users enter their online credentials and Plaid instantly authenticates their account. Plaid works with Stripe as an ACH processor to simplify bank-to-bank payments. Read more about Plaid here.


Is your PayLink up to date?

Make sure to upgrade to the latest version of PayLink before trying to process a Plaid transaction.


Plaid Setup Prerequisites
Please have the following before you start the setup process.

A Plaid account
An activated Stripe account
For Test Payments - A Payment Gateway record with T est Mo de = "True" that is connected to the activated Stripe account
For Live Payments - A Payment Gateway record with T est Mo de = "False" that is connected to the activated Stripe account


Integrating with Plaid

Prior to Plaid Integration

Make sure your Stripe account is activated prior to Plaid integration. If you attempt to connect to Stripe through the Plaid dashboard with a test only Stripe account you will not be able to move forward until you activate the Stripe account.


1. Sign up for a Plaid account, if you haven't already done so.
2. Navigate to the "Team Settings" menu in the upper navigation bar.
3. Click Integrations.


4. Select your integration provider (i.e. Stripe).
5. Click Enable next to your provider.
6. Follow the steps for enabling the provider.
7. Once integrated you will see the label "ON" in the lower left-hand corner if the provider's icon.


8. Copy the keys listed in the "Keys" menu in your Plaid dashboard in a safe place. We will use them when we set up your Payment Gateway in Salesforce.


Add User Permissions
1. Create a new Permission Set in Setup. Name it "Access Encrypted Data."
2. Navigate to System Permissions.
3. Click Edit.
4. Set V iew Enc ry pted Data = "True" (checked).
5. Click Save.
6. Navigate to the user record in Setup for the person who authenticated the Paylink app. This is the person who clicked the Authenticate button while running the Paylink setup wizard.
7. Add the permission set you just created to their user record.


How to Setup Your Payment Gateway

Payment Gateway Setup Notes

For testing using test bank data:
Con gure your Test Mode Stripe Payment Gateway with the Sandbo x Sec ret and Client I d .
W hen ready for go live and customer use:
Make sure your live Stripe Payment Gateway record has the P ro duc tio n Sec ret and Client I d .


1. Navigate to a Payment Gateway with P ro v ider = "Stripe."
2. Add your Plaid keys to the P laid U ser I D and P laid Sec ret elds. See the table below for eld matching.
Note: Once you enable Plaid in Production you will use a different secret key. See the Plaid documentation for Production Setup.

Plaid Keys                                                                                                                                                                 Payment Gateway Fields
Client I d                                                                                                                                                              P laid U ser I D
Sandbo x Sec ret                                                                                                                                                        P laid Sec ret
P ro duc tio n Sec ret                                                                                                                                                  P laid Sec ret

3. Click Save.
4. Click Connect to Gateway to re-establish a connection with your gateway provider.


Create a Transaction
1. Navigate to the Transaction object.
2. Click New.
3. Select Rec o rd T y pe = "Charge."
4. Click Next.
5. Enter the A mo unt you would like to process through Plaid. (required)
6. Select a Currenc y I SO . (required)
7. Set a P ay ment Gateway with the Stripe gateway that is connected to Plaid.
8. Click Save.


Use PayLink to Process a Plaid Transaction
1. Navigate to the PayLink section of the Transaction record you just created.
2. Click the P ay Link URL eld.


3. Observe the PayLink page. Click Pay.


4. Click the Bank tab and click Pay $x.xx.


5. Choose your bank.


6. Enter your bank credentials. For testing, use username: user_good and password: pass_good.


7. Select a checking or savings account and click Continue.


8. If the Transaction processes successfully, you will see a success message.


Company Name on the Plaid Consent Screen
Ever wondered where Plaid gets the company name used on the consent screen? You can navigate to your Plaid dashboard and customize screens there, or you can do it in Salesforce.


Company Info Object

Make sure you have a Company Info record that stores the Co mpany I nf o Name you want to see on the Plaid consent screen.


1. Navigate to the Payment Gateway record used for Plaid.
2. Click the Pencil next to the Co mpany I nf o eld.
3. Select a Company Info record.
4. Click Save.

NOTE: You may need to add the Co mpany I nf o eld to your Payment Gateway page layout.


Why Plaid vs ACH
You can use Plaid payment methods for future Transactions.
You can eliminate the micro deposit veri cation step.
Plaid offers a direct link to your bank account without having to type in a routing number or account number.


Process Scheduled Transactions and Reattempt Logic

Scheduled Batch Job to Process Scheduled Transactions
When you complete the Setup Wizard we schedule a Blackthorn | Payments batch jobs to run nightly. You can also manually run these batch job any time you want from the Blackthorn | Payments Admin tab.

If you re a batch process to capture all the open Transactions and another batch process is already running, the second process will quietly fail. This way, protection against double-charges is implemented.


Process Scheduled Charge Transactions
There is a nightly scheduled batch job that will automatically capture the charge Transactions.

Batch Job Name: Blackthorn | Payments Daily Captures

Those Transactions have to meet the following criteria to be processed:

Auto-Process checked
A valid Payment Method
Due Date or Date To Process = Less than or equal to Today
Transaction Status = "Open"
Currency ISO
Amount

The elds below are needed for Transfer Transactions (Stripe Connect) to be automatically processed:

Auto-Process checked
A valid Connected Account
Due Date or Date To Process = Less than or equal to Today
Transaction Status = "Open"
Currency ISO
Amount


Process Scheduled Refund Transactions
There is a nightly scheduled batch job that will automatically capture the refund Transactions.

Batch Job Name: Blackthorn | Payments Daily Refunds

Those Transactions have to meet the following criteria to be processed:

Auto-Process checked
Payment Method is the same as the original Transaction
Due Date or Date To Process = Less than or equal to Today
Transaction Status = "Open"
Transactions Type = "Refund"
Amount is negative
Original Transaction (if refund) = original Transaction


Reattempt Logic
The reattempt logic allows you to automate reattempted Transactions. A new Transaction record will automatically create from the reattempt logic if the original one fails. Out-of-the-box, Blackthorn | Payments enables reattempt logic for four reattempts, one day apart.


What Payment Gateway are you using?

Reattempt logic applies to Stripe, Authorize.net, and Spreedly payment gateways.


Automated Reattempts applies to Transactions with:

A Payment Method.
Auto-Process checked
Due Date equals or is less than TODAY.
T ransac tio n Status = "Failed".

Customized your reattempt logic in custom settings.


Reattempt Logic Process
If the Transaction fails, a new Transaction is automatically generated with a T ransac tio n Status = "Open".
The new Transaction is generated in a scheduled job under Blackthorn Payments | Daily Captures. If you want to change the frequency of when these jobs process, click Manage.
Each newly generated Transaction from the failed Transaction is related. On the original failed Transaction record, you'll see all of the reattempts in a related list and a eld called Reattempt Number that auto-increases by 1 each time that original transaction is reattempted.
Based on the reattempt number, you can take action.
Our recommendation: Create a Process Builder process whereby each criterion res by an incremental Reattempt Number, such as
Reattempt #1, do nothing.
Reattempt #2, auto- re an email template to the Payment Method email address with a PayLink so the customer can update their card.
Reattempt #3, create a Task for someone internal to follow-up, etc.
The reattempt logic should function whether the Transaction was initially auto-processed or processed in real time, as determined by the setting in Blackthorn Pay - Trigger Settings.

The full use case can be found here.


Next Steps
Learn how to auto-process Transactions.
Con gure reattempt logic in custom settings.
Setup a valid Payment Method


Troubleshooting
If you have received an error with the auto-process and/or reattempt logic or have a question, please view our Troubleshooting or FAQ page. If you still have Default Payment Method questions, please contact Blackthorn Support. We're happy to help!


Recurring Charges and Subscription Options

Payment Schedules
Many payment gateways offer “subscriptions”, such as PayPal or Braintree, but these are just recurring charges. Blackthorn Payments has this same concept with Payment Schedules.

Think of a gym membership. Every month, you’re charged $80 and you get an email. There is not a multi-line invoice generated, there’s no proration calculation, there typically is no upgrade or downgrade logic, etc. The recurring charge is often just canceled and a new schedule is started at the beginning of the next month.


Stripe Billing Subscriptions
True subscriptions generate invoices with multiple line items every billing cycle. Stripe Billing provides this functionality, which is also part of Blackthorn Payments. Other options include Chargify, Chargebee, Zuora, and Recurly. These systems allow for upgrade, downgrade, pause, and proration scenarios, with automatically calculated prices.

Blackthorn Payments supports both use cases. For the simpler one, use our Payment Schedules. For the more comprehensive one, use our support for Stripe Billing.


Reports

Introduction
Basic reports are included in the app as a template to give you a sense of what elds can be ltered on and what type of metrics you can yield. We recommend starting with these Reports and editing them to reach your desired metrics.

Navigate to Reports.

Lightning: Click on the app launcher | Under "All Items" | Click on Reports.

Classic: Click on "All Tabs" ("+" icon in the top right) | Click on Reports.

In the left-hand column, click on the "Blackthorn | Payments Reports" folder.


Out of the Box Reports
The below Reports are all accessible when installing Blackthorn | Payments.


Transactions to x: All Transactions that need to be xed and have an "Open" status.
Completed and failed Transactions: All completed and failed Transactions by month.
Historical gross revenue: All successful Transactions.
Reconciliation and Payouts: All payouts with their related charges and refunds.
Revenue forecast by month: "Open" status Transaction by monthly due date. coming soon
Transactions to be reattempted: Transactions that have been created with reattempt logic.
Transactions failed today: Transactions that failed to capture today.
Transactions due in the next 7 days: Transactions with "Open" status and Due Date within 7 days.
Transactions completed today: Transactions that were "Completed" and "Captured" today.
Transactions completed this month: Transactions that were "Completed" and "Captured" this month.


Next Steps
Use our "out of the box" Dashboard to see your Report data in a variety of displayed components.


Troubleshooting
If you have received an error with our Reports or have a question, please view our Troubleshooting or FAQ page. If you still have Default Payment Method questions, please contact Blackthorn Support. We're happy to help!


Salesforce Shield / Platform Encryption with all Blackthorn apps

Overview
If your Salesforce org has implemented data security with Shield Platform Encryption, here's how you can set this up and prevent running into any errors while using our Blackthorn apps.

Salesforce Shield and Blackthorn's apps work with Salesforce Shield aka Platform Encryption enabled. It works with Deterministic based encryption. This must be done in three places. The key, the global option, and per- eld.


Setup

Step 0
The running user of each app, typically the person who installed both apps, must have a pro le that can view encrypted elds. Alternatively, you can use a dedicated integration user that no one has access to with this pro le to query and create records with the necessary elds.


If you're a system admin and don't have "View Encrypted Data" access on pro le, you can create a custom permission set to include the access and assign it to your users. See required user permissions for shield platform encryption here.


To con gure this, navigate to Setup, type 'plat' to nd the below (short for platform). The red arrows highlight where you'll need to click to get to the con guration areas below:


Classic navigation


Lightning Navigation


Step 1
1. Visit Setup | Platform Encryption | Key Management.
2. Select 'Data in Salesforce (Deterministic)' and generate your key.


Step 2
1. Visit Setup | Platform Encryption | Advanced Settings.
2. Enable 'Deterministic Encryption'.


Step 3
1. Setup | Platform Encryption | Encryption Policy then click 'Encrypt Fields'.
2. For the Email eld (or any other erroring eld you get when enabling Shield and/or installing our apps, whichever comes rst, set those elds to Deterministic - Case Insensitive.


To know more about how Shield Platform Encryption Works, see here.


Suggested Con guration for Blackthorn Fields

The tables below will provide a list of elds from our applications that should NOT be encrypted using Salesforce Shield.
These elds are used to lter the SOQL result and so they should be excluded from the encryption in order for our apps to work.
Formula & Reference elds cannot be encrypted.
After marking all elds for encryption if historical data is present you will need to export and import records to trigger a full encryption of data at rest or log a case with Salesforce Support to have a back end encryption job processed. As of Spring '19 you can now also perform this encryption sync yourself using the self service option in the
Salesforce help portal.
Picklist elds can not be encrypted.
Blackthorn will maintain the list whenever a new eld is added to the apps.


Payments
Object Name                                                                                                     Field Name                                                                                 Object Type                                                              Encryption Type
Contact                                                                                                    Email                                                                                                               Standard                                                          No Encryption
Product2                                                                                                   Product_ID__c                                                                                                       Standard                                                          No Encryption
Transaction__c                                                                                             Transaction_Id__c                                                                                                   Custom                                                            No Encryption
Transaction__c                                                                                             Transfer_Payment_Id__c                                                                                              Custom                                                            No Encryption
Transaction__c                                                                                             Key__c                                                                                                              Custom                                                            No Encryption
Payment_Intent__c                                                                                          Payment_Intent_Id__c                                                                                                Custom                                                            No Encryption
Payment_Method__c                                                                                          Card_Id__c                                                                                                          Custom                                                            No Encryption
Payment_Method__c                                                                                          ACH_Key__c                                                                                                          Custom                                                            No Encryption
Payment_Method__c                                                                                          Fingerprint__c                                                                                                      Custom                                                            No Encryption
Payment_Gateway__c                                                                                         Webhook_Label__c                                                                                                    Custom                                                            No Encryption
Payment_Gateway__c                                                                                         Stripe_User_Id__c                                                                                                   Custom                                                            No Encryption
Plan2__c                                                                                                   Plan_Id__c                                                                                                          Custom                                                            No Encryption
Coupon2__c                                                                                                 Coupon_Id__c                                                                                                        Custom                                                            No Encryption
Dispute__c                                                                                                 Dispute_ID__c                                                                                                       Custom                                                            No Encryption
Stripe_Customer__c                                                                                         Email__c                                                                                                            Custom                                                            No Encryption
Stripe_Customer__c                                                                                         Customer_Id__c                                                                                                      Custom                                                            No Encryption


Events
Object Name                                                                                                    Field Name                                                                               Object Type                                                               Encryption Type
Account                                                                                                      Name                                                                                                            Standard                                                           No Encryption
Attendee__c                                                                                                  Registration_Status__c                                                                                          Custom                                                             Deterministic
Attendee__c                                                                                                  Email2__c                                                                                                       Custom                                                             Deterministic
Attendee__c                                                                                                  Key2__c                                                                                                         Custom                                                             Deterministic
Attendee__c                                                                                                  Email__c                                                                                                        Custom                                                             Deterministic
Attendee__c                                                                                                  Attendence_Status__c                                                                                            Custom                                                             Deterministic
Email_Template__c                                                                                            SF_Template_Id__c                                                                                               Custom                                                             Deterministic
Email_Template__c                                                                                            Name                                                                                                            Custom                                                             No Encryption
Event_Group__c                                                                                               Name                                                                                                            Custom                                                             No Encryption
Event__c                                                                                                     Name                                                                                                            Custom                                                             No Encryption
Event__c                                                                                                     Event_Start_Date__c                                                                                             Custom                                                             No Encryption
Event__c                                                                                                     Key2__c                                                                                                         Custom                                                             Deterministic
Contact                                                                                                      Name                                                                                                            Standard                                                           No Encryption
Event_Item__c                                                                                                Item_Name__c                                                                                                    Custom                                                             No Encryption
Event_Noti cation__c                                                                                         Title__c                                                                                                        Custom                                                             No Encryption
Form_Element__c                                                                                              Maps_To_Object__c                                                                                               Custom                                                             Deterministic
Form_Element__c                                                                                              Question__c                                                                                                     Custom                                                             No Encryption
Form_Submission__c                                                                                           Key__c                                                                                                          Custom                                                             No Encryption
Lead                                                                                                         Name                                                                                                            Standard                                                           No Encryption
Session__c                                                                                                   Start_Date__c                                                                                                   Custom                                                             No Encryption
Speaker__c                                                                                                   Last_Name__c                                                                                                    Custom                                                             No Encryption
Speaker__c                                                                                                   First_Name__c                                                                                                   Custom                                                             No Encryption
Sponsor__c                                                                                                   Tier__c                                                                                                         Custom                                                             No Encryption
Sponsor__c                                                                                                   Display_Name__c                                                                                                 Custom                                                             No Encryption
Track__c                                                                                                     Name                                                                                                            Custom                                                             No Encryption
Event_Setting__c                                                                                             Name                                                                                                            Custom                                                             No Encryption
Payment_Gateway__c                                                                                           Name                                                                                                            Custom                                                             No Encryption
Form__c                                                                                                      Name                                                                                                            Custom                                                             No Encryption
Campaign                                                                                                     Name                                                                                                            Custom                                                             No Encryption


For any elds that are lookups the reference object Name eld cannot be used to encrypt.
This is not supported in Event Wizard.
If you are not planning to add these elds in the Event Wizard eldset, the elds can be encrypted. The type should be Deterministic.


SCA and MOTO
Strong Customer Authentication and Mobile Orders/Telephone Orders

Strong Customer Authentication (SCA), as part of PSD2 regulation in Europe, requires changes to how European customers authenticate online Stripe payments. Card payments require a different process, namely 3D Secure, in order to meet SCA requirements. We've updated Payments to prevent Transactions from being declined by banks. Read more here.


Who is Affected?
The new requirements for SCA affect our customers in Europe who use Stripe as that is where the PSD2 regulation is being implemented. Read more here.


Scope

Recommended
Blackthorn Payments supports the following features.

Capturing a Transaction through PayLink with SCA regulated Payment Methods.
Capturing a Transaction through Donations with SCA regulated Payment Methods.


Not Recommended
Capturing SCA regulated Payment Methods and Transactions through the Virtual Terminal.
Capturing SCA regulated Payment Methods through the Transaction object.

These options require additional con guration and must be agged as MOTO (mail orders & telephone orders) when sent to Stripe from the Virtual Terminal since the card is not present for authentication. MOTO puts a Transaction out of the scope of SCA.

When SCA is applied, the business will bene t from a “liability shift” in their Transactions. This means that should fraud occur, the bank (as opposed to the company) will be liable to cover the costs as the bank authorized the Transaction.

Putting SCA exemptions in place returns the “liability shift” to the company. Therefore, a company needs to weigh the pros and cons of the liability shift before adding an exemption.

This is why Stripe uses the MOTO parameter via API feature agged, and it isn’t available by default. Blackthorn only applies MOTO to Virtual Terminal and auto-processed Transactions, as these types are out of scope for SCA.

Please watch the below videos for instructions on how to enable SCA and MOTO.


SCA


Are you using SCA with Events?

To successfully use SCA with Events, you must use Stripe Checkout as SCA is only supported by Stripe. (SCA is not supported by Authorize.net or Spreedly.)


MOTO


How to Enable SCA
To enable SCA in your org, complete the following steps.

1. Click the Gear icon.
2. Click Setup.
3. In the Quick Find box, enter and click "Custom Settings."
4. Click Manage next to Blackthorn Pay - Trigger Settings.
5. Click Edit.
6. Set Enable SCA = "True" (checked).


7. Click Save.

If you haven't done so already, set up Stripe Checkout. To support the SCA ow, Stripe Checkout must be used with Events. Click here to learn how to set up Stripe Checkout. (SCA support is only available through Stripe.)


Payment Gateway Con guration for MOTO
Before using MOTO to create and capture payments from the Virtual Terminal, you must add the Stripe MOT O Enabled eld to the Payment Gateway record page layout.

When Stripe MOT O Enabled = "True" (checked), the MOTO ag will be set on Stripe charge requests. In other words, your Transactions will succeed when using a Payment Method that doesn't require additional authentication.


Payment Method Con guration for MOTO
If you need to create new Payment Methods from the Payment Method object and capture Transactions from the Transaction object, you must add the Enable MOT O eld to the Payment Method's Charge Card page layout.

When Enable MOT O = "True" (checked), the MOTO ag will be set on Stripe charge requests so that Transactions can be captured without going through two-factor authentication.


Contact Stripe to Con gure Your Stripe Account
To charge a newly created SCA regulated credit card number in the Virtual Terminal and Transaction object, you must contact Stripe support to have your Stripe account con gured for MOTO.

1. Reach out to Stripe Support to get your Stripe Account “Gated” for MOTO.Navigation: Stripe Support Site from Help Menu > Click Contact Support > This will initiate a chat with support.
2. Stripe will ask you why you need this. Tell them that you need to take over the phone payments through the API with the Blackthorn App.
3. Make sure Stripe Support gates MOTO for your account in Test and Live mode.


Testing SCA for PayLink
Use the following test card to prompt for additional authentication -> 4000002500003155

Other regulatory (3D Secure) test cards can be found here.

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


What Errors Will I See if My Stripe Account Has Not Been Setup for MOTO Payments?
If your Stripe account has not been gated for MOTO by the Stripe support team you will notice that your Transactions will fail when you try to capture a charge from the Transaction object or the Virtual Terminal for new SCA regulated Payment Methods.

W hat Does This Look Like?

When capturing a charge from the Transaction object and MOTO is not gated on the Stripe Account:


When a capturing a charge from the Virtual Terminal and MOTO is not gated on the Stripe account:


Failure message from Virtual Terminal


Error message on the Transaction record that was created from the Virtual Terminal


What Does the Additional Authentication Step Look Like?
When using features like PayLink, the ow of the UI has an additional step. This step supports the additional authentication process.

In live mode, customers will navigate to the PayLink as they've done in the past. After clicking PAY customers will be asked to verify their identity with a push noti cation, a text message, or another method chosen by their bank. Read more here.


What About Existing Payment Methods?
Existing Payment Methods that are saved in your orgs should continue to work with the new SCA regulations. Also, Payment Methods that do not require the additional authentication step will continue working as expected.


How Will SCA affect Stripe Billing?
If you need to enable SCA in your Salesforce org, existing Payment Methods used with your Stripe Billing records will continue working as expected.

If you set up a new Subscription through Salesforce and it requires a new Payment Method, you must authorize the Payment Method before the Stripe Subscription will appear as "Active" in the Stripe dashboard.


How Do I Make Sure My Card Is Authorized?
Use an existing, valid Payment Method.
Create a Payment Method in the Virtual Terminal.
Create a Payment Method through the New Payment Method button on a Contact/Account record.


How Can I Use the Stripe Dashboard to Authorize a Payment Method


If you create a new Subscription in Salesforce that requires a new Payment Method and push it Stripe, you will see that the Subscription shows as incomplete. This is because the Payment Method still needs to be authorized.

Complete the authorization step in Stripe.

1. Navigate to the Subscription in Stripe.
2. Click on the "Open" Invoice associated with the Subscription record.
3. In the Details section of the Invoice in Stripe, click the link next to "Payment Page."
4. Complete the authorization process and capture the payment.


Frequently Asked Questions
Q: W ill existing, valid credit card Payment Methods still work after SCA is enabled?

Yes! Valid credit card Payment Methods will continue to work as expected after you enable SCA.

Q: W ill existing, valid ACH Payment Methods still work after SCA is enabled?

Yes! New and existing ACH Payment Methods will continue to work as expected after you enable SCA.

Q: If SCA is enabled and I use Plaid with Stripe, will I encounter any issues?

No, with SCA Enabled you can still continue to use Plaid without issue or interruption.

Q: If I enable SCA and use Events and PayLink, will there be any issues with Event registration?

To successfully use SCA with Events, you must use Stripe Checkout as SCA is only supported by Stripe. (SCA is not supported by Authorize.net or Spreedly.)

Q: If I enable SCA and use DocumentLink and PayLink, there will there be any issues with DocumentLink?

No, DocumentLink will continue to work without issue after SCA is enabled for cards NOT requiring authentication. SCA-ready support for DocumentLink is on our product roadmap.

Q: W ith SCA enabled, can I can use PayLink and Donations checkout and the Payment Method can be used for future recurring payments (without having to re-verify)?

Yes! Once the Card has been authenticated through the PayLink or Donations checkout, that Payment Method can be used for future or recurring payments without additional authentication.

Q: W ith SCA enabled, can I create ACH Payment Methods through PayLink or Donations and reuse them in the future?

Yes! ACH Payment Methods are not affected by SCA regulations.

Q: W ith the Virtual Terminal, can I capture payments the same way before SCA was enabled?

Yes, but with some additional setup. Please see the additional setup needed here.


Scheduled Batch Jobs

Change to Schedule Recommended Payment Jobs

For existing users, clicking Schedule Recommend Payment Jobs will no longer trigger the “Blackthorn | Payments Transaction Rollup To Parent” scheduled job. Instead, you will need to click the Schedule Transaction Rollup to Parent Job button.


Jobs can be scheduled to run together in a batch or run manually on their own. To manually trigger a job, go to the Batch Jobs or Scheduled Jobs tab from the Blackthorn | Payments Admin tab and click the relevant button.

Jobs that have been scheduled can be seen by going to Setup > Jobs > Scheduled Jobs. All job names start with Blackthorn | Payments.


The following is a list of batch jobs we schedule once you complete the Setup Wizard and click the Schedule Recommended Payment Jobs button on the Scheduled Jobs tab.


Which time zone does the process use when running a scheduled job?
Per the Salesforce Apex guide, "The `System.schedule` method uses the user's timezone for the basis of all schedules."


Blackthorn | Payments Balance Update

Runs nightly at 2:00 am.
Updates any available and pending Stripe balances for all Payment Gateways and Connect accounts.
The Update Balances button is located on the Blackthorn | Payments Admin’s Batch Jobs tab.


Blackthorn | Payments Billing Balance Rollup

Runs nightly at 4:00 am.
Updates balances on Invoices (Blackthorn Invoices and Stripe Invoices) from related and captured Transactions.


Blackthorn | Payments Daily Captures

Runs nightly at 12:00 am.
Processes scheduled charge Transactions with Due Date = “TODAY”.
The Process Scheduled Charge Transactions Now button is located on the Blackthorn | Payments Admin’s Batch Jobs tab.


Blackthorn | Payments Daily Captures (Authorized)

Runs nightly at 12:00 am.
Processes scheduled authorized Transactions with Due Date = “TODAY”.
The Process Scheduled Charge Transactions Now button is located on the Blackthorn | Payments Admin’s Batch Jobs tab.


Blackthorn | Payments Daily Refunds

Runs nightly at 2:00 am.
Processes scheduled refund Transactions with Due Date = “TODAY”.
The Process Scheduled Refund Transactions Now
button is located on the Blackthorn | Payments Admin’s Batch Jobs tab.


Blackthorn | Payments Log Record Cleanup

Runs nightly at 12:00 am.
Deletes any Blackthorn Log records that were created 30+ days ago.
If you have a large number of Blackthorn Log records to delete immediately, execute the following code in the Salesforce Developer Console. It will delete everything except for records created within the last ve days. However, since this job deletes only 10,000 records at a time, you may need to execute the code multiple times.


Plaintext                                                                                                                                                                                                                                                                                                                                          Copy

Integer daysToKeep = 5;
bt_stripe.BlackthornLogService.deleteOldBlackthornLogRecords(daysToKeep);


Blackthorn | Payments Query Number Managed Package Users

Finds the number of Payments and Events users based on permission set assignments and then updates the LMO.


Blackthorn | Payments Set Payout

Runs nightly at 4:00 am.
Connects completed Payout records with related Charge and Transfer (Stripe Connect) records.
The Process Payment Balance History button is located on the Blackthorn | Payments Admin’s Batch Jobs tab.


Blackthorn | Payments Webhook Record Cleanup

Runs nightly at 12:00 am.
Deletes successfully processed Webhook Event records.


Blackthorn | Payments Webhook Record Processing @ 0

Runs at the top of each hour (12:00, 1:00, 2:00, etc.) and schedules a new job to run ve minutes after the last batch run nishes.
Processes Webhook Event records.


Blackthorn | Payments Transaction Rollup To Parent

Runs every 30 minutes.
Updates a Transaction’s parent records with the (child) Transaction's summary. This includes Payouts, Captures, Transfers, Refunds, and the Total elds on the parent record.
The Schedule Transaction Rollup To Parent Job button is located on the Blackthorn | Payments Admin's Scheduled Jobs' tab.


For new installations, the following changes were made to the “Blackthorn | Payments Transaction Rollup To Parent” scheduled job.

After installing Payments, the "Blackthorn | Payments Transaction Rollup To Parent" scheduled job will no longer be automatically scheduled.
To opt-in to the “Blackthorn | Payments Transaction Rollup To Parent” scheduled job, the Payments Admin will need to go to the Blackthorn | Payments Admin page and click the Schedule Transaction Rollup to Parent Job button.
If Disable T rans Ro llup to P arent is set to “True” in Blackthorn Pay - Trigger Settings and “Blackthorn | Payments Transaction Rollup To Parent” is scheduled, then real-time rollups do NOT run, but the scheduled batch job DOES run every hour to process rollups.

NOTE: For existing users, clicking Schedule Recommend Payment Jobs will no longer trigger the “Blackthorn | Payments Transaction Rollup To Parent” scheduled job. You will need to click the new Schedule Transaction Rollup to Parent Job button.


The following batch jobs will be schedule if Blackthorn Pay - Features custom setting has the Billing Valid Through with a future date. (Stripe Billing batches)


Blackthorn | Payments Send Stripe Invoices

Runs daily at 6:00 am.
Sends an Invoice to a customer when Send I nv o ic e On Date = "TODAY".


Blackthorn | Payments Past Due Invoices

Runs daily at 5:00 am.
Updates the Invoice P ay ment Status = "Past Due" when the Due Date < Today and P ay ment Status = "Unpaid".
The Update Invoices button is located on the Blackthorn | Payments Admin’s Batch Jobs tab.


Blackthorn | Payments Daily Captures – High Volume

Schedules the Transaction auto-charge batches using the batch size of 75.
Click the Schedule High Volume Transaction Job button on the Blackthorn | Payments Admin page’s Scheduled Job tab.
The Schedule High Volume Transaction Job button is available when the auto charge batch size exceeds 1.
The Schedule Billing Jobs button is visible when Stripe Billing is enabled through a future date.
The Schedule High Volume Transaction Job button is hidden when the batch size resets to 1.
When the Schedule High Volume Transaction Job button is clicked, the Blackthorn | Payments Daily Captures - High Volume scheduled job will replace the Blackthorn | Payments Daily Captures job and will run at midnight.


How do I change the scheduled job/apex job user?

Before making any changes, please ensure that the person scheduling the jobs has Admin (Blackthorn | Payments (Admin)) access to Payments. The steps below will delete the current scheduled jobs and user and reschedule the jobs to run under the user who clicks the button.

1. Go to the Blackthorn | Payments Admin tab.
2. Click the Scheduled Jobs tab.
3. Click Schedule Recommended Payment Jobs.


Spreedly

Action Required for Spreedly Gateways when you upgrade to Payments version 6.48

As part of Salesforce’s security requirements and to better protect your sensitive data, all Spreedly keys, including the Spreedly Payment Gateway access token and the Payment Intent Client Sec ret eld must now be encrypted. Starting with version 6.48, customers with existing Spreedly gateways must manually reconnect those gateways in the
Dashboard after upgrading.

W hat does reconnecting mean? Reconnecting requires you to open each existing Spreedly gateway and click Create Spreedly Gateway. This process encrypts your Spreedly key.

W hat happens if you don’t reconnect after upgrading to a new version? Until each Spreedly gateway is reconnected, all Transactions routed through that gateway will fail — meaning no payments will process for that gateway.


Spreedly is a service that allows you to securely store credit cards and use them to perform transactions for a number of PaymentGateways and third-party APIs. It does this by simultaneously providing a card tokenization/vault service as well as a gateway and receiver integration service. PaymentMethods tokenized by Spreedly are stored at Spreedly, allowing you
to independently store a card and then pass that card to different endpoints based on your business requirements. We refer to the ability to use a Spreedly token against multiple gateways/end points as “universal tokenization.”

To read more about Spreedly, click here.


Spreedly Payment Gateways

Supported and Fully Tested
Cybersource via Spreedly


Used by Blackthorn Customers, but Not Fully Tested
Braintree
Cardconnect
Elavon
eWAY
Fat Zebra
Litle
Orbital
Pay ow Pro
Paypal
Sage


Not Supported
Worldline


Set Up the Payment Gateway Page Layout

Payment Gateway Customer Record Update
Since Spreedly does not have an equivalent record (e.g., user id) for customers, a Payment Gateway Customer record will not be created in Salesforce.


1. Click the Gear icon in the upper right-hand corner.
2. Click Setup.
3. Click the Object Manager tab.
4. Locate the Payment Gateway object.
5. Click the Field & Relationships tab.
6. Locate the P ro v ider eld.
7. In the Values section, click New.
8. Enter “Spreedly” and click Save.
9. Click the Page Layouts tab.
10. Click Payment Gateway Layout.
11. Add the following elds to your Payment Gateway page layout:
Spreedly Env iro nment Key
Spreedly Co nf igured Gateway
Gateway T o k en
Spreedly P riv ate Key (use with iframed components)
Spreedly Certif ic ate T o k en (use with iframed components)
12. Click on the Buttons section.
13. Drag and drop the Create Spreedly Gateway button to the Custom Buttons section.
14. Click on the Mobile & Lightning Actions section.
15. Drag and drop the Create Spreedly Gateway button to the Salesforce Mobile and Lightning Experience Actions section.
16. Click Save.


Spreedly and Iframed Components
Spreedly has updated its authentication requirements for iframes, resulting in changes to the Events app’s iframe checkout process.

The following changes ensure the Events webapp correctly passes newly required values to the Spreedly gateway when Event registrations occur via an iframe.

Complete the following steps to enable the new authentication method.


Update Spreedly Con guration

1. Navigate to Environment Settings in the Spreedly dashboard.
2. Enable the checkbox "Enable Secure Tokenization."
3. Select the option "iFrame or Spreedly Express."


Blackthorn Con guration
Con rm that the following elds are on the Payment Gateway page layout you use for your Spreedly gateway.

Spreedly Env iro nment Key (bt_stripe__Spreedly_Environment_Key__c)
This eld stores the environment key that is included in your API credentials. Spreedly auto-generates the key and uses it to reference the environment that organizes your payment data.
Spreedly Co nf igured Gateway (bt_stripe__Spreedly_Con gured_Gateway__c)
This eld stores the Payment Gateway that was created with Spreedly.
Spreedly Certif ic ate T o k en (bt_stripe__Spreedly_Certi cate_Token__c)
This eld stores the Spreedly certi cate token used for payment gateway routing. Spreedly auto-generates it and uses it to reference the stored certi cate securely. Known in Spreedly as certi cateToken, it is a public identi er for your key pair and helps Spreedly verify that the signature was generated with your private key. (This can be used in the
frontend.)
Spreedly P riv ate Key (bt_stripe__Spreedly_Private_Key__c)
This eld stores the PEM-formatted private key used for SSL client certi cate authentication with Spreedly. Known as PRIVATE_KEY in Spreedly, the key is used to digitally sign a message so Spreedly can verify the message is coming from your system. (This should be only used on the backend of the Events webapp and PayLink.)


Permission Sets
Users with the Blackthorn | Payments (Admin) permission set have Read/Edit access. All other permission sets except Blackthorn | Payments (Stripe Billing), which has no access, have Read access.

Additional information about these elds is on the Spreedly dashboard.


Set Up Braintree**
Complete the following steps to set up Braintree.

1. Gather the following details from your Braintree account.
Merchant Account Id
Merchant Id
Public Key
Private Key
2. After logging in to Braintree, go to Settings.
The Merchant Account Id and Merchant Id can be found on the Business Tab, under Merchant Accounts.
The Public Key and Private Key are on the API tab under Keys.
3. On the Spreedly gateway record, click the Create Spreedly Gateway button.
4. Select Braintree from the list of gateways.
5. Change the Auth Mode to Blue.
6. Enter the details gathered above into the matching elds.

**Braintree is used by some Blackthorn customers, but Blackthorn does not of cially support Braintree. Use at your own risk.


Virtual Terminal Custom Setting
Before using Spreedly with Cybersource to accept payments, the Virtual Terminal custom setting Sho w A ddress must be enabled. This ensures that the address elds (Street , City , State , and Co untry / Regio n ) will be visible on the Payment Method creation page in the Virtual Terminal.


Add A Spreedly Payment Gateway
NOTE: When setting up a Payment Gateway using Spreedly, you cannot add Authorize.net and Stripe as a gateway. Authorize.net and Stripe function as stand-alone Payment Gateways.


1. Contact Blackthorn Support to obtain a Spreedly Environment Key.
2. Navigate to the Payment Gateway object.
3. Click New.
4. Enter a P ay ment Gateway Name .
5. Set P ro v ider = “Spreedly”.
6. Check the T est Mo de checkbox if you are setting this up in your sandbox for testing. Do not check the box if this is a Live Payment Gateway in production.
7. Populate the Def ault Currenc y and Def ault Co untry      elds.
8. Enter the key provided by Blackthorn Support in the Spreedly Env iro nment Key       eld.


9. Click Save.
10. Click the Create Spreedly Gateway button.
11. Select the Payment Gateway you want to connect (Ex. CardConnect; EBANX). For test mode, select "Spreedly Test".
12. If prompted, add additional information from the selected gateway.
13. Click Create.
14. The Spreedly Co nf igured Gateway and Gateway T o k en elds will be populated automatically.


Add a CyberSource Payment Gateway
1. Contact Blackthorn Support to obtain a Spreedly Environment Key.
2. Navigate to the Payment Gateway object.
3. Click New.
4. Enter a P ay ment Gateway Name .
5. Set P ro v ider = “Spreedly”.
6. Leave the T est Mo de checkbox blank. Only check if you are setting this up in your sandbox for testing.
7. Populate the Def ault Currenc y and Def ault Co untry      elds.
8. Enter the key provided by Blackthorn Support in the Spreedly Env iro nment Key       eld.


9. Click Save.
10. Click the Create Spreedly Gateway button.
11. Select the CyberSource Payment Gateway.
12. Enter the Transaction Key and Username.
Use the SOAP toolkit key you created in Cybersource as the Transaction Key.
Use the Merchant ID from CyberSource as the Username. (Where do I nd the Merchant ID?)
13. Click Create.
14. The Spreedly Co nf igured Gateway and Gateway T o k en elds will be populated automatically.


Test Spreedly
Test your Payment Gateway using either the test Spreedly card or the test Spreedly ACH bank account.


Test a Spreedly Card

Warning
Real card and bank account information cannot be used in Test Mode.


1. Con rm that the Payment Gateway has T est Mo de set to “TRUE”.


2. Go to the Payment Method tab and click New.
3. Select Card and click Next.


4. Using the information provided below, complete the following elds.
Ho lder’s Name = use any name
Number = “4111111111111111”
Ex piratio n Mo nth = use any month
Ex piratio n Y ear = use any year
CV V = use any 3-digit number
P o stal Co de = use any 5-digit number
P ay ment Gateway = use the Payment Gateway you just set up
5. Click Save.


This Payment Method is now valid and can be used to capture and refund Transactions.

For more information about testing Spreedly Payment Gateways, click here.


Spreedly and ACH Bank Account Limitation

Blackthorn does not support webhook callbacks for gateways that are con gured through Spreedly. As a result, Blackthorn does not recommend submitting ACH payments via Spreedly.

If an ACH payment is submitted via Spreedly, users must check their gateway to see if the payment is complete. Users cannot con rm if the payment was successful by going to Salesforce.

If you do use ACH payments with Spreedly, please proceed with caution.


Test a Spreedly ACH Bank Account

Warning
Real card and bank account information cannot be used in Test Mode.


1. Con rm that the Payment Gateway has T est Mo de set to “TRUE”.


2. Go to the Payment Method tab and click New.
3. Select A CH and click Next.


4. Using the information provided below, complete the following elds.
Ho lder’s Name = use any name
A c c o unt Number = “9876543210”
Ro uting Number = “021000021”
A c c o unt Ho lder T y pe = either option
Currenc y I SO = “USD”
Co untry I SO = “US”
5. Click Save.

This Payment Method is now valid and can be used to capture and refund Transactions.

For more information about testing Spreedly Payment Gateways, click here.


Default Payment Method Limitation

The default logic related to Payment Methods, which is offered as part of our Integrations to Stipe and Authorize.net, is not supported for Spreedly since Spreedly doesn’t have an equivalent record to the Payment Gateway Customer object. Customers can create matching logic with automation to work around this limitation.


Create Credit Card Payment Methods

LIMITATION

If you create a new Payment Method for a Spreedly gateway by clicking the New button on the Payment Method List view, the new Payment Method will be saved, but the P ay ment Metho d Status will not be updated to “Valid” or “Invalid.”


From the Payment Method Object
1. Navigate to the Payment Method object.
2. Click New.
3. Set Rec o rd T y pe = "Card"
4. Fill in the following elds.
a. Ho lder's Name
b. A c c o unt Ho lder T y pe
c. Currenc y I SO
d. Co untry I SO
5. Set P ay ment Gateway = “Spreedly”.
6. Click Save.


From the Virtual Terminal
1. Navigate to an object or record where you can access the Virtual Terminal (Opportunity, Invoice, etc..)
2. Set A c tio n = "New Payment Method".
3. Set P ay ment Gateway = “Spreedly”.
4. Click the CREDIT CARD tab.
5. Fill in the following elds.
a. Name o n c ard
b. Card number
c. Card Ex piratio n
d. CV C
e. P o stal c o de
6. Click Add +.


Create ACH Payment Methods

Spreedly and ACH Bank Account Limitation

Blackthorn does not support webhook callbacks for gateways that are con gured through Spreedly. As a result, Blackthorn does not recommend submitting ACH payments via Spreedly.

If an ACH payment is submitted via Spreedly, users must check their gateway to see if the payment is complete. Users cannot con rm if the payment was successful by going to Salesforce.

If you do use ACH payments with Spreedly, please proceed with caution.


From the Payment Method Object
1. Navigate to the Payment Method object.
2. Click New.
3. Set Rec o rd T y pe = "ACH".
4. Fill in the following elds.
a. Ho lder's Name
b. A c c o unt Ho lder T y pe
c. Currenc y I SO
d. Co untry I SO
5. Set P ay ment Gateway = “Spreedly”.
6. Click Save.


From the Virtual Terminal
1. Navigate to an object or record where you can access the Virtual Terminal (Opportunity, Invoice, etc..)
2. Set A c tio n = "New Payment Method".
3. Set P ay ment Gateway = “Spreedly”.
4. Click the BANK tab.
5. Fill in the following elds.
6. Name o n ac c o unt
7. A c c o unt ho lder ty pe
8. Ro uting Number
9. A c c o unt number
10. Click Add +.


Process a Payment
NOTE: Blackthorn Payments does not support using DocumentLink to make a payment with a Spreedly Payment Gateway.


From the Transaction Object
1. Navigate to the Transaction object.
2. Click New to create a new record.
3. Select the "Charge" for the Rec o rd T y pe .
4. Enter the amount in the A mo unt eld.
5. Select your P ay ment Gateway .
6. Select the P ay ment Metho d .
7. Click Save.
8. Click Capture to charge the Transaction..


From Virtual Terminal
1. Navigate to an object or record where you can access the Virtual Terminal (Opportunity, Invoice, etc..)
2. Set A c tio n = "New Single Charge".
3. Set P ay ment Gateway = “Spreedly”.
4. Fill in the following elds.
a. Related T o
b. P ay ment Metho d
c. A mo unt
d. Currenc y
e. P ro c ess T y pe
5. Click Process.


FAQ

How do eChecks work with Spreedly?
Customers can create ACH Payment Methods with Spreedly that can be used with a gateway's eCheck service. See more details about the eCheck gateways that Spreedly supports here.

When using eChecks, with the exception of an offsite gateway like PayPal, the response for eChecks will always be successful on Spreedly's end. Otherwise, the noti cation will happen outside of Spreedly. If a Transaction fails, the gateway user will be noti ed, and they will need to update the Transaction in Salesforce.


What is the fee per transaction when using PayPal as a payment gateway?
The fee per transaction when using PayPal as a payment gateway is 3.49% + a at fee depending on the country. The at fee for the USA is 0.49 USD (standard rate).


Stripe

Introduction
Stripe is "A suite of APIs that powers commerce for businesses of all sizes." Stripe is not to be confused with Square, the in-person point-of-sale solution, rather Stripe is purpose-built for back-end payment processing.


Pricing
Stripe's pricing is a simple at fee of 2.9% per transaction plus 30 cents (USD). The rate changes based on your home country. Better rates are available if you process over $80k/month. Contact us if you'd like an intro to our Stripe partner manager to discuss rates.

If you're a 501(c)(3), email sales+nonpro t@stripe.com and include your Employer Identi cation Number (EIN) to receive a discounted Transaction fee.

If you capture ACH payments, the fee is 0.8% capped at $5.00 (USD).


Change your home country at the bottom of Stripe's page.


Available Currencies
Blackthorn Payments and Stripe supports processing payments in 135+ currencies. View the full list.


Sign up for Stripe
If you need to create an account with Stripe, this can be completed in the quick start process. Sign-up takes minutes to complete and then you can begin taking payments. The rst payout to your bank account takes a week, but each payout after that is 1-2 days.


New Stripe Account
1. Navigate to the Blackthorn | Payments Setup Wizard.
Lightning: Navigate to app launcher > select "Payments (Admin)" app > click the Blackthorn | Payments Setup Wizard tab
Classic: Navigate to the application drop-down button (blue button in the upper right-hand corner) > select "Payments (Admin)" app > click the Blackthorn | Payments Setup Wizard tab.
2. Select "Test" then click Connect with Stripe.
3. Enter the information below and click Create your Stripe account.


4. Enter in additional information and click Authorize access to this account.
If you don't want to add additional information regarding your account now, just click the Skip this account form at the top of the page.


You are now setup with a Stripe account and that account is connected to your Salesforce Org.


Existing Stripe Account
The instructions below are for connecting an existing Stripe account to your Salesforce Org.

1. Navigate to Blackthorn | Payments Setup Wizard.
Lightning: Navigate to app launcher > select "Payments (Admin)" app > click the Blackthorn | Payments Setup Wizard tab.
Classic: Navigate to the application drop-down button (blue button in the upper right-hand corner) > select "Payments (Admin)" app > click the Blackthorn | Payments Setup Wizard tab.
2. Select "Test" then click Connect with Stripe.
3. Click Sign Innext to "Already have a Stripe account?"
If you are already signed into your account, your username will be in place of the "Already have a Stripe account" and you can click Skip this account form.
4. Enter your Stripe account credentials and click Sign in to your account.


Your existing Stripe account is now connected to your Salesforce Org.


Objects

Blackthorn | Payments to Stripe Translation
Payment Gateway Customer = Customer.
Payment Method = Card, Bank Account, or other.
Transaction = Payment (Charge), Adjustment, Transfer, Payout (as Record Types on Transaction).


Core Objects
Payment Gateway: Everything "routes" through a Payment Gateway: Payment Method, Transaction, and Stripe Customer.
Payment Method: This object houses all the Payment Method (card, ACH) information for your customer.
Transaction: This object captures, authorizes, and refunds all Transactions connected with your Stripe account.


Secondary Objects
Payment Gateway Customer: Stripe (and other payment gateways) maintain their concept of what Salesforce would refer to as a Person Account. The Stripe Customer is the Stripe-side data model for the entity of the Payment Method holder and Transaction relations.
Payment Schedule: This object allows you to create forward-looking, scheduled Transactions that can be automatically captured.


Tertiary Objects
Webhook Event: When Stripe sends Webhook Event records, we capture them in this object. They are processed every ve minutes from a scheduled process that runs in the background.
Company Info: The Company Info object is used by many of our other apps, such as Blackthorn Events. If your organization has multiple business entities, this is where they'd be de ned.
Location: Similar to Company Info, Location is used by other apps.


Migrating Payment Methods and Transactions
Are you currently using PayPal, Authorize.net, Braintree, CyberSource, First Data or another gateway? If you currently 'tokenize' your cards, and hopefully you do to remain PCI compliant, you'll need new tokens once you switch to Stripe so you don't need to ask your customers for their cards again.

Contact your Payment Gateway and contact Stripe at support@stripe.com.
Your provider will send their data to Stripe, retaining PCI compliance.
Use Blackthorn Payments' Historical Sync feature to migrate your Customers and Payment Methods (cards and if you have them, bank accounts) to Salesforce with new 'tokens' (in Stripe they utilize unique [Card] IDs, but you can think of them as tokens). We do not support any relational database logic to automatically associate these records to your
Salesforce records.
These new Card IDs can be charged in the same way as a card, but keep you PCI compliant.

If you're not currently 'tokenizing' your cards, after installing Blackthorn Payments, you can re-enter the card data as new Payment Methods. After this happens, the data will be 'tokenized', i.e. the card data will be erased (it's technically never saved) and you'll be left with unique Card IDs to subsequently charge your customers with.


Deleting Test Data

Stripe
1. Navigate to your Stripe Dashboard.
2. Toggle the V iew test data switch to "ON". (left-hand column).
3. Click Business settings. (left-hand column)
4. Select "Data".
5. Next to Test data, click Delete all test data.
6. Click Delete Now.


Salesforce
Whether you are in a Production or Sandbox Org, you will need to temporarily deactivate all triggers so that you can delete Transaction, Payment Method, and Payment Gateway Customer records.

1. Navigate to Custom Settings.
Lightning/Classic: Go to Setup > In the Quick Find box, type in and select "Custom Settings".
2. Click Manage next to Blackthorn Pay - Trigger Settings.
3. Click Edit.
4. Check the Disable A ll T riggers checkbox.
5. Click Save.
6. Delete all of your test data.
7. Navigate back to Custom Settings and UNCHECK Disable A ll T riggers .


Next Steps
Follow our quick start instructions to get Blackthorn Payments up and running.
Use our Historical Sync process to bring over existing Stripe data into Salesforce.
Complete our Go Live Checklist to make the most of Blackthorn Payments in your Org.


Overview

Pre-requisite
Stripe Billing integration is an optional feature for Blackthorn Payments. In order to enable it, contact Blackthorn Support.


Blackthorn Payments consumes the Stripe Billing API, bi-directionally
You can perform any API-supported action within Salesforce that you can perform within the Stripe dashboard. Some processes include:

Start a Stripe subscription within Salesforce from an Account
Start a Stripe subscription within Salesforce from an Opportunity
Start a Stripe subscription within Stripe that pushes to Salesforce
Update subscriptions from Salesforce that update in Stripe
Update subscriptions from Stripe that update in Salesforce
Add Usage to Salesforce that sends to Stripe to automatically
Calculate Usage aligned with Tiers and Prices.
Invoices are auto-created in Salesforce from Stripe
Charges on Invoices are auto-created in Salesforce from Stripe

Report on all of your Stripe data natively in Salesforce using native Reports and Dashboards


Stripe Billing's architecture alignment with our Salesforce-native model
Salesforce Product = Stripe Product
Salesforce Price (Custom Object) = Stripe Price
You can have multiple Prices per Product. The Price contains the amount if there are no Tiers. In this sense, it's similar to how Salesforce's Price Books work.
Salesforce Tier (Custom Object) = Stripe Tier
You can have multiple Tiers per Price.
Salesforce Usage (Custom Object) = Stripe Usage
Salesforce Subscription and Subscription Item (Custom Objects) = Stripe Subscriptions and Subscription Items
Salesforce Sales Document and Line Item (Custom Object) = Stripe Invoice and Invoice Item
For Stripe Billing to work properly, Salesforce records must exist in Stripe prior to creating or updating a Stripe Subscription from Salesforce. You can create Stripe records from Salesforce, or sync them back from Stripe.


Stripe Billing Objects Diagram


Step-by-Step Instructions

Initial Setup
1. Install Blackthorn Payments from the Candy Shop.
2. Complete the Payments Setup Wizard and connect to your Stripe account in test mode.
Webhooks are required for Stripe Billing.
3. Send Blackthorn Support your org ID to enable Stripe Billing.
4. Once enabled, navigate to the Payments Admin tab, under Stripe Billing, click the "Deploy Stripe Billing Fields" button.
5. Follow these instructions and install the Stripe Billing Screen Flow unmanaged package.
This unmanaged package allows you to launch a screen ow from the Opportunity record when a subscription needs to be generated.


Webhooks

When you set up webhooks, changes that are made in Stripe will push to Salesforce, so please have your relationship settings de ned on the Payment Gateway before enabling webhooks.


If you only have Products and Prices (Plans) in Stripe
This information needs to be in Salesforce so that you can generate subscriptions in Salesforce.

1. Navigate to your test Payment Gateway record.
2. Click the "Sync With Stripe" button.
3. Underneath "Billing," click Product. Let all products sync before clicking the "Prices" button.
4. Then click the "Prices" button. Let all Prices sync before clicking the "Coupon" button.
5. Then click the "Coupons" button.


If you have Products in Salesforce, but nothing in Stripe
Please follow the instructions for syncing a Product to Stripe.

Then you can create a Price for the Product that syncs to Stripe.


Time to test it out!
You should be able to create a subscription from an Opportunity record that syncs over to Stripe. After 1 hour (not sure why it takes so long on the Stripe side), an invoice will sync back to Salesforce related to the Subscription, Customer, and Account record.


Testing other scenarios
Give your billing scenarios a test. IE., upgrading or downgrading an existing subscription. This update will only work for future invoices. If you change a subscription when there is an open invoice, the open invoice will not be updated.

Please reach out Blackthorn Support if you have questions regarding use cases. Our team uses the feature for our app subscriptions!


Migrating Records from Stripe to Salesforce
Go to the Payment Gateway tab, click on your Payment Gateway. Click Sync with Stripe.
Make sure you have Account and Contact records in your Salesforce org that align with your Stripe records. We attempt to match Stripe Customer Emails against Contact Emails using the relationship setting feature.
Click each button from left to right, one at a time, waiting for the process to nish as viewed in Setup | Apex Jobs. Start with Customers.


No Matching

If you need to match Payment Gateway Customers (Stripe Customers) to Contacts and Accounts with custom matching IE., Billing ID, relate the Relationship Setting to the Payment Gateway record, and then for the matching logic, set it to "No Matching or Record Creation.


Settings
These settings help you control the processes for Stripe Billing.

Blackthorn | Payments Admin
Schedule recommend billing batch jobs, run batch jobs on-demand.

Permission Sets
Give access to Payments object related to Stripe Billing to Salesforce Users.

Scheduled Batch Jobs
Information about Billing speci c scheduled batch jobs.


Blackthorn | Payments Admin
This tab will help you manage your Stripe Billing settings.

The following jobs are only scheduled for customers who previously had Stripe Billing enabled for their org. (We do not support Stripe Billing for new customers.)

Click Schedule Billing Jobs on the Blackthorn | Payments Admin Scheduled Jobs tab to schedule the jobs with a single click.

To schedule each job individually, click the following buttons on the Blackthorn | Payments Admin Stripe Billing tab.

Deploy Stripe Billing: Deploys the necessary elds to use Stripe Billing in a Salesforce org.
Re-Calculate Account Revenue: Recalculates the Historic Account Values (from Transaction) and MRR/QRR/ARR (from Subscription).
Rollup Transaction to Invoice Button: Rolls Transactions up to their related Invoice (Sales Document).


Permission Sets

Prerequisite
The following is a required permission that is NOT included in the Blackthorn Payments Stripe Billing permission set, but is required to use Stripe Billing.


Object                                                                                                        Read                                                         Write                                                       Delete                            View All


Product                                                                                                        ✅                                                            ✅                                                            ✅                                 ❌


Blackthorn | Payments (Stripe Billing)
This permission set has all the permissions to the objects and elds included in the Stripe Billing functionality. This should be used by customers who want to give access to users who use the Stripe Billing feature.


Custom Permission Sets
Use the steps below to create custom permission sets. If you want users to create and edit Product records, add the permissions to the custom permission set.

1. Install the latest Blackthorn | Payments Salesforce AppExchange package in a sandbox.
2. Log in to the sandbox org as a System Admin.
3. Navigate to Setup.
4. In the Quick Find box, enter "Users."
5. Click Permission Sets.
6. Click Blackthorn | Payments (Stripe Billing).
7. Review all permissions and compare them to the custom permission sets you created. Ensure that all permissions granted by our out-of-the-box standard permission sets are recreated in your permission set.


Site Guest Users
Guest users must be assigned a custom permission set plus the Blackthorn | Payments (Site Guest User) permission set to have Read access to several standard objects that are required to process webhooks. The custom permission set must include the following:

Account - Read
Opportunity - Read
Product - Read

NOTE: Whether webhooks are processed manually or via batch jobs, sharing rules apply. Using a custom trigger allows webhooks to be processed in system mode, bypassing sharing rules. You may experience limitations for use cases, depending on your speci c scenario.


Blackthorn | Scheduled Jobs
You can nd the scheduled jobs below in Setup. In the Quick Find box, enter and click "Scheduled Jobs". All of the Payments job names start with Blackthorn | Payments.

Blackthorn | Payments Send Stripe Invoices - It runs at 6 am each day to send the Invoice to the customer when Send I nv o ic e On Date = "TODAY" on the Invoice.
Blackthorn | Payments Past Due Invoices - It runs at 5 am each day to update the Invoice P ay ment Status = "Past Due" when the Due Date < Today and P ay ment Status = "Unpaid".

You can schedule the jobs listed above by clicking the Schedule Billing Jobs button in the Blackthorn | Payment Admin tab.


Process Stripe Billing Webhook Types Asynchronously
A global method that allows customers to process certain Stripe Billing webhook types asynchronously instead of via the Blackthorn batch jobs was added. If the P ro c ess A sy nc checkbox = “True”, the existing web processing batch jobs will skip those webhooks.

Blackthorn customers are responsible for adding the logic that 1) sets the records they want as Process Async and 2) calls the async method to process them. The following example code creates a before trigger to check the P ro c ess A sy nc box and an after trigger to call the async method.

Before proceeding, two updates must be made to the Site Guest User/public user.

Step 1: To avoid permission errors, give the Blackthorn | Payments (Site Guest User) permission set Read access to the Product (Product2) object.


1. Click the Gear icon in the upper right-hand corner.
2. Click Setup.
3. In the Quick Find box, enter and click “Permission Sets.”
4. Create a new permission set.
a. Click New.
b. In the Label eld, enter a descriptive name for the permission set, such as “Read Access to Product2.”
c. Click Save.
5. Con gure object permissions.
a. Click “Object Settings” or “Object Permissions” in the Apps section.
b. Find and click the Product (Product2) object. If you don’t see it, use the search function to locate it.
c. Click Edit next to the Products heading.
d. In the Object Permissions section, set Read to “Enabled” (checked). Do not enable Edit , Create , and Delete unless they are needed.
e. Click Save.

Step 2: Assign the newly created permission set to the public user.

1. Navigate back to the site you created.
2. Click Public Access Settings.
3. Click the View Users or Assign Users button.
4. Click the link for the site guest user.
5. In the Permission Set Assignments section, click Edit Assignments.
6. Move the newly created permission set from the Available Permission Sets column to the Enabled Permission Sets column.
7. Click Save.


Plaintext                                                                                                                                                                                                                                                                                           Copy

trigger customWebhookTrigger on Webhook_Event__c (before insert, after insert) {
if (Trigger.isBefore) {
for (bt_stripe__Webhook_Event__c webhook : Trigger.new) {
if (webhook.bt_stripe__Type__c == 'invoice.created') {
webhook.bt_stripe__Process_Async__c = true;
}
}
}

if (Trigger.isAfter) {
List<Webhook_Event__c> webhooks = [SELECT Id, Name, Type__c, Process_Async__c, Processed__c, Payment_Gateway__c, Data__c FROM Webhook_Event__c WHERE Id IN :trigger.new];
for (Webhook_Event__c webhook : webhooks) {
if (webhook.bt_stripe__Process_Async__c && webhook.bt_stripe__Type__c == 'invoice.created') {
// Call without sharing class here to process the webhook
}
}
}
}


NOTE: Replace 'invoice.created' or add additional webhook types as needed.


Features
See each sub tab noting each feature!

Account Subscription Data
Creating Subscriptions from Opportunities
Migrating Subscriptions


Account Subscription Data
See all of an Account's subscription and revenue data from elds on the Account.


Let's nd out how the metrics are evaluated!

They are divided into mainly two sets of elds ~

1. Upcoming ARR/MRR/QRR -This eld indicates the total upcoming amounts of annual/monthly/quarterly recurring subscription invoices. It gets populated only when there is an upcoming Invoice in Stripe.
2. Last Finalized ARR/MRR/QRR - This indicates the total nalized or paid amounts of annual/monthly/quarterly billing subscription invoices. It gets populated when the Account's subscription has a Paid Invoice.

All the above metrics rollup from the Account's related Subscriptions where Status = "Active". If Status = "Canceled", the Upcoming MRR/ARR/QRR is set to 0. The rollup is triggered from the Subscription Item and Invoice.

Note: The subscription rollups only calculate correctly where the pricing is per-unit (vs usage-based billing).

3. Historical Account Value rolls up from the Account's related Transactions.


Account Subscription Status
When an account has a subscription associated with it, we are showcasing the Subscription Status at account level using the "Subscription Status" eld. This eld will be auto-populated.


For more than one subscription, this eld will update to "See Subscriptions". (Please add the eld onto the page layout)


Batch Apex Callouts to Stripe
Some customers use batch apex to make callouts to Stripe. This is supported for Product, Price, Coupon, Subscription, Subscription Item, Subscription Schedules, and Stripe Invoices. This functionality is available in conjunction with Salesforce's Change Data Capture feature.


Setup
1. Optional: Add a batch apex class to your org that will work with the Change Data Capture feature. (This code will be dependent on your business use case. Use your in-house development team to decide what works best for your org.)


Some use cases use declarative means to identify new Stripe Billing objects. The apex code snippet below is only an example. Your setup may differ.


Example of a batch apex class:

Your browser does not support PDF. Click here to download.

2. Add the object you would like to use to the Change Data Capture setting in Setup.


3. Navigate to Setup > Custom Settings > Blackthorn Pay - Trigger Settings > Enable Change Data Capture = TRUE.
4. Create the records you would like sent to Stripe.
5. Optional: Execute apex code that will tell the Change Data Capture logic which records to send to Stripe.


The code snippet below is only an example of a way to call the apex class from step 1. Your use case may differ and may use other declarative means for sending new records to Stripe.


Example of code used in an Execute Anonymous window of the developer console:


Java                                                                                                                                                                                                                                                                                Copy

Set<
Set <Id
Id>> recordIds = new Set
Set<<Id
Id>>{recordId1
recordId1,, recordId2
recordId2,, recordId3
recordId3,, recordId4
recordId4}};
SendingToStripeBatch batch = new SendingToStripeBatch(
SendingToStripeBatch(new Map<
Map<Id,
Id, SObject>
SObject>([SELECT Id,
Id, bt_stripeTest__Push_To_Stripe__c FROM Product2 WHERE Id IN :recordIds]
recordIds]).keySet(
keySet(), 1);
Database.
Database .executeBatch
executeBatch((batch
batch));


Once the steps above have been con gured and the code executed you will notice the related records are sent to Stripe.


Creating Subscriptions from Opportunities
You can generate Subscriptions from Opportunities and automatically push them to Stripe. In order to set the elds on the Opportunity and the Opportunity Product layouts, use the settings on the "Blackthorn | Payments Admin" tab, "Stripe Features" left-hand tab, then the "Deploy Stripe Billing" button.


Set up the Opportunity
1. Create an Opportunity or go to an existing one.
2. Add Opportunity Line Items.
3. Set the Customer lookup.

4. Add additional optional eld values as needed:
Set the Payment Method lookup eld. If not set, the default will be used.
Set the Billing Method     eld. If left blank, Charge Automatically will be used
Set the Trial End (Billing Start Date)        eld. If left blank, Subscription uses the Price default or starts immediately.

If Billing Method     eld set to "Send Invoice", set the Days Until Due     eld.
Set the Stripe Coupon     eld to apply any discounts.
Set the Memo    eld so it is included in invoice PDFs, invoice emails, and the Hosted Invoice Page.

Set the Trial Period Days      eld to de ned the number of trial period days before the customer is charged for the rst time. Both Trial End and Trial Period Days             elds if left blank, Subscription uses the Stripe Price default or starts immediately.
Set the Default Tax     eld so tax rates will apply to any subscription item that does not have tax_rates set.
Set the Billing Cycle Anchor (First Invoice)         eld to determine the date of the rst full invoice, and, for plans with Month or Year intervals, the day of the month for subsequent invoices.

Proration Behavior : Determines how to handle prorations when the billing cycle changes (e.g., when switching plans, resetting billing_cycle_anchor=now, or starting a trial), or if an item’s quantity changes.

5. Save the record.


Proration Behavior Update

If a Stripe Billing Subscription Proration Behavior = “--None--” or is left blank, any changes made to the Subscription will no longer be prorated.


Opportunity Products
1. Navigate to the "Products" related list on the "Opportunity" record
2. Create an Opportunity Product
In order to make an Opportunity Line Item a Subscription Item in the generated Subscription:
Set the related Price on the Opportunity Line Item lookup eld. The Stripe Price must be related to the selected Product.
Set the Product Type picklist to Plan.

In order to add an Opportunity Line item to the Subscription Customer's rst invoice as a one-time item:
Set the Product Type picklist to One-Time.


Push to Stripe
1. Check the Push to Stripe checkbox and save, or automate an Opportunity Stage to trigger this checkbox with a Work ow, Process Builder, or other.


Create Subscription Button

On Payments packages v5.1 and above users can add the 'Create Subscription' button to their page layout and use that button to push data to Stripe and create a new Subscription.


2. If successful, the Subscription      eld will be populated, which is a lookup to the generated Subscription.

3. Stripe will create an invoice for the Subscription. After webhooks process (depending on your org's webhook event processing frequency) a "Stripe Invoice" record will be created in the org and listed on the Subscription's Invoice related list.

Note: An Invoice that is created for a Subscription pushed from Opportunity , will have the Opportunity lookup updated on it. If the Opportunity is selected as a Transaction's parent object, then related Transaction records also populate the Opportunity lookup derived from the Invoice


Opportunity validations when generating subscriptions
Validation when                                                                                                                                                                               Error Message
No customer de ned on opportunity                                                                                                                                         Please select the Customer.
No payment method is added to the customer and trying to set the billing method to charge automatically or leaving it blank                                               If the Payment Gateway Customer has no Payment Method then the "Send Invoice" Billing Method should be used.
Billing method = Send Invoice and Days until Due eld is left blank                                                                                                        When the Billing Method is "Send Invoice", days Until Due should be populated.
Billing method = Send invoice but customer email is blank                                                                                                                 In order to create invoices that are sent to customers, the Customer must have a valid email.
Trial End < NOW                                                                                                                                                           Trial End Date should be in the future.
Trying to push a price with no Price ID populated                                                                                                                         The related Price is not yet pushed to Stripe.
Product associated with the price does not match opportunity product                                                                                                      The Product on the Opportunity Line Item should match the Price's Product.
Creating subscriptions from opportunities without adding the line items                                                                                                   A subscription cannot be created when Opportunity Line Items have missing data.
Product’s PG doesn’t match with customer’s PG                                                                                                                             The Price's Payment Gateway should match the Customer's Payment Gateway.
Price is Inactive                                                                                                                                                         The Price is marked as inactive and no new subscriptions can be created to on Price. Set the Price as Active and con rm the Stripe Price ID is populated.
Product Type set to Plan, but no price added                                                                                                                              Please select a Price.
Product Type set to Do Not Include and no other items with Product Type set to Plan have been added.                                                                      A subscription/invoice cannot be created without line items.


Migrating Subscriptions
There's no right or wrong way to do this. You can enter Products and Prices in Stripe, Subscription data in Salesforce, Tiers in Stripe, or Payment Gateway Customers in Salesforce; whatever oats your boat. This is our guide on an opinionated way to do it!

Typical entities to manage

Salesforce Accounts
Salesforce Contacts
Stripe Payment Gateway Customers
Stripe Charges
Stripe Cards & Bank Accounts
Stripe Products
Stripe Prices
Stripe Subscriptions

Salesforce and Stripe have records that relate to each other, so it's important to migrate records in the order in which one entity requires the other. For instance, you can't create a Stripe Subscription without a Stripe Payment Gateway Customer.


Steps
1. Backup your data.
2. Setup Webhooks. This creates a data mirror between Salesforce and Stripe.


Migrating from outside of Stripe to using Stripe
3. Set the Data Loader batch size to "1" (each insert will re an outbound Stripe REST callout and a few triggers will re).
4. Export your Salesforce Accounts to a CSV le.
5. In the Account CSV le, add the columns "Email" and "Description". Keep the ID (Account ID) column and the Account Name. Delete the other columns.
6. Now it's time to create Stripe Payment Gateway Customers. With Data Loader, insert Payment Gateway Customer records. Map the ID eld to the Account ID, Email should be the primary email used to either identify this Account (your main contact) or the main billing contact, and the Description should be either the Account Name, Contact Name, or
something like "Account - Contact" such as "Matrix - Morpheus Neo".
7. With the success le, you can now go in a few directions. You can next migrate Payment Methods if you have raw card data or you can migrate Products and Prices next.
8. If Payment Methods, prepare a le with the correct Record Type (Charge Card vs ACH), Account and Contact IDs, the Stripe Payment Gateway Customer Salesforce record ID, and the respective raw card ID data.
9. Products. If you want to go right into migrating Subscriptions, Stripe Subscriptions require three things: a [Stripe] Payment Gateway Customer, at least one Product, and its associated Price. They may also include a Coupon (discount code). Prices may contain Tiers. So rst, you want to migrate Products. Products can start in either Salesforce that push to
Stripe, or in Stripe that then push to Salesforce. Product sync 1:1 between Salesforce and Stripe.
10. Prices. Prices are similar to Price Book Entries in Salesforce, but they have a lot more data, such as the frequency (interval) of the billing. You can enter these in Salesforce or Stripe once you have your Products entered.
11. OPTIONAL Tiers. If you have tiered-based pricing, you can create Tier records related to your Prices in either Stripe or Salesforce.
12. Subscriptions. If you have one Product & Price per Subscription, you only need 1 CSV to migrate these into Salesforce. If you have multiple Products & Prices per Subscription, you'll need 2 (parent/child relationship). Stripe has a shortcut when you only have 1 Product & Price per Subscription. Your rst CSV needs: Account ID, 13. (Stripe) Payment
Gateway Customer ID, and applicable Subscription eld values to see (see our Subscriptions & Subscription Items documentation for details. Your second CSV needs: Quantity, Price, and other Subscription Item elds as applicable.
13. (Stripe) Payment Gateway Customers push to Stripe automatically. Products, Prices, and Subscriptions each have Push to Stripe checkbox elds you can set either on import or update once you're con dent the data migrated correctly. This will trigger the push to Stripe. If you're creating these records in Stripe, they'll appear in Salesforce via Webhooks
every 5 minutes as part of our batch.


Currently using Stripe and want to use Blackthorn Payments with Stripe Billing
1. Go to the Payment Gateway tab, click on your Payment Gateway. Click Sync with Stripe.
2. Make sure you have Account and Contact records in your Salesforce org that align with your Stripe records. We attempt to match Stripe Payment Gateway Customer emails against Contact emails to set lookups.
3. Click each button from left to right, one at a time, waiting for the process to nish as viewed in Setup | Apex Jobs. Start with Payment Gateway Customers.


Stripe Billing Object and Stripe API Interaction

Usage
Submission Method:
Automatically pushed to Stripe upon save of related objects
Description:
When the Subscription_Item__c & Quantity elds are de ned, the usage record is automatically created in stripe. There are no updates.


Product
Submission Method:
Automatically pushed to Stripe upon save of related objects
Description:
Once the Payment Gateway record is saved on the product record, the product is automatically created in Stripe. No updates are allowed once the product is pushed to Stripe.


Subscription
Submission Method
Click the button / Check the Push to Stripe     eld
Description
Initially, a subscription is created by clicking the Submit to Stripe button. We also provide a Push To Stripe checkbox eld on the subscription. When checked, a subscription is created in Stripe. Once created & subscription Id is present - it then automatically syncs on updates. The elds that trigger auto sync of the subscription to Stripe are:
1. Payment Method
2. Coupon
3. Billing Method
4. Days Until Due
5. Amount Threshold
6. Reset Billing Cycle Anchor 7. Cancel At Period End
7. Prorate
8. Proration Date
9. Billing Cycle
10. Anchor First Invoice
11. Trial End
12. Trial From Price
13. Tax Percent
14. Pending Invoice Item
15. Interval
16. Pending Invoice Item
17. Interval Count


Subscription Item
Submission Method:
Submitted along with Subscription
Description:
Once the subscription is saved in stripe any new updates or new line items added - are automatically synced. The Price & Quantity
elds will trigger an automatic update.


Sales Document
Submission Method:
Click the button/Check the Push to Stripe     eld
Description:
Initially, an Invoice is created by clicking the Submit to Stripe button. We also provide a Push To Stripe checkbox eld. When checked, it creates an Invoice in Stripe. Once created and an Invoice Id is present - it then automatically syncs on updates. The elds that trigger an auto sync of the Invoice to Stripe are:
1. Payment Method
2. Coupon
3. Billing Method
4. Days Until Due
5. Due Date
6. Customer

Updates are only allowed when the Invoice Stage = Draft. Once the Invoice is sent or nalized you cannot update the Invoice.


Line Item
Submission Method:
Submitted along with Invoice
Description:
Once the Sales Document is saved in Stripe as an Invoice, any updates or new line items added will automatically sync to Stripe. The Price & Quantity
elds will trigger an automatic update. This can be disabled via a Custom Setting, "Disable_LineItem_AutoSync_With_Stripe__c."


Stripe Coupon
Submission Method:
Click the button / Check the Push to Stripe    eld
Description:
A coupon is created by clicking the Submit to Stripe
button. We also provide a Push To Stripe
checkbox eld that when checked creates a coupon in Stripe. No updates.


Stripe Price
Submission Method:
Click the button / check the Push to Stripe    eld
Description:
A Stripe Price is created by clicking the Push to Stripe button. We also provide a Push To Stripe checkbox eld that when checked creates a Price in Stripe. Once created and the Price Id is present - it then automatically syncs on updates. The elds that trigger the auto-sync are:
1. Active
2. Product
3. Name
4. Trial Period Days


Tier
Submission Method:
n/a
Description:
Tiers are pushed when a Price is pushed. No updates are allowed.


Stripe Gateway Order
Submission Method:
Click the button
Description:
Created when you click the Push to Stripe button. No updates are allowed.


Gateway Order Item
Submission Method:
Submitted along with the Stripe Gateway Order
Description:
Gateway Order Items are pushed with the Stripe Gateway Order.


Gateway SKU
Submission Method:
Click the button
Description:
Created when you click the Push to Stripe button. No updates are allowed.


Gateway SKU's
Stock Keeping Units represent speci c Product variations.

You can create SKU's only for Good-type Products. You can create these Products on Stripe Dashboard | Orders | Products.


Once you have created a Product, you can add SKU's in the Inventory section of that Product on the Stripe Dashboard.


Products and SKU's get pushed into the Salesforce org via webhooks.
Products and SKU's can be updated from the Stripe Dashboard. The updated records are synced via webhooks.
Deleted SKU's are deleted from the Salesforce org.


Creating SKU's from Salesforce
You can create a SKU record in Salesforce and push it to Stripe.

1. Create a Gateway SKU record.
2. Set the Product lookup. Note:
The Product should be synced with Stripe.
The Product Type should be Good.
3. Set Currency ISO and Price elds.
4. Optionally, set Inventory Type and Inventory Quantity elds.
5. Save the record.
6. Click 'Push to Stripe' button on the layout.
7. You should see the SKU Id eld populated.


Invoices
An Invoice states the amount a customer owes. Invoices can be generated periodically from Subscriptions or as a one-off Invoice. A Stripe Invoice is created from the Blackthorn Invoice (bt_stripe__Sales_Document__c) object.


Types of Invoices
There are two types of Invoices created by the Blackthorn Invoice object: Invoice and Stripe Invoice.


Invoices
The checkout process generates Invoices. Not all elds from a Blackthorn Invoice are mapped to a Stripe Invoice, and Invoices can work independently from Stripe Invoices.


Stripe Invoices
A Stripe Invoice is included with all records coming from Stripe Billing. All elds on a Stripe Invoice are mapped to an Invoice.

The following list includes the Stripe Invoice elds that are mapped to an Invoice:

Name
Customer (Mandatory)
Subscription
Stripe Coupon
Stripe Invoice Id
Stripe Hosted Invoice Link
Currency
Bill To Street
Bill To Street 2
Bill To City
Bill To State
Bill To Country
Bill To Postal Code
Ship To Street
Ship To Street 2
Ship To City
Ship To State
Ship To Country
Ship To Postal Code


Automatically Generated Invoices
When a customer’s transaction is complete and the charge is successful, Stripe generates a Stripe Invoice, which is synced to Salesforce through a webhook.

NOTE: Invoices are only generated automatically from Stripe Billing. Payment Schedules cannot create Invoices.


One-Off Invoices
You can create an individual Stripe Invoice for a customer.


Add Line Items
Before you push the Invoice to Stripe, you must add at least one Line Item (bt_stripe__Line_Item__c) to the Invoice. The Line Item(s) record will inherit one of the following record types.

Rec o rd T y pe = "Line Item" This is used for all non-Stripe Line Items on an Invoice.
Rec o rd T y pe = "Stripe Line Item" This is used for Stripe Invoices.

The Line Item record(s) must include either a U nit P ric e and Quantity , OR a P ric e and P ro duc t , before the Invoice can be pushed to Stripe.


Create a One-Off Invoice
1. Go to the Invoice you want to sync to Stripe.
2. Con rm that the following elds contain a value.
Custo mer
Currenc y
3. Con rm that the Invoice has at least one Line Item with the Desc riptio n and the U nit P ric e and Quantity        elds populated.
4. Check the P ush T o Stripe checkbox.
5. Click Save.


Update Line Items
You can update existing Line Items when the Invoice Status = "Draft." This will trigger updates to the Stripe Invoice.


Log a Partial Payment as Non-Gateway
If you receive a partial payment, such as a check, you can log it as non-gateway against an Invoice in Stripe by using the customer’s Payment Gateway Customer A c c o unt Balanc e eld in Salesforce.

Before the Invoice is due, Stripe will automatically apply the amount from the customer's A c c o unt Balanc e eld. Webhooks will update the remaining balance on the customer record. A Salesforce Transaction record will be created once the Invoice is paid in full.

If the Invoice remains partially paid, the Invoice’s Balanc e Due eld will re ect the remaining amount due, and the Invoice’s P ay ment Status will be set to "Unpaid."


Steps
1. Go to Setup.
2. In the Quick Find box, enter and click "Payment Gateway Customer."
3. Click the Page Layouts tab.
4. Select the "Stripe Customer Layout."
5. Drag and drop the A c c o unt Balanc e eld onto the page layout.
6. Click Save.
7. Open the Payment Gateway Customer record and refresh the page.
8. Click the Pencil icon next to the A c c o unt Balanc e eld.
9. Enter the value of the paid Invoice amount.


10. Click Save.

You will see the A c c o unt Balanc e re ected in your Stripe dashboard.


Open the Stripe Invoice to see the applied amount.


Once the Invoice is paid, a Transaction will be created and logged against the Invoice in Salesforce.


Mapping a Stripe Invoice Status to an Invoice Status
The following table shows the mapping relationship between the Stripe Invoice statuses and the Invoice statuses:


Stripe Invoice Status                                                                                                                                                                                                  Invoice Status


draft                                                                                                                                                                                                                  Draft


open                                                                                                                                                                                                                   Sent


paid                                                                                                                                                                                                                   Completed*


uncollectible                                                                                                                                                                                                          Rejected


void                                                                                                                                                                                                                   Voided


*Invoices with Status = "Completed" cannot be edited.


Troubleshooting & FAQs

Troubleshooting
Review the following scenarios that may cause an error before syncing an Invoice with Stripe.


Scenario                                                                                                                                                       Error Message


The Invoice Custo mer eld is blank.                                                                                                                            To push an Invoice to Stripe, you must enter a value in the Custo mer eld.


Modify the discount Code on an Invoice after the Invoice is pushed to Stripe                                                                                   The discount Code cannot be modi ed using the API.


The P ay ment Gateway       eld on the Payment Gateway Customer record is not de ned.                                                                          Add a Payment Gateway to the P ay ment Gateway        eld.


Invoice Status = "Draft" and Due Date = "before today"                                                                                                         The Invoice's Due Date must be in the future.


Invoice Status = "Draft", Billing Metho d = "Send Invoice," and Day s U ntil Due and Due Date are blank                                                        If the Billing Metho d is set to "Send Invoice," the Day s U ntil Due eld must contain a value.


The Invoice's Billing Metho d is set to "Send Invoice," but Payment Gateway Customer's Email eld is blank.                                                     To create an Invoice to send to a Payment Gateway Customer, the Email eld must have a valid email.


The Invoice's Billing Metho d is set to "Charge Automatically," but the Invoice's P ay ment Metho d eld is blank, not valid, or not veri ed.                   To create an Invoice that will be charged automatically, the P ay ment Metho d eld must have a payment method. Add a Payment Method or change the Billing Metho d to "Send Invoice."


Try to change the Invoice Status when it is set to "Completed" or "Voided."                                                                                    The Invoice Status eld cannot be changed if it is set to "Completed" or "Voided."


Try to update an Invoice when the Status is set to anything BUT "Draft."                                                                                       An Invoice can only be updated when the Status is set to "Draft."


Add a Line Item to an Invoice when the Status is set to anything but "Draft."                                                                                  Line Items can only be added to an Invoice when the Status is set to "Draft."


FAQs
Q: Can I create a custom record type?
A: No, custom record types are currently not supported.

Q: How will my coupon (discount Code) be applied?
A: Coupons (Code Disc o unt P erc entage or Disc o unt A mo unt ) applied to prorated Subscriptions in Stripe will be applied only at the Invoice level, not at the prorated Line Item level.

Q: W hat permissions does my Site Guest User need?
A: A guest user must be assigned the Blackthorn | Payments (Site Guest User) permission set and custom permissions to have Read access to several standard objects, which are required to process the webhooks. The custom permission set must include the following object permissions:

Account - Read
Opportunity - Read
Product2 – Read

Q: How do I update the Metadata       eld on a Line Item?
A: Add the Metadata eld to the Line Item’s page layout. If a value is populated from this parameter, you will see the update in Salesforce once the webhook process is complete.


Products
Products can be created in Salesforce or Stripe. Products de ne what you sell. Before you can create a Price or Subscription you need to create a Product.


Product Permission Limitations

Product is a standard object so it is not included in the Stripe Billing permission set. If you would like users to create and edit product records be sure to add permissions to a custom permission set. Additionally, you can have System Administrators perform actions with products.


Add Important Fields to the Page Layout
You'll want to add the following elds to your Product page layout:

Product ID

Type

Payment Gateway


Creating a Product
1. Create a Salesforce Product or navigate to an existing one.
2. Set the Payment Gateway lookup eld to an active Payment Gateway (click the lookup selector and select).
3. Set the Type picklist to Service.Prices can be created only for products of type 'Service'.

4. The Product will automatically be pushed to Stripe.You'll know it worked if you see a Product ID      eld value populated within a couple of seconds.


Existing Stripe Products
If you already have created products in Stripe, you can sync them with your Salesforce org.

1. Go to the Payment Gateway record.
2. Click Sync with Stripe .
3. New Products will be created in Salesforce.


Retrigger the Action of Pushing to Stripe
There may be some instances where the Product record did not automatically push to the Payment Gateway. For times like these we've added a button labeled Push To Stripe . This button works very much like the buttons with the same name on the Price and Subscription objects.


1. Add the Push To Stripe button to your Product page layout.
2. Navigate to the Product record you would like to add to the Payment Gateway.
3. Click Push To Stripe

4. On the next page push Save .
5. You should see a green success message if this worked.
6. You'll also notice that the Product ID    eld was populated.

Note: You cannot use the Push To Stripe button for Product updates. Those changes are not supported.


Product prices

Note that your Salesforce Product prices don't effect the Stripe Prices of your products.


Stripe Coupons
Everyone loves discounts! Stripe Coupons are used to reduce the amount charged to the customer. With Blackthorn, we have you covered.


What do they do?
Can be Amount based or Percentage based
Can have time ranges when they are applicable
Can have a maximum redemption quantity
Can be set on a Subscription or a Customer


Create Stripe Coupons
To get started, navigate to the App Launcher and search for "Stripe Coupons"

Create a Stripe Coupon record.
Set Payment Gateway       eld.
Set Currency       eld.
Set Amount Off or Percent Off        elds.

Amount Off will take off a speci c dollar amount. For example; I ll in "10" here. This will subtract my total amount by 10.

Percent Off will take off a speci c percentage from the total. For example; I ll in "10" here. This will subtract the total amount by 10%.

Set Duration picklist.

Save the record.
Click Push to Stripe button.


If the Valid checkbox is checked, the Stripe Coupon is saved in Stripe.


Stripe Coupon elds
Code Name Name of the Stripe Coupon. This name is seen by your customer.

Payment Gateway Payment Gateway the Stripe Coupon is linked to.

Currency is required if this is an amount-based coupon.

Amount Off Amount of the discount applied to the Subscriptions.

Percentage Off Percentage of the discount applied to the Subscriptions.

Max Redemptions Maximum times the Stripe Coupon can be used by customers.

Duration Forever, Once or Repeating.

Duration In Months If Duration is set to 'Repeating`, length of the time range the Stripe Coupon is valid after being applied to a Subscription.

Redeem By Date after the Stripe Coupon is no longer valid.

Times Redeemed Number of times the Stripe Coupon has been used.


Subscription discounts
You can set a discount by setting the Stripe Coupon lookup eld on the Subscription before pushing the Subscription to Stripe. After this, the discount is applied to the Invoices, and the Stripe Coupon lookup eld is set on the Invoice records.


Customer discount
You can add a discount for a Customer. In this case, the discount will be added for every Invoice for the customer, generated from Subscriptions. To set a discount for a Customer, set the Stripe Coupon lookup eld on the Stripe Customer record.

If you set the Stripe User Coupon lookup eld to null (remove the value and save), the discount is no longer applied.


Delete Stripe Coupons
You can delete a Stripe Coupon from Stripe. After this, the Stripe Coupon is no longer usable.

In order to do so, go to the Stripe Coupon record and click the 'Delete From Stripe' button. After this, you if the Deleted from Stripe checkbox is checked, the Stripe Coupon was deleted from Stripe.


Stripe Gateway Orders
Stripe Gateway Order records in Salesforce are copies of the Order records in Stripe. These records get synced via webhooks. Note that you can't create Orders manually within the Stripe Dashboard.


Order Id is the Stripe Id of the order record.

Related Gateway Order Items carry Stripe Id's as well.
Related Gateway Order Items connect the SKU records to the Order; so they are the junction object between Orders and Products.


Create Stripe Gateway Orders from Salesforce
You can create a Stripe Gateway Order record with Line Items and push it into Stripe.

1. Create a Stripe Gateway Order record.
2. Set Customer and Currency ISO elds.
3. Set Shipping Street eld (the rest of address-related elds are optional).
4. Create at least one related Gateway Order Item record.
Set the Gateway SKU lookup
Set the Quantity
5. Click Push to Stripe button on the layout.
6. You should see populated Status, Amount and Order Id elds.


Stripe Prices & Tiers

The Payments package v5.1 requires Stripe API version 2020-08-27 or above.


We've renamed Plan to Price to support Stripe API updates. Customers must use Stripe API version 2020-08-27 or above in order to use the Price updates in v5.1.


Stripe Price records track how much and how often to charge for a Subscription. They can be used for recurring or one-time purchases and support various business structures. One way to think about the differences between a one-time price and a recurring price is that a user is charged a one-time fee to set up a Subscription, and then over time, the user is
charged a recurring amount for the Subscription.


About the Stripe Price Fields
P ro duc t : The Product related to this Stripe Price
I nterv al : The frequency with which the Subscription will be billed. Leave this blank if you are creating a one-time price.
Previously, I nterv al was a required eld. If you use a Payments package version earlier than Version 5.1 and want to use one-time prices, you must perform the following updates.
Change the required default setting for the I nterv al eld, so it is no longer required to create a Stripe Price record.
Remove the eld from the Stripe Price page layout if you do not need it.


I nterv al Co unt : The number of intervals (speci ed in the interval property) between subscription billings. For example, I nterv al = “Month” and I nterv al Co unt = “3 bills every 3 months.”
A mo unt : This is the amount to be charged. Do not use this eld if you have more than one Tier.
A ggregate U sage : Only for Usage-based prices. The usage is calculated at the end of the interval.
Billing Sc heme : If set to “Tiered,” you need to set Tiers for the Price
T iers Mo de : In volume-based tiering, the maximum quantity within a period determines the per-unit price. In graduated tiering, pricing can successively change as the quantity grows.
T rial P erio d Day s : Default number of trial days when subscribing a customer to this price.


Create a New Stripe Price Record
This example uses the minimal requirements to create a new Stripe Price record.

1. Create a new Stripe Price record.
2. Set the Stripe P ric e Name , Currenc y , and I nterv al properties.
3. Optional—Add a name to Stripe Name to use as a nickname alongside the Stripe P ric e Name . This allows for up to 255 characters to be referenced, while the Stripe P ric e Name can only utilize 80 characters.
4. Select a P ro duc t . (The P ro duc t must already be in Stripe.)
5. Set the Billing Sc heme .
6. Check A c tiv e .
7. Click Save.
8. Click Push to Stripe.

Prices may only be created for Products (Product2) with T y pe set to “Service.” If the Product has T y pe set to “Good,” a validation error will occur.


Disable Validations
To prevent the validation from ring before data is pushed to Stripe, use the Disable P lan Stripe V alidatio n eld in the “Blackthorn Pay – Trigger Settings” custom setting.

1. Go to Setup.
2. In the Quick Find box, enter and click “Custom Settings.”
3. Click Manage next to “Blackthorn Pay – Trigger Settings.”
4. Click Edit.
5. Check the Disable P lan Stripe V alidatio n checkbox.
6. Click Save.

Additional validations will be executed, and you will get an error message if something went wrong. If the P ric e I D eld is populated, the Stripe Price is pushed to Stripe and ready to use. You can also pull existing Stripe Prices from Stripe, using the Sync feature on Payment Gateway.


Stripe Price Tiers
Tiered prices must have Tier records. You need to create Tier records before pushing the Stripe Price to Stripe.


Minimal Requirements for Tiers
A Tier must have a value in either the Flat A mo unt or U nit A mo unt eld.
A Tier must have an U p T o property, which speci es the upper bound of the Tier, which is inclusive.
A tiered Stripe Price must have at least two Tiers
The last tier should be open-ended, and the U p T o eld left blank.

Both licensed and metered Stripe Prices can be tiered.


Tier Pricing Example
A Stripe Price has three Tiers:

0-10, Flat Amount $100
0-100, Unit Amount 1
100 - null, Unit Amount 0.5

In this case,

A Subscription with Quantity = “15” will be billed as $105 (100 + (5*1))
A Subscription with Quantity = “25” will be billed as $115 (100 + (15*1))
A Subscription with Quantity = “200” will be billed as $240 (100 + (90*1) + (100*0.5))


Update a Stripe Price
After pushing the Stripe Price record to Stripe the rst time, only the Stripe Name (nickname in Stripe) and A c tiv e elds can be updated. Any updates to those elds will automatically sync to Stripe after saving the Stripe Price record.


Push to Stripe Checkbox
Instead of using the Push to Stripe button, you can use the Stripe Prices’ P ush to Stripe checkbox. When the eld is checked, the data on the Stripe Price record will be pushed to Stripe.

Once the operation is complete, the Stripe Price P ric e I D eld will be populated.

NOTE: You may need to add the P ric e I D eld to the Stripe Price’s page layout.


Considerations
Do not use the checkbox in an asynchronous context, as the trigger starts a future method. If you need to use the checkbox in a future or batch context, complete the following steps.


Update Change Data Capture

1. Go to Setup.
2. In the Quick Find box, enter and click “Change Data Capture.”
3. Locate “Enable Price” (bt_stripe__Plan2__c), and move it to the Selected Entries column.
4. Click Save.


Update Custom Settings

1. Go to Setup.
2. In the Quick Find box, enter and click “Custom Settings.”
3. Click Manage next to “Blackthorn Pay - Trigger Settings.”
4. Click Edit.
5. Check Disable P lan_P ushT o Stripe .
6. Click Save.

Now, the P ush T o Stripe checkbox will work in an asynchronous context.

NOTE: If you run the insert Price operations in batch, set your batch size to around 30. You will need to consider the time limits as well as the callout limits.


Subscriptions & Subscription Items
Subscriptions are the life blood of Stripe Billing! The initial creation of one can be simple, using just the Subscription object, or more thorough, using both Subscription and Subscription Item.

Use only the Subscription object if your Subscription has just one Stripe Price. Subscription has elds for Stripe Price, quantity, and other single-price related elds. After pushing to Stripe, a Subscription Item will be auto-created for the single Stripe Price and updated in Salesforce.

Use both Subscription and Subscription Item if your Subscription has more than two Prices. Each Subscription Item represents one Stripe Price. If you're used to Opportunity and Products, it's the equivalent of having more than two Opportunity Products.

When creating a Subscription, ll out all applicable initial elds before pushing it to Stripe. If there are multiple Subscription Items, create each one then navigate to the Subscription and click the Push to Stripe button.


Create a Subscription
These are the minimal requirements.

1. Create a new Subscription record by navigating to the Subscription object and clicking New.
2. Set Rec o rd T y pe to "Subscription." (The "Subscription Schedule Phase" Rec o rd T y pe is used with the Subscription Schedule object.)
3. Set the P ric e eld if there is only one Price. Setting the P ric e will automatically set the Product look up.

4. Select a Custo mer . The Custo mer is the Payment Gateway Customer to be used (required by Stripe). The email address of this Stripe Customer will be the recipient of the invoices sent with each billing.
5. Populate the Quantity      eld. Optional: Populate the Memo eld so it is included in invoice PDFs, invoice emails, and the Hosted Invoice Page.
6. Click Save.
7. Click Push to Stripe. You'll know the Subscription was successfully created in Stripe if you see the Subsc riptio n I D eld populated.

As a convenience feature, the P ay ment Metho d will be populated with the Customer's default source (i.e. their card or ACH account).


Subscription Fields
P ric e : The price of the item the customer subscribes to.
Custo mer : The subject of the Subscription.
P ay ment Metho d : If left blank, the default will be used.
Enable P ay ment Metho ds : You can choose which payment methods will be available to pay for a Subscription when an invoice is issued. The following Values are available to choose from: ACH Credit (pushed by them), ACH Debit (pulled by you), Canadian pre-authorized debit, BECS Direct Debit, Bacs Direct Debit, Bancontact, Boleto, Card, EPS, FPX,
iDEAL, Przelewy24, SEPA Direct Debit, and Wechat Pay.
Subsc riptio n Name : You can set an arbitrary name for reference; if left blank, populated automatically.
Quantity : The quantity of the items subscribed to. Leave blank for metered prices.
Billing Cy c le A nc ho r (First I nv o ic e) : Determines the date of the rst full invoice, and, for prices with Month or Year intervals, the day of the month for subsequent invoices. If not left blank, the rst invoice will be prorated.
Billing Metho d : When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions.
Day s U ntil Due : Number of days a customer has to pay invoices generated by this Subscription. This value will be null for Subscriptions where Billing Metho d = "Charge Automatically."
U pc o ming I nv o ic e A mo unt : This eld will auto-populate with the upcoming invoice amount from Stripe.
P ro ratio n Behav io r : Determines how to handle prorations when the billing cycle changes (e.g., when switching plans, resetting billing_cycle_anchor=now, or starting a trial), or if an item’s quantity changes. When editing a Subscription record you can use "Send Invoice" if you want the customer to immediately pay the price difference when switching to
a more expensive subscription on the same billing cycle. See the Stripe Docs for more detail.


Proration Behavior Update

If a Stripe Billing Subscription P ro ratio n Behav io r = “--None--” or is left blank, any changes made to the Subscription will no longer be prorated.


Not Seeing a Picklist Value?

1. Check that you have installed the latest Payments package.
2. Navigate to Blackthorn | Payment Admin > Upgrades > Click Add Picklist Values.


Subscription Date Fields
Trial End : Set this eld on creation if you want your billing to begin at a future date. Not a backdated date. If set, the rst full interval invoice is created for zero dollars, and the rst dollar amount invoice is created at the end of the trial. Payment Source is not a required criteria in order to create the Subscription

Backdate Start Date : If the subscription started in the past, set this date on subscription creation. This eld does not effect billing and is for historical purposes, unless proration handling is invoked. See more information here on backdating.

Billing Cycle Anchor (First Invoice) : If your invoicing should occur on a certain date, set this value, and it will override the trial-date invoicing. Just be mindful of setting or not setting proration. See more information about prorating here. If you want to reset this date post-subscription creation, use Reset Billing Cycle Anchor .


The rest of these elds are not editable from Salesforce and are set automatically after subscription creation. Trial Start , Start , Date Ended , Current Period Start , Current Period End , Processed Date (Created) .


Update a Subscription
You can update a Subscription record if it is already pushed to Stripe. If you edit any of the below elds after the Subscription is already in Stripe, Salesforce will update the Stripe Subscription in real-time upon saving. The following elds are updatable:

Quantity : Can be updated only if there is only one Subscription Item.

Price : Can be updated only if there is only one Subscription Item.

Payment Method : Updates the Source which is used for the Subscription

Coupon : You can add a Coupon. If you delete the eld, the Coupon is removed.

Billing Method

Days Until Due : only if Billing Method is set to 'Send Invoice'.


Subscription Update Limitations

If a Subscription eld is NOT added to the list above that means you will not be able to use it to update a Subscription record. Some examples might include the elds Pending Invoice Item Interval and Pending Invoice Item Interval Count .


Subscription Items
One Subscription can have more than one Stripe Price. In this scenario, instead of setting the Price      eld on Subscription, create separate Subscription Item records. You need to create Subscription Items before pushing the Subscription. Also note that if you are setting the Stripe Price and Quantity on the Subscription during creation, a Subscription Item will be
created automatically using these parameters (as referenced at the top of this page).


When adding a One-Time Price as a Subscription Item to an existing Subscription record, the additional Subscription Item will sync to Stripe as an Invoice Item and be added to the next Invoice generated by the Subscription.


Update Subscription Items
You can update existing Subscription Items with the below elds. This will trigger updates to the Stripe Subscription and invoke upgrade, downgrade, credit, and prorate logic.

Quantity : Once changed, updates to the Stripe Subscription will be made.

Price : Changing the Price on the Subscription / Subscription Item is no longer possible as the change isn't accepted/re ected in the Stripe Billing Dashboard. Please follow the steps below to update the Price .

1. Make a new Stripe Price.
2. Create a new Subscription Item.
3. Delete the old Subscription Item.
4. Click Push to Stripe .
5. Click Save in Stripe .
6. Click Return to Record .

7. Click the Stripe URL to con rm the change.


Delete Subscription Items
If you delete a Subscription Item record, it is deleted in Stripe as well. You can't delete the last Subscription Item record, so at least one Item should stay on the Subscription.


Restrictions
On a Subscription every product can be included only once; i.e. Stripe Prices with the same Product are not allowed
Stripe Price Interval and Interval Count should be matched. For example, you cannot include a weekly and a daily Stripe Price on the same Subscription


Pausing a Subscription
In Stripe you have the ability to pause a subscription when you need to stop payments for a period of time. We've added a couple elds to the Subscription object that track those updates with webhooks. You will not be able to pause a subscription from Salesforce and send to Stripe. These elds only update based on changes in Stripe. More details on pausing
a payment collection in Stripe can be found here .

Paused? will be checked if a user has paused the subscription in the Stripe dashboard.

Resumes At is a date/time eld that will be updated with the value the user sets in the Strip dashboard to resume subscription payments.

Paused Invoice Behavior : If a Subscription record is paused this eld could be populated with one of the three following values: "Keep As Draft", "Mark Uncollectible", or "Void".
Note: You will need to add these elds to your Subscription page layout.


Subscription validations before syncing with Stripe


W hen                                                                                                                                                                        Error Message
No customer lookup set                                                                                                               No Customer on the Subscription.
No Payment gateway set                                                                                                               Please de ne payment gateway on the Customer.
Billing Method = Send Invoice, but no Payment Method added for the customer                                                          In order to create invoices that are charged automatically, the Customer must have a Payment Method. Add a Payment Method or select Send Invoice.
Billing Method = Send Invoice, but customer email blank                                                                              In order to create invoices that are sent to the customer, the customer must have a valid email.
Payment Method status not valid/veri ed                                                                                              The Customer's Payment Method is not Valid or Veri ed.
Billing Method = Send Invoice, but Days until due blank                                                                              If the Billing Method is Send Invoice, the Days Until Due eld should be set.
No price/ subscription item added                                                                                                    No Items or Prices are on the Subscription.
Date of Billing Cycle Anchor is <= Today.                                                                                            The Billing Cycle Anchor (First Invoice) date needs to be in the future. Please update the date and try again.
If we are trying to update the value of Billing cycle Anchor after pushing the subscription to Stripe. (this is set only one time)   You can change a Subscription’s Billing Cycle by setting a Trial End Date. As a reminder, you probably want to also set Prorate to False so the customer is not credited for previously paid, but unused time.
Trying to update the Trial end date in past after pushing to Stripe                                                                  The Trial End Date needs to be a future date.
If Payment Method for ACH on subscription not validated/veri ed                                                                      The customer’s payment method is not valid or Veri ed.
Attempting to set Proration Behavior = "Send Invoice" on the initial push to Stripe.                                                 You can't use Send Invoice proration behavior for a new subscription.


Subscription Schedules
A Subscription Schedule allows you to create and manage the lifecycle of a Subscription by pre-de ning expected changes. These changes can include updates to the Subscription’s prices that are scheduled to automatically occur in the future.


Upgrade Your Org to Use Subscription Schedules
After upgrading to the latest Payments package that includes Subscription Schedules, the Subscription object will have two new Rec o rd T y pe options: "Subscription" and "Subscription Schedule Phase." To use these record types properly, follow the steps below.

1. Update the existing Subscriptions to the new "Subscription" Rec o rd T y pe .
a. Navigate to Blackthorn | Payments Admin tab.
b. Click the Stripe Billing tab.
c. Click the Assign Subscription Record Type button.
2. Add the Subscription Schedule Phase layout to the "Subscription Schedule Phase" Rec o rd T y pe and assign the two Subscription record types to pro les.
a. Navigate to the Blackthorn | Payments Admin tab.
b. Click the Stripe Billing tab.
c. Click the Deploy Stripe Billing button.


New Orgs

Customers installing Blackthorn Payments for the rst time will notice the new object for Subscription Schedule and 2 new record types for Subscription once installation is complete.


Create a Subscription Schedule

Not Seeing Subscription Schedules?

Make sure you have upgraded to Payments v5.1 or higher.


1. Navigate to the Subscription Schedule object and click New to create a new record.
Note: The elds on the Subscription object are here as well.
2. Add a value in the Custo mer eld.
Note: This is the only required eld.
3. Click Save.


Cancel the Subscription Schedule

Complete the following steps to cancel the Subscription Schedule.

1. Go to the Subscription Schedule record.
2. Open the navigation bar.
3. Click Cancel/Release Schedule.


Create the Subscription Schedule Phase
A Subscription Schedule Phase is one of the record types related to the Subscription object. Previously, the Subscription object only had one record type. Now it will have two: Subscription and Subscription Schedule Phase.

1. Navigate to the Subscription Schedule Phase Related List on Subscription Schedule and click New.
2. Set Rec o rd T y pe = .
3. Add P ric e if there is only one price for this Subscription. If there are multiple Stripe Prices, you should use Subscription Items.
4. Select a Billing Metho d .
5. Populate I teratio ns with the number associated with this phase. Is this the rst iteration or the second, third, and so on.
6. Select a date for the Date Ended eld. This will signify the end of this Subscription Schedule Phase.
7. You can add additional detail using the other elds on this record, but they are not required.
8. Click Save.


Add Subscription Items
You only need to do this if you have more than one Stripe Price.

1. Navigate to the Subscription Item Related List on the Subscription Schedule Phase you just created.
2. Click ‘New.
3. Add values to the Quantity , P ric e , and P ro duc t elds.
4. Click Save.


Usage

Creating Usage Based Billing
Create a Stripe Price where Usage Type is set to "Metered". Using the Aggregate Usage         eld you can set the summing up behavior (see Price documentations for details).
Create a Subscription using this Stripe Price. Quantities on a Subscription using a Metered Price can't be set.
Push the Subscription to Stripe.
Navigate to the Subscription Item on the Subscription related list. Select a Subscription Item.
Create a related Usage record on the related Usage list.
Set the Quantity     eld.
Save the record.
You should see the Usage ID        eld populated after a few minutes.


Stripe Checkout
Stripe Checkout is a solution prepackaged from Stripe. We've added an integration so users will be able to utilize its functionality right from Salesforce. Read more about Stripe Checkout here.


Prerequisites
1. Contact Blackthorn Support to share your org ID. Support will use it to enable Stripe Checkout from the backend. This applies to both Sandbox and Production.
2. The PayLink package must be installed and con gured in your org. Use the Payments Setup Wizard to install PayLink if you haven't already.
3. Stripe Checkout must be used with Payment Gateways with the P ro v ider set to "Stripe".


Con gure PayLink

Add Stripe Checkout to the PayLink Con guration Object
1. Navigate to the PayLink Con guration object in Setup.
2. Click the Fields and Relationships tab.
3. Click the link for the A llo wed P ay ment Metho ds eld.
4. Go to the Values section.
5. Click New.
6. Add "Stripe Checkout" to the text box.
7. Click Save.


Set the Value on the Paylink Con guration Record
1. Navigate to the Paylink Con guration record that you will use for your Stripe Checkout Transactions.
2. Click Edit (the pencil icon) next to the A llo wed P ay ment Metho ds eld.
3. Move "Stripe Checkout" to the Chosen column.
4. Click Save.


Con gure the Payment Gateway

Update Your Page Layout
1. Navigate to the Payment Gateway object in Setup.
2. Click the Page Layouts tab.
3. Click the Payment Gateway Layout link.
4. Add the A c c epted Chec k o ut P ay ment Metho ds eld to the Page Layout.
5. Click Save.


Set Values on the Payment Gateway Object
1. Navigate to the Stripe Payment Gateway that will be used for Stripe Checkout.
2. Select your required values for the following elds.
Def ault Currenc y
Def ault Co untry
3. Edit the A c c epted Chec k o ut P ay ment Metho ds eld to include the Payment Method to be used for Stripe Checkout. The supported payment method types for Stripe Checkout are here.

NOTE: Stripe updates this list periodically.

Payment Method Limitations: Certain payment methods like Sepa Debit only work with certain currencies (EUR). Check out this payment method fact sheet to review the limitations of each payment method type.


Add Permissions to Access Encrypted Data
1. Go to Permission Sets in Setup.
2. Click New.
3. Enter "Access Encrypted Data" in the Label eld.
4. Click Save.
5. Navigate to System Permissions.
6. Click Edit.
7. Check the V iew Enc ry pted Data checkbox.
8. Save the permission set.
9. Navigate to the user record in Setup for the person who authenticated the PayLink app. This is the person who clicked the Authenticate button while running the PayLink setup wizard.
10. Add the new permission set to their user record.


Assign the Proper Page Layout to the Corresponding Record Type
1. Navigate to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, enter and click "Payment Method."
4. Click the Page Layouts tab.
5. Click Page Layout Assignment.
6. Click Edit Assignment.
7. Set the P age Lay o ut to U se to "Other" and con rm that the "Other" column lists "Other" for each relevant pro le.
8. Click Save.


Setup Webhooks
If you haven't already setup webhooks in your org you'll want to do this. Stripe Checkout utilizes data that is brought into the org via webhooks. Related records like Payment Method and Payment Gateway Customer are attached to the Transaction AFTER the webhooks process.

Check out this guide for setting up Webhooks.


Enable SCA
If you are using Strong Customer Authentication (SCA) and Stripe Checkout with Events, you must also enable the SCA feature.

To enable SCA in your org, complete the following steps.

1. Click the Gear icon.
2. Click Setup.
3. In the Quick Find box, enter and click "Custom Settings."
4. Click Manage next to Blackthorn Pay - Trigger Settings.
5. Click Edit.
6. Set Enable SCA = "True" (checked).


7. Click Save.


Access Stripe Checkout from PayLink
1. Create a Transaction record.
2. At a minimum set the following:
A mo unt
P ay ment Gateway (Must be a Payment Gateway connected to Stripe)
P ay Link Co nf iguratio n (Must be the PayLink Con guration with Stripe Checkout set as an A llo wed P ay ment Metho ds .)
3. Click the PayLink URL populated in the P ay Link eld.


Complete a Stripe Checkout with PayLink
1. Wait for the PayLink page to load.
2. Click PAY.
3. Wait for Stripe Checkout to load.
4. Complete the Stripe Checkout form.
5. Observe the success page.
6. Observe the Paylink elds "Amount Paid" and "Paid on" are displayed.

Quick Help: If you aren’t redirected to Stripe Checkout after clicking PAY from the PayLink, you may need to reauthorize your Payment Gateway. Open the related Payment Gateway record and click Connect to Gateway.


Stripe Checkout Considerations

Existing Payment Methods
Currently, Payment Method records created in Stripe Checkout cannot be reused for additional Transactions or updated through Blackthorn.

This includes capturing an authorized one-time payment. We understand this does not create a new Transaction, but it does change the status of an existing one-time payment. Therefore, these are considered "one-time" Payment Methods, which can only be refunded through Blackthorn Payments.


Stripe Payment Method Types
The Payment Method object includes the T y pe eld, which identi es the payment method type used for Stripe Checkout. This eld differs from the Payment Method’s Rec o rd T y pe eld.

For example, say you use iDEAL to complete a Stripe Checkout transaction. After the Payment Method record is created and the webhook has been processed, you will see that the Payment Method’s Rec o rd T y pe = "Other" and T y pe = "Ideal."

Click here to see a list of Stripe-supported payment method types. We are working to incorporate most of the Stripe-supported payment method types into our solution; however, we will not support AfterPay / ClearPay.


Apple Pay and Google Pay
In order to see the option for Apple Pay or Google Pay in Stripe Checkout you must be viewing Stripe Checkout from a supported device. Discover more about wallets here.

Example: To view the Apple Pay button in Stripe Checkout you must be using an iOS device AND have your Apple Wallet con gured.


Currency Errors
If, while using Stripe Checkout, you encounter and error on the Transaction record that refers to currency there is a workaround available while we develop a long-term solution. Currently, only USD, EUR, and GBP are added to the package as values available on the Payment Intent object. You'll need to add values following the instructions below for any currency
outside of those values.


What you'll see on the Transaction record:

Erro r Message = "Insert failed. First exception on row 0; rst error: INVALID_OR_NULL_FOR_RESTRICTED_PICKLIST, Currency: bad value for restricted picklist eld: cny: [bt_stripe_Currency_c]"
Erro r P arameter = "The Transaction/Payment Intent was captured in Stripe but failed to save correctly in Salesforce."

The above errors were displayed when attempting to use Stripe Checkout with the AliPay Payment Method T y pe and a Transaction with the Currenc y I SO = "CNY".

How Do You Resolve?
You'll want to add the desired currency value to the Currenc y picklist on the Payment Intent object.

1. Navigate to Setup -> Object Manager -> Payment Intent -> Fields & Relationships -> Currency.
2. Click New in the Values section.
3. Add the Currenc y value to the list of picklist values. (ex: "CNY")
4. Click Save.


Stripe Metadata

Stripe To Salesforce Mapping

Introduction
Blackthorn Payments now retrieves all Metadata values from Stripe for Payment Gateway Customer, Payment Method, Transaction, Payment Intent, and Subscription objects. The Stripe Metadata Structure can hold 50 keys, with key names up to 40 characters long and values up to 500 characters long for a total of 27,000 characters.

Blackthorn Payments stores the Stripe Metadata in a long text area eld named bt_stripe__Metadata__c on each supported object. The Metadata is stored in JSON format and can easily be converted to a key-value map in Apex code to retrieve a value by key. The eld, Metadata__c, is not on object layouts, it must be added manually. The eld will populate via
Webhooks and the Sync feature on Payment Gateway records.

Bidirectional sync from Salesforce to Stripe is available. Blackthorn Payments sets some Salesforce record Ids in the Stripe Metadata eld and also support pushing custom key and values from Salesforce to Stripe.


Sample Use Cases
Here are some uses cases for Metadata in Stripe getting pulled into Salesforce:

1. Store keys or ids from other systems in the Stripe Metadata eld and set them on a custom eld on a Salesforce record.
2. Use the Stripe metadata eld store additional customer details and parse it so set elds on the Contact in Salesforce.
3. Store information about why a refund was created, and by whom in a custom eld on your refund transaction if any.


Example of Stripe Metadata on the Customer object (which syncs to our Payment Gateway Customer object in the eld Metadata)


Example Payment Gateway Customer record in Salesforce displaying the Stripe metadata


Here is sample trigger code that gets a values by key from the Metadata eld on Transaction. This is useful if you want to save a value for a known key on a custom eld on the Transaction or on a related record.


Plaintext                                                                                                                                                                                                                                                                                                                                                    Copy

trigger MetadataParse on bt_stripe__Transaction__c (after insert after update) {
for (bt_stripe__Transaction__c tra : Trigger.new) {
if (String.isNotBlank(tra.bt_stripe__Metadata__c)) {
Map<String,String> metadataMap = (Map<String,String>)
JSON.deserialize(tra.bt_stripe__Metadata__c, Map<String,String>.class);

// now access the metadata element using the keys & add your business logic here
String value = metadataMap.get('key');

tra.Donation_Id__c = metadataMap.get('donation_id'); //e.g. dnt_89660b7daed7, Give Transaction


//Boolean
tra.Campaign__c = metadataMap.get('campaign')=='true'? true :false; //e.g. true/false
}
}
}


Salesforce To Stripe Mapping
Blackthorn Payments now supports the ability to con gure the Salesforce eld/data to be mapped to stripe metadata key/value for Payment Gateway Customer, Payment Method, Transactions, Sales document, and Subscription objects.


Introduction
1. Install the latest payments package version 4.151 and above.
2. Con gure the custom metadata mappings in Salesforce using the Source Object and the source Field.
3. De ne a Metadata Key for the source eld.
4. Send a record from Salesforce to see the metadata in Stripe


Setup Steps
1. Go to Setup > Custom metadata Types > Stripe Metadata Mapping > Manage Stripe Metadata Mappings > New.
2. Enter a Label, Stripe Metadata Mapping Name, Metadata Key, Source object, Source eld and Save. (Edit the Layout to include these elds if not already present)


Example Stripe Metadata Mapping


3. Create a new Payment Gateway Customer record in Salesforce and de ne the Billing Country and gateway.


4. You will see the Stripe API response populated in the metadata eld on the record.


If you wish to map multiple elds of one source object, please create a new mapping for every eld.


Stripe Radar Integration
If you enabled Stripe Radar features on your Stripe account, the results are automatically mapped to the Transaction records in Salesforce.


Enable in Salesforce
Navigate to Setup | Custom Settings | Blackthorn | Payments Triggers and click the Manage button
Click Edit
Check the Enable Stripe Radar checkbox and save


Set the Transaction Fields on Layouts
Navigate to Transaction layout edit page and add the Radar-related elds to the layouts, which are the following: Risk Level , Risk Score , Network Status , Seller Message


Test Data
When setting up Blackthorn Payments, we suggest you connect your Payment Gateway in Test Mode so that you can create test Transactions, Payment Methods, and Customers.

In order to create successful test records in Salesforce, you must use the card and ACH numbers below and process through a Test Mode connected Payment Gateway.


Stripe

Test a Stripe Card

Warning
Actual card and bank account information cannot be used in Test Mode.


1. Con rm that the Payment Gateway has T est Mo de set to "TRUE".


2. Go to the Payment Method tab and click New.
3. Select "Card" and click Next.


4. Using the information provided below, complete the following elds.
Ho lder's Name = use any name
Number = “4242424242424242”
Ex piratio n Mo nth = use any month
Ex piratio n Y ear = use any year
CV V = use any 3-digit number
P o stal Co de = use any 5-digit number
P ay ment Gateway = the Payment Gateway you just set up
5. Click Save.

This Payment Method is now valid and can be used to capture and refund Transactions.

NOTE: Additional card numbers can be found in Stripe's testing documentation.


Test a Stripe ACH Bank Account

Warning
Real card and bank account information cannot be used in Test Mode.


1. Con rm that the Payment Gateway has T est Mo de set to “TRUE”.


2. Go to the Payment Method tab and click New.
3. Select "ACH" and click Next.


4. Use the data below to test either a successful or failed payment.
Successful Payment Method
Ho lder’s Name = Use any name
A c c o unt Number = “000123456789”
Ro uting Number = “110000000”
A c c o unt Ho lder T y pe = Choose either option
Currenc y I SO = “USD”
Co untry I SO = “US”
Failed Payment Method
Ho lder’s Name = Use any name
A c c o unt Number = 000111111116
Ro uting Number = 110000000
A c c o unt Ho lder T y pe = Choose either option
Currenc y I SO = “USD”
Co untry I SO = “US”
5. Click Save.

This Payment Method is now valid and can be used to capture and refund Transactions.


Test for Speci c Responses and Errors
Use the test cards below to create a Payment Method that produces a speci c response.


Incorrect CVC Code Error
Use this number to create an error about an incorrect CV V . The error message will be in the Stripe data elds.

Number = 4000000000000127


Fail to Capture
This number will create a valid Payment Method, but when you capture a Transaction with the Payment Method, the Transaction will fail. The error message will be in the Stripe data elds.


Number = 4000000000000341

Additional testing for speci c responses and errors can be found here.


Disputes
Use the card below in test mode to simulate a disputed Transaction. This number will create a valid Payment Method, but when you capture a Transaction with the Payment Method, a Dispute record will be created.

Number = "4000000000000259"


Test a Winning a Dispute
Enter the words "winning_evidence" in the A dditio nal I nf o rmatio n eld on the Dispute Evidence record to simulate the dispute being won and the funds being returned to your account as an adjustment Transaction.


Test a Losing a Dispute

Enter the words "losing_evidence" in the A dditio nal I nf o rmatio n eld on the Dispute Evidence record to simulate the dispute being closed and marked as lost. (Your account will not be credited.)

Click here for more information about Disputes.


Delete Test Data
1. Navigate to your Stripe Dashboard.
2. Toggle "ON" the V iew test data switch. (left-hand column).
3. Click Business settings. (left-hand column)
4. Select "Data".
5. Next to Test data, click Delete all test data.
6. Click Delete Now.


Salesforce

Whether you are in a Production or Sandbox Org, you will need to temporarily deactivate all triggers so that you can delete Transaction, Payment Method, and Payment Gateway Customer records.

1. Navigate to Custom Settings.
2. Click Manage next to Blackthorn - Pay Trigger Settings.
3. Click Edit.
4. Check the Disable A ll T riggers checkbox.
5. Click Save.
6. Delete all of your test data.
7. Navigate back to Custom Settings and UNCHECK Disable A ll T riggers .


Authorize.net
Test your Authorize.net Payment Gateway using either the test Authorize.net card or the test Authorize.net ACH bank account.


Test an Authorize.net Card

Warning
Actual card and bank account information cannot be used in Test Mode.


1. Con rm that the Payment Gateway has T est Mo de set to “TRUE”.


2. Go to the Payment Method tab and click New.
3. Select Card and click Next.


4. Using the information provided below, complete the following elds.
a. Ho lder’s Name = use any name
b. Number = “4111111111111111”
c. Ex piratio n Mo nth = use any month
d. Ex piratio n Y ear = use any year
e. CV V = use any 3-digit number
f. P o stal Co de = use any 5-digit number


g. P ay ment Gateway = the Payment Gateway you just set up
5. Check the Payment Gateway’s Enable A utho rize.Net CCV Filter eld if you want to require users to re-enter the CVV code for the card they are using.
6. Click Save.


This Payment Method is now valid and can be used to capture and refund Transactions.

For more information about testing Authorize.net Payment Gateways, click here.

NOTE: Additional card numbers can be found in Authorize.net's testing documentation.


Test an Authorize.net ACH Bank Account

Warning
Real card and bank account information cannot be used in Test Mode.


1. Con rm that the Payment Gateway has T est Mo de set to “TRUE”.


2. Go to the Payment Method tab and click New.
3. Select A CH and click Next.


4. Using the information provided below, complete the following elds.
a. Ho lder’s Name = use any name
b. A c c o unt Number = “000123456789”
c. Routing Number = “122105812”
d. A c c o unt Ho lder T y pe = either option
e. Currenc y I SO = “USD”
f. Co untry I SO = “US”
5. Click Save.

This Payment Method is now valid and can be used to capture and refund Transactions.


Test for Speci c Responses and Errors

Cards

Create a Payment Method using the following postal codes to generate a declined Transaction.

P o stal Co de = "46282" - This Transaction will be declined.
P o stal Co de = "46205" - The Transaction will be declined because of an AVS mismatch. The address provided does not match the cardholder's billing address.


ACH
To generate a decline using an ACH bank account, submit a Transaction over $100.


Duplicate Payment Methods
Create two Payment Methods with the same name and email address to generate "A duplicate record with ID [auth.net id] already exists error" for the second Payment Method.


Spreedly
Test your Payment Gateway using either the test Spreedly card or the test Spreedly ACH bank account.


Test a Spreedly Card

Warning
Real card and bank account information cannot be used in Test Mode.


1. Con rm that the Payment Gateway has T est Mo de set to “TRUE”.


2. Go to the Payment Method tab and click New.
3. Select Card and click Next.


4. Using the information provided below, complete the following elds.


Ho lder’s Name = use any name
Number = “4111111111111111”
Ex piratio n Mo nth = use any month
Ex piratio n Y ear = use any year
CV V = use any 3-digit number
P o stal Co de = use any 5-digit number
P ay ment Gateway = use the Payment Gateway you just set up
5. Click Save.


This Payment Method is now valid and can be used to capture and refund Transactions.

For more information about testing Spreedly Payment Gateways, click here.


Spreedly and ACH Bank Account Limitation

Blackthorn does not support webhook callbacks for gateways that are con gured through Spreedly. As a result, Blackthorn does not recommend submitting ACH payments via Spreedly.

If an ACH payment is submitted via Spreedly, users must check their gateway to see if the payment is complete. Users cannot con rm if the payment was successful by going to Salesforce.

If you do use ACH payments with Spreedly, please proceed with caution.


Test a Spreedly ACH Bank Account

Warning
Real card and bank account information cannot be used in Test Mode.


1. Con rm that the Payment Gateway has T est Mo de set to “TRUE”.


2. Go to the Payment Method tab and click New.
3. Select A CH and click Next.


4. Using the information provided below, complete the following elds.
Ho lder’s Name = use any name
A c c o unt Number = “9876543210”
Ro uting Number = “021000021”
A c c o unt Ho lder T y pe = either option
Currenc y I SO = “USD”
Co untry I SO = “US”
5. Click Save.

This Payment Method is now valid and can be used to capture and refund Transactions.

For more information about testing Spreedly Payment Gateways, click here.


PayPal

Test a PayPal Card

Limitation

Real card and bank account information cannot be used in Test Mode.


Use the following test card number to create a successful Payment Method and Transaction.


Number = "4755007800273033"
Ex piratio n Mo nth = "05"
Ex piratio n Y ear = "2022"
CV V = "105"


Transact (CashNet)
For testing purposes, create a Transact (Cashnet) Payment Gateway and use the following values.

Use the Transact (Cashnet) Payment Gateway with any Event and perform a normal (paid) checkout. You should be able to successfully complete the checkout process and perform failing checkouts that should be handled appropriately.

Use the following test card numbers:


Card Type                                                                                                                                                 Number                                                   CVV
Visa                                                                                                                                        4111111111111111
Mastercard                                                                                                                                  5454545454545454
American Express                                                                                                                            343434343434343


TouchNet
For testing purposes, create a TouchNet Payment Gateway and use the following values:

Field                                                                                                                                                                         Value
TouchNet UPay Site ID
TouchNet UPay Site URL                                                                                                 https://test.secure.touchnet.net:8443/C30002test_upay/web/index.jsp
TouchNet uPay Form Parameters                                                                                          DEPARTMENT=any

Use the TouchNet Payment Gateway with any Event and perform a normal (paid) checkout. You should be able to successfully complete a checkout as well as perform failing checkouts that should be handled appropriately.

Use the following test card numbers:

Brand                                                                                                Number                                                                            CVC/CVV                       Expiration Date
Visa                                                                                            4111111111111111                                                                                            125                              Any future date
American Express                                                                                343434343434343                                                                                             1250                             Any future date
Discover                                                                                        6011111111111117                                                                                            125                              Any future date
Mastercard                                                                                      5121212121212124                                                                                            125                              Any future date


Overview
The LWC Virtual Terminal is a versatile component that can be con gured in multiple ways to enable payment processing for your Salesforce and Experience Cloud users. You can create new or select existing Payment Methods and capture create, authorize capture, or schedule Transactions to auto-process on a speci ed date.

Compatible with Stripe, Authorize.net, and Spreedly (credit cards only), the LWC Virtual Terminal uses each supported gateway’s browse-side JavaScript library to collect payment details to maintain the highest level of PCI Compliance.

Best of all, the exible setup and con guration options allow you to create a tailored user experience that seamlessly integrates with your Salesforce business processes and self-service payments in Experience Cloud.

Pre-populate elds using Custom Metadata Types
Add custom elds using Field Sets
Show/Hide different actions and elements of the user interface (UI) using Custom Settings
Change labels using Custom Labels


Setup
The Virtual Terminal is supported for use on Lightning Record Pages, Experience Cloud Sites (both authenticated and un-authenticated), and in Screen Flows.

Click the link below to set up the Virtual Terminal for your speci c use case.


BT Payments Virtual Terminal
Lightning Record Pages

Custom Aura Legacy Component (Advanced)

Custom Component Scenario


BT Payments LWC Virtual Terminal
LWC Experience Cloud (Beta)

LWC Lightning Record Page (Beta)

LWC Screen Flow Component (Beta)


Lightning Record Pages

Coming in 2026: Deprecation of Aura Virtual Terminal Component

New Virtual Terminal con gurations should utilize our modern and feature-rich Lightning Web Component version. We plan to sunset the Aura Component and related Flow Screen Charge Component in 2026.


Don’t worry! Customers will receive advance notice of the sunset date to ensure a smooth transition.


The most common location for the BT Payments Virtual Terminal is on a Lightning Record Page. Follow the steps below to add the BT Payments Virtual Terminal to a Lightning Record Page.

1. Navigate to the Lightning Record Page where you want to place the BT Payments Virtual Terminal.
2. Click the Gear icon in the upper right-hand corner.
3. Click Edit Page to open the Lightning App Builder.
4. Scroll down to the Custom - Managed section in the Components sidebar.


5. Locate the BT Payments Virtual Terminal component in the list.
6. Drag and drop it onto the section, tab, or location of your choosing on the Lightning Record Page.


7. To ensure the BT Payments Virtual Terminal uses the correct record as the Parent Object, set the Rec o rd I d input to "{record.id}".


8. You can also add lters for component visibility if you want the BT Payments Virtual Terminal to only appear on a page when the speci ed criteria are met.
9. Click Save when you are done making the desired changes.

You can now make additional con gurations such as adding elds, pre-populating values, customizing labels, or further customizing the visible actions and defaults on the user interface.


Custom Aura Component (Advanced)

Coming in 2026: Deprecation of Aura Virtual Terminal Component

New Virtual Terminal con gurations should utilize our modern and feature-rich Lightning Web Component version. We plan to sunset the Aura Component and related Flow Screen Charge Component in 2026.


Don’t worry! Customers will receive advance notice of the sunset date to ensure a smooth transition.


Some customers have expressed the need for more exibility with the BT Payments Virtual Terminal. To address this need, users can create their own Aura Legacy Virtual Terminal component and add it where they see t. Inside the Aura Legacy Virtual Terminal component, users can pass in the following variables.

Rec o rd I d : This is the Id for the record that will load the component.
sObjec tName : This is the object type of the record that will load the component.
parentObjec tName : This is the name of the object used in the P arent Objec t eld.
parentI d : This is the Id associated with the record populated in the P arent Objec t eld.
c usto mRedirec t : Accepts values of “True” or “False”. Must be set to “True” to stop the default success popup.
disableCard : Accepts values of “True” or “False”. When set to “True”, the credit card form will NOT be displayed on the New Payment Method screen. Users will not see the credit card form on the + Add New option when clicking the P ay ment Metho d eld. Additionally, the stored Payment Methods with the Rec o rd T y pe = “Card” will not display as
a Payment Method that can be used for capturing Transactions.
disableA CH : Accepts values of “True” or “False”. When set to “True” the ACH form will NOT be displayed on the New Payment Method screen. Users will not see the ACH form on the + Add New option when clicking the P ay ment Metho d eld. Additionally, the stored Payment Methods with the Rec o rd T y pe = “ACH” will not display as a Payment
Method that can be used for capturing Transactions.
Mak e CV C Field Optio nal : If enabled, the CV C eld will be optional when adding a Payment Method.

To map the related Object, Id, or Amount elds use VT Mapping.


Experience Cloud
The following will occur when using the Aura Legacy Virtual Terminal with the Experience Cloud.

A newly created Payment Method’s P ay ment Gateway Custo mer eld will be updated with the existing Payment Gateway Customer when there is an existing Payment Gateway Customer record with the same email and Account used to create the new Payment Method.
The new Payment Method’s P ay ment Gateway Custo mer eld will be updated with a new Payment Gateway Customer record when there isn’t an existing one with the same email and Account used to create the new Payment Method.
Payment Methods added via the Virtual Terminal in the Experience Cloud will be added to the available Payment Methods for the related Account.
When a user logs into the Experience Cloud from a Contact record, the Virtual Terminal will display all available Payment Methods for the Account.


Custom Component Scenario

Coming in 2026: Deprecation of Aura Virtual Terminal Component

New Virtual Terminal con gurations should utilize our modern and feature-rich Lightning Web Component version. We plan to sunset the Aura Component and related Flow Screen Charge Component in 2026.


Don’t worry! Customers will receive advance notice of the sunset date to ensure a smooth transition.


1. Create a Lightning Component using the Developer Console.


2. Add a Name , select "Lightning Page" and "Lightning Record Page" in the Component Con guration section, and click Submit.


3. In the .cmp, add the following code, but replace the recordId and parentId with IDs from your org.

BT Payments Virtual Terminal Custom Component Sample


Plaintext                                                                                                                                                                                                 Copy

`<aura:component                         implements="flexipage:availableForAllPageTypes,flexipage:availableForRecordHome,
force:hasRecordId" access="global" >
<aura:handler name="chargeTransaction" event="bt_stripe:chargeTransaction"                                                                action="{!c.handleEvent}"/>
<bt_stripe:VirtualTerminal recordId="0035400000ewEgvAAE"
sObjectName="Contact"
parentObjName="bt_stripe__sales_document__c"
parentId="a0V540000020e7LEAQ"
disableACH="true">
</bt_stripe:VirtualTerminal>
</aura:component>`


4. Add a controller.js le if you would like to add an event handler.

Controller.js


Plaintext                                                                                                                                                                                                 Copy

`({
handleEvent : function(component, event, helper) {
var success = event.getParam("success");
var errorMessage = event.getParam("errorMessage");
var transactionId = event.getParam("transactionId");
console.log (' success ' , success);
console.log (' errorMessage ' , errorMessage);
console.log (' transactionId ' , transactionId);
}
})`


NOTE

Adding a javascript le like the one above can allow customers to pass in variables that can be used in ows to meet the needs of a business requirement.


5. Save your le.
6. Navigate to the record page where you want this custom component to live. (ex: Invoice)
7. Use the page editor to drag your custom component onto the page.


8. Click Save.

Now you'll have more exibility when using your own custom component.


LWC Experience Cloud (Beta)
Use the new LWC Virtual Terminal on any Lightning Experience Cloud page, including those with Guest User (unauthenticated) access.


IMPORTANT TO KNOW

The LWC Experience Cloud (Beta) does not enforce sharing rules.
A guest must be assigned the site guest user permission set.
Additional con guration for Account READ/WRITE and Contact READ/WRITE need to be assigned for relationship settings to work.
The related to lookup eld is not visible when enabled for a guest user.


Experience Builder Component
The LWC Virtual Terminal is in the Visualforce component in the Experience Builder.


If the user cannot see the LWC Virtual Terminal in the Experience Cloud Builder or receives an error, please refer to our FAQ guide here.


LWC Lightning Record Page


1. Find the LWC Virtual Terminal component in the list of Custom-Managed components.
2. Drag the component into the section of the page you wish to display it.
3. Set the Input Variables.
P ay ment Gateway I D : Record Id of the Payment Gateway you’d like the LWC Virtual Terminal to default to. If left blank, the component will use the default gateway of the org.
P ay ment Metho d I D : If you store a default Payment Method on a eld on the record, you can reference that eld here to ensure the terminal defaults to that P ay ment Metho d I D . Otherwise, the user can choose an available Payment Method from the list or create a new Payment Method to use.
A mo unt : Identify a eld on the underlying object you want to use to pre-populate the A mo unt eld in the LWC Virtual Terminal.
Currenc y : The value from the related Invoice's Currenc y I SO eld will automatically populate this eld. If the Invoice's Currenc y I SO eld is blank, the Virtual Terminal will use the Payment Gateway’s Def ault Currenc y value.
Desc riptio n : This can be a static message, or it can be mapped to a eld on the record. This also populates as the Desc riptio n of the Transaction created from a payment made in the LWC Virtual Terminal.
P ro c ess T y pe : Set the default P ro c ess T y pe of the component.
“Capture Now”
“Authorize Now”
“Auto-Process”
Hide A mo unt : Hides the A mo unt eld so a user cannot edit it manually.
Hide Currenc y : Hides the Currenc y       eld so a user cannot edit it manually.
Sho w A ddress : Displays the Billing Address elds for Payment Gateways with full billing address requirements.
Hide P ro c ess T y pe : Hides the P ro c ess T y pe eld so a user cannot manually change it.
Enable Lite V ersio n : A lightweight version of the LWC Virtual Terminal is available for quick entry of a new credit card and payment within the same page. Optimized for self-service and/or mobile experiences where surfacing existing Payment Methods may not be desirable.
Hide Bank T ab : If enabled, Bank details will be hidden from the list of available options when creating a Payment Method via the LWC Virtual Terminal.
Mak e CV C Field Optio nal : If enabled, the CV C eld will be optional when adding a Payment Method via the LWC Virtual Terminal.
4. Set Component Visibility (optional).
5. Click Save and navigate back to the record.


LWC Screen Flow Component
Drag and drop the LWC Virtual Terminal into a Screen Flow to create a seamless experience for your customers or internal Salesforce users.


With Screen Flows and the LWC Virtual Terminal, Admins and Developers can create an even more seamless payment experiences for Salesforce and Experience Cloud users with clicks instead of code.


NOTE

Custom Metadata Types and Custom Settings are not respected in the screen ow component.


1. Create a new screen ow.
2. Add a Screen Element and provide a Label.
3. In the Components tab scroll down to the Custom section.
4. Find LWC Virtual Terminal and drag the component to a section of the screen.
5. Con gure the following input variables.
A P I Name : This is how the component on this screen will be referenced in the rest of your ow.
A mo unt
Currenc y : The value from the related Invoice's Currenc y I SO eld will automatically populate this eld. If the Invoice's Currenc y I SO eld is blank, the Virtual Terminal will use the Payment Gateway’s Def ault Currenc y value.
Desc riptio n
Enable Lite V ersio n – Known issue affecting functionality.
Hide A mo unt
Hide Currenc y
Hide Bank T ab : If enabled, Bank details will be hidden from the list of available options when creating a Payment Method via the LWC Virtual Terminal.
Hide P ro c ess T y pe = "True"
Hide T ransac tio n Butto n : set to “True” to hide the Transaction button.
When the Transaction button is hidden, the ow’s Next or Finish button will trigger the Transaction processing logic. Upon completion, the T ransac tio n I D and Erro r Message , if any, will be available to the ow and can be mapped to variables for further processing. Once everything is complete, the ow will automatically navigate
to the next step or complete the process.
Mak e CV C Field Optio nal : If enabled, the CV C eld will be optional when adding a Payment Method via the LWC Virtual Terminal.
Parent Object A P I Name
P ay ment Gateway I D
P ay ment Metho d I D
P ro c ess T y pe = "Capture Now"
Record Id
Sho w A ddress
6. Set Component Visibility (optional).
7. Set Advanced settings (optional).


User Interface Con guration
Discover more granularity in the con guration settings when placing the Virtual Terminal component on any of the supported Salesforce declarative building tools.

Use the Blackthorn Payments | Virtual Terminal custom settings to tailor the user interface to create the optimal experience for your target user or audience.

Access Virtual Terminal Custom Settings
Manage Virtual Terminal Custom Settings
Add or Remove Virtual Terminal Fields


Manage Virtual Terminal Custom Settings

Hierarchical Structure
The Blackthorn Payments | Virtual Terminal custom settings are hierarchical. This means you can apply custom settings at the organizational level for all users, for speci c Salesforce users, or for users with speci c pro les.

Apply at the organizational level: click New above the “Default Organization Level Value” section.


Apply for speci c Salesforce users or users with speci c pro les: Click New in the lower section.


Access Custom Settings
1. Navigate to Salesforce Setup.
2. In the Quick Find box, search for and click “Custom Settings.”
3. Click Manage next to the Blackthorn Payments | Virtual Terminal custom setting.


Spreedly / Cybersource
Before using Spreedly with Cybersource to accept payments, the Virtual Terminal custom setting Sho w A ddress must be enabled. This ensures that the address elds (Street , City , State , and Co untry / Regio n ) will be visible on the Payment Method creation page in the Virtual Terminal.


Custom Settings

Dynamically Displayed Settings
The following con gurations for the LWC Virtual Terminal will by dynamically displayed.


Settings Applied at the (Global) Custom Setting Level

If Hide Card T ab = "True" (checked), the card tab will be hidden.
If Hide Card T ab = "False" (unchecked), the card tab will be shown.


Settings Applied at the Component Level

If Hide Card T ab = "False" (unchecked) on both the component and global level settings, the card tab will be shown.
If Hide Card T ab = False (unchecked) on the component level but Hide Card T ab = "True" (checked) on the global level, then the card tab will be hidden.
If Hide Card T ab = "True" (checked) on both the component and global level settings, the card tab will be hidden.


Con gurable Settings
Def ault New P ay ment Metho d : Sets the "New Payment Method" option as the default option on the Action menu.
Disable A mo unt : Prevents users from populating the A mo unt eld in the Virtual Terminal.
Disable New Charge : Removes the “New Single Charge" option from the Action menu.
Disable P ay ment Gateway : When enabled, this setting renders the P ay ment Gateway           eld as Read-Only. Note: The P ay ment Gateway      eld is only visible in orgs with multiple Payment Gateways.
Disable P ay ment Metho d Filter : When this is checked all the Payment Methods are loaded regardless of the Contact/Account set in the Virtual Terminal. This setting takes sharing rules into consideration. If a user does not have access to a Payment Method, they will not see it as an option in Virtual Terminal.
Disable Related T o : Makes the Related T o eld read-only.
Hide P arent : Removes the Parent Object eld from the Virtual Terminal.
Hide P ro c ess T y pe : Sets the P ro c ess T y pe selection to "Capture Now" and removes the picklist from the Virtual Terminal.
Hide Related T o : Removes the Related T o eld from the Virtual Terminal.
P ay ment Metho d Suc c ess Message : When a value is added to this setting, the value is used as the text in the success message box that appears when a Payment Method is created in the Virtual Terminal.
Related T o Def ault Objec t : The object added to this eld (Contact, Account, or Lead) will be the object that displays rst in the Related T o eld on the Virtual Terminal.
Sho w A ddress : Exposes additional elds to capture a full billing address when adding new Payment Methods.
T ransac tio n Suc c ess Message : When a value is added to this setting, the value is used as the text in the success message box that appears when a Transaction is captured in the Virtual Terminal.


Payment Option Features
Admins can control whether users see the ACH (Bank) and/or Card payment options on the Virtual Terminal’s New Payment Method screen.

Disable New Payment Methods
The Disable New P ay ment Metho d setting can remove the “New Payment Method” option from the Action menu.

When the Disable New P ay ment Metho d custom setting is set to “True” (checked) and either the Hide Card T ab or Hide Bank T ab is set to “False” (unchecked), the “New Payment Method” action will be hidden from the top action bar, but it will still be visible in the payment method dropdown list.

If the Hide Card T ab or Hide Bank T ab custom settings are set to “True” (checked), all “New Payment Method” actions are disabled.

Hide the Bank Tab
The Hide Bank T ab custom setting is accessed via the Blackthorn Payments | Virtual Terminal custom settings or the BT Payments LWC Virtual Terminal component settings page.

If Hide Bank T ab = “True” (enabled), the Bank tab will be hidden from the list of available Payment Method types when creating a Payment Method via the Virtual Terminal.
If Hide Bank T ab = “False” (disabled), the Bank tab will be visible.


Hide the Card Tab
The Hide Card T ab custom setting is accessed via the Blackthorn Payments | Virtual Terminal custom settings or the BT Payments LWC Virtual Terminal component settings page.

If Hide Card T ab = “True” (enabled), the Card tab will be hidden from the list of available Payment Method types when creating a Payment Method via the Virtual Terminal.
If Hide Card T ab = “False” (disabled), the Card tab will be visible.

The Hide Card T ab setting can be applied to both versions of the Virtual Terminal.


Limitation


A new Payment Method cannot be added via the Virtual Terminal when both the Hide Card T ab and Hide Bank T ab elds are enabled.


CVC Optional Feature
The Mak e CV C Field Optio nal setting allows users to make the CV C eld optional when adding a new credit card Payment Method in the Virtual Terminal. The default setting is for the CV C eld to be required.

If Mak e CV C Field Optio nal = “False”, the CV C eld is required.
If Mak e CV C Field Optio nal = “True”, the CV C eld is optional when adding a Payment Method via the Virtual Terminal.

The CVC Optional feature can be applied to the LWC and Aura Legacy Virtual Terminal versions at both the global level via the Blackthorn Payments | Virtual Terminal custom setting and locally at the LWC Virtual Terminal component level.


Exception


If your org has Custom Metadata Types for Virtual Terminal Mapping set, you'll need to manage those records since they can be in con ict with the Related T o Def ault Objec t setting.


Examples might include the following Virtual Terminal Mappings: SD.BillTo (Con) > Trans.ContactOppty.Account > TransAccount


If values are set in the T arget Field for the two mappings mentioned above, those values will take priority over the values you attempt to save in the Related T o Def ault Objec t custom setting.


CVV and Address Validation on an Authorize.net Gateway

The LWC Virtual Terminal supports CVV and address validation on an Authorize.net gateway when the Payment Gateway Liv e V alidatio n Mo de (A utho rize.net) (bt_stripe__Live_Validation_Mode__c) eld is enabled (checked). The validation only works with new and existing Payment Methods with the P ro c ess T y pe set to “Authorize Now” or “Capture Now.”

The A utho rize.net T ransac tio n Key   eld on the Payment Gateway supports the CVV and address validation by storing the Transaction Key, which is necessary to validate the CVV when charging a credit card.

“Auto-Process” Is Not Supported

The “Auto-Process” picklist value in the P ro c ess T y pe eld is not supported. Selecting the “Auto-Process” picklist option creates an open transaction that we cannot validate because Blackthorn does not store the tokenized card or the CVV. Please do not use the “Auto-Process” processing type.


Setup

1. Con rm that the Blackthorn Payments | Virtual Terminal Mak e CV C Field Optio nal custom setting is unchecked or required (default setting).
2. Add the Authorize.Net Transaction Key and Liv e V alidatio n Mo de (A utho rize.net) elds to the Payment Gateway layout.
3. Con rm the Liv e V alidatio n Mo de (A utho rize.net) eld is enabled (checked).
4. Con rm the Payment Gateway Enable A utho rize.Net CV V Filter eld is enabled (checked).


Generate a Transaction Key

1. Go to the Authorize.net Dashboard.
2. Click Account.
3. Click API Credentials & Keys
4. Select “New Transaction Key.”
5. Click Submit.


Functionality

The following scenarios will occur when the Payment Gateway's Enable A utho rize.Net CV V Filter eld is enabled, and the user is using the /LWC Virtual Terminal.

New Payment Method

P ro c ess T y pe = “Authorize Now”

A user selects the New Single Charge action, adds a new CARD Payment Method, and enters a billing address. If the P ro c ess T y pe = “Authorize Now” and the user clicks the Process button and enters the CVV code in the CVV con rmation modal, then the following will occur:

A Transaction is created in Authorize.net with status = AUTHORIZED
The address and CVV validations are displayed as MATCHED.
The Salesforce customer, Payment Method, and Transaction records are updated.

P ro c ess T y pe = “Capture Now”

A user selects the New Single Charge action, adds a new CARD Payment Method, and enters a billing address. If the P ro c ess T y pe = “Capture Now” and the user clicks the Process button and enters the CVV code in the CVV con rmation modal, then the following will occur:

A Transaction is created in Authorize.net with status = CAPTURED.
The Address and CVV validations are displayed as MATCHED.
The Salesforce customer, Payment Method, and Transaction records are updated.

Existing Payment Method

P ro c ess T y pe = “Authorize Now”

A user selects the New Single Charge action and an existing Payment Method. If the P ro c ess T y pe = “Authorize Now” and the user clicks the Process button and enters the CVV code in the CVV con rmation modal, then the following will occur:

A Transaction is created on Authorize.net with status = Authorized.
The Address and CVV validations are displayed as MATCHED.

P ro c ess T y pe = “Capture Now”

A user selects the New Single Charge action and an existing Payment Method. If the P ro c ess T y pe = “Capture Now” and the user clicks the Process button and enters the CVV code in the CVV con rmation modal, then the following will occur:

A Transaction is created in Authorize.net with status = CAPTURED.
The Address and CVV validations are displayed as MATCHED.


Add or Remove Virtual Terminal Fields
Adding, removing, and modifying elds on the Virtual Terminal is done through Field Sets. A Field Set is a grouping of elds that can be displayed on Lightning Components. A user can then add, remove, or rearrange elds from the Field Set, without altering the Lightning Component.


Limitation

Formula and auto-number elds cannot be added to the eld set.


ACH Direct Debit Mandate
The Virtual Terminal now supports ACH Direct Debit payment methods using Payment Intents with Stripe for enhanced NACHA regulation compliance.

Users are now required to give permission or a mandate to process charges against their bank account. Information about the permission will be stored in mandate elds.

What is an ACH mandate?
According to Stripe, the de nition of a ACH mandate is “a written notice of authorization to debit a bank account, agreed to by the customer before the rst debit.”

When collecting mandate details in the Virtual Terminal, the Statement Descriptor from your Stripe account (located under Settings > Public details) will be displayed in the mandate text.

You can read more about using ACH Direct Debits with Stripe here.


New Fields on the Payment Method Object
The following mandate elds have been added to the Payment Method object:

Field Label: Mandate A c c epted at
API Name: bt_stripe__Mandate_Accepted_At__c
Data Type: Date/Time
Description: The date/time that customer accepted mandate for ACH payment methods.
Field Label: Custo mer A c c eptanc e T y pe
API Name: bt_stripe__Customer_Acceptance_Type__c
Data Type: Text(7)
Description: Indicates whether the mandate acceptance was performed online or of ine.
Field Label: I P A ddress
API Name: bt_stripe__IP_Address__c
Data Type: Text(15)
Description: The IP address from which the mandate was accepted by the customer.
Field Label: U ser A gent
API Name: bt_stripe__User_Agent__c
Data Type: Text(255)
Description: The user agent of the browser from which the mandate was accepted by the customer.


The ACH (Bank Account) page layout was updated to include the new Mandate Data section where the new elds are visible.


Permission Sets
Blackthorn | Payments (User) and Blackthorn | Payments (Admin) permission sets have EDIT access to the elds.


Custom Setting
The Enable P ay ment I ntents f o r A CH P Ms custom setting was added to Blackthorn Pay - Trigger Settings. Enabling this setting allows users to send ACH payments through Stripe’s Payment Intents endpoint (ACHv2).

Complete the following steps to turn on the setting.

1. Go to Setup.
2. Enter and click “Custom Settings” in the Quick Find box.
3. Click Manage next to Blackthorn Pay - Trigger Settings.
4. Click Edit.
5. Set Enable P ay ment I ntents f o r A CH P Ms = “True” (checked).
6. Click Save.


How It Works
When the Enable P ay ment I ntents f o r A CH P Ms custom setting is enabled, users will see the mandate acceptance text in the Virtual Terminal if the selected ACH Payment Method does not already have the required mandate details. (i.e., the mandate elds are empty.)

Then, when a user charges a new or existing Stripe ACH Payment Method via the Virtual Terminal, the mandate details are recorded in the following elds on the new Payment Method record.

Mandate A c c epted at (date/time of acceptance)
Custo mer A c c eptanc e T y pe (online)
I P A ddress
U ser A gent (browser details)


Pre-Populate Fields
Map elds from the Transaction's Parent Object to the Terminal's Transaction screen using a Custom Metadata Type called, "Virtual Terminal Mapping."

Please make sure the elds mapped have the same eld type and property. For example, if you created a custom eld to prepopulate currency, make sure it matches the same format as the Currenc y I SO eld on the Transaction record.

Fields that can be prepopulated:

Related T o
P ay ment Metho d
Desc riptio n
A mo unt
Currenc y
Email
Ho lder's Name (Note: This is for credit card Payment Methods only.)
Custom Fields

Navigate to Custom Metadata Types
Virtual Terminal Transaction Con guration
New Record Screen


Navigate to Custom Metadata Types
1. Navigate to Setup.
2. In the Quick Find box, type "Custom Metadata Types".
3. Click Custom Metadata Types.
4. Click Manage Records next to Virtual Terminal Mapping.
5. Click New.
6. Add values to the following elds.
V irtual T erminal Mapping Name : This is the API name for the record. The API name can only contain underscores and alphanumeric characters. It must be unique, begin with a letter, not include spaces, not end with an underscore, and not contain two consecutive underscores. For example, "opp_amount."
Label : This is the label for the particular prepopulating record. For example, use "Opp > Trans Amount" for the label if you are prepopulating the A mo unt eld.
Sc reen : Single Transaction. Use the Related To screen for prepopulating the Related T o eld on the Terminal's Transaction screen. See example here.
So urc e Objec t : Select the Parent Object. For example, the Opportunity Object.
So urc e Field : Select the eld you want the value to come from. For example, if you want to prepopulate the Terminal's Transaction A mo unt with the Opportunity's A mo unt , then select the "Amount" eld from the list.
T arget Objec t : Select a Transaction [bt_stripe].
T arget Field : Select the eld you want the value to populate in. For example, you would select the A mo unt eld.
7. Click Save.


Virtual Terminal Transaction Con guration

Coming in 2026: Deprecation of Aura Virtual Terminal Component

New Virtual Terminal con gurations should utilize our modern and feature-rich Lightning Web Component version. We plan to sunset the Aura Component and related Flow Screen Charge Component in 2026.


Don’t worry! Customers will receive advance notice of the sunset date to ensure a smooth transition.


1. Navigate to the Transaction object in Setup.
2. Click Field Sets.
3. Click Edit next to Virtual Terminal.
4. Remove, add, and modify the elds within that box to t your use case.
Fields "In the Field Set" box are the elds currently on the Virtual Terminal's Transaction screen.
5. Click Save.


New Record Screen
The New Record screen allows you to create new records from the Related T o eld on the Virtual Terminal.


Account and Contact
The Account and Contact "New Record" screens have prede ned elds available, and a Field Set record is automatically created.

1. Navigate to the Account or Contact Object in Setup.
2. Click Field Sets.
3. Click Edit next to "Virtual Terminal."
4. Remove, add, and modify the elds within that box to t your use case. Fields "In the Field Set" box are the elds currently on the Virtual Terminal's new Account or Contact record screen.
5. Click Save.


Other Objects
Related To objects besides Account and Contact, show a blank New Record screen. To create new records, you will need to manually create a Field Set.

For example, the new Lead screen looks like this before adding a Field Set.


1. Navigate to the Lead Object in Setup.
2. Click Field Sets.
3. Click New.
4. Add values to the following elds:
Field Set Label = "Virtual Terminal"
Field Set Name = "Virtual Terminal"
If the Field Set Name value is different than above, the elds will not display on the Virtual Terminal screen.
5. Drag the elds you want to use for creating a new Lead record to the "In the Field Set" box.
6. Click Save.


The screen now has elds and will create new Lead records!


Custom Labels

The following picklist values can now be translated using custom labels.

Action
“New Single Charge”
“New Payment Method”
Process Type
“Capture Now”
“Auto-Process”
“Authorize Now”


Custom Labels are custom text values, up to 1,000 characters, that can be accessed from Apex Classes or Visualforce Pages. Our Payments package includes the following Custom Labels for the Virtual Terminal.

Action
Related To
Parent Object
Payment Method
Amount
Process Type
Currency


Before modifying a Custom Label, please complete the following con guration step in the Translation Workbench. This step is required to be able to modify customizations managed by the Payments package.

Virtual Terminal - Custom Labels with Translation Workbench Setup


Update Settings in Translation Workbench
1. Navigate to Setup.
2. In the Quick Find box, type "workbench".
3. Click Translation Workbench.
4. Click Translation Language Settings.
5. Click Enable.
6. Click Add.
7. Select your Language .
8. Check A c tiv e .
9. Click Save.


Update Virtual Terminal Labels in Custom Labels
1. Navigate to Setup.
2. In the Quick Find box, type "Custom Labels".
3. Click Custom Labels.
4. Find the Custom Labels with "VT" in the name.
5. Click the hyperlinked name of the Virtual Terminal Label you would like to modify.
6. Click New Local Translations/ Overrides.
7. Select your Language .
8. Add the text for the label you would like to see displayed in the T ranslatio n T ex t eld.

Example: Master Label = VT Action > T ranslatio n T e xt = "Custom Action". "Custom Action" will be what a user sees on the Virtual Terminal.


Available Actions
The Virtual Terminal has the capability to capture a New Single Charge or create a New Payment Method. Users are able to select which screen they would like to use by selecting an A c tio n value.


New Single Charge
The A c tio n = "New Single Charge" creates a new Transaction for the user. A c tio n = "New Single Charge" has the following elds available out of the box:

P ay ment Gateway : This eld is only visible if your org has more that one Payment Gateway.
Related T o : Use this eld to relate to an Account, Contact, or Lead.
P arent Objec t : This eld is a lookup to the Transaction Parent.
P ay ment Metho d : Only valid Payment Methods for the selected Payment Gateway will be available in this list.
Desc riptio n : Optional
A mo unt - Set to the amount you would like to charge.
Currenc y : The value from the related Invoice's Currenc y I SO eld will automatically populate this eld. If the Invoice's Currenc y I SO eld is blank, the Virtual Terminal will use the Payment Gateway’s Def ault Currenc y value.
P ro c ess T y pe : Choose from "Capture Now", "Auto-Process", or "Authorize Now".


Known Salesforce Issue

If, after capturing a Transaction, the Virtual Terminal component displays an error message at the bottom of the widow refresh your page. This error occurs due to a know Salesforce issue. Read more here.


New Payment Method
The A c tio n = "New Payment Method" gives users the ability to add a new Payment Method to a related Account, Contact, or Lead record. Users can add either credit card or bank account details.


Payment Process Type

Update

The logic in the Virtual Terminal has been updated to prevent users from receiving the "Cannot read properties of null" error when trying to add a Payment Method. The user should now select a Related To record before adding a new Payment Method.


The Virtual Terminal can also schedule payments.

1. De ne the Related T o , P arent Objec t , Desc riptio n , A mo unt , and Currenc y   elds.
2. De ne the P ay ment Metho d .
3. Change the P ro c ess T y pe to "Auto Process".
4. De ne the Capture Date .
5. Click Process.


Webhooks

Overview
Webhooks provide a mechanism where a server-side application (In this case Stripe) can notify a client-side application (in this case Payments) when a new event (like customer create, update, delete, charge capture, charge failed, etc) has occurred on the server.

Webhooks automatically send speci ed data to a destination (endpoint) from database events. Our Payments app utilizes webhooks for many of our features, such as updating your Salesforce org with credit card information and creating Dispute records.


Bene ts
1. Webhook allows us to stay up-to-date by updating the card on le with any recent changes in the credit card information by major credit card companies.
2. Allow Payouts to be received in Salesforce.
3. After capturing the transaction, webhooks allows disputes to be created in Salesforce.
4. Noti es/updates of any deleted payment gateway customer record or payment method.
5. Recognize any changes in Stripe Billing subscription/Invoices.
6. Maintains consistency of all records from Stripe into Salesforce and so on.


Instructions

Create a Force.com Domain
1. Go to Setup.
2. In the Quick Find box, enter “Sites and Domains.”
3. Click “Sites.”
4. Enter a value for your Force.com domain.
5. Click Check Availability.
6. Review and accept the Site terms of use.
7. Click Register My Force.com Domain.


Site Con guration
1. Go to Setup.
2. In the Quick Find box, enter “Sites and Domains.”
3. Click “Sites.”
4. Click New.


5. Enter a Site Label , Site Name , and a Def ault W eb A ddress . (We suggest using "webhook" or "stripe" for the Site Label and Site Name .)
6. Set A c tiv e = "TRUE" (checked).
7. For the A c tiv e Site Ho me P age eld, click the Lookup icon and select "InMaintenance". (The page is not visible. It's just a placeholder because a value is required).
8. Click Save.


Change the Default Record Owner for Webhook Events

1. Go to Setup.
2. in the Quick Find box, enter and click “Sites.”
3. Click Edit next to your webhook site.
4. Change the Def ault Rec o rd Owner to a user of your choice.
5. Click Save.


Assign the Blackthorn | Payments (Site Guest User) permission set to the public user

Site Guest User Permission Set Renamed

For users looking to setup Webhooks with a Payments package older than v5.6 you will need to add the Blackthorn | Payments (Webhooks) permission set. Additionally, you will need to add a Sharing Rule to allow the Site Guest User to access the Payment Gateway object.

The Blackthorn | Payments (Site Guest User) permission set is now a dual purpose permission set with packages v5.6 and beyond. This permission set will be used for webhook setup and REST API setup.


1. Navigate back to the Site you created.
2. Click Public Access Settings.


3. Click the View Users or Assign Users button.
4. Click the link for the site guest user.


5. Add the Blackthorn | Payments (Site Guest User) permission set to this user's record.
6. Click Save.


Not seeing the Blackthorn | Payments (Site Guest User) Permission Set?

This permission set is only available in Payments packages 5.16 and later. Please upgrade to the latest version then try again.


Con gure Webhooks and Add Webhook Events
In Stripe
In Authorize.net


Spreedly Limitation

We currently do not support webhook callbacks for Payment Gateways that are con gured through Spreedly.


Con gure Webhooks in Stripe
In this section, you will gather the different components that will make up the URL before adding it to Stripe.

The URL will have the following format: https://SITE_DOMAIN_NAME/SITE_PATH/services/apexrest/bt_stripe/webhook/WEBHOOK_LABEL

SITE_DOMAIN_NAME = The Salesforce Do main Name for the Site you set up
SITE_PATH = The P ath for the Site
WEBHOOK_LABEL = The value in the Payment Gateway W ebho o k Label eld
“services/apexrest/bt_stripe/webhook” remains the same


Create a Salesforce Webhook Site URL
1. Go to Setup.
2. In the Quick Find box, enter “Sites and Domains.”
3. Click “Sites.”
4. Locate the site you just created and click the URL.
5. Copy the URL.
6. Replace “SITE_DOMAIN_NAME/SITE_PATH” with the copied URL.
7. Leave “services/apexrest/bt_stripe/webhook” as is.
8. Open the related Payment Gateway record.
9. Copy the value in the W ebho o k Label eld.
10. Replace “WEBHOOK_LABEL” with the copied value from the W ebho o k Label eld.
11. To verify that the new URL works, open a new browser tab and paste the URL. You will see the following message.


Con gure the URL in Stripe
1. Go to your Stripe dashboard. When you create a Webhook URL for your Stripe account in test mode, ensure the "Viewing test data" switch is enabled.
2. Click the Developers tab at the bottom-left side of the screen.
3. Click Webhooks.
4. Click + Add destination to add a destination.


5. Click Your account.
6. Click into the Account section.
7. Check the Selec t all A c c o unt ev ents option.


8. Scroll down to and click into the Charge section.
9. Click the Selec t all Charge ev ents option.


10. Click into the Checkout section.
11. Check the options that are relevant to your use case.


12. Scroll down to the Invoice section.
13. Check the Selec t all I nv o ic e ev ents option.


14. Scroll down to the Payment Method section.
15. Check the Selec t all P ay ment Metho d ev ents option.


16. Scroll down to the Refund section.
17. Check the Selec t all Ref und ev ents option.


18. Click Continue.
19. Select “Webhook endpoint.”


20. Click Continue.


21. Enter a Destinatio n name .
22. Enter the URL you created in the Endpo int U RL eld.
23. Click Create destination.
24. To test the new Webhook Event, create a new charge Transaction, capture it, and charge it. A new Webhook Event will be created for the Transaction.

In Stripe, click the Events tab to see the newly created charge. The new Stripe Ev ent I D will match the Webhook Event Ev ent I D .


How do I send webhooks from Stripe to Salesforce if all the retries have been exhausted?

The only solution is to manually resend the webhooks. See Stripe’s documentation for more information.


Con gure Webhooks in Authorize.net
In this section, you will gather the different components that will make up the URL before adding it to Authorize.net.

The URL will have the following format: https://SITE_DOMAIN_NAME/SITE_PATH/services/apexrest/bt_stripe/webhook/WEBHOOK_LABEL

SITE_DOMAIN_NAME = The Salesforce Do main Name for the Site you set up
SITE_PATH = The P ath for the Site
WEBHOOK_LABEL = The value in the Payment Gateway W ebho o k Label eld
“services/apexrest/bt_stripe/webhook” remains the same


Create a Salesforce Webhook Site URL
1. Go to Setup.
2. In the Quick Find box, enter “Sites and Domains.”
3. Click “Sites.”
4. Locate the site you just created and click the URL.
5. Copy the URL.
6. Replace “SITE_DOMAIN_NAME/SITE_PATH” with the copied URL.
7. Leave “services/apexrest/bt_stripe/webhook” as is.
8. Open the related Payment Gateway record.
9. Copy the value in the W ebho o k Label eld.
10. Replace “WEBHOOK_LABEL” with the copied value from the W ebho o k Label eld.
11. To verify that the new URL works, open a new browser tab and paste the URL. You will see the following message.


Con gure the URL in Authorize.net
1. Go to your connected Authorize.net account dashboard.
2. Click the Account tab.
3. Click Settings.
4. Click Webhooks.


5. Click Add endpoint.


6. De ne a Name .
7. In the Endpo int U RL eld, enter the Salesforce webhook Site URL you created.
8. Set Status = "Active".
9. Under Select Events, check "All Events."
10. Click Save.

If you have multiple Authorize.net accounts connected to your Salesforce org and want to create a Webhook Endpoint for each in Authorize.net, you can use the same Salesforce Site. Change the WEBHOOK_LABEL part of the URL to the Webhook Label value on the Payment Gateway record you want to use.


Do you have multiple Authorize.net accounts?

If you have multiple Authorize.net accounts connected to your Salesforce org and want to create a webhook endpoint for each in Authorize.net, you can use the same Salesforce Site. It's as easy as changing the WEBHOOK_LABEL part of the URL to the W ebho o k Label value from the Payment Gateway record you want to use.


Test Webhook Connection

Test webhook connection in Stripe
Verifying in Test Mode:

1. Select the Webhook tab on the left-hand side.
2. Click your URL.
3. In the top right, click Send test webhook.


4. Set Ev ent ty pe = "customer.created".
5. Click Send test webhook.


If you received a "Test webhook sent successfully" message, then Webhooks are set up correctly!


Test webhook connection in Authorize.net
1. Click on Account tab > Settings > Webhooks.
2. Edit the Endpoint and set the Status to "Inactive."
3. Click Save.

You will see a Test Webhook button as shown in the below screenshot.


If you received a "Ping successful" message at the top, then webhooks are set up correctly!


Verifying in Live Mode
In live mode, don’t forget to create a new URL. You can copy your Test Webhook URL, and update the Webhook Label from your live Payment Gateway record.

1. Create a new Customer in Stripe.
2. Click on the newly created customer record, scroll down to Events, and select the Event record.
3. Scroll down to Webhooks.

If the Webhook record says "Success", then Webhooks are set up correctly in Production.


Adding Webhook signatures in Stripe (optional)
Webhook signatures is an additional layer of security. When setting them up, the system makes sure that the webhook event messages are not corrupted in Salesforce.

1. Go to Stripe Dashboard | Webhooks.
2. Select the webhook.
3. On the Signing Secret section click Click to Reveal .


4. Navigate in your Salesforce Org to Setup | Custom Metadata Settings.
5. Click Webhook Secret | Manage Records
6. Click New .
7. Enter values for Label , Webhook Secret Name , and Signing Secret .
8. Click Save .


Process Stripe Billing Webhook Types Asynchronously
A global method that allows customers to process certain Stripe Billing webhook types asynchronously instead of via the Blackthorn batch jobs was added. If the P ro c ess A sy nc checkbox = “True”, the existing web processing batch jobs will skip those webhooks.

Blackthorn customers are responsible for adding the logic that 1) sets the records they want as Process Async and 2) calls the async method to process them. The following example code creates a before trigger to check the P ro c ess A sy nc box and an after trigger to call the async method.

Before proceeding, two updates must be made to the Site Guest User/public user.


Step 1: To avoid permission errors, give the Blackthorn | Payments (Site Guest User) permission set Read access to the Product (Product2) object.

1. Click the Gear icon in the upper right-hand corner.
2. Click Setup.
3. In the Quick Find box, enter and click “Permission Sets.”
4. Create a new permission set.
a. Click New.
b. In the Label eld, enter a descriptive name for the permission set, such as “Read Access to Product2.”
c. Click Save.
5. Con gure object permissions.
a. Click “Object Settings” or “Object Permissions” in the Apps section.
b. Find and click the Product (Product2) object. If you don’t see it, use the search function to locate it.
c. Click Edit next to the Products heading.
d. In the Object Permissions section, set Read to “Enabled” (checked). Do not enable Edit , Create , and Delete unless they are needed.
e. Click Save.

Step 2: Assign the newly created permission set to the public user.

1. Navigate back to the site you created.
2. Click Public Access Settings.
3. Click the View Users or Assign Users button.
4. Click the link for the site guest user.
5. In the Permission Set Assignments section, click Edit Assignments.
6. Move the newly created permission set from the Available Permission Sets column to the Enabled Permission Sets column.
7. Click Save.


Plaintext                                                                                                                                                                             Copy

trigger customWebhookTrigger on Webhook_Event__c (before insert, after insert) {
if (Trigger.isBefore) {
for (bt_stripe__Webhook_Event__c webhook : Trigger.new) {
if (webhook.bt_stripe__Type__c == 'invoice.created') {
webhook.bt_stripe__Process_Async__c = true;
}
}
}

if (Trigger.isAfter) {
List<Webhook_Event__c> webhooks = [SELECT Id, Name, Type__c, Process_Async__c, Processed__c, Payment_Gateway__c, Data__c FROM Webhook_Event__c WHERE Id IN :trigger.new];
for (Webhook_Event__c webhook : webhooks) {
if (webhook.bt_stripe__Process_Async__c && webhook.bt_stripe__Type__c == 'invoice.created') {
// Call without sharing class here to process the webhook
}
}
}
}


NOTE: Replace 'invoice.created' or add additional webhook types as needed.


Next Steps
Insert the Virtual Terminal onto your parent object(s) Page Layouts.
Use Payment Schedules to create future looking Transactions in minutes.
Learn about our supported Payment Methods.


Troubleshooting
If you have received an error in the Setup Wizard, with Webhooks or have a question, please view our Troubleshooting or FAQ page.


Overview

Blackthorn Mobile Payments
We make it easy to accept credit card, check, ACH, cash, and money order payments with your mobile phone. The charge process is super fast and easy - enter an amount, choose a Payment Method, and charge. Once the transaction is complete, you can email a receipt to the customer by entering their email.


Payment Methods
Use card reader support for tap, dip, and swipe credit card payment options.
Charge credit cards in person to receive card present swipe rates.
Other Payment Methods include ACH, cash, check, and money order.
Handle the entire payment process in a PCI-compliant manner.


Android Devices
On Android devices, only card, cash, check, and ACH payment methods are available. The Money Order payment option is not available.


Salesforce Connected App Changes
Salesforce recently announced a change to its security policy around Connected Apps, effective August 28th. As a result, Blackthorn recommends verifying that these Connected Apps are installed in your Salesforce orgs.

Blackthorn | Connected App - required to use Blackthorn Events and Blackthorn Payments
Mobile Check-in App - required for using Blackthorn Mobile Check-in
Blackthorn | Mobile Connected App - required for using Blackthorn Mobile Payments
Blackthorn Message - required for using Blackthorn Messaging

Please review the attached pdf for instructions to check that the required Connected Apps are installed and connected correctly.

Your browser does not support PDF. Click here to download.


Salesforce Integration
The Mobile Payments app can be opened from the Salesforce mobile app and the Salesforce Field Service mobile app. The link to our app can send data to pre-populate a Payment Gateway, charge A mo unt , Desc riptio n , and a related Salesforce record.
Charge Transaction and Payment Method records are stored in Salesforce where they can be related to an Account, Contact, or any other standard or custom object.
Payment Methods from a swipe or dip can be re-used in Salesforce for other charges or subscriptions on Transactions with a Payment Intent.
Checks can be scanned and processed using the Check 21 integration via the Salesforce mobile app.
Users can process different Transactions across different Payment Gateways and create a successfully processed Transaction and a valid Payment Method.
If the Transaction's Contact/Account matches an existing user with the same Payment Gateway used for the new Transaction, the existing user will be attached to the new Payment Method and new Transaction.
If the Transaction’s Contact/Account does not match an existing user with the same Payment Gateway, a new Payment Gateway Customer will be created and attached to the new Payment Method and Transaction.


Setup Mobile Payments
To set up the Mobile Payments app in Salesforce, please follow these instructions.


Setup Field Service Lightning Payments
To set up the Fields Service Lightning, please follow these instructions.


Supported Devices
We strive to ensure that Blackthorn Mobile Payments app supports devices that Salesforce supports for their mobile app. Please review the requirements below.


Mobile Platform Requirements
The app requires that devices meet the minimum operating system requirements below.

Operating System                                                                                                         Version Requirement
Android                                                                                                                                                                    7.0 or later*
iOS                                                                                                                                                                        13.4 or later*

*NOTE: As of June 4, 2024, both iOS and Android version requirements will be updated in 2024. Please be aware that the minimum version requirement will increase.


Version Requirements

Minimum operating system requirements are subject to change. Blackthorn bears the sole responsibility of making changes to this list, with or without advanced notice.


Supported Stripe Readers
The following readers are supported on the Mobile Payments app (iOS and Android). We do not support any other kinds of bluetooth readers or POS terminals.

Stripe Reader M2 (USA only)
BBPOS Chipper 2X BT (USA only)
BBPOS WisePad 3 (AUS, MYS, NZL, SGP, AUT, BEL, FRA, DEU, NLD, LUX, CHE, DNK, NOR, SWE, ESP, PRT, CZE, IRL, GBR, FIN, and CAN)

Card readers are NOT supported with non-Stripe Payment Gateways.


Supported Browsers
Chrome
Safari
Edge
Android Webview
Firefox
Safari (in-app)
Samsung Internet


Supported Screen Resolutions
1920×1080 (Desktop computers)
1536×864 (Desktop computers)
1366x768 (Laptops)
360×640 (Android devices)
414×896 (iOS devices)
375×667 (iOS devices)


Supported operating systems, browsers, and screen resolutions are subject to change. Blackthorn bears the sole responsibility of making changes to this list, with or without advanced notice.

Devices such as Microsoft Surface and Surface Pro devices with touch technology enabled will experience Blackthorn Payments in a non-mobile app form.


Install & Setup

Known Issue: Permission Sets

Users must have Read access to any elds added to the “Blackthorn Pay - Transaction Parent” custom setting. If Read access isn’t granted, users will receive an ‘insuf cient permissions’ error when using the Mobile Payments app.

This issue is scheduled to be xed in early 2026.


Package Install
1. Install the latest version of Blackthorn Payments and complete the setup wizard.
2. Install the Blackthorn Mobile Payments package in a sandbox or production and assign licenses to all users that need access.
3. Install our iOS app.


Add Mobile Pay Action to Transaction Page Layout
The Mobile Pay action can be added to the Transaction page layout to link the Salesforce mobile app to the Blackthorn Mobile Payments app. This allows Salesforce mobile app users to take a mobile payment.

Follow the steps below to add the Mobile Pay action to the Transaction page layout.

1. In Salesforce, click the Gear icon to go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, search for and click the Transaction object.
4. Click the Page Layouts tab.
5. Click the Charge Transaction Layout.
6. Click the Mobile & Lightning Actions tab.
7. Drag and drop the Mobile Pay action in the Salesforce Mobile and Lightning Experience Actions section.
8. Click Save.


Select a Payment Gateway
If you are using Stripe, you must con rm that a location is set for the Payment Gateway in Stripe before using the Mobile Payments app.

The user can select a Payment Gateway when creating a Transaction either in Salesforce or in the Mobile Payments app. If there are multiple Payment Gateway records, the app will default to the default Payment Gateway.

If the user creates the Transaction from the Mobile Payments app, they can select a Payment Gateway on the Home page. Initially, the default Payment Gateway will be selected. If a user selects a different Payment Gateway, the app will remember the new selection the next time a new Transaction is created.


Enable Send Receipt Email in Salesforce
After a mobile transaction is complete, Salesforce can send a receipt via email to the customer if the Rec eipt Email eld is populated AND the T ransac tio n Status = “Completed”.

Follow the steps below to enable this feature.

1. In Salesforce, go to Setup > Work ow Rules.
2. Click Activate next to "Send Blackthorn | Payments Receipt (Text)".


Set Up Stripe Locations
Before using your Stripe account, con rm that Locations have been set up. All card readers require an assigned Location. Use the following steps to set up Locations in your Stripe Dashboard if they aren’t already set up.

1. Log into your Stripe Dashboard.
2. Click Payments.
3. Click Readers.
4. Click Locations.
5. On the Locations page, click New.
6. Enter the name and address details for each physical location.
7. Click Save.
8. Once you’ve created each Location, click New in the Location’s “Reader” section to register each card reader to a Location.


Card Reader Firmware Updates

BREAKING CHANGE - iOS Devices

Stripe users must add locations to their Stripe dashboard before upgrading their iOS mobile devices to the latest version. If you do not add locations rst, you won't be able to connect to a Stripe card reader.


We've added the ability to update your card reader rmware inside the Mobile Payments app.

1. Navigate to the Reader screen.
2. Connect your reader.
3. Notice that while connecting the reader, we are checking for rmware updates.
4. If your reader has a rmware update available, a link to install the update will appear.
5. Follow the on-screen prompts to install the update.


Connecting to an Android Device
When connecting a Stripe card reader, a modal screen will appear on the Mobile Payments app to ask for Bluetooth permissions for the following new permissions in Android 12 or higher. It may take up to two to three minutes for the card reader to appear on the screen.

BLUETOOTH_CONNECT: required to connect to paired Bluetooth devices.
BLUETOOTH_SCAN: required to scan and pair nearby Bluetooth devices.
BLUETOOTH_ADVERTISE: required to advertise to nearby Bluetooth devices.


Save Card Details with the Stripe Terminal
There are two options for collecting reusable card details with Stripe Terminal. Please click one of the options below for speci c instructions from Stripe.


SetupIntents
Collect information directly, without charging a card: This method uses SetupIntents, a new API endpoint, to collect a card’s details without charging the card.


Payment Intents
Save card details after payment (US only): This method uses PaymentIntents to create reusable tokens for US customers.

The Payment Intent’s Capture Metho d eld also includes the following picklist values: “Manual,” “Automatic,” or “Automatic Async” (automatic_async), which matches Stripe’s library. The default value for the Capture Metho d eld is “Automatic Async.”


Virtual Terminal Custom Setting
Before using Spreedly with Cybersource to accept payments, the Virtual Terminal custom setting Sho w A ddress must be enabled. This ensures that the address elds (Street , City , State , and Co untry / Regio n ) will be visible on the Payment Method creation page in the Virtual Terminal.


Skip Receipt Screen Custom Setting
iOS Mobile Payments app users can now use the Blackthorn Payments | Mobile Settings custom setting Sk ip Rec eipt Sc reen to determine if the last screen will show the option to send a receipt.

If Sk ip Rec eipt Sc reen = “True” (checked), the last screen won’t show the option to send a receipt.
If Sk ip Rec eipt Sc reen = “False” (unchecked), the last screen will show the option to send the receipt.

To update the setting, follow the steps below.

1. Click the Gear icon.
2. Click Setup.
3. In the Quick Find box, enter and click “Custom Settings.”
4. Click Manage next to Blackthorn Payments | Mobile Settings.
5. Click New.
6. Check the Sk ip Rec eipt Sc reen checkbox.
7. Click Save.


Troubleshooting
If you need to determine which software version was used for a Transaction, add the Mo bile A pp V ersio n eld to your Transaction object. The Mo bile A pp V ersio n will automatically populate with the application platform name (iOS or Android) and the version number.

If you have any questions about the setup process, please contact Blackthorn Support. We're happy to help!


Con guration Options
The Mobile Payments app can be customized in the following ways:


Lock an Amount
On a Salesforce Transaction record, if you set the Mo bile Lo c k A mo unt = "Yes", the Mobile Payments app will not allow the A mo unt value to be changed for that Transaction.


Skip the Intro Screen
On a Salesforce Transaction record, if you set the Mo bile Sk ip I ntro Sc reen = "Yes", the Mobile Payments app will not show the Intro screen (Description, Amount, Currency, etc) for that Transaction.


Set Payment Methods
If values are set on the Transaction A c c epted P ay ment Metho ds eld or the Payment Gateway A c c epted P ay ment Metho ds eld, only the set Payment Methods will be available for the selected Payment Gateway or Transaction.

The Accepted Payment Methods elds are evaluated in the following order:

1. If the Transaction A c c epted P ay ment Metho ds eld is set, use those values for the Transaction.
2. Otherwise, if the Payment Gateway A c c epted P ay ment Metho ds eld is set, use those values for the Transaction.
3. If neither of those elds are set, all Payment Methods are available for use.


Using Tap to Pay
Users can now set A c c epted P ay ment Metho ds = "Tap to Pay" on the Payment Gateway, Transaction, and Payment User Override objects.


Require an Existing Transaction for Mobile
The Require Ex isting T ransac tio n f o r Mo bile eld on the Payment Gateway record is available in the Mobile Payments app. This setting blocks users from processing a payment in the app if there isn’t an existing Transaction in Salesforce before the app is launched.

If this eld is checked and a user tries to capture a payment from the Mobile Payments app, the user will get an error.


iOS Mobile Save Reusable Payment Methods

Important Notes


We only support this feature on iOS mobile devices and for Stripe payment gateways. To use this feature, you must have Version 2.0.2 of the Mobile Payments app and Version 6.42 of the Payments package.


The iOS Mobile Payments app’s user interface now includes a “Save card for future payments” checkbox.

When submitting a payment via a card reader or by typing in a card’s information, users can check the checkbox to allow their card information to be saved and reused for future payments. A message will appear in Stripe indicating the user has given consent for the card’s information to be stored and used for future payments.

If the checkbox is not checked, no card information will be saved.

Admins can enable or disable this feature using the custom attribute “Enable_Reusable_Payments.” For example, the following will occur if the mobile device is of ine

If the Payee checks "Save card for future payments," then the Payment Method Status will be set to "Valid."
If the Payee does not check the "Save card for future payments" checkbox, then the Payment Method Status will be set to "One-time."

You will need to connect to a card reader at least once while connected to the internet before attempting to collect of ine payments.


Use Case
A eld engineer must collect a payment at a customer's home. Now, the customer can consent to their payment information being saved and stored as a reusable Payment Method in Salesforce. The eld engineer’s organization can then charge the same Payment Method for items such as a subscription or a payment schedule for a service.


Add “Enable_Reusable_Payments” to your Org
1. Go to Setup.
2. In the Quick Find box, search for and click “Manage Connected Apps.”
3. Click Edit next to “Blackthorn | Mobile Connected App.”


4. Click New next to Custom Attributes.


5. Set A ttribute k ey = ENABLE_REUSABLE_PAYMENTS.
6. Set A ttribute V alue = "1" . Make sure to include the quotes.


7. Click Save.
8. Open the Mobile Payments app and log out.
9. Log in to the app.

Now, when a payment is entered, the user can check the “Save card for future payments” checkbox.

To disable the custom attribute, an Admin must delete the “Enable_Reusable_Payments” custom attribute.


Testing
In Blackthorn Payments, add a Payment Gateway with T est Mo de = "TRUE".

Stripe offers physical test cards for purchase that work with special amounts. Those amounts are listed here.


Navigation
The Mobile Payments app includes a navigation menu to access different sections in the application.


Home
This is the main screen of the application where users enter details about their Transactions and associate them with an Account and/or a Contact.


Tokenize Card
This section of the application allows users to enter credit card details. The information is then tokenized and added to Salesforce as a Payment Method, which can be associated with an Account and/or a Contact.


The Payment Gateway selected on the Home screen will be the Payment Gateway you see populated on the Payment Method that is created through this Tokenize method.


Reader
The Reader page allows users to connect the Mobile Payments app to a card reader. This is also where you can update the rmware of your card reader. When searching for a card reader, it may take up to two to three minutes for it to appear on the screen.

Mobile Payments will search for rmware updates each time you connect a card reader. If your reader needs an update, an install link will be presented. Otherwise, a message stating that your reader has the latest update will be displayed.


Support
The Support page allows users to contact our Customer Success team. This is where they can submit a case or access our documentation.


About
The About page will display the app version. This can be helpful for troubleshooting, or if you want to check that you've installed the latest version.


Logout
This is the basic option for logging out of the app.


Check 21 Integration

iOS Only

Currently, the Check 21 integration is only compatible with iOS Mobile Payments.


Overview
Blackthorn supports Check 21 integration by utilizing Check 21 technology into the Blackthorn Mobile Payments iOS app and the Salesforce.com applications. It allows you to accept payments in the eld by scanning checks.

Check 21, a third-party provider, will be leveraged through its API and native Salesforce package to achieve the check and money order processing.


Limitations
A warning message will appear when the Transaction to Account rollup batch job attempts to roll up more than 10,000 Transactions related to a single Account. This message lets users know the rollup job is approaching Salesforce limits and will appear as a Blackthorn Log.
If the batch job detects more than 40,000 Transactions rolling up to a single Account, the job will create a cap at 40,000 Transactions and generate a Blackthorn Log recommending users disable the batch job via Custom Settings.


Package Installs
1. Install the latest version of Blackthorn Payments and complete the Setup Wizard.
2. Install the Blackthorn Mobile Payments package and assign licenses to all users who need access.
3. Install Check 21.
4. Install the Check 21 Integration package.
5. Assign MCC Payology permission set to the user.


Setup

Custom Settings Setup
1. Navigate to Setup > Custom Settings > CheckForce API Custom Settings
2. Click Manage.
3. Click New.
4. Enter the data listed in the following image.


Page Layout Updates
Update your Charge Transaction page layout to include four elds:

* T ransac tio n Sub-T y pe
* So urc e
* Chec k Capture Submissio n
* Mo bile Sk ip I ntro Sc reen

The T ransac tio n Sub-T y pe will be de ned as "Check", So urc e will be de ned as "Mobile", and Chec k Capture Submissio n will be populated after submitting a check through the mobile app.


Use Check Scanning Functionality from a Mobile App
1. Open an existing Transaction from the Salesforce app that has the A mo unt populated, a Check 21 enabled Payment Gateway selected, and the A c c epted P ay ment Metho ds = "Check".
2. Click the Mobile Pay button at the top of the screen.


3. You will be directed to a screen where you can scan the front and rear images of your check.
Note: Setting Mo bile Sk ip I ntro Sc reen = "Yes" on the Transaction will take the user directly to the check scanning page. Otherwise, you will see a screen to validate the eld values from the Transaction.


If Check 21 is not installed in the org, the user will not see the screen above.


4. Tap on the left image to start scanning of the front of the check. It will ask for camera permissions, which you will need to accept, or the scan won’t be possible.
5. Take a picture of the check. You'll notice a green rectangle appears. Line up the border with the check image. This rectangle will rotate with the screen orientation.
6. Follow the directions above to capture an image of the back of the check.
7. Once you have captured both the front and rear check images, the application will upload the images to the Check 21 API for image recognition.


8. Verify the data from the images is correct, and click on Pay to nish the process.
Note: You can edit the values detected by Check 21.


9. The user will then be directed to a success screen where they can send an email receipt if needed.


10. The Transaction T ransac tio n Status eld will be updated to "Completed".


Of ine for Mobile
Users can now collect payments with intermittent, limited, or no internet connectivity with the Mobile Payments app’s new Of ine for Mobile feature.

For example, if a user is out in the eld and has an intermittent internet connection, they can collect a payment, and the following will occur behind the scenes.

A card, cash, ACH, or card reader payment is collected.
The payment information is saved in the device’s local storage.
The internet connection is restored.
The locally stored payment information is synced to the Payments app / Salesforce.
All payment information on the mobile device is deleted.


Custom Setting
Users now can collect payments when the Mobile Payments app is of ine by turning on a new custom setting.

Location: Blackthorn Payments - Mobile Settings
Field Label: Enable Of f line Mo bile
API Name: bt_stripe__Enable_Of ine_Mobile__c
Default = unchecked


Functionality

Mobile Pay

When Enable Of f line Mo bile is checked (enabled), the Mobile Pay button (Mobile Payments package) includes the A mo unt and Desc riptio n in the URL.
When Enable Of f line Mo bile is unchecked (disabled), then the URL remains the same.


FSL

When Enable Of f line Mo bile is checked (enabled), then the Mobile Pay hyperlink (Mobile Payments FSL Extension package) includes the A mo unt and Desc riptio n in the URL.
When Enable Of f line Mo bile is unchecked (disabled), then the URL remains the same. The URL will be regenerated when the A mo unt and/or Desc riptio n is updated on the Transaction.


Features

FSL
The Field Service mobile app and new of ine functionality will ship as a known issue as the deep link does not update as intended. This is because, with its current implementation, there is no way to update the link without connecting to the internet and performing a data sync.


New Menu Option
A new menu option called “Pending changes (x)” was added to the left-hand navigation. The label includes the number of pending records.

When a user taps the Pending charges option, they will see a new screen with a list of Transactions that were saved while the device was of ine. The list of records will be synched and validated in Salesforce as soon as the internet connection is restored. The records will then be removed from the Pending changes list.

A dialog box will also show the user that there are pending changes if they try to log out of the app.


Payment Gateways
The Mobile Payments app will download and securely store a list of the available Payment Gateways the rst time the home screen loads. This allows users to capture payment details and select a valid Payment Gateway when an active internet connection isn’t available.

IMPORTANT: Change made to a Payment Gateway in Salesforce won’t be re ected in the Mobile Payments app until the home screen is loaded while the app is connected to an internet connection.


Reminders
When a user is working of ine, they will see a message reminding them that there is no active internet connection. The message will automatically appear and disappear based on whether the app can nd an active internet connection.

Users will also see a con rmation popup after a cash payment is submitted. This functionality works similarly to the way card and ACH payments work.


Security
When a device is of ine, and a Transaction is paid, the related information will be encrypted and stored locally on the device.

Any additional information created or changed while the app is of ine will sync to Salesforce when the app is online.

After syncing, all information will be validated, processed, and deleted from the of ine/local storage.


Payment Intents and Stripe Payment Methods

Prerequisites
To use this feature, you must meet the following criteria:

Use on iOS mobile device and a Stripe payment gateway.
Have Version 2.0.2 of the Mobile Payments app and Version 6.42 of the Payments package.


Overview
W hat is a Payment Intent record? A Payment Intent record is used by Stripe for its Strong Customer Authentication (SCA) feature, which helps make the payment process more secure.

Purpose of Feature Update: To change how Payment Intents are con rmed by the Mobile Payments app.


Previous Functionality
The Mobile Payments app con rmed the Payment Intent before making any calls to Salesforce to capture the Payment Intent.

Once the Payment Intent was con rmed, additional updates could no longer be made. That meant, all metadata mapping or customer information needed to be added to the Payment Intent before it was con rmed. But, the details required are located in Salesforce.


New Functionality
The Mobile Payments app now con rms the Payment Intent record is updated with any required metadata mapping and customer info before Stripe captures the Payment Intent. The streamlined process also reduces the number of API calls made to Stripe.


How It Works

New Custom Settings
The Blackthorn Payments | Mobile Settings custom setting includes the Co nf irm P ay ment I ntents (bt_stripe__Con rm_Payment_Intents__c) eld, which allows you to change where in the process the Payment Intent will be con rmed.

To use the new setting and postpone the initial con rmation of intent until additional information is gathered, set Co nf irm P ay ment I ntents to “False.”
To revert to the out-of-the-box behavior of immediate intent con rmation, set Co nf irm P ay ment I ntents to “True” or leave the eld blank.

New Order of Operation: The Mobile Payments app creates the Payment Intent and updates it with any required metadata mapping and customer information before Stripe receives it.


Enter Payment Methods Manually
Previously, Stripe only supported creating Payment Intents with the Mobile Payments app if the card information was captured by a card reader (versus typing the card numbers manually).

Now, the following solution applies when manually typing in a card’s information.

Since the payload going to Stripe includes a Payment Method ID but no Payment Intent ID (which was not created because the card info was typed in), the Stripe payment intents API will create the new Payment Intent record. This passes the following information to Stripe: Payment Method, customer information, and whether the customer has given consent to
save the Payment Method by checking the box in the Mobile Payments app.

After completing the transaction, the result is newly created Transaction and Payment Method records linked to the customer in Stripe and Salesforce. If the customer checks the box to allow their Payment Method to be reused, it will also be saved for future use.


Using a Card Reader
After using a card reader to complete a Transaction on the Mobile Payments app, a reference to the Payment Method record will be stored with the captured Payment Intent in Salesforce and Stripe.


Additional Con gurations
When the Mobile Payments app and a card reader are used to complete a payment, and the following custom settings are selected, the Payment Intent's information will be updated before an attempt to con rm/capture it.

Blackthorn Payments | Mobile Settings Co nf irm P ay ment I ntents eld is not checked.
Blackthorn Pay - Trigger Settings Enable SCA eld is checked.

Scenario 1: If an Account or Contact record is not selected, a new Payment Gateway Customer (PGC) will be generated for each Transaction.

Use the Mobile Payments app and card reader to complete a payment when an existing Account and/or Contact is not selected.

The captured payment in the Stripe account will include the customer ID and the charge/transaction ID.

Stripe will share a message indicating that the Payment Method was set up for future or scheduled payments. The pm_id was also set up for future use.

Comparing the values from Stripe with those on the Salesforce Transaction record will show that the Custo mer I D , P ay ment Metho d I D , and T ransac tio n I D match the values in Stripe.

The Transaction’s related Payment Intent, Customer, and Payment Method records will be complete and include the IDs from Stripe.

The new Payment Method can now be used to complete a new Transaction, which will generate a new Payment Gateway Customer record.

Scenario 2: If a Contact and/or Account records are selected, a new Payment Gateway Customer (PGC) will be created, if required, and used for subsequent Transactions.

Use the Mobile Payments app and card reader to complete a payment where an existing Account and/or Contact are selected.

The captured payment in the Stripe account will include the customer ID and the charge/transaction ID.

Stripe will share a message indicating that the Payment Method was set up for future or scheduled payments. The pm_id was also set up for future use.

Comparing the values from Stripe with those on the Salesforce Transaction record will show that the Custo mer I D , P ay ment Metho d I D , and T ransac tio n I D match the values in Stripe.

The Transaction’s related Payment Intent, Customer, and Payment Method records will be complete and include the IDs from Stripe. The new Payment Method can now be used to complete a new Transaction.

Here’s where things differ from the rst scenario.

Now, when a user completes a new payment using the same Contact and/or Account records, a new PGC record is not created. Instead, the PGC record from the original Transaction is used.

A new Payment Method is generated each time, but it will be linked to the rst PGC record created for this speci c combination of Contact and/or Account records.


Stored Of ine Payment Information
Salesforce’s SmartStore is a multithreaded, secure solution for of ine storage. It manages and stores payment information on mobile devices when they are of ine.

When a Transaction occurs, the following information will be stored for each Payment Method type.


Cash Payments
Description: Transaction Desc riptio n
Amount: Transaction A mo unt
Currency: Transaction Currenc y I SO
Method: HTTP method for API call once connection is restored
Path: Salesforce API endpoint to call once connection is restored
Timestamp: Unix timestamp when record was created
Gateway: Payment Gateway ID
Account Id: Associated Salesforce Account
ContactId: Associated Contact information
Email: Email recipient for sending the receipt


Typed Card Payments
Description: Transaction Desc riptio n
Amount: Transaction A mo unt
Currency: Transaction Currenc y I SO
Method: HTTP method for API call once connection is restored
Path: Salesforce API endpoint to call once connection is restored
Timestamp: Unix timestamp when record was created
Idempotent UUID: Unique identi er to prevent duplicate processing
Gateway: Payment Gateway ID
Card Details
Name: Cardholder name
Email: Cardholder email address
Expiry: Card expiration date
ZIP: Billing address ZIP code
Card number: Card number
Account Id: Associated Salesforce Account
ContactId: Associated Contact information
Email: Email recipient for sending the receipt


Card Reader Payments
Description: Transaction Desc riptio n
Amount: Transaction A mo unt
Currency: Transaction Currenc y I SO
Method: HTTP method for API call once connection is restored
Path: Salesforce API endpoint to call once connection is restored
Timestamp: Unix timestamp when record was created
Idempotent UUID: Unique identi er to prevent duplicate processing
Gateway: Payment Gateway ID
Payment Intent Id: Of ine Id for the Payment Intent. The card information is managed by Stripe.
Account Id: Associated Salesforce Account
ContactId: Associated Contact information
Email: Email recipient for sending the receipt


ACH Payments
Description: Transaction Desc riptio n
Amount: Transaction A mo unt


Currency: Transaction Currenc y I SO
Method: HTTP method for API call once connection is restored
Path: Salesforce API endpoint to call once connection is restored
Timestamp: Unix timestamp when record was created
Idempotent UUID: Unique identi er to prevent duplicate processing
Gateway: Payment Gateway ID
Bank Details
Account Holder: Name on bank account
Account Number: Bank account number
Routing Number: Bank routing/ABA number
Holder Type: Account holder type
Account Id: Associated Salesforce Account
ContactId: Associated Contact information
Email: Email recipient for sending the receipt


Tap to Pay
Mobile Payments app users now have the option to use the Tap to Pay feature to accept contactless payments via the Stripe Terminal SDK.


Prerequisites
Tap to Pay on iPhone is currently only available in the US.
Tap to Pay on Android is currently in beta in Australia, Canada, New Zealand, Singapore, the United Kingdom, and the United States.

To read more about using iOS devices with Stripe’s Tap to Pay feature, click here.

To read more about using Android devices with Stripe’s Tap to Pay feature, click here.


Mobile Wallet Tokens


Mobile wallet tokens are not reusable on either iOS or Android mobile devices.


iOS
Tap to Pay for iOS is now a supported Payment Method for Stripe transactions in the Mobile Payments app. As of today, Tap to Pay is only supported on Stripe.

The SDK for Tap to Pay on iPhone requires iOS mobile devices to meet the following criteria:

Running iOS 16.0 or later
iPhone XS or later
The device Is not jailbroken; the device bootloader is locked and unchanged.
Note: iPads do not have NFC reading capabilities, so they are not currently supported.


Functionality
To use the Tap to Pay feature, set A c c epted P ay ment Metho ds = "Tap to Pay" on the Payment Gateway, Transaction, and Payment User Override objects.

Tap to Pay requires an active internet connection and will not be supported if the Mobile Payments app is in of ine mode.
Tap to Pay supports existing Terminal functionality that saves card details for future online reuse. However, the Save Card functionality applies only to physical cards, not mobile wallets.
Used Payment details cannot be stored and reused if the payment is made using a mobile wallet (e.g., Google Pay, Apple Pay, etc.), as mobile wallet tokens cannot be reused. For more detailed information, please read this article from Stripe.
The Payments Mobile app does not support PIN entry as a fallback for payments that require an additional layer of authentication.


Android
Tap to Pay for Android is now a supported Payment Method for Stripe transactions in the Mobile Payments app. As of today, Tap to Pay is only supported on Stripe.

The SDK for Tap to Pay on Android requires Android mobile devices to meet the following criteria:

Contains a functioning NFC antenna and chipset
It isn’t rooted, and the device bootloader is locked and unchanged
Runs a current version of Android (Android 10 or above)
Uses Google Mobile Services
Has a hardware-backed keystore
Access to a stable connection to the internet


Functionality
To use the Tap to Pay feature, set A c c epted P ay ment Metho ds = "Tap to Pay" on the Payment Gateway, Transaction, and Payment User Override objects.

Tap to Pay requires an active internet connection and will not be supported if the Mobile Payments app is in of ine mode.
Tap to Pay supports existing Terminal functionality that saves card details for future online reuse. However, the Save Card functionality applies only to physical cards, not mobile wallets.
Used Payment details cannot be stored and reused if the payment is made using a mobile wallet (e.g., Google Pay, Apple Pay, etc.), as mobile wallet tokens cannot be reused. For more detailed information, please read this article from Stripe.
The Payments Mobile app does not support PIN entry as a fallback for payments that require an additional layer of authentication.
Tap to Pay for Android may require additional veri cation for transactions over a certain amount. To learn more about regional limits, click here.


Mobile Payments Android Releases

Changes to the Mobile Apps Login Process

Starting January 20, 2026, both the Mobile Payments and Mobile Check-in apps may require new users to activate their devices during the Salesforce login process. The Salesforce article, “Device Activation for Salesforce Orgs,” explains the device activation process.


Whether a new user needs to activate their device will be determined by the customer’s org settings. Additional information can be found here: “Changes to Device Activation for Single Sign-On (SSO) Logins.”


Please review the updates below and follow the upgrade instructions for your speci c device to upgrade your Mobile Payments app.


Build 2.0.1
Released 10 July 2024


Bug Fixes
If “Tap to Pay” is added as a picklist value for the A c c epted P ay ment Metho ds eld on a Payment Gateway, Android Mobile Payments app users will see “Tap to Pay” as an accepted payment option. (Known Issue: 000003417)
Android Mobile Payments app users with a Spreedly/Cybersource payment gateway will see an updated error message when an invalid (or missing) value is entered in the postal code eld for credit card payments. The new error message is “Please enter a valid Zip/Postal Code and try again.”
Android Mobile Payments app users will now be able to process a payment when using an Authorize.net gateway. Previously, the app randomly crashed, and the user was unable to complete the Transaction.


Build 2.0.0
Released 23 January 2024


Bug Fixes
Android Mobile Payments app users making a cash payment can now add/edit the description on the nal screen. Previously, Android users could not add or edit the description.


Enhancements
Users will see a con rmation message stating that an email receipt was sent after manually entering a card payment. Previously, the con rmation message was not visible.
Users will see a lock icon next to the Contact and Account         elds on an existing Transaction, indicating that they cannot edit those elds. Previously, users could edit the Contact and Account     elds on an existing Transaction from the Mobile Payments FSL app, causing duplicate Payment Gateway Customer records to be created.


Of ine for Mobile

The Field Service mobile app and new of ine functionality will ship as a known issue as the deep link does not update as intended. This is because, with its current implementation, there is no way to update the link without connecting to the internet and performing a data sync.
If the Mobile Payments app loses its internet connection, a red indicator bar with the message, “No internet connection” will be displayed at the top of the screen.
A user will see the Pending changes screen with the list of records waiting to be sent to Salesforce when they save information to local storage. Once the app is online and the records are successfully sent to Salesforce, the record will be removed from the Pending changes list.
In the app’s navigation menu, there will be a “Pending changes” option when there are recording waiting to be synced to Salesforce. The label will include the count of pending records.
If a user tries to accept a cash payment when the device is of ine, they will receive a popup with the following message. “No internet connection. The payment cannot be processed. You can save the payment for later and it will automatically retry when connection restores.” After choosing to save the payment, the following con rmation message will
appear. “Payment saved in local storage. It will be processed when the connection restores.”
While the Mobile Payments app is online, it will download the list of available Payment Gateways. After the initial download, users can access the Payment Gateways list from the home screen when the app is of ine. Note: Any change made to a Payment Gateway in Salesforce won’t be re ected in the Mobile Payments app until the app is loaded again
while online.
The Mobile Payments app accepts the following payment types.
Card (manually entered and swiped)
Cash
ACH
Card Reader


Tap to Pay
Tap to Pay for Android is now a supported Payment Method for Stripe transactions in the Mobile Payments app. As of today, Tap to Pay is only supported on Stripe.

The SDK for Tap to Pay on Android requires Android mobile devices to meet the following criteria:

Contains a functioning NFC antenna and chipset
Isn’t rooted and the device bootloader is locked and unchanged
Runs a current version of Android (Android 10 or above)
Uses Google Mobile Services
Has a hardware-backed keystore
Access to a stable connection to the internet

Tap to Pay requires an active internet connection and will not be supported if the Mobile Payments app is in of ine mode.

Tap to Pay supports existing Terminal functionality that saves card details for future online reuse. However, the Save Card functionality applies only to physical cards, not mobile wallets.

Payment details used cannot be stored and re-used if the payment used is a mobile wallet (e.g., GooglePay, ApplePay, etc.) as mobile wallet tokens cannot be reused. For more detailed information, please read this article from Stripe.

The Payments Mobile app does not support pin entry as a fallback for payments that require an additional layer of authentication.

Tap to Pay for Android may require additional veri cation for transactions over a certain amount. To learn more about regional limits, click here.


Build 1.1.14
Release 10 October 2023


Bug Fixes
Some Android devices crashed after the users logged in to the Mobile Payments app. The issue was identi ed and has now been resolved.
After collecting a payment on the Mobile Payments app, the billing email provided by the user will be stored in the email address eld on the related Payment Method and Payment Gateway Customer records. If an email is already stored on a related Payment Method and Payment Gateway Customer records, the existing email will not be overwritten by
the newly provided billing email. (Known Issue: 000002690)
To prevent duplicate Payment Gateway Customer records from being created by FSL users in the eld, the following update was made to the Mobile Payments app. The ability to edit/remove Contact and Account records from an existing Transaction was removed. For Transactions created by the app, the Contact and Account records can be
edited/removed. (Known Issue: 000002734)
Card Reader Payments on the Android Mobile Payments app will now process as expected.
When a user captures a card payment with a Spreedly gateway, the Country selected will determine if the State            eld is required.

After completing a Transaction with a Spreedly gateway, the Payment Status will be set to "Captured". Previously, the Payment Status was set to " Authorized".
Users can now click the Disconnect button to manually disconnect a card reader.
When trying to Tokenize a Payment Method to Authorize.net on the Mobile Payments app, a Transaction with Amount = “0” will no longer be created.


Enhancements
Previously, Blackthorn Mobile FSL app users received the following error message, “invalid ID eld: {!btfslmobileext__Open_Charge_Record_Id__c),” without providing additional detail. Users will now see the following message, “Something went wrong. Please return to the Field Service app, refresh the record, then try again.”
The label that displays at the bottom of the Android Mobile Payments app has been updated to “Return to Salesforce Field Service” so the label re ects the correct Salesforce name.


Build - 1.1.13
Release June 2023


Bug Fixes
An intermittent issue that occurred when processing a mobile card reader payment has been xed. The app will no longer attempt to update the Payment Intent while the related Transaction is being captured.
Card Reader Payments on the Android Mobile Payments app will now process as expected.
Improved error handling when using the Android app.
Some Android devices crashed after the users logged in to the Mobile Payments app. The issue was identi ed and has now been resolved.
To prevent duplicate Payment Gateway Customer records from being created by FSL users in the eld, the following update was made to the Mobile Payments app. The ability to edit/remove Contact and Account records from an existing Transaction was removed. For Transactions created by the app, the Contact and Account records can be
edited/removed. (Known Issue: 000002734)


Build - 1.1.12
Release 23 March 2023


Bug Fix
The Mobile Payments app will now skip the Intro Screen when the Mobile Skip Intro Screen checkbox is checked on a Transaction.


Build - 1.1.11
Released 14 February 2023


Bug Fixes
Android Mobile Payments app users can now log in to the app after an expired session without the app crashing.
When entering payment information on the credit card payments screen, users will now rst choose a Country and then select a State . This change will prevent the error that occurred when a user entered a country name that contained two words.


Build - 1.1.11
Released 20 December 2022


Bug Fix
Updates to timeouts have been made to ensure Android Mobile Payments app users can log in and log out without experiencing periodic app crashes and successfully complete a payment.


Enhancements
Users can now create and authorize new Payment Methods using a Spreedly Payment Gateway via the Mobile Payments app.
When a Spreedly/Cybersource Payment Gateway is used to enter a Payment Method on the Mobile Payments app, the First name and Last name                     elds on the credit card screen are now visible and required.
To create a new Payment Method with a Spreedly Payment Gateway with Cybersource in the Android Mobile Payments app, users must complete the following billing address elds. These elds will automatically appear on the Payment Method entry screen when using a Cybersource gateway via Spreedly and map to the Billing Information elds
located on the Payment Method object.
Street (Field API Name: bt_stripe__Billing_Street__c)


City (Field API Name: bt_stripe__Billing_City__c)
State (Field API Name: bt_stripe__Billing_State__c)
Postal Code (Field API Name: bt_stripe__Billing_Postal_Code__c)
Country (Field API Name: bt_stripe__Billing_Country__c)
A customer’s billing address information will be captured correctly in the Mobile Payments app and populated properly in the Cybersource dashboard.
Users can now enable a setting that will take the user directly to the Payment Method entry screen after tapping a deeplink to the Android Mobile Payments app. To set up this feature, create a new Transaction with the following settings.
Record Type = “Charge”
Mobile Skip Intro Screen = “Yes”
In the Accepted Payments Methods multi-select picklist on the Transaction (bt_stripe__Accepted_Payment_Methods__c), move “Card (Typed)” to the Chosen column.
After doing this, the following deeplinks will now navigate directly to the Payment Method entry screen:
“Mobile Pay” (btfslmobileext__Mobile_Pay__c) on the Transaction
“Mobile Pay” (btfslmobileext__Mobile_Pay__c) and “Mobile Authorize” (btfslmobileext__Mobile_Auth__c) on the Work Order related to the Transaction (Transaction lookup eld “btfslmobileext__WorkOrder2__c”)
When using the Android Mobile Payments app, users can now turn off the send receipt screen after authorizing or capturing a Transaction by enabling the new Custom Setting “Skip Receipt Screen”. This can be found under Setup > Custom Settings > Blackthorn Payments | Mobile Settings > Manage.
If Skip Receipt Screen = "True", then the last screen will not show the option to send a receipt.
If Skip Receipt Screen = "False", then the last screen will show the option to send a receipt.
Field Information
Field Label: Skip Receipt Screen

API Name: bt_stripe_Skip_Receipt_Screen__c
Data Type: Checkbox


Build 1.1.10
Released 06 April 2022


Enhancements
The “Require Existing Transaction for Mobile” feature is now supported in Blackthorn Mobile Payments for Android devices. This setting will block users from processing a payment in the Mobile Payments app if there isn’t an existing Transaction in Salesforce before the app is launched.


Build 1.1.9
Released 22 March 2022


Bug Fixes
After successfully completing a payment on the Mobile Payments app and attempting to complete a second transaction, the currency symbol will now appear before the charge amount on the Reader screen instead of the word “null”.
When a Mobile Payments app user clicks Support on the main navigation screen, they will now see the correct Support content.
The “Pair a reader” page in the Mobile Payments app loads correctly when the user navigates there from the side navigation.
If a user selects an Account or Contact with an associated email address, the email address will now appear on the receipt screen.
The Return To Field Service Lightning button has been added to the Mobile Payment app’s receipt screen.
We resolved a breaking change caused by the Android 12 update. When using an Android device to make a payment via the Mobile Payments app, users are now able to click Next and complete the Transaction rather than being taken back to the Field Service App.

When a user performs a Transaction in the Mobile Payment app on an Android device, they will be presented with the following Payment Methods: Card, Cash, Check, and ACH. The Money Order option is not available on Android devices.


Enhancements
When connecting a Stripe card reader, a modal screen will appear on the Mobile Payments app to ask for Bluetooth permissions for the following new permissions in Android 12 or higher.
BLUETOOTH_CONNECT: required to connect to paired Bluetooth devices.
BLUETOOTH_SCAN: required to scan and pair nearby Bluetooth devices.
BLUETOOTH_ADVERTISE: required to advertise to nearby Bluetooth devices.


Build 1.1.8
Released 14 December 2021


Breaking Change

Stripe users need to add locations to their Stripe dashboard before upgrading their Android mobile devices to the latest version. If the locations are not added rst, users will be unable to connect to a Stripe card reader.


Enhancements
The Android Mobile Payment app release includes updates to meet the new Stripe Terminal mobile SDKs version 2.0.0 requirements. To assist users and meet the locations requirement of the new SDK, Blackthorn has added the ability to add a device location to a reader. Users will see a new eld on the reader screen and can now select a location that
was previously created in their Stripe dashboard. These changes do not impact the payment functionality of the app.
When a user selects a UK Payment Gateway while using the Android Mobile Payments, the GBP currency is automatically selected. The accepted Payment Methods are "Cash" and "Card".


Build 1.1.6
Released 10 May 2021


Enhancements
Added: A Payment Gateway selector on the Tokenize Card screen now that multiple provider options are available.
Added: A validation to inform users when the Payment Gateway selected is not con gured properly.


Bug Fixes
Resolved: Clicking OK after entering card details on the tokenize screen always resulted in navigation to the home screen. We've updated the click action for this button to return the user to the tokenize screen when a card results in errors. This will allow the user to easily make updates to the card details.
Resolved: When adding an Authorize.net card using the tokenize screen there was a error being displayed and also a related Transaction record was created. The logic has been updated to prevent both of these items from occurring.


Build 1.1.5
Released 13 Apr 2021


Bug Fixes
Restored the ability to send email receipts for ACH Transactions.
Resolved: When capturing cash Transactions the Mobile Payments app was crashing. Users will now be able to complete a cash Transaction in the Mobile Payments app.


Build 1.1.3
Released 24 Mar 2021


Enhancements
Added the ability to capture Authorize.net credit card payments using manual card entry.
Added the ability to capture Authorize.net ACH payments.
Removed the ability to send email receipts for ACH transactions since they result in a "Pending" Payment Status This should be a more intuitive user experience.


Authorize.net Note

The ability to add related Accounts and Contacts to an Authorize.net Transaction will be in an upcoming release.


January 2021 Update
Released 27 Jan 2021


Enhancements
We didn't update the functionality of the app so that's why you do not see a new version number, but we did update the Play Store app listing to include a more detailed description and screenshots of the app.


Build 1.1.2
Released 23 Dec 2020


Enhancements
Added: The ability to programmatically check the battery level prior to a rmware update.


Bug Fixes
Resolved: If users were on a Payments package that didn't include all of the new eld references there was an error displaying. Logic has been put in place to determine what Payments package the Mobile Payments user has installed.


Build 1.1.1
Released 30 Nov 2020


Enhancements
Added: bt pre x for the key value used as header detail for card reader Transactions.
Added: An About page so users can view the Mobile Payments app version from the app rather than the Play Store.
Added: Mobile App Version labels for use inside of Salesforce. You can now add a eld Mobile App Version to your Transaction to see what Mobile App version was used to create the record.
Added: The ability to update the card reader rmware from the Mobile Payments app. Read more here.


Bug Fixes
Fixed a bug to correct issue of not being able to send an email receipt for cash payments.


Build 1.1.0


Released 15 Oct 2020


Enhancements
Added a disconnect button when a card reader is connected to the Mobile Payments app.
Included the Tokenize Card feature from iOS Mobile Payments in our Android application.
The Mobile Payments app now includes better error handling during token expiration.
Enhanced the Contact lookup for a more intuitive user experience.


Bug Fixes
Fixed a bug to correct issue of not being able to connect to a card reader.


Mobile Payments iOS Releases

Changes to the Mobile Apps Login Process

Starting January 20, 2026, both the Mobile Payments and Mobile Check-in apps may require new users to activate their devices during the Salesforce login process. The Salesforce article, “Device Activation for Salesforce Orgs,” explains the device activation process.


Whether a new user needs to activate their device will be determined by the customer’s org settings. Additional information can be found here: “Changes to Device Activation for Single Sign-On (SSO) Logins.”


Please review the updates below and follow the upgrade instructions for your speci c device to upgrade your Mobile Payments app.


Build 2.0.2
Released 31 June 2025


Enhancements

Saved Payment Methods for iOS

Important Note

We only support this feature on iOS mobile devices and for Stripe payment gateways. To use this feature, you must have Version 2.0.2 of the Mobile Payments app and Version 6.42 of the Payments package.


The iOS Mobile Payments app’s user interface now includes a “Save card for future payments” checkbox. When submitting a payment via a card reader or by typing in a card’s information, users can check the checkbox to allow their card information to be saved and reused for future payments. This feature can be used both online and of ine.

Admins can enable or disable this feature using the custom attribute “Enable_Reusable_Payments.” For example, the following will occur if the mobile device is of ine.

If the Payee checks "Save card for future payments," then the Payment Method Status will be set to "Valid."
If the Payee does not check the "Save card for future payments" checkbox, then the Payment Method Status will be set to "One-time."

Click here for information about adding reusable payment methods to your org.


Payment Intents
iOS Mobile Payments app users can now accept payments submitted via a card reader or entered manually. The updated payment submission process now passes the following information to Stripe: Payment Method, customer information, and whether the customer has consented to save the Payment Method by checking the box in the Mobile Payments app.

After completing the transaction, the result is newly created Transaction and Payment Method records linked to the customer in Stripe and Salesforce. If the customer checks the box to allow their Payment Method to be reused, it will also be saved for future use.

Use the Blackthorn Payments | Mobile Settings custom setting, Co nf irm P ay ment I ntents (bt_stripe__Con rm_Payment_Intents__c), to change where the Payment Intent will be con rmed.

If Co nf irm P ay ment I ntents is “True” or doesn’t exist, the Mobile Payments app processes the Payment Intent as it currently does, without con rming additional information.
If Co nf irm P ay ment I ntents is “False,” The Mobile Payments app con rms additional information before con rming the Payment Intent.

Click here for more information about Payment Intents.


Build 2.0.1
Released 09 July 2024


Enhancements
Blackthorn iOS Mobile FSL app users will now see the following message in the Blackthorn Logs, “Something went wrong. Please return to the Field Service app, refresh the record, then try again.” Previously, users received this message, “invalid ID eld: {!btfslmobileext__Open_Charge_Record_Id__c),” causing confusion.
iOS Mobile Payments app users can now use the Blackthorn Payments | Mobile Settings custom setting Sk ip Rec eipt Sc reen to determine if the last screen will show the option to send a receipt.
If Sk ip Rec eipt Sc reen = “True” (checked), the last screen won’t show the option to send a receipt.
If Sk ip Rec eipt Sc reen = “False” (unchecked), the last screen will show the option to send the receipt.
When a user opens the iOS Mobile Payments app from an existing Transaction, the Co ntac t and A c c o unt elds will have padlock icons next to them, indicating that the elds are read-only.
When the CheckForce API custom setting’s MCC Duplic atio n V alidatio n is enabled, users can con gure the error message a payer receives when they use a duplicate check to pay. To update the error message, go to the CheckForce API custom setting’s Duplic ated Erro r Message setting.


Bug Fixes
iOS Mobile Payments app users can now process payments using an ACH Payment Method and an Authorize.net gateway. Previously, users received the following error. “PM is not valid: dataDescriptor contains invalid value” and could not complete the Transaction.
When an iOS Mobile Payments app user logs out of the app, stored Payment Gateways will be removed. Previously, an intermittent issue caused the app to crash when a new user logged into the app.
If a user tries to use a non-Stripe gateway with a Stripe card reader, they will receive the following error message. “Card Readers are only supported by Stripe Payment Gateways.” Previously, the screen became stuck when a user tried to select a non-Stripe Payment Gateway, and the user didn’t receive an explanation.
When an organization does not have Check21 installed, a check is an acceptable form of payment on the iOS Mobile Payments app. The user will see a screen like the one displayed when accepting a cash payment.
iOS Mobile Payments app users can now successfully tokenize a credit card using an Authorize.net gateway. Previously, initiating the tokenization process caused the following error message to be displayed: "Transaction failed."
iOS Mobile Payments app users can now change a Payment Gateway on the home screen and click Tokenize a card without the gateway reverting to the default gateway.
The Stripe Terminal SDK was updated to version 3.3.0 to allow Mobile Payments app users to complete of ine card transactions successfully. Previously, users received an “SDK Not Connected” error message, and the of ine card transaction failed.

If you have any questions, please don't hesitate to contact Blackthorn Support.


Build 1.4
Released 28 September 2023


Enhancements

Of ine for Mobile

LIMITATION

The Field Service mobile app and new of ine functionality will ship as a known issue as the deep link does not update as intended. This is because, with its current implementation, there is no way to update the link without connecting to the internet and performing a data sync.


• Mobile Payments – Version 2.0.0 (6)
• Mobile Payments FSL Extension – Version 1.66
• Mobile Payments iOS – Version 1.4

Users now can collect payments when the iOS Mobile Payments app is of ine by turning on a new custom setting.

Location: Blackthorn Payments - Mobile Settings
Field Label: Enable Of f line Mo bile
API Name: bt_stripe__Enable_Of ine_Mobile__c
Default = unchecked
Functionality
Mobile Pay
When Enable Of f line Mo bile is checked (enabled), then the Mobile Pay button (Mobile Payments package) includes the amount and description in the URL.
When Enable Of f line Mo bile is unchecked (disabled), then the URL remains the same.
FSL
When Enable Of f line Mo bile is checked (enabled), then the Mobile Pay hyperlink (Mobile Payments FSL Extension package) includes the amount and description in the URL.
When Enable Of f line Mo bile is unchecked (disabled), then the URL remains the same. The URL will be regenerated when the amount and/or description is updated on the Transaction.


The Mobile Payments app will download and securely store a list of the available Payment Gateways the rst time the home screen loads. This allows users to capture payment details and select a valid Payment Gateway when an active internet connection isn’t available.
NOTE: Change made to a Payment Gateway in Salesforce won’t be re ected in the Mobile Payments app until the home screen is loaded while the app is connected to an internet connection.
When a user is working of ine, they will see a message reminding them that there is no active internet connection. The message will automatically appear and disappear based on whether the app can nd an active internet connection.
When the Mobile Payments app is of ine, users will see a con rmation popup after a cash payment is submitted. This functionality works similarly to the way card and ACH payments work.
When a device is of ine and a Transaction is paid, the related information will be encrypted and stored locally on the device.
Any information created or changed while the app is in of ine mode will sync to Salesforce when the app is back online where the information will be validated and processed. The information will then be deleted from the of ine storage.
A new menu option called “Pending changes (x)” was added to the left-hand navigation. When a user taps the Pending charges option, they will see a new screen with a list of Transactions that were saved while the device was of ine. The list of records will be synched and validated in Salesforce as soon as the internet connection is restored. A dialog
box will also show the user that there are pending changes if they try to log out of the app.


Tap to Pay

LIMITATION

Tap to Pay on iPhone is currently available in the US only.


Mobile Payments app users now have the option to use the Tap to Pay feature to accept contactless payments via the Stripe Terminal SDK. NOTE: Mobile wallet tokens are not reusable.
Users can now select A c c epted P ay ment Metho ds = "Tap to Pay" on the Payment Gateway, Transaction, and Payment User Override objects.
The SDK for Tap to Pay on iPhone requires iOS mobile devices to meet the following criteria:
Running iOS 16.0 or later
iPhone XS or later
The device Is not jailbroken; the device bootloader is locked and unchanged.
Note: iPads do not have NFC reading capabilities, so they are not currently supported.
Tap to Pay requires an active internet connection.
Payment details used cannot be stored and re-used if the payment used is a mobile wallet.
Pin entry as a fallback for payments that require an additional layer of authentication is not supported.

For more information about using Tap to Pay on iOS, click here.


Bug Fixes
An intermittent issue that occurred when processing a mobile card reader payment has been xed. The app will no longer attempt to update the Payment Intent while the related Transaction is being captured.
Blackthorn was incorrectly sending a “Paid = True” parameter for all Check Transactions. This caused some automation to be triggered and the status of the Transaction to be incorrectly updated. This parameter will no longer be sent for check Transactions.
To prevent duplicate Payment Gateway Customer records from being created, users can no longer edit existing Contact and Account information in the Mobile Payments app when the app is launched from an existing Transaction (from FSL or Salesforce mobile).
The Pay button located on the Check 21 check scanning page will be enabled once the user enters the check information. Previously, the Pay button remained grayed out until a refresh was performed.
If a user enters a billing email address on the Mobile Payments app, the billing email will be stored on the resulting Payment Gateway Customer, Payment Method, and Transaction records. The billing email will only be stored on these records if the email is new, and no matching records are found. If a matching record is found, the email address on the
relevant records will NOT be updated.


Build 1.1.12
Released 14 December 2021


Breaking Change

Stripe users need to add locations to their Stripe dashboard before upgrading their iOS mobile devices to the latest version. If the locations are not added rst, users will be unable to connect to a Stripe card reader.


Enhancements:

The iOS Mobile Payment app release includes updates to meet the new Stripe Terminal mobile SDKs version 2.0.0 requirements. To assist users and meet the locations requirement of the new SDK, Blackthorn has added the ability to add a device location to a reader. Users will see a new eld on the reader screen and can now select a location that was
previously created in their Stripe dashboard. These changes do not impact the payment functionality of the app.
When a user selects a UK Payment Gateway while using the iOS Mobile Payments, the GBP currency is automatically selected. The A c c epted P ay ment Metho ds are "Cash" and "Card".


Build 1.1.11
Released 10 May 2021

Enhancements:

Added: A Payment Gateway selector on the Tokenize Card screen now that multiple provider options are available.
Added: A validation to inform users when the Payment Gateway selected is not con gured properly.
Added: Updated the messaging when the location permission is disabled for the Mobile Payments app. This will inform users why they are unable to use the card reader and allow them to update their app settings.

Bug Fixes:

Resolved: When P o stal Co de was added during Transaction capture with manual card payments the value wasn't being added to the resulting Payment Method. Now users will see P o stal Co de populated on the Payment Method created in Salesforce.


Build 1.1.9
Released 5 Apr 2021

Restored the ability to send email receipts for ACH Transactions.


Build 1.1.8
Released 29 Mar 2021

Enhancements:

Added the ability to capture Authorize.net credit card payments using manual card entry.
Added the ability to capture Authorize.net ACH payments.
Removed the ability to send email receipts for ACH transactions since they result in a "Pending" P ay ment Status This should be a more intuitive user experience.
In order to match the Android Mobile Payments app UI, we added a P o stal Co de eld to manual credit card entries.
Check21 Users: We added edge detection to the check capture feature. This will prevent blurry image capture.


Authorize.net Note

The ability to add related Accounts and Contacts to an Authorize.net Transaction will be in an upcoming release.


Build 1.1.6
Released 28 Jan 2021

Enhancements:

Updated the iOS App Store app listing to include a more detailed description and screenshots of the app.


Build 1.1.5
Released 15 Dec 2020

Enhancements:

Added the platform name to the version data that appears in the Mo bile A pp V ersio n eld on the Transaction. This will further allow users to troubleshoot items by identifying from which platform a Transaction originated.
The eld labeled Mo bile A pp V ersio n will now populate a value for all types of Payment Methods not just those associated with Stripe.

Bug Fixes:

Resolved: When the iPad was oriented to the landscape position the Return to Salesforce button was moving outside of the visible screen.
Resolved: If users were on a Payments package that didn't include all of the new eld references there was an error displaying. Logic has been put in place to determine what Payments package the Mobile Payments user has installed.


Build 1.1.4
Released 23 Nov 2020

Enhancements:

The Mobile Payments app now includes better error handling during token expiration.
Added an About page so users can view the Mobile Payments app version from the app rather than the App Store.
Added Mobile App Version labels for use inside of Salesforce. You can now add a eld Mo bile A pp V ersio n to your Transaction to see what Mobile App version was used to create the record.
Added the ability to update the card reader rmware from the Mobile Payments app. Read more here.
Added messaging to the Reader page to let users know that their card reader rmware has the latest update.

Bug Fixes:

Resolved: A bug where the Scanned Amount eld wasn't always clickable in landscape view on iPad.
Resolved: An error stating 'No such payment_intent' that was being produced when a user created multiple Transactions using more than one Payment Gateway.
Resolved: An instance where an OK button was not clickable.
Resolved: Frozen Support page elements. The user can now navigate through the Support page.


Build 1.1.3
Released 15 Oct 2020

Enhancements:

Added a validation to verify if Require Ex isting T ransac tio n f o r Mo bile is enabled in Salesforce.
Check 21 Customers: Additional validations for check and money order processing.
Routing Number must be exactly 9 digits and not contain spaces/symbols.
Acceptable value lengths for Account Number include 4-19 digits and no spaces/symbols.


Build 1.1.1
Released 2 Oct 2020

Enhancements:

Added Contact and Account lookup elds on the Mobile Payments app home screen.
Provided a Tokenize Card option to tokenize credit card and associate to Contact and/or Account via lookup elds.
Incorporated the Blackthorn brand update with new colors and logo.
Added "Money Order" as a picklist value on the A c c epted P ay ment Metho ds elds on the Payment Gateway and Transaction objects.
Check 21 Customers: Added a rectangle to image capture for the check payment method.
Check 21 Customers: Devices now have the ability to reorient the rectangle when they have been rotated.
Check 21 Customers: Added validations to check processing

Bug Fixes:

Implemented a x for rounding issues that were occurring on some transactions.


Payments Error Codes
If you still have questions after looking through our Troubleshooting documentation please contact Blackthorn Support. We're happy to help!


Keys for Idempotent Requests Error
Error: "Keys for idempotent requests can only be used with the same parameters they were rst used with."

To resolve the error, complete the following steps.

1. Remove any value from the Key        eld on the Transaction.
2. Change the T ransac tio n Status to “Open”.
3. Reprocess the Transaction.


Your request to install the package Blackthorn Payments was unsuccessful
If you see long error messages while installing the app, please verify the following.

You're the system administrator of your Salesforce instance.
If you have Salesforce shield running in your org, follow our guide here.


Troubleshooting General Errors

Blackthorn no longer supports Payments APIs.

The documentation provided is a self-help resource for legacy implementations only.


Check the automated processes and rules in place on the following sources and related objects:

Objects:
Payment Gateway Customer, Payment Method, Transaction, Account, Contact, and any Transaction Parent you set in the Setup Wizard, such as an Opportunity

Look at:

Process Builders
Work ows
Validations
Apex Triggers
Field Level Permissions
Object Level Permissions (Sharing Settings)
If by a custom UI, Salesforce API or our Payments API


{"success":false,"errors":{"E_UNKOWN_ERROR":"PDF Generator Error"}} OR A time-out message: Application Error - an error occurred in the application and your page could
not be served....
Click here to reauthorize your production org.

Click here to reauthorize your sandbox org.


Facing error while setting up webhook endpoint in Stripe OR Authorize.net OR in Experience Clouds with Virtual Terminal
You may see the following errors while setting up the endpoint in Stripe/Auth.net dashboard or if you are using the Virtual Terminal in the Salesforce Experience Cloud.

1. Test Webhook Error:500 (stripe)
2. Test Webhook Error:400 (stripe)
3. Error occurred in connecting to endpoint (Auth.net)
4. Result:[id=null, message=Problem with nding PG by label primary . List size: 0, success=false]” with an error 400 (stripe)
5. Unable to nd a Payment Gateway for id=null (Virtual Terminal in the Experience Cloud)

To resolve this, please follow the steps below.

1. Login to Salesforce, navigate to Setup > Sharing settings > Payment Gateway > Change the Default External Access from Private to Public Read Only.
2. Uncheck the Secure guest user record access option. It overrides the Default External Access and sets it to private for every object including the Payment Gateway (PG).


btcombobox error when trying to upgrade.
If you receive this issue when installing or upgrading Payments, the component must implement at least one of exipage:availableForAllPageTypes, exipage:availableForRecordHome interface. BT_comboboxResult: The component must implement at least one of exipage:availableForAllPageTypes, exipage:availableForRecordHome interface.

Please remove the btcombobox component from a lightning page. Odds are you have it on the Opportunity lightning page layout.


Permission error: bt_stripe.SObjectSelector.FLSException: You do not have permission to read the eld OtherStreet: (bt_stripe)
To resolve this error, please upgrade to the latest version of Payments from here.


Row with duplicate name at index:2


This occurs when there are duplicate entries created for the Transaction parent. You will not be able to proceed ahead until you delete the duplicates. To do this, go to Setup > Custom Settings > Transaction parents > Manage. Click "Del" next to the duplicate item in the list.


The Transaction can't be authorized.


If you have received this error, check to make sure the Payment Method related to this Transaction is not an ACH Payment Method. ACH Payment Methods are not able to authorize Transactions.


Test webhook error: Domain unknown.


If you have received this error, check your Webhook URL. If you are using Blackthorn Payments with a developer account remove the ".secure". If you are using any other account, make sure the ".secure" is included.


Customer cus_AwROhSB7FyifGc does not have a linked source with ID ba_1AaYW9BQbf3hbNo9B8juK4lo
This error means that the related Payment Method on the Transaction no longer has a valid Card ID Token. What this means is most likely the card or ACH token was deleted in Stripe. Please view related Stripe Payment Gateway Customer record to verify if there is a valid Payment Method form. If there is no longer a valid Payment Method form, create a new
payment for this Stripe Payment Gateway Customer OR edit the existing Payment Method with the updated card/ACH information, remove the values from the card id and customer id, select save and this Payment Method will sync back to Stripe.


Terminal error on new record screen


This error means you have a required eld that needs a value in order to create the new record and most likely that eld is not in the Virtual Terminal's new record screen. To x, verify all required elds are in the Virtual Terminal's new record screen. Click here for instructions on adding elds to your Virtual Terminal.


“No such customer: 'cus_**************'” Error
Q: I am trying to create a new Payment Method, but got “No such customer: 'cus'.” W hat does it mean?

A: The “No such customer: 'cus_**************'” error means that the customer does not exist on the connected account that you are trying to charge. Please create a new Payment Gateway Customer and try again.


Payments FAQ
If you still have questions after looking through our Troubleshooting documentation please contact Blackthorn Support. We're happy to help!


Payment Gateways

Set Up a Payment Gateway for a Newly Acquired Company
What are the best practices for setting up a Payment Gateway for a company we've recently acquired?

We suggest creating a new Stripe account and a new Payment Gateway for your newly acquired company. From Blackthorn's end, we can support two gateways - one for each company. To learn more about creating and managing multiple Stripe accounts, click here. If you have more Stripe-speci c questions, please reach out to Stripe support.


Spreedly and the Payment Gateway Customer record
Why isn’t a Payment Gateway Customer record created when I add a Payment Method via the Virtual Terminal with Spreedly as the Payment Gateway?

Since Spreedly does not have an equivalent record (ex. user id) for customers, a Payment Gateway Customer record will not be created in Salesforce.


Virtual Terminal

Blocked by Content Security Policy error on Virtual terminal


Follow step 4 in this guide to ensure your domain is allowlisted.


Can't See the Related To Field on the Virtual Terminal
Why can't I see the Related T o eld on the Virtual Terminal?

The reason you cannot see the Related T o eld is that there is an issue with your Transaction Parent settings. Please navigate to Custom Settings, click manage next to Transaction Parents, verify that all records have a Transaction eld with the correct API format.


Can't See the BT Payments LWC Virtual Terminal in the Experience Cloud Builder
I can’t see the BT Payments LWC Virtual Terminal component in the Experience Cloud Builder. How do I x that?

If an Experience Cloud user cannot see the BT Payments LWC Virtual Terminal component, please verify the following.

The digital experience user has a Payment License, if in production.
The user has been assigned the correct permission set(s).


Transactions

Remove a Transaction Parent Object
How do I remove a Transaction parent object?

Please see our Transaction documentation.


Update Scheduled Transactions
If the user who installed Blackthorn Payments is no longer active, schedule jobs will fail. Those jobs include capturing Transactions and Webhook Services.

1. Navigate to Schedule Jobs.
Lightning/Classic: Setup | In the Quick Find/Search type in and click "Scheduled Jobs".
2. Click "Del" next to Blackthorn | Payments Daily Captures.
3. Navigate to Apex Classes.
Lightning/Classic: Setup | In the Quick Find/Search type in and click "Apex Classes".
4. Click the Schedule Apex button.
5. Job Name: "Blackthorn | Payments Daily Captures"
6. Apex Class: Select "Transaction_Scheduler"
7. Apex Execution: Select "Weekly" | Check "Sunday-Saturday" | Start = Today's Date | End = As far out as possible | Preferred Start Time = 1:00AM
8. Click Save.


Stripe

Stripe Sync Job Keeps Running
When you sync the gateway data the sync job keeps running even after hours. The sync job keeps on restarting as long there are Stripe customers found. To solve the issue:


Use the lter to sync with dates


Once the job is done syncing for the de ned dates, it'll show as completed.


Invoice Button Isn't Working
Why isn’t the Send Invoice button on the Invoice object sending the Invoice to the customer?

Clicking the button sends the Invoice from Stripe, and Stripe’s email settings control the process. If you don’t see an email, it may be an issue with your Stripe email settings or a restriction on Stripe’s side that is preventing emails from being sent for test mode Invoice s.


Prevent the Invoice from Being Sent Immediately
How do we prevent the Invoice Status from changing to “Sent” immediately after the Invoice is pushed to Stripe from Salesforce?

To stop the Invoice Status from changing to “Sent” immediately after creating and pushing it to Stripe, you must disable the Disable Send I nv o ic e I mmediately custom setting.

Complete the following steps to disable the custom setting.

1. Go to Setup.
2. In the Quick Find box, search for and click “custom settings.”
3. Click Manage next to Blackthorn Pay - Trigger Settings.
4. Click Edit.
5. Set Disable Send I nv o ic e I mmediately = “True” (checked).
6. Click Save.


Remove a Payment Method Parent Object
How do I remove Payment Method parent object?

Please see our Payment Methods documentation.


Unable to see Payment Objects in the Experience Cloud
If the digital experience user is unable to see the payment object (Example - Invoice) in the Experience Cloud, please verify the following.

1. The user has a Payments License (If production).
2. The user has assigned Blackthorn | Payments (Community/Platform User) permission set assigned.
3. The organization-wide default for Payment Gateway = "Public Read-Only."


Updating Webhook Record Cleanup
1. Navigate to Schedule Jobs.
Lightning/Classic: Setup | In the Quick Find/Search type in and click "Scheduled Jobs".
2. Click "Del" next to Blackthorn | Payments Webhook Record Cleanup.
3. Navigate to Apex Classes
Lightning/Classic: Setup | In the Quick Find/Search type in and click "Apex Classes".
4. Click the Schedule Apex button.
5. Job Name: "Blackthorn | Payments Webhook Record Cleanup"
6. Apex Class: Select "WebhookCleanupJob_Scheduler"
7. Apex Execution: Select "Weekly" | Check "Sunday-Saturday" | Start = Today's Date | End = As far out as possible | Preferred Start Time = 1:00AM
8. Click Save.


Update Checkout Payment Screen
Can I update the Attendee-related elds on the payment screen's page layout?

No, the payment screen's page layout can't be con gured because the selected Payment Gateway automatically formats it.


Deactivating a User who Activated Scheduled Jobs
1. Before the original user’s account/pro le is deactivated, have a second user perform the following steps.
Go to the Blackthorn | Payments Admin tab.
Click the Scheduled Jobs tab.
Click the Schedule Recommended Payments Jobs button and any other relevant buttons on this tab.
Go to the Blackthorn | PayLink Setup Wizard tab.
Click Grant Access to authorize PayLink.
2. Remove the original user’s Payments license permission set(s).


Duplicate Rule References a Missing Matching Rule
Error: "conference360_Attendee_c.BT_Event_Attendee_Duplicate_Rule: This duplicate rule references a matching rule that doesn't exist. Update the referenced matching rule"

If you experience this error message when performing an upgrade, create the following matching and duplicate rule in your org.

Matching Rule Name: BT Events Attendee Matching Rule
API Name: BT_Events_Attendee_Matching_Rule
Description: matched attendee under an event
Matching Criteria : (Attendee: EventEXACTMatchBlank = FALSE) AND (Attendee: Email2EXACTMatchBlank = FALSE) AND (Attendee: First_Name2FUZZY: FIRST NAMEMatchBlank = FALSE) AND (Attendee: Last_Name2FUZZY: LAST NAMEMatchBlank = FALSE)
Duplicate Rule Name: BT Event Attendee Duplicate Rule
API Name: BT_Events_Attendee_Matching_Rule
Record level security: Bypass sharing rules

Please make sure the matching rule references the duplicate rule. Once done, try upgrading the app again.


Payments Troubleshooting
If you still have questions after looking through our Troubleshooting documentation please contact Blackthorn Support. We're happy to help!


Keys for Idempotent Requests Error
Error: "Keys for idempotent requests can only be used with the same parameters they were rst used with."

To resolve the error, complete the following steps.

1. Remove any value from the Key        eld on the Transaction.
2. Change the T ransac tio n Status to “Open”.
3. Reprocess the Transaction.


Spreedly and the Payment Gateway Customer record
Why isn’t a Payment Gateway Customer record created when I add a Payment Method via the Virtual Terminal with Spreedly as the Payment Gateway?

Since Spreedly does not have an equivalent record (ex. user id) for customers, a Payment Gateway Customer record will not be created in Salesforce.


Your request to install package "Blackthorn Payments" was unsuccessful
If you see long error messages while installing the app, please verify the following..

You're the system administrator of your Salesforce instance.
If you have Salesforce shield running in your org, follow our guide here.


Blocked by Content Security Policy error on Virtual terminal


Follow step 4 in this guide to ensure your domain is allowlisted.


Troubleshooting general errors

Blackthorn no longer supports Payments APIs.

The documentation provided is a self-help resource for legacy implementations only.


Check the below automated processes and rules in place on the following sources and related objects:

Objects:
Payment Gateway Customer, Payment Method, Transaction, Account, Contact, and any Transaction Parent you set in the Setup Wizard, such as an Opportunity

Look at:

Process Builders
Work ows
Validations
Apex Triggers
Field Level Permissions
Object Level Permissions (Sharing Settings)
If by a custom UI, Salesforce API or our Payments API


{"success":false,"errors":{"E_UNKOWN_ERROR":"PDF Generator Error"}} OR A time-out message: Application Error - an error occurred in the application and your page could
not be served....
Reauth using this link: https://documentlink.billing360.io/auth/salesforce.


Facing error while setting up webhook endpoint in Stripe OR Authorize.net OR in Experience Clouds with Virtual Terminal
You may see the following errors while setting up the endpoint in Stripe/Auth.net dashboard or if you are using the Virtual Terminal in the Experience Cloud.

1. Test Webhook Error:500 (stripe)
2. Test Webhook Error:400 (stripe)
3. Error occurred in connecting to endpoint (Auth.net)
4. Result:[id=null, message=Problem with nding PG by label primary . List size: 0, success=false]” with an error 400 (stripe)
5. Unable to nd a Payment Gateway for id=null (Virtual Terminal in the Experience Cloud)

To resolve this, please follow the below steps -

1. Login to Salesforce, navigate to Setup > Sharing settings > Payment Gateway > Change the Default External Access from Private to Public Read Only.
2. Uncheck the Secure guest user record access option. It overrides the Default External Access and sets it to private for every object including the Payment Gateway (PG).


btcombobox error when trying to upgrade.
If you receive this issue when installing or upgrading Payments, the component must implement at least one of exipage:availableForAllPageTypes, exipage:availableForRecordHome interface. BT_comboboxResult: The component must implement at least one of exipage:availableForAllPageTypes, exipage:availableForRecordHome interface.

Please remove the btcombobox component from a lightning page. Odds are you have it on the Opportunity lightning page layout.


Permission error: bt_stripe.SObjectSelector.FLSException: You do not have permission to read the eld OtherStreet: (bt_stripe)
To resolve this error, please upgrade to the latest version of Payments from here.


Row with duplicate name at index:2


This occurs when there are duplicate entries created for the Transaction parent. You will not be able to proceed ahead until you delete the duplicates. To do this, go to Setup > Custom Settings > Transaction parents > Manage. Click "Del" next to the duplicate item in the list.


The Transaction can't be authorized.


If you have received this error, check to make sure the Payment Method related to this Transaction is not an ACH Payment Method. ACH Payment Methods are not able to authorize Transactions.


Removing the Transaction or Payment Method parent object.
Please see our Transaction and Payment Methods documentation.


Test webhook error: Domain unknown.


If you have received this error, check your Webhook URL. If you are using Blackthorn Payments with a developer account remove the ".secure". If you are using any other account, make sure the ".secure" is included.


Unable to see Payment objects in the Experience Cloud
If the digital experience user is unable to see the payment object (Example- Sales document) in the the Experience Cloud, please verify the following -

1. User has a Payment License (If production)
2. User has assigned Blackthorn | Payments (Community/Platform User) permission set assigned.
3. The organization-wide default for Payment Gateway = Public Read-Only.


Customer cus_AwROhSB7FyifGc does not have a linked source with ID ba_1AaYW9BQbf3hbNo9B8juK4lo
This error means that the related Payment Method on the Transaction no longer has a valid Card ID Token. What this means is most likely the card or ACH token was deleted in Stripe. Please view related Stripe Payment Gateway Customer record to verify if there is a valid Payment Method form. If there is no longer a valid Payment Method form, create a new
payment for this Stripe Payment Gateway Customer OR edit the existing Payment Method with the updated card/ACH information, remove the values from the card id and customer id, select save and this Payment Method will sync back to Stripe.


Can't see the Related To eld on the Virtual Terminal
The reason you cannot see the Related To eld is that there is an issue with your Transaction Parent settings. Please navigate to Custom Settings, click manage next to Transaction Parents, verify that all records have a Transaction eld with the correct API format.


Terminal error on new record screen


This error means you have a required eld that needs a value in order to create the new record and most likely that eld is not in the Virtual Terminal's new record screen. To x, verify all required elds are in the Virtual Terminal's new record screen. Click here for instructions on adding elds to your Virtual Terminal.


Updating Scheduled Transactions
If the user who installed Blackthorn Payments is no longer active, schedule jobs will fail. Those jobs include capturing Transactions and Webhook Services.

Navigate to Schedule Jobs.

Lightning/Classic: Setup | In the Quick Find/Search type in and click "Scheduled Jobs".

Click "Del" next to Blackthorn | Payments Daily Captures.
Navigate to Apex Classes

Lightning/Classic: Setup | In the Quick Find/Search type in and click "Apex Classes".

Click Schedule Apex button
Job Name: "Blackthorn | Payments Daily Captures"
Apex Class: Select "Transaction_Scheduler"


Apex Execution: Select "Weekly" | Check "Sunday-Saturday" | Start = Today's Date | End = As far out as possible | Preferred Start Time = 1:00AM
Click Save.


Updating Webhook Record Cleanup
Navigate to Schedule Jobs.

Lightning/Classic: Setup | In the Quick Find/Search type in and click "Scheduled Jobs".

Click "Del" next to Blackthorn | Payments Webhook Record Cleanup.
Navigate to Apex Classes

Lightning/Classic: Setup | In the Quick Find/Search type in and click "Apex Classes".

Click Schedule Apex button
Job Name: "Blackthorn | Payments Webhook Record Cleanup"
Apex Class: Select "WebhookCleanupJob_Scheduler"
Apex Execution: Select "Weekly" | Check "Sunday-Saturday" | Start = Today's Date | End = As far out as possible | Preferred Start Time = 1:00AM
Click Save.


Stripe Sync Job Keeps Running
When you sync the gateway data the sync job keeps running even after hours. The sync job keeps on restarting as long there are stripe customer found. To solve the issue:

Use the lter to sync with dates


Once the job is done syncing for the de ned dates, it'll show as completed.


“No such customer: 'cus_**************'” Error
Q: I am trying to create a new Payment Method, but got “No such customer: 'cus'.” W hat does it mean?

A: The “No such customer: 'cus_**************'” error means that the customer does not exist on the connected account that you are trying to charge. Please create a new Payment Gateway Customer and try again.


DocumentLink Error Codes and Messages
Status                           API Error/Console Error                                                                             Description                                                                                                                      Error on Client Side
400      E_INVALID_CODE: Invalid documentlink code                             Invalid document code, it doesn't have a valid structure.                                                            This DocumentLink is not valid. Please make sure you entered the correct URL.
This DocumentLink account has been suspended. If you are the account owner, please contact us to have your account re-activated at Blackthorn
402      E_UNLICENSED: No active license available                             There is no active license for that Org.
Support.
This DocumentLink account is not set up correctly. If you are the account owner, please contact us for help with setting up your account at Blackthorn
403      E_NOT_AUTHORIZED: App is not authorized to access org                 License does not have an OAuth User, requires authentication.
Support.
Document isn't found, either because it doesn't exist or there is a typo in the url. The document code has a valid
404      E_NOT_FOUND: Document not found                                                                                                                                                            This document is not available.
structure.
500      E_NOT_PAYABLE: Document is no payable                                 There is no payment gateway set.                                                                                     Oops... Something unexpected just happened. Please try again or let us know if the issue persists.
This DocumentLink account is not set up correctly. If you are the account owner, please contact us for help with setting up your account at Blackthorn
502      E_INVALID_CLIENT: Payments API is not enabled                         Payments API is not enabled/available for this org.
Support.
422      E_CAPTURE_ERROR                                                       Capture error, payment status is not 'Captured'.                                                                     No error shown on Client side.
422      E_CAPTURE_ERROR: Failed to close transaction                          Capture error, transaction status is 'Open'.                                                                         No error shown on Client side.
422      E_CAPTURE_ERROR: ???????                                              Payment failed, speci c error message returned                                                                       No error shown on Client side.
E_PROCESS_ERROR: No successful payment method received from
424                                                                            Payment method list is empty on response when creating new payment methods.                                          The transaction failed after the payment capture. Please contact XXXXX and con rm payment was received and attributed to this document.
response
424      E_PROCESS_ERROR: Cannot locate a captured transaction                 Transaction list is empty on processing request.                                                                     The transaction failed after the payment capture. Please contact XXXXX and con rm payment was received and attributed to this document.
500      E_SERVICE_ERROR: Payments API is disabled                             Blackthorn API has not been enabled for this org.                                                                    Oops... Something unexpected just happened. Please try again or let us know if the issue persists.
500      E_SERVICE_ERROR: ??????                                               Server errors when sending requests to Salesforce API.                                                               Oops... Something unexpected just happened. Please try again or let us know if the issue persists.
500      E_RESPONSE_ERROR: ??????                                              Error on the capture request, speci c error message returned.                                                        Oops... Something unexpected just happened. Please try again or let us know if the issue persists.
500      E_RESPONSE_ERROR: No successful transactions received from response   Transaction list is empty on capture request.                                                                        Oops... Something unexpected just happened. Please try again or let us know if the issue persists.
500      E_RESPONSE_ERROR: Payment was declined                                Transaction status is 'Failed' on capture request.                                                                   Oops... Something unexpected just happened. Please try again or let us know if the issue persists.


Payments: Release Notes & Webinar Recordings
We update our Payments package often with new features and bug xes. You can always get the latest stable version of the Payments package from the Candy Shop.


Release Notes

Latest Version
February 2026 - Version 6.57


Older Versions
January 2026 - Version 6.52
November 2025 - Version 6.49
October 2025
September 2025 - Version 6.48
August 2025 - Version 6.44
July 2025 - Version 6.42
June 2025 - Version 6.40
May 2025 - Version 6.37
April 2025 - Version 6.32
March 2025 - Version 6.3
February 2025 - Version 6.29
January 2025 - Version 6.28


2024

December 2024 - Version 6.27
November 2024 - Version 6.26
October 2024 - Version 6.25
September 2024 - Version 6.23
August 2024 - Version 6.22
July 2024 - Version 6.20
June 2024 - Version 6.19
May 2024 - Version 6.18
April 2024 - Version 6.17
March 2024 - Version 6.16
February 2024 - Version 6.13
January 2024 - Version 6.11


2023
December 2023 - Version 6.8
November 2023 - Version 6.6
October 2023 - Version 6.4
September 2023 - Version 6.3
August 2023 - Version 6.0.1
July 2023 - Version 5.108.2
June 2023 - Version 5.106
May 2023 - Version 5.103
April 2023 - Version 5.99.1
March 2023 - Version 5.95
February 2023 - Version 5.93
January 2023 - Version 5.91


2022
December 2022 - Version 5.85
October 2022 - Version 5.76
September 2022 - Version 5.71.2
August 2022 - Version 5.70
July 2022 - Version 5.66
June 2022 - Version 5.63
April 2022 - Version 5.58
March 2022 - Version 5.53
February 2022, version 5.49


2021
December 2021, version 5.46
November 2021, version 5.41
October 2021, version 5.34
September 2021, version 5.33
August 2021, version 5.31
July 2021, version 5.29
June 2021, version 5.24
May 2021, version 5.22
April 2021, version 5.20
March 2021, version 5.17
February 2021, version 5.15
January 2021, version 5.14


Mobile Payments App
Mobile Payments iOS Releases
Mobile Payments Android Releases


Release Webinar Recordings
View our YouTube Playlist for our most recent videos!

January 2021
December 2020
November 2020
October 2020
September 2020
June 2018
March 2018


Important De nitions

BT Salesforce Release
The following applies to a Salesforce release.

Salesforce xes REQUIRE a package upgrade to see and utilize the xes/enhancements.
Only users with a System Administrator pro le or the ModifyAllData system permission can install packages.


Webapp Release
The following applies to a Webapp Release (previously referred to as a platform release).

Webapp xes/changes usually do not require updates to the Salesforce package.
These updates are applied to all customers automatically; you cannot opt-out.


Monthly Milestone Release
A Monthly Milestone Release includes feature enhancements and bug xes for the BT Salesforce Release and the Webapp Release.


Major Release
The following list describes a Major release.

Includes the four previous Monthly Milestone Releases.
Occurs two months after a Salesforce Seasonal Release.


Blackthorn 2025 Release Dates
Both Salesforce and Webapp releases are delivered on the same day. The second Tuesday of the month is our tentative target date for releases, starting at 8 am Eastern time. However, to assure quality, all dates are tentative and may change without notice. Use the following dates to plan and prepare for our 2025 releases.

January 2025 – Monthly Milestone

BT Salesforce Release: 1/14/2025 1/21/2025
Webapp Release: 1/14/2025 1/21/2025

February 2025 – Monthly Milestone

BT Salesforce Release: 2/11/2025 3/5/2025
Webapp Release: 2/11/2025 2/19/2025

March    2025 – Monthly Milestone

BT Salesforce Release: 3/11/2025 3/18/2025
Webapp Release: 3/11/2025 3/18/2025


April 2025 – Major Release

BT Salesforce Release: 4/8/2025 4/22/2025
Webapp Release: 4/8/2025 4/22/2025


May 2025 – Monthly Milestone

BT Salesforce Release: 5/13/2025 5/27/2025
Webapp Release: 5/13/2025 5/27/2025

June 2025 – Monthly Milestone

BT Salesforce Release: 6/10/2025 7/1/25
Webapp Release: 6/10/2025 7/1/25

July 2025 – Monthly Milestone

BT Salesforce Release: 7/8/2025
Webapp Release: 7/8/2025


August 2025 – Major Release

BT Salesforce Release: 8/12/2025 8/26/2025
Webapp Release: 8/12/2025 8/26/2025

September 2025 – Monthly Milestone

BT Salesforce Release: 9/9/2025 10/7/2025
Webapp Release: 9/9/2025 10/7/2025

October 2025 – Monthly Milestone

BT Salesforce Release: 10/14/2025 10/28/2025
Webapp Release: 10/14/2025 10/28/2025

November 2025 – Monthly Milestone


BT Salesforce Release: 11/11/2025 11/18/2025
Webapp Release: 11/11/2025 11/18/2025


December 2025 – Major Release

BT Salesforce Release: 12/9/2025 12/16/2025
Webapp Release: 12/9/2025 12/16/2025


February 2026 - Version 6.57
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Table of Contents
(Release Date: February 18, 2026)

Bug Fixes
Enhancements
Known Issues
Upgrade Instructions
Important De nitions


Bug Fixes
Stripe Metadata Mappings: If a user creates Stripe metadata mappings with the Transaction object (source object), future Transaction records created by registering for an Event will automatically send all metadata in the mapped elds to Stripe. Previously, only the metadata from the Transaction P ay ment Metho d Billing Email was sent to Stripe. The
metadata from the other mapped elds was not sent. (Known Issue: 000005024)
Transactions: If a user partially captures an authorized Transaction that uses a Payment Method on a Stripe gateway, the Transaction will be partially captured after clicking the Capture button or checking the Capture eld. The Transaction’s T ransac tio n Status will change from “Process” to “Completed,” and the P ay ment Status will be set to
“Partially Captured.” Previously, the P ay ment Status remained set to “Authorized.”
LWC Virtual Terminal: When using the LWC Virtual Terminal component inside a Salesforce Flow, declined transactions will now properly display error messages and "card declined" noti cations instead of automatically advancing to the next screen. The component will now correctly handle transaction failures and provide clear feedback to users about
the transaction status. This x ensures proper error handling in Flow implementations where users need to see transaction results before proceeding. When a payment is declined with error code 2 or other failure responses, the Virtual Terminal will display appropriate error messages and wait for user acknowledgment rather than progressing
automatically through the ow. Previously, when a transaction was declined using the LWC Virtual Terminal inside a ow, the component failed to display error or "card declined" messages and instead automatically advanced to the next screen as if the transaction was successful. This behavior mirrored issues from the existing PaymentChargeFlow
component where success messages appeared regardless of actual transaction results.


Enhancements
Spreedly: When the tokenization option is enabled for Spreedly Payment Gateways in production, users can successfully create a Payment Method in the Virtual Terminal or via a PayLink. The tokenizer iframe URL now includes the necessary Spreedly authorization components. Previously, authentication issues were caused by Spreedly's enhanced security
“Enable Secure Tokenization” setting. The system returned a 401 error and a generic "failure to create payment method" message.


Accessibility
Updates were made to the LWC Virtual Terminal to enhance the user experience, especially for keyboard navigation and assistive technologies.

When a user tabs to the Related T o eld, it will be announced. Once in the eld’s lookup, the user can tab through or use the down/up arrows to navigate the list. Each option will be announced as it is selected.
The information announced for the Desc riptio n eld’s tooltip now matches what a user hears when accessing the eld’s tooltip from a community page, a record page, or screen ow.
Fields with a red asterisk will include “star” when the elds are announced.
When a success or error message occurs, it will be announced.
If a lookup eld includes the option to create a new Account, Contact, Lead, or Payment Method, and a user tabs or uses the keyboard to navigate to the Create New option, a new window will open, allowing the user to create the new record. Afterwards, the user is returned to the eld where it was created.
When creating a new Payment Method, a user can also press Shift-TAB to navigate through the elds in reverse order.


Known Issues
Events Salesforce – Issue with Processing Fees and the Invoice: Although a user has paid the full amount due and the checkout process is complete, the related Invoice shows a Balanc e Due of the amount in the Fee A mo unt eld, while the Status eld is set to “Ready To Bill,” and the P ay ment Status eld is set to “Partially Paid.”
PayLink - Accessibility Issue: Users cannot switch between the Card and Bank (ACH) tabs when navigating with the Space and Enter keys on a keyboard. This will be xed in the April 2026 PayLink Webapp release.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


January 2026 - Version 6.52
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Table of Contents
(Release Date: January 27, 2026)

Bug Fixes
Enhancements
Upgrade Instructions
Important De nitions


Bug Fixes
Refunds: If a user initiates a refund for a payment Transaction from Stripe, the resulting refund Transaction in Salesforce will include a value from Stripe in the T ransac tio n I D eld. Previously, the Transaction’s T ransac tio n I D eld was blank.
Line Items: From an Invoice, a user can change the value in a Line Item’s Disc o unt Co de eld without causing an error or deleting the Line Item record. (Known Issue: 000003287)
Permissions: Users can complete a payment without Read access to the Transaction’s (custom) parent object and/or elds when accepting a payment by entering a valid card or bank account number on the Mobile Payments app, or accepting a payment by entering a valid Payment Method on the Transaction record and clicking Charge. A new validation
was implemented to prevent permission errors related to Transaction parent elds when a user with insuf cient eld access tries to accept a payment via the Mobile Payments app. Previously, users received insuf cient object and eld access permission errors when trying to accept a payment via the Mobile Payments app. (Known Issue: 000005099)


Virtual Terminal
After a user con gures the Virtual Terminal mapping to use the Source Parent Object and Source Parent Field, the Virtual Terminal will retrieve Parent eld values and populate target elds as expected, regardless of which Virtual Terminal is used – the old version or the LWC Virtual Terminal. Previously, the LWC Virtual Terminal would not load, and the
old Virtual Terminal would load but not apply mappings properly or load the Payment Method. (000005029)
The Sho w A ddress eld on the Blackthorn Payments | Virtual Terminal’s Custom Settings is enabled. If a user tries to create a new Payment Method to process a single-charge Transaction using the Aura Virtual Terminal component, they will see the Add+ and Reset buttons on the new Payment Method screen. Previously, the buttons were no longer
visible because Salesforce updated its rendering of iframed components.


Enhancements

LWC Virtual Terminal and Flows
The user experience of submitting a payment with the BT Payments LWC Virtual Terminal in a ow has been recon gured to create a more straightforward experience. Previously, the placement of the Process button led users to miss clicking it or to click it multiple times, resulting in duplicate payments.

Now, when submitting a payment using the BT Payments LWC Virtual Terminal in a ow, the following will occur:

If the Hide T ransac tio n Butto n setting in the Virtual Terminal ow component is set to “True,” the Process button won’t be visible, and clicking the Next/Finish button will trigger the Transaction to be processed.
If a payment attempt fails, the user will see an error message and a retry option.
If a payment is successfully processed, the ow automatically advances the user to the next step.
Duplicate Transactions will not be created.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


November 2025 - Version 6.49
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Table of Contents
(Release Date: November 19, 2025)

Bug Fixes
Enhancements
Upgrade Instructions
Important De nitions


Bug Fixes
Stripe Transaction: A user can capture a Transaction (payment) when the Name or Description elds are mapped from the Transaction via Stripe Metadata Mapping, and the Transaction’s status elds will be updated accordingly. Previously, when a user clicked the Capture button on the Transaction, they got an error. (Known Issue: 000004947)
Invoices: When applying/removing a discount Code to/from an Invoice after an Event registration, the related Line Items will re ect the correct amounts, and the Invoice’s Fee A mo unt will be recalculated. Previously, the Invoice’s Fee A mo unt value was not recalculated.
Virtual Terminal: If the Blackthorn Payments | Virtual Terminal’s Hide Bank T ab or Hide Card T ab custom setting is enabled, then the Payment Method labels (“Name on Card,” “Card Number,” “Name on account,” and “Account holder type“) will be fully visible. Previously, the labels were cut off on the Payment Method page in Virtual Terminal.


Authorize.net Transaction
If the values in a captured Transaction match or exceed the Authorize.net fraud detection settings, the Transaction’s T ransac tio n Status eld will update to “On Hold.” The “On Hold” value prevents a reattempt Transaction from being created before the Transaction can be reviewed and approved or declined.

If an “On Hold” Transaction is voided or declined, the T ransac tio n Status will be updated to “Failed” and no reattempt Transaction will be created.
If the Transaction is approved, the T ransac tio n Status will be changed to “Completed.”

Transactions that fall outside the Authorize.net fraud detection settings and do not require review will not have their T ransac tio n Status set to “On Hold.” Instead, a reattempt Transaction will be created. Previously, failed Transactions were reprocessed and charged, even though the initial and the reattempt failed. (Known Issue: 000004119)


Enhancements
Payment Gateway Customers: When a user creates a new Payment Method, one of the following scenarios will occur. Previously, when a new Payment Method without an existing Payment Gateway Customer (PGC) was created, the Payment Method was incorrectly associated with an existing PGC from the same Account rather than creating a new
PGC.
Scenario 1: A Contact exists on the Payment Method, and the Contact is associated with an Account. If Salesforce nds a PGC where both the Contact and Account match, then the new Payment Method will be linked to that PGC.
Scenario 2: A Contact exists on the Payment Method. The related Account and Contact do not have a matching PGC. Salesforce searches for an existing PGC with a billing email address that matches the email address associated with the Payment Method. If the resulting PGC has the same Account, then the Payment Method will be linked to
that PGC.
Scenario 3: A Contact exists on the Payment Method, and the Contact is associated with an Account. Salesforce cannot nd a matching PGC by searching Contact and Account records, nor by searching by the billing email address. Therefore, Salesforce creates a new PGC for the Payment Method. A new PGC will be created even if another PGC is
related to the Account that is associated with the PM. If they do not match, they should not get associated.
Error Tracking: We enhanced our system's ability to track and diagnose payment processing issues, enabling our Support team to identify and resolve problems more quickly. The changes include:
Better error tracking across payment processing components
Capturing more detailed information when payment issues occur
Improved system monitoring to catch problems faster


DocumentLink

Enhancements
The color palette used for DocumentLink has been updated to use neutral colors instead of the traditional Blackthorn palette.
The following updates were made to DocumentLink to remove accessibility-related errors.
Increase the color contrast ratio between text and background.
Remove redundant alternative text.
De ne page regions using semantic HTML elements (header, nav, main, footer) or appropriate ARIA roles.


Known Issue
Users must have Read access to any elds added to the “Blackthorn Pay - Transaction Parent” custom setting. If Read access isn’t granted, users will receive an ‘insuf cient permissions’ error when using the Mobile Payments app. This issue is scheduled to be xed in early 2026.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacts extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


October 2025
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Table of Contents
Important Note
Spreedly Reminder
Upgrade Instructions
Important De nitions


Important Note
There is no release for Payments for October 2025. The next Payments release will be in November 2025.


Spreedly Reminder
Updates were made to the storage of sensitive data. Both the Spreedly Payment Gateway access token and the Payment Intent Client Sec ret eld are now encrypted. Current Spreedly users must reauthorize the gateway after upgrading Payments to Version 6.45 or higher. These settings are automatically con gured during new installations of the Payments app.

W hat does reconnecting mean? Reconnecting requires you to open each existing Spreedly gateway and click Connect Spreedly Gateway. This process encrypts your Spreedly key.
W hat happens if you don’t reconnect after upgrading to a new version? Until each Spreedly gateway is reconnected, all Transactions routed through that gateway will fail — meaning no payments will process for that gateway.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


September 2025 - Version 6.48
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Table of Contents
(Release Date: 10/14/2025)

Bug Fix
Enhancements
PayLink
Field/Layout Updates
Upgrade Instructions
Important De nitions


Bug Fix
Line Items: If an Attendee registers for a waitlisted Session, the related Invoice’s Line Item for the waitlisted Session will have Total = “0.” Previously, the waitlisted Session’s Line Item listed the Total as the actual cost of the Session. (Known Issue: 000004779)


Enhancements
Spreedly: As part of Salesforce’s security requirements and to better protect your sensitive data, all Spreedly keys, including the Spreedly Payment Gateway access token and the Payment Intent Client Sec ret eld must now be encrypted. Starting with version 6.48, customers with existing Spreedly gateways must manually reconnect those gateways in
the Dashboard after upgrading.
W hat does reconnecting mean? Reconnecting requires you to open each existing Spreedly gateway and click Create Spreedly Gateway. This process encrypts your Spreedly key.
W hat happens if you don’t reconnect after upgrading to a new version? Until each Spreedly gateway is reconnected, all Transactions routed through that gateway will fail — meaning no payments will process for that gateway.
Payment Method: The Payment Method Stripe T o k en (bt_stripe__Stripe_Token__c) eld was deprecated.


Virtual Terminal
The LWC Virtual Terminal was updated to support CVV and address validation on Authorize.net gateways when the Payment Gateway Liv e V alidatio n Mo de (A utho rize.net) (bt_stripe__Live_Validation_Mode__c) eld is enabled (checked). The validation only works with new and existing Payment Methods with the P ro c ess T y pe set to “Authorize Now” or
“Capture Now.”

Important Note: The “Auto-Process” picklist value in the P ro c ess T y pe eld is not supported. Selecting the “Auto-Process” picklist option creates an open transaction that we cannot validate because Blackthorn does not store the tokenized card or the CVV. Please do not use the 'Auto-Process' processing type.

To support the CVV and address validation, the A utho rize.net T ransac tio n Key (bt_stripe__Auth_Net_Transaction_Key__c) was added to the Payment Gateway. This eld stores the Transaction Key, which is necessary to validate the CVV when charging a credit card.

Object: Payment Gateway
Field Label: A utho rize.net T ransac tio n Key
API Name = bt_stripe__Auth_Net_Transaction_Key__c
Data Type = Text
Help Text = Transaction Key generated in AuthNet Account settings. It will be encrypted after saving for security.
Description = It stores the AuthNet transaction key necessary for the card code validation.

Click here for more information about how the update works with the different Process Types.


PayLink

Enhancement
Accessibility-related errors occurring on the PayLink landing page and after clicking the PAY button on the Payment Details page have been resolved.


Field/Layout Updates

New
Object: Payment Gateway
Field Label: A utho rize.net T ransac tio n Key
API Name = bt_stripe__Auth_Net_Transaction_Key__c
Data Type = Text
Help Text = Transaction Key generated in AuthNet Account settings. It will be encrypted after saving for security.
Description = It stores the AuthNet transaction key necessary for the card code validation.


Old
The Payment Method Stripe T o k en (bt_stripe__Stripe_Token__c) eld was deprecated.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


August 2025 - Version 6.44
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Table of Contents
(Release Date: 8/26/25)

Breaking Change
Bug Fixes
Enhancement
DocumentLink
Mobile Payments App
Upgrade Instructions
Important De nitions


Breaking Change

Salesforce Connected App Changes
Salesforce recently announced a change to its security policy around Connected Apps, effective August 28th. As a result, Blackthorn recommends verifying that these Connected Apps are installed in your Salesforce orgs.

Blackthorn | Connected App - required for using Blackthorn Events and Blackthorn Payments
Mobile Check-in - required to use the Blackthorn Mobile Check-in app
Blackthorn | Mobile Connected App - required to use the Blackthorn Mobile Payments app
Blackthorn Message - required for using Blackthorn Messaging

Please review the attached pdf for instructions to check that the required Connected Apps are installed and connected correctly.

Your browser does not support PDF. Click here to download.


Bug Fixes
Split Payments: When Split Payments is enabled for an Event and the Event has a P ay ment Gateway and a Do natio n P ay ment Gateway , Attendees can complete the checkout process. Two Transaction records related to the Invoice will be created. Previously, a BT Log with a “Duplicate id in list:” error was also generated.
Invoices: If an Attendee registers for a free Event, the Invoice will be created as expected. Previously, when an Invoice was generated for a free Event, the Invoice’s P ay ment Status was set to “Unpaid,” and the “Send the Event Payment Request Email” work ow was triggered, sending a payment request email to the Attendee. (Known Issue: 000004688)
Refunds: When a user performs a non-gateway refund on a non-gateway Transaction, the original Transaction’s Retained A mo unt and Retained Net A mo unt elds update correctly. Also, their values do not revert when a user edits either the refund or the original Transactions’ elds. Previously, full and partial refunds on non-gateway Transactions
did not correctly update the original Transaction elds, and/or they reverted them after an update was made to the original Transaction. (Known Issue: 000004865)
Line Items: If an Attendee registers for a waitlisted Session, the related Invoice’s Line Item for the waitlisted Session will have T o tal = “0.” Previously, the waitlisted Session’s Line Item listed the T o tal as the actual cost of the Session. (Known Issue: 000004779)
Transactions: When an Attendee uses an ACH payment method to register for a paid Event on an Authorize.net gateway, the related Transaction will have the T ransac tio n Status set to “Completed” and the P ay ment Status set to “Captured.” Previously, ACH Transactions were stuck with T ransac tio n Status = “Completed” and P ay ment Status =
“Authorized.” (Known Issue: 000004775)


Enhancement
Historical Sync: The performance of the “PaymentGateway_SyncBatchable” batch job was improved, especially when running a Historical Sync on a Payment Gateway with a large volume of Stripe transactions. Previously, the batch job running the sync failed, and users saw an “Apex CPU time limit exceeded” error.


DocumentLink

Bug
If an Invoice contains values in the Do c umentLink Field 3 and Do c umentLink Field 3 (Label) elds, the information in those elds will be visible on the related DocumentLink. Previously, the information was not visible on the DocumentLink. (Known Issue: 000004688)


Mobile Payments App

Enhancements

Saved Payment Methods for iOS
The iOS Mobile Payments app’s user interface now includes a “Save card for future payments” checkbox. When submitting a payment via a card reader or by typing in a card’s information, users can check the checkbox to allow their card information to be saved and reused for future payments. This feature can be used both online and of ine.

Admins can enable or disable this feature using the custom attribute “Enable_Reusable_Payments.” For example, the following will occur if the mobile device is of ine.

If the Payee checks "Save card for future payments," then the Payment Method Status will be set to "Valid."
If the Payee does not check the "Save card for future payments" checkbox, then the Payment Method Status will be set to "One-time."

Click here for information about setting up the “Save card for future payments” feature.


Payment Intents
iOS Mobile Payments app users can now accept payments submitted via a card reader or entered manually. The updated payment submission process now passes the following information to Stripe: Payment Method, customer information, and whether the customer has consented to save the Payment Method by checking the box in the Mobile Payments app.

After completing the transaction, the result is newly created Transaction and Payment Method records linked to the customer in Stripe and Salesforce. If the customer checks the box to allow their Payment Method to be reused, it will also be saved for future use.

Use the Blackthorn Payments | Mobile Settings custom setting, Co nf irm P ay ment I ntents (bt_stripe__Con rm_Payment_Intents__c), to change where the Payment Intent will be con rmed.

If Co nf irm P ay ment I ntents is “True” or doesn’t exist, the Mobile Payments app processes the Payment Intent as it currently does, without con rming additional information.
If Co nf irm P ay ment I ntents is “False,” The Mobile Payments app con rms additional information before con rming the Payment Intent.

Click here for more information about Payment Intents.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


July 2025 - Version 6.42
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Table of Contents
(Release Date: July 16, 2025)

Bug Fixes
Enhancements
Upgrade Instructions
Important De nitions


Bug Fixes
Transactions: When SCA is enabled, users can complete a partial capture of a Transaction. Previously, the user got the following error message: “This PaymentIntent's capture_method could not be updated because it has a status of requires_capture. You may only update the capture_method of a PaymentIntent with one of the following statuses:
requires_payment_method, requires_con rmation.”
DocumentLink Webapp: Users can successfully download large or complex Invoice PDFs. Previously, downloading large or complex PDFs resulted in a timeout error.
PayLink Webapp: A user can now submit a payment via a PayLink that includes acceptance language with large text. Previously, the required name eld was hidden, and the user could not scroll to access it, preventing them from completing the payment process. (Known Issue: 000004807)


Invoices
If an Event Organizer applies or removes a discount Code from an Attendee’s Event registration Invoice, the Invoice’s T ax A mo unt will be recalculated and re ect the updated Line Item totals. Previously, the Invoice’s T ax A mo unt was recalculated based on the Invoice’s T o tal A mo unt without considering how an applied or removed discount would
impact that value. (Known Issue: 000004780)
If an Attendee registers for an Event and later pays via a DocumentLink, the Invoice’s Balanc e Due will not go below zero if a discount Code is added to the Invoice’s Disc o unt Co de eld after the invoice has been paid. Previously, adding a discount Code after an Invoice was paid caused the Balanc e Due eld to be calculated as a negative value.
(Known Issue: 000004771)


Enhancements

Spreedly Gateway Updates for Iframes
Spreedly has updated its authentication requirements for iframes, resulting in changes to the Events app’s iframe checkout process. The following changes ensure the Events’ webapp correctly passes newly required values to the Spreedly gateway when Event registrations occur via an iframe.


Updated Spreedly Con guration
Complete the following steps to enable the new authentication method.

1. Navigate to Environment Settings in the Spreedly dashboard.
2. Enable the checkbox "Enable Secure Tokenization."
3. Select the option "iFrame or Spreedly Express."


Blackthorn Con guration
Con rm that the following elds are on the Payment Gateway page layout you use for your Spreedly gateway.

Spreedly Env iro nment Key
Spreedly Co nf igured Gateway
Spreedly Certif ic ate T o k en
Spreedly P riv ate Key


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


June 2025 - Version 6.40
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue


Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. T est Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Table of Contents
(Release Date: July 1, 2025)

Bug Fixes
Enhancement
Upgrade Instructions
Important De nitions


Bug Fixes
TouchNet Gateway: Users can now register for an Event with a TouchNet payment gateway on an Experience Cloud site. The payment page will open in a new pop-up window, allowing users to complete the registration process. Previously, users intermittently got the following error, which prevented them from registering for the Event. "We're sorry, a
system error occurred. Please try again later." (Known Issue: 000004680)
Transactions: Users can now select any Payment Method type and Payment Gateway (Stripe, AuthNet, or Spreedly) to capture a Transaction or cancel a Payment Schedule. Previously, they got the following error message when trying to capture a Transaction or cancel a Payment Schedule: "duplicate eld selected: bt_stripe_Sales_Document_c Error is in
expression '{!charge}' in page bt_stripe:transaction_charge: (bt_stripe)"
Reattempt Transactions: Transaction reattempts work correctly for Stripe, Spreedly, and Authorize.net credit cards, as well as for ACH Transactions on Spreedly and Authorize.net gateways. Previously, reattempts for Transactions with a failed card or ACH Payment Method would not work even though the Blackthorn Pay – Reattempt Settings custom
setting was enabled.


Authorize.net Transactions
If a user processes a refund for a Transaction that used an Authorize.net payment gateway, none of the elds on the Invoice will be updated. Previously, after performing a full or partial refund on a Transaction that used an Authorize.net gateway, several Invoice elds were changed, including the P ay ment Status eld, which changed from “Paid” to
“Unpaid.” (Known Issue: 000004647)
Transactions using an Authorize.net gateway that are scheduled to auto-process will now process correctly on the scheduled date. Previously, when a user clicked the Process Scheduled Charge Transactions Now button to schedule Transactions using an Authorize.net gateway, the webhooks were not created, and the Transactions were not captured.


Enhancement
Payment Methods: The iOS Mobile Payments app’s user interface now includes a “Save card for future payments” checkbox. When submitting a payment via a card reader on the app, users can check the checkbox to allow their card information to be saved and reused for future payments. A message will appear in Stripe indicating the user has given
consent for the card’s information to be stored and used for future payments. If the checkbox is not checked, no card information will be saved.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


May 2025 - Version 6.37
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue


Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. T est Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Table of Contents
(Release Date: May 28, 2025)

Bug Fixes
Enhancements
Field/Layout Updates
Upgrade Instructions
Important De nitions


Bug Fixes
Non-Gateway Transactions: After manually refunding a non-gateway Transaction, the refund Transaction’s Retained A mo unt and Retained Net A mo unt elds will display the correct amounts. Previously, the elds incorrectly displayed a negative amount equal to the original Transaction’s A mo unt (20 vs. -20) instead of 0.00. (Known Issue:
000004546)
Codes: When a user enters an “amount-off” Code (T y pe = “Discount” and applied at the Event level) during checkout, the discount will be calculated correctly. Previously, the discount amount used in the calculation was $3, regardless of the amount con gured in the Code.


Enhancements
Payment Intents: The Payment Intent’s Capture Metho d eld now supports the “Automatic Async” (automatic_async) value to align with the latest Stripe Library version. This value is used internally to support Stripe’s required behavior and is not intended for user selection. The new default value for the Capture Metho d eld is “Automatic Async.”
Payments Receipt Emails: The Transaction work ow rules, “Send Blackthorn | Payment Receipt (HTML) and “Send Blackthorn | Payment Receipt (Text),” for the Payments Receipt Email were converted to the “Send Blackthorn | Payment Receipt” ow. Users can now launch the Payments Receipt Email from the ow in the Payments package. The email
receipt will be sent when the Transaction is completed/captured and will contain the Transaction’s Desc riptio n in a merge eld. Note: “Send Blackthorn | Payment Receipt (HTML) and “Send Blackthorn | Payment Receipt (Text)” were deprecated.
Spreedly Payment Gateway: The new elds, Spreedly P riv ate Key and Spreedly Certif ic ate T o k en , were added to the Payment Gateway object to ensure authentication occurs correctly when using iframed components and a Spreedly Payment Gateway.
Field Label: Spreedly P riv ate Key
API Name: bt_stripe__Spreedly_Private_Key__c
Data Type: Long Text Area(4096)
Description: Stores the PEM-formatted private key used for SSL client certi cate authentication with Spreedly.
Field Label: Spreedly Certif ic ate T o k en
API Name: bt_stripe__Spreedly_Certi cate_Token__c
Data Type: Text(255)
Description: Stores the Spreedly certi cate token used for payment gateway routing. Auto-generated by Spreedly and used to reference the stored certi cate securely.
Permission Set Updates for Both Fields
Read/Edit: Blackthorn | Payments (Admin)
Read: Blackthorn | Payments (User), Blackthorn | Payments (Manager), Blackthorn | Payments (Community/Platform User), Blackthorn | Payments (Site Guest User), and Blackthorn | Payments (Lite User)
No Access: Blackthorn | Payments (Stripe Billing)


Field/Layout Updates

New
Object: Payment Gateway
Field Label: Spreedly P riv ate Key
API Name: bt_stripe__Spreedly_Private_Key__c
Data Type: Long Text Area(4096)
Description: Stores the PEM-formatted private key used for SSL client certi cate authentication with Spreedly.
Field Label: Spreedly Certif ic ate T o k en
API Name: bt_stripe__Spreedly_Certi cate_Token__c
Data Type: Text(255)
Description: Stores the Spreedly certi cate token used for payment gateway routing. Auto-generated by Spreedly and used to reference the stored certi cate securely.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


April 2025 - Version 6.32
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue


Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. T est Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Table of Contents
(Release Date: April 22, 2025)

Off-Cycle Release
Bug Fixes
Enhancement
PayLink
Upgrade Instructions
Important De nitions


Off-Cycle Release

May 7, 2025
The April 2025 update to the Stripe checkout logic was reversed so additional work can be completed. The original x caused issues for those Payment Methods that don’t follow the “authorize rst and charge later” process and prevented payments from being accepted. Until then, if a user closes their browser while a payment is processing, the payment will be
charged, skipping the authorization step, and the ERS process will fail.


Bug Fixes
Fees: When a discount Code is applied at the Event Item level, the total amount due will be correctly displayed in the payment screen summary. Previously, the amount due was miscalculated after applying the discount.
Virtual Terminal: If a user enters an invalid ACH Payment Method in the Virtual Terminal, they will see a descriptive error message telling them what needs to be xed so the Payment Method can be accepted. Previously, users saw a generic error message. (Known Issue: 000003117)
Permission Sets: Users with the Blackthorn | Payments (Manager) permission set can successfully add Line Items to an existing or new Invoice. Previously, they received bad query errors. (Known Issue: 000003048)


Refund Transactions
When a partial refund is processed via Authorize.net, the original Transaction’s Retained A mo unt and Retained Net A mo unt are reduced by the partial refund amount, and the original Transaction’s P ay ment Status is updated to “Partially Refunded.” Previously, processed partial refunds appeared as full refunds in Salesforce. (Known Issue:
000002797)
When a partially disputed Transaction is won, the Retained A mo unt , Retained Net A mo unt , and P ay ment Gateway Fee elds will be updated correctly. Previously, if a partial dispute was won, the retained amounts on an original Transaction were not updated correctly. (Known Issue: 000004124)


Enhancement
The following deprecated features/apps were deleted from the Blackthorn Payments app. This change will not impact underlying objects, permission sets, or related components.
Blackthorn | Stripe Billing (Developer Name: Blackthorn_Billing)
Blackthorn | Stripe Billing (Developer Name: Blackthorn_BillingLi)
Blackthorn | Stripe Connect (Developer Name: BT_Stripe_Connect)
Blackthorn | Stripe Connect (Developer Na


PayLink

Webapp Release

Enhancement

Auto-translating special characters/symbols when using PayLink now works as expected.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


March 2025 - Version 6.3
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue


Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. T est Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Table of Contents
(Release Date: March 18, 2025)

Bug Fixes
Upgrade Instructions
Important De nitions


Bug Fixes

Virtual Terminal
The logic related to the Virtual Terminal custom settings Disable New P ay ment Metho d , Hide Card T ab , and Hide Bank T ab has been updated.

When the Virtual Terminal custom setting Disable New P ay ment Metho d is set to “True” (checked) and either the Hide Card T ab or Hide Bank T ab is set to “False” (unchecked), the “New Payment Method” action will be hidden from the top action bar, but it will still be visible in the Payment Method dropdown list.
If the Hide Card T ab or Hide Bank T ab custom settings are set to “True” (checked), all “New Payment Method” actions are disabled.

Click here to read more about the Virtual Terminal’s custom settings.


Transactions
When a user registers for a paid Ticket and submits a payment on an Authorize.net gateway, the Transaction’s New A mo unt eld will be correctly updated when webhooks are processed, creating a successful paid Transaction. Previously, the value in the New A mo unt eld was incorrectly cleared when webhooks were processed. (Known Issue:
000004435)
When using a PayConex payment gateway via Spreedly to accept a payment, the Transaction will be charged and completed successfully. Previously, the currency code was changed to lowercase letters when trying to capture the authorized charge, causing an error. (Known Issue: 000004528)


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


February 2025 - Version 6.29
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue


Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. T est Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Table of Contents
(Release Date: March 5, 2025)

Bug Fixes
Upgrade Instructions
Important De nitions


Bug Fixes
Line Items: If the U nit P ric e on a Line Item is updated, the Invoice’s T ax A mo unt and T o tal A mo unt elds will be updated to re ect the new U nit P ric e . Previously, the T ax A mo unt and T o tal A mo unt elds were not updated when changes were made to the related Line Item record. (Known Issue: 000003418)
LWC Virtual Terminal: The following will occur when using the LWC Virtual Terminal with the Experience Cloud.
A newly created Payment Method’s P ay ment Gateway Custo mer eld will be updated with the existing Payment Gateway Customer when there is an existing Payment Gateway Customer record with the same email and Account used to create the new Payment Method.
The new Payment Method’s P ay ment Gateway Custo mer eld will be updated with a new Payment Gateway Customer record when there isn’t an existing one with the same email and Account used to create the new Payment Method.
Payment Methods added via the LWC Virtual Terminal in the Experience Cloud will be added to the available Payment Methods for the related Account.
When a user logs into the Experience Cloud from a Contact record, the Virtual Terminal will display all available Payment Methods for the Account.
Previously, when a user created a new Payment Method from the LWC Virtual Terminal in an Experience Cloud, the new Payment Method didn’t correctly trigger the matching to or creation of a new Payment Gateway Customer. The newly created Payment Method also didn’t appear in the LWC Virtual Terminal drop-down list. (Known Issue:
000003244)
PayLink: When a user selects a different language in the Transaction P ay Link Display Language eld for the PayLink record, special characters will be translated correctly. Previously, special characters used in French were not recognized; instead, random characters were included. (Known Issue: 000004454)


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


January 2025 - Version 6.28
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. T est Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Table of Contents
Bug Fix
Enhancement
PayLink
Upgrade Instructions
Important De nitions


Bug Fix
When embedding the BT Payments LWC Virtual Terminal in a ow, users can con gure the P ro c ess T y pe parameter to be able to accept payments by setting P ro c ess T y pe to "Capture Now." Previously, when a user tried to capture a payment using the BT Payment LWC Virtual component in a ow, they experienced an issue where the Pay button
was grayed out and could not be used. (Known Issue: 000004276)


Enhancement
As part of the January 2025 release and in preparation for the next Mobile Payments app update, the Co nf irm P ay ment I ntents (bt_stripe__Con rm_Payment_Intents__c) eld will be automatically added to the Blackthorn Payments | Mobile Settings custom setting. Once the feature is live, the Payment Intent process will be streamlined to reduce the
number of API calls made to Stripe. Previously, the Mobile Payments app con rmed the Payment Intent before making any calls to Salesforce to capture it, preventing additional updates before con rmation.


PayLink

Webapp Release

Bug Fix

PayLink users can now use the keyboard to switch between the Card and Bank tabs during checkout, improving accessibility. Previously, users could not switch tabs when using a keyboard.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


December 2024 - Version 6.27
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue


Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. T est Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Table of Contents
Bug Fixes
Enhancement
Upgrade Instructions
Important De nitions


Bug Fixes
Permission Sets: The Blackthorn | Payments (Manager) permission set was updated to give read and write access to the Invoice’s Fee A mo unt eld.
Transactions: If a disputed Transaction is won, the chargeback reversal Transaction’s Retained A mo unt will be set to the original Transaction’s A mo unt . Previously, the chargeback reversal Transaction’s Retained A mo unt was set to “0.” (Known Issue: 000004103)
Authorize.net: If a user tries to add a Payment Method for a Contact, Account, or Lead but the Customer Pro le (Payment Gateway Customer in Salesforce) has only been deleted in the Authorize.net dashboard, they will get the following message. “The Payment Method could not be registered: Customer Pro le could not be found in the Payment
Gateway." The error message will also be saved in the Payment Method’s Erro r Message eld. Previously, an error occurred when a user tried to add a new Payment Method from the Virtual Terminal except the Authorize.net Customer Pro le was already deleted in the Authorize.net dashboard. (Known Issue: 000003988)


Virtual Terminal
When creating a New Single Charge payment in the LWC Virtual Terminal, users can only select a Payment Method from the list related to the selected Contact, Account, or Lead record. Previously, users could choose any Payment Method in the org. (Known Issue: 000004186)
The Virtual Terminal will use the Currenc y value from the related Invoice Currenc y I SO eld. If the Invoice’s Currenc y I SO eld is blank, the Virtual Terminal will use the Payment Gateway’s Def ault Currenc y value. Previously, the Virtual Terminal Currency eld defaulted to “Choose One...” and the Payment Gateway’s Def ault Currenc y value did
not change the value in the Virtual Terminal. (Known Issue: 000004186)
The following will occur when using the Aura Virtual Terminal with the Experience Cloud. Previously, when a user created a new Payment Method from the Virtual Terminal in an Experience Cloud, the new Payment Method didn’t correctly trigger the matching to or creation of a new Payment Gateway Customer. The newly created Payment Method also
didn’t appear in the Virtual Terminal drop-down list. (Known Issue: 000003244)
A newly created Payment Method’s P ay ment Gateway Custo mer eld will be updated with the existing Payment Gateway Customer when there is an existing Payment Gateway Customer record with the same email and Account used to create the new Payment Method.
The new Payment Method’s P ay ment Gateway Custo mer eld will be updated with a new Payment Gateway Customer record when there isn’t an existing one with the same email and Account used to create the new Payment Method.
Payment Methods added via the Virtual Terminal in the Experience Cloud will be added to the available Payment Methods for the related Account.
When a user logs into the Experience Cloud from a Contact record, the Virtual Terminal will display all available Payment Methods for the Account.


Enhancement
Transactions: When a Transaction with an ACH Payment Method using a Stripe gateway fails, the following occurs.
A new Transaction is created. Its Rec o rd T y pe is set to “Refund,” T ransac tio n Status is set to “Failed,” P ay ment Status eld is blank, and the Stripe Fee related to the failure is recorded.
The original Transaction’s T ransac tio n Status is changed to “Failed.” (Known Issue: 000002910)


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


November 2024 - Version 6.26
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue


Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. T est Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Table of Contents
Bug Fixes
Enhancement
DocumentLink
Field/Layout Updates
Upgrade Instructions
Important De nitions


Bug Fixes
Payment Method: When a user creates a card or ACH Payment Method with a Spreedly Payment Gateway from the Virtual Terminal, the Payment Method’s P ay ment Metho d Status will be set to “Valid.” Previously, the P ay ment Metho d Status eld was blank after the Payment Method was created.
Transactions: When a partial refund is issued for a Transaction, the refunded Transaction’s A mo unt re ects the correct amount, and the Transaction's P ay ment Status is set to "Partially Refunded." Previously, a refund Transaction was created for the full amount of the original Transaction, and the original Transaction's P ay ment Status was incorrectly
set to "Refunded."
Virtual Terminal: When users click the Reset button in the Virtual Terminal, previously populated elds will be emptied. Previously, clicking the Reset button caused nothing to happen. (Known Issue: 000003098)
Authorize.net: If a user tries to save a new Payment Method with an incorrect zip code on an Authorize.net gateway, they will receive an error message letting them know that the Address Veri cation Security (AVS) failed and the Payment Method will not be saved. Previously, users received the following, confusing error message. "The element
'getCustomerPaymentPro leRequest' in namespace 'AnetApi/xml/v1/schema/AnetApiSchema.xsd' has invalid child element 'unmaskExpirationDate' in namespace 'AnetApi/xml/v1/schema/AnetApiSchema.xsd'. List of possible elements expected: 'clientId, r" (Known Issue: 000003902)
Disputes: When a Stripe dispute Transaction creates a refund Transaction, the refund Transaction’s P ay ment Status is set to "Refunded." Previously, when a Transaction was disputed and won, the refund Transaction did not have a value in the P ay ment Status eld. (Known Issue: 000003522)
Subscriptions: When a user manually pushes a Stripe Billing Subscription to Stripe, the Subscription Item will be updated with the Stripe ID. Previously, after the webhook occurred, a second Subscription Item with the correct information was created instead of the original Subscription Item being updated. (Known Issue: 000003035)


Enhancement
The new custom checkbox eld, Enable A utho rize.Net CV V Filter , on the Payment Gateway allows users to require Attendees to re-enter their CVV code for Transactions using an Authorize.net gateway.
Field Label: Enable A utho rize.Net CV V Filter
API Name: Enable_Auth_Net_CVV_Filter__c
Data Type: Checkbox
Help Text: When checked, transactions using an Authorize.net gateway will require the user to re-enter the CVV code for the card being used.


DocumentLink

Accessibility Enhancements
The Download button on the Invoice now has a label that is readable by screen readers, improving accessibility.
Duplicate content was removed from Invoices, stopping screen readers from reading all content twice.
The contrast between an Invoice’s text and background was improved, improving the Invoice’s readability and ensuring it meets accessibility standards.


Field/Layout Updates

New
Object: Payment Gateway
Field Label: Enable A utho rize.Net CV V Filter
API Name: Enable_Auth_Net_CVV_Filter__c
Data Type: Checkbox
Help Text: When checked, transactions using an Authorize.net gateway will require the user to re-enter the CVV code for the card being used.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


October 2024 - Version 6.25
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Table of Contents
Bug Fixes
DocumentLink
Upgrade Instructions
Important De nitions


Important Note
Blackthorn customers will not be impacted by the most recent Authorize.net change. Recently, Authorize.net contacted many of their customers to let them know they are updating their SSL /TLS certi cates. Based on information provided by Authorize.net, Blackthorn products will not be affected by this change.


Bug Fixes
Custom Settings: When the Blackthorn Pay – Trigger Settings custom setting Enable P ay ment I ntents f o r A CH P Ms = “True” (checked), hidden elds remain hidden, and mapping works as expected. Previously, if the custom setting was checked, hidden elds were visible, mapping broke, and users received a Terminal Data Initialization Error. (Known
Issue: 000003932)
Transactions: When using an Authorize.net Payment Gateway, the Transaction’s P ay ment Status will change to “Captured” once the Transaction is processed. Previously, the P ay ment Status was set to “Authorized” instead of “Captured” after the Transaction was processed. (Known Issue: 000003818)
Field Service Lightning (FSL): If a user adds a long Transaction record Desc riptio n to the Work Order’s Of f line Mo bile P ay U RL eld, the text will remain within the character count limit and no longer generate an error. Previously, this caused some required parameters to be omitted from the URL, which generated Blackthorn Logs with the following
error message. “Update failed, Of ine Mobile Pay URL: data value too large”. (Known Issue: 000003840)


Payment Schedules
When a Transaction’s T ransac tio n Status is set to “Failed,” the related Payment Schedule eld Sc hedule Status will be set to "Failed," and P ay ment Status will be set to "Overdue." Previously, the Sc hedule Status was set to “Future,” and the P ay ment Status was set to “Scheduled.” Click here for more information about the statuses and their
de nitions. (Known Issue: 000002805)
If a Contact cancels their Payment Schedule (Sc hedule Status = “Canceled” or “Canceled and Refunded”), a new Transaction will not be automatically generated. Previously, when the Payment Schedule’s Sc hedule Status was set to “Canceled,” a new Transaction was automatically generated, and the Sc hedule Status was changed back to “Active.”
(Known Issue: 000003787)


Virtual Terminal
Users searching for a Payment Method in the LWC Virtual Terminal will see identifying information such as the Payment Method’s Ho lder's Name , Email , or Last 4 Digits, depending on the Payment Method type and available information. Previously, the user saw the Payment Method’s numeric Salesforce name (E.g., PM0000001, PM0000002, etc.),
making it dif cult to locate the correct Payment Method. (Known Issue: 000003097)
When using the “New Single Charge” action in the LWC Virtual Terminal, users will see only those Payment Methods related to the selected Contact, Account, or Lead. Previously, the list of available Payment Methods included ones unrelated to the selected Contact, Account, or Lead. (Known Issue: 000003144)
When using the LWC Virtual Terminal from an Invoice record, the Description eld on the LWC Virtual Terminal will have the same value as the Invoice’s Subjec t eld. Previously, some elds con gured using the Custom Metadata Types mapping feature were incorrectly mapped when loading the LWC Virtual Terminal. (Known Issue: 000003273)


DocumentLink

Bug Fixes
When using the Data Dictionary with DocumentLink, users will see the value in the Invoice’s Dy namic Fee Name eld replace the Line Item row label for "Tax." Previously, the Line Item row label for "Tax" did not display the Dy namic Fee Name value, even though the Dy namic Fee Name value replaced “Tax in the totals section.
Formatting changes (italic, bold, etc.) made to the Invoice’s Do c umentLink Field 1 , Do c umentLink Field 2 , and Do c umentLink Field 3 elds will appear as they were formatted on the DocumentLink. Previously, formatting changes were not applied to the DocumentLink. (Known Issue: 000003693)


Upgrade Instructions
Go to the Blackthorn Candy Shop to upgrade Payments to the newest version.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


September 2024 - Version 6.23
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. T est Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Table of Contents
Bug Fixes
Enhancements
Upgrade Instructions
Important De nitions


Bug Fixes
Virtual Terminal: When the Virtual Terminal is in Lite Mode, input parameters will be correctly mapped when embedding the LWC Virtual Terminal in a screen ow. Previously, the input parameters were not mapped to the Virtual Terminal elds. (Known Issue: 000003009)
Scheduled Jobs: The Blackthorn | Payments Daily Captures scheduled job will successfully capture Transactions without creating a Blackthorn Log when the Payment Gateway Liv e V alidatio n Mo de (A utho rize.net) eld = “False.” Previously, the Blackthorn | Payments Daily Captures scheduled job failed, creating Blackthorn Logs with the following
error message. "SObject row was retrieved via SOQL without querying the requested eld: bt_stripe_Payment_Gatewayc.bt_stripeLive_Validation_Mode_c". (Known Issue: 000003889)


Enhancements
Permission Sets: The new permission set, Blackthorn | Payments (Lite User), was created. Users with this permission set have read-only access to all BT Payments objects and standard Salesforce functionality, such as reports and dashboards. Note: Users with this permission set cannot use packaged actions such as capturing Transactions, processing
Refunds, etc.
Payment Methods: Changes made to a credit card number and expiration date in Authorize.net will be mapped to the related Payment Method in Salesforce.
Webhooks: Improved and optimized our webhook processing logic using a strategy design pattern.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


August 2024 - Version 6.22
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. T est Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Table of Contents
Bug Fix
Enhancements
Mobile Payments App
Upgrade Instructions
Important De nitions


Bug Fix
Payment Methods: Attendees can now complete the payment and registration process for an Event when checking out with an ACH Payment Method on a Stripe gateway. Previously, the Attendee received the following error message: “Warning. Checkout failed, please try again later.” (Known Issue: 000003393)


Enhancements
Batch Jobs: The Payment Balance Update batch process now only includes Connected Accounts with Update Balance = “True” (checked). Previously, it included all Connected Accounts, causing a large number of accounts to be processed together.
Stripe Billing: Stripe Billing users can create one-off Invoices in Salesforce that will sync to Stripe for accurate revenue recognition without editing the data in the Stripe Dashboard. The Line Item elds Service Start Date and Service End Date will sync with Stripe’s end and start Supply dates.


Mobile Payments App

Bug Fix
The Mobile Payments app’s logic was updated to ensure a user can process different Transactions across different Payment Gateways and create a successfully processed Transaction and a valid Payment Method.
If the Transaction's Contact/Account matches an existing user with the same Payment Gateway used for the new Transaction, the existing user will be attached to the new Payment Method and new Transaction.
If the Transaction’s Contact/Account does not match an existing user with the same Payment Gateway, a new Payment Gateway Customer will be created and attached to the new Payment Method and Transaction.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


July 2024 - Version 6.20
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue


Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. T est Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Table of Contents
Bug Fixes
Enhancements
Upgrade Instructions
Important De nitions


Bug Fixes
Fees: The Fee object’s T y pe eld is now required to create a Fee record from an Event record. Previously, creating a Fee record with the T y pe eld left blank resulted in Blackthorn Logs and errors.
Virtual Terminal: A user with a non-admin pro le and a Blackthorn | Payments (Admin), Blackthorn | Payments (Manager), or a Blackthorn | Payments (User) permission set can now create a Payment Method from the LCW and Aura Virtual Terminal. Previously, a user with a non-admin permission set would see an error when creating a Payment Method
using the Virtual Terminal. (Known Issue: 000002947)
Transactions: If a user enters an invalid Payment Method for a Transaction and then enters a valid Payment Method, the Transaction will be processed successfully without updating the T ransac tio n Status and P ay ment Metho d elds multiple times. Previously, the Transaction’s T ransac tio n Status changed from “Completed” to “Failed” and back to
“Completed,” and the P ay ment Metho d changed from the original value to the new value and back to the original value. (Known Issue: 000003409)
PaymentChargeFlow: To improve the user experience, the PaymentChargeFlow now includes logic to validate the input length for the Card Number , CV V , Ex p Mo nth , and Ex p Y ear and will display an error message as a user enters incorrect information. Previously, the PaymentChargeFlow did not include validation and waited for information to get
to the gateway before notifying the user of an incorrect character length. (Known Issue: 000003796)
Payment Method: If a user enters incorrect Payment Method information and receives an error, they can now click the X to close the error message, enter the correct information, and successfully process the payment. Previously, dismissing the error message prevented the user from completing their payment Transaction.


Enhancements
Fees: The Fee object’s page layout was updated to make the T y pe eld required to create a Fee record.
Spreedly: If a Spreedly Transaction fails, the Transaction will now contain the following information describing the reason for the failure.
If the response includes an error code, it will be stored in the Transaction’s Erro r Co de eld.
The Transaction’s token will be stored in the Transaction’s Spreedly T ransac tio n T o k en eld.
The date the Transaction was processed will be stored in the P ro c essed Date eld.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


June 2024 - Version 6.19
Please review the updates below and follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. T est Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Table of Contents
Bug Fixes
Enhancement
DocumentLink
PayLink
Field Updates
Upgrade Instructions
Important De nitions


Bug Fixes
The default Payment Method will be set correctly when using the Virtual Terminal to create more than one Payment Method with a Spreedly payment gateway. Previously, all added Payment Methods were automatically set to be the default Payment Method. (Known Issue: 000003129)


Authorize.net and Flow Screen Charge Component

PLEASE READ

This update applies ONLY to users with an Authorize.net gateway who use the Flow Screen Charge (PaymentChargeFlow) Component. Do not use these elds for any other scenarios. It will cause the Transaction to fail.

This update is a work in progress, and support for CVV and address validation for other features will occur in future updates.


To enable CVV validations when using an Authorize.net gateway and the PaymentChargeFlow component, check the new Liv e V alidatio n Mo de (A utho rize.net) eld on the Payment Gateway record and add the Sho w A ddress eld to the PaymentChargeFlow component.

When both are enabled, additional address elds (Street, City, State, and Country) will be visible and required, and the validation process will occur.

Object: Payment Gateway
Field Label: Liv e V alidatio n Mo de (A utho rize.net)
API Name: Live_Validation_Mode__c
Data Type: checkbox
Default Value: False (unchecked)
Description:
If checked, the Payment Method will use the "liveMode" to submit a zero-dollar or one-cent Transaction (depending on the card type and the processor support) to con rm the card number belongs to an active credit or debit account.
If unchecked, the Payment Method will use the "testMode" to perform a Luhn mod-10 check on the card number without further validation.


Enhancement
The Invoice record has a new eld called Dy namic Fee Name . The eld is populated when an Invoice related to an Event with an associated tax Fee is created or updated. The eld’s value will then be used in DocumentLink’s Invoice to override the Tax column’s label. This update is related to the foundational development of the Tax/GST feature and is
not functional.
Field Label: Dy namic Fee Name
API Name: bt_stripe__Dynamic_Fee_Name__c
Data Type: Text
Description: The name of the label used to display the tax Fee on an Invoice. For Events, it is the Fee Name of the Fee associated with the Event.


DocumentLink

Bug Fix
When a user downloads an Invoice pdf from DocumentLink, the date format will remain the same as the browser locale format. Previously, the date changed to the US date format after downloading the Invoice pdf. (Known Issue: 000002642)


Enhancement
Line Item names, descriptions, and other content will now wrap correctly when a user views a DocumentLink Invoice. Previously, the text was cut off, preventing users from viewing the entire amount.


PayLink

Enhancement
Users can now translate button labels and other static text on PayLinks. The Data Dictionary provides multilingual support, allowing Admins to establish a default language that serves as the primary language for all users. Admins can also override the default language and customize users' language experiences when speci c prede ned criteria are met.

The Transaction object now includes two new elds; the Data Dic tio nary Gro up eld and the P ay Link Display Language eld.

Field Name: Data Dic tio nary Gro up
API Name: bt_stripe__Data_Dictionary_Group__c
Data Type: Lookup(Data Dictionary Group)
Description: Select the Data Dictionary Group that contains the translated override values (Data Dictionary Entries) for the chosen Display Language.
Field Name: P ay Link Display Language
API Name: PayLink_Display_Language__c
Data Type: picklist
Description: List of supported display languages for PayLink. This eld is set to English by default.

The following logic describes how the Data Dictionary Group/Data Dictionary Entry records interact with the P ay Link Display Language eld.

PayLink labels are displayed in English, the default language, when either of the following is true.
The Transaction’s P ay Link Display Language and Data Dic tio nary Gro up elds are blank.
The Transaction’s P ay Link Display Language eld is blank, and the Data Dic tio nary Gro up does not have a Data Dictionary Entry for English.
PayLink labels use a Data Dictionary Entry’s values if the attached Transaction’s Data Dic tio nary Gro up has a Data Dictionary Entry record that uses the same language as the Transaction’s P ay Link Display Language .
PayLink labels are displayed in the selected Transaction P ay Link Display Language if a Data Dictionary Group does not include a Data Dictionary Entry record for the selected P ay Link Display Language .
PayLink labels are displayed in English if a Data Dictionary Group has a Data Dictionary Entry record with Language / Lo c ale = “English,” and the Transaction’s P ay Link Display Language eld is blank.
PayLink labels are displayed in the selected Transaction’s P ay Link Display Language when the Transaction’s Data Dic tio nary Gro up eld does not have a value.

Click here for more information about translating PayLinks.


Field/Layout Updates

New
Object: Invoice (This update is related to the foundational development of the Tax/GST feature and is not functional.)
Field Label: Dy namic Fee Name
API Name: bt_stripe__Dynamic_Fee_Name__c
Data Type: Text
Description: The name of the label used to display the tax Fee on an Invoice. For Events, it is the Fee Name of the Fee associated with the Event.
Object: Transaction
Field Name: Data Dic tio nary Gro up
API Name: bt_stripe__Data_Dictionary_Group__c
Data Type: Lookup(Data Dictionary Group)
Description: Select the Data Dictionary Group that contains the translated override values (Data Dictionary Entries) for the chosen Display Language.
Field Name: P ay Link Display Language
API Name: PayLink_Display_Language__c
Data Type: picklist
Description: List of supported display languages for PayLink. This eld is set to English by default.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


May 2024 - Version 6.18
Once you have reviewed the updates listed below, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. T est Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Bug Fixes
After a payment is captured, the webhooks are processed, and the Transaction is refunded, the P ay ment Status will be set to “Refunded”. Only failed refunds will trigger an update to the Transaction’s P ay ment Status , Retained A mo unt , and Retained Net A mo unt elds. Previously charge.refund.updated webhooks would incorrectly update
successfully refunded Transactions to P ay ment Status = "Captured". (Known Issue: 000003377)
When using Stripe Checkout for payments, the resulting T ransac tio n Status will be correctly updated to “Completed,” and the related Payment Intent Status will be set to “Succeeded.” Previously, the T ransac tio n Status was set to “Failed Payment Intent.” (Known Issue: 000003449)
When creating a new Payment Method in a Spreedly gateway, Payment Methods with either a 2 or 4-digit value in the card’s Ex piratio n Y ear eld will be correctly stored and synched to the Payment Gateway. Previously, 2-digit values in the Ex piratio n Y ear eld caused the Payment Method to be rejected. (Known Issue: 000003214)
After completing the checkout process via a TouchNet gateway, the related Payment Method’s Ho lder's Name eld will populate correctly. Previously, the Ho lder's Name eld remained empty.


Enhancements
The Chat button on the Blackthorn | Payments Admin and Blackthorn | Payments Setup Wizard tabs has been deprecated.
The Payments app will now include the Event’s T ax Fee and Event Item’s T ax -Ex empt elds in the Invoice/Transaction processing. This update is related to the foundational development of the feature and is not functional.

If you have any questions or need help with testing, please contact Blackthorn Support.


April 2024 - Version 6.17
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Bug Fixes
A valid Payment Method can now be removed from a Spreedly gateway using the Salesforce UI. An error message will be displayed when a user tries to remove a Payment Method that was already deleted. Previously, when a user tried to remove a Payment Method, the process wasn’t successful. (Known Issue: 000003046)
When processing a payment using a Stripe gateway, the Payment Intent’s Payment Method and Payment Gateway Customer                 elds will contain the associated Payment Method and Payment Gateway Customer records. Previously, the Payment Intent was created without the related Payment Gateway Customer and Payment Method. (Known Issue:
000003189)
Users can now click the Remove From Gateway button to remove a Payment Method from Salesforce without creating a duplicate Payment Method. Previously, a duplicate Payment Method was created with Payment Method Status = “Valid” while the original Payment Method correctly showed Payment Method Status = "Deleted from Payment

Gateway". (Known Issue: 000002803)
Clicking the Stripe URL     eld on a Payout Transactions record will take the user to the corresponding Stripe page. Previously, clicking the Transaction’s Stripe URL      eld took the user to a Stripe error page that said, “Sorry, something went wrong.”
If the Payments, Events, and Storefront apps and the Base package are installed, and a user applies a Code with a Code Eligibility to a single Store Product, the resulting Invoice will be created successfully. Previously, the user received the following apex error in a Blackthorn Log, and the Invoice failed to be created. “Insert failed. First exception on row 1;
rst error: FIELD_INTEGRITY_EXCEPTION, Event Item: Id value of incorrect type: a3L79000000ab5mEAA: [conference360__Event_Item__c]”
If a Payment Processing Fee is applied to a paid Event and a discount Code less than 100% off is applied to the Event Item, the following will occur. The related discount Line Item and calculations will be correctly re ected on the Invoice, and the Attendee will be charged the correct amount. Previously, Attendees saw the correct amount due, but they
were charged the full amount during checkout. (Known Issue: 000003499)

If you have any questions, please don't hesitate to reach out to Blackthorn Support.


March 2024 - Version 6.16
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Bug Fixes
Payments made with an Authorize.net Payment Gateway via a DocumentLink will now process correctly. Previously, Invoices were not always created, forcing users to update the Transaction with the Invoice manually. Users also received the following error. "The provided key 'sk_live_********************uNhC' does not have access to account 'xxxxx' (or
that account does not exist). Application access may have been revoked.", "type": "invalid_request_error", "code": " (Known Issue: 000003170)
Opportunity Products with Product Type = “One-Time” will only be added to the rst Invoice. They will not be added to the Subscription. Previously, editing a Subscription with a regular Opportunity Product and an Opportunity Product with Product Type = “One-Time” caused the one-time Opportunity Product to be incorrectly added to the

Subscription in Stripe. (Known Issue: 000003150)
A Payment Gateway Customer (PGC) record will be created if an email address is valid. Previously, the PGC validation rule prevented PGC records from being created if the email address domain had more than four characters. (Known Issue: 000003258)
When the Relationship Settings’ Contact Account Rule        eld is set to “Bucket Account,” a new Contact record without a matching Account will be added to the “Bucket Account.” Previously, the Account matching rules incorrectly added the new Contact record to the “Basic Bucket” Account.
When processing Invoice webhooks asynchronously, the Invoice will include the relevant information from the associated Account, Contact, and Payment Method records. Previously, the Invoice was missing information from the Account, Contact, and Payment Method records. (Known Issue: 000003266)
The guest user must also be assigned a custom permission set in addition to the Blackthorn | Payments (Site Guest User) permission set to have Read access to several standard objects to process the webhooks. The custom permission set must include the following object permissions:
Account - Read
Opportunity - Read
Product2 - Read
NOTE: When webhooks are processed via batch or manually, sharing rules apply. Using a custom trigger will allow webhooks to be processed in system mode, bypassing sharing rules. You may experience limitations for use cases, depending on your speci c scenario.


Enhancement

High Volume Batch Processing
High volume batch processing enables the scalability of our batch processes. The new logic queries high volumes of Transactions, splits the results, and invokes concurrent batches. Previously, the batch processes were limited to one record at a time to ensure that Payments was compliant with Salesforce's limits.

Opt-In Instructions: If you want to enable this feature, please contact Blackthorn Support. There is no additional cost. Support will guide you through testing in a sandbox before determining the nal value for the batch size setting. The value is based on the speci c customizations in your org.


DocumentLink

Bug Fix
The contact email in the DocumentLink error message has been updated to the Blackthorn Support contact link. (Known Issue: 000003061)


Base Package

Enhancement
The Smart Scheduler (Blackthorn Base package) was added to the Blackthorn Candy Shop. Messaging customers can now use Smart Scheduler without downloading the Events or Storefront apps.

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


February 2024 - Version 6.13
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Important Update
The Smart Scheduler (Blackthorn Base package) was added to the Blackthorn Candy Shop. Messaging customers can now use Smart Scheduler without downloading the Events or Storefront apps.


Bug Fixes
When using an Authorize.net payment gateway, the customer's information will be captured and added to the customer's billing information section on the Transaction Detail page (in Authorize.net). Previously, the collected address information wasn't sent to Authorize.net even though the payment was received. (Known Issue: 000003103)
The auto-renew payment schedule will generate a new Transaction if the initial Transaction is paid with an ACH transfer. The payment schedule will also be updated appropriately after the Transaction is completed. Previously, a new Transaction was not generated, and the payment schedule was not updated correctly. (Known Issue: 000002886)


Line Item Object
The Line Item’s Total    eld will be calculated correctly when the record is created or updated. Previously, the Total   eld contained an incorrect value.

The Line Item’s Total description and help text have been updated.
Description: The Total amount, calculated as the Net amount plus Tax, less any written off amounts.
Help Text: The Total Amount including Tax, less any discounts and written off amounts.


Virtual Terminal Custom Settings
In the Blackthorn Payments | Virtual Terminal custom setting, the help text for the Disable New Payment Method and Default New Payment Method                elds was updated to remind users not to enable both options simultaneously.
Default New Payment Method : Shows the "New Payment Method" screen when loading the Virtual Terminal. Can't be enabled with "Disable New Payment Method."

Disable New Payment Method : Disables the ability to create a new Payment Method in the Virtual Terminal. Can't be enabled with "Default New Payment Method.”

In the Blackthorn Payments | Virtual Terminal custom setting, help text for the Show Address     eld was added. Help text: "When enabled, additional address elds (Street, City, State, and Country/Region) will be visible on the Payment Method creation page in the Virtual Terminal. These elds are required for certain Spreedly gateways.”


Enhancements
The introduction of high-volume batch processing resolves the issue of scalability with our batch processes. Previously, batch processes were limited to one record at a time to ensure that Payments was compliant with Salesforce's limits. The new protected custom setting is in Blackthorn Pay – Features.
Field Label: Auto-Change Batch Size
API Name: Auto_Charge_Batch_Size__c
Data Type: Number(3,0)
Description: Controls the batch size of the scheduled job. The default setting is 1. Currently, the maximum supported value is 75.
The labels of the Virtual Terminal versions have been updated to match the naming convention of the other custom components. Previously, both versions were similarly named and dif cult to tell apart.

## BT Payments Virtual Terminal

BT Payments Virtual Terminal -> BT Payments LWC Virtual Terminal


DocumentLink

Update
We received reports from some customers that Invoices were not loading correctly after the February release. While we investigate the issue, we have rolled back the DocumentLink webapp to the January release. The previously listed bug x will be included in the next release.

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


January 2024 - Version 6.11
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Bug Fixes
If a user changes a write-off Transaction’s Transaction Status from “Open” to “Completed”, the related Invoice’s Balance Due will be recalculated. Previously, the Balance Due did not update.
If a user deletes a write-off Transaction, the related Invoice’s Balance Due will be recalculated. Previously, the Balance Due did not update.

When prorating a Subscription, the Line Item's Unit Price will match what is in Stripe. Previously, Invoice Line Items that were created from a prorated Subscription showed the wrong Unit Price . (Known Issue: 000003034)
Subscriptions with an ACH Payment Method can now be automatically charged. Previously, a bug that was introduced in August caused Subscriptions with ACH Payment Methods to fail.


Enhancement
The Solution Id     eld was added to the new protected custom setting, Blackthorn Pay – Features. The protected custom setting will be created during package upgrades and new installations and can only be accessed and edited by Blackthorn. When Payments is installed/upgraded in production, the Solution Id   eld will be populated with
Blackthorn's partner ID and included when Blackthorn sends data to Authorize.net.


Mobile Payments FSL Updates

Bug Fix
The Offline Mobile Pay URL      eld was removed from the Work Order page layout URLs section as the system only uses the eld to launch the Mobile Payments app.

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


December 2023 - Version 6.8
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Bug Fixes
When a Stripe Transaction fails to process successfully, the Transaction Status        eld will update to “Failed” instead of “Pending Payment Intent”. Previously, the Transaction’s Transaction Status did not re ect the related Stripe status. (Known Issue: 000003047)

A user can complete the checkout process when a discount Code is applied across many different Events. Previously, users received the “Apex CPU time limit exceeded” error. (Known Issue: 000003052)
Users can process the "invoice.created" webhook with the updated trigger code. Previously, the trigger code caused the following error: "Variable does not exist: bt_stripe". (Known Issue: 000002859)
To ensure the webhooks generated for “customer.created” and “invoice.created” are processed immediately by the trigger, make the following updates to the Site Guest User/public user.
Step 1: To avoid permission errors, give the Blackthorn | Payments (Site Guest User) permission set Read access to the Product (Product2) object.
Click the Gear icon in the upper right-hand corner.
Click Setup.
In the Quick Find box, enter and click “Permission Sets.”
Create a new permission set.
Click New.
In the Label     eld, enter a descriptive name for the permission set, such as “Read Access to Product2.”

Click Save.
Con gure object permissions.
Click Object Settings or Object Permissions in the Apps section.
Find and click the Product (Product2) object. If you don’t see it, use the search function to locate it.
Click Edit next to the Products heading.
In the Object Permissions section, set Read to “Enabled” (checked). Do not enable Edit , Create , and Delete unless they are needed.
Click Save.
Step 2: Assign the newly created permission set to the public user.
Navigate back to the site you created.
Click Public Access Settings.
Click the View Users or Assign Users button.
Click the link for the site guest user.
In the Permission Set Assignments section, click Edit Assignments.
Move the newly created permission set from the Available Permission Sets column to the Enabled Permission Sets column.
Click Save.


PayLink

Webapp Release

Enhancement

PayLink now includes a more ef cient method to reduce the number of API calls required to con rm the user license status.


Bug Fix

PayLink will display the currency based on the value in the Currency Display        eld on the Paylink Con guration record. Previously, the Currency Display   eld value did not impact how the currency was displayed.

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


November 2023 - Version 6.6
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


New Feature: Allocations
The Allocation object now supports a Transaction with Transaction Type = “Write Off”.
When an Allocation record is created, it's related to an Invoice, a Line Item, and a Transaction. The Allocation record represents the allocation or a partial amount of the Transaction’s Amount and is related to a particular Line Item on an Invoice.


New Fields
Invoice object: Write Off Amount      eld
Field Label: Write Off Amount

API Name: bt_stripe__Write_Off_Amount__c
Description: If write-off Transactions are related, then this eld is automatically populated. If no write-off Transactions are present, then this eld will be blank.
Line Item object: Amount Written Off        eld
Field Label: Amount Written Off
API Name: bt_stripe__Amount_Written_Off__c
Description: Auto-populates when a write-off Allocation is related to Line Item.


New Field Updates
When an Allocation record is created, the following updates are made.

The related Line Item elds will be updated.
Amount Written Off

Balance Due = Total - ( Balance Paid + Amount Written Off )

The related Invoice eld will be updated.
Allocation Rollup      eld = Line Item Balance Paid - (Line Item Amount Refunded + Line Item Amount Written Off )
The Line item’s Balance Due      eld updates to re ect changes to Line Item elds, including Unit Price , Quantity , and Write Off Amount .


Updated Rollup Calculations
The following calculations were updated to include write-off amounts and the new elds on the Invoice and Line Item records.

Balance Paid: When the Allocation’s Type = "Payment" and the Allocation is associated with a Line Item object, then the Allocation’s Amount is automatically rolled up to the Line Item’s Balance Paid              eld.
Amount Refunded: When Allocation’s Type = "Refund" and the Allocation is associated with a Line Item object, then the Allocation’s Amount is automatically rolled up to the Line Item’s Amount Refunded                eld.
Amount Written Off: When Allocation’s Type = "Write Off" and the Allocation is associated with a Line Item object, then the Allocation’s Amount automatically rolled up to the Line Item’s Amount Written Off                 eld.

Balance Due: Line Item Balance Due = Line Item Total - (Line Item Balance Paid + Line Item Amount Written Off )
Retained Amount: Line Item Retained Amount = Line Item Balance Paid - (Line Item Amount Refunded )
Total: Line Item Total = Line Item Net Amount + Line Item Tax - Line Item Write Off Amount

Allocation Rollup: Invoice Allocation Rollup = (the sum of all Allocation Type = “Payment”) – (The sum of all Allocation Type = “Refund” + the sum of all Allocation Type = “Write off”)

Click here for a more detailed explanation of updated Allocations


Bug Fixes
If a user edits an Invoice record, the Invoice Fee Amount will now equal the sum of all fee Line Item amounts. (A fee Line Item is a Line Item with Is Payment Processing Fee = “True” (checked).) Previously, changes to the Invoice record caused the Fee Amount to reset to “0”.

Using the Virtual Terminal to test an Authorize.net ACH Payment Method when ECheck Type = “PPC” or “CCD” will no longer result in the ECheck Type                 eld changing to “WEB”. (Known Issue: 000002689)
Users who have upgraded their org to the Winter ’24 Salesforce release can now create a new Payment Method with the LWC version of the Virtual Terminal when Action = “New Single Charge”. Previously, creating a new Payment Method with Action = “New Single Charge” caused an error.
Attendees can successfully complete the checkout process when registering for an Event. Previously, an error related to duplicate logic prevented the Transaction from completing successfully.


Enhancements

Flow Screen Charge Component
Blackthorn Payments users can now translate the labels the user sees (and override the Standard out-of-the-box values) when using the Flow Screen Charge component.


Pre-requisite Step
Before proceeding, you must enable Translations in your Salesforce org. Follow the steps below to con gure the Flow Screen Charge component custom labels.

1. Navigate to Setup.
2. In the Quick Find box, type "Custom Labels".
3. Click Custom Labels.
4. Find the Custom Labels in the "PaymentChargeFlow" category or the ones with "ChargeFlow" as a pre x. (See the chart above.)
5. Click on the Label you would like to modify.
6. Click New Local Translations/ Overrides.
7. Select your Language .
8. Add the text for the label you would like to see displayed in the Translation Text       eld.


The language displayed will depend on the Language con gured in the User Setting of the Salesforce user.

The custom labels are as follows.

Custom Label Name                                                                                                                      API Name                                                                                           Standard Label (English)
ChargeFlow Account                                                                                                                   ChargeFlow_Account                                                                                                          Account
ChargeFlow Amount                                                                                                                    ChargeFlow_Amount                                                                                                           Amount
ChargeFlow Card Holder Name                                                                                                          ChargeFlow_Card_Holder_Name                                                                                                 Card Holder Name
ChargeFlow Card Number                                                                                                               ChargeFlow_Card_Number                                                                                                      Card Number
ChargeFlow Charge Card                                                                                                               ChargeFlow_Charge_Card                                                                                                      Charge Card
ChargeFlow_Charge Description                                                                                                        ChargeFlow_Charge_Description                                                                                               Charge Description
ChargeFlow_Contact                                                                                                                   ChargeFlow_Contact                                                                                                          Contact
ChargeFlow Currency                                                                                                                  ChargeFlow_Currency                                                                                                         Currency
ChargeFlow CVV                                                                                                                       ChargeFlow_CVV                                                                                                              CVV
ChargeFlow Email                                                                                                                     ChargeFlow_Email                                                                                                            Email
ChargeFlow Exp Month                                                                                                                 ChargeFlow_Exp_Month                                                                                                        Exp Month
ChargeFlow Exp_Year                                                                                                                  ChargeFlow_Exp_Year                                                                                                         Exp Year
ChargeFlow Payment Details                                                                                                           ChargeFlow_Payment_Details                                                                                                  Payment Details
ChargeFlow Payment Gateway                                                                                                           ChargeFlow_Payment_Gateway                                                                                                  Payment Gateway
ChargeFlow_Please_Wait                                                                                                               ChargeFlow_Please_Wait                                                                                                      Please Wait
ChargeFlow Postal Code                                                                                                               ChargeFlow_Postal_Code                                                                                                      Postal Code
ChargeFlow Related To                                                                                                                ChargeFlow_Related_To                                                                                                       Related To


DocumentLink

Enhancement
To improve DocumentLink’s performance and stability, the number of API calls required to validate a user license has been reduced.


Bug Fix
When viewing an Invoice with Line Items via DocumentLink, the Line Items will be displayed with the title and body grouped together, and the entire entry on a single page. Previously, Line Items were being split mid-way through a Line Item and placed on two pages. (Known Issue: 000002725)


PayLink

Bug Fix
Customers, who enter American Express card details on a PayLink payment form with a Spreedly gateway, will no longer run into an issue when entering the 4-digit CVC code. Previously, the user was automatically moved to the next eld after only entering three of the four Amex CVC digits. (Known Issue: 000002883)


If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


October 2023 - Version 6.4.1
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Enhancements

Spreedly
The reattempt logic for failed transactions processed via Spreedly is now supported. This logic schedules and tracks reattempted Transactions and triggers customizable actions based on the reattempt number.
Spreedly Payment Methods can now be created using the Salesforce UI (Payment Method tab).


Virtual Terminal
Admins can now use the new custom setting Hide Card Tab to con gure the Virtual Terminal. If Hide Card Tab is enabled, the option to create credit card Payment Methods from the Virtual Terminal will be removed. This setting can be applied to both versions of the Virtual Terminal.

Additional con gurations for the LWC Virtual Terminal will be dynamically displayed.
Settings applied at (Global) Custom Setting Level
If Hide Card Tab = “True” (checked), then the card tab will be hidden.
If Hide Card Tab = “False” (unchecked), then the card tab will be shown.

Settings applied at Component Level
If Hide Card Tab = “False” (unchecked) on both the component and global level settings, then the card tab will be shown.
If Hide Card Tab = "False" (unchecked) on the component level but Hide Card Tab = “True” (checked) on the global level, then the card tab will be hidden.

If Hide Card Tab = “True” (checked) on both the component and global level settings, then the card tab will be hidden.

A new Payment Method cannot be added via the Virtual Terminal when both the Hide Bank Tab and Hide Card Tab                elds are enabled.


Fees
Type , a new eld, was added to the Fee object. The eld is used to distinguish between tax fees and payment processing fees. Each type has a corresponding lookup eld on the Event object and different functionality. The Type         eld uses the same permissions as the Default Fee     eld.
Field Label: Type

Field Name: bt_stripe__Type__c
Data Type: Picklist
Picklist Values
“Payment Processing”
“Tax”
The new eld, Tax Display Setting , determines how taxes are displayed and calculated for an Event. To turn on tax-inclusive pricing, rst set the Fee record’s Type = “Tax” and then select a value for Tax Display Setting . Please note that taxes are always displayed separately on the nal payment screen.

Field Label: Tax Display Setting

Field Name: bt_stripe__TaxDisplaySetting__c
Picklist Values:
"Tax-Inclusive Pricing” - The advertised price will include tax.
"Calculated at Checkout” – The tax will not be visible until the nal payment screen.


Bug Fixes
The help text for the Retain Webhook Records for (Days)         eld in the Blackthorn | Payments Trigger custom setting was updated to match the user documentation and clarify the purpose and behavior of the eld. (Known Issue: 000002739)

After refunding the remaining amount on an already partially refunded Invoice, the Payment Status will now correctly show as "Refunded". Previously, the Payment Status remained as "Partially Refunded".

A refund Transaction will now be created after initiating a refund from within the Stripe dashboard. Previously, a refund Transaction was not created in Salesforce. (Known Issue: 000002939)
This also xed an issue for some customers where the Payment Gateway would not always populate when Transactions were created from webhooks.
The Payment Gateway and Transaction objects’ Accepted Payments Method            eld will now include the “Tap to Pay” value. Previously, the eld value was only available if users performed a new installation. Now the eld value is available for both newly installed and upgraded Payments packages.


Field/Layout Updates

New
Note: You may need to manually add these elds to the Fee object page layout.


Location: Fee object
Field Label: Type

Field Name: bt_stripe__Type__c
Picklist Values
“Payment Processing”
“Tax”
Field Label: Tax Display Setting

Field Name: bt_stripe__TaxDisplaySetting__c
Picklist Values:
Tax-Inclusive Pricing”
Calculated at Checkout”


If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


September 2023 - Version 6.3
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


It’s a New App!
Blackthorn Storefront is the lightest weight and easiest app to use to create a store from inside Salesforce. Add products to sell and let your customers add them to a cart and check out.

Storefront allows for the purchase of products including courses and digital items without an associated Attendee record. You can use your org’s existing Products and Price Books as well as integrate custom Forms into your store to ask custom questions and collect answers in Salesforce.

For more information about adding Storefront, please contact your CSM or Account Executive.


Enhancements
The following elds were added to the Payment Gateway object.
Field Name: TouchNet uPay Site ID

API Name: bt_stripe__TouchNet_uPay_Site_ID__c
Data Type: Text(15)
Field Name: TouchNet uPay Site URL

API Name: bt_stripe__TouchNet_uPay_Site_URL__c
Text(255)


Virtual Terminal
The following picklist values on the Action and Process Type           elds on the Virtual Terminal can now be translated using custom labels.

Action

“New Single Charge”
“New Payment Method”
Process Type

“Capture Now”
“Auto-Process”
“Authorize Now”


CVC Optional Feature
The following updates can be applied to the LWC and Aura versions at both the global level via the Virtual Terminal custom settings and locally at the LWC component level.


Admins can now control whether the ACH payment option (Bank tab) on the Virtual Terminal’s New Payment Method screen is available by using a new custom setting. The new custom setting, Hide Bank Tab , is accessed via the Blackthorn Payments | Virtual Terminal custom settings or the VT LWC Component Settings page.

Field Label: Hide Bank Tab
Description: If enabled, Bank details will be hidden from the list of available options when creating a payment method via the Virtual Terminal.
Functionality
If Hide Bank Tab = “True”, then the Bank tab will be hidden, and the user will only see the add card option.

If Hide Bank Tab = “False”, then the Bank tab will be visible.

A new custom setting called Make CVC Field Optional has been added to the Blackthorn Payments | Virtual Terminal custom settings. This setting allows users to make the CVC          eld optional when adding a new credit card Payment Method in the Virtual Terminal. The default setting is for the CVC   eld to be required.
Field Label: Make CVC Field Optional

Description: If enabled, the CVC eld will be optional when adding a payment method via the Virtual Terminal.
Functionality
If Make CVC Field Optional = “False”, then the CVC eld is required.

If Make CVC Field Optional = “True”, then the CVC eld is optional.


Bug Fixes
When the charge.refund.updated webhook runs, the refunded amount will be recorded as a negative amount and correctly re ected on any Invoice totals. (Known Issue: 000002873)
After a Transaction is disputed and a refund Transaction is created, the following will occur. (Known Issue: 000002253)
If the refund is a partial refund, the Retained Amount = the amount retained after the partial refund.
If the refund is a full refund, the Retained Amount = "0".

The Retained Net Amount = Retained Amount - Payment Gateway Fee (Dispute Fee).

If a Stripe ACH Transaction fails, Stripe will charge a Charge Fee and a Charge Failure Fee. This x ensures that both fees are recorded in Salesforce. (Known Issue: 000002910)
When a Transaction is captured via a Spreedly Payment Gateway, the Non-Gateway Transaction eld will no longer be set to "True" (checked), allowing Transactions to be synced with the Payment Gateway. (Known Issue: 000002920)
The four instances of “load_dataset” in the Candy Shop’s install path have been changed to “Load Sample Data.”


LWC Virtual Terminal

Known Issue: 000002905

The custom metadata mapping feature now works as expected and in the same manner as the original Virtual Terminal. Both versions of the Virtual Terminal now support data mapping in the same way.
The new LWC Virtual Terminal will correctly associate a newly generated Transaction with a Contact/Lead/Account when the Virtual Terminal is placed on the Contact, Lead, or Account object.
When the Blackthorn Payments | Virtual Terminal custom setting Hide Parent = "True", then the Parent            eld will not be displayed on the LWC Virtual Terminal.
Once a Transaction is successfully processed using the LWC Virtual Terminal, any values entered in the Virtual Terminal will be removed.


Field/Layout Updates
The following elds were added to the Payment Gateway object.
Field Name: TouchNet uPay Site ID
API Name: bt_stripe__TouchNet_uPay_Site_ID__c
Data Type: Text(15)
Field Name: TouchNet uPay Site URL

API Name: bt_stripe__TouchNet_uPay_Site_URL__c
Text(255)

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


August 2023 - Version 6.0.1
Once the updates listed below have been reviewed, please follow the (upgrade instructions) to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Enhancements

Tap to Pay
Users can now select Accepted Payment Method = “Tap to Pay” on the Payment Gateway, Transaction, and Payment User Override objects.


PayLink
When using PayLink, the Postal code      eld will be visible once a user selects a country. If the user selects the US, Canada, United Kingdom, Austria, Germany, or Switzerland, the Postal code   eld will be required.


Bug Fixes
To give users the ability to decide whether the “Bill To” and “Ship To” values on a DocumentLink should be automatically updated when a change is made to the Account or Contact details on a related Invoice, a new custom setting was created. (Known Issue: 000002824)
Name: Retain Invoice text values
Location: Blackthorn Pay - Trigger Settings.
Functionality
If Retain Invoice text values = "False", then the address Information elds will be updated on the Invoice record. This is the default setting.

If Retain Invoice text values = "True", then the address Information elds will not be updated on the Invoice record.

Changes made to the default Payment Method in Blackthorn Payments will be re ected in Stripe and vice versa. (Known Issues: 000002255 and 000002301)
Using Product eld values with decimals will now sync to Stripe without causing an error. (Known Issue: 000002857)
If the Amount on an authorized Transaction that uses an Authorize.net Payment Gateway is changed to a lesser amount, the Transaction’s Payment Status will be updated to “Partially Captured”. (Known Issue: 000002422)
The LWC Virtual Terminal will now run correctly inside the Salesforce Field Service Lightning app.
If a user clicks the Add Payment Fields to Page Layouts button on the Blackthorn Payments Admin tab after upgrading the Payments app, the Payment Method object’s ACH (Bank Account) page layout will include the Mandate Data section (and elds). The following elds are in the Mandate Data section.
Mandate Accepted At : The date/time that customer accepted mandate for ACH payment methods.

IP Address : The IP address from which the mandate was accepted by the customer.

Customer Acceptance Type : Indicates whether the mandate acceptance was performed online or of ine.

User Agent : The user agent of the browser from which the mandate was accepted by the customer.


Subscriptions
The UNABLE_TO_LOCK_ROW error that occurred after creating a Subscription in Stripe and modifying the related Invoice with a one-time Line Item has been corrected. (Known Issue: 000002008)
To ensure that an Invoice generated from a Subscription has the same Payment Method as the Subscription, a new custom setting was created. (Known Issue: 000002799)
Name: Update Invoices with Subscription PM

Location: Blackthorn Pay – Trigger Settings
Functionality
If Update Invoices with Subscription PM = "False", then the default Payment Method is updated on the Invoice when creating the Invoice record from the Subscription record.

If Update Invoices with Subscription PM is = "True", then the same (non-default) Payment Method is updated on the Invoice while creating the Invoice record from the Subscription record.
NOTE: The rst Invoice will always use the Payment Method from the Subscription. All subsequent Invoices will use the Payment Method determined by the Update Invoices with Subscription PM                eld.


Payment Gateway Customers
To prevent duplicate Payment Gateway Customer (PGC) records from being created when using the Mobile Payments app and a card reader, the following changes were made. (Known Issue: 000002785)
If a payment is submitted and a Contact or Account is selected, the Contact/Account will be related so future payments are matched to the existing PGC, preventing duplicate PGC records from being generated.
If a PGC record can't be matched to an id, we will attempt to match the PGC record against the parent Contact/Account and use the parent’s PGC record instead of creating a new record. If we nd an exact match, we will reuse the existing PGC record.
To prevent duplicate Payment Gateway Customer (PGC) records from being created when manually entering credit card details into the Mobile Payments app, the following will occur. If a PGC record that matches both the related Account and Contact records on the Transaction doesn’t exist, a new PGC record will be created. The new record will include
the Transaction's related Account and Contact records. (Known Issue: 000002785)
After accepting a payment with the Salesforce Field Service Lighting and Mobile Payments app, the Payment Gateway Customer record will be correctly associated with the Account or Contact details selected during the payment process. (Known Issue: 000002681)
To ensure that only valid email addresses are accepted in the Payment Gateway Customer’s (PGC) Email       eld, the following validation rule was added to the custom settings. (Known Issue: 000002133)

Name: Disable Customer Email Validation

Location: Blackthorn Pay - Trigger Settings
Functionality
If Disable Customer Email Validation = “False” and a user enters an invalid email address in the PGC record’s Email        eld, the user will receive the following message. “We hit a snag. Review the errors on this page. Email entered must be a valid email address format.”
If Disable Customer Email Validation = “True” and a user enters an invalid email address in the PGC record’s Email        eld, the user will NOT receive an error message and the PGC record will be created.


If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


July 2023 - Version 5.108.2
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Bug Fixes
Payments made with an Authorize.net Payment Gateway via a DocumentLink will now process correctly, resulting in no Blackthorn Logs being created. (Known Issue: 000002046)
The Unit Price of a Line Item now supports up to 12 decimal places. This will ensure that Line item and Invoice totals re ect the correct amount once they are pushed to Stripe, especially when the Unit Price is less than 0.01 and will be rounded up. (Known Issue: 000002765)

If the custom setting Enable Payment Intents for ACH PM's Custom = "True", a Transaction's Transaction Status will now be updated to "Completed" after the webhook is processed.
If the custom setting Automatically Create Allocation = "True" in Blackthorn Pay - Trigger Settings, then an Allocation will be created for each Line Item when the Transaction is captured. The same will occur when a Transaction is refunded. (Known Issue: 000002518)

When a payment using a TouchNet Payment Gateway is correctly processed from the Event Registration Page, Blackthorn Logs with the following error will no longer be created. “Invalid conversion from runtime type bt_stripe.PaymentGatewayTouchNet to bt_stripe.PaymentGatewayStripe” (Known Issue: 000002774)
If a Code with Type = “Discount” is applied to a Free Event Item at the Event Item level, the Code will be applied successfully.

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


June 2023 - Version 5.106
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Labeling Updates
To simplify the release note process, we have relabeled the different sections in the Release Notes. Going forward, each bullet point will be listed under either BT Salesforce Release or Webapp Release (previously referred to as a platform release). The BT Salesforce Release typically occurs the week before the Webapp Release.

For more information about the new terminology, please review Important De nitions.
To review the dates for each release type, please see the Blackthorn 2023 Release Dates.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Breaking Change / New Feature

The New Virtual Terminal
Our Virtual Terminal has been fully rebuilt in LWC to accommodate even broader use cases! It is supported in Lightning, Lightning Utility Bar, Salesforce Mobile, Salesforce Communities, Global Quick Actions, and Custom Components. The new Virtual Terminal can do everything our existing Virtual Terminal can PLUS the following.

Screen Flows: Drag and Drop the Virtual Terminal into a Screen Flow to create a seamless experience for your customers or internal Salesforce users.
Component Level Con guration: Discover even more granularity in con guration settings when placing the component on Lightning record pages.
Experience Cloud Guest User Compatible: Use the new Virtual Terminal on a public Experience Cloud page with restrictions.
The “Lite” Version: Explore the possibilities with the Virtual Terminal’s “Lite” Version, a single-page, payment form optimized for self-service and unauthenticated experience cloud use. Available in the Community Builder and in Screen Flow. Respects all mappings and settings.

NOTE: The existing Virtual Terminal will continue to be available for the foreseeable future.


Enhancement
The individual Related List components on the Invoice lightning page have been replaced by the Related Lists component. This allows users to edit the Related Lists via the page layout editor instead of having to add each Related List individually.


Bug Fixes
The Payout batch will no longer result in an error when a failed refund Transaction is associated with a charge Transaction.
Payments now supports processing webhooks sent on Stripe’s latest API version (2022-11-15). Webhooks sent on any Stripe API version should process successfully.
Additional duplicate protections were added to payment processing for Authorize.net gateways. (Known Issue: 000002748)
The issue causing Transactions to not be assigned to Payouts during the Stripe dispute process was xed.
Processing a mobile payment with a Stripe gateway will no longer result in a duplicate Payment Method with Payment Method Status = "One-Time" being created. The Transaction will be associated with the original Payment Method. (Known Issue: 000002723)

An intermittent issue that occurred when processing a mobile card reader payment has been xed. The app will no longer attempt to update the Payment Intent while the related Transaction is being captured.
If a user tries to add a Payment Method using the Virtual Terminal and the Related To      eld is left blank, they will receive the following message: "This eld is required: Related To".
The Name and Email        elds on the Create a Stripe Customer screen in the Stripe Billing Component are required to create a new Stripe customer.


If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


May 2023 - Version 5.103
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


New Virtual Terminal Feature
Virtual Terminal now supports ACH Direct Debit using Payment Intents with Stripe for enhanced Nacha regulation compliance.

Webhooks related to ACHv2 Payment Methods will process and update the appropriate record(s) in Salesforce successfully while ensuring no errors are created.
The following mandate elds have been added to the Payment Method object:
Mandate Accepted at (date/time eld)

Customer Acceptance Type

IP Address

User Agent

The ACH (Bank Account) page layout was updated to include the new Mandate Data section where the new elds are visible.
Blackthorn Payments (User) and Blackthorn Payments (Admin) permission sets were updated to include edit access to the new elds.
“Enable Payment Intents for ACH PMs,” a new custom setting, was added to Blackthorn Pay - Trigger Settings. Enabling the new setting will allow users to send ACH payments through Stripe’s Payment Intents endpoint (ACHv2).
1. Go to Custom Settings.
2. Click Blackthorn Pay – Trigger Settings.
3. Set Enable Payment Intents for ACH PMs = “True”.

4. Click Save.
When ACH Payment Intents are enabled, users will see the mandate acceptance text in the Virtual Terminal if the selected ACH Payment Method does not have the required mandate details.
When ACHv2 is enabled and a new or existing Stripe ACH Payment Method is charged via the Virtual Terminal, the mandate details including the following are recorded on the new Payment Method record.
Mandate Accepted at (date/time of acceptance)

Customer Acceptance Type (online)

IP address

User Agent (browser details)

When collecting mandate details in the Virtual Terminal, the Statement Descriptor from your Stripe account, located under Settings > Public details, will be displayed in the mandate text.
You can read more about using ACH Direct Debits with Stripe here: https://stripe.com/docs/payments/ach-debit


Enhancements
A global method that allows customers to process certain Stripe Billing webhook types asynchronously instead of via the Blackthorn batch jobs was added. If the Process Async checkbox = “True”, the existing web processing batch jobs will skip those webhooks.

Blackthorn customers are responsible for adding the logic that 1) sets the records they want as Process Async and 2) calls the async method to process them. The following example code creates a before trigger to check the Process Async box and an after trigger to call the async method.


Plaintext                                                                                                                                                                                                                                                                                                                               Copy

trigger ProcessWebhooksAsync on bt_stripe__Webhook_Event__c (before insert, after insert) {


if (Trigger.isBefore) {
for (bt_stripe__Webhook_Event__c webhook : Trigger.new) {
if (webhook.bt_stripe__Type__c == 'customer.created') {
webhook.bt_stripe__Process_Async__c = true;
}
}
}

if (Trigger.isAfter) {
for (bt_stripe__Webhook_Event__c webhook : Trigger.new) {
if (webhook.bt_stripe__Process_Async__c && webhook.bt_stripe__Type__c == 'customer.created') {
bt_stripe.ProcessEventStripeAsync(webhook);
}
}
}


}


NOTE: Replace 'customer.created' or add additional webhook types as needed.


Bug Fixes
The Stripe webhook type ‘charge.refund.updated’ is now supported and will processes correctly. Once processed, the Webhook Event’s Not Supported           eld will be set to “False” (or not checked) and the refund Transaction’s Transaction Status will be set to “Failed”. (Known Issue: 000002637)
Currently, PayLink doesn’t support allowing users to retry a payment after an initial failure. We’ve corrected the user interface to prevent users from retrying to make a payment, which resulted in an error. This update will happen on Tuesday, May 9 when the PayLink front end release occurs. (Known Issue: 000002644)
An error caused by clicking the Deploy Stripe Billing button in the Blackthorn | Payments Admin tab has been xed.
The following limitation has been added to the Check 21 Integration.
A warning message will appear when the Transaction to Account rollup batch job attempts to roll up more than 10,000 Transactions related to a single Account. This message lets users know the rollup job is approaching Salesforce limits and will appear as a Blackthorn Log.
If the batch job detects more than 40,000 Transactions rolling up to a single Account, the job will create a cap at 40,000 Transactions and generate a Blackthorn Log recommending users disable the batch job via Custom Settings.

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


April 2023 - Version 5.99.1
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Bug Fixes
“Disable Transaction Create From WO,” a new custom setting, was added to the Blackthorn Payments | FSL Settings. When the setting is checked, the automation that creates a Transaction related to a Work Order will be disabled.
Coupons with decimal values that are created in Stripe and Salesforce will now display the correct values.
To prevent errors when using PayLink, the Payment Method matching logic was updated to only match existing Valid or Veri ed Payment Methods.
DocumentLink will now correctly display the values on the underlying Invoice record, even if those values are manually updated.
If elds in a Field Set are marked as required, the elds will now appear as required elds in the Virtual Terminal.
The available Payment Method choices in the Virtual Terminal will now be ltered to only include the Payment Methods where the user also has access to the Payment Method’s Payment Gateway Customer record.

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


March 2023 - Version 5.95
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Bug Fixes
For Stripe Customers using the Dispute feature, the reversal Transaction Payment Method      eld would not populate with the original Payment Method. We've xed this defect so that the Payment Method    eld populates as expected.

Virtual Terminal users creating a new Payment Method can now set the Payment Gateway          eld when using the Virtual Terminal with the Virtual Terminal Mapping feature. The mapping feature has been updated so the Payment Gateway   eld will be populated according to the mapping setting.

When a Stripe ACH Transaction fails, the Transaction’s Balance Status will revert to null. This behavior is consistent with failed credit card Transactions.
Stripe users can now process a refund Transaction from Salesforce if the related Payment Method was deleted in Salesforce.

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


February 2023 - Version 5.93
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Off-Cycle Release

Events Version 3.89
January 31, 2023

Updates were made to the backend Attendee registration process to prevent duplicate charges and duplicate ERS records. To resolve this issue, customers MUST upgrade both packages to the latest Events (3.89) and Payments (5.92) versions.


Payments Version 5.92
January 31, 2023

The following updates were made to prevent a Coupon on the rst (prorated) Invoice from being applied to the entire Invoice as well as individual prorated Line Items when Proration Behavior = “Create Prorations” on a Subscription using a percentage off Coupon.


New Field
Location: Line Item object
Field Label: Is Not Discountable

API Name: IsNotDiscountable__c
Added to Stripe Billing permission set
Functionality
The default setting for this eld is “False”.
Users must set Is Not Discountable = "True" on any Line Item records that should not be discounted.


Bug Fixes
When using Stripe, the Captured Amount on an authorized Transaction record will be captured even if the amount is less than the authorized Transaction.
If a Stripe Billing Subscription Proration Behavior = “--None--” or is left blank, any changes made to the Subscription will no longer be prorated.

Previously, the trigger that summed the total Transactions related to an Account and populated the Historical Account Value       eld caused failures. The occurred during Check and Money Order scans for Check 21 and Mobile Payments users when more than 50,000 Transactions were related to a single Account. To prevent this from occurring, a new

custom setting in Blackthorn Pay - Trigger Settings was created. The new Disable Trans Rollup To Account custom setting will disable the trigger.


If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


January 2023 - Version 5.91
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Off-Cycle Releases

Events Version 3.89
January 31, 2023

Updates were made to the backend Attendee registration process to prevent duplicate charges and duplicate ERS records. To resolve this issue, customers MUST upgrade both packages to the latest Events (3.89) and Payments (5.92) versions.


Payments Version 5.92
January 31, 2023

The following updates were made to prevent a Coupon on the rst (prorated) Invoice from being applied to the entire Invoice as well as individual prorated Line Items when Proration Behavior = “Create Prorations” on a Subscription using a percentage off Coupon.


New Field
Location: Line Item object
Field Label: Is Not Discountable
API Name: IsNotDiscountable__c
Added to Stripe Billing permission set
Functionality
The default setting for this eld is “False”.
Users must set Is Not Discountable = "True" on any Line Item records that should not be discounted.


Bug Fix
Users can now create a new Payment Method and successfully complete a Transaction when using Blackthorn APIs with web forms and an Authorize.net Payment Gateway.


Enhancements

Version Updates

PayLink: Version 1.23
FSL Extension: Version 1.64


The current Payments package will be installed when a user installs PayLink from the Blackthorn | Payments Setup Wizard tab.
There is a new custom setting in Blackthorn Pay – Trigger Setting: Enable Auth Trans Rollup on WorkOrder .

With this setting enabled, if a Transaction is authorized for an amount less than the Balance Due on the Work Order, a new Transaction is automatically created with an amount equal to the difference between the rst Transaction and the original amount due.
The Balance Due and Balance Paid          elds on a Work Order will update automatically when a Transaction with an amount less than the Balance Due on the Work Order is authorized. This change allows these elds to be used with authorized charges.


Field Service Lightning (FSL) Extension Package

NOTE: If you are interested in the Blackthorn FSL Extension Package, please contact your account manager.


A new lookup eld, Payment Method, was added to the Work Order object. The new eld allows users to associate a Payment Method with a Work Order in the Field Service Mobile extension package.
NOTE: Users must have the Blackthorn | Payments FSL and Blackthorn | Payments (User) permission set to access the eld.
Field Label: Payment Method
API Name: btfslmobiletext__Payment_Method__c
Data Type: Lookup
An FSL user can add and authorize a payment or add a new Payment Method while connected to a Spreedly Payment Gateway. The authorized Transaction will be associated with an FSL Work Order to be used later.
To perform these tasks, two new elds -- Mobile Add Card and Mobile Authorize -- have been added to the Work Order object. The elds store links that launch the Mobile Payments app and take the user directly to the correct screen to complete the selected action. Both elds include the Blackthorn | Payments FSL permission set with Read
Access = “True”.

Field Label: Mobile Add Card

API Name: btfslmobiletext__Mobile_AddCard__c
Purpose: Contains the URL that will launch the Mobile Payments app directly to the add card screen.
Field Label: Mobile Authorize
API Name: btfslmobiletext__Mobile_Auth__c
Purpose: Contains the URL that will launch the Mobile Payments app directly to the authorize screen.


Spreedly with Cybersource
When using a Cybersource gateway connected via Spreedly to make a purchase or authorization, information in the Spreedly/Cybersource elds will be mapped to the following new elds on the Transaction object.
Field Label: Authorization Code

API Name: bt_stripe_Authorization_Code__c
Data Type: Text(255)
Field Label: Reconciliation Id
API Name: bt_stripe_Reconciliation_Id__c
Data Type: Text(255)
Transaction authorizations are now supported when using a Cybersource gateway via Spreedly.
A user can prede ne up to 20 elds to be passed as Merchant De ned Data from Salesforce to Spreedly/Cybersource so the data will be visible in Cybersource. While this will sync the Merchant De ned Data elds from Salesforce to Cybersource, it is not a bi-directional sync. Updates made to these elds in Cybersource will not be re ected in Salesforce.


AuthLink
Users can now send an authorization link (AuthLink) to customers to authorize the amount of a Transaction that was charged to the customer's Payment Method. This functions similarly to how PayLink already functions, with authorizations instead of charges.
The AuthLink will be created and stored in the Transaction record after the Transaction is created.

If an existing AuthLink is deleted and the record is saved, a new AuthLink will be generated.

The AuthLink will be generated at the same time as the PayLink .
Access to the AuthLink       eld requires the Blackthorn | Payments (User) permission set.

Field Information
Field Label: AuthLink

API Name: AuthLink__c
Type: URL(255)
When a user authorizes a payment via AuthLink, the Transaction’s Payment Status = “Authorized”.
Blackthorn supports AuthLink for Stripe, Authorize.net, and our supported Spreedly Payment Gateways.


Mobile Payments App - Android Release

Build - 1.1.11
Released 20 December 2022


Bug Fix

Updates to timeouts have been made to ensure Android Mobile Payments app users can log in and log out without experiencing periodic app crashes and successfully complete a payment.


Enhancements

Users can now create and authorize new Payment Methods using a Spreedly Payment Gateway via the Android Mobile Payments app.
When a Spreedly/Cybersource Payment Gateway is used to enter a Payment Method on the Android Mobile Payments app, the First name and Last name                 elds on the credit card screen are now visible and required.
To create a new Payment Method with a Spreedly Payment Gateway with Cybersource in the Android Mobile Payments app, users must complete the following billing address elds. These elds will automatically appear on the Payment Method entry screen when using a Cybersource gateway via Spreedly and map to the Billing Information elds
located on the Payment Method object.
Street (Field API Name: bt_stripe__Billing_Street__c)
City (Field API Name: bt_stripe__Billing_City__c)
State (Field API Name: bt_stripe__Billing_State__c)
Postal Code (Field API Name: bt_stripe__Billing_Postal_Code__c)
Country (Field API Name: bt_stripe__Billing_Country__c)
A customer’s billing address information will be captured correctly in the Android Mobile Payments app and populated properly in the Cybersource dashboard.
Users can now enable a setting that will take the user directly to the Payment Method entry screen after tapping a deeplink to the Android Mobile Payments app. To set up this feature, create a new Transaction with the following settings.
Record Type = “Charge”
Mobile Skip Intro Screen = “Yes”
In the Accepted Payments Methods multi-select picklist on the Transaction (bt_stripe__Accepted_Payment_Methods__c), move “Card (Typed)” to the Chosen column.
After doing this, the following deeplinks will now navigate directly to the Payment Method entry screen:
“Mobile Pay” (btfslmobileext__Mobile_Pay__c) on the Transaction
“Mobile Pay” (btfslmobileext__Mobile_Pay__c) and “Mobile Authorize” (btfslmobileext__Mobile_Auth__c) on the Work Order related to the Transaction (Transaction lookup eld “btfslmobileext__WorkOrder2__c”)
When using the Android Mobile Payments app, users can now turn off the send receipt screen after authorizing or capturing a Transaction by enabling the new Custom Setting “Skip Receipt Screen”. This can be found under Setup > Custom Settings > Blackthorn Payments | Mobile Settings > Manage.
If Skip Receipt Screen = "True", then the last screen will not show the option to send a receipt.
If Skip Receipt Screen = "False", then the last screen will show the option to send a receipt.

Field Information
Field Label: Skip Receipt Screen
API Name: bt_stripe_Skip_Receipt_Screen__c
Data Type: Checkbox

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


December 2022 - Version 5.85
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Enhancements
Plaid users can now add a customer’s name and email to the Bank section of the PayLink form.
To ensure new Payment Methods created via a Cybersource (via Spreedly) Payment Gateway are created with all mandatory elds, validations have been added to ensure users ll in the Street , City , Country/Region , and State             elds.


Bug Fixes
New installations of the Payments app will successfully complete the “Setup Payment Jobs” step and the overall installation process.


Transactions
When Work Order Line Items are deleted from a Work Order, the amount of the related Transaction record will update accordingly.
Resolved an issue preventing Payout records from being created after Transaction records were synced via the Historical Sync feature.
Corrected an issue that was causing multiple changes to the Net Payment Gateway Fee         eld on Disputed Transaction records.
Chargeback Transaction records (refunds) are now properly relating to Payout records in Salesforce, as they are in Stripe.


Stripe
Coupons ( Amount Off and Percentage Off ) applied to prorated Subscriptions in Stripe will be applied only at the Invoice level and not at the prorated Line Item level.

Coupons cannot be applied on a Stripe Invoice Line Item; they can only be applied on the Invoice itself.
When a Stripe Invoice Line Item is changed in Salesforce, the update will be pushed to the Invoice in Stripe.
After completing an ACH Transaction using a Stripe Payment Gateway via PayLink, the micro-deposit prompt will no longer be visible since Stripe waives micro-deposits.
Additional updates have been made to prevent the micro-deposit message from appearing when Stripe has waived the micro-deposit requirement, the Skip ACH Validation custom setting is enabled, and a Transaction with an ACH Payment Method is being processed via PayLink.

When a Stripe Payment Gateway that was set up with Plaid is used to complete a Transaction via PayLink, the Customer Name & Email will be captured correctly, populated on the Payment Gateway Customer record, and sent to Stripe.


Authorize.net
An error was resolved that occurred when using Authorize.net and PayLink which caused the Bank Account Type selector to appear inactive when a user tried to make an ACH payment.

To prevent incorrect duplicate Transactions when using Authorize.net, a new custom setting labeled “Duplicate window” was added to ”Blackthorn Pay - Trigger Settings”. The new custom setting includes the following functionality.
The user is UNABLE to capture the duplicate Transaction when
the Transaction is within the time mentioned in the Duplicate window custom setting
the Duplicate window = “NULL” in Custom Settings

The user is ABLE to capture the duplicate Transaction when
the time is after the time set in the Duplicate window custom setting
running the Batch Job


Invoice
If the Street 2 (Bill To)     eld in the address is populated on the Invoice, the second line of the address will now be visible on the DocumentLink.
Changes made to the Invoice’s Compact Layouts will be retained after upgrading the Payments app.
After an ACH payment is made via a DocumentLink, the Balance Due         eld on the Invoice will update to zero and the PAY button will no longer be visible.


Virtual Terminal
When using the Virtual Terminal to create a new Payment Method, users must populate the Related To              eld in order to save the new Payment Method. This is to ensure the Payment Gateway Customer and Payment Method are linked to an existing Contact or Account.

Updated the Virtual Terminal to ensure the “New Payment Method” action loads properly after Salesforce orgs are upgraded to the Winter ‘23 release.


If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


October 2022 - Version 5.76
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Off-Cycle Releases

Version 5.75
(September 21, 2022)

Payment Methods created using a Spreedly / Cybersource Payment Gateway in the Virtual Terminal will now successfully capture Transactions.
A new Custom Setting called “Show Address” has been added to the Blackthorn Payments | Virtual Terminal Custom Settings. When the Show Address checkbox is enabled, additional address elds ( Street , City , State , and Country/Region ) will be visible on the Payment Method creation page in the Virtual Terminal.
We’ve resolved an issue related to failed Events checkouts when using an Authorize.net Payment Gateway.
Authorize.net users will no longer encounter a failed payment scenario when using the Virtual Terminal on a Contact record where the Email    eld on the Contact is blank.


Version 5.75.1

(September 28, 2022)

The following update is a Feature Flag. Users are now able to store a Payment Method created via the Spreedly integration in the Payment Gateway as well as interact with it outside of the Spreedly integration.

Custom Settings: Blackthorn Pay - Trigger Settings
New Field: Save PM to Gateway Vault From Spreedly
If Save PM to Gateway Vault From Spreedly = “TRUE”, the Third Party Token           eld on the Payment Method record will be populated.

If Save PM to Gateway Vault From Spreedly = “FALSE”, the Third Party Token           eld on the Payment Method record will NOT be populated.

Payment Method Object
New Field: Third Party Token

API Name: bt_stripe.payment_method.third_party_token


Bug Fixes
When a Footer image is added to a DocumentLink Template and the Template is related to an Invoice, the downloaded Invoice pdf will display the Footer image correctly.
Clicking the Deploy Stripe Billing button on the Blackthorn | Payments Admin tab will successfully deploy the Stripe Billing elds to the Opportunity page layout.

Custom Metadata mapped elds in Stripe will now be populated automatically after completing the registration process for a paid Event.
After creating a new Subscription in Salesforce, the text added to the Memo eld on the Subscription record will sync to the Memo eld on the Invoice in Salesforce and subsequently in Stripe.

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


September 2022 - Version 5.71.2
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Bug Fixes
A validation rule has been added to prevent users from deleting the last Subscription Item on a Subscription, as this action is not supported by Stripe and results in an error.
If the Terms and Conditions URL eld on the PayLink Con guration is populated, the Terms and Conditions will be visible during the transaction, even if the Acceptance Language       eld is left blank.
To prevent errors from occurring when editing a Payment Method, the Stripe integration will use the postal_code parameter instead of the zip code.
An error related to Historical Sync, which would cause the job to loop in response to an error message from Stripe, has been xed. The synced data will now be displayed correctly.

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


August 2022 - Version 5.70
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Bug Fixes
When a non-default Payment Method is selected on a new Stripe Invoice in Salesforce, the selected Payment Method will no longer be overridden by the default Payment Method when the Invoice is pushed to Stripe.
When a user creates a new Payment Method with a bank account (ACH) that already exists as a Payment Method, the Payment Method Status will be set to “Invalid”. The Error Message       eld will display the following message: “Duplicate - A bank account with that routing number and account number already exists for this customer.”
Government Cloud users who want to use PayLink need to reach out to Blackthorn Support to have instanceUrl added to their PayLink license.

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


July 2022 - Version 5.66
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Enhancements
If a user creates a Stripe Subscription with the Billing Method = “Charge Automatically” and the custom setting Disable Stripe Pay Immediately set to “True” and then pushes the Subscription to Stripe, the user will be able to edit the Subscription Invoice before submitting it to the recipient.


Bug Fixes
A disputed Transaction’s Transaction Status and Payment Status will only undergo the minimum number of required status changes during the dispute process.
Users will no longer receive an error when making a payment from a DocumentLink via an authorize.net Payment Gateway if the new credit card details match the credit card details of an existing Payment Method.
For Orgs that use the State and Country picklists on their Contact and Lead records: if a user enters an incorrect country or state on the Payment Gateway Customer, they will no longer receive the error “There’s a problem with this country.” The Contact or Lead record will be created as expected; however, the following elds will remain blank.
Contact record: Mailing State/Providence and Mailing Country          elds

Lead record: State/Providence and Country         elds

If Stripe has waived the micro deposit and the Skip ACH Validation     eld is enabled, proces


Android Mobile Payments App Updates

For information about the most recent Android Mobile Payment App updates, please review the Android Mobile Payments app Release Notes.


If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


June 2022 - Version 5.63
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Enhancements

Virtual Terminal
The Process button on the New Single Charge screen of the Virtual Terminal will remain grayed out until the Payment Method information is added.
If a user clicks the + Add New button on the Virtual Terminal to create a new Payment Method and then clicks the Add + button on the New Payment Method screen without completing the required credit card elds, they will receive an error message. The error message will display the following message for each corresponding eld.
“This eld is required: Name on card”
“This eld is required: Card number”
“This eld is required: Card expiration”
“This eld is required: CVC”
“This eld is required: Postal code”
If a user clicks the + Add New button on the Virtual Terminal to create a new Payment Method and then clicks the Add + button on the New Payment Method screen without completing the required bank details, they will receive an error message. The error message will display the following message for each corresponding eld.
“This eld is required: Name on account”
“This eld is required: Routing number”
“This eld is required: Account number”
“This eld is required: Account holder type”


Donations
Users can now add Donation’s “Embedded Form Code” as a module on a Hubspot landing page and successfully preview the page.


Candy Shop
The PayLink package will be installed and the PayLink Admin permission set will be assigned automatically when the Payments app is installed from the Candy Shop.


PayLink
The PayLink package will be installed and the PayLink Admin permission set will be assigned automatically when the Payments app is installed from the Candy Shop.
When Bacs Direct Debit is enabled for PayLink w/Stripe Checkout, users can now complete Payment Transactions using a Bacs Direct Debit account.


Bug Fixes
The following default settings will now install correctly after installing Payments 5.57.
The Opportunity and Invoice will now be included in the Transaction Relationships in the Payment Setup Wizard.
The Default Relationship Settings record will now be available in the Relationship Settings object.
If a user tries to enter a card number in the Name on card    eld when adding Payment Method via the Virtual Terminal, they will now receive an “Adding Payment Failed - Name on card eld is not valid” error. Additionally, a customer record in Stripe with the card number as the Name will no longer be created.


Stripe
Multiple refund Transactions will no longer occur after a single ACH Dispute has been processed in Stripe.
An error was resolved, preventing mapped Stripe Metadata from syncing automatically from Salesforce to Stripe.
When a business wins a Stripe Dispute with submitted evidence, the Webhooks will now process correctly to create a new Transaction that shows the funds were reinstated and credited back to the business.
After winning a disputed charge in Stripe, the correct amount will be credited back to the account and re ected in the Retained Net Amount    eld.


DocumentLink
When viewing an Invoice from a DocumentLink, the Phone provided on the DocumentLink Template will now appear in the Company Info section of the Invoice.

An image added to the Footer section of a DocumentLink Template will no longer cause the Invoice to load incorrectly.


Android Mobile Payments App Updates

For information about the most recent Android Mobile Payment App updates, please review the Android Mobile Payments app Release Notes.


If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


April 2022 - Version 5.58
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Breaking Changes
We no longer set the value of the Proration Behavior         eld on Subscriptions to “Create Prorations” to prevent Coupons from being applied multiple times to the same Subscription.

The Record Type option, ”Order”, on an Invoice has been deprecated. When manually creating a new Invoice, users can now choose from “Stripe Invoice” or “Invoice”.

The “All Order” list view on the Invoices object has been removed.


Enhancements
Updates to the Payments Setup Wizard have been made.
For new installs, the following changes were made to the “Blackthorn | Payments Transaction Rollup To Parent” scheduled job.
After installing Payments, the "Blackthorn | Payments Transaction Rollup To Parent" scheduled job will no longer be automatically scheduled.
To opt-in to the “Blackthorn | Payments Transaction Rollup To Parent” scheduled job, the Payments Admin will need to go to the Blackthorn | Payments Admin page and click the Schedule Transaction Rollup to Parent Job button.
If Disable Trans Rollup to Parent is set to “True” in Blackthorn Pay - Trigger Settings and “Blackthorn | Payments Transaction Rollup To Parent” is scheduled, then real-time rollups do NOT run, but the scheduled batch job DOES run every hour to process rollups.


NOTE: For existing users, clicking Schedule Recommend Payment Jobs will no longer trigger the “Blackthorn | Payments Transaction Rollup To Parent” scheduled job. You will need to click the new Schedule Transaction Rollup to Parent Job button.


Stripe Billing Component
The following updates were made to the Stripe Billing Component to allow Invoices to be associated with Subscription Schedules.
The Subscription Schedule        eld was added to the Invoice object.

When a Subscription Schedule is created, the Subscription Schedule look-up will be auto populated on the Invoice.

Related Invoices will also be displayed on the Subscription Schedule page as a Related list.
The Stripe Billing Component can now be added to the Opportunity page layout by clicking the Deploy Stripe Billing button on the Stripe Billing page in the Blackthorn | Payments Admin tab.


Bug Fixes
The eld Webhook Batch Delay Minutes was added to the “Blackthorn Pay - Trigger Settings” (Custom Setting). If the new eld is set to a speci c amount of time by the system user, new incoming Webhook Events will process only after the previously set amount of time has passed. This will prevent duplication of records when Webhook Events

process prior to receiving API responses back from the Payment Gateway.


Stripe
An error preventing Dispute Evidence records from syncing to Stripe after setting the Type value has been resolved.

If a Line Item on a Stripe Invoice is deleted in Stripe, the Line Item will also be deleted on the Salesforce Invoice record.
If a user deletes a Payment Gateway Customer in Stripe, the Deleted From Payment Gateway             eld on the Payment Gateway Customer record will be checked.
A data conversion issue has been resolved so customers can now successfully send numbers in a decimal format from Salesforce to Stripe Metadata.
A Coupon, which is added to a subscription in Stripe, will now be populated in the Coupon         eld in the Subscription Schedule phases in Salesforce.
When using Coupons with Invoices, Coupons will only be attached to the Invoice in Stripe without being attached to the Customer in Stripe.
All changes made to the Description        eld of a Transaction will now be pushed to Stripe consistently.

Prices with Tiers can now be properly synced from Stripe when using Webhooks or Historical Sync.


Virtual Terminal
An error affecting Virtual Terminal users has been resolved for customers who previously used and uninstalled our Blackthorn FSL extension package.
An error message will no longer be displayed when capturing a payment using the ACH Payment Method in the Virtual Terminal. The Transaction Status will be set to “Completed” and the Payment Status will be set to “Captured”.


Authorize.net
A validation check will now block live Authorize.net accounts from being connected in Salesforce sandboxes to prevent users from inadvertently charging live payments from test environments.
Errors that occurred after using PayLink to charge the same customer more than once using Authorize.net have been resolved.


Donations
ReCaptcha will remain visible on the Donations payment screen even if the donor moves backward and forward within the Widget.
To ensure the image will be displayed correctly on the Donation Form after adding the Image URL to the Content eld, the user will need to make sure one of the Events, Payments, or PayLink packages are installed and authorized.


Android Mobile Payments App Updates

For information about the most recent Android Mobile Payment App updates, please review the Android Mobile Payments app Release Notes.


If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


March 2022 - Version 5.53
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
To upgrade Payments to the newest version, go to the Blackthorn Candy Shop.


Enhancements

Stripe Billing Component
The order of options on the “Select the Billing Frequency and Currency” screen have been reordered. Users will now see them in the following order: Select Subscription Billing Frequency (Interval) , “Advanced,” and Currency .

On the “Review Subscription Details” screen, the text “Number of periods between the above Billing Frequencies” has been changed to “Number of periods between billing cycles.”
The name of the “Select Coupon” screen has been changed to “Select a Coupon”.
The “Select or Create a Coupon” label on the “Select a Coupon” screen (previously “Select Coupon”), has been changed to “Select a Coupon”
When the Prorate this Subscription? option is set to “Active” on the “Select Subscription Dates and Billing Details” page, the Select a Proration Behavior option will be removed and the Proration Behavior on the new Subscription will automatically be set to “Creation Prorations.”

If a user tries to set the Trial - End Date to a date or time that is AFTER the Future Billing - Start Date , the user will see the following message: “Trials must end before or on the billing cycle start date. You need to adjust either the billing cycle start date or the trial end date.”

The Payment Gateway will be updated based on the Customer de ned on the Opportunity. As a result, the user will not be prompted to choose a Payment Gateway or Payment Gateway Customer. Instead, the “Select the Billing Frequency and Currency” page will appear after clicking the Next button on the “Create New Stripe Billing Subscription”
page.
The following updates were also made to the “Create New Stripe Billing Subscription” page.
The header on the “Select the Stripe Customer” page has been changed to “ Select a Stripe Customer”.
On the “Select a Stripe Customer” page, the Select a Customer picklist will display a list of customers with email addresses that are related to the selected Gateway and to the same Account as the Opportunity.
After clicking the Create Customer button on the “Select a Stripe Customer” page, the header on the next page will now be “Create a Stripe Customer”. The “Select a Contact” screen will not be visible if there are no Contacts related to the Account.

The Email     eld on the “Create a Stripe Customer” page is now a required eld.

A Description      eld was added to the “Create a Stripe Customer” page.


Bug Fixes
If a Payment Gateway Customer is deleted and a new Payment Method is created with the previous Payment Gateway Customer’s credit card details, a new Payment Gateway Customer with a valid Payment Method will now be created.
Users without API access can now create new Line Items for an Invoice.
After creating a Line Item on an Invoice with the Quantity left blank, the Quantity on the Line Item will default to "1".
The label for the Sales Document lookup eld (conference360Sales_Documentc) on the Opportunity object has been changed to Invoice . This change will ensure the Events package has the correct label updates for Invoice (previously Sales Document).
The Payment Gateway Customer matching rule will no longer block the creation of duplicate Payment Gateway Customers when those customers are using different Payment Gateways.
NOTE: Users upgrading Payments will need to manually deactivate the current "Payment Gateway Customer Dup Rule" matching rule and activate the new Payment_Gateway_Customer_Matching_Rule2 matching rule. The new matching rule will be installed automatically for new installations.


Stripe
When a Transaction is successfully disputed in Stripe, the Transaction Id on the chargeback reversal transaction (refund) will now populate correctly.
When the Subscription Schedule is canceled in Stripe, the following will now occur:
The Subscription Schedule Status is updated to “Canceled”.

The Canceled On Date on the Subscription Schedule is updated to the date the Subscription was canceled.

In Salesforce, if a user edits or clears the value of a eld which is mapped to Stripe Metadata, then the change will now automatically get pushed to Stripe.
Tiers created in Stripe related to Prices will now be created in Salesforce when using webhooks or the historical sync functionality.
After winning a disputed charge in a Stripe gateway, the Net Amount of the nal reversal charge will show the $15.00 Stripe dispute fee as added to the original Amount instead of deducted from it.


Virtual Terminal
The logic in the Virtual Terminal has been updated to prevent users from receiving the "Cannot read properties of null" error when trying to add a Payment Method. The user should now select a Related To record before adding a new Payment Method.


Authorize.net
The Email     eld on the Payment Method will no longer be cleared out after processing Payment Method webhooks from Authorize.net.


Spreedly
To prevent the 'bill_to_city' parameter in a Spreedly transaction payload from being left blank after processing a transaction, the payload structure and api method were updated to include the Payment Method address elds.


DocumentLink
Images set on an Invoice record in the elds DocumentLink Field 1 or DocumentLink Field 2 will now load properly when viewing the DocumentLink.


Android Mobile Payments App Updates

For information about the most recent Android Mobile Payment App updates, please review the Android Mobile Payments app Release Notes.


If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


February 2022 - Version 5.49
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
1. Review the Bug Fixes.
2. Install Version 5.49 of Blackthorn Payments here.
Production Install Link
Sandbox Install Link


3. Navigate to Blackthorn | Payments Setup W izard, click the PayLink tab, and install the latest PayLink package.


Enhancements
Per changes made in the January 2022 release, all references to Sales Document have been changed to Invoice.
When a user uses the Virtual Terminal to add a Payment Method or make a payment, they will no longer see suggestions or auto- ll capabilities in the Payment Method eld of the New Single Charge screen.
To ensure the entire text, “Payment information will be collected after clicking “Complete”” on the checkout form translates correctly, a translation label for "Payment information will be collected after clicking “COMPLETE”" was added to the Data Dictionary Group. The translation labels, “LBL_PAYMENT” and “LBL_REGISTER” were also added to the
Tabbed UI.
The following updates have been made to the Blackthorn | Payments Setup Wizard.
“Connect to Gateway” tab
The size of the Skip and Connect Later button has been increased.
The message “If you're doing the setup as part of Blackthorn Events for just free events, skip this step, but nish the wizard.” has been added.
“Record Types” tab
After choosing “Yes” and clicking the Make magic happen button, the “Other” Record Type will be assigned to the Payment Method of that pro le.

“Relationships” tab
The Invoice label and message, “Included: Invoice and Opportunity” will now be displayed.
The buttons Create and Continue have been combined into a single button, Create & Combine .
The Create & Combine button will not appear until the user selects an object from the Select object(s) dropdown.

“Virtual Terminal” tab
The “Virtual Terminal” tab has been added between the “Relationships” and “PayLink” tabs.
An embedded video explaining what the Virtual Terminal is and a link to its user guide has been included.


Bug Fixes
Creating a Stripe Billing Subscription with an applied Coupon will no longer cause the Coupon to be added at the Payment Gateway Customer level after the webhooks process. The Coupon will also not be visible in the Customer record in the Stripe Account.

If there is a problem adding the Payment Method via the Virtual Terminal, the error message from the gateway will now be displayed to the user.
Users with a Salesforce Platform licenses will not longer receive an insuf cient permissions error when creating Transactions in an org where Opportunity is set up as a Transaction Parent.
After updating the Memo or Billing Method         elds on an Invoice in Salesforce, the information will be pushed to Stripe correctly and the new values will be mapped to Stripe correctly. To stop invoices from being sent before they are ready, users can check the Disable Send Invoice Immediately   eld in the “Blackthorn Pay - Trigger Settings.”
When using Stripe Connect, webhooks from Stripe will now correctly create an ACH External Account (Payment Method) as "Veri ed" in Salesforce if that account is already veri ed in Stripe.
When using the Payments Setup Wizard, users are now able to navigate from the “PayLink” page to the “Let’s Get Started” page by clicking the Continue button.
When there are over 200,000 Invoice records in an org, a user can now successfully register an Attendee for an Event without generating a Blackthorn log with an error message. Additionally, the following will occur.
When a new Invoice record is created, the Name       eld will be populated with the same value as the Invoice ID.

The Name       eld on an Invoice will be auto-populated when a user leaves it blank.
The Name       eld on an Invoice will not be overwritten when a user adds a value.


Compliance
On the Manage App tab of Blackthorn Compliance, users can click the Enable Daily Audit / Disable Daily Audit button to schedule the automated daily audit. The automated process queries all records in your org to check for the con gured regex patterns.

IP Addresses are now supported for out-of-the-box masking on Case records. To enable this, complete the following steps.
1. Go to Setup.
2. Search for and click “Custom Metadata Types.”
3. Click Manage Records next to “DetectionPattern.”
4. You can now enable IP Addresses for matching and con gure the Case elds you would like to match on.
The Case lookup eld will be auto-populated in the Log record when the Case record is submitted with any or all of the following: Subject , Description , and Internal Comments .
The Negative Detection Pattern will now prevent the masking of postal tracking codes, such as in the scenario of VISA detection patterns masking postal tracking codes. To ensure this occurs, the logic was updated to trap negative patterns rst and not run matches with positive patterns.


Field, Object, and Layout Changes

New Fields, Objects, and Layouts
The “Virtual Terminal” tab has been added between the “Relationships” and “PayLink” tabs.
The Enable Daily Audit / Disable Daily Audit button has been added to the Manage App tab in Compliance.


General Updates
The component logos and labels in the Lightning App Builder have been updated to include the new Blackthorn logo and labeling convention.
The objects/tabs in Blackthorn's apps have been updated so a unique icon represents each app.
A Refer A Friend button has been added to the following admin pages/wizards.

Blackthorn | Payments Admin tab
Blackthorn | Events Admin tab
Blackthorn | Donations Admin tab
Blackthorn | Compliance Admin tab
Blackthorn | Payments Setup Wizard tabThe respective admin can click the Refer A Friend button to share a friend's name and email address with Blackthorn.
A new user’s license will automatically be applied when the license is authenticated through OAuth during the installation of Payments and Events. This step will streamline the installation process.

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


December 2021 - Version 5.46
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
1. Review the Bug Fixes.
2. Install Version 5.46 of Blackthorn Payments here.
Production Install Link
Sandbox Install Link


3. Navigate to Blackthorn | Payments Setup W izard, click the PayLink tab, and install the latest PayLink package.


Enhancements
The Chat button is now available on the Payments Setup Wizard and Blackthorn | Payments Admin screens.
Updates to the Blackthorn | Payments Admin tab:
The Metadata Updates button was changed to Upgrade .
The Deploy Record Types button on the Upgrade tab was changed to Enable All Record Types . To enable all record types, click Enable All Record Types , go to the Payment Method tab, and click New . The new Record Type , "Other" will be listed with "Card" and "ACH".
To add the Accepted Checkout Payment Methods          eld to Payment Gateway object, go to Blackthorn | Payments Admin, click Upgrade , and click Add Payment Fields to Page Layout . Go to the Payment Gateway record to con rm the eld was added.
The Add Picklist Values button was added to the Upgrade tab.
To add "Stripe Checkout" to the Allowed Payment Methods         eld, go to the PayLink Con guration object and click New . Go to the Payment Gateway record to con rm the eld was added.
Users can now download a PDF invoice from a DocumentLink without being required to submit a payment via a connected Payment Gateway. The Pay button on the DocumentLink may be visible or hidden, but the Download button will always be visible.
The new Stripe Billing component is in Beta release. If it is manually added to the layout, the user will see that the Product Type dropdown on the Choose Price for each Product element on the Opportunity record has been changed to a radio button.
The Source (Object) and Source (Field) elds have been added to the Stripe Metadata Mapping default layout.


Bug Fixes
Using Historical Sync will no longer cause Transactions to be overwritten with the data from other Transactions.
When a Sales Document is associated with a Lead, the name associated with the Lead will appear in the Bill To          eld on the Sales document.

To prevent a Transaction from being incorrectly updated after multiple payment attempts, the Transaction Status will change to “Failed” when the charge (transaction) fails and is not left in “Open” status.

Instead of duplicate transaction reattempts being created, only a single transaction reattempt will be created after a charge.failed webhook processes the rst reattempt.


Virtual Terminal
Users will no longer receive an error related to the record Id attribute when adding the Virtual Terminal aura component to a Lightning page.
A Payment Gateway Customer’s addresses will now be automatically pushed to Stripe after creating a new Payment Method for that account in the Related To               eld of the Virtual Terminal.

Source elds will only map to elds in the Virtual Terminal when speci c mapping exists between the source and target elds. Extra elds will no longer map to a transaction from an object record when no metadata mapping has been con gured for those elds.
The Parent Object       eld in the Virtual Terminal will now correctly auto-populate with the current Transaction parent object as long as it is de ned in the Custom Settings.


PayLink
Government Cloud users can now authorize PayLink successfully after reaching out to the Support team to provide their Salesforce Domain.
If a payment fails using PayLink, we now expose the error description given by the payment gateway instead of a generic error message. The new error message will be visible as of January 7, 2022.


Stripe
When a subscription is canceled and unpaid invoices are voided, the Account subscription rollup elds will update accordingly.
After creating a new Subscription, the accompanying webhooks will process, ensuring that the existing Subscription Line Items are not duplicated and match what was sent to Stripe.
After making multiple payment attempts that are related to a single Payment Intent in Stripe, a separate record will be made in Salesforce for each failed Transaction (payment attempt).
To prevent invoices from being sent prematurely when updating a eld on a draft invoice, check Disable Send Invoice Immediately in “Blackthorn Pay - Trigger Settings.”

Deleting text in a Payment Gateway Customer (PGC) eld will now automatically update the relevant eld in Stripe.


Authorize.net
When processing a CIM pro le/payment method without an email address in Authorize.net, the net.authorize.customer.created webhook will process correctly and create a new record or update an existing one.
The Payment Method Email will no longer be deleted after a webhook is processed for Authorize.net.


Compliance
When using Blackthorn Compliance in trial mode, users can mask a maximum of 10 records. At the 11th record, a log le that says, "This record was not masked as this org’s license has run out of masked record allowances. Contact Blackthorn.io for questions." will be created.
The Case    eld in the Log record will now auto-populate when a a eld is masked on a Case record.


Donations

Enhancements
To assist with security, the reCaptcha setting on Donations forms will automatically be turned on.


Bug Fixes
When the Custom Setting Disable Payments Validations is enabled and a user unchecks the Paid checkbox on an NPSP Payment record, validation errors will no longer appear on the NPSP Payment record.

On the Donations form, the spelling of “processing” in the Processing Message has been corrected.


Field, Object, and Layout Changes

New Fields, Objects, and Layouts
The Add Picklist Values button was added to the Upgrade tab.
The Source (Object) and Source (Field) elds have been added to the Stripe Metadata Mapping default layout.


General Updates
The component logos and labels in the Lightning App Builder have been updated to include the new Blackthorn logo and labeling convention.
The objects/tabs in Blackthorn's apps have been updated so a unique icon represents each app.
A Refer A Friend button has been added to the following admin pages/wizards.

Blackthorn | Payments Admin tab
Blackthorn | Events Admin tab
Blackthorn | Donations Admin tab
Blackthorn | Compliance Admin tab
Blackthorn | Payments Setup Wizard tabThe respective admin can click the Refer A Friend button to share a friend's name and email address with Blackthorn.
We’ve added a new Apex class to avoid a common cause of confusion around Event authorization in a newly refreshed partial or full sandbox. This class will reset the authorization components in the newly refreshed sandbox so users are aware that authorization has not yet been completed. Users will need to add
the BTEventsPostSandboxRefreshapex class to the sandbox refresh process for this reset capability.

Permissions associated with the Blackthorn | Events (Admin) Permission Set’s Object Settings have been API enabled and updated to include:
Accounts: Read/View
Contacts: Read/View
Products: Read
A new user’s license will automatically be applied when the license is authenticated through OAuth during the installation of Payments and Events. This step will streamline the installation process.

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


November 2021 - Version 5.41

We've expanded our Support Community!
We just rolled out two great features in our Support Community to help take the stress out of success!


Salesforce Knowledge: Visit our Support Community and search our Knowledge articles for helpful troubleshooting tips, FAQs, and current issues before opening a case.
Known Issues: We pulled data directly from our engineering tools to create a current list of Known Issues. Use our Knowledge articles to learn more and subscribe to an issue to track its progress without opening a case.


Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application from the AppExchange.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
1. Review the Bug Fixes.
2. Install Version 5.41 of Blackthorn Payments here.
Production Install Link
Sandbox Install Link


3. Navigate to Blackthorn | Payments Setup W izard, click the PayLink tab, and install the latest PayLink package.


Enhancements
Blackthorn's previous logo and watermark has been removed from PayLink and DocumentLink.
The optimization of existing functionality with our Mobile Payments app for Android will allow the user to successfully process manually entered card, ACH, and card reader transactions.

Stripe Billing


Changing the Price on the Subscription / Subscription Item is no longer possible as the change isn't accepted/re ected in the Stripe Billing Dashboard. If you try to change a Price on the Subscription / Subscription Item, you will receive this error message. "Price cannot be updated for a Subscription Item. Please delete this Subscription Item and add a

new Subscription Item to update the Subscription." For speci c instructions, please click here.
There are several important updates to the Stripe Billing app.
On the Blackthorn | Payments Admin page, the Deploy Stripe Billing , Assign Stripe Invoice Record Type , and Assign Subscription Record Type buttons have been combined to create a new Deploy Stripe Billing button.
The DocumentLink Template, Payment Methods, and Company Info tabs have been removed.
On all Stripe Billing objects, the buttons in the top right corner have been updated to Edit , Push To Stripe , Delete , and Clone .


"Stripe Invoice" is now the default Sales Document record Type for all Standard Users.
The following tabs have been relabeled.
Coupons —> Stripe Coupons
Prices —> Stripe Prices
Gateway Orders —> Stripe Gateway Orders
A new eld, Enable Payment Methods , has been added on the Subscription object. The following Values in the multi-select picklist are now available for the user to select.

ACH Credit (pushed by them)
ACH Debit (pulled by you)
Canadian pre-authorized debit
BECS Direct Debit
Bacs Direct Debit
Bancontact
Boleto
Card
EPS
FPX
giropay
iDEAL
Przelewy24
SEPA Direct Debit
SOFORT
Wechat Pay


Bug Fixes
When a generated Transaction fails and the Payment Schedule's Recurrence Method is set to "Keep One Open", two transactions will be created — one for a reattempt Transaction that has a due date set according to your Reattempt Settings and one with a due date set for the next billing frequency.

Stripe Billing


The Description     eld of a Transfer Transaction will no longer be incorrectly cleared by the processing of a related Webhook Event.

If a Transaction in Stripe fails, the Charge.failed webhook will process as expected and create the failed Transaction rather than causing the webhook to fail with the "Unable to nd Payment Gateway with ID = null" error.
When Transactions fail for Stripe customers using the Transaction Reattempt feature, a duplicate reattempt Transaction will no longer be generated when Charge.Failed webhooks process.


Compliance
Users will see the following updated names for Blackthorn Compliance
Blackthorn Compliance (previously PCIFY)
SecureAttachment for Blackthorn Compliance (previously SecureAttachment for PCIFY)
Blackthorn Compliance-Email2Case (previously PCIFY-Email2Case)
Blackthorn Compliance-Chatter (previously PCIFY-Chatter)
Blackthorn Compliance-Chat (previously PCIFY-Chat)


Donations

Donations Package Installation

If you are installing the Donations package for the rst time, you will automatically see the eld donation360Picklist_Valuesc on the Form Question page layout.

If you have previously installed the Donations package and are upgrading it, you will need to manually update the page layouts to remove donation360Picklist_Values_Longc and add donation360Picklist_Valuesc.


If you have any questions about this or need help with testing, please don't hesitate to reach out to us through our support form.


October 2021 - Version 5.34
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
1. Review the Bug Fixes.
2. Install Version 5.41 of Blackthorn Payments here.
Production Install Link
Sandbox Install Link


3. Navigate to Blackthorn | Payments Setup Wizard, click the PayLink tab, and install the latest PayLink package.


Bug Fixes
The Source     eld of a refund transaction will now be set on record creation. For example, if the refund Transaction is created from a webhook event, the Source will specify “Webhook.” Or if the refund is processed from Salesforce, the Source      eld will specify “Salesforce UI.”

After changing the Default Source on a Payment Gateway Customer to a different Payment Method, the Default Payment Method checkbox that Payment Method will be checked automatically. All Transactions with Transaction Status = 'Open' related to the Payment Gateway Customer will automatically be updated with the new Payment

Method. The remaining payment methods’ Default Payment Method checkbox should be empty.
When processing a Transaction using PayLink, a checkbox to accept Terms and Conditions is now available for both ACH and Credit Card Payment Method types.

Stripe Billing

When adding a One-Time Price to a Subscription Line on an existing Subscription record, the addition will sync to Stripe as Invoice Items without error and will be Invoiced on the next Subscription generated Invoice.
Webhook Events related to Subscription Schedules will now process without throwing a null pointer exception error.
For customers using SCA and Payment Intents, Payment Intent records created from Webhook Events will be automatically related to the associated Transactions in Salesforce.
When using an ACH Payment Method with DocumentLink on a Stripe account that has had the micro-deposit requirement waived, users will no longer see the noti cation about micro-deposits.
After deleting a Subscription line item that had previously been pushed to Stripe, the line item will now also be deleted in Stripe. Additionally, future webhooks will not re-create the line item in Salesforce.
After registering an attendee for an event and completing the checkout process, the attendee will now receive an email/receipt from Stripe if Stripe receipts are enabled. To ensure that this occurs, the Email     eld must be populated on the Payment Gateway Customer record and associated to the Transaction and Payment Method.

The one-time lines on the Subscription invoice in Stripe will now re ect the Quantity that was entered on the Subscription Item in Salesforce. Previously, the quantity was set to 1 in Stripe, regardless of the Quantity set on the Subscription Item in Salesforce.

The Subscription lookup eld on the Subscription Schedule record will now populate correctly after a subscription schedule in Stripe is created or updated and the webhook is processed.

When making a payment with 6+ digits in Euros and a European Stripe account, Stripe Checkout will now process the transaction correctly.

Authorize.net

Transaction Rollup elds on Parent records will now calculate properly for Transactions processed through Authorize.net with ACH Payment Methods.
The intermittent issue causing payments to sometimes process more than once when using the Virtual Terminal with an Authorize.net gateway has been resolved.
Updates have been made to the PaymentChargeFlow Component when it used with Authorize.net in the following scenarios.
Users will no longer receive a 'Before Insert or Upsert list must not have two identically equal elements' error.
When entering the exact Card Holder Name and Email Address of an existing Authorize.net customer, users will no longer receive a Customer Pro le duplicate error.
When using the exact Payment Method previously entered by a returning customer, users will not longer receive a Payment Pro le duplicate error.

Spreedly


We're now passing the account type of Checking or Savings to Spreedly when processing Transactions with an ACH Payment Method. The error, “An unexpected error occurred," should no longer occur.


Donations
Enhancements


The Donations app and the Events app use the object name, “Form Submission.” To alleviate confusion, the object name in Donations has been changed to “Blackthorn Donations Form Submission,” and the object name in Events has been changed to “Blackthorn Events Form Submission.”

Bug Fixes

The Form Question page layout has been updated to remove the deprecated 'donation360_Picklist_Values_Longc' eld and add the correct 'donation360_Picklist_Valuesc' eld.


Donations Package Installation

If you are installing the Donations package for the rst time, you will automatically see the eld donation360Picklist_Valuesc on the Form Question page layout.

If you have previously installed the Donations package and are upgrading it, you will need to manually update the page layouts to remove donation360Picklist_Values_Longc and add donation360Picklist_Valuesc.


Previously, if the Payment Date    eld on a Nonpro t Success Pack (NPSP) Payment record was updated, Blackthorn's automation would update the transaction's Processed Date to the wrong date/time. The Processed Date on a Transaction will now be set to the exact date/time of the Payment Date listed on the Payment record.

Rather than giving the user an error, clicking on the “Getting Started” link on the Donations Setup Wizard page will now take the user to the Donation Form Setup webpage.
Resolved a Donation Form Submission processing error occurring with Recurring Donations. The following actions will occur:
Future Open Transactions will be created.
Campaign Members will be added.
The Recurring Donation will be created.
The Current Transaction will be captured.

If you have any questions about this or need help with testing, please don't hesitate to reach out to Blackthorn Support.


September 2021 - Version 5.33
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
1. Review the Bug Fixes.
2. Install Version 5.33 of Blackthorn Payments here.


Production Install Link
Sandbox Install Link


3. Navigate to Blackthorn | Payments Setup W izard, click the PayLink tab, and install the latest PayLink package.


Bug Fixes
Resolved: The Clear button on the Virtual Terminal has been removed from all screens. This was determined to be an unnecessary feature.

Resolved: Transaction reattempts were not being processed properly for Authorize.net Transactions. The reattempt logic has been updated to add support for Authorize.net Payment Gateways.
Resolved: The Payment Charge Flow component was throwing a component error when being used by customers to execute charging a Transaction. We've removed the reference to customerId to prevent this error from being displayed in the future.

Resolved: The Sales Document (Invoice)       eld on a refund Transaction created from a Webhook Event was not displaying the proper value. We made an update to ensure users see the related Sales Document information displayed on the Transaction record regardless of how the Transaction was refunded.

Resolved: Added the ability for the Mobile App Version     eld to be populated when charging Authorize.net Card and ACH payments through the mobile app.
Resolved: When Lead records were automatically created using Relationship Settings, one word Name values were appearing with the pre x of null . We've adjusted the code that creates the Lead record to consider one word values and remove the word null as text in the Company           eld.


Stripe Billing

Resolved: When creating a Stripe Invoice using the Create Invoice button on Opportunity, the related Line Items did not re ect a "Stripe Line Item" Record Type. Users will now notice Stripe Invoices contain Stripe Line Items.

Resolved: Customers with more than 10 items on a Stripe Invoice noticed that the Sales Document created in Salesforce only displayed a maximum of 10 of the Line Items. We've updated our logic so that when Stripe Invoices are being synced either by webhooks or Historical Sync, all Line Items will be displayed on the Sales Document in Salesforce.
Resolved: We cleaned up some of our error messaging for Stripe Billing. Unnecessary characters were being displayed, and they have been removed.


August 2021 - Version 5.31
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that has been postponed inde nitely. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
1. Review the Bug Fixes.
2. Install version 5.31 of Blackthorn Payments here.


Production Install Link
Sandbox Install Link


3. Navigate to Blackthorn | Payments Setup W izard, click the PayLink tab, and install the latest PayLink package.


Bug Fixes
Resolved: Users were noticing that the Transaction work ow email receipts were not sending with Authorize.net as the Provider on Payment Gateway. The work ow rule criteria has been updated to better evaluate Billing Email on Transactions.
Resolved: Disputed ACH Transactions were resulting in webhook event errors. We've updated our dispute logic to prevent the webhook error and allow for the Dispute record to be created and Transactions to get subsequently updated.
Resolved: The “New Payment Method” Action was unable to load while being viewed on a Salesforce Community page. This was due to a CSP violation. We've added payments.blackthorn.io to the CSP Trusted Sites in Setup as a packaged item.

Resolved: A Customer reported hitting a CPU timeout when trying to create a Sales Document from the Opportunity using the Create Invoice button. We found that when you have multiple Opportunity Products with the same Product, Quantity, and Amount that our Create Invoice button on Opportunity starts to loop when creating Line Items
and eventually times out. Our logic has been updated to prevent the looping behavior.
Resolved: Transaction rollups were not being properly calculated after ACH Transactions were processed. We reordered the processing sequence so the rollups trigger would re at the right time when webhooks are being used.NOTE: Make sure you do not have the Disable Trans Rollup To Parent custom setting enabled.
Resolved: Some users were reporting seeing errors while processing authorize.net Transactions through Paylink. We've updated our API request to add additional detail to prevent a duplicate error from appearing in the future.
Resolved: Some Payment Methods were being duplicated and causing errors after being created from the Virtual Terminal. We updated our logic to prevent this from happening in the future.

Stripe Billing


Resolved: Using the Sync with Stripe button on Payment Gateway was not pulling in Stripe Invoices. We've updated our historical sync service to prevent this from happening in the future.
Resolved: Using the Sync with Stripe button on Payment Gateway was not pulling in Canceled Subscription data. We've updated our query logic to pass in all statuses.

Resolved: Users were unable to set the Account Balance to "0" in Salesforce on the Payment Gateway Customer record and see the update in Stripe. We've added logic to check for custom balances even if they equal 0 to ensure the "0" value can be sent to Stripe.

Resolved: When modifying the Account lookup on an active Subscription the Active Subscription Names           eld on Account was not being properly updated. We've updated our trigger to re when the Account lookup on Subscription is changed so the records will stay in sync.

Field Service Lightning


Resolved: Refund Transactions were created, but not associated to Work Orders. We've made updates so Refund Transactions created via webhooks will automatically relate to the Work Order and trigger the balance rollups.


In order to see the update from the issue above you will need to update your org to ensure the latest version of our FSL Extension package is installed, as well as, a version of Payments 5.31 or greater.

Blackthorn FSL Extension Package Version 1.57 Installation Link: https://login.salesforce.com/packaging/installPackage.apexp?p0=04t4P000002qnJw


July 2021 - Version 5.29
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that will be enforced in Winter '22. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
1. Review the Bug Fixes and Enhancements.
2. Install version 5.29 of Blackthorn Payments here.


Production Install Link
Sandbox Install Link


3. Navigate to Blackthorn | Payments Setup W izard, click the PayLink tab, and install the latest PayLink package.


Enhancements
Added Paylink v1.21 to Blackthorn | Payments Setup Wizard.
Enabled Coupons, Subscriptions, Subscription Items, and Stripe Invoices to be used with Batch Apex Callouts to Stripe. This is in addition to the other Stripe Billing objects that were previously enabled to be used in this way.


Bug Fixes
Resolved: Contact and Account records created from Relationship Settings matching were not always retaining full name values. This happened when a customer added 3 text values to the Name             eld on a Payment Gateway Customer record. We've updated logic to consider scenarios where 3 text values are added. This includes when a customer is
using Middle Names .

Resolved: Some customers were running into errors when querying the Payment Gateway object while trying to use our API for a checkout process on their site. We've added additional read permissions for Site Guest User pro le so they can access the proper token elds.
Resolved: When adding a path to a Salesforce community URL users noticed that they were not getting redirected properly after using the visualforce version of Virtual Terminal. We've made an update so now we are reading the existing URL and redirect the user using that URL when the visualforce component is used. The Aura component version of
Virtual Terminal already had the capability of reading the URL path and redirecting the user correctly.
Resolved: Users who added the aura version of Virtual Terminal to a community page noticed that elds like Related To and Parent Object where not getting populated. We've added a design attribute to this component so those values can be displayed.
Resolved: The Add Picklist Values button on the Payments Admin page was not always triggering updates. This has been xed.

Resolved: When using Virtual Terminal and an Authorize.net Payment Gateway users noticed missing Payment Method data. After webhooks processed the Account lookup on the Payment Method record was being removed. We updated the logic to not overwrite the eld with the blank values.

Resolved: DocumentLink invoices were not re ecting the date format from the browser's locale. The locale detection code has been updated to prevent this from occurring in the future.
Resolved: When using Stripe Checkout in conjunction with CNY currencies and Alipay an error was being displayed in Paylink and on the Transaction record. We've added CNY as a Currency value on the Payment Intent object to allow for successful Transaction processing.

Resolved: When clicking the Remove From Gateway button on a Payment Method record the action was not being re ected in the corresponding gateway. We've updated the Payment Gateway logic on the visualforce page to allow users without the System Administrator pro le proper accessibility.
Resolved Updated the PAY button behavior for DocumentLink so the experience is similar no matter what payment provider is being used.

Resolved: The Default Relationship Settings record was not being created with fresh installs of Blackthorn Payments. The record is now appearing.
Resolved When adding ACH Payment Methods using Virtual Terminal in conjunction with Webhooks con gured, users noticed that the Payment Method Status was being updated to "One-Time". We have resolved this webhook behavior so that the Payment Method Status will not update to "One-Time" and the Record Type will remain "ACH".

Stripe Billing


Resolved: When updating a Price on a Subscription in Stripe the record in Salesforce wasn't re ecting the change in all the necessary locations. Users will now notice that the Price      eld is updated on the Subscription record if the Price has been updated in Stripe.
Resolved: Inbound webhooks and historical sync records were not creating Price or Invoice related records when a Price from Stripe included more than 2 numbers after the decimal. We've added another eld in Salesforce on the Stripe object and labeled it Full Amount . This way we can write values to that eld that include up to 12 decimal places.

Resolved: Blackthorn Logs were being generated when Subscription Schedule records were being pushed to Stripe. We've updated the Sales Document logic related to Subscription creation to address this.

Donations


Added support for the Middle Name       eld on Contact. When users have enabled the Middle Name user interface setting in setup they will notice that Middle Name can be added to a Contact record. Subsequently, when users added names to the Donation form that includes three space separated values, they'll see all three values on the Contact record.


Updates to Custom Settings & Fields
Full Amount has been added to the Price object


June 2021 - Version 5.24
Once the below updates have been reviewed, please follow the upgrade instructions to upgrade your payments application from the AppExchange.


Important upgrade note for all

Starting with this June 2021 release, we will require all customers to be no more than 3 versions behind the latest version. We'll start reaching out to customers this month that are more than 3 versions behind


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that will be enforced in Winter '22. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
1. Review the Bug Fixes and Enhancements.
2. Install version 5.24 of Blackthorn Payments here.
Production Install Link
Sandbox Install Link


3. Navigate to Blackthorn | Payments Setup W izard, click the PayLink tab, and install the latest PayLink package.


Features
Stripe Checkout for Paylink. Users are now able to con gure their orgs to use Stripe Checkout. This is a Stripe-hosted payment page.


Bug Fixes
Resolved: Users were experiencing errors when attempting to connect their Spreedly Payment Gateway to Paypal. We've updated the Spreedly API request to now set the auth_mode to prevent this error from occurring.
Resolved: We noticed that sometimes when using the Sync with Stripe button on a Payment Gateway that Blackthorn Log records were being generated even when records were successfully generated. We've made some updates so users will not see those arbitrary log records.

Resolved: When using the Refund button on a Transaction the amount to be refunded was not displaying the proper amount each time. We've made an update to re ect the amount that can be refunded rather than the original Transaction amount.

Resolved: Removed unsupported elds from the DocumentLink Template object. This should prevent confusion when users nd elds that are not seeming to function as they are labeled.
Resolved: When a Connected Account record was updated to subsequently no longer qualify for a "Veri ed" Verification Status no errors were being presented on the record. We made an update to our webhook logic to look for errors and add them to the Connected Account record.

Resolved: Users reported that previously the objects Sales Document and Opportunity were precon gured as transaction parents during Payments Setup Wizard steps. Since this was no longer happening in the last few packages we added back this con guration.
Resolved: When logging in as a Platform License User a Blackthorn Log record was being generated after adding a Line Item to a Sales Document record. Additionally, the rollups to display certain balance elds were not being executed. An additional check to see if the current user has access to the Product and Pricebook objects has been added to
prevent this behavior from occurring.

Donations


Resolved: Google Analytics tracking was not working on certain donation forms. We've added cookieFlags: 'SameSite=None; Secure', when creating Google Analytics trackers to minimize this from occurring.
Resolved: When unchecking the checkbox for the Require CVV     eld on our Donations Form the resulting form still required the user to populate CVV. We've updated our logic so the form will respect this con guration.


NOTE: The CVV update for Donations will go live June 15th


Con guration Check

Double check your Donation Form records to ensure that you have either enabled or disabled the checkbox for Require CVV per your business needs.


Updates to Custom Settings & Fields
Removed the following elds from the DocumentLink Template object:
Background color

Button color

Card color theme

Logo

Due Date label

Requested by label

Amount due label

Documentation


May 2021 - Version 5.22
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Important upgrade note for all

Starting with this June 2021 release, we will require all customers to be no more than 3 versions behind the latest version. We'll start reaching out to customers this month that are more than 3 versions behind


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that will be enforced in Winter '22. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
1. Review the Bug Fixes and Enhancements.
2. Install version 5.22 of Blackthorn Payments from the appExchange here

Direct Links:

- Production Install Link
- Sandbox Install Link


3. Navigate to Blackthorn | Payments Setup W izard, click the PayLink tab, and install the latest PayLink package.


Enhancements
Stripe Billing: Added support for the value "Send Invoice" on the picklist Proration Behavior on the Subscription object.
As we continue to build out more exibility with the Virtual Terminal we've added another Custom Setting. This setting labeled Disable Payment Method Filter will allow users to select any Payment Method they have sharing access to regardless of the record being related to an Account or Contact. Check out all of our Custom Settings for Virtual

Terminal.
Added validation messages for the required elds on the Payment Method form in Virtual Terminal. If users enter incomplete data they will now see an intuitive message.


Bug Fixes
Resolved: Payment Schedules utilizing the "Keep One Open" option were resulting in a Next Payment Date that did not match the date on the next open Transaction record. The logic for Payment Schedules has been updated to re ect the correct Next Payment Date.
Resolved: While using the live Plaid integration, users noticed that the Account/Contact details from the Salesforce Transaction are rendered on the consent screen. When Account/Contact details are attached to a Transaction users can now use the Company Info   eld on the Payment Gateway record to trigger the value displayed on the consent screen.

Checkout out more details on the Plaid page.
Resolved: We updated the error message displayed when a Payment Gateway isn't properly setup and a user attempts to pay with Paylink. Since this is a customer facing message the direction is now informing the user to contact the company where the Transaction originated.
Resolved: Customers noticed that when the Custom Setting Enable SCA was set to TRUE they were having issues using the Sync with Stripe button to sync ACH Payment Methods. Customers should now be able to use the Sync with Stripe button to sync both ACH and Card Payment Methods.
Resolved: We've updated the webhook processing order to stay inline with the Stripe Documentation. This should allows for Transaction records in Stripe to stay synced with those in Salesforce.
Resolved: When creating a new Transaction related to a Payment Gateway Customer with the Payment Gateway lookup blank, the default Payment Gateway is lled in automatically instead of the one set on the Payment Gateway Customer. We've added logic to fetch the Payment Gateway from the related Payment Gateway Customer on the
Transaction.
Resolved: When the default Payment Method was updated for a Payment Gateway Customer, the related open Transactions were not re ecting the change. The Payment Method logic has been modi ed to ensure the default record stays in sync with Payment Gateway Customers and open Transactions.
Resolved: When using a card reader with the Payments mobile app to complete a Transaction the records that appeared in the Stripe dashboard were not syncing the Customer and Payment records. We've updated our logic so the records can be re ected correctly in Stripe.
Resolved: Installation errors when attempting to install Blackthorn Donations in an org with a fresh install of Blackthorn Payments.
Resolved: Users reported encountering errors on Form Submission records when a Contact was already associated with a Campaign related to the Donation Form record. We are now preventing the creation a duplicate record which results in error.

Authorize.net

Resolved: Authorize.net Payment Methods synced in Salesforce through webhooks were producing "XXX" values for Expiration Date . When customers attempted to update the Expiration Date they were receiving errors and noticed records marked as "Invalid". We've updated the values being returned from the API to prevent errors and invalid

Payment Method records.
Resolved: A null pointer error was being displayed on the Webhook Event created when an Authorize.net Transaction was charged via their Virtual Terminal on their portal. We've updated how we process Authorize.net Webhook Events to avoid this error.
Resolved: Authorize.net customers were noticing the value from Description on a Customer Pro le was mapping to Holder's Name on the Payment Method instead of the Name from the Payment Pro le in authorize.net. Now users will notice we are retrieving the Billing Information First Name and Last Name from Authorize.net and writing
those values to Holder's Name on Payment Method and Name on Payment Gateway Customer.

Resolved: Authorize.net customers noticed that when making updates to Payment Gateway Customer records in Salesforce the Customer ID on the Customer Pro le in the Authorize.net portal was being cleared. We've updated the data updates from webhooks to Authorize.net to prevent this from occurring.

Resolved: When webhooks from Authorize.net were being processed in Salesforce the related records(Payment Gateway Customer, Payment Method, and Transaction) were not being related to one another properly and Blackthorn logs were being created. We've updated how these webhooks get processed so the related lookups will be populated
correctly.

Stripe Billing

Resolved: Customers reported receiving errors when attempting to push Subscription records with certain Payment Methods to Stripe. We've added support of Payment Methods created by the Payment Method API to avoid errors while creating Subscription records.


Updates to Custom Settings & Fields


Added: Custom Setting labeled Disable Payment Method Filter to the Blackthorn Payments | Virtual Terminal group.

Added: A value labeled "Send Invoice" to the picklist Proration Behavior on the Subscription object.


April 2021 - Version 5.20
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Breaking Change

If you are currently using the custom setting Terminal Related To Default Object from the Blackthorn Pay - Trigger Settings you need to switch to the new custom setting Related To Default Object now located under Blackthorn Payments | Virtual Terminal. The custom setting Terminal Related To Default Object has been removed.


Important upgrade note for all

Starting with the June 2021 release, we will require all customers to be no more than 3 versions behind the latest version. We'll start reaching out to customers this month that are more than 3 versions behind.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that will be enforced in Summer '21. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
1. Review the Bug Fixes and Enhancements.
2. Install Version 5.41 of Blackthorn Payments here.
Production Install Link
Sandbox Install Link


3. Navigate to Blackthorn | Payments Setup Wizard, click the PayLink tab, and install the latest PayLink package.


Enhancements
We have removed the "terminal" logo and Clear button from the Virtual Terminal. This will allow the component to seamlessly appear on the record page without it looking out of place.

The Virtual Terminal now displays a spinner while loading on the page. This will help users know when the Virtual Terminal component has fully loaded so they don't input data into the wrong eld.
Updated the Payments Setup Wizard Paylink step so that it loads the latest version of Paylink (v1.20).
Removed the Custom Setting labeled Terminal Related To Default Object from Blackthorn Pay - Trigger Settings. This was a cleanup item as this setting has moved to the Custom Setting group labeled Blackthorn Payments | Virtual Terminal.

Added the ability to modify the recordId associated with the Related To       eld on Virtual Terminal. We also added the ability to modify the Parent Object at the same time. This will give customers more exibility when customizing the Virtual Terminal in a ow or in another custom component.
Virtual Terminal will now have the ability to capture success or failure responses from Transactions. We're adding code that can be reused by customers in custom components for this feature. Additionally, we're adding a code mechanism for disabling the success pop up that occurs after capturing a Transaction in Virtual Terminal.
We added additional global variables for the Virtual Terminal that will control which type of Payment Method form in displayed inside custom components. This variable, when used in a custom component, will also have the ability to lter stored Payment Methods by type.
Added an update to our Payments REST API so the Account and Contact IDs can be accepted when working with Authorize.net requests.
For Stripe ACH Payment Methods we have implemented the use of a Stripe ngerprint to uniquely identify ACH Payment Methods.


If you would like to bypass Stripe's ngerprint logic and use our legacy logic for ACH Payment Methods do the following:Navigate to Custom Settings -> Blackthorn Pay - Trigger Settings -> Disable Fingerprint Matching (ACH) set to 'TRUE'.


Bug Fixes
Resolved: When a Payment Method resulting in an "Invalid" Payment Method Status was added from the Virtual Terminal users were seeing a success message. This was because the logic was noting whether or not the Payment Method was saved. We've updated the logic to throw a failure message when a Payment Method is saved, but invalid. This

will be more intuitive for users.
Resolved: The custom setting labeled Hide Parent was hiding the Parent         eld on the Virtual Terminal, but also it was preventing the parent record value from populating on Transactions captured from the Virtual Terminal. The logic has been updated so users will now see the parent ID on Transactions captured from Virtual Terminal regardless of if

the eld was hidden or not.
Resolved: The eld text for Card Expiration on the Paylink form was not intuitive to users and needed to match the UI for Virtual Terminal. This eld has been modi ed so instead of saying Card Expiry it now says Card Expiration .

Resolved: Users noticed that when creating a graduated Price in Stripe with a large unit value ( 999,999,999,999,999 ) a BT Log with an exception was created and the Price was not being synced in Salesforce properly. We have updated our logic to allow for the larger value to prevent this exception. Users will now be able to create Prices in Stripe within
Stripe's value limits and sync with Salesforce.
Resolved: When the Custom Setting Disable Trans Rollup Parent was set to "True" there were instances of the Transaction rollup logic still being triggered. We've made an update so whether the scheduled batch TransactionRollupToParentService runs automatically or whether the user manually triggers TransactionRollupToParentService the

logic will not be executed if the Custom Setting is checked.
Resolved: The proration behavior logic for Subscription Schedules was not matching the behavior users came to expect after using prorations with Subscriptions. The logic has been updated so Backdate Start Date values on Subscription Schedules entered from Salesforce should sync with Stripe. This will allow Subscription invoices to be created

appropriately.
Resolved: Blackthorn Log records were being generated when Transactions were being updated from Stripe. We've added logic to prevent the null pointer error that was being presented in the Blackthorn Log.
Resolved - When creating Subscription Schedules there were instances where duplicate Subscription records were being created after the webhook processed. We updated the logic to add the Subscription ID to the active Subscription Schedule Phase to prevent a duplicate Subscription record from being created.
Resolved - Government Cloud orgs were reporting that they were seeing errors when attempting to use the Payments Setup Wizard. Users will now be able to navigate through the wizard without errors. Additionally, they will notice that the Relationship step now adds a record to the Transaction Parent Custom Setting as expected.


Updates to Custom Settings & Fields
Added a Custom Setting labeled Disable Fingerprint Matching (ACH) - This custom setting can be found under Blackthorn Pay - Trigger Settings. When enabled Stripe ACH Payment Methods will bypass the ngerprint logic that Stripe has implemented and use a custom matching logic we developed before Stripe ngerprints were implemented.


March 2021 - Version 5.17
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Breaking Change

Be aware that the following Custom Settings have been deprecated as of this release: Terminal Disable New Charge, Terminal Default New Payment Method, and Terminal Disable New Payment Method. If you are already utilizing these settings be sure to uncheck them in your org and use Disable New Charge, Default New Payment Method, and Disable New
Payment Method instead.


Important upgrade note for all

Starting with the June 2021 release, we will require all customers to be no more than 3 versions behind the latest version. We'll start reaching out to customers in April that are more than 3 versions behind.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that will be enforced in Summer '21. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
1. Review the Bug Fixes and Enhancements.
2. Install version 5.17 of Blackthorn Payments here:
Production Install Link
Sandbox Install Link


3. Navigate to Blackthorn | Payments Setup W izard, click the PayLink tab, and install the latest PayLink package.


Enhancements
Updated the Field Label and Help Text included on the Blackthorn Payments | Virtual Terminal Custom Setting for Disable Amount to re ect the updates to that functionality. The ability to disable the Amount             eld on the Virtual Terminal is now something that users can enable for a Virtual Terminal that lives in a Salesforce Community or in the
Salesforce Org they are using.
We've added another Custom Setting to Blackthorn Payments | Virtual Terminal. The setting is labeled Disable Payment Gateway . When this setting is enabled the user will notice that the Payment Gateway eld on the Virtual Terminal is read only.Note: The Payment Gateway          eld on the Virtual Terminal is only visible in orgs with multiple Payment
Gateways.
In an effort to consolidate all of the Virtual Terminal Custom Settings into one place, we moved Terminal Related To Default Object to Blackthorn Payments | Virtual Terminal. This setting was previously in the Custom Setting labeled Blackthorn Pay - Trigger Settings. Additionally, we renamed this setting. It is now labeled Related To Default

Object .


Bug Fixes
Resolved: We noticed the success message that's visible when creating a Subscription from an Opportunity needed an update. This message has been modi ed to accurately re ect the action taking place.
Resolved - If a customer ever had multiple Payment Gateways for the same provider we noticed the Virtual Terminal might not recognize the difference. Let's say upi are trying to use the Virtual Terminal to save a SCA Payment Method for Stripe. You can now do that even if another non-SCA Stripe Payment Gateway in your org is set as a default.
Resolved - When using the Virtual Terminal Custom Setting for Transaction Success Message the success message was still visible even when a Transaction failed. Now you will only see the failure message when a Transaction fails.
Resolved - When enabling the Custom Setting Hide Related To the eld Payment Method was also hiding. You'll now notice that when this setting is enabled only the Related To                 eld is hidden.

Resolved - There were instances where the Sales Document wasn't re ecting the applied credit from Stripe in the Amount Paid         eld. This caused the Balance Due to remain on the Sales Document equal to the credit. This also left the Payment Status set to 'Partially Paid'. Our logic has been updated to capture these amounts and update the elds

accordingly.
Resolved - When using Paylink to charge a Transaction the Payment Gateway Customer lookup was not being populated.

Resolved - While using Paylink to charge a Stripe ACH Transaction, when the Transaction Status was still pending the Account and Contact lookups were not being properly populated.


Custom Settings/ Custom Labels - Updates
Removed: Terminal Disable New Charge

Removed: Terminal Default New Payment Method
Removed: Terminal Disable New Payment Method

Added: Disable Payment Gateway

Moved: Terminal Related to Default Object
Renamed: Terminal Related To Default Object to Related To Default Object


February 2021 - Version 5.15
Once the updates listed below have been reviewed, please follow the upgrade instructions to upgrade your Payments application.


Important upgrade note for all

Starting with the June 2021 release, we will require all customers to be no more than 3 versions behind the latest version. We'll start reaching out to customers in April that are more than 3 versions behind.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that will be enforced in Summer '21. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
1. Review the Bug Fixes and Enhancements.
2. Install version 5.15 of Blackthorn Payments here:
Production Install Link
Sandbox Install Link


3. Navigate to Blackthorn | Payments Setup W izard, click the PayLink tab, and install the latest PayLink package.


Enhancements
Added the ability to override Virtual Terminal labels using Custom Labels. This will give users more of an opportunity to customize Virtual Terminal for their speci c use case.
Added additional controls in the Custom Setting named Blackthorn Payments | Virtual Terminal . They include the ability to control settings for the elds Related To , Parent Object , and Process Type . You'll also notice you now have the ability to add custom success messages when capturing a Transaction and creating a new Payment Method
from the Virtual Terminal.


Deprecated Settings

Be aware that the following settings are slated to be deprecated: Terminal Disable New Charge , Terminal Default New Payment Method , and Terminal Disable New Payment Method . If you are already utilizing these settings be sure to uncheck them in your org and use Disable New Charge , Default New Payment Method , and Disable New Payment
Method instead.


Bug Fixes
Resolved: Account and Contact updates to related Payment Schedule Transactions were not staying in sync. We updated the logic to ensure that when updates were made to the Account or Contact lookup all related records would re ect the update.
Resolved: Updated the Validation Rule text for default Relationship Settings and Payment Gateways to remove a typo.
Resolved: The text that appeared when cancelling a Payment Schedule was not aligned with the action that was to be performed. The text has been updated to re ect a clear cancellation message.
Resolved: When marking the Default Payment Method checkbox as 'True' on the Virtual Terminal, the new Payment Method record was not being set as default. We've xed this so subsequent Payment Method records will display the default ag with the correct condition.

Resolved: NPSP introduced Enhanced Recurring Donations and enabling this was causing an error with the Form Submission processing in Donations. We've added a x so that the Form Submission record can be processed without error.
Resolved: Users were experiencing errors while attempting to install the FSL extension package. A new package has been created with a dependency on Payments 5.14 or later. Please be sure to check our FSL Extension Package doc when attempting to install.
Resolved - There were occurrences of the expected Work Order logic not happening when the Field Service Lightning Extension package was installed. We have released a new extension package and you'll now notice that Transaction records are being created and the proper elds are getting populated when a Work Order Line Item is created.
Resolved: When 'Enable SCA' was checked in Blackthorn Pay Trigger Settings, the value in the Description         eld on the Transaction was not being sent to Stripe. You'll now notice that when adding a value to that eld from the Transaction object it shows up on the entry in the Stripe dashboard.


New Custom Settings/ Custom Labels
Custom Settings added to Blackthorn Payments | Virtual Terminal:
Hide Parent
Hide Related To
Hide Process Type
Disable Related To
Transaction Success Message
Payment Method Success Message
Custom Labels added:
VT Action
VT Related To
VT Parent Object
VT Payment Method
VT Amount
VT Process Type
VT Currency


January 2021 - Version 5.14

January Payments Webinar

Our January Payments Webinar has been pre-recorded! Register for the on-demand webinar here. Once registered, you will receive an email with a link to watch!


Once the below updates have been reviewed, please follow the upgrade instructions to upgrade your payments application from the AppExchange.


Salesforce Release Update Known Issue

Enable Secure Static Resources for Lightning Components is a Salesforce Release Update that will be enforced in Summer '21. Test Run on this Release Update should remain disabled in order to use our Virtual Terminal components. This is due to a Salesforce Known Issue.


Upgrade Instructions
1. Review the Bug Fixes.
2. Install Version 5.14 of Blackthorn Payments


Sandbox Install Link
Production Install Link


3. Navigate to Blackthorn | Payments Setup W izard, click the PayLink tab, and install the latest PayLink package.


NEW! Stripe Billing Plug-in

Stripe Billing Screen Flow for Opportunities
We've created an unmanaged package containing a screen ow template that our Stripe Billing customers can use further streamline creating Subscriptions from Opportunities! Click here for more details!


Bug Fixes
Resolved: When using the +Add New payment method option via the New Single Charge Action picklist on the Virtual Terminal, the newly created Payment Method was not being populated in the Payment Method                eld. This has been corrected so the user will be able to capture a charge after adding a valid Payment Method.

Resolved: The "Authorize Now" option from the Process Type picklist on the Virtual Terminal was fully capturing Transactions rather than just authorizing them. Users will now notice the Virtual Terminal is authorizing Transactions as expected.
Resolved: Updated the Blackthorn | Payments (Admin) permission set to include Modify All and View All permissions for the core payments objects. This ensures users who do not have the standard 'Modify All Data' permission on their pro le, but has our Payments (Admin) permission set have full access to all records of our objects.
Resolved: Blackthorn Logs were being generated when creating Payment Schedule records. The null pointer reference has been removed so that this no longer occurs. This did not visibly or functionally affect Payment Schedules in prior versions, despite the generation of a Blackthorn Log.
Resolved: Updated the Card Expiry label in the Virtual Terminal to now read as Card Expiration . This update will clarify the eld label for users.

Resolved: The Hint and Label       elds for Form Questions on the Donations form were truncating values and wrapping text in an unsightly way. The text for those 2 elds in now appropriately visible.

Resolved: Added Paylink front end support for the elds Amount Due , Due Date , and Requested By on the Paylink Con guration. If a user adds a value to those elds you will now see the value re ected on the Paylink window.


Bug Fixes for Spreedly
Resolved: Added failure message pop-ups for adding Spreedly Payment Methods in the Virtual Terminal. Previously, the Virtual Terminal was either freezing or displaying a component error.
Resolved: When Spreedly was marked as the default Payment Gateway the form to enter payment details was not being displayed with the New Payment Method button. Users with a default Spreedly Payment Gateway will be able to use the New Payment Method button to add Payment Method records.

Resolved: Success and failure message windows were not being displayed when using the "New Single Charge" Action picklist on the Virtual Terminal. The user will now notice a success or failure message instead of an error when adding a new Payment Method via this option.


