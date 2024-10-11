# CreateOAuthClientResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**DataDto**](DataDto.md) |  | 

## Example

```python
from openapi_client.models.create_o_auth_client_response_dto import CreateOAuthClientResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOAuthClientResponseDto from a JSON string
create_o_auth_client_response_dto_instance = CreateOAuthClientResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreateOAuthClientResponseDto.to_json())

# convert the object into a dict
create_o_auth_client_response_dto_dict = create_o_auth_client_response_dto_instance.to_dict()
# create an instance of CreateOAuthClientResponseDto from a dict
create_o_auth_client_response_dto_from_dict = CreateOAuthClientResponseDto.from_dict(create_o_auth_client_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


