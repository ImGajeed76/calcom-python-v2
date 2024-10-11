# MarkAbsentBookingInput20240813


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **bool** | Whether the host was absent | [optional] 
**attendees** | **List[str]** | Toggle whether an attendee was absent or not. | 

## Example

```python
from openapi_client.models.mark_absent_booking_input20240813 import MarkAbsentBookingInput20240813

# TODO update the JSON string below
json = "{}"
# create an instance of MarkAbsentBookingInput20240813 from a JSON string
mark_absent_booking_input20240813_instance = MarkAbsentBookingInput20240813.from_json(json)
# print the JSON string representation of the object
print(MarkAbsentBookingInput20240813.to_json())

# convert the object into a dict
mark_absent_booking_input20240813_dict = mark_absent_booking_input20240813_instance.to_dict()
# create an instance of MarkAbsentBookingInput20240813 from a dict
mark_absent_booking_input20240813_from_dict = MarkAbsentBookingInput20240813.from_dict(mark_absent_booking_input20240813_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


