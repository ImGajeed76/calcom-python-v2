# UpdateScheduleOutput20240611


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**ScheduleOutput20240611**](ScheduleOutput20240611.md) |  | 
**error** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.update_schedule_output20240611 import UpdateScheduleOutput20240611

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduleOutput20240611 from a JSON string
update_schedule_output20240611_instance = UpdateScheduleOutput20240611.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduleOutput20240611.to_json())

# convert the object into a dict
update_schedule_output20240611_dict = update_schedule_output20240611_instance.to_dict()
# create an instance of UpdateScheduleOutput20240611 from a dict
update_schedule_output20240611_from_dict = UpdateScheduleOutput20240611.from_dict(update_schedule_output20240611_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


