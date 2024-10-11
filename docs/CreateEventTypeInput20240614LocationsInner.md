# CreateEventTypeInput20240614LocationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | only allowed value for type is &#x60;phone&#x60; | 
**address** | **str** |  | 
**public** | **bool** |  | 
**link** | **str** |  | 
**integration** | **str** |  | 
**phone** | **str** |  | 

## Example

```python
from openapi_client.models.create_event_type_input20240614_locations_inner import CreateEventTypeInput20240614LocationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventTypeInput20240614LocationsInner from a JSON string
create_event_type_input20240614_locations_inner_instance = CreateEventTypeInput20240614LocationsInner.from_json(json)
# print the JSON string representation of the object
print(CreateEventTypeInput20240614LocationsInner.to_json())

# convert the object into a dict
create_event_type_input20240614_locations_inner_dict = create_event_type_input20240614_locations_inner_instance.to_dict()
# create an instance of CreateEventTypeInput20240614LocationsInner from a dict
create_event_type_input20240614_locations_inner_from_dict = CreateEventTypeInput20240614LocationsInner.from_dict(create_event_type_input20240614_locations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


