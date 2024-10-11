# GetAllOrgMemberships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**OrgMembershipOutputDto**](OrgMembershipOutputDto.md) |  | 

## Example

```python
from openapi_client.models.get_all_org_memberships import GetAllOrgMemberships

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllOrgMemberships from a JSON string
get_all_org_memberships_instance = GetAllOrgMemberships.from_json(json)
# print the JSON string representation of the object
print(GetAllOrgMemberships.to_json())

# convert the object into a dict
get_all_org_memberships_dict = get_all_org_memberships_instance.to_dict()
# create an instance of GetAllOrgMemberships from a dict
get_all_org_memberships_from_dict = GetAllOrgMemberships.from_dict(get_all_org_memberships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


