# DestinationCalendarsOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**DestinationCalendarsOutputDto**](DestinationCalendarsOutputDto.md) |  | 

## Example

```python
from openapi_client.models.destination_calendars_output_response_dto import DestinationCalendarsOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationCalendarsOutputResponseDto from a JSON string
destination_calendars_output_response_dto_instance = DestinationCalendarsOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(DestinationCalendarsOutputResponseDto.to_json())

# convert the object into a dict
destination_calendars_output_response_dto_dict = destination_calendars_output_response_dto_instance.to_dict()
# create an instance of DestinationCalendarsOutputResponseDto from a dict
destination_calendars_output_response_dto_from_dict = DestinationCalendarsOutputResponseDto.from_dict(destination_calendars_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


