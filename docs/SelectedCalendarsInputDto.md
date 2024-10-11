# SelectedCalendarsInputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration** | **str** |  | 
**external_id** | **str** |  | 
**credential_id** | **float** |  | 

## Example

```python
from openapi_client.models.selected_calendars_input_dto import SelectedCalendarsInputDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedCalendarsInputDto from a JSON string
selected_calendars_input_dto_instance = SelectedCalendarsInputDto.from_json(json)
# print the JSON string representation of the object
print(SelectedCalendarsInputDto.to_json())

# convert the object into a dict
selected_calendars_input_dto_dict = selected_calendars_input_dto_instance.to_dict()
# create an instance of SelectedCalendarsInputDto from a dict
selected_calendars_input_dto_from_dict = SelectedCalendarsInputDto.from_dict(selected_calendars_input_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


