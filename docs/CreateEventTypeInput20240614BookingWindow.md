# CreateEventTypeInput20240614BookingWindow

Limit how far in the future this event can be booked

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Whether the window should be business days, calendar days or a range of dates | 
**value** | **List[str]** | Date range for when this event can be booked. | 
**rolling** | **bool** | If true, the window will be rolling aka from the moment that someone is trying to book this event. Otherwise it will be specified amount of days from the current date. | [optional] 
**disabled** | **bool** | Indicates if the option is disabled | [default to False]

## Example

```python
from openapi_client.models.create_event_type_input20240614_booking_window import CreateEventTypeInput20240614BookingWindow

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventTypeInput20240614BookingWindow from a JSON string
create_event_type_input20240614_booking_window_instance = CreateEventTypeInput20240614BookingWindow.from_json(json)
# print the JSON string representation of the object
print(CreateEventTypeInput20240614BookingWindow.to_json())

# convert the object into a dict
create_event_type_input20240614_booking_window_dict = create_event_type_input20240614_booking_window_instance.to_dict()
# create an instance of CreateEventTypeInput20240614BookingWindow from a dict
create_event_type_input20240614_booking_window_from_dict = CreateEventTypeInput20240614BookingWindow.from_dict(create_event_type_input20240614_booking_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


