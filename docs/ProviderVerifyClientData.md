# ProviderVerifyClientData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**organization_id** | **float** |  | 
**name** | **str** |  | 

## Example

```python
from openapi_client.models.provider_verify_client_data import ProviderVerifyClientData

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderVerifyClientData from a JSON string
provider_verify_client_data_instance = ProviderVerifyClientData.from_json(json)
# print the JSON string representation of the object
print(ProviderVerifyClientData.to_json())

# convert the object into a dict
provider_verify_client_data_dict = provider_verify_client_data_instance.to_dict()
# create an instance of ProviderVerifyClientData from a dict
provider_verify_client_data_from_dict = ProviderVerifyClientData.from_dict(provider_verify_client_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


