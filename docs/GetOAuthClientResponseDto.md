# GetOAuthClientResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**PlatformOAuthClientDto**](PlatformOAuthClientDto.md) |  | 

## Example

```python
from openapi_client.models.get_o_auth_client_response_dto import GetOAuthClientResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetOAuthClientResponseDto from a JSON string
get_o_auth_client_response_dto_instance = GetOAuthClientResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetOAuthClientResponseDto.to_json())

# convert the object into a dict
get_o_auth_client_response_dto_dict = get_o_auth_client_response_dto_instance.to_dict()
# create an instance of GetOAuthClientResponseDto from a dict
get_o_auth_client_response_dto_from_dict = GetOAuthClientResponseDto.from_dict(get_o_auth_client_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


