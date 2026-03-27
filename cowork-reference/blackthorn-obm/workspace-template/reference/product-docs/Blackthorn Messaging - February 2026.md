# Blackthorn Messaging - February 2026

Table of contents
Blackthorn Messaging

Welcome to Blackthorn Messaging!
Con gure Bulk Messaging


## Installation


Pre-Installation Requirements
Streaming API Access
Install from Salesforce AppExchange
Post-Installation Steps


Blackthorn Messaging

Create a Template


## Account Setup


Account Setup Overview


### Activate Account


EMEA - Account Registration (Production)
Account Registration (Production)
Account Registration (Sandbox)


## Account Setup


Phone Number Setup
Account Activation
Authenticate a User
Con gure Settings


## Individual Messaging


Individual Messaging
Con gure Leads
Con gure Contacts
Con gure Accounts
Con gure Opportunities
Con gure Cases
Con gure Custom Objects
Inbound Messages


Inbound Image Messages (MMS)
Blackthorn Messaging Inbox


## Conversation Maintenance


Conversation Maintenance
Real-Time Conversation Updates
Conversations
Mass Close Conversations
Accept and Transfer Conversations
Merge Conversations
Conversation Ownership Routing


## Phone Number Lookups


Phone Number Lookups
Admin Page
Reports and Object Model
Enable Phone Number Lookup Automations
Run a Batch Process to Lookup Your Existing Phone Numbers
Lookups with Bulk Messages
Lookups and Individual Messages


## Campaigns


Campaigns
Campaign Response Rules
Con gure Campaigns
Send a Bulk Message from a Campaign


## Automation


Automation
Use the Process Builder to Send an Automated Text Message
Use Flow to Automate Outbound Text Messages
Messaging Send Message Flow
Migrate Work ow Rules to Flow


## Additional Features


Additional Features
A2P Form in Admin Page
After Hours Response
Auto Recharge your Message Balance
Click to Call with CTI


Con gure Default and Excluded Phone Fields by Object
Filter your Inbox Using Conversation List Views
HELP and STOP Message Compliance
How Do I Increase our Message Balance?
Improved File Management for MMS Attachments
Link Tracking
Manage Opt-outs
Number of Conversations in the Messenger
Number of Conversations to Load in Inbox
Prohibit Sending Attachments (Custom Permission)
Schedule Jobs for Admin
Schedule SMS Messages
Set a Default from Number
Short Codes
Smart Scheduler
Sticky Sidebar in the Inbox
Track Phone Number Opt-ins


### Setup


Upgrade the Messaging App
Upgrade the Blackthorn Base, Payments, and Events Apps
Assign New Permission Sets
Create an Org-wide Email Address
Update Permission Sets for the Messaging App


#### Con gure the Smart Scheduler Component


Start Here
Register Your Account
Authenticate a User
Add the BT Event Scheduler Component to the Event Record
Activate the Smart Scheduler's Feature Toggle


#### Troubleshooting


Messaging App Is Not Installed
Messaging App Is Not Con gured
Custom Object Is Not Con gured for Sending SMS


#### Scheduled Jobs from the Event Record


Scheduled Jobs from the Event Record
Schedule an Email
Schedule an SMS

Manage Scheduled Jobs
Filter the Smart Scheduler List View


#### Scheduled Jobs from the Global


Scheduler

Scheduled Jobs from the Global Scheduler
Schedule an Email
Schedule an SMS
Manage Scheduled Jobs
Check the Status of Each Sent SMS and Email
Filter the Global Scheduler List View


### Getting Started


Schedule Emails with SendGrid


## Self-Service Tasks


Add User Licenses and Phone Numbers
Upgrade a Trial Plan to a New Plan


## FAQ


General FAQ


### Attachments FAQ


How Do Users Upload Attachments to SMS?
What Types of Files Are Supported for MMS?


## FAQ


Do You Have a List of Published IP Addresses?
How Do I Update my Payment Method?
How Do I Grant Access to Messaging Support?
What Does this Error Message Mean?
What Happens When my Message Balance Reaches Zero?
Why don’t I see any phone numbers when I try to send a message?


## Release Notes


Release Notes
August 2025 - Salesforce Connected Apps Update
March 2025 - Version 3.48
February 2025 - Version 3.47


### 2024


October 2024 - Version 3.46
July 2024 - Version 3.44.3
June 2024 - Version 3.44.1
May 2024 - Version 3.44
April 2024 - Version 3.43.21


#### February 2024


February 2024 - Version 3.43.19
February 2024 - Version 3.43.16


#### January 2024


January 2024 - Version 3.43.14
January 2024 - Version 3.43.13
January 2024 - Version 3.43.12


#### November 2023


November 2023 - Version 3.43.11
November 2023 - Version 3.43.7


### 2023


September 2023 - Version 3.43.2
August 2023 - Version 3.43.1


#### July 2023


July 2023 - Version 3.42.3
July 2023 - Version 3.42.1
July 2023 - Version 3.42


### 2023


June 2023 - Version 3.40
May 2023 - Version 3.39
March 2023 - Version 3.38


#### January 2023


Version 3.36.7
Version 3.36.6
Version 3.36.5


#### December 2022


Version 3.36.4
Version 3.36.3
Version 3.36.2
Version 3.36.1


### 2022


May 2022 - Version 3.36
April 2022 - Version 3.34
January 2022 - Version 3.30


### 2021


October 2021 - Version 3.27
March 2021 - Version 3.18.3


### 2020


November 2020 - Version 3.13
April 2020 - Version 3.5


Welcome to Blackthorn Messaging!
This guide will help you become familiar with the key features of our powerful, business-class text
messaging software. Blackthorn Messaging delivers enterprise-level text messaging capabilities for
your fast-paced teams. It gives you the ability to send and receive text message communication from
directly within Salesforce. It allows you to manage two-way text message conversations with your
prospects and customers with a series of powerful tools such as templates, campaigns, and work ow
automation.


Installation
Account Setup
Individual Messaging
Conversation Maintenance
Con gure Bulk Messaging
Phone Number Lookups
Campaigns
Create a Template
Automation
Additional Features
FAQ
Release Notes


Performance and Scale Testing

Performance and Scale testing must be pre-approved by both Salesforce and Blackthorn. Please
complete the steps below.

1. Follow the guidance provided by Salesforce and seek Salesforce approval.
2. Once you obtain Salesforce approval, submit a case to Blackthorn with your plan and detailed
testing scenarios. You will be able to upload attachments after your ticket has been opened.
3. If approved, Blackthorn will work with you to determine an optimal date and time to run your
tests.

Please read Performance and Scale of Your Experience Cloud Site for additional resources.


Con gure Bulk Messaging

How many messagings can I send at one time?

Blackthorn Messaging limits bulk messages to 200 at a time.


Con gure Accounts
1. Click the Gear icon in the top right corner.
2. Click Setup.
3. Click the Object Manager tab.
4. Search for and click the Account object.
5. Click the List View Button Layout tab.
6. Click Edit.
7. Scroll down to the Custom Buttons section.
8. Add the Send Bulk SMS button to the Selected Buttons column.
9. Click Save.


Con gure Contacts
1. Click the Gear icon in the top right corner.
2. Click Setup.
3. Click the Object Manager tab.
4. Search for and click the Contact object.
5. Click the List View Button Layout tab.
6. Click Edit.
7. Scroll down to the Custom Buttons section.
8. Add the Send Bulk SMS button to the Selected Buttons column.
9. Click Save.


Con gure Leads
1. Click the Gear icon in the top right corner.
2. Click Setup.
3. Click the Object Manager tab.
4. Search for and click the Lead object.


5. Click the List View Button Layout tab.
6. Click Edit.
7. Scroll down to the Custom Buttons section.
8. Add the Send Bulk SMS button to the Selected Buttons column.
9. Click Save.


Con gure Custom Objects
In Blackthorn Messaging, you have the option to set up Custom Objects for bulk messaging. Here are
the steps to be followed.


Add a Custom Checkbox or Boolean Field to a Custom
Object
1. Navigate to the Setup menu.
2. Find the speci c object.
3. Go to Fields and Relationships.
4. Click New.
5. Choose Data T y pe = “Checkbox”.
6. Click Next.
7. Set Field Label = “Do Not SMS”.
8. Enter the API name as Field Name = “Do_Not_SMS__c”.
9. Click Next.
10. Apply the necessary eld-level security.
11. Click Next.
12. Click Save.


Copy the existing Visualforce page markup
1. Go to Setup > Visualforce Pages
2. Click into the page named "SendBulkLead_ltng".
3. Select all of the markup. Copy to the clipboard.


Create the new Visualforce page
1. Go to Setup.
2. In the Quick Find box, enter and click "Visualforce Pages".
3. Click New.
4. Set the Label to "SendBulk[CustomObjectName]". For example, if your custom object is


named Attendee then Label = "SendBulkAttendee".
5. Paste the markup that you copied from the previous step into the page.
6. Make the following changes:
a. On Line 1, change the StandardController to the API Name of your object. This
should end with "__c" for custom objects.
b. On Line 1, change the recordSetVar parameter to the Name of your object. This
should be the object label and would typically not end with "__c".
c. On Line 9, change the "c" in front of SendBulkSMSMessenger to "simplesms".
d. On Line 9, change the sobjectApiName to the API Name of your object.
7. Click Save.
8. Update all relevant pro les or permission sets to include access to the new Visualforce page.


Create the List View Button
1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, search for and click your custom object.
4. Click the Buttons, Links, and Actions tab.
5. Click New Button or Link.
6. Set the following:
Label = "Send Bulk SMS"
The Name eld will automatically update to "Send_Bulk_SMS".
{variable.Field_SF_NewButton_ListButton}} = "True" (checked)
Display Chec k bo x es (f o r Multi-Rec o rd Selec tio n) = "True" (checked)
Co ntent So urc e = "Visualforce Page"
Co ntent = Choose the Visualforce page you just created.
7. Click Save.


Add the List Button to your Object List Views.
1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, search for and click your custom object.
4. Click the Search Layouts tab. for Salesforce Classic.
5. Click Edit next to Default Layout.
6. Move the Send Bulk SMS button from the Available Buttons column to the Selected Buttons
column.
7. Click Save.


Great job! Now you should be able to visit any of your list views for this object (except Recently
Viewed), and you'll see the Send Bulk SMS button!


Pre-Installation Requirements
You will need a Salesforce account to begin. If you aren't a Salesforce customer yet you can sign up for
a free trial here.

If you have a Salesforce account, then you're all set! Blackthorn Messaging is compatible with the
following Salesforce editions: Professional, Enterprise, Unlimited and Performance.


For Professional Edition Users
If you have Professional Edition, you will need to have API access enabled in your org. If you don't
have API access then you can contact your Salesforce account rep to have this feature added.


Browser Compatibility
Messaging has been tested on most major browsers. We are compatible with Chrome, Safari, Firefox,
Microsoft Edge, Internet Explorer 11.


Streaming API Access
Blackthorn Messaging utilizes Salesforce's Streaming API for several features, so it is important to
ensure that your Users have the necessary access. Since these are standard Salesforce objects we
cannot include these permissions in the Messaging package, so you will need to con rm the proper
access after you have installed Messaging.


Who Needs These Permissions?
Every user that will have access to Messaging.


What Permissions Are Required
Read and Edit access on the Streaming Channel object.
Read/Write access to the Streaming Channel record that Messaging creates, which is named
"/u/TexteyRealtimeUpdate".


How Do I Check For These Permissions
Let's start with the Streaming Channel Object permissions.


1. Go to Setup > Users > Pro les.
2. Select the Pro le that you want to check.
3. If you use the Enhanced Pro le layout, select Object Settings. Search for the Streaming
Channels object. Grant Read and Edit Access.
4. Repeat 1-3 for every Pro le that a Messaging user may have.


If you do not use the Enhanced Pro le layout, go to the Pro le and click Edit. Then, scroll down
to the object permissions section and nd Streaming Channels. Ensure the checkboxes for Read
and Edit are checked.


Alternative Solution
An alternative to modifying the Pro les directly would be to create your own custom Permission Set
that simply grants Read and Edit access to the Streaming Channel object. Then, you can assign that
Permission Set to your users as needed.

Next, let's look at the permissions for the Messaging-speci c Streaming Channel record.

When you install Messaging, a Streaming Channel with the name "/u/TexteyRealtimeUpdate" is created.
Your users will need Read/Write access to this record in order to push and receive updates on it.

1. Go to Setup > Sharing Settings.


2. Scroll to "Streaming Channel".


3. If the org-wide access is Public Read/Write, you do not need to take any further action.
4. If the org-wide access is Private or Public Read Only, then you will need to explicitly share
the record with your users. See below (you have to switch to Classic for this):


Check for Error Noti cations
If your users see any errors or alerts that reference the Streaming Channel, then please revisit these
steps to ensure they have the correct permissions.


Install from Salesforce AppExchange
Blackthorn Messaging can be installed from the Blackthorn Candy Shop into your environment with
these simple steps.

1. Go to the Blackthorn Messaging CandyShop listing.
2. Click the Install Blackthorn SMS - Click Here for Details button.
3. Login with the credentials to your Salesforce account.
4. Select Install in Production or Install in Sandbox based on where you want to install the
package.
5. Choose one of the pro les below:
Install for Admins Only: this option will assign the Messaging pro le permissions
to only those users with a System Administrator pro le.
Install for All Users: this option will assign the Messaging pro le permissions to
ALL users in your Salesforce org.
Install for Speci c Pro les: this option will let you choose which pro les to assign
the Messaging pro le permissions.


Recommendation

We generally advise choosing the Install for Speci c Pro les option. This gives you the greatest
level of control over which users will initially have access to Messaging.


6. Accept the remote site named "api.textey.io".
7. Messaging should now begin installing into your Salesforce org. The installation process can
take several minutes and there's a possibility you will see a message that says "it's taking a
long time". Don't worry, you'll receive an email when the installation is complete. So far, so
good!
8. Once installation is complete, navigate to the Messaging App in the drop-down menu located
at the top right-hand corner of Salesforce.
9. Click on the Messaging Administration tab to continue with the setup.


Post-Installation Steps


After the installation is complete you will want to determine which users need access to Blackthorn
Messaging and what functions they need to perform. Messaging includes two primary Permission Sets
that make it easy to add/remove the necessary permissions from a User. This gives you access control
at the User level.

We'll cover the provided Permission Sets and Custom Permissions so that you're familiar with how
they work.


Streaming API Access
You will need to ensure that your Users have access to the Streaming API and Streaming Channel
object. Follow the steps in the Streaming API Access article.


Permission Sets

Blackthorn Messaging Admin User
This permission set applies to users with a Salesforce license. Users have full access to the
Administration page and edit access for all Blackthorn Messaging related objects, elds, and
Visualforce pages.


Please Read

Blackthorn Messaging Admin User is an additive permission set. That means that it must be
added to the Messaging Standard User permission set for users who need to send text
messages and access to the Administration page.


Blackthorn Messaging Admin User - Platform
This permission set applies to users with any license. Users have full access to the Administration page
and edit access to all Blackthorn Messaging related objects, elds, and Visualforce pages.


Blackthorn Messaging Lightning User
This permission set applies to users with a Salesforce license. Users have the ability to switch to
Lightning, when necessary, to utilize Blackthorn Messaging Lightning Component(s). This permission
set isn't required if you have access to Lightning within the User's Pro le or another permission set


Blackthorn Messaging Lightning User - Platform
This permission set allows users to switch to Lightning, when necessary, to utilize Blackthorn
Messaging Lightning Component(s). This permission set isn't required if users have access to Lightning
within the User's Pro le or another permission set


Blackthorn Messaging Standard User
This permission set applies to users with a Salesforce license. Users have access to the Blackthorn
Messaging related objects, elds, and Visualforce pages, as necessary, to utilize Blackthorn Messaging.
Users do not have access to the Administration page.


Blackthorn Messaging Standard User - Community
This permission set applies to community users with any license. Users have access to Blackthorn
Messaging related objects and elds, as necessary, to utilize Blackthorn Messaging. This gives the
community user the ability to use record messenger to send SMS via the Community record detail
page.


Blackthorn Messaging Standard User - Platform
This permission set applies to users with any license. Users have access to Blackthorn Messaging
related objects, elds, and Visualforce pages as well as the Send Messaging SMS and Send Messaging
Bulk SMS custom permissions. Users do not have access to the Administration page.


Custom Permissions

Send Messaging SMS
This permission allows a user to access the Textey Messenger lightning component on page records. If
the user does not have this permission they will not be able to send a text message using the Textey
Messenger lightning component.


Send Messaging Bulk SMS
This permission allows a user to access the Messaging Bulk SMS lightning component which is
accessed either from list views or a Campaign. If the user does not have this permission they will not
be able to send a bulk text message using the Messaging Bulk SMS lightning component.


Messaging Administrator
This permission allows a user to access the Messaging Administration page. The Administration page
provides access to phone number management, con guration settings, and it's also where you can
purchase additional text messages.


Custom Blackthorn Messaging Standard User -
Community
This custom permission set provides limited access to Community users. See Set Up Community User
Permission Set for instructions.


Assign Permission Sets
Now that you understand the different permissions you can go ahead and assign them to your users.
The most common scenario would be to simply assign a Permission Set to your users. For example,
let's say you want to assign the Messaging Standard User Permission Set to everyone who will use
Messaging. Let's look at how to do that:

1. Go to Setup > Users > Permission Sets.
2. Click the Messaging Standard User Permission Set.
3. Click the Manage Assignments button.
4. Click the Add Assignments button.
5. Select the Users who need access.
6. Click the Assign button.

Great! Now all of those users have the necessary permissions to use Messaging.


If any of these people will also need access to the Messaging Administration page you can follow the
steps above, just select Messaging Administration User instead of Messaging Standard User.


Assign Custom Permissions
If you have a scenario where the Permission Sets won't work for you, or if you'd rather control access
at the Pro le level or create your own Permission Set then you can do the following:


Add Custom Permissions to a Pro le
1. Go to Setup > Users > Pro le.
2. Click the speci c Pro le you want to modify.
3. In the Apps section, click on Custom Permissions.
4. Click Edit. You should see the three Messaging custom permissions.
5. Assign the permissions you want.
6. Click Save.


Add Custom Permissions to a Permission Set
1. Go to Setup > Users > Permission Sets.
2. Click the speci c Permission Set you want to modify.
3. In the Apps section, click on Custom Permissions.
4. Click Edit. You should see the three Messaging custom permissions.
5. Assign the permissions you want.
6. Click Save.


Manage Licenses for Blackthorn Messaging Personal
Plan
If you are subscribed to the Messaging Personal Plan then you have a limited number of available
licenses. This means you need to take an additional step to grant each user a Messaging package
license. If you have the Messaging Basic or Messaging Business plan you can ignore the following
steps.

1. Go to Setup > Apps > Installed Packages.
2. Click the Manage Licenses link next to Messaging.
3. Click the Add Users button.
4. Select users from the available users list and Add the license.


Set Up the Community User Permission Set

Setup Steps for Assigning Permission Sets to a
Community User
1. Click the Gear icon in the upper right-hand corner.
2. Click Setup.
3. Type “Permission Sets” in the Quick Find box.
4. Click Permission Sets.
5. Click Clone next to the permission set “Blackthorn Messaging Standard User – Community”.
6. Set the Label to “Custom Blackthorn Messaging Standard User – Community”.

7. Set the API Name to “Custom_Textey_Standard_User_Community”
8. Click Save.
9. Open the permission set that you just created.
10. In the Apps section, click Assigned Apps.
11. Click Edit.
12. Remove the following Enabled Apps.
simplesms.Textey (simplesms__SimpleSMS)
simplesms.Textey (simplesms__Textey_ltng)
13. Click Save.

You can now assign this permission set to Community users.


Create Community Users

Create a New Account

1. Enter “Accounts” in the All Apps menu search.
2. Click Accounts.
3. Click New.
4. Enter an Account Name . (We suggest using “Community Account”, but the Account Name
can be anything.)
5. Click Save.


Create a New Contact

1. Enter “Contacts” in the All Apps menu search.
2. Click Contacts.
3. Click New.
4. Enter a First Name and Last Name .

5. Set Account Name to the Account created in Create a New Account.
6. Enter a phone number in the Phone      eld.


7. Click Save.


Create a New User

1. In the Contact you just created, click the Enable Customer User button. (The button is only
available if your org has Community access enabled.)
2. Enter an Email .

3. Enter a User Name
4. Set License = “Customer Community Login”.

5. Click Save.


Assign a Permission Set

1. Click the Gear icon in the upper right-hand corner.
2. Click Setup.
3. Type “Permission Sets” in the Quick Find box.
4. Click Permission Sets.
5. Click the permission set you created in Setup Steps for Assigning
6. Permission Sets to a Community User.
7. Click Manage Assignments.
8. Click Add Assignment to assign users to the permission set.
9. Add the user you created in Create a User and click Assign.


Share a From Phone Number with Community Users

Add an Account Lookup to the Phone Number Object

1. Click the Gear icon in the upper right-hand corner.
2. Click Setup.
3. Click the Object Manager tab.
4. In the Quick Find box, enter “Phone Number”.
5. Click Phone Number.
6. Click the Fields & Relationships tab.
7. Click New.
8. Select Lookup Relationship .

9. Click Next.
10. Set Related To = “Account”.

11. Click Next.
12. Enter a Field Label and Field Name .

13. Click Next.


14. Click Next.
15. Click Next.
16. Click Save.


Populate the Account in a Phone Number Record

1. Go to the Messaging app.
2. Open the Phone Number Tab that you want to share with a Community user.
3. In the Account    eld, add the Account you created in Create a New Account.

4. Click Save.
NOTE: If you want to make Phone Numbers available to other communities, clone the Phone
Number record and add different Accounts to the Phone Number record.


Your Phone Number sharing journey begins here

1. Go to Setup.
2. In the Quick Find box, search for “Digital Experiences”.
3. Open the Digital Experiences folder and click Settings.
4. Scroll down to the Sharing Sets section.
5. Click New.
6. Set Label = “BT Messaging Phone Number Sharing”.

7. Click into the Sharing Set Name     eld.

8. In the Select Pro les section, select the pro le of the Community users that you want to use
the From Number .

Example: Customer Community Login User and Customer Community Plus Login User
9. In the Select Objects section, add the Phone Number object to the Selected Objects column.
Note: The Phone Number object should be Public Read Only for Default External Access in
OWD.
10. In the Con gure Access section, click Set-up.
a. Set the Account for the user.

b. Set Target Phone Number = “Account__c”.

c. Set Access Level = “Read Only”.
d. Click Update.
11. Click Save.


Create a Template
Blackthorn Messaging provides some great options to create and use templates when sending SMS
messages.


Create an SMS Template

Attachments

Users can attach images (jpeg, png, and gif), PDFs, and vCards to an SMS Template.

However, only one attachment can be sent per SMS Template . If more than one le is
attached, only the last le attached will be sent with the message. For example, an image is
attached rst. A PDF is then attached. Lastly, a vCard is attached. Only the attached vCard will
be sent with the SMS.


1. Go to the SMS Templates tab.
2. Click New.
3. Select a Template Object. Choose from the objects that are in you Salesforce account.


4. Complete the following elds.
SMS T emplate Name
Toggle A c tiv e to on.
In the Insert Field box, select a eld from the related object. The selected eld will
automatically be added to the message Bo dy .
Enter the remaining text for the message Bo dy .
Add work ow rule options if you are using the Template in a work ow Task.
(Work ow rules help automate outbound messages.)


5. Click Save.

You now have an SMS Template.


Send an SMS Template
Complete the following steps to send an SMS Template from an object.

1. Navigate to a record that matches the SMS Template's Objec t type you created.
2. Click Send SMS.
3. Select the SMS Template you just created in the Template dropdown. Choosing the template
populates the message body with the SMS Template’s Bo dy . You’ll also see that eld merge
action has been performed.
4. Update the message body as needed.
5. Click Send Now.


Account Setup Overview

Use the links below to walk through each step of the setup process.


Activate Account (Production)
Activate Account (Sandbox)
Phone Number Setup
Authenticate a User
Con guration Settings


EMEA - Account Registration (Production)
After you've completed the installation steps, it’s time to activate your Blackthorn Messaging account.
When we say "activation," we are referring to a one-time process that will create a Messaging account
and link it to your Salesforce org.


1. Go to the Messaging Administration tab.
2. You will see a dialog that asks if you already have a Messaging account. Click No, I need an
account to indicate that you do not have a Messaging account.


3. This will open the Account Registration dialog box.
a. Set Account Region = “Europe (EU1)”.

b. Review our Terms of Service and Privacy Policy.
c. Click the I have read… checkbox.
d. Click Activate Now.


4. Click Yes, I have an account.


5. Set Account Region = “Europe (EU1)”.
6. Contact Blackthorn Support for the Account Number & API Key.
7. Once you have the Account Number & API Key, enter them in the Account Number and API
Key   elds.
8. Click Save.


Congratulations! Your Messaging account has been created and placed in Trial status.


What is the Trial status?
When your account is initially created, it is placed in "Trial" status. This allows you to provision one
phone number and send/receive fty (50) text messages. You will have access to all the existing
features. After you exhaust the available 50 text messages you can upgrade to a paid plan using the
Upgrade button located on the Messaging Administration page.


Demo Phone Numbers

View the Demo Phone Number


The demo phone number is in the managed Phone Number section. To create a demo phone number,
click the Create Record button. You cannot add Call Forwarding or add more phone numbers to the
list of provided numbers.


Send the First Outbound Message
The recipient must subscribe to the phone number before the user can send the rst outbound
message.


Share Required Information
Customers must share the following information with a recipient before the recipient can subscribe to
the phone number.

RLC


NMC


Bulk


Validation Errors

Send a Single Message
If a user sends a message without the recipient subscribing to the number, then the
user will receive the following error message. “Recipient customer +1XXXXXXXXXX
yet not subscribed to receive demo messages from +1XXXXXXXXXX”


Send Bulk Messages
If a user sends a Bulk SMS message without the recipient subscribing to the
number, the user will see the following error message in each SMS Message
record. “Recipient customer +1XXXXXXXXXX yet not subscribed to receive demo
messages from +1XXXXXXXXXX”


Opted-in Numbers
Users can see which phone numbers have opted-in for the demo number by going
to the Messaging Admin tab and clicking the Phone icon.


Purchase the Demo Number

Users can purchase a new number once they upgrade their trial account to a paid license. At that point,
the following will occur.


The demo number will be removed from the Messaging Admin page.
Recipients will be unsubscribed from the demo number.


Account Registration (Production)
After you've completed the installation steps, it’s time to activate your Blackthorn Messaging account.
When we say "activation," we are referring to a one-time process that will create a Messaging account
and link it to your Salesforce org.


1. Go to the Messaging Administration tab.
2. You will see a dialog that asks if you already have a Messaging account. Click No, I need an
account to indicate that you do not have a Messaging account.


3. This will open the Account Registration dialog box.
a. Set Account Region = “United States (US1)”.

b. Review our Terms of Service and Privacy Policy.
c. Click the I have read… checkbox.

d. Click Activate Now.


4. Click Yes, I have an account.


5. Set Account Region = “United States (US1)”.
6. Contact Blackthorn Support for the Account Number & API Key.
7. Once you have the Account Number & API Key, enter them in the Account Number and API
Key    elds.
8. Click Save. Your account is now registered and activated.


9. To change the credentials, click the Change Credentials button.


10. Update the elds as needed and click Proceed.


Congratulations! Your Messaging account has been created and placed in Trial status.


What is the Trial status?
When your account is initially created, it is placed in "Trial" status. This allows you to provision one
phone number and send/receive fty (50) text messages. You will have access to all the existing
features. After you exhaust the available 50 text messages you can upgrade to a paid plan using the
Upgrade button located on the Messaging Administration page.


Demo Phone Numbers

View the Demo Phone Number

The demo phone number is in the managed Phone Number section. To create a
demo phone number, click the Create Record button. You cannot add Call
Forwarding or add more phone numbers to the list of provided numbers.


Send the First Outbound Message

The recipient must subscribe to the phone number before the user can send the first
outbound message.


Share Required Information


Customers must share the following information with a recipient before the recipient
can subscribe to the phone number.

RLC


NMC


Bulk


Validation Errors

Send a Single Message
If a user sends a message without the recipient subscribing to the number, then the user
will receive the following error message. “Recipient customer 1XXXXXXXXXX yet not
subscribed to receive demo messages from 1XXXXXXXXXX”


Send Bulk Messages
If a user sends a Bulk SMS message without the recipient subscribing to the number, the
user will see the following error message in each SMS Message record. “Recipient customer


1XXXXXXXXXX yet not subscribed to receive demo messages from 1XXXXXXXXXX”


Opted-in Numbers
Users can see which phone numbers have opted-in for the demo number by going to the
Messaging Admin tab and clicking the Phone icon.


Purchase the Demo Number

Users can purchase a new number once they upgrade their trial account to a paid
license. At that point, the following will occur.

The demo number will be removed from the Messaging Admin page.
Recipients will be unsubscribed from the demo number.


Account Registration (Sandbox)
If you have just installed Blackthorn Messaging for the rst time and you are in a Sandbox
environment, then please reach out to Blackthorn Support so we can setup your account.

It is possible to use Messaging in a sandbox environment, it's just that we don't allow the provisioning
of new Messaging accounts from a sandbox.

After we setup your account you'll receive an email with account credentials and instructions on how
to proceed.


Refreshing your Sandbox

Using the production Account and API Key in the refreshed sandbox is not permitted. If a user
tries to open the Messaging Admin tab after the Sandbox is refreshed, they will see the
following error.

"Request is not allowed as account xxxx is con gured with another org."


Phone Number Setup
After your account has been activated you will need to con gure a phone number so you can begin
sending and receiving text messages. The phone number that you setup will be a 10-digit number
(long code) that you choose from a list of available numbers using our search feature.


Add a Phone Number
Follow the steps below to search for a new phone number and instantly provision it to your account.


1. Go to the Blackthorn Messaging Administration tab.
2. Click into the Phone Numbers section.
3. Click the Add Phone Numbers button.
4. At this point you'll have the option to search by area code or by pattern:
Area Code: An area code search is a very simple search where you input an area
code and available phone numbers in that area code are displayed.
Pattern: A pattern search lets you input a speci c number (or letter) pattern and any
phone numbers that match that pattern are displayed.
For example, if you type 5678 you will see a list of phone numbers with
the pattern 5678 located somewhere in the number.
If you need to be more speci c about where in the number the pattern is
located you can use asterisks (*) as a wildcard. For example, if you type
**5678 then you will only see phone numbers where 5678 is located in
the last 4 digits of the phone number.
5. When you nd the phone number you want, click the Select link next to the number. This
will instantly provision the phone number to your account. You're almost ready to send your
rst text.


Additional Types of Phone Numbers
If you have an existing phone number (either landline or VOIP) that you would prefer to enable please
contact Blackthorn Support.

We can also provide toll-free numbers, please contact Blackthorn Support.


Create the Phone Number record


After you provision your phone number it will be displayed on the Messaging Administration page. The
next step is to create a Phone Number custom object record so that this number can be used within
Salesforce. Each phone number that you provision will need to have its own Phone Number record.

1. Go to the Messaging Administration page.
2. Click into the Phone Numbers section.
3. Click the Create Record button located next to your phone number.
4. Give the phone number a Display Name . This should be something descriptive as it will be
displayed in the From Number drop-downs. For example, "Sales", "Support", or "Sally Smith".
5. Set to Active or Inactive . Active means the phone number can be selected, by users
who have access to it, to send outbound messages. Inactive means the number will be
hidden so that users cannot select it to send outbound messages.
6. The Available for Campaign is a special eld that determines whether a phone number

can be used in conjunction with a Salesforce Campaign. Do not enable this if you want to use
this phone number for standard two-way text messaging.
7. Add a Help Message and Stop Message to your record. These elds de ne the auto-

response message that is sent in certain situations. This helps you to be compliant with best
practices.


Con gure Phone Number Access
After you create the Phone Number record you will want to determine who has access to send
outbound text messages from it. This is controlled by the record's visibility. This means that if a User
has Read access to the Phone Number record then they can use it. By default the Phone Number
object's org-wide sharing is set to Private, so only the Record Owner, anyone above the Record Owner
in the Role hierarchy, and anyone who has been explicitly granted sharing access can see the record.

Let's look at how to grant sharing access to the record:

1. Go to the Messaging Administration tab.
2. Click into the Phone Numbers section.
3. Next to your phone number click the record link which should look something like this -
PhoneNumber-0000.
4. Click the Sharing button located on the Phone Number record page.
5. Click the Add button.
6. Add the Users who need access to this Phone Number. Set the Access Level to "Read

Only".
7. Click Save.


Account Activation
The A2P submission process is crucial for businesses and organizations that send automated
messages to users' phone numbers. To enhance this process, we added a new step called Account
Activation that will occur between the Account Registration and Phone Number Setup steps.

The Account Activation step requires users to activate their account before adding phone numbers for
A2P messaging. The goal is to help prevent errors that may occur due to incomplete or inaccurate
account information.


After completing the initial Account Registration, users will see the Account Activation screen. Users
must enter the Contact Information, Business Information and Usage & Content details.


Account Setup Process
Perform the following steps to set up your account.

1. Complete the Account Registration by providing the Account Number and API key provided
by Blackthorn Support.
2. Click the Account Activation tab.
3. Complete the elds in the General Business Information window.
Business Name (required)
Business Address (required)
Industry (required)
Company Website (required)


4. Click Next.
5. Complete the elds in the Business Entity Information window.
Business Entity Type (required)
Business Registration Number (required)
Business Registration Number Type (required)
Company Status (required)


6. Click Next.
7. Complete the elds in the Usage & Content window.
Message Volume
Use Case
Opt In Type
Opt In Proof Url


8. Click Next.
9. Complete the elds in the Contact Information (Primary & Secondary) window.
Primary Contact
First Name
Last Name
Title
Job Position
Email
Phone
Secondary Contact
First Name
Last Name
Title
Job Position
Email
Phone


10. Click Next.
11. Review the information in the Review & Submit window.


12. Click Submit.


After successful completion of all the steps, the Account Activation gets submitted to Twilio.


Phone Number Searching API

Validating A2P Details
Validating A2P details is a crucial step that occurs when sending automated messages to users via
platforms like Twilio. This step includes reviewing and verifying the information provided by the
business or organization who intends to use the A2P messaging services.

Twilio, for example, follows a meticulous validation process before approving the submission. The
validation process typically takes about 2 to 3 weeks. During that time, the submitted information is
carefully examined to ensure compliance with regulations and best practices.


Searching Phone Numbers

During Twilio’s review and approval period, users can search for and use Phone Numbers by utilizing
toll-free phone numbers. This feature ensures that businesses can continue their operations and
prepare for A2P messaging without causing any interruptions.


Authenticate a User

Prerequisite
A user must have the Blackthorn Messaging Admin User permission set before they can be made an
Authenticated User.


What is an Authenticated User?
You will need to setup one "Authenticated User" for your Blackthorn Messaging account. An
Authenticated User is a Salesforce user that has provided access to Messaging so we can push data
into your Salesforce org. Messaging uses the secure OAuth2 protocol to connect to your Salesforce
environment through a user that has granted access to the Messaging connected application.

If you do not setup an Authenticated User then you will not be able to receive incoming text messages,
delivery status updates, or link tracking info.

When you receive an incoming text message to one of your provisioned phone numbers, Messaging
will push that message data to a custom web service in your Salesforce environment. It's important to
understand that the web service will run in the context of the Authenticated User. This means that
Messaging’s access will be controlled by the Authenticated User's pro le and permissions. Messaging
will only have access to the records that the Authenticated User has access to. As an example, if the
Authenticated User does not have access to a particular Contact record due to some Pro le or Sharing
Rule restriction, then Messaging won't be able to match an inbound text message from that Contact to
the record due to lack of visibility.

We recommend that the Authenticated User has, at a minimum, the following object access:

Read/Edit access on the Account, Contact, Lead, Opportunity, and Case objects.
Read/Edit access on all Custom Objects that you will con gure for text messaging.
Read/Edit/Create access on the Phone Number, SMS Message, SMS Template, and Media
objects.
Edit access on all Fields on the Phone Number, SMS Message, SMS Template, and Media
objects.

The Authenticated User does not necessarily need to be a System Administrator, but they should be a
user who has visibility to the records that you will use for text messaging. This includes record data
such as Accounts, Contacts, Leads, Opportunities, Campaigns, and any other Custom Objects that an
SMS message record could be attached to.

Messaging will never delete a record from your Salesforce org.


Messaging does not store any of your standard object, custom object, or SMS Template
records.


Connect an Authenticated User
Now that you understand what an Authenticated User is and how it works, you can follow these steps
to complete the setup:

1. Login as the Salesforce User you want to authenticate.
2. Go to the Messaging Administration tab.
3. Go to the Con guration Setting section.
4. In the Authenticated User (for Inbound Messages) section, click the Authenticate Me button.
5. You will be directed to an OAuth permissions page where you'll click on Allow to grant
access. You should be redirected back to the Messaging Administration page.
6. Now the user is connected as the Authenticated User for the Messaging application. You will
see the name and email of the Authenticated User displayed under the Authenticated User
(for Inbound Messages) section.
7. If you need to change the Authenticated User just click on the delete (trash can) icon next to
the email. You can then login as a different user and re-authenticate.


Reauthorize a User
If any of the following scenarios occur, please reauthorize the user.

A password is changed.
A user is removed.
OAuth access is removed.
A domain is changed.


Con gure Settings
You can con gure Blackthorn Messaging based on how you want the application to perform. To do so,
go to the Messaging Administration tab and click the Con guration Settings tab.

Let’s take a look at each option in detail.


General

Enable Campaigns
Enable this option if you intend to use inbound keyword campaigns. If this box is NOT checked then
Messaging will not attempt to match inbound messages to a campaign.


Enable Trackable Links
Enable this option if you want all URLs that begin with “http://” or “https://” to be shortened into a
trackable link.


Add Messages to Contact on Lead Conversion
When this option is enabled, all messages associated with a Lead will be carried over to the Contact
when the Lead is converted.


Message

Inbound Message Settings

Auto-Create Leads

Enable this option if you want a Lead to be created whenever an inbound message is not matched to
an existing record.


Post Incoming Messages to Chatter
Enable this option if you want a Chatter post to be made to the SMS Message record owner whenever
an incoming text message is received. This is especially helpful on the Salesforce mobile app because
the Chatter post will create an alert.


Default Search Objects
When an incoming text message is received and it cannot be matched to an existing conversation
between the two phone numbers, Messaging will search all the phone elds in this object to nd a
matching record.

You can also enter multiple objects in this eld, i.e. “Contact, Lead”. Messaging will rst attempt to nd
a Contact that matches this phone number. If one is not found, it will then attempt to nd a Lead that
matches the phone number.


Outbound Message Settings

Enable Task Trigger

If enabled, an SMS is automatically sent to the person in the Task’s Name eld when the Task record
is created if the Subjec t eld starts with “Send SMS” and only the Template’s Co de is entered in the
Co mments eld.


Attach Outbound Images

Enable this option if you want to save OUTBOUND images as an attachment to your message. This
only pertains to single messages. Bulk messages that contain an image will never have the image
saved as an attachment.

If this option is enabled, each image attachment will consume le storage space in your Salesforce org.


Consent Popup Frequency

Select either “Once per Recipient,” “Once per Sender,” or "Once per Recipient (Opt-in)" to con gure how
frequently the SMS consent popup will be displayed to the Salesforce user. The popup cannot be fully
disabled due to Messaging’s consent policy. Click here to learn how to change the content of your
help/stop consent messages.


SMS Signature
Your SMS Signature will be attached to the initial message for each number until you receive a reply
from the recipient. Include your company’s name and opt-out instructions in your signature.


Enable Incoming Message Sound
Complete the following steps to enable the incoming message sound.

1. Go to Setup.
2. In the Quick Find box, enter and click "Custom Settings".
3. Click Manage next to Incoming Message Sound.


4. Set I nbo x I nc o ming Message V o lume = "True" (checked).
5. Set I nc o ming Message V o lume = "True" (checked).
6. Click Save.


TO Phone Number Settings
Use the TO Phone Number Settings to con gure the following settings for the Account, Campaign,
Case, Contact, Lead, Opportunity, and User records.

1. Select a phone number eld to include as an option in the TO Phone Number dropdown in
the Messaging component.
2. Select the default phone number eld that users will see.


Scheduled Jobs
The Scheduled Jobs setting allows Admins to start, stop, and delete scheduled jobs. The START /
STOP button was added to control messaging scheduling from the record-level component.


Actions to Perform
Start: To begin or set out the scheduled job for individual messages.
Stop: Pauses the scheduled job, which ceases all the individual planned messages from
sending.
Delete: Cancels or removes the scheduled bulk SMS from sending. You cannot restart it once
you delete the bulk SMS schedule.

Note: The individually scheduled messages will automatically get started/resumed if any user sends an
SMS from the Blackthorn Messaging Messenger.


Start a Scheduled Job
An Admin can only schedule a job if that job starts on the Messaging Admin tab. Complete the steps
below to start using Scheduled Jobs.


1. Go to the Messaging Admin tab.
2. Click Con guration Settings in the left-hand navigation bar.
3. Click the Scheduled Jobs tab.
4. Click START.


Stop a Scheduled Job
If there are pending scheduled jobs in the queue, an Admin cannot stop them. All the currently
scheduled jobs must be completed before the process can be stopped.

The Admin will see the warning icon next to the STOP button when there are jobs scheduled.


After the queue is empty and the Admin clicks STOP, they will receive the following con rmation
message.


Schedule a Message (RLC)
Users will not be able to schedule a message from the record level component (RLC) until an Admin
starts the scheduled job in the Messaging Admin con guration settings. The Schedule for Later
button will also be disabled.


If a user tries to schedule a message and the scheduled job is not started, they will receive the
following error message.


Actions to Perform

You can separately perform additional actions on messages.

Edit Message: Change the body of the message
Reschedule Message: You can schedule the message for another time
Send Now: Sends the message right away


Cancel Message: Calls off the message
Delete Message: Removes the message


Individual Messaging
To gain a better understanding of how Blackthorn Messaging works, let's break it up into two parts.
The rst part we'll explore is the user interface (UI). The second part is the data model.


User Interface
How do I interact with Messaging when I'm in Salesforce? What does it look like? How do I send a
text message?

We're glad you asked. There are four potential interfaces that you'll encounter when using Messaging.
We'll take a look at each one in more detail.


Record Page Messenger
The Messenger component is added to another object's page layout and provides a way to send,
receive, and view the text message history related to a single record. The record can be an Account,
Person Account, Contact, Lead, Case, Opportunity, or a Custom Object record.

The Messenger component can be added to record pages in both Lightning and Classic. On Lightning
record pages, it is added as a custom lightning component. On Classic record pages, it is added as an
inline Visualforce page.


Lightning


Classic


Conversation Inbox
The conversation inbox provides an interface for you to manage multiple conversations from a single
page. The left-hand sidebar displays each conversation with messages grouped by unique phone
number. The right-hand panel provides a scrollable window to view all message history, as well as a
composer to send a new message.


Lightning


Classic


Utility Bar Inbox
This is a condensed version of the conversation inbox that can be accessed from the utility bar in
Lightning. This utility bar application is persistently docked at the bottom of the page, and can be
opened/closed with a click. This allows you to ef ciently carry on multiple conversations while freely
navigating around Salesforce doing your work!


Lightning


Bulk SMS Component
The bulk SMS page provides an interface to send a text message to a list of recipients at the same
time. The bulk SMS page is accessed either from an object List View or from a Campaign.


Lightning


Classic


Data Model
The Messenger data model is designed to be intentionally lightweight when it comes to custom
objects. Eight custom objects are installed into your org.

Conversation
SMS Message
Media
SMS Template
Phone Number
Conversation Filter
Phone Number Lookup
SMS Campaign Response Rule


Phone Number


The Phone Number records correspond to the text-enabled phone numbers that are provisioned to
your Messenger account. Most users will only need Read access to the Phone Number records, except
for Administrators who should have Edit access.


SMS Template
Each template you add will create a new SMS Template record. This record stores information about
the template such as the Name, Status, and the body of the template.


SMS Message
Every text message that you send or receive will create an SMS Message record. This record contains
quite a bit of information about the message, such as the Message Date/Time, the contents of the
message, any related records, link tracking info, and more.


Media
When you receive a text message that contains an image, a Media record will be created. The Media
record will be related to the SMS Message record through a lookup relationship.


SMS Campaign Response Rule
If you create an inbound SMS Keyword Campaign you can de ne auto-responses to be sent back
when someone texts in your keyword. The SMS Campaign Response Rule records are created and
connected to the Campaign.


Con gure Leads
Use the steps below to con gure the Lead object for SMS messaging in Lightning or Classic.


Lightning

Update the Page Layout and Related List

Add the Do Not SMS Field.

1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, search for and click “Lead.”
4. Click the Page Layouts tab.
5. Select the layout type you need to update.
6. Click the Fields tab.
7. In the Quick Find box, search for the Do No t SMS eld.
8. Drag and drop the Do No t SMS eld onto the page layout.


Add the Related List

1. Click the Related Lists tab.
2. In the Quick Find box, search for the “SMS Messages” Related List.
3. Drag and drop the Related List onto the page layout.
4. Click the Wrench icon to open the Properties for this related list.


5. Add these elds in the following order:
a. Message Date
b. Direc tio n
c. Message (Full)
d. Status
e. Fro m P ho ne
f. T o P ho ne
g. SMS Message Number
6. In the Sort By drop-down, choose "SMS Message Number" and "Descending."
7. Click the plus sign (+) located in the Buttons section.
8. Uncheck the box next to New and click Ok.
9. Click Save.


Lightning Record Page Layout
1. Click the Lightning Record Pages tab.
2. Click the name of the layout you want to modify.
3. Click Edit.
4. Complete the following steps if you don't see any Lightning page layouts listed.
a. Click New.
b. Choose Record Page.
c. Click Next.
d. Enter a Label (i.e. Lead Layout).
e. Set Objec t = “Lead.”
f. Click Next.
g. Click the Clone Salesforce Default Page tab.
h. Choose Lead Record Page Default.
i. Click Done.
5. You should now be in the Lightning App Builder.
6. On the left-hand navigation bar, scroll down to the Custom-Managed section.


7. Locate the Blackthorn Messaging Messenger component.
8. Drag and drop the component onto the page layout.
9. The right-hand column will have the con guration options. We recommend keeping the Max
Height (in pix els) = "400px", but you can modify it as needed.
If you've added the component to a sidebar, set Co lumn(s) = “One Column.”
If you've added it to a wide section of the page, you can set Co lumn(s) = “Two
Column” to maximize the space.
10. Click Save.


11. Click Activation.
12. Review the settings.
13. Click Close. Refresh your browser for the changes to take effect.
14. Open a Lead record to see the Blackthorn Messaging Messenger component on your page.


Classic

Update the Page Layout and Related List

Add the Do Not SMS Field

1. Go to Setup.
2. In the Quick Find box, enter “Leads.”
3. Click Page Layouts.


4. Click Edit next to the layout type you need to modify. This will open the Page Layout Editor.
5. Click the Fields tab.
6. In the Quick Find box, search for the Do No t SMS eld.
7. Drag and drop the Do No t SMS eld onto the page layout.


Add the Related List

1. Click the Related Lists tab.
2. In the Quick Find box, search for the “SMS Messages” Related List.
3. Drag and drop the Related List onto the page layout.
4. Click the Wrench icon to open the Properties for this related list.


5. Add these elds in the following order:
a. Message Date
b. Direc tio n
c. Message (Full)
d. Status
e. Fro m P ho ne
f. T o P ho ne
g. SMS Message Number
6. In the Sort By drop-down, choose "SMS Message Number" and "Descending."
7. Click the plus sign (+) located in the Buttons section.


8. Uncheck the box next to New and click Ok.
9. Save the page layout.


Classic Record Page Layout
1. Click the Visualforce Pages tab.
2. Drag and drop the "+Section" on the page.
3. Enter a Sec tio n Name such as "Messaging."
4. Under Display Section Header On, check Detail P age and Edit P age .
5. Set Lay o ut to “1-Column.”
6. Click Ok.


7. In the Visualforce Pages section, nd the page named "SendLead_ltng."
8. Drag and drop SendLead_Itng in the section you just created.
9. Hover over the section and click the Wrench icon to open the Properties for this section.
10. Update the following elds.
a. Change Height (in pix els) to "500."
b. Set Sho w sc ro llbars = “True” (checked).
c. Click Ok.


11. Click Save to save the page layout.


Con gure Contacts
Use the steps below to con gure the Contact object for SMS messaging in Lightning or Classic.


Lightning

Update the Page Layout and Related List

Add the Do Not SMS Field.

1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, search for and click “Contact.”
4. Click the Page Layouts tab.
5. Select the layout type you need to update.
6. Click the Fields tab.
7. In the Quick Find box, search for the Do No t SMS (Co ntac t) eld.
8. Drag and drop the Do No t SMS (Co ntac t) eld onto the page layout.


Add the Related List

1. Click the Related Lists tab.
2. In the Quick Find box, search for the “SMS Messages (Contact)” Related List.
3. Drag and drop the Related List onto the page layout.
4. Click the Wrench icon to open the Properties for this related list.


5. Add these elds in the following order:
a. Message Date
b. Direc tio n
c. Message (Full)
d. Status
e. Fro m P ho ne
f. T o P ho ne
g. SMS Message Number
6. In the Sort By drop-down, choose "SMS Message Number" and "Descending."
7. Click the plus sign (+) located in the Buttons section.
8. Uncheck the box next to New and click Ok.
9. Click Save.


Lightning Record Page Layout
1. Click the Lightning Record Pages tab.
2. Click the name of the layout you want to modify.
3. Click Edit.
4. Complete the following steps if you don't see any Lightning page layouts listed.
a. Click New.
b. Choose Record Page.
c. Click Next.
d. Enter a Label (i.e. Contact Layout).
e. Set Objec t = “Contact.”
f. Click Next.
g. Click the Clone Salesforce Default Page tab.
h. Choose Contact Record Page Default.
i. Click Done.
5. You should now be in the Lightning App Builder.
6. On the left-hand navigation bar, scroll down to the Custom-Managed section.


7. Locate the Blackthorn Messaging Messenger component.
8. Drag and drop the component onto the page layout.
9. The right-hand column will have the con guration options. We recommend keeping the Max
Height (in pix els) = "400px", but you can modify it as needed.
If you've added the component to a sidebar, set Co lumn(s) = “One Column.”
If you've added it to a wide section of the page, you can set Co lumn(s) = “Two
Column” to maximize the space.
10. Click Save.


11. Click Activation.
12. Review the settings.
13. Click Close. Refresh your browser for the changes to take effect.
14. Open a Contact record to see the Blackthorn Messaging Messenger component on your page.


Classic

Update the Page Layout and Related List

Add the Do Not SMS Field

1. Go to Setup.


2. In the Quick Find box, enter “Contacts.”
3. Click Page Layouts.
4. Click Edit next to the layout type you need to modify. This will open the Page Layout Editor.
5. Click the Fields tab.
6. In the Quick Find box, search for the Do No t SMS eld.
7. Drag and drop the Do No t SMS eld onto the page layout.


Add the Related List

1. Click the Related Lists tab.
2. In the Quick Find box, search for the “SMS Messages” Related List.
3. Drag and drop the Related List onto the page layout.
4. Click the Wrench icon to open the Properties for this related list.


5. Add these elds in the following order:
a. Message Date
b. Direc tio n
c. Message (Full)
d. Status
e. Fro m P ho ne
f. T o P ho ne


g. SMS Message Number
6. In the Sort By drop-down, choose "SMS Message Number" and "Descending."
7. Click the plus sign (+) located in the Buttons section.
8. Uncheck the box next to New and click Ok.
9. Save the page layout.


Classic Record Page Layout
1. Click the Visualforce Pages tab.
2. Drag and drop the "+Section" on the page.
3. Enter a Sec tio n Name such as "Messaging."
4. Under Display Section Header On, check Detail P age and Edit P age .
5. Set Lay o ut to “1-Column.”
6. Click Ok.


7. In the Visualforce Pages section, nd the page named "SendLead_ltng."
8. Drag and drop SendLead_Itng in the section you just created.
9. Hover over the section and click the Wrench icon to open the Properties for this section.
10. Update the following elds.
a. Change Height (in pix els) to "500."
b. Set Sho w sc ro llbars = “True” (checked).
c. Click Ok.


11. Click Save to save the page layout.


Con gure Accounts
Use the steps below to con gure the Account object for SMS messaging in Lightning or Classic.


Lightning

Update the Page Layout and Related List

Add the Do Not SMS Field.

1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, search for and click “Account.”
4. Click the Page Layouts tab.
5. Select the layout type you need to update.
6. Click the Fields tab.
7. In the Quick Find box, search for the Do No t SMS (A c c o unt) eld.
8. Drag and drop the Do No t SMS (A c c o unt) eld onto the page layout.


Add the Related List

1. Click the Related Lists tab.
2. In the Quick Find box, search for the “SMS Messages (Account)” Related List.
3. Drag and drop the Related List onto the page layout.
4. Click the Wrench icon to open the Properties for this related list.


5. Add these elds in the following order:
a. Message Date
b. Direc tio n
c. Message (Full)
d. Status
e. Fro m P ho ne
f. T o P ho ne
g. SMS Message Number
6. In the Sort By drop-down, choose "SMS Message Number" and "Descending."
7. Click the plus sign (+) located in the Buttons section.
8. Uncheck the box next to New and click Ok.
9. Click Save.


Lightning Record Page Layout
1. Click the Lightning Record Pages tab.
2. Click the name of the layout you want to modify.
3. Click Edit.
4. Complete the following steps if you don't see any Lightning page layouts listed.
a. Click New.
b. Choose Record Page.
c. Click Next.
d. Enter a Label (i.e. Account Layout).
e. Set Objec t = “Account.”
f. Click Next.
g. Click the Clone Salesforce Default Page tab.
h. Choose Account Record Page Default.
i. Click Done.
5. You should now be in the Lightning App Builder.
6. On the left-hand navigation bar, scroll down to the Custom-Managed section.


7. Locate the Blackthorn Messaging Messenger component.
8. Drag and drop the component onto the page layout.
9. The right-hand column will have the con guration options. We recommend keeping the Max
Height (in pix els) = "400px", but you can modify it as needed.
If you've added the component to a sidebar, set Co lumn(s) = “One Column.”
If you've added it to a wide section of the page, you can set Co lumn(s) = “Two
Column” to maximize the space.
10. Click Save.


11. Click Activation.
12. Review the settings.
13. Click Close. Refresh your browser for the changes to take effect.
14. Open an Account record to see the Blackthorn Messaging Messenger component on your
page.


Classic

Update the Page Layout and Related List

Add the Do Not SMS Field

1. Go to Setup.
2. In the Quick Find box, enter “Accounts.”


3. Click Page Layouts.
4. Click Edit next to the layout type you need to modify. This will open the Page Layout Editor.
5. Click the Fields tab.
6. In the Quick Find box, search for the Do No t SMS eld.
7. Drag and drop the Do No t SMS eld onto the page layout.


Add the Related List

1. Click the Related Lists tab.
2. In the Quick Find box, search for the “SMS Messages” Related List.
3. Drag and drop the Related List onto the page layout.
4. Click the Wrench icon to open the Properties for this related list.


5. Add these elds in the following order:
a. Message Date
b. Direc tio n
c. Message (Full)
d. Status
e. Fro m P ho ne
f. T o P ho ne
g. SMS Message Number


6. In the Sort By drop-down, choose "SMS Message Number" and "Descending."
7. Click the plus sign (+) located in the Buttons section.
8. Uncheck the box next to New and click Ok.
9. Save the page layout.


Classic Record Page Layout
1. Click the Visualforce Pages tab.
2. Drag and drop the "+Section" on the page.
3. Enter a Sec tio n Name such as "Messaging."
4. Under Display Section Header On, check Detail P age and Edit P age .
5. Set Lay o ut to “1-Column.”
6. Click Ok.


7. In the Visualforce Pages section, nd the page named "SendLead_ltng."
8. Drag and drop SendLead_Itng in the section you just created.
9. Hover over the section and click the Wrench icon to open the Properties for this section.
10. Update the following elds.
a. Change Height (in pix els) to "500."
b. Set Sho w sc ro llbars = “True” (checked).
c. Click Ok.


11. Click Save to save the page layout.


Con gure Opportunities
Use the steps below to con gure the Opportunity object for SMS messaging.

A P ho ne eld is required on any object you want to use for text messaging. The Opportunity object do
not come with a standard P ho ne eld, so you will need to ensure that you have created at least one
custom P ho ne eld.


Lightning

Create a Do Not SMS Field
If the Do No t SMS eld hasn’t been added to your Opportunity object, add it now.


1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, enter and click “Opportunity.”
4. Click the Fields & Relationships tab.
5. Click New.
6. Select “Checkbox” and click Next.


7. Enter the following information.
a. Field Label : “Do Not SMS”
b. Field Name : “Do_Not_SMS”
c. Help T ex t : “Check this box to stop an SMS message from being sent to this
Opportunity.”
d. Set the remaining elds based on your requirements.


8. Click Next.


9. Select the pro le access for this eld.
10. Click Next.
11. Select the layouts you want to add the eld to.
12. Click Save.


Update the Page Layout and Related List

Add the Do Not SMS Field

1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, search for and click “Opportunity.”
4. Click the Page Layouts tab.
5. Select the layout type you need to update.
6. Click the Fields tab.
7. In the Quick Find box, search for the Do No t SMS eld.
8. Drag and drop the Do No t SMS eld onto the page layout.


Add the Related List

1. Click the Related Lists tab.
2. In the Quick Find box, search for the “SMS Messages” Related List.
3. Drag and drop the Related List onto the page layout.
4. Click the Wrench icon to open the Properties for this related list.


5. Add these elds in the following order:
a. Message Date
b. Direc tio n
c. Message (Full)
d. Status
e. Fro m P ho ne
f. T o P ho ne
g. SMS Message Number
6. In the Sort By drop-down, choose "SMS Message Number" and "Descending".
7. Click the plus sign (+) located in the Buttons section.
8. Uncheck the box next to New and click Ok.
9. Click Save.


Lightning Record Page Layout
1. Click the Lightning Record Pages tab.
2. Click the name of the layout you want to modify.
3. Click Edit.
4. If you don't see any Lightning page layouts listed, complete the following steps.
a. Click New.
b. Choose Record Page.
c. Click Next.
d. Enter a Label (i.e. Opportunity Layout).


e. Set Objec t = “Opportunity.”
f. Click Next.
g. Click the Clone Salesforce Default Page tab.
h. Select a page layout.
i. Click Done.
5. You should now be in the Lightning App Builder.
6. On the left-hand navigation bar, scroll down to the Custom-Managed section.
7. Locate the Blackthorn Messaging Messenger component.
8. Drag and drop the component onto the page layout.
9. The right-hand column will have the con guration options. We recommend keeping the Max
Height (in pix els) = "400px", but you can modify it as needed.
If you've added the component to a sidebar, set Co lumn(s) = “One Column.”
If you've added it to a wide section of the page, you can set Co lumn(s) = “Two
Column” to maximize the space.
10. Click Save.


11. Click Activation.
12. Review the settings.
13. Click Close. Refresh your browser for the changes to take effect.


14. Open an Opportunity record to see the Blackthorn Messaging Messenger component on your
page.


Con gure Cases
Use the steps below to con gure the Case object for SMS messaging.


Create a Do Not SMS Field
If the Do No t SMS eld hasn’t been added to your Case object, add it now.


1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, enter and click “Case.”
4. Click the Fields & Relationships tab.
5. Click New.
6. Select “Checkbox” and click Next.


7. Enter the following information.
Field Label : “Do Not SMS”
Field Name : “Do_Not_SMS”
Help Text: “Check this box to stop an SMS message from being sent to this Case.”
Set the remaining elds based on your requirements.


8. Click Next.


9. Select the pro le access for this eld.
10. Click Next.
11. Select the layouts you want to add the eld to.
12. Click Save.


Update the Page Layout and Related List

Add the Do Not SMS Field
1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, search for and click “Case.”
4. Click the Page Layouts tab.
5. Select the layout type you need to update.
6. Click the Fields tab.
7. In the Quick Find box, search for the Do No t SMS eld.
8. Drag and drop the Do No t SMS eld onto the page layout.


Add the Related List
1. Click the Related Lists tab.
2. In the Quick Find box, search for the “SMS Messages” Related List.
3. Drag and drop the Related List onto the page layout.
4. Click the Wrench icon to open the Properties for this related list.


5. Add these elds in the following order:
Message Date
Direc tio n
Message (Full)
Status
Fro m P ho ne
T o P ho ne
SMS Message Number
6. In the Sort By drop-down, choose "SMS Message Number" and "Descending".
7. Click the plus sign (+) located in the Buttons section.
8. Uncheck the box next to New and click Ok.
9. Click Save.


Lightning Record Page Layout
1. Click the Lightning Record Pages tab.
2. Click the name of the layout you want to modify.
3. Click Edit.
4. If you don't see any Lightning page layouts listed, complete the following steps.
a. Click New.
b. Choose Record Page.
c. Click Next.
d. Enter a Label (i.e. Case Layout).
e. Set Objec t = “Case.”
f. Click Next.
g. Click the Clone Salesforce Default Page tab.
h. Select a layout.
i. Click Done.
5. You should now be in the Lightning App Builder.


6. On the left-hand navigation bar, scroll down to the Custom-Managed section.
7. Locate the Blackthorn Messaging Messenger component.
8. Drag and drop the component onto the page layout.
9. The right-hand column will have the con guration options. We recommend keeping the Max
Height (in pix els) = "400px", but you can modify it as needed.
If you've added the component to a sidebar, set Co lumn(s) = “One Column.”
If you've added it to a wide section of the page, you can set Co lumn(s) = “Two
Column” to maximize the space.
10. Click Save.


11. Click Activation.
12. Review the settings.
13. Click Close. Refresh your browser for the changes to take effect.
14. Open a Case record to see the Blackthorn Messaging Messenger component on your page.


Con gure Custom Objects
Use the steps below to con gure a custom object for SMS messaging. You will need to add a lookup
eld on the SMS Message object and create a new eld on the custom object. For this example, we are
using the Attendee object.


SMS Object

Create a Custom Object Lookup Field
1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, enter and click “SMS Message.”
4. Click the Field & Relationships tab.
5. Click New.
6. Select “Lookup Relationship” and click Next.


7. Set Related T o to “Attendee” and click Next.


8. Enter the following information.
Field Label : “Attendee”
Field Name : “Attendee”
Help T ex t : “The Attendee who is related to this SMS message”
Child Relatio nship Name = “SMS_Message”
Set the remaining elds based on your requirements.


9. Click Next.
10. Select the pro le access for this eld.
11. Click Next.
12. Make sure the new eld will be added to the page layout.


13. Click Next.


14. Enter a Related List Label .


15. Click Save.

Messaging will now detect the relationship between the SMS Message and Attendee objects. You can
also add the Messaging Messenger component to this object's page and create SMS Templates for this
object.


Custom Object

Create a Do Not SMS Field
1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, enter and click “Attendee.”
4. Click the Fields & Relationships tab.
5. Click New.
6. Select “Checkbox” and click Next.


7. Enter the following information.
Field Label : “Do Not SMS”
Field Name : “Do_Not_SMS”


Help T ex t : “Check this box to stop an SMS message from being sent to this
Attendee.”
Set the remaining elds based on your requirements.


8. Click Next.
9. Select the pro le access for this eld.
10. Click Next.
11. Make sure the new eld will be added to the page layout.


12. Click Save.


Create a Data Type Phone Field


To send SMS messages to a custom object, the custom object needs a Phone eld that has Data
T y pe = "Phone." Messaging will not detect phone numbers in text elds.


1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, enter and click “Attendee.”
4. Click the Fields & Relationships tab.
5. Click New.
6. Select “Phone” and click Next.


7. Enter the following information.
Field Label : “Phone”
Field Name : “SMS_Phone
Help T ex t : "Use this phone number to send to send SMS messages.”
Set the remaining elds based on your requirements.


8. Click Next.
9. Select the pro le access for this eld.
10. Click Next.


11. Make sure the new eld will be added to the page layout.


12. Click Save.


Lightning

Update the Page Layout and Related List

Add the Do Not SMS Field

1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, search for and click “Attendee.”
4. Click the Page Layouts tab.
5. Select the layout type you need to update.
6. Click the Fields tab.
7. In the Quick Find box, search for the Do No t SMS eld.
8. Drag and drop the Do No t SMS eld onto the page layout.


Add the Related List

1. Click the Related Lists tab.
2. In the Quick Find box, search for the “SMS Messages” Related List.
3. Drag and drop the Related List onto the page layout.
4. Click the Wrench icon to open the Properties for this related list.


5. Add these elds in the following order:
a. Message Date
b. Direc tio n
c. Message (Full)
d. Status
e. Fro m P ho ne
f. T o P ho ne
g. SMS Message Number
6. In the Sort By drop-down, choose "SMS Message Number" and "Descending".
7. Click the plus sign (+) located in the Buttons section.
8. Uncheck the box next to New and click Ok.
9. Click Save.


Lightning Record Page Layout
1. Click the Lightning Record Pages tab.
2. Click the name of the layout you want to modify.
3. Click Edit.
4. If you don't see any Lightning page layouts listed, complete the following steps.
a. Click New.
b. Choose Record Page.
c. Click Next.
d. Enter a Label (i.e. Attendee Layout).
e. Set Objec t = “Attendee.”


f. Click Next.
g. Click the Clone Salesforce Default Page tab.
h. Choose a layout.
i. Click Done.
5. You should now be in the Lightning App Builder.
6. On the left-hand navigation bar, scroll down to the Custom-Managed section.
7. Locate the Blackthorn Messaging Messenger component.
8. Drag and drop the component onto the page layout.
9. The right-hand column will have the con guration options. We recommend keeping the Max
Height (in pix els) = "400px", but you can modify it as needed.
10. If you've added the component to a sidebar, set Co lumn(s) = “One Column.”
11. If you've added it to a wide section of the page, you can set Co lumn(s) = “Two Column” to
maximize the space.
12. Click Save.


13. Click Activation.
14. Review the settings.
15. Click Close. Refresh your browser for the changes to take effect.
16. Open an Attendee record to see the Blackthorn Messaging Messenger component on your
page.


Inbound Messages
Before you can begin to receive inbound messages you will rst need to ensure that you have
authenticated a Salesforce user for Blackthorn Messaging. You won't be able to receive inbound
messages into Salesforce until you complete this.

But, what happens when you receive an inbound message to one of your phone numbers? Let's
explore the process below.


Inbound Message Routing
When an inbound text message is received, the rst step is to create the SMS Message record in
Salesforce. We also need to relate the SMS Message record to the appropriate parent record (i.e. a
Contact, Lead, Account, etc). There are two methods that Messaging uses to match an inbound
message to the appropriate parent record. We’ll explain these two methods in detail.


Existing Conversation
The rst attempt to match an inbound message to the correct parent record is to search for an existing
conversation between the two phone numbers. Messaging will look for an outgoing message to the
sender’s phone number from the phone number that the sender is replying to.

Let’s look at an example to understand this better. You have sent a message to a contact named John
Doe. You have sent the message from 555-555-5555 to 555-555-9999 (this is John Doe’s mobile
number). John Doe replies from his mobile phone number (555-555-9999) to your phone number
(555-555-5555). Messaging will detect the outgoing message from 555-555-5555 and the inbound
message will be associated to the John Doe contact record.


Record Search
When an inbound message is received and no existing conversation is detected, Messaging will
perform a search of your records to nd the sender’s phone number. The inbound message will then
be associated to the rst record that is found that contains the sender’s phone number. You determine
the objects that you want Messaging to search using the Default Search Object setting on the
Con guration Settings page.

Let’s look at an example. On the Con guration Settings page, you’ve set the Default Search Object to
Contact. An inbound message is received from 555-555-9999, but there has never been an outgoing
message sent to that phone number. Messaging will now then search all of your Contact phone
number elds looking for a Contact that contains 555-555-9999. The inbound message will be
associated to the rst record (most recently modi ed) that contains that phone number.


You can also set multiple objects in the Default Search Object eld. The object names need to be
separated by a comma. For example, let’s say you’ve set the Default Search Object to "Contact, Lead".
Messaging will rst search all Contacts for the matching phone number. If no Contacts are matched
then the Leads will be searched for a match.


What if there’s no match?
If neither the Existing Conversation nor the Record Search methods nd a match for the phone
number, then the next step depends on your con guration settings.

1. If the Auto-Create Leads option is enabled (on the Con guration Settings page), then a new
Lead will be created and the inbound SMS Message record will be associated to the new
Lead. New Leads are given some default values for the required elds. They are as follows:
Last Name: “SMS Lead datetime” (where datetime is the date/time the Lead was
created)
Company: “SMS Lead”
Mobile: the sender’s phone number
2. If the Auto-Create Leads option is NOT enabled, then the inbound message will create a new
SMS Message record but it will not be associated with a parent record.


Inbound Image Messages (MMS)
Inbound image messages can contain photos/media plus text or only photos/media. If the inbound
image message does NOT contain text, an email noti cation will not be triggered.

This is expected behavior as there is a work ow rule called “Email Owner When SMS Message
Received” that is triggered only if the Message eld on the SMS Message record contains text.

To resolve this issue, clone the work ow rule and remove the rst criteria. This will trigger an email
noti cation when an inbound message contains photos/media but no text.


Object Structure
When an inbound image message with text is received, the image is saved as a Salesforce File. The File
is related to the Media record which is related to the SMS Message record.


Blackthorn Messaging Inbox
Let's take a closer look at how you can use the Blackthorn Messaging Conversations page.


Filter your view


When you rst open the Messaging Conversations page you will see all of your organization's
Conversations listed on the left-hand side in chronological order (descending from newest to oldest).

However, you'll likely want to lter this view to only see those Conversations you're interested in.
Here are the details for your ltering options:


Display
All Conversations: Starts with the set of all Conversations that the current user has visibility
to.
My Conversations: Starts with only those Conversations owned by the current user.
My Sent Messages: Shows only the current user's outbound text messages. These may
include text messages that were sent but are not part of a Conversation.


Conversation Status
Needs Response: Conversations where the last text message was inbound. This should
indicate that you need to respond back.
Responded: Conversations where the last text message was outbound. This indicates that
your organization was the last to respond to the conversation.
Closed: Conversations that have been closed internally.


Phone Number
This lter allows you to see Conversations based on which of your internal phone numbers are used.
For example, if you have a phone number that is used for Customer Support and you only want to see
Conversations where that number is involved, you can use this lter.


List View
This lter lets you use your pre-de ned object list views to determine which conversations you see.
For example, let's say you have a list view for your Hot Leads. You can select that list view from this
lter so that only conversations with those Leads will be visible.


Compose a New Message


Now you can compose a new text message directly from the Messaging Conversations page. Just
select the New Message icon and search for the record you want to text. You'll then be able to
compose your text message, including use of templates and ability to add an image.


Conversation Maintenance
Conversations
Conversation Ownership Routing
Accept and Transfer Conversations
Merge Conversations
Real-Time Conversation Updates
Mass Close Conversations


Real-Time Conversation Updates
When you are managing multiple text message conversations across a team of people, it's important
that the conversations stay in sync. This means that if one person has taken ownership of a
conversation, or is in the middle of typing a reply, everyone else should have visibility into that. This
helps teams be more productive by knowing which conversations are being responded to, and prevents
your team from inadvertently stepping on each other's toes by responding to the same message.

Blackthorn Messaging streams real-time updates in the following scenarios:

The conversation ownership changes.
The conversation status changes.
A user is typing a message into the conversation.
A new conversation message is sent.

When one of these updates is streamed, it means that any other users who have the Messaging
component on their page (either on the Messaging Conversations page, the Utility Bar, or on a record
page) will see that update, too.

For these updates to work properly, your users will need access to the Streaming API and speci cally
the StreamingChannel object in Salesforce.


Conversations

What is a Conversation?
You can think of a Conversation as a container for a group of text messages. Each Conversation is
de ned by attributes such as Start Time and End Time and is unique to the phone numbers
involved (your internal Messaging phone number and the recipient's phone number).

A Conversation is either Open or Closed, and it will have a status such as "Needs Response" or
"Responded" so that you can easily surface those conversations that need attention.


How is a Conversation created?
The good news is you don't need to create Conversations manually. They will be created automatically
based on logical rules.

A Conversation is only created from an inbound text message. When you send a text message to
someone a Conversation isn’t immediately created. After all, it's just an outbound text message. If that
person responds back, a new Conversation will be created, and both text messages (your outbound
and their inbound) will be part of the new Conversation.

If someone sends you an inbound text and an existing Open Conversation between your phone
numbers doesn’t exist, a new Conversation will be created.


How does a Conversation work after it's created?
Once a Conversation is created between two phone numbers, any text messages sent between those
two phone numbers will be contained within that Conversation while it is open.

Each time a message is added to the Conversation, the status updates to re ect whether the last
message was inbound or outbound.

If the last message is inbound, the status is "Needs Response".
If the last message is outbound, the status is "Responded".

When the Conversation is closed, no further text messages will be added to that particular
Conversation.


Where do I view Conversations?


The existing Messaging Conversations page has been updated to include some new features. Also, the
Messaging Messenger component that you access on the record pages has been updated to include
new features related to the Conversations.


Messaging Conversations Component


Messaging Messenger Component (on Record pages)


Conversation History Component (New)


Mass Close Conversations
Watch this quick video on how to mass close conversations.


Accept and Transfer Conversations
You now have the ability to Accept or Transfer conversations within Blackthorn Messaging. Accepting a
conversation means assigning ownership of that conversation to yourself. While Transferring a
conversation means assigning ownership of that conversation to another user or queue.


Merge Conversations
Sometimes you may need to merge two conversations together. This can occur when you close a
conversation, but then your customer replies back in response. You will have two distinct conversation
records that you may decide to merge into one.

Keep in mind that you can only merge conversations that occur between the same two phone
numbers. You cannot merge conversations that exist between different internal/recipient phone
numbers.


Conversation Ownership Routing
Conversation Routing allows you to designate how new conversations are assigned ownership when
they are created.


The routing is con gured at the phone number level, allowing you to set a different routing
option for each of your phone numbers.
The ownership can be routed to a user, queue, or to the related record owner.


Setting Up Ownership Routing Is Important
When a customer sends you a text message, a new Conversation record is created (assuming there is
not already an open Conversation between your two phone numbers. This Conversation record needs
to be owned by someone so that it can be looked at and responded to.

Conversation Routing lets you determine who that someone is so that the conversation can be
assigned to the appropriate person. The routing for each phone number can be customized in the
Blackthorn Messaging Administration page.


1. Go to the Messaging Administration page.
2. Click into the Phone Numbers section (phone icon).
3. Click the pencil icon under Ownership Routing.


Let's Look at Each of the Routing Options

User

You can assign all new conversations for a phone number to a speci c User. This is a good option
when you have a unique phone number con gured for each user. You can assign all new conversations
for the phone number to that one particular user.


Queue
Assign new conversations for a phone number to a Queue. Here we are referring to a standard
Salesforce Queue. You would rst need to create a Queue and con gure it to own Conversation and
SMS Message objects. This type of routing is a good option when you have a generic phone number
that multiple users are responsible for monitoring.

For example, let's say you publish a phone number on your website for your customers to text you.
You then have a group of Salesforce users who are responsible for monitoring the inbound texts to
that phone number.


Related Record Owner
This option will dynamically set the owner of the new conversation based on the user who owns the
related record. For example, suppose one of your Leads sends a text message to you and a new
Conversation is created. That Conversation will then be assigned ownership to the Lead Owner.


Last Sent Message Owner
This option will dynamically route the new Conversation to the user who sent the last outbound text
message to this recipient. As an example, let's say you have a Contact record named Arthur Blank. You
have two users, Julio and Matt. Matt owns the Contact record, but Julio sends a text message. When
Arthur responds the conversation is routed to Julio as he was the last outbound sender to Arthur.


Phone Number Lookups
Phone Number Lookups is a feature that's now available within the Blackthorn Messaging application.
In this article, you'll learn what a Phone Number Lookup is and why it's important to your business.
You will also nd links to other helpful articles that explain the technical how-tos of this new feature
and provide you with some example use cases.


What is a Phone Number Lookup?
A phone number lookup is a process where, given a phone number, we can identify the number's
carrier (Verizon Wireless, AT&T, etc) and the type of phone it is (landline, mobile, or VoIP). A lookup can
also identify a Bad Number which is a badly formatted number or one that does not exist.

When a phone number is looked up using this feature, the phone number information is stored in your
Salesforce org for use in other areas of the Messaging application.


What are the bene ts of Phone Number
Lookups?
Save money. When you send an SMS the carrier will attempt to deliver that message even if the
recipient's phone number is a landline. This still results in the message being deducted from your
Messaging account balance. The problem, however, is that the message will not reach anyone so you
have unnecessarily wasted messages from your balance, and that costs money. Messaging has new
built-in features that help you utilize your phone number lookup data to prevent unnecessarily sending
messages to landlines and bad numbers.

Validate user input. You most likely create phone number data in Salesforce using a number of sources
and methods. For example, you may collect data through forms on your website, third-party
integrations, and/or from your Salesforce users manually entering phone numbers. You end up with a
lot of phone numbers in your org, but you don't really have insight into the type of phone and whether
it is a landline, mobile, or just some non-existent phone number that someone typed in. Messaging
now has built-in automations that allow you to instantly look up a phone number using the Process
Builder.


Admin Page
The new Phone Number Lookup admin page has three main areas of functionality on the right-hand
side.


Let's look at each section, starting from the top-right.


Phone Number Lookup Results
This section shows you key metrics for your phone number lookup data at a glance.


New Numbers: This is the quantity of phone numbers that have been discovered in your org
but have not been looked up yet.
Opt Outs: This is the quantity of phone numbers that have been discovered in your org, but
the phone number exists on a record that has opted out (i.e. where the Do Not SMS eld is
checked). Phone numbers are excluded from being looked up if they are on a record where
that person has opted out of receiving text messages.
Ready to Lookup: This is the net number of phone numbers that will be looked up when you
start the Lookup Numbers batch process. This number is derived from the following formula
"New Numbers - Opt Outs".
Completed Lookups: This is the number of phone number lookup records in your org that
have a Status of "Success". This means the phone number is valid and we have collected the
lookup data. You should also see a link to a Salesforce report of Phone Number Lookup
records.


Lookup Phone Numbers
This section guides you through the steps necessary to discover and lookup the phone numbers that
exist in your org. Blackthorn Messaging includes two primary batch processes that work together to
rst nd new phone numbers in your org, and then process the lookups on those phone numbers to
collect and store the phone number details.


Let's look at each button and what it does.

Find New Numbers: This initiates a batch process to nd new phone numbers in your org
that have not been looked up yet. When you click the button you'll be able to select the
objects that you want Messaging to search through to nd phone numbers. When this
process completes, the data points will be updated in the section above titled "Phone
Number Lookup Results".


Purchase Lookups: After you run the batch process to determine how many new phone
numbers need to be looked up in your org, you will need to ensure that you have the
necessary lookup credits on your balance. Each phone number that you collect lookup data
for will deduct one lookup credit from your balance. If you don't have suf cient lookup
credits on your balance this button will be enabled to allow you to purchase additional
lookup credits. For your convenience, the difference between your current balance and what
you need will be calculated for you.
Lookup Numbers: This will initiate a batch process to begin collecting and appending the
lookup data for each phone number in your org. The new phone numbers that exist in your
org will be sent to a Messaging service to be processed. Each phone number will be looked
up to nd the carrier data and then that data will be pushed back to your Salesforce org and
stored in the Phone Number Lookup records.


Phone Number Lookup Settings
This section provides optional con guration settings that can be managed as needed.


Let's look at each setting below.


Enable Automatic Phone Number Lookups: When this setting is activated, a lookup will
automatically be performed whenever a user attempts to send a text message to a phone
number that has not been looked up, yet. This setting only affects individual messages sent
by a user from the Messaging Messenger or Messaging Conversations component.
Show Visual Indicators for Phone Numbers Not Looked Up: When this setting is activated,
you will see a question mark icon next to any phone number that has not been looked up,
yet. This question mark will be visible in the To drop-down on the Messaging Messenger and
Messaging Conversation components.


Show Con rmation Popup for Landlines and Bad Numbers: When this setting is activated,
a user will see a con rmation popup if they attempt to send a text to a landline or an invalid
phone number. This popup will only occur when an individual message is sent from the
Messaging Messenger or Messaging Conversation components.


Reports and Object Model
The Phone Number Lookup feature introduces a new object into the Blackthorn Messaging object
model that facilitates storing information about a particular phone number. The object is named Phone
Number Lookup.

Let's take a look at the anatomy of a Phone Number Lookup record.

Object Name: Phone Number Lookup

Fields:

Field
Type                                     Description
Name
Carrier
Error           Text         Error message provided if there is an error with the lookup
Code
Carrier
Text         Name of the phone carrier (Verizon, AT&T, etc)
Name
Country                      Calling code pre x of the country for which this phone number is
Text
Code                         associated.
Do Not                       This will be TRUE if the phone number exists on a record where the Do
Checkbox
SMS                          Not SMS eld is TRUE.
Expiration
Date         By default, this will be 6 months after the Last Lookup Date.
Date
Last
Lookup          Date         The date on which this phone number was last successfully looked up.
Date
A ag that indicates whether this record needs to be looked up. This
Lookup          Formula
will be checked when the Status = New or if the Expiration Date has
Pending         (Checkbox)
passed.
Mobile
Country         Text         Identi er for the mobile network operator.
Code
Mobile
Network         Text         Identi er for the mobile network operator.
Code
National                     The traditional formatting of the phone number speci c to the
Text
Format                       country. For example, (555) 555-5555.
Number
Text
Type
Phone
Text         The phone number in E.164 format. For example, +15555555555.
Number
The status of this lookup record. Accepted values are New, Success,
Status          Text
Failure, or Bad Number.


Enable Phone Number Lookup
Automations
When you rst install Blackthorn Messaging (or upgrade from a version earlier than 3.12), you will
most likely want to run the initial batch process to lookup all of your existing phone numbers.
However, after that process is complete, you will want to be able to lookup phone numbers
automatically on a go-forward basis as they're captured within your various records in Salesforce.

Let's explore the options for automating these lookups.


Enable Automatic Phone Number Lookups
Con guration Setting


On the Messaging Administration page, there is a con guration setting that you can activate named
"Enable Automatic Phone Number Lookups". It's important to understand exactly what this setting
does.

This setting only affects individual text messages sent from the Messaging Messenger component, or
from the Messaging Conversations page. When a user sends a text message to a phone number that
has not been looked up, the phone number will rst be looked up in real-time using the Messaging
phone number lookup service.


If the phone number is mobile or VoIP, the text will immediately be sent. If the phone number is a
landline or bad/invalid phone number, then the user will be prompted with a pop-up alert to let them
know this and they can choose to not send the text.

Keep in mind that this will consume one lookup credit from your lookup balance. The trade-off is that
by looking up the phone number you will prevent sending to a landline or invalid phone number thus
wasting that text message.

Also, this process will create the Phone Number Lookup record in Salesforce. The good news is that
after you lookup the phone number once it will continue to prevent/alert any user that tries to send a
text to that number.


Messaging Lookup Number (Process Builder)
Another option for automating phone number lookups is to use the new Messaging Lookup Number
action from within the Process Builder. This is a new custom Apex action that you can leverage from
anywhere in your processes.

This action is ideal for the Process Builder because it performs the phone number lookup
asynchronously. Since the phone number lookup makes an Apex callout to the Messaging lookup
service, this async process lets you invoke this action directly after a record insert or update without
error. The phone number will be looked up and then the Phone Number Lookup record will be created.
This callout is wrapped in an asynchronous queued job, so it may take a few seconds to execute the
lookup and create the data.

Let's look at a scenario for using this action in the process builder. In this quick video tutorial, we'll
demonstrate creating a Process to automatically lookup Lead phone numbers as soon as the Lead is
created.


Messaging Lookup Number (Flow)
This is a custom Apex action that can be inserted into your ows. This particular action is more suited
for use within a Flow (as opposed to the above action for process builders) because it makes a
synchronous callout to the phone number lookup service. This allows you to get the lookup response
back in real time and possibly branch your logic using this information.


Run a Batch Process to Lookup Your
Existing Phone Numbers
Blackthorn Messaging now includes functionality to help you eliminate wasted messages, conserve
your message balance, and save money by identifying landline and badly formatted phone numbers
and preventing you from sending text messages to them.

For these features to work, however, it is crucial to perform a lookup on each of your phone numbers.
Performing a lookup means that Messaging processes the phone number and stores information about
that phone number in your Salesforce org. This information is then used by various Messaging
components.

When you rst install Messaging (or upgrade to version 3.12 or higher), you will not have any Phone
Number Lookup data in your org. This means that the Messaging components cannot infer any
information about your phone numbers.

The rst step is to run an initial batch process to gather up your phone numbers and process them
through the Messaging lookup service. Once this process is complete you will have Phone Number
Lookup records in your org that provide carrier information about each phone number.


Step 1: Find New Numbers


When you click the Find New Numbers button, you can select the objects you want Messaging to
include when searching for new phone numbers. This list includes standard objects such as Accounts,
Contacts, Leads, Cases, and Opportunities. Custom objects that have been con gured for texting will
also be available to select. The objects that you select will be the only objects included when searching
for phone numbers.

Another option is to choose the age of any existing Phone Number Lookup records that you want to
exclude. By default, Messaging will place a 6-month expiration date on the record so that you know
how long ago you last looked up the phone number.

Once you've made the above choices, you will click the Run button. This will begin the process of
nding any new phone numbers in your org that have not been looked up yet.


Keep in mind that this process is not yet sending the phone numbers to the Messaging lookup
service, we're just trying to identify any numbers that need to be looked up.


There are a few points to consider here:


This process will create Phone Number Lookup records in your org.
There will only be one Phone Number Lookup record for each unique phone number that is
found. If you have a particular phone number that exists on more than one record, there will
only be one Phone Number Lookup record created for that phone number.
This process will normalize the phone numbers into E.164 format which means that if you've
entered the same phone number in multiple variations, Messaging should be able to account
for that and still only create one Phone Number Lookup record. For example, Messaging will
treat 555-555-5555, (555) 555-5555, 555.555.5555, 5555555555 to be the same phone
number and put it into the format of +15555555555.
The Status of these Phone Number Lookup records will be set to "New".
Any phone numbers that are found to exist on a record that has opted-out (Do Not SMS =
true) will be agged. This will prevent them from being looked up in the subsequent step.


Step 2: Purchase Lookups


After you run the rst step to nd new phone numbers, you will need to ensure that you have an
adequate amount of phone number lookup credits on your balance. Each phone number that is
successfully looked up will deduct one lookup credit from your balance.

You can easily purchase lookups by clicking the Purchase Lookups button shown above. If you do not
have an adequate amount of lookup credits on your balance you won't be able to proceed to Step 3.


Step 3: Lookup Numbers


Start the nal step in the process by clicking the Lookup Numbers button. At this point, all of the
phone numbers that have been calculated as part of the Ready to Lookup set will be processed
through the Messaging lookup service. The results will be updated back onto the Phone Number
Lookup records that were created in Step 1.

The length of time that it takes this process to complete will depend on the amount of phone numbers
that are being processed. For large datasets > 100K phone numbers, it could take several hours to
complete. You will see the job progress information in the middle of the page once this job starts. You
can always leave the page and come back to monitor the progress. An email noti cation will be sent
once the process is complete.


Lookups with Bulk Messages
When you send a bulk message, either from a List View or a Campaign, you will now see a checkbox
labeled Ex c lude Landlines and Bad Numbers . This box will be checked by default. When you send
the bulk message each phone number that's either a landline or a bad/invalid number will be skipped.
This makes it very simple to prevent you from unnecessarily wasting messages from your balance.

For this feature to work properly you must have already performed a lookup on your phone numbers,
either using the batch process or through an automation. Phone numbers will not be looked up at the
point of sending the bulk message. The bulk message will leverage the existing Phone Number Lookup
data that exists at the time you send the text.


Lookups and Individual Messages
The Blackthorn Messaging Messenger component will leverage your Phone Number Lookup data in a
few new ways.


Display phone number types in the To drop-down.
Alert you if you try to send a text to a landline (optional).
Automatically lookup a phone number when you send a text (optional).

Let's look at each one.

The component can now display the phone type next to each phone eld listed in the To drop-down.
This will help you quickly identify which phone numbers are not capable of receiving SMS.

When you're selecting a phone eld to send a text message to, you will see one of the following icons:


This indicates the phone number is either a Mobile or VoIP number. Mobile phone numbers are SMS-
capable and are the type of phone numbers associated with a recipient's mobile phone. VoIP phone
numbers are typically SMS-capable and are associated with an internet phone service, such as Google
Voice, Skype, etc.


This indicates the phone number is a landline. This is a business, home phone, or a phone number that
is otherwise incapable of receiving SMS.


This indicates the phone number has not been looked up, yet. Thus, we cannot determine what type of
phone number it is. You would need to perform a lookup on the phone number before one of the
above icons would be displayed.

You can turn on a setting that will alert you if you try to send a text to a landline. You will see a pop-
up that lets you cancel sending the message.


You can turn on a setting to enable automatic lookups. When you send a text to a number that has not
been looked up, it will rst perform a lookup on the phone number. If the phone number is a landline,
you will see a pop-up alerting you and allowing you to choose to proceed or cancel. If the phone
number is not a landline the text message will be sent.


Campaigns
Con gure Campaigns
Send a Bulk Message from a Campaign
Campaign Response Rules


Campaign Response Rules
In text messaging, automated conversations give you the ability to conduct a back-and-forth text
message conversation with a recipient without having to manually send messages. Automated
conversations can collect information from your recipient and update Lead or Contact elds with the
data from the recipient’s responses. They are used in conjunction with keyword campaigns and
templates. The best way to understand how automated conversations work is to look at an example.

In the example below we’ll look at how to build an automated conversation that collects the rst
name, last name, and email address of someone who opts into our campaign.


Con gure Campaign Page Layout
You will need to add a button and a eld to your Campaign page layout.


1. Go to Setup > Customize > Campaigns > Page Layouts.
2. Click Edit next to the page layout you want to con gure.
3. Add the button named SMS Response Rules.
4. Add the elds named Phone Number , Phone Number (Display) , SMS Keyword , Enforce

Single Conversation .

5. Save the layout.


Create Response Templates
Automated conversations rely on templates for the actual message that will be replied. It’s important
to note that, since both Leads and Contacts can be associated with a Campaign, you should create
both a Lead template and a Contact template for each response.

In this example, our conversation will have three responses so we’ll need six templates in total.

The templates will be as follows:


Name                                                    Body
Promo Campaign             Thanks for signing up for our Promo campaign! Please reply with your
Response 1 (Lead)          First Name and Last Name so I know how to refer to you.
Promo Campaign             Thanks for signing up for our Promo campaign! Please reply with your
Response 1 (Contact)       First Name and Last Name so I know how to refer to you.
Promo Campaign             Great! Hi {!FirstName}, we’re almost done. Please reply with your email
Response 2 (Lead)          address so we can send you more info about this offer.
Promo Campaign             Great! Hi {!FirstName}, we’re almost done. Please reply with your email
Response 2 (Contact)       address so we can send you more info about this offer.
Promo Campaign             Got it. Look for an email soon at {!Email}. Look forward to speaking with
Response 3 (Lead)          you. If you gave any wrong info just reply PROMO.
Promo Campaign             Got it. Look for an email soon at {!Email}. Look forward to speaking with
Response 3 (Contact)       you. If you gave any wrong info just reply PROMO.

Now that our templates are created it’s time to create the response rules.


Add Response Rules
In order to add these responses to our Promo campaign, we need to do the following:

1. Navigate to the Promo campaign record.
2. Click the SMS Response Rules button. This opens a new page where we will build the
responses.
3. Click the Add Rule button. This will open a dialog box where we will create the rst rule. The
following elds are available on the rule creation page:
Order: the order in which the rule executes (i.e. 1, 2, 3, etc)
Save the Lead Response: The eld to save the recipient’s response if the recipient
is a Lead.
Save the Contact Response: The eld to save the recipient’s response if the
recipient is a Contact.
Auto-Response for Leads: The template to reply with if the recipient is a Lead.
Auto-Response for Contacts: The template to reply with if the recipient is a
Contact.


Populate Fields for the First Response Rule
Order: 1
Save the Lead Response: None. Since the rst message received is the campaign keyword
there’s no need to save the response.
Save the Contact Response: None. Since the rst message received is the campaign
keyword there’s no need to save the response.
Auto-Response for Leads: Promo Campaign Response 1 (Lead)
Auto-Response for Contacts: Promo Campaign Response 1 (Contact)


Populate Fields for the Second Response Rule
Order: 2
Save the Lead Response: Name. This saves the response into the Name eld.
Save the Contact Response: Name. This saves the response into the Name eld.
Auto-Response for Leads: Promo Campaign Response 2 (Lead)
Auto-Response for Contacts: Promo Campaign Response 2 (Contact)


Populate Fields for the Third Response Rule
Order: 3
Save the Lead Response: Email. This saves the response into the Email eld.
Save the Contact Response: Name. This saves the response into the Email eld.
Auto-Response for Leads: Promo Campaign Response 3 (Lead)
Auto-Response for Contacts: Promo Campaign Response 3 (Contact)

This concludes the creation of our response rules. We’re now ready to start auto-conversing.


Pulling It All Together
Now that we’ve nished building our response rules, let’s look at how the automated conversation
works!

Let’s say someone texts in PROMO to your campaign phone number. We’ll assume the phone number
is new and the incoming message is not matched to any record in Salesforce. A new Lead is created
with default information (assuming the Auto-Create Leads option is enabled). The Lead will be
associated with the Promo Campaign and the automated conversation will start.

By setting up a keyword campaign with an automated conversation, we’ve achieved the following:


Captured a new Lead
Associated the new Lead to a Campaign
Populated the First Name, Last Name, Mobile Phone, and Email of the new Lead

All of this was accomplished without any live interaction on our part.


Con gure Campaigns
You can send a bulk message to all of the Campaign Members on your Campaigns. This article will
cover how to con gure the Campaign object for bulk sending.


Add Custom Fields
There are four elds that you should add to your Campaign page layout.


Phone Number (simplesmsPhone_Numberc)

Phone Number Display (simplesmsPhone_Number_Displayc)

SMS Keyword (simplesmsSMS_Keywordc)

Enforce Single Conversation (simplesmsEnforce_Single_Conversationc)


We suggest creating a new "Messaging" section on your page layout and adding these four elds to it.


Add Custom Button
Add the custom button named Send SMS. You may see multiple Send SMS buttons, so hover over
them to nd the one with the API Name of simplesms__Send_SMS_ltng. This is the button you
should drag and drop onto your page.


Send a Bulk Message from a Campaign
In this articles we'll explore how to send a bulk message to a list of Campaign Members from a
Campaign.


Add a Phone Number to the Campaign
The rst step is to determine which phone number you'll send the text from. You'll need to choose one
phone number and every message in the Campaign will be sent from that phone number. The Phone
Number that you want to send from must be marked as Available for Campaign on the Phone
Number record.


Start the Campaign Wizard


To begin building your text message, just click the Send SMS button. When you click this button you
will be presented with the Campaign Wizard. This is where you input your message (or use a template)
and preview your message before sending.

NOTE: There is no limit for the number of Bulk SMS messages sent from the Campaign Wizard.


Automation
Use the Process Builder to Send an Automated Text Message
Use Flow to Automate Outbound Text Messages
Work ow Messaging


Use the Process Builder to Send an
Automated Text Message
Watch this video tutorial on using Blackthorn Messaging's invocable apex action in the Process Builder
to send an automated text message.


The Messaging managed package includes an invocable Apex action that sends an outbound text
message. Invocable Apex can be used within your Process Builder and Flows.

When setting up a process in the Process Builder, at the point in your process where you want to send
the text message, do the following:


1. Click Add Action.
2. Select Apex.
3. Name your action.
4. Select "Send Messaging Message" from the Apex Class        eld.


Required Fields
You will then be prompted with four required elds:


From Phone: the phone number that the text message will be sent from. This must be one of
your text-enabled phone numbers provisioned through Messaging.
To Phone: the recipient's phone number.
Parent Id: the Id of the record to relate the SMS Message record to. The Parent Id record will


also be used to gather any merge data referenced in a template. For example, if you are
sending a text to a Lead and using a template that merges data from that Lead, then you
would put the Lead Id into this eld.
Owner Id: the Id of a Salesforce user or queue that will own the SMS Message record.


Additional Fields
Template Code: when using an SMS Template for your outbound text message, enter the
template code into this eld. To nd the code, go to the SMS Template that you want to use
and copy the value from the Code eld. It will look something like this "Lead-1234".
Message: if you do not want to use a template you can enter the wording for your text
directly into this value.
Timezone Id: if you have a template that merges in a date/time eld, you can set the time
zone that the date/time is converted to. If you do not set at TimeZone Id then your template
will display the date/time in GMT. For example, if you want to convert to Eastern Daylight
Time you would enter America/New_York. See here for a list of supported time zones -
Supported Time Zones
Additional Parent Field Name: you can relate the SMS Message record to a second record.
Enter the name of the eld on the SMS Message object that you want to populate. For
example, if you are sending a text message to a Contact but want to also relate the SMS
Message to the Account, you can populate this eld with a value of simplesmsAccountc. This
is the API name of the Account lookup eld on the SMS Message object.
Additional Parent Id: this is used in conjunction with the Additional Parent Field Name. Enter
the Id of the record that you want to relate the SMS Message to. Using our example from
above, you would create a eld reference to [Contact].AccountId to input relate the SMS
Message to the Contact's Account.

The Template Code and Message        elds are mutually exclusive. You should only populate one of
them, not both. If both are populated then the Template Code will take precedent.


Use Flow to Automate Outbound Text
Messages
Watch this video tutorial on using Blackthorn Messaging’s invocable apex action in a Flow to send
automated text messages. In this example, we'll build a daily recurring "Happy Birthday" text message.
The Flow will run every day and send a text to any Contacts who have a birthday on that day.


Messaging Send Message Flow
To prevent "SOQL queries: 101 limit error" errors when trying to send SMS messages using a ow
with the Apex Class, we created a new ow called Blackthorn Messaging Send Message(Flow).


Flow Con guration


Entry Criteria De ned on Account Object


Get a Contact Record from the Account


Looping the Process to Handle Contacts


De ne the Variables to get Data from the Contact Record


Recipient Variable


Collect Contact Records into a Collection Variable


Call the Apex Method to Send SMS to the Valid Contact
Records


Migrate Work ow Rules to Flow
Work ow Rules have been converted to Flows to provide the bene ts listed below.

Better Performance
The ability to re ne and streamline high-volume automation via features like Run
Asynchronously, Fast Field Updates (Before Save), and Entry Conditions.
Improved error handling, troubleshooting, and debugging
Click into the ow from an error email and see the path that was run.
Try different record updates straight from the debugger in triggered ows.
See how their governor limits will be impacted while debugging.
Exceptional extensibility with invocable actions and sub- ows
Users can package pieces of automation, either in Flow or Apex, to create building
blocks that empower Admins and standardize common interactions.


New Messaging Flows

SMS Message Record Actions and Related Record
1. Trigger: The ow starts when a new SMS Message (simplesms__ SMS_Message__c) record
is created.
2. Decision Check: The ow checks if the new message is of type "Incoming.”
3. Action: If it is an incoming message, an email alert is sent to the owner of the message.
4. End: If the conditions aren’t met, the ow takes no further action.

Summary: This Salesforce ow automates a process for sending an email alert to the owner of an
SMS message whenever a new "Incoming" SMS message is created. It ensures that owners are
noti ed promptly when they receive new messages, improving responsiveness.


SMS Campaign Response Rule Record Fast Field Updates
1. Trigger: The ow starts when a new SMS Campaign Response Rule
(simplesms__SMS_Campaign_Response_Rule__c) record is created or updated.
2. Decision Check: The ow checks if the A uto Respo nse T emplate (Co ntac t)
(simplesms__Auto_Response_Template_Contact__c) eld is lled or contains a new value.
3. Action on True: Set the A uto Respo nse Message Co ntac t
(simplesms__Auto_Response_Message_Contact__c) eld with the related A uto Respo nse
T emplate (Co ntac t) eld’s value (Auto_Response_Template_Contact__r.Body__c).


4. Decision Check: The ow checks if the A uto Respo nse T emplate (Lead)
(simplesms__Auto_Response_Template_Lead__c) eld is lled or contains a new value.
5. Action on True: Set the A uto Respo nse Message Lead
(simplesms__Auto_Response_Message_Lead__c) with the related A uto Respo nse
T emplate (Lead) eld’s value (Auto_Response_Template_Lead__r.Body__c).
6. End: If the conditions aren’t met, the ow takes no further action.

Summary: This Salesforce ow sets the value of the auto-response template body related to a Contact
or Lead if the template is selected in an SMS campaign.


SMS Message Record Fast Field Updates
1. Trigger: The ow starts when a new SMS Message (simplesms__ SMS_Message__c) record
is created or updated.
2. Decision Check: The ow checks whether the Fro m (simplesms__From_Num__c) eld was
changed or if it has a new value.
3. Action on True: Verify if the Fro m (simplesms__From_Num__c) eld has a length of 5
characters; if so, keep it as is. Otherwise, set the Fro m (simplesms__From_Num__c) eld to
the last 10 characters.
4. Decision Check: The ow checks whether the T o (simplesms__To__c) eld was changed or
contains a new value.
5. Action on True: Check if the T o (simplesms__To__c) eld has a length of 5 characters; if so,
keep it as is. Otherwise, remove the following characters: "(', ')", and "-" and set the T o
(simplesms__To__c) eld to the last 10 characters.
6. End: If the conditions aren’t met, the ow takes no further action.

Summary: This Salesforce ow automates setting the values of Fro m and T o based on the eld
length. If the length is 5, it remains unchanged. If it exceeds 10, only the last 10 characters are kept.


Number Lookup Status Record Actions and Related
Record
1. Trigger: The ow starts when a new Number Lookup Status
(simplesms__Number_Lookup_Status__c record is created or updated.
2. Decision Check: The ow checks whether the record is new or if its Status
(simplesms__Status__c) eld has changed to “Complete” or “Error.”
3. Action on True: Send an email to the current user to inform them that Blackthorn Messaging
has nished looking up phone numbers. (Textey Lookup Number Complete Noti cation)
4. End: If the conditions aren’t met, the ow takes no further action.


Summary: This Salesforce ow sends an email when the number lookup process is nished and the
Status is set to “Complete” or “Error.”


Old Work ow Rules - No Longer in Use

Email Owner When SMS Message Received
Criteria: (SMS Message: Message NOT EQUAL TO null) AND (SMS Message: Direction
EQUALS Incoming)
Description: It will send an email to the SMS message's owner when the SMS message is
received.


Number Status Success/Failure
Criteria: Number Lookup Status: Status EQUALS Complete,Error
Description: It will send an email to the Number Lookup State's owner when the Status
changes to either "Complete" or "Error".


Populate From Phone Field
Criteria: SMS Message: From NOT EQUAL TO null
Description: Updates the SMS Messages From Phone eld.


Populate To Phone Field
Criteria: SMS Message: To NOT EQUAL TO null
Description: It will update the SMS Messages To Phone eld.


Update Template Message Contact
Criteria: OR( ISNEW() ,ISCHANGED( simplesms__Auto_Response_Template_Contact__c ) )
Description: It will update the SMS Campaign Response Rule's Auto Response Message
Contact eld.


Update Template Message Lead
Criteria: OR( ISNEW() ,ISCHANGED( simplesms__Auto_Response_Template_Lead__c ) )
Description: It will update the SMS Campaign Response Rule's Auto Response Message
Lead eld.


Additional Features
Click to Call with CTI
Prohibit Sending Attachments (Custom Permission)
After Hours Response
Schedule SMS Messages
Schedule Jobs for Admin
Improved File Management for MMS Attachments
A2P Form in Admin Page
Sticky Sidebar in the Inbox
Number of Conversations to Load in Inbox
Number of Conversations in the Messenger
Con gure Default and Excluded Phone Fields by Object
Set a Default from Number
Filter your Inbox Using Conversation List Views
Auto Recharge your Message Balance
Link Tracking
HELP and STOP Message Compliance
Manage Opt-outs


A2P Form in Admin Page
To support the new A2P Messaging routes we have included the required registration form directly in
the signup process located in the Messaging Administration page.

NOTE: Users must complete the A2P submission process for both Production and Sandbox orgs.


After Hours Response
You can’t reply to customers’ texts while you’re recharging at home. Instead, use after-hours auto
replies to let customers know when you and your team will be available for business text messaging.

After Hours Response work just like email auto replies. You can set up your business SMS platform to
send an SMS template when it receives customer messages during a certain time period. In this case,
the time period would be your out-of-of ce hours.

Messaging Administration > Phone Numbers > AFTER HOUR RESPONSE


Set Up an Auto Response Message
1. Go to the "Messaging Administration" tab.
2. Click the Phone icon, along the left navigation, taking you to the Phone Numbers page.
3. Click the Add Phone Numbers button.
4. Add a Phone Number by area code or by pattern.
5. Click on the Edit icon under the column "After Hour Response".
6. Select the associated Business Hours.
7. Provide a auto reply message (remember 160 character limit per SMS).
8. Click Save.


Auto Recharge your Message Balance
Never run out of messages again. You can now automatically add more messages to your account
when your balance falls below your desired threshold.

To enable this functionality, please complete the following steps:

1. Navigate to the Messaging/Textey Administration tab.
2. Ensure that a Payment Method is added in the Account Information section.
3. Click the SMS icon.
4. Set Auto-recharge to "TRUE".
5. Select a Payment Method and the upper and lower limits for adding new messages.
6. Click Save.

This functionality is available on recent releases of the application. If you are unable to view the elds
listed in the steps above, it may require an upgrade to the Messaging Application. We recommend
upgrading your sandbox environment and testing rst before upgrading your live production
environment.


Click to Call with CTI
In this article, we'll explore the feature that allows users to call within Salesforce!


What happens when CTI is disabled?
When the CTI option is disabled, you won’t be able make any calls. A line over the phone icon also
indicates that this feature won’t work.


When the CTI option is enabled, the phone icon and phone number will appear as indicated below.


Enable CTI in Salesforce
1. Go to Setup.
2. In the Quick Find box, search for and click "Call Centers."
3. Open a Call Center App. (if installed eg: Zoom Phone Call Center)
4. Click Manage Call Centers Users.
5. Add a user to the App.
6. Log in to Blackthorn Messaging as the assigned user.
7. Click the Phone Number from Messaging Conversations and make your call.

Let's have a quick look!


Watch video on YouTube
Error 153
Video player configuration error


Watch on


Con gure Default and Excluded Phone
Fields by Object
When sending text messages from a record you can now con gure which phone elds are displayed in
the To drop-down in the Messenger. Sometimes you'll want to default a certain eld and even exclude
some elds from showing up.


Filter your Inbox Using Conversation List
Views
This option opens up many more ltering options for your inbox. Create list views on the Conversation
object and use those list views for your inbox lters.


HELP and STOP Message Compliance
Before initiating an SMS campaign, there are certain compliance guidelines that you should be aware
of. Wireless carriers require certain information to be included in HELP and STOP message content for
all US short codes.


We recommend handling those keywords for your long codes (10-digit phone numbers) also.


The recommended best practice is to include information in the following format. This ensure that your
HELP and STOP messages are considered compliant if your number is tested by a carrier.


HELP Message
A compliant response is required whenever users text HELP or INFO to one of your phone numbers.

Here’s an example:


End User: HELP or INFO
Response: {Company Name} {Description}. Help at {Email} or {Phone Number}. Msg&Data
rates may apply. {Message frequency}. Text STOP to cancel.
The “description” should be a single word that de nes the type of messages. For
example, “Sales”, “Support”, or “Promo”.
The “email” should be a business email like support@blackthorn.io.
The “phone number” should be a business phone number like your main of ce
phone number.
The “message frequency” must be speci c but can be any interval. For example, “1
msg per day”, “4 messages per month”, etc. If the message frequency will vary
based on user interaction, you can use “1 msg per user request”.

You should con gure a HELP message for each phone number that is provisioned to your account. You
can do this by going to the Phone Number record and typing your message into the Help Message
eld.

This way, whenever someone texts the words HELP or INFO to that phone number, Blackthorn
Messaging will reply automatically with your help message.


STOP Message


A compliant response is required whenever users text STOP, END, CANCEL, UNSUBSCRIBE, or QUIT
to one of your phone numbers.

Here’s an example:

End User: STOP, END, CANCEL, UNSUBSCRIBE, QUIT
Response: You are unsubscribed from {Company Name} alerts. No more messages will be
sent. Reply HELP for help or {Phone Number}.

You should con gure a STOP message for each phone number that is provisioned to your account. You
can do this by going to the Phone Number record and typing your message into the Stop Message
eld.

Whenever someone texts the words STOP, END, CANCEL, UNSUBSCRIBE, or QUIT to that phone
number, Messaging will auto-reply with your help message. Messaging will also check the Do Not
SMS checkbox on the related parent record.


Do you need to change the consent popup frequency?

Click here to learn how to con gure how frequently an SMS consent popup will be displayed.


How Do I Increase our Message Balance?

Add Messages
To add additional messages to your balance, you can do the following:


1. In Salesforce, go to the Messaging Administration page.
2. Navigate to the SMS section (SMS icon on the left-hand side).
3. Click the Add Messages button.
4. Enter the Quantity of messages you want to purchase. You will see a con rmation of the
price for these additional messages.
5. Click Checkout.
6. Con rm your payment method and click Buy Messages.

If the payment is processed successfully, your messages will be immediately added to your balance
and your account will be placed back into "Active" status.


Update Your Payment Method
Users can change the Payment Method at any time.


Update a Card’s Information
1. Click the Add Card button.


2. Update the First Name , Last Name , Card Number , Ex piry Date , CV V , or address
elds.


3. Click Add Card.


Change the Default Payment Method
1. Click Choose Default Payment.
2. Select a Payment Method.
3. Click Save.


4. Once a card is set as the default Payment Method, it will remain the default Payment Method
until changed.


Delete a Payment Method
Users cannot delete a card that is set as the default Payment Method or is con gured for auto-
recharge. Any other saved Payment Method can be deleted.

1. Click the card you want to delete.
2. Click Con rm.


Improved File Management for MMS
Attachments
Now you can leverage Salesforce Libraries to control and manage which les can be sent in text
messages.


Link Tracking
Have you ever wondered how effective your SMS campaigns are? One great way of doing this is to
add a trackable URL to your message. Blackthorn Messaging comes complete with a feature called Link
Tracking that allows you to do just that!

Link Tracking works by automatically shortening the URLs in your message into a trackable URL that is
unique to each message. This feature works for any message that contains a URL, whether it’s a single
message, bulk message, work ow message, or campaign message. When you send a bulk message
that contains a URL, each individual message will receive its own unique trackable link.

Tracking the clicks you receive on your SMS campaigns is important because it differentiates this from
the website traf c that your receive through other marketing campaigns.

When a recipient clicks on the trackable link, they will be redirected to the original URL and the click
will be tracked. The SMS Message record will be immediately updated in Salesforce.


Only URLs that begin with http:// or https:// will be shortened. If you do not want a link to be
tracked, simply omit the http:// or https://.


Enable Link Tracking
To utilize the Link Tracking feature, the feature must be enabled in the app settings rst.


1. Click on Messaging app in the dropdown on the top right hand corner.
2. Navigate to Administration tab.
3. Click on Con guration Settings in the Account Management page.
4. Ensure the Enable Trackable Links option is enabled. If this is not enabled, none of your
links will be shortened.


Send a Message with a URL
Let’s try sending a message to a Contact that contains a link to Blackthorn’s website.


1. Go to the speci c record.
2. Click Send SMS.
While the message contains the URL https://www.blackthorn.io, the recipient will see a
shortened version. The unique set of characters at the end of the shortened URL tracks the
link back to this particular message. When the recipient clicks on the link, they are redirected


to the original URL.

Now, let’s take a behind-the-scenes look at the speci c SMS Message record in Salesforce to see how
the link tracking works.

You will notice that the following elds in Link Tracking Info section have been updated.


Clicks: the number of times the link was clicked by the recipient.
First Click: a time stamp of the rst click on the URL
Last Click: a time stamp of the last click on the URL
Links Clicked: the original URL of the link that was clicked
Short Links: the shortened URL

You can set work ow rules that alerts you when the URL is clicked. Alternatively, you can run reports
that show all messages when the number of clicks are greater than zero.


Manage Opt-outs
Whenever someone texts one of the STOP keywords to one of your phone numbers, the Do Not SMS
checkbox eld will be checked on the parent record.


Single Phone Numbers
For example, someone texts STOP from 555-555-5555 and the incoming message is matched to a
Contact named John Doe. The Do Not SMS checkbox will then be checked on John Doe’s Contact
record. When the Do Not SMS checkbox is checked on a record, Blackthorn Messaging will not let you
send a message to that record.

The rst image below shows a Contact where the Do Not SMS checkbox is checked. The second
image shows the message that will be displayed when you attempt to send a message to that
Contact.


Bulk Messaging
When you send a bulk message or a campaign message, any records that have the Do Not SMS
checkbox checked will be skipped and no message will be sent to those records.


Number of Conversations in the
Messenger
For better performance in the Blackthorn Messaging Messenger component, you can set a default page
size of the number of messages that load when the component loads.


Number of Conversations to Load in Inbox
For better performance in the Blackthorn Messaging Inbox, you can set a default page size of the
number of Conversations that load when the Inbox loads.


Prohibit Sending Attachments (Custom
Permission)

Disallow Users from Sending Attachments in
Messages (Custom Permission)
In the new January '22 release, we introduced a Custom Permission that controls which users are
allowed to send attachments in their SMS messages.


Prevent Users from Sending Attachments in
Messages (Custom Permission)
1. Go to Setup.
2. Create a new Permission Set.
3. Assign one or more users to the Permission Set.
4. Apps > Custom Permissions.
5. Click Edit.
6. Add the Custom Permission: "simplesms.Prevent Textey Attachments".
7. Click Save.

Now Login to the assigned user and check the Blackthorn Messsaging Messenger!


Schedule Jobs for Admin
Select a date and time in the future and rest assured that your message will be sent whether you're at
your desk or on the go.

Whenever a message is scheduled to be sent at a later time, whether a single message or bulk SMS,
all the messages will appear under the Scheduled Jobs.

Messaging Administration -> Con guration Settings -> Scheduled Jobs


Actions to Perform on Scheduled Jobs
Start: To begin or set out the scheduled job for individual messages.
Stop: Puts a pause to the scheduled job, which will cease all the individual planned messages
from sending.
Delete: Cancels or removes the scheduled bulk SMS from sending. You cannot restart it once
you delete the bulk SMS schedule.


Note: The individually scheduled messages will automatically get started/resumed if any user sends an
SMS from the Blackthorn Messaging Messenger.


Actions to Perform on Scheduled Messages
An insight of all the messages scheduled individually. You can separately perform additional actions on
these messages.


Edit Message: Change the body of the message
Reschedule Message: You can schedule the message for another time
Send Now: Sends the message right away
Cancel Message: Calls off the message
Delete Message: Removes the message


Schedule SMS Messages
If you haven't done so already, please review the steps for starting and stopping scheduled jobs and
messages.

SMS Messages can be scheduled via two interfaces.


Record Page Messenger
Bulk SMS


Which Message eld should I use?

End users will see the message in the Message (Full) eld. They won’t receive the message in
the Message eld. Understanding this is especially important for messages over 256 characters,
which will appear cut off in the Message eld.


Record Page Messenger


An insight of all the messages scheduled individually. You can separately perform furthermore actions
on these messages.


Edit Message: Change the body of the message
Reschedule Message: You can schedule the message for another time
Send Now: Sends the message right away
Cancel Message: Calls off the message
Delete Message: Removes the message


When you are not the owner of the messages that are scheduled, you will not be able to view them or
perform any actions.


Bulk SMS


Do you want to send SMS messages from an Event?

If you have Messaging installed and would like to send SMS messages from an Event using the
Smart Scheduler, click here.


Set a Default from Number
When a user has access to send text messages from multiple phone numbers, they can now choose
which one shows as the default.


Short Codes

Paid Feature

Short Codes is a paid add-on. Please contact Blackthorn Support for more information.


A short code is a shorter telephone number used to send and receive SMS and MMS messages
between mobile phones.

You may want to use short codes instead of a traditional ten-digit number to send large volumes of
messages in a short amount of time. Since short codes are pre-approved by carriers, they are less likely
to be labeled as spam.

While Blackthorn can initiate the short code application for you via Twilio, please review our
recommended reading rst.


United States
US Industry Standards: CTIA Short Code Monitoring Handbook
Messaging Principles and Best Practices
Twilio Opt-in Process


Canada
Canadian Industry Standards
CSC Code of Conduct
Twilio Opt-in Process
French-language requirements for Canadian Short Codes


United Kingdom
UK Industry Standards
Twilio Guidelines
Requirements for UK Short Codes


Industry Standards Note


Complying with industry and compliance standards for your location is crucial. It is your responsibility
to understand and comply with them. Please consult with your legal counsel to ensure you meet your
local requirements.


Smart Scheduler


Which Blackthorn Apps Do You Use?

The Smart Scheduler component can be used with our Events app, Messaging app, or both! If
you are only using Events, ignore the steps about updating Messaging and Messaging’s
permissions.

If you want to learn more about our Messaging app, please contact your account manager!


Sticky Sidebar in the Inbox
If you open the sidebar on the Blackthorn Messaging Inbox, it will remain open as you click into
different conversations.


Track Phone Number Opt-ins
The date and time that an SMS message recipient gives consent will be recorded on the record page.

To see the new settings, go to Messaging Admin Tab > Con guration Setting > Messaging Tab.


Under the Outbound Message Settings heading, the Consent Settings now includes the
Co nsent P o pup Frequenc y     eld with the “Once per Recipient (Opt-In)” option.
Select the object that you want to capture the consent date and time. By default, all objects
con gured to send SMS will be selected.
When Co nsent P o pup Frequenc y is set to “Once per Recipient (Opt-In),” you will see the
following pop-up message.
“Please make sure you have created the eld SMS Optin DateT ime on the
selected Objects before enabling this setting or else the consent date time will not
get captured. See our documentation for more info.”


Expected Behavior

If the SMS Optin DateT ime eld value is blank, message recipients will receive an SMS
Consent pop-up modal since consent is happening today.
When a message recipient selects the checkbox and clicks the Send button, the current date
and time will populate the SMS Optin DateT ime eld.
If no conversation record exists, the Consent Signature will be appended to the message
since it is happening today.
If the SMS Optin DateT ime eld is not blank, then message recipients will not see the
SMS Consent pop-up modal, and the SMS will be sent.
If the SMS Optin DateT ime eld has a future date, then message recipients will see the
SMS Consent pop-up modal.
When a message recipient selects the checkbox and clicks the Send button, the current date
and time will replace the future date in the SMS Optin DateT ime eld.
The following will occur if the Task trigger or Invocable Method is used to send SMS.
If the SMS Optin DateT ime eld is blank, the recipient will not receive the SMS.
The SMS Message record will not be created when Status = “Error.” The


error message will be “This person has not Opt-In for SMS
communication.”
If the SMS Optin DateT ime eld has a value, recipients will receive the SMS.
If the SMS Optin DateT ime eld contains a future date, the recipient will not
receive the SMS.
The SMS Message record will not be created when Status = “Error.” The
error message will be “This person has not Opt-In for SMS
communication.”


Upgrade the Messaging App

Which Blackthorn Apps Do You Use?

The Smart Scheduler component can be used with our Events app, Messaging app, or both! If
you are only using Events, ignore the steps about updating Messaging and Messaging’s
permissions.

If you want to learn more about our Messaging app, please contact your account manager!


1. Go to the Candy Shop.
2. Click Blackthorn Messaging.
3. Click Product Upgrade.
4. Click Login to Install.
5. Select “Production or Developer Org” or “Sandbox or Scratch Org.”
6. Complete the login process.
7. Click Install.
8. Review the Product Terms of Use and Licenses.
9. Check the “I con rm I have read and agree to these product terms of use and licenses”
checkbox.
10. Click Con rm.

After the upgrade process completes, you will receive an email con rming that Messaging has been
installed.


Upgrade the Blackthorn Base, Payments,
and Events Apps
The Smart Scheduler, which is now located in the Blackthorn Base Package, is available via the
Blackthorn Candy Shop. Messaging customers can now use Smart Scheduler without downloading the
Events or apps.


Before installing and setting up the Smart Scheduler component, the Blackthorn Base Package,
Payments, and Events apps must be upgraded to their most recent versions. Since upgrading the
Events app triggers the Payments app and Base Package to upgrade, you do not need to upgrade each
one separately.


1. Go to the Candy Shop.
2. Click Blackthorn Events.
3. Click Product Upgrade.
4. Click Login to Install.
5. Select “Production or Developer Org” or “Sandbox or Scratch Org.”
6. Complete the login process.
7. Click Install.
8. Review the Product Terms of Use and Licenses.
9. Check the “I con rm I have read and agree to these product terms of use and licenses”
checkbox.
10. Click Con rm.


After completing the upgrade, you will receive three emails con rming that Blackthorn Base Package,
Events, and Payments have been installed.


Are you creating a new sandbox?


A new API Key and Account Number are required each time a new sandbox is created, and
Smart Scheduler is being used. If new credentials are not obtained, the original API Key and
Account Number will be copied from Production, breaking the Production org.


Refreshed sandboxes with con gured credentials from Support will work as expected.


Known Limitation: If a new sandbox is created, BUT Smart Scheduler isn’t being used, a new
API Key and Account Number are still needed. If new credentials are not obtained, production
emails won’t be sent because two orgs have the same API Key and Account Number.


Which Blackthorn Apps Do You Use?
The Smart Scheduler component can be used with our Events app, Messaging app, or both! If you only
use Events, ignore the steps about updating Messaging and its permissions.

If you want to learn more about our Messaging app, please get in touch with your account manager!


Assign New Permission Sets
After upgrading the Payments and Events, assign new permission sets to users so they can use the
new components and features.


Blackthorn | Base (Admin): This permission set allows users to register a Smart Scheduler
Account and authenticate the user. The user also has access to all components including the
ability to schedule and send Global and Record Level SMS and email.
Blackthorn Base User: This permission set allows users to access components including the
ability to schedule and send Global and Record Level SMS and email.

Complete the steps below to assign the permission sets.


1. Click the Gear icon.
2. Click Setup.
3. In the Quick Find box, enter and click “Users.”
4. Click the name of the user whose permissions need to be updated.
5. On the user’s record, scroll down to the Permission Set Assignments.


6. Click Edit Assignments.
7. Add the permission sets related to Base (Blackthorn | Base (Admin) or Blackthorn | Base
(User)), Payments, and Events.
8. Select the Assignments as shown below and add them.


9. Click Save.


Create an Org-wide Email Address
Occasionally, an organization-wide or alias email address may be needed to allow users to send emails
from the Essentials Edition.

Complete the steps below to set up an org-wide email.

1. Click the Gear icon.
2. Click Setup.
3. In the Quick Find box, enter and click “Organization-Wide Addresses.”
4. Click Add.
5. Enter a Display Name and Email A ddress .
6. Select either A llo w A ll P ro f iles to U se this Fro m A ddress or A llo w Only Selec ted
P ro f iles to U se the Fro m A ddress . If you select the latter, choose the pro les you want
to add.
7. Click Save.

A veri cation email will be sent to the newly created org-wide email address. Once the org-wide email
address has been veri ed, it will be available to the assigned pro les.


Update Permission Sets for the Messaging
App
After the Messaging app is upgraded, assign permission sets to users so they can use the new
components and features. (If the permission sets are not already assigned.)

Complete the steps below to assign the permission sets.


1. Click the Gear icon.
2. Click Setup.
3. In the Quick Find box, enter and click “Users.”
4. Click the name of the user whose permissions need to be updated.
5. On the user’s record, scroll down to the Permission Set Assignments.
6. Click Edit Assignments.
7. Add the permission sets related to the Messaging app. (Blackthorn Messaging Admin User,
Blackthorn Messaging Lightning User, and Blackthorn Messaging Standard User)
8. Select the Assignments as shown below and add them.


9. Click Save.


Start Here

Add the Smart Scheduler Admin Tab
Once the component is installed, add the Smart Scheduler Admin tab to the Messaging navigation bar
using one of the following methods.


1. Go to the Messaging app.
2. Click the App Launcher.
3. Enter and click "Smart Scheduler Admin".


4. Click the Down icon on the Smart Scheduler Admin tab.
5. Click + "Add Smart Scheduler Adm"... to Nav Bar".


OR


1. Go to the Messaging app.
2. Click the Pencil icon in the navigation bar.
3. Click Add More Items.


4. Click the All tab.
5. Search for "Smart Scheduler Admin".
6. Check the box next to "Smart Scheduler Admin".


7. Click Add 1 Nav Item.
8. Click Save.


Next Steps
1. Register your Account
2. Authenticate a User
3. Add the BT Event Scheduler Component to the Event Record


Register Your Account

Are You Using a Sandbox or Dev Org?

If you are using a sandbox or dev org and haven’t already contacted us, please contact
Blackthorn Support to provide the following before proceeding.

Organization name
Org id
Org type (production or sandbox/dev org)
Primary email address
Whether you want to enable just Email (for Events only customers) or Email +
Messaging (for Events & Messaging customers)

IMPORTANT: Customers with new sandboxes need to contact Blackthorn Support for a unique
API Key & Account Number. Reusing an API Key & Account Number from a different sandbox or
a production org prevents Smart Scheduler from working since the con guration (API Key &
Account Number) is uniquely set per org ID.


Registering your account allows us to identify your org on the server and provide security. Your account
number and API key allow us to authenticate subsequent calls and associate created schedules with
your account. A registered account is also required for Org level control for the following areas.

Primary Communication Address
Feature Flags
N days before noti cation con guration
Any futuristic attribute

To register your account, please complete the steps below.

1. Click No, I need an account.


2. Review the Product Terms of Use and Licenses.
3. Check the “I con rm I have read and agree to these product terms of use and licenses”
checkbox.


4. Click Activate Now.


Congratulations! Your Base account has been created.


Critical Step

Before proceeding to the next section, please contact Blackthorn Support with the newly
generated account number. Once the account is manually enabled, you will be able to continue.


Authenticate a User
After successfully activating the Scheduler component, you will need to activate or authenticate the
user.

1. Log in as the Salesforce user you want to authenticate.
2. Navigate to Blackthorn | Scheduler Admin using the App Selector.
3. Click Authenticate Me in the Authenticated User section.
4. Click Allow on the OAuth permissions page to grant access. You will be redirected to the
Scheduler Administration page.

If you need to change the authenticated user, click the delete (trash can) icon next to the authenticated
user’s email. Then log in as a different user and authenticate that user.


Add the BT Event Scheduler Component
to the Event Record
Complete the steps below to add Messaging’s Communication tab to your Event object.


1. Open an Event record.
2. Click the Gear icon.
3. Click Edit Page.


4. Click the “More” tab in the Event page layout.


5. Click Add Tab.


6. Click the new tab and select T ab Label = “Custom”.
7. Enter Custo m Label = “Communication”.


8. Click Done.
9. Move the Communication tab to the top of the Tabs list so First T ab = “Communications”.
10. Set Def ault T ab = “First Tab.”
11. In the left navigation pane under Components, search for “BT Event Scheduler.”
12. Click and drag the BT Event Scheduler component to the Communication tab.


13. Click Save.


14. Click Activate.
15. Click the App Default tab.
16. Click Assign as App Default.


17. Select “Events (Admin)” and “Events (Planner)”.
18. Click Next.
19. On the Assign Form Factor screen, choose your preferred platform, and click Next.


20. If everything looks okay on the Review Assignments screen, click Save.
21. Click Save.
22. Return to the Event record page.


To watch a video of the process, click here.


Activate the Smart Scheduler's Feature
Toggle
To activate the Smart Scheduler's Feature Toggle, you can either contact Blackthorn Support or follow
the steps below.


1. Go to Setup.
2. In the Quick Find box, enter and click "Custom Metadata Types."
3. Click Manage Records next to Blackthorn Feature Toggle.
4. Click Edit next to Smart Scheduler Activation Record.
5. Check the A c tiv e checkbox.


6. Click Save.
7. Return to the Blackthorn | Scheduler Admin tab.
8. Refresh the page.
9. You will be taken to the Account Registration page.


Messaging App Is Not Installed
Scheduler Admin
If the BT Messaging App is not installed in your Salesforce org, a warning message tells the user to
install the app in the Global Scheduler.


If the BT Messaging App is not installed in your Salesforce org, a warning message tells the user to
install the app in the Event Record Page Scheduler.


Scheduler User
The Scheduler User does not have access to the Administration Settings. When they land on the
Record Level Scheduler, a warning message tells them to contact the System Administrator.


Messaging App Is Not Con gured
Scheduler Admin
When the Messaging App is not con gured on a Global Scheduler after installation, a warning
message tells the user to con gure their Messaging Account.


The same warning message also appears on the Record Level.


Scheduler User
The Scheduler User does not have access to the Administration Settings. When they land on the
Record Level Scheduler, a warning message tells them to contact the System Administrator.


Custom Object Is Not Con gured for
Sending SMS
Complete the steps below to con gure a custom object for messaging.


1. Click the Gear icon in the upper right-hand corner.
2. Click Setup.
3. Click Create.
4. Click Objects.
5. Click SMS Message.
6. Click New in the Custom Fields & Relationships section.
7. Create a Lookup Relationship eld that is related to your custom object. In this example, we
used a custom object named Student.
8. Complete the remainder of the new eld wizard as you would for any new Lookup eld.
9. After the new Lookup eld is created, Messaging will detect the relationship. You can now
add the Messaging Messenger component to this object's pages. You will also be able to
create Templates for this object.

To send text messages to this object, add a Phone eld with Data T y pe = “Phone”. Messaging does
not detect phone numbers in text formula elds.


Scheduled Jobs from the Event Record
Complete the steps below.


1. Schedule an Email
2. Schedule an SMS
3. Manage Scheduled Jobs
4. Filter the Smart Scheduler List View


Schedule an Email

1. Go to the Event record that you want to schedule the email for.
2. Click the Communication tab.
3. Click New Message.


Recipients Section

1. Select Schedule “an Email”
2. Select “Event Attendees” or “Session Attendees”
3. Enter a Sc hedule Name .
4. Select a Fro m Email A ddress .
5. Select a T o Email .
6. Choose an A ttendee Filter .
If you set A ttendee Filter = “Attendance Status”, select the relevant options in
the A ttendanc e Status eld.
If you set A ttendee Filter = “Registration Status”, select the relevant options in
the Registratio n Status eld.
There must be at least one recipient listed in T o tal Rec ipients . If a zero is listed
under T o tal Rec ipients , check that you have the correct status selected and
review the Attendees that should have the chosen status.
7. Con rm that the amount under Email Balanc e is greater than the number of T o tal
Rec ipients .
8. Click Next.


Schedule Section

1. Choose one of the three options below to schedule your email.
Send the email at a speci c date and time
Choose the speci c date and time in the Selec t a Date / T ime eld.
Send the email X Minutes/Hours/Days After/Before the selected trigger.
Enter the number.
Choose “Days”, “Hours”, or “Minutes”.
Select “Before” or “After”.
Choose “Event Start Date/Time”, Event End Date/Time”, “Event Attendee
Registration Date”, or “Event Attendee Created Date”.
Select No w to send the email two minutes after the email is scheduled.
2. Click Next.


Message Section

1. In the Email T emplate eld, search for an existing Email Template or click Create New to
create a new one.
2. Click Next.


Send Test Section

1. Enter a T est Email(s) . Make sure to use an email that can be checked easily. Using your
email is a good option.
2. Select a T est Rec o rd .
3. Click Send Test.
4. After you receive the success message, click Schedule.

The schedule will now be visible under Schedule History on the Scheduler tab. Please refer to the
video for the process ow for sending an email.


Schedule an SMS

1. Go to the Event record that you want to schedule the SMS for.
2. Click the Communication tab.
3. Click New Message.


Recipients Section

1. Select Schedule “an SMS”
2. Select “Event Attendees” or “Session Attendees”
3. Enter a Sc hedule Name .
4. Select a country in the Send SMS Fro m eld.
5. Set Send SMS T o = “Phone”.
6. Choose an A ttendee Filter , if needed.
If you set A ttendee Filter = “Attendance Status”, select the relevant options in
the A ttendanc e Status eld.
If you set A ttendee Filter = “Registration Status”, select the relevant options in
the Registratio n Status eld.
7. There must be at least one recipient listed in T o tal Rec ipients . If a zero is listed under
T otal Recipients, check that you have the correct status selected and review the
Attendees that should have the chosen status.
8. Con rm that the amount under SMS Balanc e is greater than the number of T otal
Recipients.
9. Click Next.


Schedule Section

1. Choose one of the three options below to schedule your SMS.
Send the SMS at a speci c date and time
Choose the speci c date and time in the Selec t a Date / T ime eld.
Send the SMS X Minutes/Hours/Days After/Before the selected trigger.
Enter the number.
Choose “Days”, “Hours”, or “Minutes”.
Select “Before” or “After”.
Choose “Event Start Date/Time”, Event End Date/Time”, “Event Attendee
Registration Date”, or “Event Attendee Created Date”.
Select No w to send the SMS two minutes after the SMS is scheduled.
2. Click Next.


Message Section

1. In the Message Text box, enter the message that you would like to send.
2. Click Next.


Send Test Section

1. Enter a T est P ho ne Number(s) . Make sure to use a phone number that can be checked
easily.
2. Select a T est Rec o rd .
3. Click Send Test.
4. After you receive the success message, click Schedule.

The schedule will now be visible under Schedule History on the Scheduler tab. Please refer to the
video for the process ow for sending an SMS.


Manage Scheduled Jobs

Do not delete Scheduler records.

Instead, update the Scheduler Status to “Unschedule” or “Archive” via the Smart Scheduler
component.


The list of Email Scheduled Jobs is located under Schedule History on the Event Page. You can perform
several actions for each job in the List view, depending on the Status of that job.


When the Scheduler Status = “Draft”, the options are to “Edit” and “Archive” the job.


When the Scheduler Status = “Active”, the options are “Archive”, “Unschedule” and “View
Detail”.


When the Scheduler Status = “Inactive”, the only option is to “Archive”.


When the Scheduler Status = “Unschedule”, the job will be located on the History record. If
you select “Unschedule”, you will receive the following message and the job will be removed
from the list.


FAQ
Q: Can I migrate Schedule records from production to a sandbox?

A: No. When a Salesforce sandbox is refreshed from production, the sandbox will NOT contain the
existing Schedule records that are in production. You will need to manually create the Schedule records
in the sandbox.


Filter the Smart Scheduler List View

You can also lter the scheduled jobs using the lters on the Record Level Scheduler, as shown in the
picture below.


The available lters are

Action Type: Email, SMS
Schedule Type: Object, Record
Status: Active, Completed, Draft, Inactive
Include Archived (Toggle)

The lters are set to the following by default:


Action Type: Email, SMS
Schedule Type: Record
Status: Active, Draft
Include Archived (Toggle): Inactive


Scheduled Jobs from the Global Scheduler
Complete the steps below.


1. Schedule an Email
2. Schedule an SMS
3. Manage Scheduled Jobs
4. Check the Status of Each Sent SMS and Email
5. Filter the Global Scheduler List View


Schedule an Email

Important De nitions

What are the Base and Related objects?
Base Object = the container/parent record
Related Object = the audience inside the Base Object or “container or parent record” or who
should receive the message


When should I use the Global Scheduler?
The Global Scheduler provides users with additional Attendee lter options, such as V isibility
Co ntro l and Dietary P ref erenc e , to use as trigger elements.

The Event-level scheduler only sends an email to Event or Session Attendees based on the value in
one of two statuses: Registratio n Status or A ttendanc e Status .


Use Case Examples

Example 1: Invite Attendees across all Events
Base Object: Event (no criteria)
Related Object: Attendee with V isibility Co ntro l = “Member”
Result: Send a reminder email to all Attendees who are Members across all Events.


Example 2: Workshops this week with extra Attendee
lters
Base Object = Event with Ev ent Start Date = “this week” AND Catego ry = “Workshop”
Related Object: Attendee with Registratio n Status = Registered AND V isibility Co ntro l
= “Member”
Result: Send a message only to registered members who are attending workshops this week.


Schedule an Email
Let’s explore how to create a schedule and send an Email via the Global Scheduler.


1. Go to Blackthorn | Scheduler Admin > Administration > Messages.
2. Click New Message.


Recipients Section
1. Select Schedule “an Email”.
2. Choose a Base Object or parent record.
3. Choose a Related Object or who will receive the email.
4. Complete the mandatory elds.
Sc hedule Name
Fro m Email A ddress
T o Email
5. Enter lter criteria for the Base and/or Related Objects.
6. Click Next.

NOTE: Always de ne the Base Object (parent record) for the Related Object (recipient), regardless of
whether you are setting lter criteria for the parent.


Schedule Section
Enter the required information to schedule the email.


Message Section
There are two ways to create an email: use an Email Template or compose an email here.


Email Template

1. Select Template.
2. Select an Email T emplate
3. Click Next.


Compose Email

1. Select Compose Email.
2. Enter a Subjec t .
3. Enter a Bo dy .
4. Click Next.


Send Test Section
1. Enter a T est Email . Make sure to use an email that can be checked easily. Using your email


is a good option.
2. Select a T est Rec o rd .
3. Click Send Test.
4. After you receive the success message, click Schedule. Your recipients will receive the email
per the scheduled date and time.


Batch Jobs and Email Frequency
Batch jobs function similarly for the Global Scheduler and the Smart Scheduler (from the Event record).
The primary difference is that if the Email Noti cation Settings Co nso lidated email f requenc y is set
to “Once in a day,” the batch volume for the Global Scheduler can be much higher when many record
updates occur in a single day. This scenario will not occur with the Smart Scheduler.

If you want to update the Co nso lidated email f requenc y     eld, go to the Smart Scheduler Admin
tab, click the Con guration Settings icon in the left-hand navigation, and set Co nso lidated email
f requenc y to “Once in a day.”


Schedule an SMS

Let’s explore how to create a schedule and send an SMS via Global Scheduler.


1. Go to Blackthorn | Scheduler Admin > Administration > Schedule.
2. Click Create Schedule.


Recipients Section

1. Select Schedule “an SMS”.
2. Choose a Base Object.
3. Choose a Related Object.
4. Complete the mandatory elds.
Sc hedule Name
Send SMS Fro m
Send SMS T o
Provide any conditions (if any)
5. Click Next.


Schedule Section

Enter the required information to schedule the SMS.


Message Section

1. In the Message Text box, enter the message that you would like to send.
2. Click Next.


Send Test Section

1. Enter a T est P ho ne Number(s) . Make sure to use a phone number that can be checked
easily.
2. Select a T est Rec o rd .
3. Click Send Test.
4. After you receive the success message, click Schedule. Your recipients will receive the SMS
per the scheduled date and time.


Manage Scheduled Jobs

Do not delete Scheduler records.

Instead, update the Scheduler Status to “Unschedule” or “Archive” via the Smart Scheduler
component.


To see a list of scheduled jobs, go to Blackthorn | Scheduler Admin > Administration > Scheduled Jobs.
The list of Email Scheduled Jobs is in this list. For each job in the List view, you can perform a few
actions depending on the Status of that job.

When the Scheduler Status = “Draft”, the options are to “Edit” and “Archive” the job.


When the Scheduler Status = “Active”, the options are “Archive”, “Unschedule” and “View
Detail”.


When the Scheduler Status = “Inactive”, the only option is to “Archive”.


FAQ
Q: Can I migrate Schedule records from production to a sandbox?


A: No. When a Salesforce sandbox is refreshed from production, the sandbox will NOT contain the
existing Schedule records that are in production. You will need to manually create the Schedule records
in the sandbox.


Check the Status of Each Sent SMS and
Email
The ability to check the status of an individual message in a Scheduled Job is available. However, to
check the status of an individual message, the Scheduler Status must be “Active”.


SMS


EMAIL


Filter the Global Scheduler List View

You can also lter the scheduled jobs by using the Filters on the Record Level Scheduler as shown in
the picture below.


The available lters are:


Action Type: Email, SMS
Schedule Type: Object, Record
Status: Active, Completed, Draft, Inactive
Include Archived (Toggle)

The lters are set to the following by default:

Action Type: Email, SMS
Schedule Type: Object
Status: Active, Draft
Include Archived (Toggle): Inactive


Schedule Emails with SendGrid
Use SendGrid from the Events app to send scheduled emails that are created using the Smart
Scheduler.

For information about setting up SendGrid, please click here.


Pre-requisites
If you haven’t already set up Smart Scheduler, please complete the tasks on the following pages.


1. Upgrade the Messaging App
2. Upgrade the Blackthorn Base, Payments, and Events Apps
3. Assign New Permission Sets
4. Create an Org-wide Email Address
5. Activate the Smart Scheduler's Feature Toggle
6. Start Here
7. Register Your Account
8. Authenticate a User
9. Add the BT Event Scheduler Component to the Event Record


Add the SendGrid API Key in the BT Base App
1. Open the Events (Admin) app.
2. Click the Smart Scheduler Admin tab. (If you don’t see the tab, click here to review the steps.)
3. Click Add API Key.
4. Enter the SendGrid A P I Key .
5. Click Save.


Once the SendGrid A P I Key is available in the Events app, you can retrieve it from the Smart
Scheduler Admin tab by clicking Retrieve From Event App and use it in the BT Base app.


Settings

Turn On/Off the SendGrid Feature
You can turn on/off the feature that allows users to schedule SendGrid emails from the BT Base app.


1. Open to the Events (Admin) app.
2. Click the Smart Scheduler Admin tab.
3. Click the Con guration Settings tab.
4. Toggle the A llo w Sc hedule c reatio n with SendGrid setting on or off.
5. Click Update Setting.


Set Email Noti cations
You can select SendGrid for email noti cations from the Email Noti cation Settings on the Smart
Scheduler Admin tab.


1. Open to the Events (Admin) app.
2. Click the Smart Scheduler Admin tab.
3. Click the Con guration Settings tab.
4. Set Selec t platf o rm f o r email no tif ic atio n to “SendGrid.”
5. Select an email address in the Fro m Email A ddress eld.
6. Click Update Settings.


Functionality
A llo w Sc hedule c reatio n with SendGrid can only be toggled on/off if the SendGrid
A P I Key   eld contains a value.
The SendGrid A P I Key must be added to the BT Base Admin app before users can select
"SendGrid" in the Selec t platf o rm f o r email no tif ic atio n eld.
Users cannot remove/modify the API Key if the A llo w Sc hedule c reatio n with SendGrid
setting is toggled "ON."
Users cannot remove/modify the API Key if there is an active email scheduled job with
SendGrid selected as the from email.
Users cannot remove/modify the API Key when SendGrid is selected as the platform for


email noti cation in the Email Noti cation Settings.


Schedule SendGrid Emails
Use the Smart Scheduler to schedule SendGrid emails.

1. Make sure A llo w Sc hedule c reatio n with SendGrid is set to “On.”
2. Open the relevant Event record.
3. Click the Communications tab. (If you don’t see the Communications tab, click here to learn
how to add it.)
4. Click New Message.


Recipients Section
1. Select Schedule “an Email.”
2. Select “Event Attendees” or “Session Attendees.”
3. Enter a Sc hedule Name .
4. Select “SendGrid.”


5. Select a Fro m Email A ddress .
6. Select a T o Email .
7. Choose an A ttendee Filter .
If you set A ttendee Filter = “Attendance Status”, select the relevant options in


the A ttendanc e Status eld.
If you set A ttendee Filter = “Registration Status”, select the relevant options in
the Registratio n Status eld.
8. There must be at least one recipient listed in T o tal Rec ipients .
9. If a zero is listed under T o tal Rec ipients , check that you have the correct status selected
and review the Attendees that should have the chosen status.
10. Con rm that the amount under Email Balanc e is greater than the number of T o tal
Rec ipients .
11. Click Next.


Schedule Section
1. Choose one of the three options below to schedule your email.
Send the email at a speci c date and time
Choose the speci c date and time in the Selec t a Date / T ime elds.
Send the email X Minutes/Hours/Days After/Before the selected trigger.
Enter the number.
Choose “Days”, “Hours”, or “Minutes”.
Select “Before” or “After”.
Choose “Event Start Date/Time”, Event End Date/Time”, “Event Attendee
Registration Date”, or “Event Attendee Created Date”.
Select No w to send the email two minutes after the email is scheduled.
2. Click Next.


Message Section
1. In the Email T emplate eld, search for an existing Email Template or click Create New to
create a new one.
2. Click Next.


Send Test Section
1. Enter a T est Email . Make sure to use an email that can be checked easily. Using your email
is a good option.
2. Select a T est Rec o rd .
3. Click Send Test.
4. After you receive the success message, click Schedule.


Add User Licenses and Phone Numbers
Existing users with the Blackthorn Messaging Admin permission set can add additional user licenses
and phone numbers via the Messaging Admin tab.


1. Go to the Messaging Admin page.
2. In the Current Plan section, click the Manage Subscription button.


3. Complete the following steps in the pop-up window.
To add more user licenses, click the + sign in the User Licenses(s) column.
To add more phone numbers, click the + sign in the Phone Number(s) column.
The - sign will be disabled to prevent reducing number of user licenses and phone
numbers from going below the previous amount.


4. The pricing details for the new licenses/phone numbers will be visible in the Additional
Subscription column.
5. The revised balance, that will be effective on the next billing date, is shown in the New
Subscription column.
6. In this example, the user already has a default payment method set up.
7. Click Checkout and complete the checkout process.


Add a New Payment Method
Complete the steps below if you need to enter a new payment method to complete the checkout
process.


1. After adding additional licenses or phone numbers, click Checkout.
2. In the pop-up window, complete the following steps.
3. Click in the Choose a Payment Method eld.


4. Click Add a new card to add a new payment method.


5. In the Add Payment Method window, enter a Payment Method and related address.
6. Review the policy and terms agreement and click the checkbox.
7. Click Con rm.


Upgrade a Trial Plan to a New Plan


Watch video on YouTube
Error 153
Video player configuration error


Watch on


1. Go to the Messaging Admin tab.
2. In the Current Plan section, click Upgrade Account.


3. Con rm that the Business Name, Business Address, Industry, and Company Website are
correct.


4. Click Next.


5. Con rm that the Business Entity Type, Business Registration Number, Business Registration
Number Type, and Company Status are correct.
6. Click Next.


7. Con rm the following information.
Primary Contact: First Name, Last Name, Title, Job Position, Email, Phone
Secondary Contact: First Name, Last Name, Title, Job Position, Email, Phone


8. Click Next.


9. Review all of the information, and if correct, click Submit.


10. Review the available plans and click Select Plan next to your selection. For more information
about pricing, click here.


11. Review the plan you selected. Enter any additional User Licenses and/or Phone Numbers you
need.
12. Click Con rm and Pay.


13. Enter a Payment Method and related address.
14. Review the policy and terms agreement and click the checkbox.


15. Click Con rm.


Congratulations! You have upgraded your plan.


General FAQ
Q: How do I cancel my Messaging plan in the app?
A: While users can perform upgrades from the Admin panel, there isn't a self-service option to cancel.
Please contact Blackthorn Support to create a case, and they will help you cancel your subscription.

Q: How do I remove phone numbers from my subscription?
A: The rst step to remove one or more phone numbers is to contact Blackthorn Support. We will then
remove unwanted phone numbers from your Twilio and Salesforce accounts and update your
subscription to re ect the correct number of phone numbers.


How Do Users Upload Attachments to
SMS?

What permissions do I need to upload
attachments?
Before a user can upload attachments to SMS, their Pro le permissions must be updated.


1. Click the Gear icon in the top right-hand corner.
2. Click Setup.
3. In the Quick Find box, enter and click “Pro les.”
4. Select the Pro le that relates to the user(s) to whom you need to give the ability to add
attachments.
5. Scroll down to the Enabled Custom Permissions section.
6. Click Edit in the Enabled Custom Permissions header.
7. Move “Blackthorn Messaging.simplesms.Prevent Blackthorn Messaging Attachments” from
the Enabled column to the Available column.
8. Click Save.

Users related to the Pro le can now attach les via the Paperclip icon.


Why can't I see the Attachment button?
If the Paperclip icon or attachment button isn't visible for some phone numbers, check the formatting
of the phone number. Phone numbers can't include any of the following in the number.


spaces
parantheses
hyphens


What Types of Files Are Supported for
MMS?
You can send multimedia message service (MMS) messages using Blackthorn Messaging.

However, as les are sent as binary data directly through the carrier networks there are some
limitations as to the type and size of the les that can be sent. These limitations are imposed by the
individual carrier networks not by us.


Video Files

At this time, video les can only be sent by attaching a video’s link to your SMS message.


The following le types are supported.

JPEG (.jpg or .jpeg)
GIF (.gif)
PNG (.png)

The le size is limited to 3MB. Files of the above types will be automatically optimized and resized to t
into the speci cations of the individual carrier networks.

The following le types are accepted:


PDF (.pdf)
vCard (.vcf)

Files of these type cannot be optimized or resized so their original size must be 650 KB or less in order
to meet the limitations of the carrier networks.

You will receive an error when sending an invalid le type or a le that's too large.


Do You Have a List of Published IP
Addresses?

Product Data Usage
The following IP address is being used for BT Product Data Usage.

54.236.121.198


Static IP Addresses
The following table shows which apps support xed or static IP addresses.

Application                          AWS Region                      AWS IPs
Events webapp** / Connect360               us-east-1 (Virginia)                 35.175.67.37
54.83.187.87
us-west-2 (London)                   3.9.71.98
13.43.139.207
ap-southeast-2 (Sydney)              13.238.52.100
3.24.236.249
ap-southeast-1 (Singapore)           54.251.181.141
13.228.230.156
(Storefront)                               us-east-1 (Virginia)                 35.175.67.37
54.83.187.87
DocumentLink                               us-east-1 (Virginia)                 35.175.67.37
54.83.187.87
PayLink                                    us-east-1 (Virginia)                 35.175.67.37
54.83.187.87
Authorization app                          us-east-1 (Virginia)                 35.175.67.37
54.83.187.87

** The Events webapp, by default, uses the proxy for Transact (Cashnet) and TouchNet. If you enable
IP restrictions for Transact (Cashnet) and TouchNet, you must also update those systems directly.


Add IP Addresses
To add a static IP address, follow the steps below.


1. Go to Setup.


2. Scroll down to the Users section and click Users.
3. Locate the authorized user and click their Pro le.
4. Scroll down to the Login IP Ranges section.
5. Click New.
6. Add the start and end IP addresses.
7. Click Save.

For customers outside of the U.S., you will need the us-east-1 IPs and the regional IPs. Con rm the
region by going to the License > Org Instance eld (AUS = Sydney IPs, APAC = Singapore IPs, etc.)

You do not need the staging IPs unless you are using staging.events.blackthorn.io, which is used
internally by Blackthorn.

Note: Do not add the IP addresses to Security > Network Access.


How Do I Update my Payment Method?
Users can change the Payment Method at any time.


Update a Card’s Information
1. Click the Add Card button.


2. Update the First Name , Last Name , Card Number , Ex piry Date , CV V , or address
elds.


3. Click Add Card.


Change the Default Payment Method
1. Click Choose Default Payment.
2. Select a Payment Method.
3. Click Save.


4. Once a card is set as the default Payment Method, it will remain the default Payment Method
until changed.


Delete a Payment Method
Users cannot delete a card that is set as the default Payment Method or is con gured for auto-
recharge. Any other saved Payment Method can be deleted.

1. Click the card you want to delete.
2. Click Con rm.


How Do I Grant Access to Messaging
Support?
1. In Salesforce, go to My Settings (or Setup).
2. Click Grant Account Login Access.
3. You'll see Messaging Support as an option. Select 1 Day, 3 Days, 1 Week, or 1 Month.


What Does this Error Message Mean?

Why do I see the message "No phone numbers
are visible for you to send from"?
You may encounter this warning message that states you don't have visibility to any phone numbers to
send from.


This means that the User who is seeing the message does not have visibility to any of your
Messaging-enabled phone number records. Review the steps in the article Phone Number Setup.

If you have already con gured a phone number, do the following:


1. If you're in Lightning, switch to Salesforce Classic (yes, we know...   ).
2. Go to the Phone Number record that the User should have access to.
3. Click the Sharing button on the record. (Located at the top next to the Edit and Delete
buttons).
4. Add the User who is seeing the warning message, and grant Read access.

If you've con rmed the user has access to the record, but they are still seeing the message, do the
following:


1. Go to the Phone Number record.
2. Uncheck the Available for Campaign checkbox.
3. Save the record.


Why do I see the message "PushTopic is not
accessible"?
You may encounter a warning that sates "PushTopic is not accessible". This warning message would be
seen either on the Blackthorn Messaging Messenger component or the Messaging Conversations page.
If you see this message it means that the logged-in user does not have access to the PushTopic object.


PushTopic is a standard Salesforce object that is used with the Streaming API. Basically, it's how the
Messaging components listen for new inbound text messages.


To solve this issue, you can simply do the following:


1. Go to the Pro le of the User who is seeing this message.
2. Click Edit.
3. Go to the Object Settings and nd PushTopic.
4. Ensure the Pro le has, at minimum, READ access to the PushTopic object.
5. Save the Pro le.


What Happens When my Message
Balance Reaches Zero?
When your message balance reaches zero you will not be able to send any outbound text messages
until your balance is increased. Your inbound messages will still be sent to Salesforce so you won't
miss any text messages from customers, but you will not be able to respond.

Your account will also be temporarily placed in "Suspended" status until your message balance
increases.

To add additional messages to your balance, you can do the following:


1. In Salesforce, go to the Messaging Administration page.
2. Navigate to the SMS section (sms icon on the left-hand side).
3. Click the Add Messages button.
4. Enter the Quantity of messages you want to purchase. You will see a con rmation of the
price for these additional messages.
5. Click Checkout.
6. Con rm your payment method and click Buy Messages.

If the payment is processed successfully, your messages will be immediately added to your balance
and your account will be placed back into "Active" status.


Why don’t I see any phone numbers when
I try to send a message?

Grant Access
If the phone nummber is already con gured, perform the following steps.


1. If you're in Lightning, switch to Salesforce Classic.
2. Go to the Phone Number record that the User should have access to.


3. Click Sharing.
4. Add the User who sees the warning message, and grant Read access.


Update Phone Number Record
If you've con rmed the user has access to the record but still can’t see phone numbers, complete the
following steps.


1. Go to the Phone Number record.
2. Click the Pencil icon next to the A v ailable f o r Campaign eld.


3. Uncheck the A v ailable f o r Campaign checkbox.
4. Click Save.


Release Notes

Current Release Notes

February 2025
Version 3.47


Previous Release Notes

October 2024
Version 3.46


July 2024
Version 3.44.3


June 2024
Version 3.44.1


May 2024
Version 3.44


April 2024
Version 3.43.21


February 2024
Version 3.43.16


January 2024
Version 3.43.14


Version 3.43.13
Version 3.43.12


November 2023
Version 3.43.11
Version 3.43.7


September 2023
Version 3.43.2


August 2023
Version 3.43.1


July 2023
Version 3.42.3
Version 3.42.1
Version 3.42


June 2023
Version 3.40


May 2023
Version 3.39


March 2023
Version 3.38


January 2023
Version 3.36.7
Version 3.36.6
Version 3.36.5


December 2022
Version 3.36.4
Version 3.36.3
Version 3.36.2
Version 3.36.1


May 2022
Version 3.36


April 2022
Version 3.34


January 2022
Version 3.30


October 2021
Version 3.27


March 2021
Version 3.18.3


November 2020
Version 3.13


April 2020
Version 3.5


August 2025 - Salesforce Connected Apps
Update
Salesforce recently announced a change to its security policy around Connected Apps, effective August
28th. As a result, Blackthorn recommends verifying that these Connected Apps are installed in your
Salesforce orgs.


Blackthorn | Connected App - required for using Blackthorn Events and Blackthorn Payments
Mobile Check-in - required to use the Blackthorn Mobile Check-in app
Blackthorn | Mobile Connected App - required to use the Blackthorn Mobile Payments app
Blackthorn Message - required for using Blackthorn Messaging

Please review the attached pdf for instructions to check that the required Connected Apps are installed
and connected correctly.

Your browser does not support PDF. Click here to download.


March 2025 - Version 3.48
Please review the updates below and follow the upgrade instructions to upgrade your Messaging
application.


Table of Contents
(Release Date: April 29, 2025)

Bug Fix
Enhancements
Upgrade Instructions
Important De nitions


Bug Fix
When sending an SMS message from a Lead record, the template used for the SMS Message
will be mapped to the SMS Message’s SMS T emplate eld. Previously, when a user created
an SMS Message from a template and clicked the Send SMS button to send it from a Lead
record, the template was not mapped to the Lead’s related SMS Message record’s SMS
T emplate eld. (Known Issue: 000004250)


Enhancements
Mapping that occurs during the account activation process was updated to ensure that the
Business Entity T y pe and Co mpany Name elds are set correctly when the Business
Entity T y pe eld is set to “Corporation.” If the Business Entity T y pe eld is changed
from “Corporation” to another value, the value in the Co mpany Name eld on the A2P
registration record will be removed. (Known Issue: 000004048)
The Auto Recharge system was redesigned to ensure accurate balance deduction and
simultaneous message count depletion for bulk messaging. The improved system enables
seamless billing for bulk message sends, eliminating the need for manual intervention.


Upgrade Instructions
Go to the Blackthorn Candy Shop to upgrade Messaging to the newest version.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


February 2025 - Version 3.47
Please review the updates below and follow the upgrade instructions to upgrade your Messaging
application.


Bug Fix
When users don’t have the correct permission to Push Topic & Streaming Channel objects for the
assigned permission set, they will see an error message. Previously, on incoming messages, users
didn’t know there was a problem as the utility component did not give the user an indication that there
was an error. The error details were logged as console.log.


Enhancement
Mapping during the account activation process was updated to ensure that the Business Entity
T y pe and Co mpany Name elds are set correctly when the Business Entity T y pe eld is set to
“Corporation.” If the Business Entity T y pe eld is changed from “Corporation” to another value, the
value in the Co mpany Name eld on the A2P registration record will be removed. Previously, the
company name was mapped to the Business Entity T y pe eld, which prevented users from
submitting the form. (Known Issue: 000004048)


Upgrade Instructions
Go to the Blackthorn Candy Shop to upgrade Messaging to the newest version.

Blackthorn has adopted Salesforce’s managed package installer to simplify the installation process.
The installer will con rm that the correct versions are installed.


October 2024 - Version 3.46

Bug Fix

Scheduled SMS Messages from Campaign Not Working

Description
When using a Campaign with more than 2,000 Campaign Members to send bulk SMS messages, the
Campaign Member list would not load or show a validation message, as expected. Even though the
SMS messages were scheduled, the Apex Jobs script showed an unexpected Error.


Resolution
Updated the code in the Apex Job, which also removed additional lters that caused the error.


Enhancement

Long Loading Times when Accessing the Messaging
Admin tab

Description
Newly onboarded users and those using a demo account experienced long wait times when opening
the Messaging Admin tab.


Resolution
Introduced a new and enhanced Messaging Admin tab that has faster loading times.


July 2024 - Version 3.44.3

Bug Fixes

Unable to Authenticate a User During the Installation

Description

Users could not click the “Authenticate a User” tab on the Messaging Admin tab during the setup
process. This happened because the Phone Number Setup step did not nish after the demo phone
number records were created. (Demo phone number records are available to test Demo Accounts.)


Resolution
Demo Account customers can now click the “Authenticate a User” tab to authenticate a user after the
Phone Number Setup is complete.


Demo Account Phone Number Formatting Error

Description
Fixed an error related to the Send Blackthorn Messaging Message ow and the Demo Account’s phone
number formatting

Demo Account users could not send messages when using the Invocable method in Flo w Name =
“Send Blackthorn Messaging Message.” This occurred because the Invocable method searched for a
static numbers format in the Object record. The static format was +1XXXXXXXXXX. And even though
the recipient number was subscribed, they got the following error message in the SMS record:
“Recipient XXXXXX yet not subscribed to receive demo message from YYYYYY.”


Resolution

Once users upgrade the Messaging app, Demo Account numbers that have been opted-in (subscribed)
will be sent via the ow.


Enhancements

Messaging App Tracks when Phone Number Opt-in
Occurs

Description
The date and time that the message recipient user gave consent will be recorded on the record page. To
see the new settings, go to Messaging Admin Tab > Con guration Setting > Messaging Tab.


Under the Outbound Message Settings heading, the Consent Settings now includes the
Co nsent P o pup Frequenc y     eld with the “Once per Recipient (Opt-In)” option.
Users can select the object for which they want to capture the consent date and time. By
default, all objects con gured to send SMS will be selected.
When a user sets Co nsent P o pup Frequenc y to “Once per Recipient (Opt-In),” they will
see the following pop-up message.
“Please make sure you have created the eld SMS Optin DateT ime on the
selected Objects before enabling this setting or else the consent date time will not
get captured. See our documentation for more info.”


Expected Behavior

If the SMS Optin DateT ime eld value is blank, message recipients will receive an SMS
Consent pop-up modal since consent is happening today.
When a message recipient selects the checkbox and clicks the Send button, the current date
and time will populate the SMS Optin DateT ime eld.
If no conversation record exists, the Consent Signature will be appended to the message
since it is happening today.
If the SMS Optin DateT ime eld is not blank, then message recipients will not see the
SMS Consent pop-up modal, and the SMS will be sent.
If the SMS Optin DateT ime eld has a future date, then message recipients will see the
SMS Consent pop-up modal.
When a message recipient selects the checkbox and clicks the Send button, the current date
and time will replace the future date in the SMS Optin DateT ime eld.
The following will occur if the Task trigger or Invocable Method is used to send SMS.
If the SMS Optin DateT ime eld is blank, the recipient will not receive the SMS.
The SMS Message record will not be created when Status = “Error.” The


error message will be “This person has not Opt-In for SMS
communication.”
If the SMS Optin DateT ime eld has a value, recipients will receive the SMS.
If the SMS Optin DateT ime eld contains a future date, the recipient will not
receive the SMS.
The SMS Message record will not be created when Status = “Error.” The
error message will be “This person has not Opt-In for SMS
communication.”


Utility Item "Blackthorn Messaging Messenger" Error

Description
Users cannot send messages from the Blackthorn Messaging Messenger utility item component if it
has been added to a (non-managed) Salesforce app. Additionally, users cannot send messages from
the component after navigating to a speci c Contact record.


Resolution
The Blackthorn Messaging Messenger utility item component can now be used with (non-managed)
Salesforce apps. To use the Blackthorn Messaging Messenger component, it must be added to the
Blackthorn Conversation Utility utility item.


June 2024 - Version 3.44.1

Bug Fix

"Uncaught Object Error" on Bulk SMS Campaign Page

Description
Previously, when a user tried to send bulk SMS from a campaign record, they received the following
error. Also, when they clicked Done, the screen did not update.

"Uncaught #<Object> throws at https://xxxxxxxxxxxx--
simplesms.vf.force.com/auraFW/javascript/VXZJYkJtTFAtX2RjOGFiVmZaelpqQTk4bkk0bVJhZGJ
CWE9mUC1IZXZRbmcyNDguMTAuMy01LjAuOQ/aura_prod.js:103:67615"


Resolution
We removed unnecessary libraries, which were loading even though they were not in use anymore, to
x both issues.


Enhancement

Refreshing a Sandbox Will Not Interrupt the Production
Account

Description
Refreshing a sandbox caused the Account and API Key to be cloned, which caused problems with the
related production account in the BT Base package and Messaging app.


Resolution

Using the production Account and API Key in the refreshed sandbox is now restricted. If a user tries to
open the Messaging Admin tab after the Sandbox was refreshed, they will see the following error.


May 2024 - Version 3.44

Bug Fix

Auto-Recharge Label on a Payment Method

Description
Restrict users from deleting credit cards that are selected for the Auto-Recharge process or are used in
other places.


Resolution
In the Payment Methods section on the Messaging Admin tab, users will see the Auto-Recharge label
next to the card selected for auto recharge. The label lets them know that this card cannot be deleted.


Enhancement

Apex Limit Reached when Sending SMS

Description
When trying to send SMS messages using a ow with the Apex Class - ‘"Send Blackthorn Messaging
Message," users received too many "SOQL queries: 101 limit error" errors.


During testing in debug mode, the send SMS noti cation was executed without an issue; however, the
system threw the following error for the eight Contact records in the list. Error:System.LimitException:
simplesms:Too many SOQL queries: 101


Resolution
We introduced a new ow called Blackthorn Messaging Send Message(Flow).


Flow Con guration


Entry Criteria De ned on Account Object


Get a Contact Record from the Account


Looping the Process to Handle Contacts


De ne the Variables to get Data from the Contact Record


Recipient Variable


Collect Contact Records into a Collection Variable


Call the Apex Method to Send SMS to the Valid Contact Records


April 2024 - Version 3.43.21

Bug Fixes

Twilio No Longer supports DUNS Numbers

Description
Users who set the Business Register Type to a DUNS number on the Business Entity Information
form could not complete the A2P registration process.


Resolution


The DUNS option in the Business Register Type      eld was removed because Twilio no longer
supports DUNS numbers. In the future, the Business Register Type options will be updated
dynamically when Twilio makes changes.


After-hours Message Function Not Working

Description

The after-hours message function would not send messages even though the incoming and outgoing
messages worked correctly for the number.


Resolution
An update during the Salesforce maintenance release caused an issue related to Apex Class versioning.
Updating the Apex Class version resolved the issue. Customers can now receive messages from the
After Hour response message feature.


February 2024 - Version 3.43.19

Bug Fix

Missing State Blocked User from Submitting Details

Description
If a company is headquartered in Washington, DC, users could not activate their account since DC
(District of Columbia) was not an option in the State      eld.


Resolution
The State    eld picklist has been updated from the API side, so the list of states will be dynamically
generated. This will allow states to be added or removed in the future.

The following updates were also made to the component.

If a state list is available for a country, the user will see the drop-down list.
If a state list is unavailable, the user will see a free-form text eld where they can manually
enter the state’s name.


Enhancement

New Onboarding Process for the Messaging App

Register for a Trial Account
When registering for a trial account, users will see a banner with the “Currently Using Demo Account”
message in the following locations.


Messaging Admin Page


RLC


Conversation


Utility


Bulk


View the Demo Phone Number
Users will see the demo phone number in the managed Phone Number section.


To create a demo phone number, click the Create Record button.
Users cannot add Call Forwarding.
Users cannot add additional phone numbers to the list of provided numbers.


Send the First Outbound Message
The recipient must subscribe to the phone number before the user can send the rst outbound
message.

Share Required Information
Customers must share the following information with a recipient before the recipient can subscribe to
the phone number.


RLC


NMC


Bulk


Validation Error


Send a Single Message
If a user sends a message without the recipient subscribing to the number, then the
user will receive the following error message. “Recipient customer +1XXXXXXXXXX
yet not subscribed to receive demo messages from +1XXXXXXXXXX”


Send Bulk Messages
If a user sends a Bulk SMS message without the recipient subscribing to the
number, the user will see the following error message in each SMS Message
record. “Recipient customer +1XXXXXXXXXX yet not subscribed to receive demo
messages from +1XXXXXXXXXX”


Opted-in Numbers
Users can see which phone numbers have opted-in for the demo number by going
to the Messaging Admin tab and clicking the Phone icon.


Purchase the Demo Number
Users can purchase a new number once they upgrade their trial account to a paid license. At that point,
the following will occur.


The demo number will be removed from the Messaging Admin page.
Recipients will be unsubscribed from the demo number.


February 2024 - Version 3.43.16

Important Update
The Smart Scheduler (Blackthorn Base package) was added to the Blackthorn Candy Shop. Messaging
customers can now use Smart Scheduler without downloading the Events or Storefront apps.


Bug Fixes

Issue Using a Site License

Description
A user with a Site License received the following warning message on the Contact record after
upgrading the production org. “The component is part of the AppExchange Package Blackthorn
Messaging, and requires a license to use."


Resolution
Previously, the Messaging app did not acknowledge the license assignment record, causing problems
when trying to send SMS messages. Users with a Site License must upgrade the Messaging app to
version 3.43.16 or higher to resolve the issue.


SOQL Limit Error


Description
After activating and con guring the Messaging app for an org with a large number of active users, the
following error was triggered upon opening a Contact record with the RLC component. “Error:
Simplesms: too many query rows: 50001”


Resolution
Updates were made to manage orgs with a large number of active users who have avatars.

If you have any questions, please don't hesitate to contact Blackthorn Support.


January 2024 - Version 3.43.14

Bug Fixes

Error on SMS Message Component

Description

A customer received the following error message when using the SMS message component. The issue
was speci c to the contact record.

"This page has an error. You might just need to refresh it. Action failed:
simplesms:ChatAttachment$controller$handleInit [Cannot read properties of unde ned (reading
'indexOf')] Callback failed: apex://simplesms.Ctrl_Ltng_Send/ACTION$getMessagesForMessenger
Failing descriptor: {simplesms:ChatAttachment$controller$handleInit}"


Resolution
The absence of information in media records caused the issue. Users will now see an error message in
the Messaging component if data is missing.


Users Blocked from Sending Messages

Description


Internal and Community users were blocked and unable to send messages after upgrading to the
November release. Both internal and community users were assigned the “Textey-Partner” permission
set. Users received the error message below:


Resolution
We eliminated checks that attempted to read the value of the organization eld, removing back-end
issues related to the eld ID. Internal and Community users should be assigned either the Blackthorn
Messaging Standard User or Blackthorn Messaging Standard User - Community permission set.


January 2024 - Version 3.43.13

Bug Fix

Users Blocked and Unable to Send Messages

Description
After upgrading to the November release, internal and Experience Cloud users were blocked and
unable to send messages. Users received the following error message: “You do not have permission to
read the eld Id on Organization.” Both user types were assigned a custom permission set, and the
organization had a Site license.


Resolution
Since the system was designed to show this component only if the user had the correct permission set
or was assigned a Messaging license, the following updates were made.


The system will determine if the user is an Experience Cloud user. If they are, the system will
automatically allow the user to send messages.
We recommend that customers assign a Blackthorn Messaging Standard User or Blackthorn
Messaging Standard User – Community permission set.


January 2024 - Version 3.43.12

Enhancement

Inbound Messages: START and Removing the DND on
the End User’s Record

Description

When an end user texted “START”, the Do Not SMS (Contact)      eld was not updated to “False”,
preventing messages from being sent by the Messaging user.


Resolution
When an end user texts “START”, the Do Not SMS (Contact)      eld on their Contact record is set to
“False” (unchecked), allowing SMS messages to be sent to the end user.


Bug Fix

Bulk Messages from Campaign Wizard Reach Apex CPU
Limit

Description
Customers, who used the Campaign Wizard to send out 50,000+ Campaign Members’ SMS messages,
received the following Apex CPU Time Limit error: "simplesms: Too many query rows: 50001".


Resolution


Users can now send Bulk SMS messages (50,000+) from the Campaign Wizard.


November 2023 - Version 3.43.11

Bug Fixes

Non-Admin User License Issue

Description
When a non-admin user attempts to send a bulk SMS via a Campaign, they are unable to access the
lightning components and receive an error message stating that they do not have a license.


Resolution
This issue, which was caused by a separate issue where non-admin users with Site User account
licenses encountered an error in the Messaging component, has been resolved.


"Inbox Conversation List" Apex Trace Error

Description
Random Apex errors that referenced a tracing issue in the “Inbox Conversion List” occurred when
accessing Lead, Contact, and Account records.


Resolution

The Apex Trace Error in the “Inbox Conversation List” was found to occur where the component was
integrated into the Utility. The problem, which was caused by network issues that disrupted data
transactions, has been resolved.


EU Accounts - Cannot Add Phone Numbers

Description
Users cannot add phone numbers on EU Accounts from the Messaging Admin tab if A2P is not
processed. The user received the following error message. “Error creating phone number: You can only
use a tollfree number while A2P registration is pending approval, please upgrade your package to
purchase tollfree numbers.”


Resolution


Users with EU Accounts can now add new phone numbers without completing the A2P registration
process as it is no longer required.


EU Account Errors - Account Activation

Description
For EU Accounts, users received an error when working in the Account Activation section of the
Account Setup Process if the A2P registration was not competed.


Resolution

Users registered to an EU server will not be blocked due to an incomplete or unsubmitted
A2P registration.
A green mark will appear to indicate a complete Account activation status.
All other users will receive an error if the A2P information is incomplete or has not been
submitted.


November 2023 - Version 3.43.7

Enhancements
If a Messaging account is suspended (Account Status = “Suspended”), then the user will
receive the following error message. “Your account is suspended, Please reach out to our
Success Team.”


A user will receive an error message If they have not been assigned a Messaging license, but
have been assigned a permission set.


In the Send Bulk SMS box with the Terms of Service acknowledgment, the spelling of the
word organization has been changed from “organisation” to “organization”.


Bug
Users can send Bulk SMS from a Campaign if the number of members in the list is more than
1000 as there is no maximum limit. The limit for the number of records that can be displayed
in the UI is 1000.


September 2023 - Version 3.43.2

Enhancements

Improve the A2P Submission Process
The A2P submission process is crucial for businesses and organizations that send automated
messages to users' phone numbers. To enhance this process, we added a new step called Account
Activation that will occur between the Account Registration and Phone Number Setup steps.

The Account Activation step requires users to activate their account before adding phone numbers for
A2P messaging. The goal is to help prevent errors that may occur due to incomplete or inaccurate
account information.


User Experience
After completing the initial Account Registration, users will see the Account Activation screen. Users
must enter the Contact Information, Business Information and Usage & Content details. The screens
will provide clear instructions and a guided path to activate an account.


Error Handling for Incomplete Activation

If a user attempts to add phone numbers for A2P messaging without completing the Account
Activation step, they will encounter an error message. The error message is - "Please submit A2P
details using a guided path and try again.”


Updated Account Setup Process
Perform the following steps to set up your account.


1. Complete the Account Registration by providing the Account Number and API key provided
by Blackthorn Support.
2. Click the Account Activation tab.
3. Complete the elds in the General Business Information window.
Business Name (required)
Business Address (required)
Industry (required)
Company Website (required)


4. Click Next.
5. Complete the elds in the Business Entity Information window.
Business Entity Type (required)
Business Registration Number (required)
Business Registration Number Type (required)
Company Status (required)


6. Click Next.
7. Complete the elds in the Usage & Content window.
Message Volume
Use Case
Opt In Type
Opt In Proof Url


8. Click Next.
9. Complete the elds in the Contact Information (Primary & Secondary) window.
Primary Contact
First Name
Last Name
Title
Job Position
Email
Phone
Secondary Contact
First Name
Last Name
Title
Job Position
Email
Phone


10. Click Next.
11. Review the information in the Review & Submit window.


12. Click Submit.


After successful completion of all the steps, the Account Activation gets submitted to Twilio.


Process of Phone Number Searching API

Validating A2P Details
Validating A2P details is a crucial step that occurs when sending automated messages to users via
platforms like Twilio. This step includes reviewing and verifying the information provided by the
business or organization who intends to use the A2P messaging services.

Twilio, for example, follows a meticulous validation process before approving the submission. The
validation process typically takes about 2 to 3 weeks. During that time, the submitted information is
carefully examined to ensure compliance with regulations and best practices.


Searching Phone Numbers
During Twilio’s review and approval period, users can search for and use Phone Numbers by utilizing
toll-free phone numbers. This feature ensures that businesses can continue their operations and
prepare for A2P messaging without causing any interruptions.


August 2023 - Version 3.43.1

Enhancement

Work ow Rule to Flow Migration
The Work ow Rules have been converted to Flows to provide the bene ts listed below.
Better Performance
The ability to re ne and streamline high-volume automation via features like Run
Asynchronously, Fast Field Updates (Before Save), and Entry Conditions.
Improved error-handling, troubleshooting, and debugging
Click into the ow from an error email and see the path that was run.
Try different record-updates straight from the debugger in triggered ows.
See how their governor limits will be impacted while debugging.
Exceptional extensibility with invocable actions and sub ows
Users can package pieces of automation, either in Flow or Apex, to create building
blocks that empower Admins and standardize common interactions.


Work ow Rule Details
Rule Name: Email Owner When SMS Message Received
Criteria: (SMS Message: Message NOT EQUAL TO null) AND (SMS Message:
Direction EQUALS Incoming)
Description: It will send an email to the SMS message's owner when the SMS
message is received.
Rule Name: Number Status Success/Failure
Criteria: Number Lookup Status: Status EQUALS Complete,Error
Description: It will send an email to the Number Lookup State's owner when the
Status changes to either "Complete" or "Error".

Rule Name: Populate From Phone Field
Criteria: SMS Message: From NOT EQUAL TO null
Description: Updates the SMS Messages From Phone        eld.
Rule Name: Populate To Phone Field
Criteria: SMS Message: To NOT EQUAL TO null
Description: It will update the SMS Messages To Phone      eld.
Rule Name: Update Template Message Contact


Criteria: OR( ISNEW() ,ISCHANGED(
simplesms__Auto_Response_Template_Contact__c ) )
Description: It will update the SMS Campaign Response Rule's Auto Response
Message Contact     eld.
Rule Name: Update Template Message Lead
Criteria: OR( ISNEW() ,ISCHANGED(
simplesms__Auto_Response_Template_Lead__c ) )
Description: It will update the SMS Campaign Response Rule's Auto Response
Message Lead    eld.


Bug Fix

Description
The Error Message     eld on the SMS Message record does not show errors on undelivered
messages, even though the error message can be seen in Twilio.


Resolution
If a user sends a message to a valid phone number, but the message is not delivered to the recipient,
then Twilio’s error message will be shown in the Error Message     eld on the SMS Message record.


July 2023 - Version 3.42.3

Bug Fix

Description
When a recipient texts “Stop” back to the sender, the recipient receives an opt-out con rmation
message, but the Do Not SMS checkbox on the Contact record is not updated. The sender in this
scenario has the Blackthorn Messaging Standard User and Blackthorn Messaging Lightning User
permission sets.


Resolution
The Do Not SMS checkbox on the Contact record will be automatically set to “True” when the
recipient replies “Stop.”


July 2023 - Version 3.42.1

Enhancement
Users can attach images (jpeg, png, and gif), PDFs, and vCards to an SMS Template and send the
Template using either an Invocable Method or a Task Trigger.

Default and excluded Phone Field       elds can also be con gured by object. When sending text
messages from a record, you can change which Phone Field          elds are displayed in the To drop-
down.


Limitation

Only one attachment can be sent with per Template. If more than one le is attached, only the
last le attached will be sent with the message. For example, an image is attached rst. A PDF is
then attached. Lastly a vCard is attached. Only the attached vCard will be sent with the SMS.


Enable Task Trigger in the Messaging Admin


1. Switch to Salesforce Classic.
2. Create an Account record with a phone number.
3. Select Create New Task in the Activity.
4. Populate the Task elds using the instructions below.
Assigned To : Select any user.

Subject : This eld MUST start with the phrase “Send SMS” followed by your

subject.
Due Date : We recommend choosing Rule Trigger Date plus 0 days.

Status : We recommend choosing “Completed” so the task does not appear on

the user’s My Tasks list.
Priority : We recommend choosing “Normal”.

Comments : Enter the Code associated with the Template that you are using. Locate

the Template’s code in the Code   eld. Do NOT add anything else to the Comments
eld.


5. Click Save.


Bug Fix

Description
A user with an active Messaging license and Admin User permission set received an error when they
clicked the Messaging Admin tab.

The error message was "argument cannot be Null."


The user was also unable to authorize the Messaging app.


Resolution
The URI     eld located on the Blackthorn Messaging Settings custom setting contains an API that is
used to communicate with the server. To prevent the “Argument cannot be Null” error, the following
will occur. If the URI   eld’s data is removed, then the eld will point to a production server. If there is
data in the URI    eld, then the data will be used.


July 2023 - Version 3.42

Enhancements

Permission Set
Users who are assigned the Blackthorn Messaging Admin User permission set can only access the
Messaging Admin page.


Users who do not have access


Users who have access

The Blackthorn Messaging Admin User permission set provides users with edit access to all Blackthorn
Messaging related objects, elds, visualforce pages, and the Messaging Admin tab.


Scheduled Job (Admin)

Start a Scheduled Job
An Admin can only schedule a job if that job starts on the Messaging Admin tab. Complete the steps
below to start using Scheduled Jobs.


1. Go to the Blackthorn Messaging app.
2. Go to the Messaging Admin tab.
3. Click Con guration Settings in the left-hand navigation bar.
4. Click Scheduled Jobs.
5. Click START.


Stop a Scheduled Job

If there are pending scheduled jobs in the queue, an Admin cannot stop the scheduled jobs. All of the
currently scheduled jobs must be completed before the process can be stopped.


The Admin will see the warning icon next to the STOP button when there are jobs scheduled.


After the queue is empty and the Admin clicks STOP, they will receive the following con rmation
message.


How to Replicate the Issue
If a user performs the steps in the following use case, they will receive an error in the con rmation
message after clicking OK.


1. Open the Scheduled Jobs tab on a new page in your web browser.
2. Click START (keep the tab open).
3. Go to a Contact record and schedule a message from a record level component (RLC).
4. Go back to the original page where you stopped the job.
5. Click OK in the con rmation message.


The user will receive an error message stating that we are unable to stop the job due to scheduled
messages.


Schedule a Message (RLC)
Users will not be able to schedule a message from the record level component (RLC) until an Admin
starts the Scheduled Job in the Messaging Admin con guration settings. The “Schedule for Later” icon
will also be disabled.


If a user tries to schedule a message and the Scheduled Job is not started, they will receive the
following error message.


How to Replicate the Issue
If a user performs the steps in the following use case, they will receive an error in the con rmation
message after clicking Schedule Message.


1. Go to the Messaging Admin tab.
2. Click Con guration Settings in the left-hand navigation bar.
3. Click the Scheduled Jobs tab.
4. Click START.
5. Navigate to a Contact record and try to schedule a message.
6. Go back to the Scheduled Jobs tab and click STOP.
7. Go back to the Contact record and click the Schedule Message button.

The user will see the error message.


Bug Fixes

Apex Errors

Description
Users intermittently received an Apex Error from Salesforce when sending messages from a Lead
record.


Resolution

The Scheduled Jobs setting was added to the Administration Con guration Settings to allow Admins
to start/stop the job. A START / STOP button was added to control messaging scheduling from the
record level component.


Apex Script Unhandled Exceptions after Messaging
Upgrade

Description
After upgrading to the most recent Messaging release (3.36.3), Apex errors occurred.


Resolution
This issue happened when a non-Admin user tried to send Bulk SMS and messages using the
Invocable Method. The permission issue that happened in the background was due to the Salesforce
release.


ViewAllData or ViewAllRecords Permissions

Description

An Apex Error required all users to have ViewAllData or ViewAllRecords permissions.


Resolution


This issue happened when a non-Admin user tried to send Bulk SMS and messages using the
Invocable Method. The permission issue that happened in the background was due to the Salesforce
release.


Apex Error: (CORE.AKCRON_JOB_DETAIL) Violated

Description
An error with the Blackthorn Messenger Scheduler scheduled job occurred, preventing the scheduled
job from running.


Resolution
The Messaging Messenger Scheduler will now always run in the back end.


Scheduled Messages not Being Sent at the Correct Time

Description

Scheduled messages are not being sent at the correct time. For instance, a user scheduled messages
from a Campaign to be sent at 12:00 pm, but the message was sent at 12:00 am.

See the image below for an example Campaign where we recently tested and recreated this behavior.

Messages were scheduled for 6/3/2023 at 12:55 PM (EDT or UTC-04:00)
Messages were sent on 6/4/2023 at 12:55 AM (EDT or UTC-04:00)


How to Replicate the Issue


1. Open Blackthorn Messaging.
2. Click the Contacts tab.
3. Click on a test Contact record. (Use your cell phone number as the Contact’s phone number.)
4. Click Send New Message.
5. Write a message and schedule for a later time.


The Message will not be sent at that time.


Resolution
The time zone conversion will no longer depend on the subscriber’s time zone.


Error Popping Up

Description
After opening an SMS Widget, the user received an error.


How to Replicate the Issue
Open the SMS Utility in Salesforce.


Resolution

The Utility Component has been renamed.


Change the SF Classic "Send Bulk SMS" Button Label

Description
The Lightning and Classic versions of the Send Bulk SMS buttons had the same label, making it
impossible to differentiate between the two in a multi-select picklist.


Resolution
The Classic Salesforce button label has been changed to Send Bulk SMS (Classic). The Lightning
Salesforce button label will remain as Send Bulk SMS.


June 2023 - Version 3.40

Enhancements

Permission Set
Users who are assigned the Blackthorn Messaging Admin User permission set can only access the
Messaging Admin page.

Users who do not have access


Users who have access


The Blackthorn Messaging Admin User permission set provides users with edit access to all Blackthorn
Messaging related objects, elds, visualforce pages, and the Messaging Admin tab.


Scheduled Job (Admin)


Start a Scheduled Job

An Admin can only schedule a job if that job starts on the Messaging Admin tab. Complete the steps
below to start using Scheduled Jobs.

1. Go to the Blackthorn Messaging app.
2. Go to the Messaging Admin tab.
3. Click Con guration Settings in the left-hand navigation bar.
4. Click Scheduled Jobs.
5. Click START.


Stop a Scheduled Job
If there are pending scheduled jobs in the queue, an Admin cannot stop the scheduled jobs. All of the
currently scheduled jobs must be completed before the process can be stopped.

The Admin will see the warning icon next to the STOP button when there are jobs scheduled.


After the queue is empty and the Admin clicks STOP, they will receive the following con rmation
message.


How to Replicate the Issue
If a user performs the steps in the following use case, they will receive an error in the con rmation
message after clicking OK.


1. Open the Scheduled Jobs tab on a new page in your web browser.
2. Click START (keep the tab open).
3. Go to a Contact record and schedule a message from a record level component (RLC).
4. Go back to the original page where you stopped the job.
5. Click OK in the con rmation message.

The user will receive an error message stating that we are unable to stop the job due to scheduled
messages.


Schedule a Message (RLC)
Users will not be able to schedule a message from the record level component (RLC) until an Admin
starts the Scheduled Job in the Messaging Admin con guration settings. The “Schedule for Later” icon
will also be disabled.


If a user tries to schedule a message and the Scheduled Job is not started, they will receive the
following error message.


How to Replicate the Issue
If a user performs the steps in the following use case, they will receive an error in the con rmation
message after clicking Schedule Message.


1. Go to the Messaging Admin tab.
2. Click Con guration Settings in the left-hand navigation bar.
3. Click the Scheduled Jobs tab.
4. Click START.
5. Navigate to a Contact record and try to schedule a message.
6. Go back to the Scheduled Jobs tab and click STOP.
7. Go back to the Contact record and click the Schedule Message button.
8. The user will see the error message.


Bug Fixes

Apex Errors

Description
Users intermittently received an Apex Error from Salesforce when sending messages from a Lead
record.


Resolution
The Scheduled Jobs setting was added to the Administration Con guration Settings to allow Admins
to start/stop the job. A START / STOP button was added to control messaging scheduling from the
record level component.


Apex Script Unhandled Exceptions after Messaging
Upgrade

Description
After upgrading to the most recent Messaging release (3.36.3), Apex errors occurred.


Resolution

This issue happened when a non-Admin user tried to send Bulk SMS and messages using the
Invocable Method. The permission issue that happened in the background was due to the Salesforce
release.


ViewAllData / ViewAllRecords Permissions

Description
An Apex Error required that all users have ViewAllData or ViewAllRecords permissions.


Resolution
This issue happened when a non-Admin user tried to send Bulk SMS and messages using the
Invocable Method. The permission issue that happened in the background was due to the Salesforce
release.


Apex Error: (CORE.AKCRON_JOB_DETAIL) Violated

Description

An error with the Blackthorn Messenger Scheduler scheduled job occurred, preventing the scheduled
job from running.


Resolution
The Messaging Messenger Scheduler will now always run in the back end.


Scheduled Messages not Being Sent at the Correct Time

Description
Scheduled messages are not being sent at the correct time. For instance, a user scheduled messages
from a Campaign to be sent at 12:00 pm, but the message was sent at 12:00 am.

See the image below for an example Campaign where we recently tested and recreated this behavior.

Messages were scheduled for 6/3/2023 at 12:55 PM (EDT or UTC-04:00)
Messages were sent on 6/4/2023 at 12:55 AM (EDT or UTC-04:00)


How to Replicate the Issue


1. Open Blackthorn Messaging.
2. Click the Contacts tab.
3. Click on a test Contact record. (Use your cell phone number as the Contact’s phone number.)
4. Click Send New Message.
5. Write a message and schedule for a later time.

The Message will not be sent at that time.


Resolution
The time zone conversion will no longer depend on the subscriber’s time zone.


Error Popping Up

Description


After opening an SMS Widget, the user received an error.


How to Replicate the Issue


1. Open the SMS Utility in Salesforce.


Resolution
The Utility Component has been renamed.


Change the SF Classic "Send Bulk SMS" Button Label

Description
The Lightning and Classic versions of the Send Bulk SMS buttons had the same label, making it
impossible to differentiate between the two in a multi-select picklist.


Resolution
The Classic Salesforce button label has been changed to Send Bulk SMS (Classic). The Lightning
Salesforce button label will remain as Send Bulk SMS.


May 2023 - Version 3.39

Enhancements

Region-based Changes
The following changes were made to the activation of Blackthorn Messaging to accommodate differing
regional requirements.


US

After you've completed the installation steps, it’s time to activate your Blackthorn Messaging account.
When we say "activation," we are referring to a one-time process that will create a Messaging account
and link it to your Salesforce org.


1. Go to the Messaging Administration tab.
2. You will see a dialog that asks if you already have a Messaging account. Click No, I need an
account to indicate that you do not have a Messaging account.


3. This will open the Account Registration dialog box.
a. Set Account Region = “United States (US1)”.
b. Review our Terms of Service and Privacy Policy.
c. Click the I have read… checkbox.

d. Click Activate Now.


4. Click Yes, I have an account.


5. Set Account Region = “United States (US1)”.
6. Contact Blackthorn Support for the Account Number & API Key.
7. Once you have the Account Number & API Key, enter them in the Account Number and API
Key     elds.
8. Click Save. Your account is now registered and activated.


9. To change the credentials, click the Change Credentials button.


10. Update the elds as needed and click Proceed.


EMEA
After you've completed the installation steps, it’s time to activate your Blackthorn Messaging account.
When we say "activation," we are referring to a one-time process that will create a Messaging account
and link it to your Salesforce org.

1. Go to the Messaging Administration tab.


2. You will see a dialog that asks if you already have a Messaging account. Click No, I need an
account to indicate that you do not have a Messaging account.


3. This will open the Account Registration dialog box.
a. Set Account Region = “Europe (EU1)”.

b. Review our Terms of Service and Privacy Policy.
c. Click the I have read… checkbox.
d. Click Activate Now.


4. Click Yes, I have an account.


5. Set Account Region = “Europe (EU1)”.
6. Contact Blackthorn Support for the Account Number & API Key.


7. Once you have the Account Number & API Key, enter them in the Account Number and API
Key     elds.
8. Click Save.


Your account is now registered and activated.


Card UI Changes
The UI for the Payment Methods section has been modi ed to be more user-friendly.


Clicking the Add Card button opens a new window. This provides an easy and faster way to
enter the First Name , Last Name , Card Number , Expiry Date , CVV and other details.


Alternatively, the user can click Choose Default Payment to make payments using the
default Payment Method. Users can change the Payment Method at any time.


Once a card is set as the default Payment Method, it will remain the default Payment Method
until changed.


User cannot delete a card if it is set as the default Payment Method.


Cards not set as the default Payment Method can be deleted at any time.


Bug Fix

Community User Permission Set

Description
Users received the following error when trying to assign a Community user the standard Community
permission set. “Can’t assign permission set Blackthorn Messaging Standard User - Community to
user [name]. The user license doesn’t allow Assigned Apps”.


Resolution


To resolve this issue, we removed the Assigned Apps’ permissions. Complete the steps below to set
up a Community user and share From Phone Numbers.


Setup Steps for Assigning Permission Sets to a Community User

1. Click the Gear icon in the upper right-hand corner.
2. Click Setup.
3. Type “Permission Sets” in the Quick Find box.
4. Click Permission Sets.
5. Click Clone next to the permission set “Blackthorn Messaging Standard User – Community”.
6. Set the Label to “Custom Blackthorn Messaging Standard User – Community”.
7. Set the API Name to “Custom_Textey_Standard_User_Community”
8. Click Save.
9. Open the permission set that you just created.
10. In the Apps section, click Assigned Apps.
11. Click Edit.
12. Remove the following Enabled Apps.
simplesms.Textey (simplesms__SimpleSMS)
simplesms.Textey (simplesms__Textey_ltng)
13. Click Save.

You can now assign this permission set to Community users.


Create Community Users

1. Create a new Account.
a. Enter “Accounts” in the All Apps menu search.
b. Click Accounts.
c. Click New.
d. Enter an Account Name . (We suggest using “Community Account”, but the
Account Name can be anything.)

e. Click Save.
2. Create a new Contact.
a. Enter “Contacts” in the All Apps menu search.
b. Click Contacts.
c. Click New.
d. Enter a First Name and Last Name .
e. Set Account Name to the Account created in Step 1.
f. Enter a phone number in the Phone     eld.

g. Click Save.
3. Create a new user.


a. In the Contact you just created, click the Enable Customer User button. (The button
is only available if your org has Community access enabled.)
b. Enter an Email .
c. Enter a User Name
d. Set License = “Customer Community Login”.
e. Click Save.
4. Assign a permission set.
a. Click the Gear icon in the upper right-hand corner.
b. Click Setup.
c. Type “Permission Sets” in the Quick Find box.
d. Click Permission Sets.
e. Click the permission set you created in Setup Steps for Assigning
f. Permission Sets to a Community User.
g. Click Manage Assignments.
h. Click Add Assignment to assign users to the permission set.
i. Add the user you created in Step 3 and click Assign.


Sharing From Phone Number to the Community users

1. Add an Account lookup to the Phone Number object.
a. Click the Gear icon in the upper right-hand corner.
b. Click Setup.
c. Click the Object Manager tab.
d. In the Quick Find box, enter “Phone Number”.
e. Click Phone Number.
f. Click the Fields & Relationships tab.
g. Click New.
h. Select Lookup Relationship .

i. Click Next.
j. Set Related To = “Account”.
k. Click Next.
l. Enter a Field Label and Field Name .
m. Click Next.
n. Click Next.
o. Click Next.
p. Click Save.
2. Populate the Account in a Phone Number record.
a. Go to the Messaging app.
b. Open the Phone Number Tab that you want to share with a Community user.


c. In the Account      eld, add the Account you created in Create Community Users –
Step 1.
d. Click Save.
NOTE: If you want to make Phone Numbers available to other communities, clone
the Phone Number record and add different Accounts to the Phone Number record.
3. Your Phone Number sharing journey begins here.
a. Go to Setup.
b. In the Quick Find box, search for “Digital Experiences”.
c. Open the Digital Experiences folder and click Settings.
d. Scroll down to the Sharing Sets section.
e. Click New.
f. Set Label = “BT Messaging Phone Number Sharing”.
g. Click into the Sharing Set Name      eld.
h. In the Select Pro les section, select the pro le of the Community users that you
want to use the From Number .
Example: Customer Community Login User and Customer Community Plus Login
User
i. In the Select Objects section, add the Phone Number object to the Selected Objects
column.
Note: The Phone Number object should be Public Read Only for Default External
Access in OWD.
j. In the Con gure Access section, click Set-up.
i. Set the Account for the user.
ii. Set Target Phone Number = “Account__c”.
iii. Set Access Level = “Read Only”.
iv. Click Update.
k. Click Save.


March 2023 - Version 3.38
The Messaging app Version 3.38 includes Patch updates 3.36.1 to 3.36.7 and the updates listed below.


Task Trigger

Description
When an SMS message was sent with missing From Phone or To Phone Numbers, the user
received an unhelpful error message that could not be tracked.


Resolution
Using the Task Trigger will create an error message that is better de ned and can be tracked from Apex
Jobs.


Backend Process Updates for the Smart
Scheduler
The backend process has been updated to support the Smart Scheduler component with the Events
app.


Preview/Test SMS will not show in the RLC and Conversations tab.
Messages that are sent through Smart Scheduler using an SMS template will be attached to
the SMS Message record.
Selecting the SMS action in the Smart Scheduler will open the messaging component for
composing messages (Template attachment and Media attachment).
When you select the SMS action, you will see the SMS Balance in the Smart Scheduler
component.


Version 3.36.7

Lightning Component Cutting Off Large
Scheduled Messages

Description
Customers who use the Messaging Lightning Component to schedule messages with more than 256
characters had their messages cut off, rather than the whole message being sent. This only happened
when using the scheduling feature.


Resolution
The end user will now receive message with content greater than 256 characters when Messages are
scheduled through the Record Level Schedule feature.


Version 3.36.6

Issue with Date/Time Merge Fields in SMS
Templates

Description
After applying merge tags on custom and standard date/time elds, only the date eld will be
populated. The time eld is left blank.


Resolution
An SMS Template will include the date and time values in the message body when the merge tags on
the custom/standard date/time elds are used, the Time Zone is included, and the message is sent via
an invocable method.


Account with Unlimited Phone Numbers
Subjected to Limit

Description
A customer with unlimited phone numbers is receiving an error and being limited to 200 phone
numbers when they try to add more than 200 phone numbers.


Resolution
The way the system retrieves phone numbers has been updated to allow the system to display 200+
phone numbers.


Version 3.36.5

Issue when Upgrading the Messaging Trial
Version

Description
When upgrading the Messaging trial version via the Upgrade Account button, the Business
Registration Number Type        eld’s picklist values are not available, even though the eld is mandatory.


Resolution
We have updated the Upgrade Account process to ensure the Business Registration Number Type
eld picklist values are available.


Version 3.36.4

A2P Registration

Description
The Business Registration Number Type was missing its picklist values.


Resolution
The picklist values have been added to the eld.


Version 3.36.3

Legacy Utility Component Removed from
Package

Description
A user had the following error message when logged into the Messaging Admin tab.


Resolution
The Conversation Legacy from the utility on Textey App was removed.


Version 3.36.2

Power Dialer: Component Error

Description
The error message "A component error has occurred" has occurred while running the powerdialer and
occasionally when opening Lead records.


Resolution
External IDs will now populate correctly, stopping the error from occurring.


Apex Errors

Description
The customer intermittently received the following Apex Error from Salesforce when users sent
messages from the Lead record.


Resolution
Created a method to terminate previous jobs if they are already in the system. We have tested with
multiple users by terminating the jobs scheduled by the other users.

We will perform a backend sort when the actual job is running. If the job already exists, we will not
schedule it again!

NOTE: This issue still exists and occurs in different ways. The team is working on a robust x!


Slowness in the Org

Description
A user recently upgraded the Blackthorn Messaging app managed package and noticed extreme
slowness in their org.


Resolution
We updated the Utility Functions and functionality to identify the operating console and worked on the
Console App related library.


Version 3.36.1

Issue with Adding New Payment Method

Description
The customer received an error message when trying to add a new Payment Method in the Textey
Administration tab.


Resolution
This was a backend issue with the API. A patch version has been released. Alternatively, you can
follow the steps below.

NOTE: This must follow syncing with a client.

1. Find the client's Account ID located on the Messaging Admin tab.
2. Search for the account in the Blackthorn Messaging app.
3. Go to the Account detail page.
4. Click Edit.
5. Check the checkbox Allow Plan Upgrade .
6. Ask the client to refresh the Messaging Admin page and add a new card from the Add Card
button.
7. After the client successfully adds the card, go to the Blackthorn Messaging Account detail
page.
8. Click Edit.
9. Uncheck the Allow Plan Upgrade checkbox.


May 2022 - Version 3.36
Read on for the latest updates in the May 2022 release!


Enhancements

Alert Client if the Authenticated User is Inactive
In the Blackthorn Messaging Admin, Authenticated User is responsible for creating Incoming messages
records. If the authenticated user is not active in Salesforce then no incoming messages data will be
created.


Plaintext                                                                                      Copy

Messaging Admin > Administration > Settings > Authenticated User
Section


In this release, we made sure that when the Authenticated User is Inactive, an email alert will be sent
to the Customer/Client via Primary Contact. Also when the Authenticated User is Inactive, the
Messaging Admin tab in Salesforce will give an error message.


Alert Client if the User is not Authenticated
Since there is not a User Authenticated, there will not be incoming message records created in
Salesforce. We need to make sure that the Authenticated User is set up. An error message will appear
for setting up the user, and an email alert will also be sent to the Contact.


Plaintext                                                                                      Copy

Messaging Admin > Administration > Settings > Authenticated User
Section


Auto Response Message
Updates have been made to the following scenario: an End User sets up the Auto Response (After
Hour SMS) and receives a text message after hours.


Previously
If the User/Client sent an after-hours text message to the End User, the User/Client would receive an
auto-response message from the End User.


Update
If the User/Client sends an after-hours text message to the End User containing the keywords: STOP,
END, CANCEL, QUIT, and UNSUBSCRIBE, an auto-response message will not be sent to the End User.


Admin Con guration: Object Picker vs API Names
Default Search Objects
Parent Objects for Reply


Plaintext                                                                                    Copy

Messaging Admin > Administration > Settings > Message Tab > Inbound
Message Settings


In this release, we have introduced a Multi-Select picklist where the Admin can see all the objects that
are related to sending and receiving messages.


Twilio Messaging Policy
Twilio has updated its Consent Policy. All Organizations that are using the Blackthorn Messaging app
must also follow the new policy.

In this release, we have introduced a pop-up alert message that appears when the user sends a
message to a new number for the rst time.


For RLC
Once Per Recipient
For each phone number, the Salesforce sender will get a pop-up when sending the very rst message.


Outbound Message should be appended with a Signature.
Users will continue to see the pop-up until the recipient replies to the message.

To change the settings, go to: Custom Settings > Blackthorn Messaging Settings > Consent Popup
Frequency

Once Per Sender
The Salesforce sender will get a pop-up only once.

Outbound Message should be appended with Signature.
The outbound message signature should be appended if there is no reply from the recipient.
The custom setting will work at the user level.

The change the settings, go to: Custom Setting > Blackthorn Messaging User Preference > Consent
Con rmation > True


For Bulk SMS

Users will see a pop-up when they send a message with the following conditions:

The Signature on the message will not append if the conversation exists between the #To &
#From number pair.
The Signature on the message will append for the rst message to the recipient number.


Consent Pop Up Messages


The very rst message will contain Organization Name with HELP/STOP guidance.


Upgrade Instructions
1. Review the Enhancements in this article.
2. Install updates from the Blackthorn Candy Shop.


April 2022 - Version 3.34
Read on for the latest updates in the April 2022 release!


Enhancements

Upgrade Plan Screen
The Upgrade Plans screen UI has been updated. New Customers will now see the options listed
below.


Button Alignments

Upgrade Plan Button


The button alignment has been changed along with the text and color under the Messaging Admin.


Change Credentials
Removed the red color and made sure that the button is in sync with the Upgrade Account.


Contact and Company Information


When the customer is upgrading for the rst time, the details will be pre-populated from the org
company information. Afterward, the A2P will show the information from the API that the customer
has submitted.


Bug Fixes


Date/Time Issue: Fixed the issue with showing Today/Tomorrow in the RLC component.
Filters in code need to apply to the date as well as the time format.


Watch video on YouTube
Error 153
Video player configuration error


Watch on


Phone Number Lookup: Whenever the “Number Type” eld is blank on the Phone Number
Lookup record, the users were facing issues when sending the SMS. Now the issue has been
handled in the RLC component where we have a warning message on the Phone Number
when we hover over.


Scheduled Batch: We have an Apex Class “ScheduledBatchRLC” which doesn’t run
continuously. In the present day, we have to raise a Salesforce case to do it. Now with the
new release, the “ScheduledBatchRLC” auto-sync job will be up and running continuously.
Attempt to dereference null object error: When the customer was trying to send bulk
messages from Opportunity the issue of dereference null object has been identi ed. This is
now xed and handled in this release by creating the eld “Do_Not_SMS__c” on the
opportunity which already exists on other objects (Accounts/Contacts/Leads).


Upgrade Instructions
1. Review all Enhancements and Bug Fixes in this article.
2. Install updates from the Salesforce AppExchange.


January 2022 - Version 3.30
Read on for the latest updates in the January 2022 release.


Enhancements
Scheduled Jobs. Select a date and time in the future and rest assured that your message will
be sent whether you're at your desk or on the go.
Scheduled Messages. The users can view the scheduled messages and perform different
actions on these messages like Editing the Message, Rescheduling the Messages, Canceling,
Deleting and Sending it right away!
Auto Response. Never to wait on a text anymore. The user can set up an auto response
outside of their working hours & holidays.
Disallow Users from Sending Attachments in Messages (Custom Permission). Added a
new custom permission, “simplesms.Prevent Textey Attachments” which will disallow users
from sending attachments in SMS messages.
Click to call with CTI. Integration with different call centers.


Bug Fixes
Resolved the issue with User's Locale settings and also Date/Time conversion.
Normalization of the phone numbers.
Resolved an issue in a previous version where an Apex automation could fail if using SMS
Template that did not contain any merge elds.


October 2021 - Version 3.27
Read on for the latest updates in the October 2021 release.


Enhancements
Auto Recharge your Message Balance. Never run out of messages again. You can now
automatically add more messages to your account when your balance falls below your
desired threshold.
Filter your Inbox using Conversation List Views. This option opens up many more ltering
options for your inbox. Create list views on the Conversation object and use those list views
for your inbox lters.
Set a Default From Number. When a user has access to send text messages from multiple
phone numbers they can now choose which one shows as the default.
Con gure Default and Excluded Phone Fields by Object. When sending text messages
from a record you can now con gure which phone elds are displayed in the To drop-down
in the Messenger. Sometimes you'll want to default a certain eld and even exclude some
elds from showing up.
Set the number of messages that load in the Textey Messenger. For better performance in
the Textey Messenger component you can set a default page size of the number of messages
that load when the component loads.
Set the number of conversations that load in the Textey Inbox. For better performance in
the Textey Inbox you can set a default page size of the number of Conversations that load
when the Inbox loads.
Sticky sidebar on the Textey Inbox. If you open the sidebar on the Textey Inbox it will
remain open as you click into different conversations.
A2P Messaging form included in Textey Administration page. To support the new A2P
Messaging routes we have included the required registration form directly in the signup
process located in the Textey Administration page.
Improved File management for MMS attachments. Now you can leverage Salesforce
Libraries to control and manage which les can be sent in text messages.
Enhancements to invocable apex class. You can now send bulk messages of different object
types and templates.
Real-time check for Opt-Out when sending scheduled Bulk SMS. Now when you schedule
a bulk message, either from a Campaign or List View, the Do Not SMS checkbox on the
record will be used to determine whether or not to send the message to the recipient. This
means that if someone opts-out after you've scheduled a message that includes them they


won't receive that scheduled bulk text.


Bug Fixes
The Next Payment Date shown on the Textey Administration page would in some cases be
blank.
Resolved issue where Textey Messenger would not load on a Community page layout.
Resolved issue where Campaign lookup eld on the SMS Message record was sometimes
blank when sending a bulk message from a Campaign.
Resolved issue where animated GIFS were not animating when viewed in the Messenger.
Resolved broken icons within the Messenger when viewing certain le attachments.
Resolved issue where List Views that referenced a parent record would sometimes cause an
error when used as a conversation lter.
When ltering on an SObject list view in the Textey Conversations component there could be
an error if using a related record eld in the list view lter. For example, if you created a
Contact list view and ltered on a eld like "Account.Name" then an error might have been
generated when you tried to lter your conversations using that list view.
When an org had Multi-Currency enabled there could be a problem where Conversation
records were not created properly.
When sending an automated text using the invocable "Send Textey Message" apex action,
sometimes when the recipient's area code started with "44" (i.e. "443-555-5555") then it
con icted with the UK country code of "+44" and the message would not be sent.
Resolved an issue in a previous version where an Apex automation could fail if using an SMS
Template that did not contain any merge elds.


March 2021 - Version 3.18.3
Read on for the latest updates in the March 2021 release.


Enhancements
We've added support for International Text Messaging (limited pilot). Reach out to
support@textey.io if you have a use case for messaging outside of the US & Canada and
want to learn more.
An additional option was added to the Conversation Ownership Routing feature. This new
option is called Last Sent Message Owner. This option will route the ownership of a
Conversation to the user who sent the last outbound text message to the recipient.
When the owner of a Conversation is changed this event is streamed to all Textey
components. This creates a real-time UI update and could immediately add/remove this
Conversation from a user's inbox depending on their lters.
The Textey Messenger component can now be added to a Conversation record page layout.
This allows users to navigate to a Conversation record and converse directly from there. This
is helpful if you route Conversations through Salesforce Omnichannel as Work Items and
want to be able to open the Conversation record and conduct the text message conversation
from there.
Clicking a link from any of the Textey components, while in a Console application, will open a
subtab of the Console instead of opening an entirely new browser tab.
When a user is in the Textey Messenger component and clicks the To drop-down eld they
can hover over the phone eld label to see the actual phone number.
A new checkbox eld named Allow Media has been added to the Phone Number object.

Unchecking this box on the Phone Number record will remove the attachment icon when a
user is sending from this phone number, thus they would not be able to send an attachment.
We have added support for sending two additional types of les as MMS. It is now possible
to send PDF les and vCard les (aka Virtual Contact Files).


Bug Fixes
RESOLVED: The Add Messages to Contact on Lead Conversion setting was not re-parenting
Conversation records from Leads to Contacts. Only SMS Message records were being added
to the new Contact, but now the Contact => SMS Message structure is preserved and moved
altogether when a Lead is converted.


RESOLVED: When a new Conversation is created the inbound SMS Message record that
created the Conversation will also be owned by the user who the Conversation is routed to.
Previously the SMS Message record might have been owned by a different user than the one
who the Conversation was routed to.
RESOLVED: We noticed that duplicate SMS Message records were created when using the
Invocable_SendMessage apex class even when the text messages were not actually sent to
the recipient.
RESOLVED: There were instances where SMS Message records could be associated to the
wrong parent records when a list of messages was sent through the
Invocable_SendMessage apex class.


November 2020 - Version 3.13
We are excited to announce the release of Textey version 3.13!


Phone Number Lookups
Phone Number Lookups is a new feature that lets you identify the line-type of a phone number. A
phone number's line type can be mobile, VoIP, or landline. When you send text messages to landlines
you are still charged for the attempted delivery of that message, which leads to wasted messages and
unnecessary costs.

Learn more about Phone Number Lookups here.


Changes to Inbound MMS
When you receive an inbound image a Salesforce File will now be created for that image and saved
related to the Media record. Your images will still be visible as before. Learn more about these changes
here.


Improved Reports and Dashboards
There are two new Dashboards included with this version. The dashboards are named:


Textey Dashboard (Lightning)
Textey Phone Number Lookup Dashboard

These have been improved with more underlying reports and take better advantage of new Lightning
dashboard components.


Bug Fixes and Improvements
Fixed UI issue where the Utility Bar was being cut off at the bottom after Winter 21 update.
When converting a Lead, all Conversation records will now be moved to the new Contact.
Improved a query that could timeout on large SMS Message datasets when an inbound
message is received.
Fixed known issue where some SMS Message records are associated to the wrong Parent Id
when sent from the Invocable_SendMessage.sendMessage() method from apex.


April 2020 - Version 3.5
We are excited to announce the release of Textey version 3.5! This release has several new features
that will expand on your ability to manage conversations. Let's take a look at each one.


Conversation Ownership Routing
You now have more control over how your SMS conversations are routed internally. This feature lets
you determine new conversation ownership per phone-number. The conversation owner can be set to
a speci c user or queue, or it can be set to dynamically detect the owner of the related record (i.e. Lead,
Contact, Account, etc). Read more about Conversation Ownership Routing here.


Accept and Transfer Conversations
You now have the ability to accept and/or transfer ownership of individual conversations. This is a great
feature to use in conjunction with ownership routing, and lets users assign a conversation to
themselves or to another user. Read more about Accepting and Transferring Conversations here.


Real-Time Conversation Updates
This includes several new enhancements aimed at keeping your team in sync with each other as they
monitor and respond to conversations. Check out the new features like typing indicators, real-time
synchronization of outbound messages, ownership changes, and conversation status updates. Read
more about Real-Time Conversation Updates here.


Merge Conversations
There may be times when you need to merge a new conversation into an existing one. You can now
perform that action from the Textey Conversations inbox or from a record page. Read more about
merging Conversations here.


Mass Close Conversations
You may end up with stale conversation records over time, especially if users don't end a conversation
in a timely manner. A stale conversation is one with an "Open" status, yet there hasn't been any recent
messaging activity. You can now create a list view of these conversations and perform a mass close
function. Read more about how to use the Mass Close Conversations feature here.


Saved Conversation Filters
You can now save pre-de ned conversation lters and switch back and forth between them for
convenience. This allows you to easily navigate between your different views without having to re-
select the lter criteria.


Link Tracking Display
Link tracking is a popular feature that lets you know if someone has clicked a trackable URL in your
message. However, before now you had to look at the SMS Message record to see if it was clicked.
This new feature will let you see if a link has been clicked as you scroll through the message history,
saving you time and clicks.


Bug Fixes and Performance Improvements
We are always working hard to improve the look and feel of Textey, while improving the application's
performance and eradicating any bugs that we (or you) might nd.


