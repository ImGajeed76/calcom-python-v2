# GetOrganizationUserOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**GetUserOutput**](GetUserOutput.md) |  | 

## Example

```python
from openapi_client.models.get_organization_user_output import GetOrganizationUserOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationUserOutput from a JSON string
get_organization_user_output_instance = GetOrganizationUserOutput.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationUserOutput.to_json())

# convert the object into a dict
get_organization_user_output_dict = get_organization_user_output_instance.to_dict()
# create an instance of GetOrganizationUserOutput from a dict
get_organization_user_output_from_dict = GetOrganizationUserOutput.from_dict(get_organization_user_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


