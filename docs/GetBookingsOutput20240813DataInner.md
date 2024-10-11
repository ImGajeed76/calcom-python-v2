# GetBookingsOutput20240813DataInner


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
**recurring_booking_uid** | **str** |  | 

## Example

```python
from openapi_client.models.get_bookings_output20240813_data_inner import GetBookingsOutput20240813DataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetBookingsOutput20240813DataInner from a JSON string
get_bookings_output20240813_data_inner_instance = GetBookingsOutput20240813DataInner.from_json(json)
# print the JSON string representation of the object
print(GetBookingsOutput20240813DataInner.to_json())

# convert the object into a dict
get_bookings_output20240813_data_inner_dict = get_bookings_output20240813_data_inner_instance.to_dict()
# create an instance of GetBookingsOutput20240813DataInner from a dict
get_bookings_output20240813_data_inner_from_dict = GetBookingsOutput20240813DataInner.from_dict(get_bookings_output20240813_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


