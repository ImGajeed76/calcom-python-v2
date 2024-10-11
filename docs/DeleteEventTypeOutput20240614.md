# DeleteEventTypeOutput20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**DeleteData20240614**](DeleteData20240614.md) |  | 

## Example

```python
from openapi_client.models.delete_event_type_output20240614 import DeleteEventTypeOutput20240614

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteEventTypeOutput20240614 from a JSON string
delete_event_type_output20240614_instance = DeleteEventTypeOutput20240614.from_json(json)
# print the JSON string representation of the object
print(DeleteEventTypeOutput20240614.to_json())

# convert the object into a dict
delete_event_type_output20240614_dict = delete_event_type_output20240614_instance.to_dict()
# create an instance of DeleteEventTypeOutput20240614 from a dict
delete_event_type_output20240614_from_dict = DeleteEventTypeOutput20240614.from_dict(delete_event_type_output20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


