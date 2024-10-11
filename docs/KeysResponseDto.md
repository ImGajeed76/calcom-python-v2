# KeysResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**KeysDto**](KeysDto.md) |  | 

## Example

```python
from openapi_client.models.keys_response_dto import KeysResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of KeysResponseDto from a JSON string
keys_response_dto_instance = KeysResponseDto.from_json(json)
# print the JSON string representation of the object
print(KeysResponseDto.to_json())

# convert the object into a dict
keys_response_dto_dict = keys_response_dto_instance.to_dict()
# create an instance of KeysResponseDto from a dict
keys_response_dto_from_dict = KeysResponseDto.from_dict(keys_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


