# SelectedCalendarOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**SelectedCalendarOutputDto**](SelectedCalendarOutputDto.md) |  | 

## Example

```python
from openapi_client.models.selected_calendar_output_response_dto import SelectedCalendarOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedCalendarOutputResponseDto from a JSON string
selected_calendar_output_response_dto_instance = SelectedCalendarOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(SelectedCalendarOutputResponseDto.to_json())

# convert the object into a dict
selected_calendar_output_response_dto_dict = selected_calendar_output_response_dto_instance.to_dict()
# create an instance of SelectedCalendarOutputResponseDto from a dict
selected_calendar_output_response_dto_from_dict = SelectedCalendarOutputResponseDto.from_dict(selected_calendar_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


