# DeleteOrgMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**OrgMembershipOutputDto**](OrgMembershipOutputDto.md) |  | 

## Example

```python
from openapi_client.models.delete_org_membership import DeleteOrgMembership

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOrgMembership from a JSON string
delete_org_membership_instance = DeleteOrgMembership.from_json(json)
# print the JSON string representation of the object
print(DeleteOrgMembership.to_json())

# convert the object into a dict
delete_org_membership_dict = delete_org_membership_instance.to_dict()
# create an instance of DeleteOrgMembership from a dict
delete_org_membership_from_dict = DeleteOrgMembership.from_dict(delete_org_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


