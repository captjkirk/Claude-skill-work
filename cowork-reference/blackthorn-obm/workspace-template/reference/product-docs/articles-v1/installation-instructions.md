## Metadata_Start 
## code: en
## title: Installs and Upgrades 
## slug: installation-instructions 
## seoTitle: Installs and Upgrades 
## description:  
## contentType: Markdown 
## Metadata_End
## Install an App for the First Time
If you are using the {{variable.Product_CandyShop}} for the first time, please review the instructions below. This example follows a user installing   {{variable.Product_Events}}, but the steps are the same for {{variable.Product_Payments}}, {{variable.Product_Compliance}}, and {{variable.Product_TexteyMessaging}}.

:::(Error) (**Are you a Government Cloud user?**)
If you are a Government Cloud user setting up Events or PayLink for the first time or creating a new Sandbox, please contact {{variable.Link_BlackthornSupport}} before starting the process. 
:::

* * *
If you are installing {{variable.Product_Events}} for the first time, the installer will automatically install the {{variable.Product_BasePackage}} first, then {{variable.Product_Payments}}, and lastly {{variable.Product_Events}}. If either {{variable.Product_BasePackage}} or {{variable.Product_Payments}} are already installed, the installer will ensure the correct versions are installed or upgraded before installing {{variable.Product_Events}}.

{{snippet.CandyShopInstall}}

## Upgrade an App

1. Go to the {{variable.Link_CandyShop}}. For the following steps, we will use the Events app, but the steps are the same for the other apps.
3. Click **Blackthorn Events**.
![Events Install new icons](https://cdn.document360.io/f977eec0-500f-40a3-b663-724a51f78075/Images/Documentation/Events%20Install%20new%20icons.png){height="" width=""}
5. Click **Product Upgrade**.
![CandyShop_upgradeapps_clickupgrade](https://cdn.document360.io/f977eec0-500f-40a3-b663-724a51f78075/Images/Documentation/CandyShop_upgradeapps_clickupgrade.png){height="" width=""}
7. Click **Log in to Install**.
![CandyShop_upgrade_clicklogin](https://cdn.document360.io/f977eec0-500f-40a3-b663-724a51f78075/Images/Documentation/CandyShop_upgrade_clicklogin.png){height="" width=""}
9. Select a **Production or Developer Org** or a **Sandbox or Scratch Org**.
![CandyShop_upgrade_selectorg](https://cdn.document360.io/f977eec0-500f-40a3-b663-724a51f78075/Images/Documentation/CandyShop_upgrade_selectorg.png){height="" width=""}
11. Log into your org.
12. Click **Install**. As each step is completed, a green checkmark will appear in the Install column. You’ll also receive an email to confirm the successful installation. 
![CandyShop_upgrade_Install](https://cdn.document360.io/f977eec0-500f-40a3-b663-724a51f78075/Images/Documentation/CandyShop_upgrade_Install.png){height="" width=""}
14. Click **View Org** to go to your Salesforce Org. 

After performing the upgrade, check the [Blackthorn | Events Admin tab’s Upgrade tab](https://docs.blackthorn.io/docs/events-admin-tab-upgrade){target=`_blank`} and [Blackthorn | Payments Admin tab’s Upgrade tab](https://docs.blackthorn.io/docs/blackthorn-payments-admin#upgrade){target=`_blank`} for additional metadata changes.
<br>