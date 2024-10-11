# GetSchedulesOutput20240611


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[ScheduleOutput20240611]**](ScheduleOutput20240611.md) |  | 
**error** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.get_schedules_output20240611 import GetSchedulesOutput20240611

# TODO update the JSON string below
json = "{}"
# create an instance of GetSchedulesOutput20240611 from a JSON string
get_schedules_output20240611_instance = GetSchedulesOutput20240611.from_json(json)
# print the JSON string representation of the object
print(GetSchedulesOutput20240611.to_json())

# convert the object into a dict
get_schedules_output20240611_dict = get_schedules_output20240611_instance.to_dict()
# create an instance of GetSchedulesOutput20240611 from a dict
get_schedules_output20240611_from_dict = GetSchedulesOutput20240611.from_dict(get_schedules_output20240611_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


