# UpdateOrgMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**OrgMembershipOutputDto**](OrgMembershipOutputDto.md) |  | 

## Example

```python
from openapi_client.models.update_org_membership import UpdateOrgMembership

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrgMembership from a JSON string
update_org_membership_instance = UpdateOrgMembership.from_json(json)
# print the JSON string representation of the object
print(UpdateOrgMembership.to_json())

# convert the object into a dict
update_org_membership_dict = update_org_membership_instance.to_dict()
# create an instance of UpdateOrgMembership from a dict
update_org_membership_from_dict = UpdateOrgMembership.from_dict(update_org_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


