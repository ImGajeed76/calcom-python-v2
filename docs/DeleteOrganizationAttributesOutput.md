# DeleteOrganizationAttributesOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**Attribute**](Attribute.md) |  | 

## Example

```python
from openapi_client.models.delete_organization_attributes_output import DeleteOrganizationAttributesOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOrganizationAttributesOutput from a JSON string
delete_organization_attributes_output_instance = DeleteOrganizationAttributesOutput.from_json(json)
# print the JSON string representation of the object
print(DeleteOrganizationAttributesOutput.to_json())

# convert the object into a dict
delete_organization_attributes_output_dict = delete_organization_attributes_output_instance.to_dict()
# create an instance of DeleteOrganizationAttributesOutput from a dict
delete_organization_attributes_output_from_dict = DeleteOrganizationAttributesOutput.from_dict(delete_organization_attributes_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


