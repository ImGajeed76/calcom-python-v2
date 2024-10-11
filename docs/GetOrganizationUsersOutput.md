# GetOrganizationUsersOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[GetUserOutput]**](GetUserOutput.md) |  | 

## Example

```python
from openapi_client.models.get_organization_users_output import GetOrganizationUsersOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationUsersOutput from a JSON string
get_organization_users_output_instance = GetOrganizationUsersOutput.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationUsersOutput.to_json())

# convert the object into a dict
get_organization_users_output_dict = get_organization_users_output_instance.to_dict()
# create an instance of GetOrganizationUsersOutput from a dict
get_organization_users_output_from_dict = GetOrganizationUsersOutput.from_dict(get_organization_users_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


