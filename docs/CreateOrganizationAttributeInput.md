# CreateOrganizationAttributeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**slug** | **str** |  | 
**type** | **object** |  | 
**options** | [**List[CreateOrganizationAttributeOptionInput]**](CreateOrganizationAttributeOptionInput.md) |  | 
**enabled** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.create_organization_attribute_input import CreateOrganizationAttributeInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationAttributeInput from a JSON string
create_organization_attribute_input_instance = CreateOrganizationAttributeInput.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationAttributeInput.to_json())

# convert the object into a dict
create_organization_attribute_input_dict = create_organization_attribute_input_instance.to_dict()
# create an instance of CreateOrganizationAttributeInput from a dict
create_organization_attribute_input_from_dict = CreateOrganizationAttributeInput.from_dict(create_organization_attribute_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


