# ExchangeAuthorizationCodeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret** | **str** |  | 

## Example

```python
from openapi_client.models.exchange_authorization_code_input import ExchangeAuthorizationCodeInput

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeAuthorizationCodeInput from a JSON string
exchange_authorization_code_input_instance = ExchangeAuthorizationCodeInput.from_json(json)
# print the JSON string representation of the object
print(ExchangeAuthorizationCodeInput.to_json())

# convert the object into a dict
exchange_authorization_code_input_dict = exchange_authorization_code_input_instance.to_dict()
# create an instance of ExchangeAuthorizationCodeInput from a dict
exchange_authorization_code_input_from_dict = ExchangeAuthorizationCodeInput.from_dict(exchange_authorization_code_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


