# RefreshTokenInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** | Managed user&#39;s refresh token. | 

## Example

```python
from openapi_client.models.refresh_token_input import RefreshTokenInput

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshTokenInput from a JSON string
refresh_token_input_instance = RefreshTokenInput.from_json(json)
# print the JSON string representation of the object
print(RefreshTokenInput.to_json())

# convert the object into a dict
refresh_token_input_dict = refresh_token_input_instance.to_dict()
# create an instance of RefreshTokenInput from a dict
refresh_token_input_from_dict = RefreshTokenInput.from_dict(refresh_token_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


