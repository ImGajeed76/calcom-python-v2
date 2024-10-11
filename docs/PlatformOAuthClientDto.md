# PlatformOAuthClientDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**secret** | **str** |  | 
**permissions** | **float** |  | 
**logo** | **str** |  | [optional] 
**redirect_uris** | **List[str]** |  | 
**organization_id** | **float** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.platform_o_auth_client_dto import PlatformOAuthClientDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformOAuthClientDto from a JSON string
platform_o_auth_client_dto_instance = PlatformOAuthClientDto.from_json(json)
# print the JSON string representation of the object
print(PlatformOAuthClientDto.to_json())

# convert the object into a dict
platform_o_auth_client_dto_dict = platform_o_auth_client_dto_instance.to_dict()
# create an instance of PlatformOAuthClientDto from a dict
platform_o_auth_client_dto_from_dict = PlatformOAuthClientDto.from_dict(platform_o_auth_client_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


