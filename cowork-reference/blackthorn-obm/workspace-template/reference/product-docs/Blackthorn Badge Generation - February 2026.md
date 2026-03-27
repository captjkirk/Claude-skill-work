# Blackthorn Badge Generation - February 2026

Table of contents
Blackthorn Badge Generation

Badge Generation Overview
Installation and Setup
Badge Layouts and Templates
Generate Badges
Technical Information
Badge Generation FAQs


Badge Generation Overview
Blackthorn Badge Generation is a Salesforce-native tool that allows event teams to generate and print
Attendee badges directly from Salesforce. It eliminates manual mail merges and third-party print tools
by combining Salesforce Flows with Nintex DocGen templates.

The simple, point-and-click process uses prebuilt templates and ows. Since the templates are Word-
based, Event Organizers can easily modify them to update branding, Attendee elds, logos, and more.

Users can then generate single badges or badges in bulk as PDF les, using Event and Attendee data
that is already in Salesforce. Once the PDF is created, it’s as simple as opening it and using your
existing printer and print process.


Bene ts
Customize templates: Word-based designs that support conditional logic, logos, headshots,
and color cues.
Pre-event or bulk generation: Create and regenerate badges for individuals or entire
Attendee Lists with one click.
Maintain Branding: Use centralized Event Settings to ensure consistent fonts, logos, and
colors.
Salesforce-native: Generate badges straight from your Event and Attendee records.


Use Cases
Donor and VIP events: Print 600+ badges for galas or university tailgates.
Conference and training management: Generate badges for Speakers, Staff, and Sponsors.
Higher Education admissions events: Customize badges as part of welcome packets for
campus visit days and welcome weekends.
On-site reprints: Instantly regenerate badges for lost or updated Attendees.
Pre-event printing: Batch-generate PDFs for smaller Events or mail-outs.


Installation and Setup

Sign Up for Access
There is an additional charge to use the Badge Generation feature. While it works seamlessly with
Blackthorn Events, it is a separate tool.

If you are an existing Blackthorn customer, please reach out to your Customer Success Manager (CSM)
or contact Blackthorn Support.


Required Permission Sets

Blackthorn Events
The Blackthorn | Events (Lite User) permission set is required to use the Blackthorn Badge Generation
tool.


Blackthorn Badge Generation
Assign your user(s) one of the following permission sets.

Blackthorn | Badge Generation (User)
To edit the Blackthorn elds related to the Blackthorn Badge Generation tool, a user must have the
Blackthorn | Badge Generation (User) permission set.

Blackthorn | Badge Generation (Read Only)
If a user only needs to read the Blackthorn elds related to the Badge Generation tool, they should
have the Blackthorn | Badge Generation (Read Only) permission set.


Nintex Objects - Generate Badges
To generate badges, a user must have a relevant Nintex permission set, which is con gured from
within Nintex. Blackthorn permission sets do not control who can generate badges.


Installation Process

Prerequisite
Before you can use the Badge Generation tool, you must install the following in your org:


Blackthorn Events - Version 5.26 or later
Nintex DocGen - Version 20.10 or later


Install Blackthorn Badge Generation
1. Go to Blackthorn Candy Shop.
2. Locate Nintex DocGen.
3. Complete the installation process as you would for other Blackthorn apps.


Setup

Add New Fields
Before you can use the Blackthorn Badge Generation tool, you must add the following elds to the
Attendee, Event, and Event Settings page layouts. For more information about these new elds, click
here.


Event Object
I mage o f V enue (Image_of_Venue__c)
Badge Lo go (Badge_Logo__c)
Event Settings Object
Do c Gen P ac k age (DocGen_Package__c)
Deliv ery Optio n (Delivery_Option__c)
Badge Size (Badge_Size__c)
Badge Lay o ut (Badge_Layout__c)
Attendee Object
Ev ent Ro le (Event_Role__c)


Add a Field to a Page Layout

1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, enter and click the name of the object.
4. Click the Page Layouts tab.
5. Click the name of the page layout.
6. Locate the eld you want to add to the page layout.
7. Drag and drop the eld onto the page layout.
8. Repeat the previous step for any other elds you need to add to this page layout.
9. Click Save.

If a record for that object is open in another tab, you must refresh the page to view the added elds.


Add New Buttons
To add the buttons on the Event and Attendee records that trigger badge generation, complete the
steps below.


Event Record

1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, enter and click "Event" (conference360__Event__c).
4. Click the Page Layouts tab.
5. Select the Event page layout you want to update.
6. Click Edit.
7. From Mobile & Lightning Actions, drag Generate Badges into the Salesforce Mobile and
Lightning Experience Actions section.
8. Click Save.


Attendee Record

1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, enter and click "Attendee" (conference360__Attendee__c).
4. Click the Page Layouts tab.
5. Select the Attendee page layout you want to update.
6. Click Edit.
7. From Mobile & Lightning Actions, drag Generate Badge into the Salesforce Mobile and
Lightning Experience Actions section.
8. Click Save.


Badge Layouts and Templates

Setup Prerequisite


To use the Blackthorn Badge Generation tool for individuals other than Attendees (ex., Speakers
and Staff), they must also have an Attendee record. Badges can only be created with the
Attendee record as the source object. Event Organizers must manually create Attendee records
for Speakers and Staff if they require a badge.


Users can create badges in various layouts and sizes for six default roles: Attendee, Speaker, Sponsor,
Staff, VIP, and Volunteer. Between the layouts, sizes, and templates, there are 36 different
con gurations.

3” x 4” Single-sided
3” x 4” Double-sided
4” x 3” Single-sided
4” x 3” Double-sided
4” x 6” Single-sided
4” x 6” Double-sided


Templates

Template Legend
The template legend is based off of the 4" x 6" double-sided template. Each of the following templates
includes some or all of the information in the template legend.


Single-Sided Templates
The following single-sided templates are available for use.


3” x 4”

There are six, single-sided, 3” x 4” templates. One for each of the roles: Attendee, Speaker, Sponsor,
Staff, VIP, and Volunteer


4” x 3”
There are six, single-sided, 4” x 3” templates. One for each of the roles: Attendee, Speaker, Sponsor,
Staff, VIP, and Volunteer.


4" x 6"
There are six, single-sided, 4” x 6” templates. One for each of the roles: Attendee, Speaker, Sponsor,
Staff, VIP, and Volunteer


Double-Sided Templates
The following double-sided templates are available for use.


3” x 4”

There are six, double-sided, 3” x 4” templates. One for each of the roles: Attendee, Speaker, Sponsor,
Staff, VIP, and Volunteer.


Front


Back


4” x 3”
There are six, double-sided, 4” x 3” templates. One for each of the roles: Attendee, Speaker, Sponsor,
Staff, VIP, and Volunteer.

Front


Back


4” x 6”
There are six, double-sided, 4” x 6” templates. One for each of the roles: Attendee, Speaker, Sponsor,
Staff, VIP, and Volunteer.

Front


Back


Edit a Template

Important Requirement


Due to the template generation logic, the Attendee record’s Ev ent Ro le eld must remain in the
template.


DocGen Packages Tab
DocGen Packages contain information about the package and one or more templates.


Tab: Data
The Data tab includes information about the DocGen Package, including its name, type, and starting
object.


Tab: Documents

The Documents tab includes the templates that are part of the DocGen Package. A DocGen Package
can include one or more templates.


Tab: Delivery

The Delivery tab includes information about the output document (PDF with generated badges). The
output document can include one or more templates that are either combined or generated separately.

Click here for instructions to rename the output le.


Update a Tag
Tags hold information in a template. For example, "<<Attendee_Event>>" is a tag that pulls the Ev ent
Name from the Event record that is related to the Attendee’s record. The information the tag pulls
then appears on a badge.

Use the following steps to change which tag appears or to change the formatting for the information
in the tag.


1. Open a DocGen Package record that includes the template you want to modify.


2. Open the Word document for that template.
3. Click the Field Tagger button on the DocGen Package record.
4. Select Word/PowerPoint Tags.
5. Select an object from the Relationship section or a section under Generic Data.
6. Select a eld and click the Copy icon. Paste the eld into the Word doc. Some elds offer
different formatting options, such as for an Event’s date formatting. If you change the
formatting for a eld that is already in the Word doc, the tag will update automatically to
re ect the new format.
7. Save the Word document.
8. Upload the saved le to Salesforce to replace the previous version. Any changes made to the
document will impact the badges related to the Word le.


Change Colors and Fonts on a Template
To change the font, font size, or colors included in a template, open the Word le, make the changes as
you would change a traditional Word document, and save the le.


Generate Badges

Prerequisites
Badges can only be created with the Attendee record as the source object. Event Organizers must
create Attendee records for Speakers and Staff if they require badges.

Con rm the following elds have values.

Event Settings Object
Do c Gen P ac k age (required)
Deliv ery Optio n (required)
Badge Size (required)
Badge Lay o ut (required)
Attendee Object
Ev ent Ro le (required)
Event Object
I mage o f V enue
Badge Lo go


DocGen Queue Tab
The DocGen Queue is the starting point for generating badges for all Attendees. Once the badges are
in the queue, Event Organizers can choose to either download them individually, merge them into a zip
le, or merge them into a single PDF.


Generate a Batch of Badges
Prerequisite: For a badge to be generated for an Attendee, that person’s Attendee record must have
the Registratio n Status set to "Registered."


1. Open an Event record.
2. Click the Generate Badges button.
3. Select a DocGen Package. Out of the box, you will only see DocGen Packages that originate
from the Attendee object.
4. Sort the badges by the registration date found in the Document Name or by the Document
Request Number to organize the badges.
5. Check the box next to each badge you want to print, or click Select All to select all badges.


Note: Using Select All will only select the rst 50 records. To select more, you must scroll
past the 50th entry.
6. Select Download 1 PDF, Download by Type (PDF, Word, Excel, or PowerPoint), or Download
Zip.
7. Click the le name to download the le
8. To print the badges, follow your organization's standard printing process.

Recommendation: Clear the DocGen Queue between jobs.


Generate a Single Badge
Use this delivery option when you need to generate a badge for a speci c Attendee. This option is
most often used on the day of the Event.

1. Open an Attendee record.
2. Click the Generate Badge button.
3. Click the name of the le to download it.
4. Click Finish.


Technical Information

New Fields

Object: Event Settings
If none of the elds on the Event Settings record have a value, you may receive an error stating that
there are no documents to process. That is because we DO NOT have any documents that are always
included.

Field Label: Do c Gen P ac k age
API Name: DocGen_Package__c
Data Type: Lookup
Description: This eld references Nintex DocGen’s DocGen object. It’s utilized within
the Badge Printing Flow, which is a component of Blackthorn’s Advanced Badge
Printing.
Help Text: Choose the DocGen package you minted to use to generate your badge.
Field Label: Deliv ery Optio n
API Name: Delivery_Option__c
Data Type: Lookup
Description: This eld references Nintex DocGen’s Delivery Option object. It’s
utilized within the Badge Printing Flow, which is a component of Blackthorn’s
Advanced Badge Printing.
Help Text: Choose a delivery option that is included in the same DocGen package
you intend to use to generate your badge.
Field Label: Badge Size
API Name: Badge_Size__c
Data Type: Picklist
Piclist Values: 3x4, 4x3, and 4x6
Description: This eld controls the size of the badge generated using Blackthorn’s
Advanced Badge Printing Feature. For instance, if you want the size of the badge to
be 4x6.
Help Text: Select the desired size for your badge.
Field Label: Badge Lay o ut
API Name: Badge_Layout__c
Data Type: Picklist
Picklist Values: Single Sided and Double Sided


Description: This eld determines the layout of the badge generated using
Blackthorn’s Advanced Badge Printing Feature. For instance, it can control whether
the badge is single-sided or double-sided.
Help Text: Select the desired layout for your badge’s output.


Object: Attendee
Field Label: Ev ent Ro le
API Name: Event_Role__c
Data Type: Picklist
Picklist Values: Attendee, Speaker, Sponsor, Staff, VIP, and Volunteer
Description: De nes the attendee's role (e.g., speaker or attendee) for badge printing
using Blackthorn Badge Generation templates.
Help Text: Select a role to be displayed when generating a badge.


Object: Event
Field Label: I mage o f V enue
API Name: Image_of_Venue__c
Data Type: Rich Text Area
Description: This eld is used to store the badge visual that appears on any double-
sided badges generated using Blackthorn’s Advanced Badge Printing feature.
Help Text: Insert the desired badge visual. The photo will automatically resize to t
the badge’s dimensions.
Field Label: Badge Lo go
API Name: Badge_Logo__c
Data Type: Rich Text Area
Description: This eld is used to store the logo that appears on any badge that is
generated using Blackthorn’s Advanced Badge Printing feature.
Help Text: Insert the desired logo to be displayed on the badge. The photo will
automatically resize to t the badge’s dimensions.


Permission Sets

Blackthorn | Badge Generation (User)
Event Settings
Do c Gen P ac k age - Read/Edit
Deliv ery Optio n - Read/Edit


Badge Size - Read/Edit
Badge Lay o ut - Read/Edit
Attendee
Ev ent Ro le - Read/Edit
Event
I mage o f V enue - Read/Edit
Badge Lo go - Read/Edit


Blackthorn | Badge Generation (Read Only)
Event Settings
Do c Gen P ac k age - Read
Deliv ery Optio n - Read
Badge Size - Read
Badge Lay o ut - Read
Attendee
Ev ent Ro le - Read
Event
I mage o f V enue - Read
Badge Lo go - Read


New Flows

Blackthorn: Print All Attendee Badges

Description
Generates a badge for all registered Attendees; fetches the Nintex document package and delivery id.


Objects Touched in Flow

(Blackthorn) Event
(Blackthorn) Event Settings
(Blackthorn) Attendee
(DocGen) DocGen
(DocGen) Delivery Option


Add the Flow/Button to the Event Record

1. Open the Event page layout.


2. Click Edit.
3. From Mobile & Lightning Actions, drag Generate Badges into the Salesforce Mobile and
Lightning Experience Actions section.
4. Click Save.


Blackthorn: Generate Single Badge

Description
Generates a badge for a single Attendee; fetches the Nintex document package and delivery id.


Objects Touched in Flow

(Blackthorn) Event
(Blackthorn) Event Settings
(Blackthorn) Attendee
(DocGen) DocGen
(DocGen) Delivery Option


Add the Flow/Button to the Attendee Record

1. Open the Attendee page layout.
2. Click Edit.
3. From Mobile & Lightning Actions, drag Generate Badge into the Salesforce Mobile and
Lightning Experience Actions section
4. Click Save.


Badge Generation FAQs

How do I update the output le name?
1. Log in to your org.
2. Go to the Blackthorn Badge Generation app.
3. Click the DocGen Package tab.
4. Click the name of the DocGen Package record you want to update.
5. Click the Delivery tab.
6. You will see the Output Filename eld under “Output Details.” It includes a combination of
static and dynamic information. The prepopulated value is "
<<Attendee_Registration_DateTime>> registration: Badge for <<Attendee_First_Name2>>
<<Attendee_Last_Name2>>”
7. Click Field Tagger.
8. Under the Relationships heading are the “Attendee,” “Badge_Settings (Event Settings),” and
“Event from Attendee” sections.
9. In this example, we will add a new registration date/time format. Click “Attendee” to locate a
eld on the Attendee object.
10. Scroll down to the Registratio n Date/ T ime eld and select a formatting option.
11. Click the Copy icon to copy the selected format style.
12. Click in the Output Filename eld.
13. Select “<<Attendee_Registration_DateTime>>” and paste the copied value. The new value,
“<<Attendee_Registration_DateTime>> registration: Badge for <<Attendee_First_Name2>>
<<Attendee_Last_Name2>>” now includes the updated date/time format.
14. Click Save.


Who should I contact for help with templates if
the data isn't displaying as expected?
Please contact Nintex as you usually would to request help.


What are some Nintex resources that I might
need?
Image Replacement: https://help.nintex.com/en-
US/docgensf/DocGenPackage/Templates/DynamicImagesInTemplates.htm


Make Changes to a Template:
https://help.nintex.com/en-
US/docgensf/DocGenPackage/Templates/FieldTagger/TagWordDocument.htm


When should I generate individual badges
instead of a single le containing all the badges?
You should generate individual badges if you need to print a badge for a single Attendee or a small
group.


How do I make my own template?
If you need to create a new template, clone an existing template, make changes to the le, and save the
le. Then, follow the steps to generate and print the badges.


How do I edit a template?
Click here for instructions on editing the information in a template.


How do I add a new Event Role?
If your organization uses different roles or speci c language for picklist values, you can add new
picklist values to the Attendee’s Ev ent Ro le eld.


Important Information About Editing an Existing Picklist Value


If you need to update an existing picklist value, you should change both the Label and the API
Name to the same value.

This is because DocGen conditional logic references the API Name, but users select the picklist
Label on the Attendee record, which then selects a template.


Add a New Picklist Value
1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, search for “Attendee.”
4. Click Attendee (conference360__Attendee__c).
5. Click the Fields & Relationships tab.


6. Click the Ev ent Ro le eld (Event_Role__c).
7. In the Values section, click New.
8. Enter a value. The value will populate both the picklist Label and the API Name.
9. Click Save.


Clone and Edit a Template
1. Go to the App Launcher.
2. In the Quick Find box, enter and click “Nintex DocGen.”
3. Click the DocGen Packages tab.
4. Click the record used to generate badges.


5. Click the Documents tab.


6. Locate the template you want to use.
7. Download the template.
8. Use the information here to edit the template.
9. Save the template with a new name.


Upload the New Template
1. Go back to the Documents tab.
2. Scroll to the bottom of the page and click Add Template.
3. Click Upload Files.
4. Select the updated template.
5. Once the le is uploaded, click Done.
6. Select “Salesforce Document.”


7. Select “DocGen Files.”
8. Click Select Template Location.
9. Click Edit on the template you have just uploaded.


10. Set I nc lude T emplate to “Conditionally.”


11. Enter the same settings used for the original template. In this example, the original template
had the following settings.
I nc lude sec tio n if = “<<Attendee_Event_Role>><<Badge_Settings_Badge_Size>>
<<Badge_Settings_Badge_Layout>>”
Equals = “Test4x3Single Sided” [NOTE: replace the original picklist value
(Attendee) with the new one (Test).]
Merge T y pe = “No Merge”
Start P age = “1”
End P age = “100”
12. Click Save.


