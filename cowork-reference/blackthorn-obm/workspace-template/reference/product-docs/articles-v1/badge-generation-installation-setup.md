## Metadata_Start 
## code: en
## title: Installation and Setup 
## slug: badge-generation-installation-setup 
## seoTitle: Installation and Setup 
## description:  
## contentType: Markdown 
## Metadata_End
## Sign Up for Access
There is an additional charge to use the Badge Generation feature. While it works seamlessly with Blackthorn Events, it is a separate tool.

If you are an existing Blackthorn customer, please reach out to your Customer Success Manager (CSM) or contact {{variable.Link_BlackthornSupport}}.

## Required Permission Sets 
### Blackthorn Events 
The {{variable.PS_ET_LiteUser}} permission set is required to use the Blackthorn Badge Generation tool.

### Blackthorn Badge Generation 
Assign your user(s) one of the following permission sets.

**Blackthorn | Badge Generation (User)**
To edit the Blackthorn fields related to the Blackthorn Badge Generation tool, a user must have the [Blackthorn | Badge Generation (User) permission set](https://docs.blackthorn.io/docs/badge-generation-technical-information#blackthorn-badge-generation-user){target=`_blank`}. 

**Blackthorn | Badge Generation (Read Only)**
If a user only needs to read the Blackthorn fields related to the Badge Generation tool, they should have the [Blackthorn | Badge Generation (Read Only) permission set](https://docs.blackthorn.io/docs/badge-generation-technical-information#blackthorn-badge-generation-read-only){target=`_blank`}.

### Nintex Objects - Generate Badges
To generate badges, a user must have a relevant Nintex permission set, which is configured from within Nintex. Blackthorn permission sets do not control who can generate badges.

## Installation Process 
### Prerequisite
Before you can use the Badge Generation tool, you must install the following in your org: 
* Blackthorn Events - Version 5.26 or later 
* Nintex DocGen - Version 20.10 or later 

### Install Blackthorn Badge Generation
1. Go to [Blackthorn Candy Shop](https://candyshop.blackthorn.io/products){target=`_blank`}.
2. Locate Nintex DocGen.
3. Complete the installation process as you would for other Blackthorn apps.

## Setup
### Add New Fields 
Before you can use the Blackthorn Badge Generation tool, you must add the following fields to the {{variable.Object_Attendee}}, {{variable.Object_Event}}, and {{variable.Object_EventSettings}} page layouts. For more information about these new fields, [click here](https://docs.blackthorn.io/docs/badge-generation-technical-information#new-fields){target=`_blank`}.

* {{variable.Object_Event}} Object
    * {{variable.Field_Event_ImageOfVenue}} (Image_of_Venue__c)
    * {{variable.Field_Event_BadgeLogo}} (Badge_Logo__c)
* {{variable.Object_EventSettings}} Object
    * {{variable.Field_EVSettings_DocGenPackage}} (DocGen_Package__c)
    * {{variable.Field_EVSettings_DeliveryOption}} (Delivery_Option__c)
    * {{variable.Field_EVSettings_BadgeSize}} (Badge_Size__c)
    * {{variable.Field_EVSettings_BadgeLayout}} (Badge_Layout__c)
* {{variable.Object_Attendee}} Object
    * {{variable.Field_Attendee_EventRole}} (Event_Role__c)

#### Add a Field to a Page Layout
1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, enter and click the name of the object.
4. Click the Page Layouts tab.
5. Click the name of the page layout.
6. Locate the field you want to add to the page layout.
7. Drag and drop the field onto the page layout.
8. Repeat the previous step for any other fields you need to add to this page layout.
9. Click {{variable.Button_Save}}.

If a record for that object is open in another tab, you must refresh the page to view the added fields.

### Add New Buttons
To add the buttons on the {{variable.Object_Event}} and {{variable.Object_Attendee}} records that trigger badge generation, complete the steps below. 

#### Event Record
1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, enter and click "Event" (conference360__Event__c).
4. Click the Page Layouts tab.
5. Select the {{variable.Object_Event}} page layout you want to update.
6. Click {{variable.Button_SF_Edit}}.
7. From Mobile & Lightning Actions, drag **Generate Badges** into the Salesforce Mobile and Lightning Experience Actions section.
8. Click {{variable.Button_Save}}.

#### Attendee Record
1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, enter and click "Attendee" (conference360__Attendee__c).
4. Click the Page Layouts tab. 
5. Select the {{variable.Object_Attendee}} page layout you want to update.
6. Click {{variable.Button_SF_Edit}}.
7. From Mobile & Lightning Actions, drag **Generate Badge** into the Salesforce Mobile and Lightning Experience Actions section.
8. Click {{variable.Button_Save}}.