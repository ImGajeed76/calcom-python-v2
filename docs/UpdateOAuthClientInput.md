# UpdateOAuthClientInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**redirect_uris** | **List[str]** |  | [optional] [default to []]
**booking_redirect_uri** | **str** |  | [optional] 
**booking_cancel_redirect_uri** | **str** |  | [optional] 
**booking_reschedule_redirect_uri** | **str** |  | [optional] 
**are_emails_enabled** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.update_o_auth_client_input import UpdateOAuthClientInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOAuthClientInput from a JSON string
update_o_auth_client_input_instance = UpdateOAuthClientInput.from_json(json)
# print the JSON string representation of the object
print(UpdateOAuthClientInput.to_json())

# convert the object into a dict
update_o_auth_client_input_dict = update_o_auth_client_input_instance.to_dict()
# create an instance of UpdateOAuthClientInput from a dict
update_o_auth_client_input_from_dict = UpdateOAuthClientInput.from_dict(update_o_auth_client_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


