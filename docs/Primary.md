# Primary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** |  | 
**integration** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**primary** | **bool** |  | 
**read_only** | **bool** |  | 
**email** | **str** |  | [optional] 
**is_selected** | **bool** |  | 
**credential_id** | **float** |  | 

## Example

```python
from openapi_client.models.primary import Primary

# TODO update the JSON string below
json = "{}"
# create an instance of Primary from a JSON string
primary_instance = Primary.from_json(json)
# print the JSON string representation of the object
print(Primary.to_json())

# convert the object into a dict
primary_dict = primary_instance.to_dict()
# create an instance of Primary from a dict
primary_from_dict = Primary.from_dict(primary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


