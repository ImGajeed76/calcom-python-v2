# ConferencingAppsOutputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Id of the conferencing app credentials | 
**type** | **str** | type of conferencing app | 
**user_id** | **float** | Id of the user associated to the conferencing app | 
**invalid** | **bool** | Whether if the connection is working or not. | [optional] 

## Example

```python
from openapi_client.models.conferencing_apps_output_dto import ConferencingAppsOutputDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConferencingAppsOutputDto from a JSON string
conferencing_apps_output_dto_instance = ConferencingAppsOutputDto.from_json(json)
# print the JSON string representation of the object
print(ConferencingAppsOutputDto.to_json())

# convert the object into a dict
conferencing_apps_output_dto_dict = conferencing_apps_output_dto_instance.to_dict()
# create an instance of ConferencingAppsOutputDto from a dict
conferencing_apps_output_dto_from_dict = ConferencingAppsOutputDto.from_dict(conferencing_apps_output_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


