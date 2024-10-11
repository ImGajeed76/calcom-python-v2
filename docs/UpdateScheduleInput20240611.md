# UpdateScheduleInput20240611


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**availability** | [**List[ScheduleAvailabilityInput20240611]**](ScheduleAvailabilityInput20240611.md) |  | [optional] 
**is_default** | **bool** |  | [optional] 
**overrides** | [**List[ScheduleOverrideInput20240611]**](ScheduleOverrideInput20240611.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_schedule_input20240611 import UpdateScheduleInput20240611

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduleInput20240611 from a JSON string
update_schedule_input20240611_instance = UpdateScheduleInput20240611.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduleInput20240611.to_json())

# convert the object into a dict
update_schedule_input20240611_dict = update_schedule_input20240611_instance.to_dict()
# create an instance of UpdateScheduleInput20240611 from a dict
update_schedule_input20240611_from_dict = UpdateScheduleInput20240611.from_dict(update_schedule_input20240611_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


