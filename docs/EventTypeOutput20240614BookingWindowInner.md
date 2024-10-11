# EventTypeOutput20240614BookingWindowInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Whether the window should be business days, calendar days or a range of dates | 
**value** | **List[str]** | Date range for when this event can be booked. | 
**rolling** | **bool** | If true, the window will be rolling aka from the moment that someone is trying to book this event. Otherwise it will be specified amount of days from the current date. | [optional] 

## Example

```python
from openapi_client.models.event_type_output20240614_booking_window_inner import EventTypeOutput20240614BookingWindowInner

# TODO update the JSON string below
json = "{}"
# create an instance of EventTypeOutput20240614BookingWindowInner from a JSON string
event_type_output20240614_booking_window_inner_instance = EventTypeOutput20240614BookingWindowInner.from_json(json)
# print the JSON string representation of the object
print(EventTypeOutput20240614BookingWindowInner.to_json())

# convert the object into a dict
event_type_output20240614_booking_window_inner_dict = event_type_output20240614_booking_window_inner_instance.to_dict()
# create an instance of EventTypeOutput20240614BookingWindowInner from a dict
event_type_output20240614_booking_window_inner_from_dict = EventTypeOutput20240614BookingWindowInner.from_dict(event_type_output20240614_booking_window_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


