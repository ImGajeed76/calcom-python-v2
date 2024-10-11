# ConferencingAppsOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[ConferencingAppsOutputDto]**](ConferencingAppsOutputDto.md) |  | 

## Example

```python
from openapi_client.models.conferencing_apps_output_response_dto import ConferencingAppsOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConferencingAppsOutputResponseDto from a JSON string
conferencing_apps_output_response_dto_instance = ConferencingAppsOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(ConferencingAppsOutputResponseDto.to_json())

# convert the object into a dict
conferencing_apps_output_response_dto_dict = conferencing_apps_output_response_dto_instance.to_dict()
# create an instance of ConferencingAppsOutputResponseDto from a dict
conferencing_apps_output_response_dto_from_dict = ConferencingAppsOutputResponseDto.from_dict(conferencing_apps_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


