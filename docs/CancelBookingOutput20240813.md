# CancelBookingOutput20240813


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**GetBookingOutput20240813Data**](GetBookingOutput20240813Data.md) |  | 

## Example

```python
from openapi_client.models.cancel_booking_output20240813 import CancelBookingOutput20240813

# TODO update the JSON string below
json = "{}"
# create an instance of CancelBookingOutput20240813 from a JSON string
cancel_booking_output20240813_instance = CancelBookingOutput20240813.from_json(json)
# print the JSON string representation of the object
print(CancelBookingOutput20240813.to_json())

# convert the object into a dict
cancel_booking_output20240813_dict = cancel_booking_output20240813_instance.to_dict()
# create an instance of CancelBookingOutput20240813 from a dict
cancel_booking_output20240813_from_dict = CancelBookingOutput20240813.from_dict(cancel_booking_output20240813_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


