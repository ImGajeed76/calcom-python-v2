# GetOAuthClientsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[PlatformOAuthClientDto]**](PlatformOAuthClientDto.md) |  | 

## Example

```python
from openapi_client.models.get_o_auth_clients_response_dto import GetOAuthClientsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetOAuthClientsResponseDto from a JSON string
get_o_auth_clients_response_dto_instance = GetOAuthClientsResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetOAuthClientsResponseDto.to_json())

# convert the object into a dict
get_o_auth_clients_response_dto_dict = get_o_auth_clients_response_dto_instance.to_dict()
# create an instance of GetOAuthClientsResponseDto from a dict
get_o_auth_clients_response_dto_from_dict = GetOAuthClientsResponseDto.from_dict(get_o_auth_clients_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


