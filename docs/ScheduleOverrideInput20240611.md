# ScheduleOverrideInput20240611


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**start_time** | **str** | startTime must be a valid time in format HH:MM e.g. 12:00 | 
**end_time** | **str** | endTime must be a valid time in format HH:MM e.g. 13:00 | 

## Example

```python
from openapi_client.models.schedule_override_input20240611 import ScheduleOverrideInput20240611

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleOverrideInput20240611 from a JSON string
schedule_override_input20240611_instance = ScheduleOverrideInput20240611.from_json(json)
# print the JSON string representation of the object
print(ScheduleOverrideInput20240611.to_json())

# convert the object into a dict
schedule_override_input20240611_dict = schedule_override_input20240611_instance.to_dict()
# create an instance of ScheduleOverrideInput20240611 from a dict
schedule_override_input20240611_from_dict = ScheduleOverrideInput20240611.from_dict(schedule_override_input20240611_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


