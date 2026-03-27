## Metadata_Start 
## code: en
## title: Test Your Authorize.net Payment Gateway 
## slug: test-your-authorizenet-payment-gateway 
## seoTitle: Test Your Authorize.net Payment Gateway 
## description:  
## contentType: Markdown 
## Metadata_End
To create test records in {{variable.Product_Salesforce}}, use the provided card and ACH numbers and process the payment in a {{variable.Object_PaymentGateway}} with {{variable.Field_PG_TestMode}} = “TRUE”.

:::(Error) (**Real card and bank account information cannot be used in test mode.**)
:::

## Testing Authorize.net Cards
Use the following test card number, valid expiration date in the future, and any random CVC number to create a successful {{variable.Object_PaymentMethod}} and {{variable.Object_Transaction}}.

* **Card number:** 4111111111111111

*This number will create a successful card {{variable.Object_PaymentMethod}} that can be used to capture, authorize, and refund {{variable.Object_Transaction}}s.*

## Testing Authorize.net ACH Bank Accounts
Use the following test bank account numbers to create an ACH {{variable.Object_PaymentMethod}} and {{variable.Object_Transaction}}. 

* **Bank account number:** 000123456789
* **Routing number:** 122105812
* **Account holder type:** Either option

*This {{variable.Object_PaymentMethod}} is now Valid and can be used to capture and refund {{variable.Object_Transaction}}s.*

For more information about testing Authorize.net Payment Gateways, click [here](https://docs.blackthorn.io/v1/docs/test-authorizenet-payment-gateway){target=`_blank`}.

**NOTE:** Additional [card numbers](https://developer.authorize.net/hello_world/testing_guide.html){target=`_blank`} can be found in Authorize.net's testing documentation.
