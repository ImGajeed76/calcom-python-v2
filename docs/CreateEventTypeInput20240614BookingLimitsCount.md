# CreateEventTypeInput20240614BookingLimitsCount

Limit how many times this event can be booked

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **float** | The number of bookings per day | [optional] 
**week** | **float** | The number of bookings per week | [optional] 
**month** | **float** | The number of bookings per month | [optional] 
**year** | **float** | The number of bookings per year | [optional] 
**disabled** | **bool** | Indicates if the option is disabled | [default to False]

## Example

```python
from openapi_client.models.create_event_type_input20240614_booking_limits_count import CreateEventTypeInput20240614BookingLimitsCount

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventTypeInput20240614BookingLimitsCount from a JSON string
create_event_type_input20240614_booking_limits_count_instance = CreateEventTypeInput20240614BookingLimitsCount.from_json(json)
# print the JSON string representation of the object
print(CreateEventTypeInput20240614BookingLimitsCount.to_json())

# convert the object into a dict
create_event_type_input20240614_booking_limits_count_dict = create_event_type_input20240614_booking_limits_count_instance.to_dict()
# create an instance of CreateEventTypeInput20240614BookingLimitsCount from a dict
create_event_type_input20240614_booking_limits_count_from_dict = CreateEventTypeInput20240614BookingLimitsCount.from_dict(create_event_type_input20240614_booking_limits_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


