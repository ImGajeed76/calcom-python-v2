# GetOrganizationAttributesOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[Attribute]**](Attribute.md) |  | 

## Example

```python
from openapi_client.models.get_organization_attributes_output import GetOrganizationAttributesOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationAttributesOutput from a JSON string
get_organization_attributes_output_instance = GetOrganizationAttributesOutput.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationAttributesOutput.to_json())

# convert the object into a dict
get_organization_attributes_output_dict = get_organization_attributes_output_instance.to_dict()
# create an instance of GetOrganizationAttributesOutput from a dict
get_organization_attributes_output_from_dict = GetOrganizationAttributesOutput.from_dict(get_organization_attributes_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


