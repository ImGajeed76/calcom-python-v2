# UpdateOrganizationAttributesOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**Attribute**](Attribute.md) |  | 

## Example

```python
from openapi_client.models.update_organization_attributes_output import UpdateOrganizationAttributesOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationAttributesOutput from a JSON string
update_organization_attributes_output_instance = UpdateOrganizationAttributesOutput.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganizationAttributesOutput.to_json())

# convert the object into a dict
update_organization_attributes_output_dict = update_organization_attributes_output_instance.to_dict()
# create an instance of UpdateOrganizationAttributesOutput from a dict
update_organization_attributes_output_from_dict = UpdateOrganizationAttributesOutput.from_dict(update_organization_attributes_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


