# CreateOrganizationAttributesOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**Attribute**](Attribute.md) |  | 

## Example

```python
from openapi_client.models.create_organization_attributes_output import CreateOrganizationAttributesOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationAttributesOutput from a JSON string
create_organization_attributes_output_instance = CreateOrganizationAttributesOutput.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationAttributesOutput.to_json())

# convert the object into a dict
create_organization_attributes_output_dict = create_organization_attributes_output_instance.to_dict()
# create an instance of CreateOrganizationAttributesOutput from a dict
create_organization_attributes_output_from_dict = CreateOrganizationAttributesOutput.from_dict(create_organization_attributes_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


