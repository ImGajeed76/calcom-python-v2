# Calendar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** |  | 
**integration** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**primary** | **bool** |  | [optional] 
**read_only** | **bool** |  | 
**email** | **str** |  | [optional] 
**is_selected** | **bool** |  | 
**credential_id** | **float** |  | 

## Example

```python
from openapi_client.models.calendar import Calendar

# TODO update the JSON string below
json = "{}"
# create an instance of Calendar from a JSON string
calendar_instance = Calendar.from_json(json)
# print the JSON string representation of the object
print(Calendar.to_json())

# convert the object into a dict
calendar_dict = calendar_instance.to_dict()
# create an instance of Calendar from a dict
calendar_from_dict = Calendar.from_dict(calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


