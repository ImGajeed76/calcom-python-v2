# UpdateOrganizationAttributeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**type** | **object** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.update_organization_attribute_input import UpdateOrganizationAttributeInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationAttributeInput from a JSON string
update_organization_attribute_input_instance = UpdateOrganizationAttributeInput.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganizationAttributeInput.to_json())

# convert the object into a dict
update_organization_attribute_input_dict = update_organization_attribute_input_instance.to_dict()
# create an instance of UpdateOrganizationAttributeInput from a dict
update_organization_attribute_input_from_dict = UpdateOrganizationAttributeInput.from_dict(update_organization_attribute_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


