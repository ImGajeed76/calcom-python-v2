# CreateEventTypeInput20240614BookingLimitsDuration

Limit total amount of time that this event can be booked

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **float** | The duration of bookings per day (must be a multiple of 15) | [optional] 
**week** | **float** | The duration of bookings per week (must be a multiple of 15) | [optional] 
**month** | **float** | The duration of bookings per month (must be a multiple of 15) | [optional] 
**year** | **float** | The duration of bookings per year (must be a multiple of 15) | [optional] 
**disabled** | **bool** | Indicates if the option is disabled | [default to False]

## Example

```python
from openapi_client.models.create_event_type_input20240614_booking_limits_duration import CreateEventTypeInput20240614BookingLimitsDuration

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventTypeInput20240614BookingLimitsDuration from a JSON string
create_event_type_input20240614_booking_limits_duration_instance = CreateEventTypeInput20240614BookingLimitsDuration.from_json(json)
# print the JSON string representation of the object
print(CreateEventTypeInput20240614BookingLimitsDuration.to_json())

# convert the object into a dict
create_event_type_input20240614_booking_limits_duration_dict = create_event_type_input20240614_booking_limits_duration_instance.to_dict()
# create an instance of CreateEventTypeInput20240614BookingLimitsDuration from a dict
create_event_type_input20240614_booking_limits_duration_from_dict = CreateEventTypeInput20240614BookingLimitsDuration.from_dict(create_event_type_input20240614_booking_limits_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


