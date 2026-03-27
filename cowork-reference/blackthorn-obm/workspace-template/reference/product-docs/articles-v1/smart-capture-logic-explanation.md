## Metadata_Start 
## code: en
## title: Smart Capture Logic Explanation 
## slug: smart-capture-logic-explanation 
## seoTitle: Smart Capture Logic Explanation 
## description:  
## contentType: Markdown 
## Metadata_End
## Salesforce Export Flow
* Existing-record detection happens up front: populateLookupCache queries both Lead and Contact objects by email (or first+last+company) so every Smart Capture lead knows if Salesforce already has a Lead, a converted Lead, or a Contact counterpart before any inserts run (functions/exportService.js:538-768).
* Each lead is turned into a state with a captured-at marker plus any fields that should live in Description; the matching record metadata (type, Salesforce Id, prior Description) is stored on that state (functions/exportService.js:2075-2119).
* States that have no match are batched through a Bulk API insert job; the CSV rows honor campaign-specific field mappings so standard and custom slots can target any writable Lead field—not just Description (functions/salesforceBulk.js:154-274, functions/exportService.js:2138-2149).
* Records that already exist (either directly from the cache or surfaced as duplicate errors from the insert job) skip field updates entirely; the service only re-attaches them to the chosen campaign and earmarks them for a description append (functions/exportService.js:1474-2249).

## Updates vs. Description Appends
* There is no field-level merge for existing Leads or Contacts; instead appendDescriptionsForExistingRecords merges the Smart Capture block into the existing Description (32 kB cap) and skips if the same lead marker is already present (functions/exportService.js:2401-2360).
* Custom fields only land in Salesforce outside Description when the admin maps custom.* slots to real Lead columns before the export; otherwise they’re stringified and appended (with labels) to the Description so historical data isn’t overwritten (functions/salesforceBulk.js:234-294).
* Because only brand-new records go through Bulk insert, there’s no risk of overwriting Salesforce-owned fields, and there is no “append-only” limitation for those fresh records—they carry every mapped field in the CSV payload (functions/exportService.js:2524-2594).

## Converted Lead Handling
* Salesforce forbids updating a converted Lead record; the export code treats any match with IsConverted or a plain Contact as a Contact from the start, so campaign attachments use ContactId instead of LeadId (functions/exportService.js:1431-2144).
* If the Bulk CampaignMember insert still hits CANNOT_UPDATE_CONVERTED_LEAD, it fetches the related ConvertedContactId and retries the attachment as a Contact before flagging an error (functions/exportService.js:2669-2690).
* Description updates follow the same rule: if a Lead description update fails with CANNOT_UPDATE_CONVERTED_LEAD, the code refetches the converted Contact Id and reruns the update against the Contact object, otherwise it records a failure (functions/exportService.js:2441-2477).