## Metadata_Start 
## code: en
## title: Smart Capture FAQs 
## slug: smart-capture-faqs 
## seoTitle: Smart Capture FAQs 
## description:  
## contentType: Markdown 
## Metadata_End
## General Questions
### What is Blackthorn Smart Capture?
Blackthorn Smart Capture is a universal lead scanning mobile app that allows event teams to capture lead information instantly using their phone. The app scans badges or business cards and enriches the data using AI without requiring QR codes.

### Who can use Smart Capture?
Smart Capture is designed for event professionals, marketers, sales representatives, and anyone who needs to capture and manage leads at trade shows, conferences, networking events, and other business gatherings. While it can be used anywhere, it was specifically designed for use at events.

### What problems does Smart Capture solve?
The Smart Capture app helps solve multiple problems, including
* follow-up delays due to waiting on data
* inconsistent data gathered processes across events
* expensive/fragmented solutions
* lack of control and visibility into ROI

### How does Smart Capture integrate with Salesforce?
Smart Capture is designed to work seamlessly with Salesforce, allowing you to:
* Export leads directly to your Salesforce org
* Map custom fields between the app and Salesforce
* Maintain data consistency across platforms
* Leverage existing lead management workflows

### What devices support Smart Capture?
Smart Capture is available as a mobile app that can be downloaded from app stores. You can locate and download the Blackthorn Smart Capture app from the Apple App Store or Google Play Store.

### What information can be captured?
The Smart Capture app can extract various contact details from scanned materials, including:
* Name and title
* Company information
* Email addresses
* Phone numbers
* Custom fields as configured

### How accurate is the data?
The data is 80% - 90% accurate but there is always a margin of error, especially since event attendees don't always have the correct information on their badges. We highly recommend always reviewing captured information before exporting to ensure accuracy.

## Security
### Is my data secure?
Yes, the Smart Capture app maintains enterprise-grade security standards and integrates securely with {{variable.Product_Salesforce}}. All data transmission between the mobile app and your {{variable.Product_Salesforce}} org is encrypted and follows industry best practices for data protection.

## Credits
### Do I need credits to use Smart Capture?
Yes, the Smart Capture app operates on a credit system. You need sufficient credits to enrich and export leads. Any leads captured beyond your credit balance will not be enriched or exported until enough credits have been purchased.

## Salesforce Integration
### What Salesforce authentication is required?
The Smart Capture app requires you to complete an authentication process during setup. This connects the app to your {{variable.Product_Salesforce}} org and ensures secure data transfer between the mobile app and your CRM system.

### How does the Salesforce integration work?
Smart Capture’s {{variable.Product_Salesforce}} integration is a manual batch export, not an auto-sync. After capturing leads at an event, users can export them by selecting Salesforce from the app’s export menu, logging in, and choosing a {{variable.Object_Campaign}}. The leads are then created as {{variable.Product_Salesforce}} {{variable.Object_Lead}}s and linked as {{variable.Object_CampaignMember}}s.

To prevent duplicate records, the logic first looks to see which {{variable.Product_Salesforce}} {{variable.Object_Lead}}s/{{variable.Object_Contact}}s exist and creates {{variable.Object_CampaignMember}}s based on them, then it creates any {{variable.Object_Lead}}s/{{variable.Object_CampaignMember}}s for {{variable.Object_Lead}}s that don't exist.

If duplicates are found, existing leads are attached to the campaign instead of recreated. Note that standard {{variable.Product_Salesforce}} duplication rules may prevent some data (like notes) from transferring.

Additional emails are added to the {{variable.Field_Lead_Description}} field. Currently, there’s no support for record types or custom fields. Events can be exported multiple times to different orgs or {{variable.Object_Campaign}}s, and users are automatically signed out after a period.

## Capture Leads  
### What types of materials can I scan?
Smart Capture can scan:
* Event badges and name tags
* Business cards
* Any printed material with contact information

[Use the steps here](/v1/docs/export-leads){target=`_blank`} to export your new leads.

### Can I collect additional information beyond standard contact details?
Yes, Smart Capture supports custom question fields. If you want to add Custom Question fields to your lead capture process, you can configure these within the app and map them to corresponding fields in your {{variable.Product_Salesforce}} org for seamless data integration.

### Can I add notes to captured leads?
Yes, after scanning a lead, you can review the captured information and add notes before exporting. This allows you to record conversation details, follow-up reminders, or other relevant information while the interaction is still fresh.

### Can I capture Leads offline?
Smart Capture allows you to scan, capture, and manage leads even when offline. The leads will be stored locally on your device and can be exported to {{variable.Product_Salesforce}} once you regain internet connectivity.

## Manage and Export Leads 
### How is information added to the Lead's Description field?
For example, when multiple Custom Question fields write to the {{variable.Field_Lead_Description}} on a {{variable.Object_Lead}} or {{variable.Object_Contact}} record, do they overwrite each other or is each value (answer) added?

All values are placed together in the {{variable.Product_Salesforce}} {{variable.Object_Lead}} record’s {{variable.Field_Lead_Description}} field, nothing is overwritten. This allows an organization to capture all of the data without having to create multiple {{variable.Product_Salesforce}} custom fields in their org to map to. Alternatively, the gathered data can remain in the app by setting the question to "Skip this field" during the export process. 

### What happens to the Description field when multiple exports occur?
If the same lead and same event are exported multiple times, the previous value in the {{variable.Object_Lead}}'s {{variable.Field_Lead_Description}} field will NOT be updated, even if the values in the Custom Question fields are changed.

However, if you capture the same lead in a different event, the {{variable.Object_Lead}}’s {{variable.Field_Lead_Description}} field WILL be updated with the new information upon export.

### Can I manage Leads offline?
Smart Capture allows you to scan, capture, and manage leads even when offline. The leads will be stored locally on your device and can be exported to {{variable.Product_Salesforce}} once you regain internet connectivity.

### What happens if I don't have enough credits?
If you don't have sufficient credits, leads will still be captured but won't be enriched or exported to your CRM until enough credits are purchased. The app will display a notification when you're running low on credits.