# BaseBookingLimitsDuration20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **float** | The duration of bookings per day (must be a multiple of 15) | [optional] 
**week** | **float** | The duration of bookings per week (must be a multiple of 15) | [optional] 
**month** | **float** | The duration of bookings per month (must be a multiple of 15) | [optional] 
**year** | **float** | The duration of bookings per year (must be a multiple of 15) | [optional] 

## Example

```python
from openapi_client.models.base_booking_limits_duration20240614 import BaseBookingLimitsDuration20240614

# TODO update the JSON string below
json = "{}"
# create an instance of BaseBookingLimitsDuration20240614 from a JSON string
base_booking_limits_duration20240614_instance = BaseBookingLimitsDuration20240614.from_json(json)
# print the JSON string representation of the object
print(BaseBookingLimitsDuration20240614.to_json())

# convert the object into a dict
base_booking_limits_duration20240614_dict = base_booking_limits_duration20240614_instance.to_dict()
# create an instance of BaseBookingLimitsDuration20240614 from a dict
base_booking_limits_duration20240614_from_dict = BaseBookingLimitsDuration20240614.from_dict(base_booking_limits_duration20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


