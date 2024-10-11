# SelectedCalendarOutputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **float** |  | 
**integration** | **str** |  | 
**external_id** | **str** |  | 
**credential_id** | **float** |  | 

## Example

```python
from openapi_client.models.selected_calendar_output_dto import SelectedCalendarOutputDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedCalendarOutputDto from a JSON string
selected_calendar_output_dto_instance = SelectedCalendarOutputDto.from_json(json)
# print the JSON string representation of the object
print(SelectedCalendarOutputDto.to_json())

# convert the object into a dict
selected_calendar_output_dto_dict = selected_calendar_output_dto_instance.to_dict()
# create an instance of SelectedCalendarOutputDto from a dict
selected_calendar_output_dto_from_dict = SelectedCalendarOutputDto.from_dict(selected_calendar_output_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


