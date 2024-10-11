# ProviderVerifyClientOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**ProviderVerifyClientData**](ProviderVerifyClientData.md) |  | 

## Example

```python
from openapi_client.models.provider_verify_client_output import ProviderVerifyClientOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderVerifyClientOutput from a JSON string
provider_verify_client_output_instance = ProviderVerifyClientOutput.from_json(json)
# print the JSON string representation of the object
print(ProviderVerifyClientOutput.to_json())

# convert the object into a dict
provider_verify_client_output_dict = provider_verify_client_output_instance.to_dict()
# create an instance of ProviderVerifyClientOutput from a dict
provider_verify_client_output_from_dict = ProviderVerifyClientOutput.from_dict(provider_verify_client_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


