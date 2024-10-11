# ScheduleOutput20240611


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**owner_id** | **float** |  | 
**name** | **str** |  | 
**time_zone** | **str** |  | 
**availability** | [**List[ScheduleAvailabilityInput20240611]**](ScheduleAvailabilityInput20240611.md) |  | 
**is_default** | **bool** |  | 
**overrides** | [**List[ScheduleOverrideInput20240611]**](ScheduleOverrideInput20240611.md) |  | 

## Example

```python
from openapi_client.models.schedule_output20240611 import ScheduleOutput20240611

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleOutput20240611 from a JSON string
schedule_output20240611_instance = ScheduleOutput20240611.from_json(json)
# print the JSON string representation of the object
print(ScheduleOutput20240611.to_json())

# convert the object into a dict
schedule_output20240611_dict = schedule_output20240611_instance.to_dict()
# create an instance of ScheduleOutput20240611 from a dict
schedule_output20240611_from_dict = ScheduleOutput20240611.from_dict(schedule_output20240611_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


