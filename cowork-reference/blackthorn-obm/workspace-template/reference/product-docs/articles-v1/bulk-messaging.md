## Metadata_Start 
## code: en
## title: Configure Bulk Messaging 
## slug: bulk-messaging 
## seoTitle:  
## description:  
## contentType: Markdown 
## Metadata_End
:::(Info) (How many messagings can I send at one time?)
Blackthorn Messaging limits bulk messages to 200 at a time.
:::

## Configure Accounts
1. Click the Gear icon in the top right corner.
2. Click **Setup**.
3. Click the Object Manager tab.
4. Search for and click the Account object. 
5. Click the List View Button Layout tab.
6. Click **Edit.**
7. Scroll down to the Custom Buttons section.
8. Add the {{variable.Button_SendBulkSMS}} button to the Selected Buttons column.
9. Click {{variable.Button_Save}}.

## Configure Contacts
1. Click the Gear icon in the top right corner.
2. Click **Setup**.
3. Click the Object Manager tab.
4. Search for and click the Contact object.
5. Click the List View Button Layout tab.
6. Click **Edit.**
7. Scroll down to the Custom Buttons section.
8. Add the {{variable.Button_SendBulkSMS}} button to the Selected Buttons column.
9. Click {{variable.Button_Save}}.

## Configure Leads
1. Click the Gear icon in the top right corner.
2. Click **Setup**.
3. Click the Object Manager tab.
4. Search for and click the Lead object.
5. Click the List View Button Layout tab.
6. Click **Edit.**
7. Scroll down to the Custom Buttons section.
8. Add the {{variable.Button_SendBulkSMS}} button to the Selected Buttons column.
9. Click {{variable.Button_Save}}.

## Configure Custom Objects
In Blackthorn Messaging, you have the option to set up Custom Objects for bulk messaging. Here are the steps to be followed.

### Add a Custom Checkbox or Boolean Field to a Custom Object

1. Navigate to the Setup menu.
2. Find the specific object. 
3. Go to Fields and Relationships. 
4. Click {{variable.button_new}}.
5. Choose {{variable.Field_Messaging_DataType}} = “Checkbox”. 
6. Click {{variable.Button_Next}}.
7. Set {{variable.Field_Messaging_FieldLabel}} = “Do Not SMS”.
8. Enter the API name as {{variable.Field_Messaging_FieldName}} = “Do_Not_SMS__c”. 
9. Click {{variable.Button_Next}}. 
10. Apply the necessary field-level security.
11. Click {{variable.Button_Next}}. 
12. Click {{variable.Button_Save}}.

### Copy the existing Visualforce page markup

1. Go to Setup > Visualforce Pages
2. Click into the page named "SendBulkLead_ltng".
3. Select all of the markup. Copy to the clipboard.

### Create the new Visualforce page

1. Go to Setup.
2. In the Quick Find box, enter and click "Visualforce Pages".
3. Click {{variable.button_new}}.
4. Set the {{variable.Field_SF_Label}} to "SendBulk[CustomObjectName]". For example, if your custom object is named Attendee then {{variable.Field_SF_Label}} = "SendBulkAttendee".
5. Paste the markup that you copied from the previous step into the page.
6. Make the following changes:
    1. On Line 1, change the StandardController to the API Name of your object. This should end with "__c" for custom objects.
    2. On Line 1, change the recordSetVar parameter to the Name of your object. This should be the object label and would typically not end with "__c".
    3. On Line 9, change the "c" in front of SendBulkSMSMessenger to "simplesms".
    4. On Line 9, change the sobjectApiName to the API Name of your object.
7. Click {{variable.Button_Save}}.
8. Update all relevant profiles or permission sets to include access to the new Visualforce page.

### Create the List View Button

1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, search for and click your custom object.
4. Click the Buttons, Links, and Actions tab.
5. Click **New Button or Link**.
6. Set the following:
    * {{variable.Field_SF_NewButton_Label}} = "Send Bulk SMS"
    * The {{variable.Field_SF_NewButton_Name}} field will automatically update to "Send_Bulk_SMS".
    * {variable.Field_SF_NewButton_ListButton}} = "True" (checked)
    * {{variable.Field_SF_NewButton_DisplayChec}} = "True" (checked)
    * {{variable.Field_SF_NewButton_ContentSour}} = "Visualforce Page"
    * {{variable.Field_SF_NewButton_Content}} = Choose the Visualforce page you just created.
7. Click {{variable.Button_Save}}.

### Add the List Button to your Object List Views.

1. Go to Setup.
2. Click the Object Manager tab.
3. In the Quick Find box, search for and click your custom object.
4. Click the Search Layouts tab.  for Salesforce Classic.
5. Click Edit next to Default Layout. 
6. Move the {{variable.Button_SendBulkSMS}} button from the Available Buttons column to the Selected Buttons column.
7. Click {{variable.Button_Save}}.

Great job! Now you should be able to visit any of your list views for this object (except Recently Viewed), and you'll see the {{variable.Button_SendBulkSMS}} button!

