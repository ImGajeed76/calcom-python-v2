# CreateTeamEventTypeOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**CreateTeamEventTypeOutputData**](CreateTeamEventTypeOutputData.md) |  | 

## Example

```python
from openapi_client.models.create_team_event_type_output import CreateTeamEventTypeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeamEventTypeOutput from a JSON string
create_team_event_type_output_instance = CreateTeamEventTypeOutput.from_json(json)
# print the JSON string representation of the object
print(CreateTeamEventTypeOutput.to_json())

# convert the object into a dict
create_team_event_type_output_dict = create_team_event_type_output_instance.to_dict()
# create an instance of CreateTeamEventTypeOutput from a dict
create_team_event_type_output_from_dict = CreateTeamEventTypeOutput.from_dict(create_team_event_type_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


