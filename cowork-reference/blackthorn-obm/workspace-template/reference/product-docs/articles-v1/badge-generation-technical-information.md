## Metadata_Start 
## code: en
## title: Technical Information 
## slug: badge-generation-technical-information 
## seoTitle: Technical Information 
## description:  
## contentType: Markdown 
## Metadata_End
## New Fields
### Object: Event Settings
If none of the fields on the {{variable.Object_EventSettings}} record have a value, you may receive an error stating that there are no documents to process. That is because we DO NOT have any documents that are *always included*.

* Field Label: {{variable.Field_EVSettings_DocGenPackage}} 
    * API Name: DocGen_Package__c
    * Data Type: Lookup
    * Description: This field references Nintex DocGen’s DocGen object. It’s utilized within the Badge Printing Flow, which is a component of Blackthorn’s Advanced Badge Printing.
    * Help Text: Choose the DocGen package you minted to use to generate your badge.
* Field Label: {{variable.Field_EVSettings_DeliveryOption}}
    * API Name: Delivery_Option__c
    * Data Type: Lookup
    * Description: This field references Nintex DocGen’s Delivery Option object. It’s utilized within the Badge Printing Flow, which is a component of Blackthorn’s Advanced Badge Printing. 
    * Help Text: Choose a delivery option that is included in the same DocGen package you intend to use to generate your badge.
* Field Label: {{variable.Field_EVSettings_BadgeSize}} 
    * API Name: Badge_Size__c
    * Data Type: Picklist
    * Piclist Values: 3x4, 4x3, and 4x6
    * Description: This field controls the size of the badge generated using Blackthorn’s Advanced Badge Printing Feature. For instance, if you want the size of the badge to be 4x6.
    * Help Text: Select the desired size for your badge.
* Field Label: {{variable.Field_EVSettings_BadgeLayout}} 
    * API Name: Badge_Layout__c
    * Data Type: Picklist
    * Picklist Values: Single Sided and Double Sided
    * Description: This field determines the layout of the badge generated using Blackthorn’s Advanced Badge Printing Feature. For instance, it can control whether the badge is single-sided or double-sided. 
    * Help Text: Select the desired layout for your badge’s output.

### Object: Attendee

* Field Label: {{variable.Field_Attendee_EventRole}} 
    * API Name: Event_Role__c
    * Data Type: Picklist
        * Picklist Values: Attendee, Speaker, Sponsor, Staff, VIP, and Volunteer
    * Description: Defines the attendee's role (e.g., speaker or attendee) for badge printing using Blackthorn Badge Generation templates. 
    * Help Text: Select a role to be displayed when generating a badge.

### Object: Event
* Field Label: {{variable.Field_Event_ImageOfVenue}} 
    * API Name: Image_of_Venue__c
    * Data Type: Rich Text Area
    * Description: This field is used to store the badge visual that appears on any double-sided badges generated using Blackthorn’s Advanced Badge Printing feature.
    * Help Text: Insert the desired badge visual. The photo will automatically resize to fit the badge’s dimensions. 
* Field Label: {{variable.Field_Event_BadgeLogo}} 
    * API Name: Badge_Logo__c
    * Data Type: Rich Text Area
    * Description: This field is used to store the logo that appears on any badge that is generated using Blackthorn’s Advanced Badge Printing feature.
    * Help Text: Insert the desired logo to be displayed on the badge. The photo will automatically resize to fit the badge’s dimensions. 

## Permission Sets
### Blackthorn | Badge Generation (User)
* {{variable.Object_EventSettings}}
    * {{variable.Field_EVSettings_DocGenPackage}} - Read/Edit
    * {{variable.Field_EVSettings_DeliveryOption}} - Read/Edit
    * {{variable.Field_EVSettings_BadgeSize}} - Read/Edit
    * {{variable.Field_EVSettings_BadgeLayout}} - Read/Edit
* {{variable.Object_Attendee}}
    * {{variable.Field_Attendee_EventRole}} - Read/Edit
* {{variable.Object_Event}}
    * {{variable.Field_Event_ImageOfVenue}} - Read/Edit
    * {{variable.Field_Event_BadgeLogo}} - Read/Edit

### Blackthorn | Badge Generation (Read Only)
* {{variable.Object_EventSettings}}
    * {{variable.Field_EVSettings_DocGenPackage}} - Read
    * {{variable.Field_EVSettings_DeliveryOption}} - Read
    * {{variable.Field_EVSettings_BadgeSize}} - Read
    * {{variable.Field_EVSettings_BadgeLayout}} - Read
* {{variable.Object_Attendee}}
    * {{variable.Field_Attendee_EventRole}} - Read
* {{variable.Object_Event}}
    * {{variable.Field_Event_ImageOfVenue}} - Read
    * {{variable.Field_Event_BadgeLogo}} - Read

## New Flows
### Blackthorn: Print All Attendee Badges 
#### Description
Generates a badge for all registered {{variable.Object_Attendee}}s; fetches the Nintex document package and delivery id. 

#### Objects Touched in Flow
* (Blackthorn) {{variable.Object_Event}}
* (Blackthorn) {{variable.Object_EventSettings}}
* (Blackthorn) {{variable.Object_Attendee}}
* (DocGen) DocGen
* (DocGen) Delivery Option

#### Add the Flow/Button to the Event Record
1. Open the {{variable.Object_Event}} page layout.
2. Click {{variable.Button_SF_Edit}}.
3. From Mobile & Lightning Actions, drag **Generate Badges** into the Salesforce Mobile and Lightning Experience Actions section.
4. Click {{variable.Button_Save}}.

### Blackthorn: Generate Single Badge
#### Description
Generates a badge for a single {{variable.Object_Attendee}}; fetches the Nintex document package and delivery id.

#### Objects Touched in Flow
* (Blackthorn) {{variable.Object_Event}}
* (Blackthorn) {{variable.Object_EventSettings}}
* (Blackthorn) {{variable.Object_Attendee}}
* (DocGen) DocGen
* (DocGen) Delivery Option

#### Add the Flow/Button to the Attendee Record
1. Open the {{variable.Object_Attendee}} page layout.
2. Click {{variable.Button_SF_Edit}}.
3. From Mobile & Lightning Actions, drag **Generate Badge** into the Salesforce Mobile and Lightning Experience Actions section
4. Click {{variable.Button_Save}}.