# CreateRecurringBookingInput20240813


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | The start time of the booking in ISO 8601 format in UTC timezone. | 
**event_type_id** | **float** | The ID of the event type that is booked. | 
**attendee** | [**Attendee**](Attendee.md) | The attendee&#39;s details. | 
**guests** | **List[str]** | An optional list of guest emails attending the event. | [optional] 
**location** | **str** | Location for this booking. Displayed in email and calendar event. | [optional] 
**booking_fields_responses** | **object** | Booking field responses. | [optional] 

## Example

```python
from openapi_client.models.create_recurring_booking_input20240813 import CreateRecurringBookingInput20240813

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRecurringBookingInput20240813 from a JSON string
create_recurring_booking_input20240813_instance = CreateRecurringBookingInput20240813.from_json(json)
# print the JSON string representation of the object
print(CreateRecurringBookingInput20240813.to_json())

# convert the object into a dict
create_recurring_booking_input20240813_dict = create_recurring_booking_input20240813_instance.to_dict()
# create an instance of CreateRecurringBookingInput20240813 from a dict
create_recurring_booking_input20240813_from_dict = CreateRecurringBookingInput20240813.from_dict(create_recurring_booking_input20240813_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


