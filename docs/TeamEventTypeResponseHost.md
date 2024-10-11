# TeamEventTypeResponseHost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **float** | Which user is the host of this event | 
**mandatory** | **bool** | Only relevant for round robin event types. If true then the user must attend round robin event always. | [optional] [default to False]
**priority** | **str** |  | [optional] [default to 'medium']
**name** | **str** |  | 

## Example

```python
from openapi_client.models.team_event_type_response_host import TeamEventTypeResponseHost

# TODO update the JSON string below
json = "{}"
# create an instance of TeamEventTypeResponseHost from a JSON string
team_event_type_response_host_instance = TeamEventTypeResponseHost.from_json(json)
# print the JSON string representation of the object
print(TeamEventTypeResponseHost.to_json())

# convert the object into a dict
team_event_type_response_host_dict = team_event_type_response_host_instance.to_dict()
# create an instance of TeamEventTypeResponseHost from a dict
team_event_type_response_host_from_dict = TeamEventTypeResponseHost.from_dict(team_event_type_response_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


