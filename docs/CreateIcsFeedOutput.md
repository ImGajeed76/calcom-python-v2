# CreateIcsFeedOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | The id of the calendar credential | 
**type** | **str** | The type of the calendar | 
**user_id** | **int** | The user id of the user that created the calendar | 
**team_id** | **int** | The team id of the user that created the calendar | 
**app_id** | **str** | The slug of the calendar | 
**invalid** | **bool** | Whether the calendar credentials are valid or not | 

## Example

```python
from openapi_client.models.create_ics_feed_output import CreateIcsFeedOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIcsFeedOutput from a JSON string
create_ics_feed_output_instance = CreateIcsFeedOutput.from_json(json)
# print the JSON string representation of the object
print(CreateIcsFeedOutput.to_json())

# convert the object into a dict
create_ics_feed_output_dict = create_ics_feed_output_instance.to_dict()
# create an instance of CreateIcsFeedOutput from a dict
create_ics_feed_output_from_dict = CreateIcsFeedOutput.from_dict(create_ics_feed_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


