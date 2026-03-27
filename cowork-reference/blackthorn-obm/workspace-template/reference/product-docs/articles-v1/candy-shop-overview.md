## Metadata_Start 
## code: en
## title: Candy Shop Overview 
## slug: candy-shop-overview 
## seoTitle: Candy Shop Overview 
## description:  
## contentType: Markdown 
## Metadata_End
Welcome to the Blackthorn [Candy Shop](https://candyshop.blackthorn.io/products){target="_blank"}! It's Blackthorn’s new web-based, one-stop shop for installations and upgrades of Blackthorn’s Salesforce apps, including Payments, Events, Compliance, and Messaging.

## New Features
The following Candy Shop features change how the apps are installed.

* Apps with dependencies will be installed automatically. For example, if you choose to install Events, Candy Shop will first install and/or upgrade the Base Package and Payments, and lastly install Events.
* Permissions Sets and trial licenses will be assigned to the installing user.
* The Events app will be authorized automatically as the user performs the installation process.
* Clicking the **View the Org** button from the Candy Shop will take you to your org’s home page once the installation is complete.
* The Blackthorn | Events Registration Processing (*EventRegistrationBatchProcess*) scheduled job will be scheduled by default when the Events app is installed. (This job is a requirement for the capacity management feature.)

## Current Limitations
The Candy Shop is in its first iteration and includes the following limitations.

* Candy Shop does NOT assign permission sets to any user other than the installing user.
* Candy Shop does NOT currently install or authorize PayLink. This step is still the final task in the Payments Setup Wizard.
* Candy Shop does NOT currently authorize DocumentLink.
* Blackthorn Donations is NOT and will not be included as an offering in the Candy Shop.

## About the Base Package
The Base Package is an integral part of the new process. It runs behind the scenes and acts as a container for the components that are shared between Blackthorn’s different apps. The great news is that you don’t need to do anything to get it up and running.

Here are some important things to remember:

* Base Package is a required prerequisite when installing Events 3.56 and above.
* Base Package is not listed separately on the Candy Shop as it “lives” in the background.

### Base Package Permission Sets
The following permissions sets are available for the Base Package.

* **Blackthorn | Base (Admin)**
Gives full permissions to all Base Package objects and functionality
* **Blackthorn | Base (User)**
Gives Create, Read, Edit, and Delete but not Modify All on select Base Package objects and fields.

 
