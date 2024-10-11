# OAuthAuthorizeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uri** | **str** |  | 

## Example

```python
from openapi_client.models.o_auth_authorize_input import OAuthAuthorizeInput

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthAuthorizeInput from a JSON string
o_auth_authorize_input_instance = OAuthAuthorizeInput.from_json(json)
# print the JSON string representation of the object
print(OAuthAuthorizeInput.to_json())

# convert the object into a dict
o_auth_authorize_input_dict = o_auth_authorize_input_instance.to_dict()
# create an instance of OAuthAuthorizeInput from a dict
o_auth_authorize_input_from_dict = OAuthAuthorizeInput.from_dict(o_auth_authorize_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


