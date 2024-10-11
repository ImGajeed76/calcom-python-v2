# UpdateTeamEventTypeOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**CreateTeamEventTypeOutputData**](CreateTeamEventTypeOutputData.md) |  | 

## Example

```python
from openapi_client.models.update_team_event_type_output import UpdateTeamEventTypeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTeamEventTypeOutput from a JSON string
update_team_event_type_output_instance = UpdateTeamEventTypeOutput.from_json(json)
# print the JSON string representation of the object
print(UpdateTeamEventTypeOutput.to_json())

# convert the object into a dict
update_team_event_type_output_dict = update_team_event_type_output_instance.to_dict()
# create an instance of UpdateTeamEventTypeOutput from a dict
update_team_event_type_output_from_dict = UpdateTeamEventTypeOutput.from_dict(update_team_event_type_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


