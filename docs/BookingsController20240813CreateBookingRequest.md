# BookingsController20240813CreateBookingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | The start time of the booking in ISO 8601 format in UTC timezone. | 
**event_type_id** | **float** | The ID of the event type that is booked. | 
**attendee** | [**Attendee**](Attendee.md) | The attendee&#39;s details. | 
**guests** | **List[str]** | An optional list of guest emails attending the event. | [optional] 
**meeting_url** | **str** | Deprecated - use &#39;location&#39; instead. Meeting URL just for this booking. Displayed in email and calendar event. If not provided then cal video link will be generated. | [optional] 
**location** | **str** | Location for this booking. Displayed in email and calendar event. | [optional] 
**booking_fields_responses** | **object** | Booking field responses. | [optional] 
**instant** | **bool** | Flag indicating if the booking is an instant booking. Only available for team events. | 

## Example

```python
from openapi_client.models.bookings_controller20240813_create_booking_request import BookingsController20240813CreateBookingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BookingsController20240813CreateBookingRequest from a JSON string
bookings_controller20240813_create_booking_request_instance = BookingsController20240813CreateBookingRequest.from_json(json)
# print the JSON string representation of the object
print(BookingsController20240813CreateBookingRequest.to_json())

# convert the object into a dict
bookings_controller20240813_create_booking_request_dict = bookings_controller20240813_create_booking_request_instance.to_dict()
# create an instance of BookingsController20240813CreateBookingRequest from a dict
bookings_controller20240813_create_booking_request_from_dict = BookingsController20240813CreateBookingRequest.from_dict(bookings_controller20240813_create_booking_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


