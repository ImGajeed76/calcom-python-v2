# CreateTeamEventTypeOutputData


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
**slot_interval** | **float** |  | [optional] 
**minimum_booking_notice** | **float** |  | [optional] 
**before_event_buffer** | **float** |  | [optional] 
**after_event_buffer** | **float** |  | [optional] 
**recurrence** | [**Recurrence20240614**](Recurrence20240614.md) |  | 
**metadata** | **object** |  | 
**price** | **float** |  | 
**currency** | **str** |  | 
**lock_time_zone_toggle_on_booking_page** | **bool** |  | 
**seats_per_time_slot** | **float** |  | [optional] 
**forward_params_success_redirect** | **bool** |  | 
**success_redirect_url** | **str** |  | 
**is_instant_event** | **bool** |  | 
**seats_show_availability_count** | **bool** |  | [optional] 
**schedule_id** | **float** |  | 
**booking_limits_count** | **object** |  | [optional] 
**only_show_first_available_slot** | **bool** |  | [optional] 
**booking_limits_duration** | **object** |  | [optional] 
**booking_window** | [**List[EventTypeOutput20240614BookingWindowInner]**](EventTypeOutput20240614BookingWindowInner.md) | Limit how far in the future this event can be booked | [optional] 
**booker_layouts** | [**BookerLayouts20240614**](BookerLayouts20240614.md) |  | [optional] 
**confirmation_policy** | **object** |  | [optional] 
**requires_booker_email_verification** | **bool** |  | [optional] 
**hide_calendar_notes** | **bool** |  | [optional] 
**color** | [**EventTypeColor20240614**](EventTypeColor20240614.md) |  | [optional] 
**seats** | [**Seats20240614**](Seats20240614.md) |  | [optional] 
**offset_start** | **float** |  | [optional] 
**custom_name** | **str** |  | [optional] 
**destination_calendar** | [**DestinationCalendar20240614**](DestinationCalendar20240614.md) |  | [optional] 
**use_destination_calendar_email** | **bool** |  | [optional] 
**hide_calendar_event_details** | **bool** |  | [optional] 
**team_id** | **float** |  | [optional] 
**owner_id** | **float** |  | [optional] 
**parent_event_type_id** | **float** | For managed event types, parent event type is the event type that this event type is based on | [optional] 
**hosts** | [**List[TeamEventTypeResponseHost]**](TeamEventTypeResponseHost.md) |  | 
**assign_all_team_members** | **bool** |  | [optional] 
**scheduling_type** | **str** |  | 

## Example

```python
from openapi_client.models.create_team_event_type_output_data import CreateTeamEventTypeOutputData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeamEventTypeOutputData from a JSON string
create_team_event_type_output_data_instance = CreateTeamEventTypeOutputData.from_json(json)
# print the JSON string representation of the object
print(CreateTeamEventTypeOutputData.to_json())

# convert the object into a dict
create_team_event_type_output_data_dict = create_team_event_type_output_data_instance.to_dict()
# create an instance of CreateTeamEventTypeOutputData from a dict
create_team_event_type_output_data_from_dict = CreateTeamEventTypeOutputData.from_dict(create_team_event_type_output_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


