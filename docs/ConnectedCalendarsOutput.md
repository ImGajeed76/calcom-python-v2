# ConnectedCalendarsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**ConnectedCalendarsData**](ConnectedCalendarsData.md) |  | 

## Example

```python
from openapi_client.models.connected_calendars_output import ConnectedCalendarsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedCalendarsOutput from a JSON string
connected_calendars_output_instance = ConnectedCalendarsOutput.from_json(json)
# print the JSON string representation of the object
print(ConnectedCalendarsOutput.to_json())

# convert the object into a dict
connected_calendars_output_dict = connected_calendars_output_instance.to_dict()
# create an instance of ConnectedCalendarsOutput from a dict
connected_calendars_output_from_dict = ConnectedCalendarsOutput.from_dict(connected_calendars_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


