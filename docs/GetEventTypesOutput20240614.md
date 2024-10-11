# GetEventTypesOutput20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[EventTypeOutput20240614]**](EventTypeOutput20240614.md) |  | 

## Example

```python
from openapi_client.models.get_event_types_output20240614 import GetEventTypesOutput20240614

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventTypesOutput20240614 from a JSON string
get_event_types_output20240614_instance = GetEventTypesOutput20240614.from_json(json)
# print the JSON string representation of the object
print(GetEventTypesOutput20240614.to_json())

# convert the object into a dict
get_event_types_output20240614_dict = get_event_types_output20240614_instance.to_dict()
# create an instance of GetEventTypesOutput20240614 from a dict
get_event_types_output20240614_from_dict = GetEventTypesOutput20240614.from_dict(get_event_types_output20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


