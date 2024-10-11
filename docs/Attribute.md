# Attribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the attribute | 
**team_id** | **float** | The team ID associated with the attribute | 
**type** | **str** | The type of the attribute | 
**name** | **str** | The name of the attribute | 
**slug** | **str** | The slug of the attribute | 
**enabled** | **bool** | Whether the attribute is enabled and displayed on their profile | 
**users_can_edit_relation** | **bool** | Whether users can edit the relation | [optional] 

## Example

```python
from openapi_client.models.attribute import Attribute

# TODO update the JSON string below
json = "{}"
# create an instance of Attribute from a JSON string
attribute_instance = Attribute.from_json(json)
# print the JSON string representation of the object
print(Attribute.to_json())

# convert the object into a dict
attribute_dict = attribute_instance.to_dict()
# create an instance of Attribute from a dict
attribute_from_dict = Attribute.from_dict(attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


