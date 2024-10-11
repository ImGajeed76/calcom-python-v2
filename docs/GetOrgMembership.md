# GetOrgMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**OrgMembershipOutputDto**](OrgMembershipOutputDto.md) |  | 

## Example

```python
from openapi_client.models.get_org_membership import GetOrgMembership

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrgMembership from a JSON string
get_org_membership_instance = GetOrgMembership.from_json(json)
# print the JSON string representation of the object
print(GetOrgMembership.to_json())

# convert the object into a dict
get_org_membership_dict = get_org_membership_instance.to_dict()
# create an instance of GetOrgMembership from a dict
get_org_membership_from_dict = GetOrgMembership.from_dict(get_org_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


