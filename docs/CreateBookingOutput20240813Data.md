# CreateBookingOutput20240813Data

Booking data, which can be either a BookingOutput object or an array of RecurringBookingOutput objects

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**uid** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**hosts** | [**List[Host]**](Host.md) |  | 
**status** | **str** |  | 
**cancellation_reason** | **str** |  | [optional] 
**rescheduling_reason** | **str** |  | [optional] 
**rescheduled_from_uid** | **str** |  | [optional] 
**start** | **str** |  | 
**end** | **str** |  | 
**duration** | **float** |  | 
**event_type_id** | **float** | Deprecated - rely on &#39;eventType&#39; object containing the id instead. | 
**event_type** | [**EventType**](EventType.md) |  | 
**attendees** | [**List[Attendee]**](Attendee.md) |  | 
**guests** | **List[str]** |  | [optional] 
**meeting_url** | **str** | Deprecated - rely on &#39;location&#39; field instead. | [optional] 
**location** | **str** |  | [optional] 
**absent_host** | **bool** |  | 
**booking_fields_responses** | **object** | Booking field responses consisting of an object with booking field slug as keys and user response as values. | [optional] 

## Example

```python
from openapi_client.models.create_booking_output20240813_data import CreateBookingOutput20240813Data

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBookingOutput20240813Data from a JSON string
create_booking_output20240813_data_instance = CreateBookingOutput20240813Data.from_json(json)
# print the JSON string representation of the object
print(CreateBookingOutput20240813Data.to_json())

# convert the object into a dict
create_booking_output20240813_data_dict = create_booking_output20240813_data_instance.to_dict()
# create an instance of CreateBookingOutput20240813Data from a dict
create_booking_output20240813_data_from_dict = CreateBookingOutput20240813Data.from_dict(create_booking_output20240813_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


