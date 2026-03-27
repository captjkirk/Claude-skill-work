# Blackthorn Compliance - February 2026

Table of contents
Blackthorn Compliance

Installation Guide
Extend Blackthorn Compliance to Other Objects


## Auditing


How to Run an Audit
Schedule Audits via Apex
Why Can't I Mask Existing Emails?
Add the Audit Tab to Blackthorn Compliance


Blackthorn Compliance

FATQ's: Frequently Asked Technical Questions


## Detection Patterns


Detection Patterns
How to Con gure Detection Patterns
How to Create Negative Detection Patterns
Supported Detection Patterns


Blackthorn Compliance

Supported File Types - SecureAttachment
API Limits - Secure Attachment


## Customize Blackthorn Compliance with Apex


Customize Blackthorn Compliance with Apex
How To Write Custom Blackthorn Compliance Apex Triggers
Example: Custom Trigger for EmailMessage
Example: Custom Trigger for Attachment


Blackthorn Compliance

Change AppExchange Payment Method


## Extension Packages


Extension Packages
Con gure for Email-to-Case
Con gure for Chatter


Con gure for Salesforce Chat (Live Agent)
Con gure for Attachments and Files


## Install / Setup SecureAttachment


Install / Setup SecureAttachment
Install SecureAttachment
Setup SecureAttachment (after installation)
Upgrade SecureAttachment
Difference between Attachment and ContentVersion (Salesforce Files)


## Debugging and Errors


Logging: The Log Object
How to Stop False Positives
My Credit Card Didn't Get Masked!


## Compliance Release Notes


Compliance Release Notes
Compliance - November 2025 - Version 3.9.1
Compliance - January 2025
Compliance - February 2024


### 2023


Compliance - July 2023
Compliance - April 2023


### 2022


Compliance - December 2022
Compliance - October 2022
Compliance - July 2022
Compliance - June 2022
Compliance - March 2022
Compliance - February 2022


### 2021


Compliance - November 2021
Compliance - December 2021
Compliance - Release 3.71
Compliance - Release 3.6
Compliance - Release 3.2
Compliance - Release 3.0


Installation Guide

ICU Local Format Requirements


To ensure Compliance meets Salesforce’s upcoming ICU Local Formats requirements, all
classes in the Compliance repository will reference API version 45.0 or higher.


Start Here
Navigate to the latest version of Blackthorn Compliance.

1. Click Get It Now on the AppExchange listing.
2. Select Log In, and enter your Production Salesforce credentials.
3. Choose the environment where you’d like to install Blackthorn Compliance.


4. If you are already logged into the Salesforce instance where Compliance will be installed,
you’ll be redirected to a con rmation page for the installation. Otherwise, you will be directed
to a login screen where you can enter the credentials for that environment.


5. When prompted to select the pro les that will be able to access the installed application,
leave the default, Install for Admins Only, and click Install.


6. Compliance will now be installed in your Salesforce org.
In most cases, this page will automatically refresh noting whether or not the
package was installed successfully.
For orgs that have complex logic/code already applied, the installation process may
take longer. In this case, an email will be sent to the email address associated with
the user who performed the installation, either con rming the success or failure of
the installation.
7. After installation, the Compliance package will be visible on the list of Salesforce Installed
Packages in Setup.


How Compliance Works


You’ve installed Compliance -- now what? Good news! Compliance is already blocking credit card
numbers from entering your Salesforce org. When Compliance is installed in your Salesforce
environment no new records can enter Salesforce with a credit card number.


Are you using a Compliance trial?


When using Compliance during a trial period, only three records or les can be agged or
deleted. The fourth record will not be masked, although a Log le with the following message
will be created. “This record was not masked as this org’s license has run out of masked record
allowances. Contact Blackthorn.io for questions.”


Detection
Detection is Compliance-speak for “stopping credit card numbers from coming in” . Compliance
Detection processes entire strings of text for numbers that match the format of known credit card
issuers. Not only that, but Compliance also determines whether the detected number is a valid credit
card. This is important because there are lots of other numbers that match similar credit card number
formats: order numbers, phone numbers, etc. Compliance never masks a number unless it is a
completely valid credit card number.


For example, when a new Case record is created, and the Description contains a number that matches a
known issuer format, Compliance will check whether the number is a valid credit card. If the number is
a valid credit card, then Compliance will appropriately mask the number before the Case is even saved.


Types of Credit Cards

What Types of Credit Cards Does Compliance Detect?

While we’re pretty good at detecting credit cards, we can’t predict the format of every type of credit
card on the planet. Compliance comes with detection patterns for the following credit card issuers:


American Express
Discover
JCB
MasterCard
Visa


China UnionPay
Diners Club Carte Blanche
Diners Club
Interpayment
Instapayment
Maestro
Dankort
Solo
UATP

Note: If you need to detect credit card number types not listed here or other Personally Identi able
Information (PII) (e.g. social security numbers) then check out Detection Patterns.


Credit Card Formats

But what if the credit card isn’t in the right format?

It doesn’t matter! Compliance will detect the following formats:


4111111111111111
4111 1111 1111 1111
4111-1111-1111-1111
411111111111*1111
3124567890411111111111111109876543
“Here is my valid credit card 4111111111111111 thanks!”

Here is an example of what Compliance will not detect: 4111%1111&1111*1111.


Audit
Auditing is Compliance-speak for “ nding the credit card numbers already stored in Salesforce” . Audit
actually uses the exact same technology as Detection, except it scans your historical Salesforce data for
credit card numbers.


**Example: **Let’s say you have a bunch of Cases from 2016 with credit card numbers stored on them.
You would simply con gure an Audit to run across all Cases in 2016. Audit will automatically nd the
credit card numbers, mask them, and send you an email when it’s done.


When you have completed an Audit, Compliance stores the results in records called “[Logs](doc:
logging-the-log-object)”. These Log records drive the native reporting and dashboards for
Compliance. Check out the Analytics tab for more information on Audit results.


Detection and Audit Actions
Actions in Compliance are “what happens when you nd a credit card number”. The default action is to
mask the number upon detection, but you are also able to Report and Delete records.


Mask
When a credit card number is detected, the default (and recommended) Action is Mask. This means that
the credit card number is masked, and permanently removed from your Salesforce org. This is NOT the
same as encryption - you cannot get the data back once it’s been masked!


Report

But what if I don’t want to mask the numbers? Great! You can also simply Report the records that are
agged as containing credit card numbers. You would still need to manually remove the numbers from
the records later.


Delete
Better safe than sorry! For some customers, they don’t want to risk the chance of storing any PII. If a
customer sends their credit card number to you, what’s the likelihood that they’ll send other sensitive
information? Selecting “Delete” for your Audit or Detection Action will delete the entire record if a
credit card number is detected. For example, if a valid credit card number is detected in the body of an
Email Message - the entire record is deleted.


Detection Patterns


Detection Patterns are how Compliance nds credit card numbers and other PII. We use a combination
of Regular Expressions (RegEx) to match speci ed patterns of numbers. The Custom Metadata Type
“DetectionPattern” comes pre-con gured with 15 patterns. These patterns are the most likely
instances of credit card numbers to be found in your Salesforce org. You may turn some of these off if
you would like, and you can even add your own patterns!


Credit card numbers are given special treatment in Compliance. When a Detection Pattern is a “Credit
Card Pattern”, we go beyond a simple RegEx match - we also make sure that the credit card number is
valid. This way we can avoid false positives getting masked accidentally. Check out the section
Con gure Detection Patterns for how to set up your own patterns.


What Objects Does Compliance Support?
While Compliance can be extended to support any object in Salesforce, it is pre-con gured to support
the following objects.


Object                              Precon gured Detection Fields


Case                                Subject, Description


Case Comment                        Comment Body


Task                                Subject, Description


Instant upgrades are available for the following objects.


Object                        Precon gured Detection Fields              Required Package


Attachment                    Body                                       Compliance-Files


Content Version               Version Data                               Compliance-Files


Feed Item                     Title, Body                                Compliance-Chatter


Feed Comment                  Comment Body                               Compliance-Chatter


Email Message                 Subject, Text Body, HTML Body              Compliance-Email2Case


LiveChat Transcript           Body                                       Compliance-LiveAgent


If you need to detect credit card numbers on other objects in Salesforce then check out Extending
Blackthorn Compliance to Other Objects for how to add your own objects to Compliance.


Con gure Compliance
Note: Compliance is a Lightning App. If you are a Salesforce Classic User, you will need to temporarily
switch to Lightning Experience before con guring Compliance. You can switch back to Classic after
you’re done. It is not required to have enabled Lightning Experience for your Salesforce Org or any
Users.

When you install Compliance - nearly all of the con guration is already done for you. Depending on
your Salesforce org, you may choose to not make any changes to the default con guration. We
recommend that you consider keeping the con guration as-is before making changes.


Setup Con guration
1. If you are a Classic User, click the Switch to Lightning Experience link. Otherwise, go to the
next step.


2. Open the App Launcher menu.


3. Select Blackthorn Compliance.
4. If you want to con gure a speci c object, click the object name.


5. Otherwise, navigate to Setup > Custom Code > Custom Metadata Types > Manager >
Manager Records.
6. You should see a list of Manager records.


7. Press Edit on the object you wish to con gure.


8. Enter a comma-delimited API name for Salesforce elds in Detection Fields (must be less
than 255 characters).
Do not add any trailing commas or spaces.
Any elds which are over 255 characters will not be included in masking.


If you need more than 255 characters, add your additional elds to
DetectionFieldsPlus.


9. Select Detection Action.


Update: Masks credit card numbers Compliance detects on records. Compliance will create a
Log record when this action occurs.
Report: Creates a Log record when this action occurs but will NOT mask the credit card
number. You can view the reported records in the PCIFY Reports Folder.
Delete: Deletes the entire records (Case, Email Message, etc) if PII is detected.


10. Press Save.

All Done! Next up, you should learn How to Run an Audit to remove PII from your existing records.


Performance and Scale Testing
Performance and Scale testing must be pre-approved by both Salesforce and Blackthorn. Please
complete the steps below.

1. Follow the guidance provided by Salesforce and seek Salesforce approval.
2. Once you obtain Salesforce approval, submit a case to Blackthorn with your plan and detailed
testing scenarios. You will be able to upload attachments after your ticket has been opened.
3. If approved, Blackthorn will work with you to determine an optimal date and time to run your
tests.

Please read Performance and Scale of Your Experience Cloud Site for additional resources.


Extend Blackthorn Compliance to Other
Objects
Blackthorn Compliance comes preloaded with Detection and Auditing for many standard objects, but
what if you want to detect credit cards on custom objects or other standard objects?


Part One: Create a new Manager Record
1. Create new Compliance Manager Record. Go to Setup > Custom Code > Custom Metadata
Types > Manager > Manager Records > New.


2. Enter the API Name of the Object in the Label     eld (must be exact API Name).


3. Enter the Name of the Object in the Manager Name      eld (cannot contain consecutive
underscores).
4. Enter the comma-delimited API names for Salesforce elds in Detection Fields (must be
less than 255 characters).
Do not add any trailing commas or spaces.
Any elds which are over 255 characters will not be included in masking.
If you need more than 255 characters, add your additional elds to
DetectionFieldsPlus .


5. Select a Detection Action .
6. Press Save.


Part Two: Extend Compliance with an Apex
Trigger
NOTE: If you are running Compliance Audits only, then you can skip this step. If you don’t need new
records to be processed and are only cleaning up old records, you can skip this step.

Now we’ll need to get a little advanced by writing a super easy Apex Trigger on the Object you are
extending Compliance to.

1. Create a new Apex Trigger for the Object:
Classic: Setup > Create > Objects > Click on the Object name > Triggers > New
Lightning: Setup > Object Manager > Click on the Object name > Triggers > New
2. Copy & Paste the following lines of code (replacing all “NewHouse” references with the API
name of the Object you wish to extend PCIFY to).


Plaintext                                                                                    Copy

trigger NewHouseTrigger on NewHouse (before insert, before update) {
if (pcify.Manager.isOnline('NewHouse')) {
pcify.Processor.maskCreditCards(                                Trigger.new,
pcify.Manager.getMaskFields('NewHouse'),                                'NewHouse'
);       }}


3. Press Save.
4. Navigate back to the Compliance App.
5. Turn on Detection for the Object.

You should see the following alert noti cation.


Congratulations! You have successfully added a new Object to Compliance.


How to Run an Audit
Auditing is an important part of any Blackthorn Compliance implementation. Auditing is how you get
rid of all the Personally Identi able Information (PII) that you already have in your org. Follow the
steps below to easily scan any Salesforce records for PII.

1. Navigate to the Audit tab.


2. Select an Object to Audit.


3. Select Audit Start Date and Audit End Date .


Audit Start Date is the Created Date from which Audit will start querying for records. Audit End
Date is the Created Date at which Audit will stop querying for records.


Note: You can change the default Audit date range eld to any other DateTime eld (such as
LastModi edDate) by changing the AuditDateField in the Manager Custom Metadata Type.


4. Select Audit Action .


"Mask" will permanently redact credit card numbers Compliance detects on records according


to the Mask Type con gured for that record’s object.
"Report" will create a Compliance log record if a credit card number is detected but will NOT
mask the number. You can view the reported records in the PCIFY Reports Folder.
"Delete" will delete the ENTIRE record if a credit card number is detected in ANY eld.

Note: Existing EmailMessages do not support Mask. For more information, go here.


5. Press RUN.
You should see the following success alert:


You will receive an email con rmation when the job is done.


Important Notes
Depending on the Audit dates selected and the Audit Action, the Audit could take a few
minutes to a few hours. We recommend testing your rst audit with a month, and then
expanding the date range to include years of records.
Masking will not be applied automatically after the creation of a new pattern since masking is
only applied when a record is created or altered.


Schedule Audits via Apex
1. Create a Schedulable Interface using the following example to call the Compliance
namespace.


Plaintext                                                                                   Copy

global class ScheduleAudit implements Schedulable {
global void execute(SchedulableContext sc){
String objectName = 'Case'; // or pass another object name
pcify__Manager__mdt manager =
pcify.Manager.getManager(objectName);

pcify.Batch batchJob = new pcify.Batch();
batchJob.objectName = manager.MasterLabel;
batchJob.fieldNames =
manager.pcify.Manager.getMaskFields(objectName);
batchJob.startDate = manager.pcify__BatchStartDate__c; // or
pass your own datetime value
batchJob.endDate = manager.pcify__BatchEndDate__c; // or pass
your own datetime value
batchJob.filterField = manager.pcify__BatchFilterField__c;
batchJob.queryLimit =
Integer.valueOf(manager.pcify__BatchQueryLimit__c);
batchJob.batchSize =
Integer.valueOf(manager.pcify__BatchSize__c);
batchJob.action = manager.pcify__AuditAction__c;
batchJob.loadQuery();
database.executebatch(batchJob, batchJob.batchSize);
}
}


2. From Setup, enter Apex Classes in the Quick Find box, select Apex Classes, and then click
Schedule Apex.


3. Specify the name of a class that you want to schedule (i.e. "ScheduleAudit").
4. Specify how often the Apex class is to run.
For Weekly—specify one or more days of the week the job is to run (such as
Monday and Wednesday).
For Monthly—specify either the date the job is to run or the day (such as the
second Saturday of every month).
5. Specify the start and end dates for the Apex scheduled class. If you specify a single day, the
job only runs once.
6. Specify a preferred start time. The exact time the job starts depends on service availability.
7. Click Save.


Why Can't I Mask Existing Emails?
There is a Salesforce limitation which prohibits us from updating/masking existing emails. This is the
feature:

update() is supported when an email record is in Draft status, and IsPrivateDraft is false. It is
also supported if Status and IsPrivateDraft are true and CreatedBy is associated with the current
user. When the email record status is not in Draft status, the IsExternallyVisible eld and custom
elds only can be updated.


This means that once an email is sent, it can no longer be updated, even manually. Since some emails
will contain Personally Identi able Information (PII), they will need to be deleted. Before deleting the
emails run an Audit with the Action set to "Report". Once you are comfortable deleting the emails, run
a second Audit with the Action set to "Delete" (or delete them manually).


Add the Audit Tab to Blackthorn
Compliance
1. Edit the Compliance Lightning App: Setup > Apps > App Manager > Compliance> Edit.


2. Click on Navigation Items in the App Settings.
3. Add the Audit tab to the Selected Items.


4. Press Save.


5. Navigate back to the Compliance Lightning App.

NOTE: Sometimes Lightning Tabs don't show up right away. You may need to refresh a few times or
log out/in in order for the Audit Tab to show.


FATQ's: Frequently Asked Technical
Questions

Masking
Q: Can you mask other objects like Contact and Account or custom objects?
A: Yes! You simply need to add these objects to Blackthorn Compliance con guration. Follow these
helpful steps.

Q: Can you mask other Personally Identi able Information (PII) data like social security numbers,
driver's licenses, and IP addresses?
A: Yes! You will need to create your own PII patterns in the Compliance con guration. Follow these
helpful steps.

Q: Can you mask mixed PII data that has a combination of letters and numbers?
A: Yes! Compliance supports matching mixed data types that include alpha, numeric, and special
characters.

Q: Can you unmask data if you need to still see the underlying information?
A: Masking is a permanent alteration of the data. That means the underlying data is not accessible and
therefore not editable, viewable, or searchable.

However, you can still do two things:
* Partial Masking: Mask everything but the last 4 characters so you can still verify SSNs, etc
* Report PII & Mask Later: Set Compliance to " ag" the records that are detected with PII, and then
automatically mask them later either with a scheduled mass update after your team has veri ed the
information, or mask individual records from a report generated by Compliance.

Q: I'm testing Compliance, and it's not masking my credit card. W hat's going on?
A: See My Credit Card Didn't Get Masked! for more details.


Detection Patterns
Q: The user guide indicates that we must use Java Regular Expression. Do you have any
documentation on this?
A: Yes, Regular Expressions are powerful but complicated.

Q: Can we scan and identify attachments containing medical and driving license details?
A: Yes, both Compliance and SecureAttachment support matching your custom PII. You will need to
create custom detection patterns with REGEX based on the format of PII.


False Positives
Q: Does    agging False Positives prevent similar records from being caught in audits, or is this just
used for crowdsourcing? Is turning off detection for that pattern or creating a negative pattern the
only way to control false positives?
A: It is only used for crowdsourcing information, and will show up in the Analytics tab. We have a help
site section about mitigating false positives, but the main method is negative patterns. Also, if you
don't receive any Instapayment credit cards, for example, then patterns like this are worth turning off
to avoid any accidental false positives.


Logs
Q: Is deleting Logs the only way to remove them from the system after we have masked or deleted
the related record? Is there a best practice for when to delete logs?
A: The best practice here depends on whether you care about the Analytics or not. The Reports &
Dashboard are based on the Logs. If you delete them, the Analytics will be 0. If you do not want to
use Analytics, many customers use a Dataloading tool to mass delete the Logs to conserve data
storage space. We do have a script to mass-delete the Logs, but it might be better to use a tool for the
job.

Q: There is some confusion over relating a Log to a record. Does the Log always have a link to the
related record?
A: The PCIFY Logs will always have a related record in either of the following scenarios:


Records are updated (i.e., Before Update).
You ran an Audit.
Compliance detected PII in Attachments or Content Version.

Attachment and Content Version logs give you the link to the actual Content Version record and the
parent Case. Cases don't need a parent record, so the "Parent Link" eld will be blank.

Compliance Triggers are Before Insert and Before Update by default. This means that when the Email
Message or Case is created, the ID of the record does not exist yet Before Insert, and therefore there
will be no related ID in the PCIFY Log. You can disable our default Compliance Triggers and write your
own, but this requires thorough knowledge of Apex coding.


SecureAttachment
Q: Are emails containing logos and signatures scanned and counted against our SecureAttachment
API usage?
A: Images included in the body of the email message are only included as API calls if they end up in
the Attachments' Related List on the Case, as either Attachment or Content Version records.


Audits
Q: If our con guration is set to mask all but the last 4 characters, will this pattern continue to be
detected in audits? For example, if we receive an attachment with this pattern, will it be caught in
an audit? If so, do we have to modify the detection pattern?
A: Audits work the same as detecting new records. If you have con guration set to "Last4," then
during audits you will also mask all but the last 4 characters.

Q: Is detection for Content Version based on the date/timestamp of the Attachment? For instance,
if I want to isolate a particular grouping of Attachments, would I run an audit pointed to that
speci c time frame?
A: The Audit Start Date & End Dates are based on the Created Date of the record. So if you're
auditing Content Version, the date range would nd all Content Version records created between those
dates. (Note: You can change the default Audit date range eld to any other Date/Time eld type (such
as Last Modified Date ) by changing the Custom Metadata Types' Manager AuditDateField
custom eld.)

Q: I know that Attachment is the old Salesforce object and Content Version is the new one. W hen
running an audit, should we use only Object = Content Version or can we use Object =
Attachment?
A: This depends on your production org. It is possible for you to have both types of records. There is a
chance that you still have old Attachments which could have PII, even if you currently use Content
Version. Here is a useful link which explains the difference.

Q: Are the timestamps in the audit the same as our System date?
A: Yes, the "Timestamp" eld on the Logs is the same as the System Created Date         eld.


Enhanced Domains
Q: Does updating the Salesforce domain URL or Enhanced Domain have an impact on the
Compliance / SecureAttachment packages?

A: Changes to the Salesforce org/Enhanced Domain URL should not impact Compliance /
SecureAttachment since we don't reference any URLs within the app or our licenses.


Detection Patterns
How to Con gure Detection Patterns
How To Create Negative Detection Patterns
Supported Detection Patterns


How to Con gure Detection Patterns
1. Select the tab “Detection Patterns”.


2. Click on the speci c Detection Pattern Name.


3. If you’re already in the Setup, navigate to: Setup > Custom Code > Custom Metadata Types >
DetectionPattern > Manage DetectionPattern.
4. You should see a list of Detection Patterns. Click Edit on the Pattern you wish to con gure.


5. Enter a Pattern.
This pattern must be a valid Regular Expression. Try a free tool like this to check whether
your regex is valid.
6. Select Mask Character.
Enter any single character you want to mask PII numbers with - the default is an asterix (e.g.
AMERICANEXPRESS****) but you could use an X, #, @, or any other single character you
need.
7. Select Mask Type.
"Full Mask": all characters are masked
"Last4": all credit card number characters are masked but the last 4 characters


(AMERICANEXPRESS****1234)
"First6andLast4": all credit card number characters are masked but the rst 6 and
the last 4 characters (AMERICANEXPRESS123456**1234)
8. If the pattern is for credit card numbers, check the box LuhnCheck .
When this box is checked, all numbers matching this pattern will go through a
Luhn algorithm check for credit card number validity.
If this box is unchecked, all numbers matching this pattern will skip the Luhn
algorithm.


What is Luhn algorithm?

The Luhn algorithm, also known as the modulus 10 or mod 10 algorithm, is a simple checksum
formula used to validate a variety of identi cation numbers, such as credit card numbers, IMEI
numbers, Canadian Social Insurance Numbers.


9. Check the box IsActive .
10. Press Save.

Tip: It is recommended that you only store the minimum amount of credit card digits you need to verify
customer accounts.


How to Create Negative Detection
Patterns


Have you ever experienced a false positive before? Was it a tracking number that resembled a credit
card number? With Negative Detection Patterns, you can effectively exclude these numbers from
Blackthorn Compliance detection. All you need to do is create your own patterns for international
phone numbers, UPS, USPS, Fedex, and other common false positives numbers.

Important:

Numbers matched with Negative Patterns are not masked nor are logs created. No action is
the correct action for Negative Patterns.
It is possible for a record to have both valid credit card numbers and false positives.
It is also possible for the same number to be both a valid credit card number and a false
positive.


Create Negative Detection Patterns
1. Navigate to Setup > Custom Code > Custom Metadata Types > DetectionPattern > Manage
DetectionPattern.
2. Click New.
3. Enter a Label .
Must be unique - cannot be the same as other pattern names
4. Enter a DetectionPattern Name .
Must be unique - cannot be the same as other pattern names
5. Enter a Pattern .
This pattern must be a valid Regular Expression. Try a free tool like this to check whether
your regex is valid.
6. Check Negative Pattern .
This eld must be true


7. Check Partial Match .
[Optional] skips the entire eld if a negative pattern is matched.
8. Check the box IsActive .
9. Click Save.


Supported Detection Patterns
Blackthorn Compliance comes with a number of of cially supported Detection Patterns. These patterns
match with common Personally Identi able Information (PII) and other sensitive data types. Below is a
list of all Detection Patterns which comes with a Compliance subscription.


Active
Name                                 Description                          Type        by
Default
Matching pattern for an American Express credit       Credit
AMERICANEXPRESS                                                                             On
card.                                                 Card
Matching pattern for a China Union Pay credit         Credit
CHINAUNIONPAY                                                                               On
card.                                                 Card
Credit
DANKORT                   Matching pattern for a Dankort credit card.                       On
Card
Credit
DINERSCLUB                Matching pattern for a Diner's Club credit card.                  On
Card
Matching pattern for a Diner's Club Blanche credit    Credit
DINERSCLUBBLANCE                                                                            On
card.                                                 Card
Credit
DISCOVER                  Matching pattern for a Discover credit card.                      On
Card
Credit
INSTAPAYMENT              Matching pattern for an Instapayment credit card.                 On
Card
Credit
INTERPAYMENT              Matching pattern for an Interpayment credit card.                 On
Card
Matching pattern for a Japanese Credit Bureau         Credit
JCB                                                                                         On
credit card.                                          Card
Credit
MAESTRO                   Matching pattern for a Maestro credit card.                       On
Card
Credit
MASTERCARD                Matching pattern for a Master Card credit card.                   On
Card
Credit
SOLO                      Matching pattern for a Solo credit card.                          On
Card
Matching pattern for a Universal Air Travel Plan      Credit
UATP                                                                                        On
credit card.                                          Card
Credit
VISA                      Matching pattern for a Visa credit card.                          On
Card
Matching pattern for an American Social Security
SSN_US                                                                          PII         Off
Number.
Negative
UPS                       Anti-pattern to exclude UPS tracking numbers.                     Off
Pattern
Negative
USPS                      Anti-pattern to exclude USPS tracking numbers.                    Off
Pattern
Combination pattern of American Express,
Discover, MasterCard, and Visa. For improved
Credit
CREDITCARD                performance, disable the major credit card patterns               Off
Card
and enable this pattern. Masking will show
"CREDITCARD*"


Don't see what you need?
If you have other sensitive data you want to mask or remove from your Salesforce, then you will need
to create your own Detection Patterns. This is a simple process of adding a new regular expression to
Compliance's metadata.


Supported File Types - SecureAttachment
SecureAttachment supports the following standard le types:

Type               API                                 Notes
JPEG                          Images
PNG8                          Images
PNG24                         Images
PDF                           Files       Multi-page and embedded images supported
GIF                           Images
BMP                           Images
CSV                           N/A         Native - no API required
Word Document (.doc)          N/A         Native - no API required
WEBP                          Images
RAW                           Images
TIFF                          Files
ICO                           Images


API Limits - Secure Attachment
Limit                    Amount                                Notes
File Size          100MB for Files                 No limit for Word docs or CSV les
10MB for Images
Request/month      50,000 for Files                *Images API request limit depends on plan
1000 - 20,000,000 for Images*
Audit Batch Size   10 records / batch


Customize Blackthorn Compliance with
Apex
How To Write Custom Compliance Apex Triggers
Example: Custom Compliance Trigger for EmailMessage
Example: Custom Compliance Trigger for Attachment


How To Write Custom Blackthorn
Compliance Apex Triggers
Blackthorn Compliance comes with native Apex Triggers on select standard objects included in the
Compliance package. But if you want to use your own triggers instead, you simply need to change the
Manager eld "Use Own Trigger". This eld controls whether or not Compliance will execute its native
triggers. In other words, you can override our apex triggers on: Case, CaseComment, Task,
EmailMessage, LiveChatTranscript, FeedItem, FeedComment, Attachment, and ContentVersion.

Important: If you are writing triggers on a Salesforce object not included in the Compliance package,
you do not need to check the eld Use Own Trigger .


1. Navigate to the Manager Setting for the standard object, Setup > Develop > Custom
Metadata Types > Manager > Manage Records > Click on the object name.
2. Press Edit.


3. Check Use Custom Trigger .


4. Press Save.


5. Create your own Apex Trigger using the code snippet below as an example.

Sample Custom PCIFY Apex Trigger


Plaintext                                                                         Copy

trigger InboundEmailMessageTrigger on EmailMessage (before insert) {
List incomingEms = new List();         // check if Detection is
turned on for Email Message     if
(pcify.Manager.getManager('EmailMessage').pcifyisActivec) {
// collect incoming emails         for (EmailMessage em :
Trigger.new) {             if (em.Incoming) {
incomingEms.add(em);             }        }               // process
only incoming emails with PCIFY
pcify.Processor.maskCreditCards(             incomingEms,
pcify.Manager.getMaskFields('EmailMessage'),
'EmailMessage'        );    }}


PCIFY Class Methods
List of methods you can call from the Compliance namespace.


Class              Method           Parameters                    Description
pcify.Processor   maskCreditCards()      records: List   Void method for scanning text for PII
eldNames:
List
objectName:
String
objectName:     Returns Manager Custom Metadata Type
pcify.Manager     getManager()
String          for a given object
objectName:     Returns list of eld names for a given
pcify.Manager     getMaskFields()
String          object
objectName:     Returns the DetectionAction for a given
pcify.Manager     getDetectionAction()
String          object


Example: Custom Trigger for
EmailMessage

Plaintext                                                       Copy

trigger InboundEmailMessageTrigger on EmailMessage (before insert) {
List<EmailMessage> incomingEms = new List<EmailMessage>();

// if use own trigger boolean is false, then stop this trigger
and use the PCIFY managed package one
if
(!pcify.Manager.useOwnTrigger(pcify.StaticUtils.EMAILMESSAGE)) {
return;
}

// if Detection is turned on for Email Message
if
(pcify.Manager.getManager(pcify.StaticUtils.EMAILMESSAGE).pcify__isA
ctive__c) {
// collect incoming emails
for (EmailMessage em : Trigger.new) {
if (em.Incoming) {
incomingEms.add(em);
}
}
// process all incoming with PCIFY
pcify.Processor.maskCreditCards(
incomingEms,


pcify.Manager.getMaskFields(pcify.StaticUtils.EMAILMESSAGE),
pcify.StaticUtils.EMAILMESSAGE
);
}
}


Example: Custom Trigger for Attachment

Apex Trigger
Plaintext                                                         Copy

trigger CustomAttachmentTrigger on Attachment (after insert) {
List<Attachment> caseAttachments = new List<Attachment>();

// if Detection is turned on for Attachment
if (pcify.Manager.getManager('Attachment').pcify__isActive__c) {
// collect Case Attachments
for (Attachment att : Trigger.new) {
if (att.ParentId.getSobjectType() ==
Case.getSObjectType()) {
caseAttachments.add(att);
}
}
// process only case Attachments with PCIFY
if (!caseAttachments.isEmpty()) {

CustomAttachmentTriggerHandler.scanFiles(caseAttachments);
}
}
}


Apex Handler Class


Plaintext                                                        Copy

public with sharing class CustomAttachmentTriggerHandler {

public static void scanFiles(List<SObject> files) {
List<String> fileIds = new List<String>();
pcify__Manager__mdt manager =
pcify.Manager.getManager('Attachment');

for (SObject file : files) {
fileIds.add(file.Id);
}
pcifyfiles.FileDetector batchJob = new
pcifyfiles.FileDetector();
batchJob.objectName = 'Attachment';
batchJob.fieldNames =
manager.pcify__MaskFields__c.deleteWhitespace().split(',');
batchJob.fileIds = fileIds;
batchJob.queryLimit =
Integer.valueOf(manager.pcify__BatchQueryLimit__c);
batchJob.batchSize =
Integer.valueOf(manager.pcify__BatchSize__c);
batchJob.action = manager.pcify__AuditAction__c;
batchJob.loadQuery();
database.executebatch(batchJob, batchJob.batchSize);
}
}


Test Class
Plaintext                                                        Copy


@isTest
public with sharing class CustomAttachmentTriggerHandlerTEST {

@isTest
static void testCustomAttachmentTrigger() {


Case c = new Case();
c.Origin = 'Email';
c.Description = 'testing';
insert c;


Attachment file = new Attachment();
file.ParentId = c.Id;
file.Name = 'test';
file.ContentType = 'application/msword';
String body = '{\"ParsedResults\":[{\"TextOverlay\":
{\"Lines\":[],\"HasOverlay\":false,\"Message\":\"Text overlay is not
provided as it is not requested\"},'+


'\"TextOrientation\":\"0\",\"FileParseExitCode\":1,\"ParsedText\":\"
Demo Cards 4355230837762992 4355-2308-3776-2992\",'+


'\"ErrorMessage\":\"\",\"ErrorDetails\":\"\"}],\"OCRExitCode\":1,\"I
sErroredOnProcessing\":false,\"ProcessingTimeInMilliseconds\":\"669\
",'+
'\"SearchablePDFURL\":\"Searchable PDF not generated as it
was not requested.\"}';
Blob mockbody = Blob.valueof(body);
file.Body = mockbody;


Test.startTest();
insert file;
Test.stopTest();

List<Attachment> attachments = [SELECT Id FROM Attachment];
System.assertEquals(attachments.size(), 1);
List<pcify__Log__c> logs = [SELECT Id, pcify__Object__c,
pcify__Category__c, pcify__RecordId__c FROM pcify__Log__c];
System.assertEquals(2, logs.size());
System.assertEquals(logs[0].pcify__Category__c, 'Record
Reported');
System.assertEquals(logs[0].pcify__Object__c, 'Attachment');
System.assertEquals(logs[0].pcify__RecordId__c,
attachments[0].Id);
}
}


Change AppExchange Payment Method
1. Go to the Salesforce AppExchange.
2. Login with your production Salesforce credentials.
3. Click on your pro le picture and select "My Installs & Subscriptions".
4. Click Manage Subscription for Blackthorn Compliance.
5. Click Edit on the bottom right of your screen.
6. Click Edit Payment, and enter the new credit card
7. Click Review Changes.
8. Click Save.


Extension Packages
The following extension packages are paid add-ons for Blackthorn Compliance. Please contact your
Account Manager to learn more about purchasing them.


Con gure Blackthorn Compliance For Email-to-Case
Con gure Blackthorn Compliance for Chatter
Con gure Blackthorn Compliance for Salesforce Chat (Live Agent)
Con gure Blackthorn Compliance for Attachments and Files


Con gure for Email-to-Case

Are you interested in this extension package?

The Con gure for Email-to Case extension package is a paid add-on for Blackthorn Compliance.
Please contact your Account Manager to learn more about purchasing it.


1. Install the Email-to-Case Extension Package:
production
sandbox
2. Once installation is complete, Turn on Detection for EmailMessage.
3. You should receive the following noti cation:


4. Congratulations! You have successfully con gured Email Messages for Blackthorn
Compliance.


You still need to install Compliance from the Blackthorn Candy Shop, but we will upgrade your
existing package to include Email-to-Case support.


Con gure for Chatter

Are you interested in the Blackthorn Compliance-Chatter extension package?

The Chatter extension package is a paid add-on for Blackthorn Compliance. Please contact your
Account Manager to learn more about purchasing it.


IMPORTANT UPDATE

For Compliance - Version 3.87 to work correctly, Chatter - Version 3.73 must be installed. Click
here to access the Chatter Version 3.73 production link.

Note: Compliance will continue to work without the additional le; however, the most recent
update won’t work.


1. Install the Chatter extension package:
production
sandbox
2. Turn on Detection for FeedItem.
3. You should see the following alert noti cation:


4. Turn on Detection for FeedComment.
5. You should see the following alert noti cation:


6. Congratulations! You have successfully con gured Chatter for Blackthorn Compliance.
7. Use the steps below to ensure the A llo w users to edit po sts and c o mments Chatter
setting is enabled. (This setting is enabled by default.)
a. Click the Gear icon in the upper right-hand corner.
b. Click Setup.
c. In the Quick Find box, search for and click "Chatter Settings".
d. Click the Edit button at the bottom of the page.


e. In the Posts and Comment Modi cation section, check the A llo w users to edit
po sts and c o mments setting.
f. Click Save.


Installing Compliance

You still need to install Compliance from the Blackthorn Candy Shop, but we will upgrade your
existing package to include Chatter support.


Con gure for Salesforce Chat (Live Agent)

Are you interested in this extension package?

The Con gure for Salesforce Chat (Live Agent) extension package is a paid add-on for
Blackthorn Compliance. Please contact your Account Manager to learn more about purchasing it.


1. Install the Salesforce Chat Extension Package:
production
sandbox
2. Install our package in a sandbox or testing environment.
3. Once installation is complete, Turn on Detection for Live Chat in custom metadata settings.
4. You should see the following alert noti cation:


5. Leverage Salesforce Sensitive Data Rules & Disable Agent Sneak Peak URL.
6. Congratulations! You have successfully con gured Salesforce Chat for Blackthorn
Compliance.

If you are using Salesforce standard feature Sensitive Data Rules, you can use them in tandem with
Compliance. Sensitive Data Rules mask known patterns during Live Chats, in browser. Compliance will
mask known patterns after the chat has ended, in the Live Chat Transcript object. To read more about
Sensitive Data Rules, click here.


You still need to install Compliance from the Blackthorn Candy Shop, but we will upgrade your
existing package to include Live Agent support.


Con gure for Attachments and Files

Are you interested in this extension package?

The Con gure for Attachments and Files extension package is a paid add-on for Blackthorn
Compliance. Please contact your Account Manager to learn more about purchasing it.


Follow the steps below to install the SecureAttachment package:


1. Navigate to the AppExchange from your Salesforce org or go directly to Blackthorn's Candy
Shop listing for Compliance.
2. Click Get It Now on the AppExchange listing.
3. Log into the AppExchange with your Production Salesforce credentials.
4. Select the environment where you’d like to install SecureAttachment.


If you are already logged into the Salesforce instance where you will be installing, you’ll be redirected
to a con rmation page for the installation. Otherwise, if you are installing to a different instance of
Salesforce, you will be brought to a login screen where you can enter the credentials for that
environment.


5. Leave the default pro le "Install for Admins Only" selected, and click Install.


6. You’ll be prompted to Approve Third-Party Access for 2 URLs. These URLs are the endpoints
in order for the OCR API to work. Make sure “Yes, grant access to these third-party web
sites” is selected, and press Continue.

SecureAttachment will now be installed in your Salesforce org.

In most cases, this page will automatically refresh noting that the package was either
successfully installed or it failed installation.
For orgs that have complex logic/code already applied, it may take longer for the installation
process. In this case, an email will be sent to the email address associated to the user who
performed the installation either con rming success or failure of the installation.
Check out “Installation Troubleshooting” for common installation issues.

Once installation is complete, you will see the the SecureAttachment package on the list of Salesforce
Installed Packages in the Setup.


After installation for Blackthorn Compliance is completed, you are ready to Con gure
SecureAttachment.


Install / Setup SecureAttachment
Install SecureAttachment
Setup SecureAttachment (after installation)
Upgrade SecureAttachment
What is the difference between Attachment and ContentVersion (Salesforce Files)?


Install SecureAttachment

Prerequisite
SecureAttachment is a paid add-on. If you are interested in using it, please contact Blackthorn Support.


Installation Steps
Follow the steps below to install the SecureAttachment package:


1. Contact Blackthorn Support to request API credentials.
2. Our support team will initiate an internal case with our engineering team to generate your
API credentials. Once this process is complete, you will receive your installation links and API
credentials.
3. Using the links provided, log in with your Production Salesforce credentials.
4. Select the environment where you’d like to install SecureAttachment.


5. If you are already logged into the Salesforce instance where you will be installing, you’ll be
redirected to a con rmation page for the installation. Otherwise, if you are installing to a
different instance of Salesforce, you will be brought to a login screen where you can enter
the credentials for that environment.
6. Select the default pro le, "Install for Admins Only" and click Install.


7. You will be prompted to Approve Third-Party Access for two URLs. These URLs are the
endpoints needed for the OCR API to work. Select “Yes, grant access to these third-party
web sites” and press Continue.

SecureAttachment will now be installed in your Salesforce org.

In most cases, this page will automatically refresh, noting that the package was either
successfully installed or it failed installation.
For orgs that have complex logic/code already applied, it may take longer to complete the
installation process. In this case, an email will be sent to con rm the success or failure of the
installation to the email address associated with the user who performed the installation.

After installation, you can see the SecureAttachment package on the list of Salesforce Installed
Packages in the Setup.


When Blackthorn Compliance installation is complete, you are ready to con gure SecureAttachment.


Setup SecureAttachment (after
installation)
There are a few more steps to completely nish setting up SecureAttachment.


STEP ONE: Add SecureAttachment Tabs to
Blackthorn Compliance
Once you have installed the SecureAttachment package, you will need to add Custom Tabs to
Compliance.

1. Edit the Compliance Lightning App. Go to Setup > Apps > App Manager > Compliance > Edit.


2. Click on Navigation Items in the App Settings.
3. Add the "Audit" tab to the Selected Items.


4. Add the "API Credentials" tab to the Selected Items.


5. Press Save.
6. At this point, you may see two Audit tabs in Compliance. SecureAttachment comes with it's
own Audit tab, and you should start using the new tab highlighted in green.


7. Hide the old tab (highlighted in red) by navigating to: Setup > Users > Pro les.
8. Select your user's Pro le.
9. Click Edit and scroll down to the Custom Tab Settings section.
10. Change the rst Audit tab to "Tab Hidden".


11. Click Save.
12. Navigate back to the Compliance Lightning App.


STEP TWO: Add Images API Credentials
SecureAttachment scans your attachments via OCR technology. You will need to enter two different
sets of credentials: 1) Images and 2) Files.


1. Click the new API Credentials tab.


2. Select Credential Type = "Images API" from the dropdown.
3. Enter the Images API Key provided by Compliance support in the API Key             eld.
4. Enter the Images API Endpoint provided by Compliance support in the API EndPoint            eld.
5. Click Save. (For security reasons, the credentials will disappear after saving.)

Stay on this page for the next step: Adding API credentials for Files.


STEP THREE: Add Files API Credentials
1. Select Credential Type = "Files API" from the drop-down.

2. Enter the Files API Key provided by Compliance support in the API Key         eld.

3. Enter the Files API Endpoint provided by Compliance support in the API EndPoint           eld.

4. Click Save. (For security reasons, the credentials will disappear after saving.)

Congratulations! You have nished integrating SecureAttachment with the APIs.


STEP FOUR: Turn On APIs in SecureAttachment
The last step is to turn on the APIs so that SecureAttachment knows you’re ready to start calling the
APIs. If you haven’t completed steps 1-3, this step won’t work!


1. Navigate to Setup > Custom Code > Custom Metadata Types > SecureAttachment Settings.


2. Click Manage Records.


3. Click on the Default record.


4. Click Edit.


5. Check Enable Files API .


6. Check Enable Images API .


7. Press Save.


STEP FIVE: Auto-Create Chatter Posts on Parent
Records [OPTIONAL]
This last step is optional. If you want to inform your agents when attachments or les are auto-
deleted or reported by Compliance, you can perform the following steps. A process builder ow will
automatically create Chatter posts on the Chatter Feed of the parent record of the Attachment or
ContentVersion record. Usually this Chatter post will be created on the Case where the Attachment
was uploaded.

1. Navigate to Setup > Process Automation > Process Builder.
2. Expand the process called "PCIFY: Create Chatter Post for Detected PII".


3. Press Activate and con rm the popup.
4. Navigate back to Setup > Custom Code > Custom Metadata Types > SecureAttachment
Settings.


5. Click Manage SecureAttachment Settings.
6. Click Default.


7. Edit and Save the "AutoChatterMessage" to your liking or keep as-is.


You’re all done! You can start using SecureAttachment now.


Upgrade SecureAttachment

BEFORE you upgrade the package
1. Check that the AuditBatchSize for Attachment and ContentVersion is 10.
Navigate to Setup > Custom Code > Custom Metadata Types > Manager.


2. Update your DetectionFields for ContentVersion and Attachment.
Navigate to Setup > Custom Code > Custom Metadata Types > Manager.


ContentVersion: VersionData, FileType, FileExtension, Title, ContentDocumentId
Attachment: Body, ContentType, Name, ParentId


NEXT follow the steps below to upgrade your
SecureAttachment package
1. Navigate to the AppExchange from your Salesforce org, or go directly to Blackthorn's Candy
Shop listing for Compliance.
2. Click Get It Now on the AppExchange listing, and follow the install prompts.
3. Once the upgrade is complete, check the following con gurations.


4. Re-enter API Credentials provided by Blackthorn Compliance Support (contact support if you
need them again).


5. Check that your Remote Site Setting URLs are exactly as follows and active.
Navigate to Setup > Security > Remote Site Settings > FilesAPI > Edit.


6. Check your SecureAttachment Settings:


You should only have APIs enabled for the credentials that you previously entered. If you entered two
API credentials (Images API and Files API) then both APIs should be enabled. If you only entered
credentials for Files API, then uncheck the checkbox for Images API.

Congratulations! You have nished upgrading SecureAttachment.


Difference between Attachment and
ContentVersion (Salesforce Files)

What is the difference between Attachment and
ContentVersion (Salesforce Files)?
There are two different attachment-like objects in Salesforce.


1. Attachment: This is the older object that many newer orgs don't use anymore, but Blackthorn
supports it for customers on older orgs.
2. Files (ContentDocument, ContentVersion): These are the newer objects known collectively as
"Salesforce Files". Depending on how the attachments are uploaded, they could end up being
saved as either object. If we are dealing with Salesforce Files, then when Blackthorn
Compliance detects a credit card number in the ContentVersion record, it will delete both the
parent ContentDocument record and all of the child ContentVersion records.

Compliance supports both types of records, but you will need to determine which object you will use
for your org in order to con gure the SecureAttachment extension package correctly.

Please remember that SecureAttachment does not support masking within Attachment or
ContentVersion records. At this time you can Report or Delete these records automatically if Personally
Identi able Information (PII) is detected.


Logging: The Log Object
Everything that Blackthorn Compliance does is in the Logs tab.


When Compliance masks a credit card, it creates a Log. When Compliance has an error, it creates a Log.
When you press the Delete button on a Log record, it creates another Log that says you just deleted
the related Case (or Email, etc). The source of Compliance analytics & reporting is actually the Log
Object. So when you create or delete the Logs, this affects the Compliance reports and the Analytics
tab dashboard.


The Log object (API Name: pcify__Log__c) is a custom object. It was created for the Compliance
application and is not the same as standard Salesforce logging.


Log Object Reference Fields
Field
API Name                    Data Type           Description        Values
Label
Id of related
RecordId       pcify__RecordId__c              Text(18)
record
Id of parent
record (for
ParentId       pcify__ParentId__c              Text(18)              Attachments and
Content Version
records)
Record                                                               Hyperlink to
pcify__Record__c                Formula (Text)
Link                                                                 related record
Hyperlink to
parent record
Parent
pcify__Parent_Link__c           Formula (text)        (for Attachments
Link
and Content
Version records)
Classi cation of     Record
Category*      pcify__Category__c              Text(255)
Log                  Reported
Record
Deleted
Record
Masked


True if credit card
Credit Card                                                      number is
pcify__CreditCardDetected__c   Formula(Checkbox)
Detected                                                         detected.


True if
Compliance has
Exception     pcify__Exception__c            Checkbox            detected an
internal error -
not detected PII.
Large                                        Long Text Area      Long summary
pcify__Large_Description__c
Description                                  (131072)            of Log event.
Triggering
SObject for Log
event. Use this
Object**      pcify__Object__c               Text(255)
eld to lter
reports by
SObject.
The Salesforce
eld in which
Field         pcify__Field__c                Text(255)           Compliance
discovered
sensitive data.
The Detection
Pattern       pcify__Pattern__c              Text(255)           Pattern matched
in the detection.
Apex origin of
Origin        pcify__Origin__c               Text(255)
Log event
A likely false
positive. This
eld is agged
automatically by
Compliance. You
False                                                            are allowed to
pcify__FalsePositive__c        Checkbox
Positive                                                         manually check
this box if you
nd valid false
positives not
caught by
Compliance.
Our con dence
in the detection
Con dence
pcify__Con denceRating__c      Formula(Text)       event. Values can     High
Rating
be High,
Medium, or Low.
Medium
Low
True if a
Pattern
pcify__PatternMatch__c         Checkbox            detection pattern
Match
was matched.


True if the
number agged
Luhn Valid     pcify__LuhnValid__c             Checkbox
passed the Luhn
Algorithm.
A standard set
of values which
Log Type*      pcify__LogType__c               Formula (Text)        can be used in       Mask
reporting

Report
Delete
Debug

*Use the Object eld to lter reports by SObject e.g. “Case” will only show you Logs where the
triggering records are Cases.

**Use either the Category eld or the Log Type eld to lter reports by action i.e. “Log Type = Report”
to only return logs where there was a report event.


How to Stop False Positives
A false positive error, or a false positive or "false alarm", is a result that indicates a predicted value
exists, when it does not. For example, a DLP solution might ag a credit card number, but if the
number is actually a mobile number, then that is a false positive. At Blackthorn Compliance, we are
conservative in enforcing PCI Compliance rules. But our algorithm also has high precision and recall,
which signi cantly reduces the false positive rate. Unfortunately, there will be instances where, despite
our best predictions, false positives squeak through. The following section explains what you should
do when this happens.


Turn on Luhn Check for all credit card patterns.
Making sure the eld Luhn Check is true for your credit card patterns will ensure that numbers will go
through a second validation; namely verifying that the supposed credit card number passes the Luhn
Algorithm.


Customize detection pattern Regular Expressions
so they are stricter.
You can customize the out-of-the-box RegEx that comes with Compliance. Consider adjusting the
RegEx patterns to be more “strict” or more of an exact match for a speci c pattern type.


Disable Patterns you don’t need.
Don’t do business overseas? Then you don’t need Maestro, JCB, and other international credit cards.
Disable these patterns to signi cantly reduce false positives. Likewise, you don’t need to mask Social
Security Numbers to be PCI compliant (that’s another story altogether).


Create Negative Detection Patterns.
Create patterns for USPS or Fedex tracking numbers, German phone numbers, and more frequent false
positive candidates with negative patterns. These will effectively exclude known patterns from
Compliance masking.


Flag Logs with the False Positive checkbox eld.


Did a false positive come up during production testing? Crowdsource false positive data by manually
agging logs which weren’t actually a credit card. False positives found by matched Negative Patterns
will be agged automatically.


My Credit Card Didn't Get Masked!
You need to make sure that you are testing with a valid credit card number. Try Validate Credit Card
Numbers or something similar.

If any of those checkmarks are red, then you probably are not using a valid credit card number for your
testing. Try using a dummy credit card number generator like: https://saijogeorge.com/dummy-credit-
card-generator/

Blackthorn Compliance checks two things:


1. Does the number match a regular expression in an active Detection Pattern?
2. Does the number pass the Luhn Algorithm?

If either of those are false, then the credit card number will not be masked. The Luhn Algorithm helps
avoid matching international phone numbers, tracking numbers, and other common false positives.

If you don't want to use the Luhn Algorithm (please think twice about this as it signi cantly reduces
your false positive rate), then you need to uncheck the checkbox eld "LuhnCheck" on the speci c
Detection Pattern you are testing:

Setup > Custom Metadata Types > DetectionPattern > Manage DetectionPatterns > Edit the
DetectionPattern you are testing

This eld controls whether or not Compliance validates the credit card number for the particular
Detection Pattern. Try unchecking that eld and re-test with the same credit card number.

If the issue persists, one of the required extension packages is likely missing. For example, if you are
trying to test masking in emails, then you need to install this extension package rst.


Compliance Release Notes

Latest Version
Compliance - February 2025


Older Versions
Compliance - February 2024
Compliance - July 2023
Compliance - April 2023
Compliance - December 2022
Compliance - October 2022
Compliance - July 2022
Compliance - June 2022
Compliance - March 2022
Compliance - February 2022
Compliance - December 2021
Compliance - November 2021
Compliance - Release 3.71
Compliance - Release 3.6
Compliance - Release 3.2
Compliance - Release 3.0


Compliance - November 2025 - Version
3.9.1
Please review the updates below and follow the upgrade instructions to upgrade your Compliance
application.


IMPORTANT UPDATE

For Compliance - Version 3.85 to work correctly, Chatter Package 3.72 must be installed. Click
here to access the Chatter Package 3.72 production link.

Note: Compliance will continue to work without the additional le; however, the most recent
update won’t work.


To avoid reaching Salesforce’s attachment size limit, users should only add les that are less
than 7MB to 8MB. If a le is larger, users must compress it before uploading it to see the
created Logs.


Enhancement
The following work ows were converted to ows so Compliance can continue to support
them after Salesforce deprecates work ows.
Audit Completed
Delete Audit Completed
Post Install Script
Report Audit Completed


Upgrade Instructions
Go to the Blackthorn Candy Shop to upgrade Compliance to the newest version.


Important De nitions

Breaking Change

A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


Compliance - January 2025
Please review the updates below and follow the upgrade instructions to upgrade your Compliance
application.


IMPORTANT UPDATE

For Compliance - Version 3.85 to work correctly, Chatter Package 3.72 must be installed. Click
here to access the Chatter Package 3.72 production link.

Note: Compliance will continue to work without the additional le; however, the most recent
update won’t work.


To avoid reaching Salesforce’s attachment size limit, users should only add les that are less
than 7MB to 8MB. If a le is larger, users must compress it before uploading it to see the
created Logs.


Bug Fix
Compliance now supports con guring Detection Patterns for all Salesforce standard objects
up to and including API version 61.0. The update supports objects used by newer Salesforce
features, such as Messaging and Record Alerts. Previously, Detection Patterns would fail to
detect sensitive data when manually con gured to run on a Salesforce object that was only
available in newer API versions.


Upgrade Instructions
Go to the Blackthorn Candy Shop to upgrade Compliance to the newest version.


Important De nitions

Breaking Change
A breaking change is a signi cant change that requires a package upgrade to see the update.


Off-Cycle or Hot x Release
A hot x is a release that corrects a problem that impacted extensive functionality.

If you have any questions, please don't hesitate to contact Blackthorn Support.


Compliance - February 2024

IMPORTANT UPDATE

For Compliance - Version 3.85 to work correctly, Chatter Package 3.72 must be installed. Click
here to access the Chatter Package 3.72 production link.

Note: Compliance will continue to work without the additional le; however, the most recent
update won’t work.


Enhancement
To ensure Compliance meets Salesforce’s upcoming ICU Local Formats requirements, all
classes in the Compliance repository will reference API version 45.0 or higher.


To avoid reaching Salesforce’s attachment size limit, users should only add les that are less
than 7MB to 8MB. If a le is larger, users must compress it before uploading it to see the
created Logs.


If you have any questions, please don't hesitate to contact Blackthorn Support.


Compliance - July 2023
Version 3.87


IMPORTANT UPDATE

For Compliance - Version 3.87 to work correctly, Chatter Package 3.73 must be installed. Click
here to access the Chatter Package 3.73 production link.

Note: Compliance will continue to work without the additional le; however, the most recent
update won’t work.


Critical Update
The Con gure for Chatter instructions were updated to help users enable the Allow users to edit
posts and comments Chatter setting. (This setting is enabled by default.)


1. Click the Gear icon in the upper right-hand corner.
2. Click Setup.
3. In the Quick Find box, search for and click "Chatter Settings".
4. Click the Edit button at the bottom of the page.
5. In the Posts and Comment Modi cation section, check the Allow users to edit posts and

comments setting.

6. Click Save.


Bug Fix
Fixed an issue related to masking phone numbers that contain parentheses. When there are
closed parentheses in a phone number, the phone number will be masked. (Known Issue:
000002754)


Chatter Extension Package
Data in chatter posts will now be masked even if the user doesn’t have the following
permissions:
Edit My Own Posts
Edit Posts on Records I Own
Can Approve Feed Post and Comment


(Known Issue: 000002766)


Enhancement
The new “Run Case Trigger In System Mode” custom setting was added to BT Compliance
Settings. Previously, if a Case record was customized and a record owner was changed by a
ow, an error would occur because the new user no longer had access to the Case record.
Now if Run In System Mode = “True”, PII data will be masked, the Case creator will be
retained, and the user will have access to the Case record.


To avoid reaching Salesforce’s attachment size limit, users should only add les that are less
than 7MB to 8MB. If a le is larger, users must compress it before uploading it to see the
created Logs.


If you have any questions, please don't hesitate to reach out to Blackthorn Support.


Compliance - April 2023
Version 3.92


IMPORTANT UPDATE

For Compliance Version 3.85 to work correctly, Chatter Version 3.72 must be installed. Click here
to access the Chatter Version 3.72 production link.

Note: Compliance will continue to work without the additional le; however, the most recent
update won’t work.


Critical Update

Critical Update
The Con gure for Chatter instructions were updated to help users enable the Allow users to edit
posts and comments Chatter setting. (This setting is enabled by default.)


1. Click the Gear icon in the upper right-hand corner.
2. Click Setup.
3. In the Quick Find box, search for and click "Chatter Settings".
4. Click the Edit button at the bottom of the page.
5. In the Posts and Comment Modi cation section, check the Allow users to edit posts and

comments setting.

6. Click Save.


Bug Fixes
Compliance users can now perform audits on custom objects.
Users can now audit the les (SecureAttachment) related to custom objects.


To avoid reaching Salesforce’s attachment size limit, users should only add les that are less
than 7MB to 8MB. If a le is larger, users must compress it before uploading it to see the
created Logs.


Compliance - December 2022
Version 3.85


IMPORTANT UPDATE

For Compliance - Version 3.85 to work correctly, Chatter Package 3.72 must be installed. Click
here to access the Chatter Package 3.72 production link.

Note: Compliance will continue to work without the additional le; however, the most recent
update won’t work.


Critical Update
The Con gure for Chatter instructions were updated to help users enable the Allow users to edit
posts and comments Chatter setting. (This setting is enabled by default.)


1. Click the Gear icon in the upper right-hand corner.
2. Click Setup.
3. In the Quick Find box, search for and click "Chatter Settings".
4. Click the Edit button at the bottom of the page.
5. In the Posts and Comment Modi cation section, check the Allow users to edit posts and

comments setting.

6. Click Save.


Bug Fix
When uploading an attachment with PII data and the Detection Action is set to "delete",

the attachment will be deleted and the Credit Cards Detected       eld on the Manager tab

will update accordingly. To con rm this setting is up to date, follow the steps below.
Lightning
Go to Setup → Search for “General Settings” in the search box → General Settings
→ make sure that Files uploaded to the Attachments related list on records are
uploaded as Salesforce Files, not as attachments = “False”.
Classic
Refresh the case details page → click on the button “Attach le” → Go back to
Salesforce lightning and Refresh the Manage App tab → The “Credit Card Detected”


in the Attachment object will be updated and the le will be deleted.


To avoid reaching Salesforce’s attachment size limit, users should only add les that are less
than 7MB to 8MB. If a le is larger, users must compress it before uploading it to see the
created Logs.


Compliance - October 2022
Version 3.85


IMPORTANT UPDATE

For Compliance - Version 3.85 to work correctly, Chatter Package 3.72 must be installed. Click
here to access the Chatter Package 3.72 production link.

Note: Compliance will continue to work without the additional le; however, the most recent
update won’t work.


Critical Update
The Con gure for Chatter instructions were updated to help users enable the Allow users to edit
posts and comments Chatter setting. (This setting is enabled by default.)


1. Click the Gear icon in the upper right-hand corner.
2. Click Setup.
3. In the Quick Find box, search for and click "Chatter Settings".
4. Click the Edit button at the bottom of the page.
5. In the Posts and Comment Modi cation section, check the Allow users to edit posts and

comments setting.

6. Click Save.


Bug Fix
Tags in Chatter posts are now retained after credit card numbers are masked.


To avoid reaching Salesforce’s attachment size limit, users should only add les that are less
than 7MB to 8MB. If a le is larger, users must compress it before uploading it to see the
created Logs.


Compliance - July 2022
Users can now successfully run the Audit job on the Account object when the Name value is
added to the detection pattern in Custom metadata.
Credit card values in a docx le will no longer go undetected when the negative detection
pattern is active. The negative detection pattern will alert the system of PII.


To avoid reaching Salesforce’s attachment size limit, users should only add les that are less
than 7MB to 8MB. If a le is larger, users must compress it before uploading it to see the
created Logs.


Compliance - June 2022
The Apex exception error, “You have uncommitted work pending - JSON string exceeds heap
size limit Refer attached” was resolved.


To avoid reaching Salesforce’s attachment size limit, users should only add les that are less
than 7MB to 8MB. If a le is larger, users must compress it before uploading it to see the
created Logs.


Compliance - March 2022
When using Compliance during a trial period, only three records or les can be agged or
deleted. The fourth record will not be masked, although a Log le with the following
message will be created. “This record was not masked as this org’s license has run out of
masked record allowances. Contact Blackthorn.io for questions.”
When an attachment with credit card information is attached to a Case, a Log record will now
be created regardless of the attachment’s background color.


To avoid reaching Salesforce’s attachment size limit, users should only add les that are less
than 7MB to 8MB. If a le is larger, users must compress it before uploading it to see the
created Logs.


Compliance - February 2022
On the Manage App tab of Blackthorn Compliance, users can click the Enable Daily Audit /
Disable Daily Audit button to schedule the automated daily audit. The automated process
queries all records in your org to check for the con gured regex patterns.
IP Addresses are now supported for out-of-the-box masking on Case records. To enable this,
complete the following steps.
1. Go to Setup.
2. Search for and click “Custom Metadata Types.”
3. Click Manage Records next to “DetectionPattern.”
4. You can now enable IP Addresses for matching and con gure the Case elds you
would like to match on.
The Case lookup eld will be auto-populated in the Log record when the Case record is
submitted with any or all of the following: Subject , Description , and Internal

Comments .

The Negative Detection Pattern will now prevent the masking of postal tracking codes, such
as in the scenario of VISA detection patterns masking postal tracking codes. To ensure this
occurs, the logic was updated to trap negative patterns rst and not run matches with
positive patterns.


Compliance - November 2021
Users will see the following updated names for Blackthorn Compliance.


Blackthorn Compliance (previously PCIFY)
SecureAttachment for Blackthorn Compliance (previously SecureAttachment for PCIFY)
Blackthorn Compliance-Email2Case (previously PCIFY-Email2Case)
Blackthorn Compliance-Chatter (previously PCIFY-Chatter)
Blackthorn Compliance-Chat (previously PCIFY-Chat)


Compliance - December 2021
When using Blackthorn Compliance in trial mode, users can mask a maximum of 10 records.
At the 11th record, a log le that says, "This record was not masked as this org’s license has
run out of masked record allowances. Contact Blackthorn.io for questions." will be created.
The Case    eld in the Log record will now auto-populate when a a eld is masked on a Case
record.


Compliance - Release 3.71

Bug Fix: EmailMessage records over the
Salesforce Character Limit
When very long EmailMessages are inserted into Salesforce, they sometimes go over the standard
character limit for long/rich text elds. Since PCIFY operates Before Insert by default, occasionally the
following error would be generated:


Plaintext                                                                                       Copy

CANNOT_INSERT_UPDATE_ACTIVATE_ENTITY : pcifye2c.EmailMessageTrigger:
data changed by trigger for
field HTML Body: data value too large: (value has been hidden)


While upgrading to the latest version of PCIFY will resolve the issue, we also recommend that you
request Salesforce support to increase the size limit for the EmailMessage TextBody and Case
Description elds


Enhancement: SOQL No Longer Required for
Accessing Custom Metadata
Due to a massive upgrade in Salesforce's Spring 21 Release, the PCIFY app no longer requires any
SOQL in processing records on Insert or Update. The new feature treats Custom Metadata Types the
same as Custom Settings - meaning we can access the records without needed SOQL at all.

The following error will no longer occur during large volume data loads:


Plaintext                                                                                       Copy

System.LimitException: pcify:Too many SOQL queries: 101


Compliance - Release 3.6

NEW Auditing Wizard


We have completely redesigned the Audit process with a brand new Lightning Web Component tab
called “Audit”.

Starting with this release you will no longer be required to swap to the Custom Metadata settings to
con gure the Audit before pressing the Run button. A simple 4 step wizard will guide you through the
Audit process, con gure your Audit, and run it all at the same time.

We’ve heard from many customers that the user experience could be improved for Auditing, so
consider this the rst of many enhancements in that area.


Audit Files And Attachments!
You’ve asked us to scan your existing Files & Attachments for a long time - and we’re thrilled to nally
give our customers what they’ve been asking for.

Via the new Auditing Wizard, you will be able to scan all of your existing PDFs, JPGs, PNGs, Word
documents, CSVs, and more for PII. Simply use the brand new Auditing Wizard the same as any other
Salesforce object.

This new feature does require integration with our OCR API, and the pricing is usage-based.


Support for Physical Credit Card Images


Sometimes your customers will take a picture of their actual credit card, and email this to you!
Previously, PCIFY had trouble picking up these non-machine readable characters since the format
tended to confuse our OCR.


Not a real credit card!

Starting in this release, PCIFY will of cially support detecting credit card numbers (and other PII) in
non-machine readable formats.


Support for CSVs
PCIFY now of cially supports detecting PII in CSV Attachments and Salesforce Files (Content).


Parent Ids for Attachments and ContentVersion
Now PCIFY Logs include the ID of the parent record. When you report Attachments or ContentVersion
records, there are two new log elds:

ParentId
Parent Link

The ParentId eld is the ID of the Case or EmailMessage that is the parent of the related Attachment
or ContentVersion record. The Parent Link eld is a link to the parent record.


Support for Handwriting (Beta)

Along with a major upgrade of our OCR, comes with one of the most exciting features this year.
Starting with this release, PCIFY will detect and remove Attachments and Files with PII written by
hand. Handwriting detection functions much the same as existing PCIFY functionality - your active
Detection Patterns will match handwritten PII data the same as text PII in a Salesforce eld. This
feature is currently in Beta - we welcome your feedback!


Bug Fixes
Delete Button on Logs not working for            Now you can delete PII attachments directly
Attachments and ContentVersion                    from the Logs after manual review.


Compliance - Release 3.2

MaskAnything™


PCIFY has always been the best AppExchange product for nding credit cards. Starting today, you’ll
also be able to nd and redact ANY data in your Salesforce orgs with our new MaskAnything™
feature.

Any string that you can match with a regular expression, you’ll be able to nd with PCIFY:


Bank account numbers
Sensitive medical data
Expiration dates
IP addresses
Email addresses
URLs
Phone numbers
The name “John.”

This data will be detected and permanently removed so your business can spend less time worrying
about compliance liabilities and more time doing what you do best.


Support for Non-Numeric Characters


You’ve asked us for alpha and special character support for a long time, and we’re thrilled to nally
give it to you:


With PCIFY v3.3 you’ll be able to create Detection Patterns for strings containing alpha, numeric, and
special characters. This means that you’ll be able to match strings such as:

Exact Matches: “Account Number: 1234”
Partial Matches: “@yahoo.com”
Mixed Characters: “1Z415364748318”

Try it for tracking numbers, expiration dates, CVVs, email addresses, IP addresses, and more - we think
you’ll like this new feature.


Allowlisting Known False Positives
Sometimes you’ll come across numbers which are known frequent false positive offenders. You don’t
want PCIFY to mask it, but you also don’t want to turn PCIFY off:


Starting in version 3.3, PCIFY will automatically ignore numbers or strings which you designate as
known false positives.


New PCIFY Detection Patterns


We’re including some extra freebies in this release - new Detection Patterns! Not only have we
improved the performance of our existing patterns, but we have given you some optional patterns to
play with:

Pattern                                          Purpose
Combines multiple credit card patterns into a single regular expression for
PerformanceBoost
improved processing times.
UPS                   Anti-pattern for excluding UPS tracking numbers from detection.
USPS                  Anti-pattern for excluding USPS tracking numbers from detection.
Fedex                 Anti-pattern for excluding Fedex tracking numbers from detection.

All of these patterns are turned off by default. We recommend testing the new patterns in your
sandbox environments before turning them on in production.


Schedule PCIFY Audits via Apex
Thanks to the great idea from a favorite customer, a global hospitality and travel platform, we have
opened access to our global classes for scheduling PCIFY Audits. You’ll be able to write your own
Scheduled Apex to set PCIFY Audits to run daily, weekly, monthly for scanning your orgs
automatically. No more pressing “Run Audit” every time!


Processor Improvements (23% faster!)
This is a major architectural improvement that we are excited about - the new version of PCIFY is on
average 23% faster than the previous version. We see huge gains in performance for both Detection
and Auditing. All you have to do to enable these processor improvements is upgrade to PCIFY 3.3.
Enjoy!


Bug Fixes


Bug                                               Impact
Expiration Dates messed up PCIFY detection         411111 11/12 confused PCIFY - not anymore.
411111 411111 confused PCIFY - not
Double credit cards messed up PCIFY detection
anymore.
SecureAttachment fails if API credentials aren’t
Now we fail a little bit more gracefully.
entered
Removed Exception logging for non-supported
It was annoying for customers.
attachment types
Now we simply ignore numbers which match
Removed logging for negative pattern matching
negative patterns.


Compliance - Release 3.0

Negative Detection Patterns


Have you ever experienced a false positive before? Was it a tracking number that resembled a credit
card number? With Negative Detection Patterns, you can effectively exclude these numbers from PCIFY
detection.

We added a new eld to Detection Patterns called Negative Pattern .

Create your own negative patterns for international phone numbers, UPS, USPS, Fedex, and
other common false positives.
Numbers matched with Negative Patterns are not masked.
Logs are generated for a matched Negative Pattern just in case the pattern is too loose (and it
really is a true positive).


False Positive Reporting


We have upgraded the Analytics tab to show false positives, exceptions, and frequent detection
patterns found by PCIFY.


We added 3 new Lightning Dashboard Components to the Analytics tab.
False positives are automatically agged, and included in a report called “False Positives
Today”.
We have improved PCIFY’s detection algorithm to both ignore false positives, and tell you


what we ignored just in case you believe they are actually true positives.
You can also manually add false positives you discover to this report by agging Logs with
the new “False Positive” checkbox eld.
These agged false positive records are excluded from your Credit Card Detection totals in
the Analytics tab.


Mask & Delete Individual Records (with
Lightning)


We have heard from customers that after you run a report audit, it would be nice if you could mask or
delete the related record directly, instead of having to switch the audit action to mask and run the same
audit again.


We have created Lightning Component Buttons so you don’t have run more audits just to
mask a few records
This is especially useful for customers with frequent false positives, who need an easy way
for their compliance teams to manually mask the record after con rming the record does
contain credit card numbers.
These buttons are automatically added to the PCIFY Log page layout, and allow your
compliance team to automatically enforce PCI Compliance on one-off records directly from
the Log without having to switch to the related Case, Email Message, or Attachment.


Enhanced Logging


We have added the following elds to the PCIFY Log object:

Field        Field
Field Description
Name         Type
A likely false positive. This eld is agged automatically by PCIFY. You
False                     are allowed to manually check this box if you nd valid false positives
Checkbox
Positive                  not caught by PCIFY. Checking this box excludes the record from credit
card detection totals.
Con dence                 Our con dence in the detection event. Values can be High, Medium, or
Formula
Level                     Low.
Pattern
Checkbox    True if a detection pattern was matched.
Match
Luhn Valid    Checkbox    True if the number agged passed the Luhn Algorithm.
A standard set of values which can be used in reporting: Mask, Report,
Log Type      Formula
Delete, Debug.
Field         Text        The Salesforce eld in which PCIFY discovered sensitive data.
Pattern       Text        The Detection Pattern matched in the detection.


