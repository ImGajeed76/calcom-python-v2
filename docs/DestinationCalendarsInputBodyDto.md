# DestinationCalendarsInputBodyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration** | **str** | The calendar service you want to integrate, as returned by the /calendars endpoint | 
**external_id** | **str** | Unique identifier used to represent the specfic calendar, as returned by the /calendars endpoint | 

## Example

```python
from openapi_client.models.destination_calendars_input_body_dto import DestinationCalendarsInputBodyDto

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationCalendarsInputBodyDto from a JSON string
destination_calendars_input_body_dto_instance = DestinationCalendarsInputBodyDto.from_json(json)
# print the JSON string representation of the object
print(DestinationCalendarsInputBodyDto.to_json())

# convert the object into a dict
destination_calendars_input_body_dto_dict = destination_calendars_input_body_dto_instance.to_dict()
# create an instance of DestinationCalendarsInputBodyDto from a dict
destination_calendars_input_body_dto_from_dict = DestinationCalendarsInputBodyDto.from_dict(destination_calendars_input_body_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


