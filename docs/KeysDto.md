# KeysDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**refresh_token** | **str** |  | 
**access_token_expires_at** | **float** |  | 

## Example

```python
from openapi_client.models.keys_dto import KeysDto

# TODO update the JSON string below
json = "{}"
# create an instance of KeysDto from a JSON string
keys_dto_instance = KeysDto.from_json(json)
# print the JSON string representation of the object
print(KeysDto.to_json())

# convert the object into a dict
keys_dto_dict = keys_dto_instance.to_dict()
# create an instance of KeysDto from a dict
keys_dto_from_dict = KeysDto.from_dict(keys_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


