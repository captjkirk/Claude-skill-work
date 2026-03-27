## Metadata_Start 
## code: en
## title: Generate Badges 
## slug: generate-badges 
## seoTitle: Generate Badges 
## description:  
## contentType: Markdown 
## Metadata_End
## Prerequisites
Badges can only be created with the {{variable.Object_Attendee}} record as the source object. Event Organizers must create {{variable.Object_Attendee}} records for {{variable.Object_Speaker}}s and {{variable.Object_Staff}} if they require badges.

Confirm the following fields have values.
* {{variable.Object_EventSettings}} Object
    * {{variable.Field_EVSettings_DocGenPackage}} (required)
    * {{variable.Field_EVSettings_DeliveryOption}} (required)
    * {{variable.Field_EVSettings_BadgeSize}} (required)
    * {{variable.Field_EVSettings_BadgeLayout}} (required)
* {{variable.Object_Attendee}} Object
    * {{variable.Field_Attendee_EventRole}} (required)
* {{variable.Object_Event}} Object
    * {{variable.Field_Event_ImageOfVenue}} 
    * {{variable.Field_Event_BadgeLogo}} 

## DocGen Queue Tab
The DocGen Queue is the starting point for generating badges for all {{variable.Object_Attendee}}s. Once the badges are in the queue, Event Organizers can choose to either download them individually, merge them into a zip file, or merge them into a single PDF.

## Generate a Batch of Badges
Prerequisite: For a badge to be generated for an {{variable.Object_Attendee}}, that person’s {{variable.Object_Attendee}} record must have the {{variable.Field_ETAttendee_RegistrStatus}} set to "Registered."

1. Open an {{variable.Object_Event}} record.
2. Click the **Generate Badges** button. 
3. Select a DocGen Package. Out of the box, you will only see DocGen Packages that originate from the {{variable.Object_Attendee}} object. 
4. Sort the badges by the registration date found in the Document Name or by the Document Request Number to organize the badges. 
5. Check the box next to each badge you want to print, or click **Select All** to select all badges. Note: Using Select All will only select the first 50 records. To select more, you must scroll past the 50th entry.
6. Select Download 1 PDF, Download by Type (PDF, Word, Excel, or PowerPoint), or Download Zip. 
7. Click the file name to download the file 
8. To print the badges, follow your organization's standard printing process.

Recommendation: Clear the DocGen Queue between jobs.

## Generate a Single Badge
Use this delivery option when you need to generate a badge for a specific {{variable.Object_Attendee}}. This option is most often used on the day of the {{variable.Object_Event}}.

1. Open an {{variable.Object_Attendee}} record. 
2. Click the **Generate Badge** button. 
3. Click the name of the file to download it. 
4. Click **Finish**.