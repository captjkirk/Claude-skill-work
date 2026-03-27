## Metadata_Start 
## code: en
## title: Extend Blackthorn Compliance to Other Objects 
## slug: extend-to-other-objects 
## seoTitle:  
## description:  
## contentType: Markdown 
## Metadata_End
Blackthorn Compliance comes preloaded with Detection and Auditing for many standard objects, but what if you want to detect credit cards on custom objects or other standard objects?

## Part One: Create a new Manager Record
1. Create new Compliance Manager Record. Go to Setup > Custom Code > Custom Metadata Types > Manager > Manager Records > New.
![manager\(1\)](https://cdn.document360.io/f977eec0-500f-40a3-b663-724a51f78075/Images/Documentation/manager%281%29.png){height="" width=""}

2. Enter the API Name of the Object in the `Label` field (must be exact API Name).
![API Name](https://cdn.document360.io/f977eec0-500f-40a3-b663-724a51f78075/Images/Documentation/API%20Name.png){height="" width=""}

3. Enter the Name of the Object in the `Manager Name` field (cannot contain consecutive underscores).

4. Enter the comma-delimited API names for Salesforce fields in `Detection Fields` (must be less than 255 characters).
    * ***Do not add*** any trailing commas or spaces.
    * Any fields which are over 255 characters ***will not be included in masking***.
    * If you need more than 255 characters, add your additional fields to `DetectionFieldsPlus`.
![detection field plus](https://cdn.document360.io/f977eec0-500f-40a3-b663-724a51f78075/Images/Documentation/detection%20field%20plus.png){height="" width=""}

5. Select a `Detection Action`.

6. Press {{variable.Button_Save}}.

## Part Two: Extend Compliance with an Apex Trigger
**NOTE:** If you are running Compliance Audits ***only***, then you can skip this step. If you don’t need new records to be processed and are only cleaning up old records, you can skip this step.

Now we’ll need to get a little advanced by writing a super easy Apex Trigger on the Object you are extending Compliance to.

1. Create a new Apex Trigger for the Object:
    * **Classic:** Setup > Create > Objects > Click on the Object name > Triggers > New
    * **Lightning:** Setup > Object Manager > Click on the Object name > Triggers > New

2. Copy & Paste the following lines of code (replacing all ***“NewHouse”*** references with the API name of the Object you wish to extend PCIFY to).

```
trigger NewHouseTrigger on NewHouse (before insert, before update) {    if (pcify.Manager.isOnline('NewHouse')) {         pcify.Processor.maskCreditCards(            Trigger.new,             pcify.Manager.getMaskFields('NewHouse'),            'NewHouse'         );    }}
```

3. Press {{variable.Button_Save}}.
4. Navigate back to the Compliance App.
5. Turn on Detection for the Object.

You should see the following alert notification.
![notification](https://cdn.document360.io/f977eec0-500f-40a3-b663-724a51f78075/Images/Documentation/notification.png){height="" width=""}

Congratulations! You have successfully added a new Object to Compliance.