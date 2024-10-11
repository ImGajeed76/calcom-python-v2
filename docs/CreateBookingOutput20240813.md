# CreateBookingOutput20240813


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**CreateBookingOutput20240813Data**](CreateBookingOutput20240813Data.md) |  | 

## Example

```python
from openapi_client.models.create_booking_output20240813 import CreateBookingOutput20240813

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBookingOutput20240813 from a JSON string
create_booking_output20240813_instance = CreateBookingOutput20240813.from_json(json)
# print the JSON string representation of the object
print(CreateBookingOutput20240813.to_json())

# convert the object into a dict
create_booking_output20240813_dict = create_booking_output20240813_instance.to_dict()
# create an instance of CreateBookingOutput20240813 from a dict
create_booking_output20240813_from_dict = CreateBookingOutput20240813.from_dict(create_booking_output20240813_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


