# RescheduleBookingInput20240813


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | Start time in ISO 8601 format for the new booking | 
**rescheduling_reason** | **str** | Reason for rescheduling the booking | [optional] 

## Example

```python
from openapi_client.models.reschedule_booking_input20240813 import RescheduleBookingInput20240813

# TODO update the JSON string below
json = "{}"
# create an instance of RescheduleBookingInput20240813 from a JSON string
reschedule_booking_input20240813_instance = RescheduleBookingInput20240813.from_json(json)
# print the JSON string representation of the object
print(RescheduleBookingInput20240813.to_json())

# convert the object into a dict
reschedule_booking_input20240813_dict = reschedule_booking_input20240813_instance.to_dict()
# create an instance of RescheduleBookingInput20240813 from a dict
reschedule_booking_input20240813_from_dict = RescheduleBookingInput20240813.from_dict(reschedule_booking_input20240813_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


