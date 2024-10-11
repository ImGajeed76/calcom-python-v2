# EventTypeOutput20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**length_in_minutes** | **float** |  | 
**title** | **str** |  | 
**slug** | **str** |  | 
**description** | **str** |  | 
**locations** | [**List[CreateEventTypeInput20240614LocationsInner]**](CreateEventTypeInput20240614LocationsInner.md) |  | 
**booking_fields** | [**List[EventTypeOutput20240614BookingFieldsInner]**](EventTypeOutput20240614BookingFieldsInner.md) |  | 
**disable_guests** | **bool** |  | 
**slot_interval** | **float** |  | 
**minimum_booking_notice** | **float** |  | 
**before_event_buffer** | **float** |  | 
**after_event_buffer** | **float** |  | 
**recurrence** | **object** |  | 
**metadata** | **object** |  | 
**price** | **float** |  | 
**currency** | **str** |  | 
**lock_time_zone_toggle_on_booking_page** | **bool** |  | 
**seats_per_time_slot** | **object** |  | 
**forward_params_success_redirect** | **object** |  | 
**success_redirect_url** | **object** |  | 
**is_instant_event** | **bool** |  | 
**seats_show_availability_count** | **object** |  | 
**schedule_id** | **object** |  | 
**booking_limits_count** | **object** |  | 
**only_show_first_available_slot** | **bool** |  | 
**booking_limits_duration** | **object** |  | 
**booking_window** | [**List[EventTypeOutput20240614BookingWindowInner]**](EventTypeOutput20240614BookingWindowInner.md) | Limit how far in the future this event can be booked | 
**booker_layouts** | [**BookerLayouts20240614**](BookerLayouts20240614.md) |  | 
**confirmation_policy** | **object** |  | 
**requires_booker_email_verification** | **bool** |  | 
**hide_calendar_notes** | **bool** |  | 
**color** | [**EventTypeColor20240614**](EventTypeColor20240614.md) |  | 
**seats** | [**Seats20240614**](Seats20240614.md) |  | 
**offset_start** | **float** |  | 
**custom_name** | **str** |  | 
**destination_calendar** | [**DestinationCalendar20240614**](DestinationCalendar20240614.md) |  | 
**use_destination_calendar_email** | **bool** |  | 
**hide_calendar_event_details** | **bool** |  | 
**owner_id** | **float** |  | 
**users** | **List[str]** |  | 

## Example

```python
from openapi_client.models.event_type_output20240614 import EventTypeOutput20240614

# TODO update the JSON string below
json = "{}"
# create an instance of EventTypeOutput20240614 from a JSON string
event_type_output20240614_instance = EventTypeOutput20240614.from_json(json)
# print the JSON string representation of the object
print(EventTypeOutput20240614.to_json())

# convert the object into a dict
event_type_output20240614_dict = event_type_output20240614_instance.to_dict()
# create an instance of EventTypeOutput20240614 from a dict
event_type_output20240614_from_dict = EventTypeOutput20240614.from_dict(event_type_output20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


