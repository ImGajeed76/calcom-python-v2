# ConnectedCalendarsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected_calendars** | [**List[ConnectedCalendar]**](ConnectedCalendar.md) |  | 
**destination_calendar** | [**DestinationCalendar**](DestinationCalendar.md) |  | 

## Example

```python
from openapi_client.models.connected_calendars_data import ConnectedCalendarsData

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedCalendarsData from a JSON string
connected_calendars_data_instance = ConnectedCalendarsData.from_json(json)
# print the JSON string representation of the object
print(ConnectedCalendarsData.to_json())

# convert the object into a dict
connected_calendars_data_dict = connected_calendars_data_instance.to_dict()
# create an instance of ConnectedCalendarsData from a dict
connected_calendars_data_from_dict = ConnectedCalendarsData.from_dict(connected_calendars_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


