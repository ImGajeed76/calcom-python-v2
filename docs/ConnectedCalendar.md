# ConnectedCalendar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration** | [**Integration**](Integration.md) |  | 
**credential_id** | **float** |  | 
**primary** | [**Primary**](Primary.md) |  | [optional] 
**calendars** | [**List[Calendar]**](Calendar.md) |  | [optional] 

## Example

```python
from openapi_client.models.connected_calendar import ConnectedCalendar

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedCalendar from a JSON string
connected_calendar_instance = ConnectedCalendar.from_json(json)
# print the JSON string representation of the object
print(ConnectedCalendar.to_json())

# convert the object into a dict
connected_calendar_dict = connected_calendar_instance.to_dict()
# create an instance of ConnectedCalendar from a dict
connected_calendar_from_dict = ConnectedCalendar.from_dict(connected_calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


