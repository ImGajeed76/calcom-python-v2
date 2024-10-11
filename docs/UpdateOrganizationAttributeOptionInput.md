# UpdateOrganizationAttributeOptionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_organization_attribute_option_input import UpdateOrganizationAttributeOptionInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationAttributeOptionInput from a JSON string
update_organization_attribute_option_input_instance = UpdateOrganizationAttributeOptionInput.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganizationAttributeOptionInput.to_json())

# convert the object into a dict
update_organization_attribute_option_input_dict = update_organization_attribute_option_input_instance.to_dict()
# create an instance of UpdateOrganizationAttributeOptionInput from a dict
update_organization_attribute_option_input_from_dict = UpdateOrganizationAttributeOptionInput.from_dict(update_organization_attribute_option_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


