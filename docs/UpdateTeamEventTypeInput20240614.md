# UpdateTeamEventTypeInput20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length_in_minutes** | **float** |  | [optional] 
**title** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**locations** | [**List[CreateEventTypeInput20240614LocationsInner]**](CreateEventTypeInput20240614LocationsInner.md) | Locations where the event will take place. If not provided, cal video link will be used as the location. | [optional] 
**booking_fields** | [**List[CreateEventTypeInput20240614BookingFieldsInner]**](CreateEventTypeInput20240614BookingFieldsInner.md) | Custom fields that can be added to the booking form when the event is booked by someone. By default booking form has name and email field. | [optional] 
**disable_guests** | **bool** | If true, person booking this event&#39;t cant add guests via their emails. | [optional] 
**slot_interval** | **float** | Number representing length of each slot when event is booked. By default it equal length of the event type.       If event length is 60 minutes then we would have slots 9AM, 10AM, 11AM etc. but if it was changed to 30 minutes then       we would have slots 9AM, 9:30AM, 10AM, 10:30AM etc. as the available times to book the 60 minute event. | [optional] 
**minimum_booking_notice** | **float** | Minimum number of minutes before the event that a booking can be made. | [optional] 
**before_event_buffer** | **float** | Time spaces that can be pre-pended before an event to give more time before it. | [optional] 
**after_event_buffer** | **float** | Time spaces that can be appended after an event to give more time after it. | [optional] 
**schedule_id** | **float** | If you want that this event has different schedule than user&#39;s default one you can specify it here. | [optional] 
**booking_limits_count** | [**CreateEventTypeInput20240614BookingLimitsCount**](CreateEventTypeInput20240614BookingLimitsCount.md) |  | [optional] 
**only_show_first_available_slot** | **bool** | This will limit your availability for this event type to one slot per day, scheduled at the earliest available time. | [optional] 
**booking_limits_duration** | [**CreateEventTypeInput20240614BookingLimitsDuration**](CreateEventTypeInput20240614BookingLimitsDuration.md) |  | [optional] 
**booking_window** | [**CreateEventTypeInput20240614BookingWindow**](CreateEventTypeInput20240614BookingWindow.md) |  | [optional] 
**offset_start** | **float** | Offset timeslots shown to bookers by a specified number of minutes | [optional] 
**booker_layouts** | [**BookerLayouts20240614**](BookerLayouts20240614.md) | Should booker have week, month or column view. Specify default layout and enabled layouts user can pick. | [optional] 
**confirmation_policy** | [**CreateEventTypeInput20240614ConfirmationPolicy**](CreateEventTypeInput20240614ConfirmationPolicy.md) |  | [optional] 
**recurrence** | [**CreateEventTypeInput20240614Recurrence**](CreateEventTypeInput20240614Recurrence.md) |  | [optional] 
**requires_booker_email_verification** | **bool** |  | [optional] 
**hide_calendar_notes** | **bool** |  | [optional] 
**lock_time_zone_toggle_on_booking_page** | **bool** |  | [optional] 
**color** | [**EventTypeColor20240614**](EventTypeColor20240614.md) |  | [optional] 
**seats** | [**CreateEventTypeInput20240614Seats**](CreateEventTypeInput20240614Seats.md) |  | [optional] 
**custom_name** | **str** | Customizable event name with valid variables:        {Event type title}, {Organiser}, {Scheduler}, {Location}, {Organiser first name},        {Scheduler first name}, {Scheduler last name}, {Event duration}, {LOCATION},        {HOST/ATTENDEE}, {HOST}, {ATTENDEE}, {USER} | [optional] 
**destination_calendar** | [**DestinationCalendar20240614**](DestinationCalendar20240614.md) |  | [optional] 
**use_destination_calendar_email** | **bool** |  | [optional] 
**hide_calendar_event_details** | **bool** |  | [optional] 
**hosts** | [**List[Host]**](Host.md) |  | [optional] 
**assign_all_team_members** | **bool** | If true, all current and future team members will be assigned to this event type | [optional] 

## Example

```python
from openapi_client.models.update_team_event_type_input20240614 import UpdateTeamEventTypeInput20240614

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTeamEventTypeInput20240614 from a JSON string
update_team_event_type_input20240614_instance = UpdateTeamEventTypeInput20240614.from_json(json)
# print the JSON string representation of the object
print(UpdateTeamEventTypeInput20240614.to_json())

# convert the object into a dict
update_team_event_type_input20240614_dict = update_team_event_type_input20240614_instance.to_dict()
# create an instance of UpdateTeamEventTypeInput20240614 from a dict
update_team_event_type_input20240614_from_dict = UpdateTeamEventTypeInput20240614.from_dict(update_team_event_type_input20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


