# CreateInstantBookingInput20240813


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | The start time of the booking in ISO 8601 format in UTC timezone. | 
**event_type_id** | **float** | The ID of the event type that is booked. | 
**attendee** | [**Attendee**](Attendee.md) | The attendee&#39;s details. | 
**guests** | **List[str]** | An optional list of guest emails attending the event. | [optional] 
**meeting_url** | **str** | Deprecated - use &#39;location&#39; instead. Meeting URL just for this booking. Displayed in email and calendar event. If not provided then cal video link will be generated. | [optional] 
**location** | **str** | Location for this booking. Displayed in email and calendar event. | [optional] 
**booking_fields_responses** | **object** | Booking field responses consisting of an object with booking field slug as keys and user response as values. | [optional] 
**instant** | **bool** | Flag indicating if the booking is an instant booking. Only available for team events. | 

## Example

```python
from openapi_client.models.create_instant_booking_input20240813 import CreateInstantBookingInput20240813

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInstantBookingInput20240813 from a JSON string
create_instant_booking_input20240813_instance = CreateInstantBookingInput20240813.from_json(json)
# print the JSON string representation of the object
print(CreateInstantBookingInput20240813.to_json())

# convert the object into a dict
create_instant_booking_input20240813_dict = create_instant_booking_input20240813_instance.to_dict()
# create an instance of CreateInstantBookingInput20240813 from a dict
create_instant_booking_input20240813_from_dict = CreateInstantBookingInput20240813.from_dict(create_instant_booking_input20240813_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


