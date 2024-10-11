# CreateScheduleInput20240611


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**time_zone** | **str** | Timezone is used to calculate available times when an event using the schedule is booked. | 
**availability** | [**List[ScheduleAvailabilityInput20240611]**](ScheduleAvailabilityInput20240611.md) | Each object contains days and times when the user is available. If not passed, the default availability is Monday to Friday from 09:00 to 17:00. | [optional] 
**is_default** | **bool** | Each user should have 1 default schedule. If you specified &#x60;timeZone&#x60; when creating managed user, then the default schedule will be created with that timezone.     Default schedule means that if an event type is not tied to a specific schedule then the default schedule is used. | 
**overrides** | [**List[ScheduleOverrideInput20240611]**](ScheduleOverrideInput20240611.md) | Need to change availability for a specific date? Add an override. | [optional] 

## Example

```python
from openapi_client.models.create_schedule_input20240611 import CreateScheduleInput20240611

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduleInput20240611 from a JSON string
create_schedule_input20240611_instance = CreateScheduleInput20240611.from_json(json)
# print the JSON string representation of the object
print(CreateScheduleInput20240611.to_json())

# convert the object into a dict
create_schedule_input20240611_dict = create_schedule_input20240611_instance.to_dict()
# create an instance of CreateScheduleInput20240611 from a dict
create_schedule_input20240611_from_dict = CreateScheduleInput20240611.from_dict(create_schedule_input20240611_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


