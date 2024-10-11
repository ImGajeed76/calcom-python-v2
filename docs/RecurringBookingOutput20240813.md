# RecurringBookingOutput20240813


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
**recurring_booking_uid** | **str** |  | 
**attendees** | [**List[Attendee]**](Attendee.md) |  | 
**guests** | **List[str]** |  | [optional] 
**meeting_url** | **str** | Deprecated - rely on &#39;location&#39; field instead. | [optional] 
**location** | **str** |  | [optional] 
**absent_host** | **bool** |  | 
**booking_fields_responses** | **object** | Booking field responses consisting of an object with booking field slug as keys and user response as values. | [optional] 

## Example

```python
from openapi_client.models.recurring_booking_output20240813 import RecurringBookingOutput20240813

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringBookingOutput20240813 from a JSON string
recurring_booking_output20240813_instance = RecurringBookingOutput20240813.from_json(json)
# print the JSON string representation of the object
print(RecurringBookingOutput20240813.to_json())

# convert the object into a dict
recurring_booking_output20240813_dict = recurring_booking_output20240813_instance.to_dict()
# create an instance of RecurringBookingOutput20240813 from a dict
recurring_booking_output20240813_from_dict = RecurringBookingOutput20240813.from_dict(recurring_booking_output20240813_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


