# CreateOrganizationAttributeOptionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**slug** | **str** |  | 

## Example

```python
from openapi_client.models.create_organization_attribute_option_input import CreateOrganizationAttributeOptionInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationAttributeOptionInput from a JSON string
create_organization_attribute_option_input_instance = CreateOrganizationAttributeOptionInput.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationAttributeOptionInput.to_json())

# convert the object into a dict
create_organization_attribute_option_input_dict = create_organization_attribute_option_input_instance.to_dict()
# create an instance of CreateOrganizationAttributeOptionInput from a dict
create_organization_attribute_option_input_from_dict = CreateOrganizationAttributeOptionInput.from_dict(create_organization_attribute_option_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


