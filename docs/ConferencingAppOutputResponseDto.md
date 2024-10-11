# ConferencingAppOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**ConferencingAppsOutputDto**](ConferencingAppsOutputDto.md) |  | 

## Example

```python
from openapi_client.models.conferencing_app_output_response_dto import ConferencingAppOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConferencingAppOutputResponseDto from a JSON string
conferencing_app_output_response_dto_instance = ConferencingAppOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(ConferencingAppOutputResponseDto.to_json())

# convert the object into a dict
conferencing_app_output_response_dto_dict = conferencing_app_output_response_dto_instance.to_dict()
# create an instance of ConferencingAppOutputResponseDto from a dict
conferencing_app_output_response_dto_from_dict = ConferencingAppOutputResponseDto.from_dict(conferencing_app_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


