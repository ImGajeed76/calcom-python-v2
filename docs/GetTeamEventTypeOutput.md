# GetTeamEventTypeOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**TeamEventTypeOutput20240614**](TeamEventTypeOutput20240614.md) |  | 

## Example

```python
from openapi_client.models.get_team_event_type_output import GetTeamEventTypeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetTeamEventTypeOutput from a JSON string
get_team_event_type_output_instance = GetTeamEventTypeOutput.from_json(json)
# print the JSON string representation of the object
print(GetTeamEventTypeOutput.to_json())

# convert the object into a dict
get_team_event_type_output_dict = get_team_event_type_output_instance.to_dict()
# create an instance of GetTeamEventTypeOutput from a dict
get_team_event_type_output_from_dict = GetTeamEventTypeOutput.from_dict(get_team_event_type_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


