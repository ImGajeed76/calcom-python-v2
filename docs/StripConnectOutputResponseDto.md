# StripConnectOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**StripConnectOutputDto**](StripConnectOutputDto.md) |  | 

## Example

```python
from openapi_client.models.strip_connect_output_response_dto import StripConnectOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of StripConnectOutputResponseDto from a JSON string
strip_connect_output_response_dto_instance = StripConnectOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(StripConnectOutputResponseDto.to_json())

# convert the object into a dict
strip_connect_output_response_dto_dict = strip_connect_output_response_dto_instance.to_dict()
# create an instance of StripConnectOutputResponseDto from a dict
strip_connect_output_response_dto_from_dict = StripConnectOutputResponseDto.from_dict(strip_connect_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


