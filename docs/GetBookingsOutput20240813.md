# GetBookingsOutput20240813


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[GetBookingsOutput20240813DataInner]**](GetBookingsOutput20240813DataInner.md) | Array of booking data, which can contain either BookingOutput objects or RecurringBookingOutput objects | 
**error** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.get_bookings_output20240813 import GetBookingsOutput20240813

# TODO update the JSON string below
json = "{}"
# create an instance of GetBookingsOutput20240813 from a JSON string
get_bookings_output20240813_instance = GetBookingsOutput20240813.from_json(json)
# print the JSON string representation of the object
print(GetBookingsOutput20240813.to_json())

# convert the object into a dict
get_bookings_output20240813_dict = get_bookings_output20240813_instance.to_dict()
# create an instance of GetBookingsOutput20240813 from a dict
get_bookings_output20240813_from_dict = GetBookingsOutput20240813.from_dict(get_bookings_output20240813_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


