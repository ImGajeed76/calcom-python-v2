# UpdateOrgTeamMembershipDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] [default to 'MEMBER']
**accepted** | **bool** |  | [optional] [default to False]
**disable_impersonation** | **bool** |  | [optional] [default to False]

## Example

```python
from openapi_client.models.update_org_team_membership_dto import UpdateOrgTeamMembershipDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrgTeamMembershipDto from a JSON string
update_org_team_membership_dto_instance = UpdateOrgTeamMembershipDto.from_json(json)
# print the JSON string representation of the object
print(UpdateOrgTeamMembershipDto.to_json())

# convert the object into a dict
update_org_team_membership_dto_dict = update_org_team_membership_dto_instance.to_dict()
# create an instance of UpdateOrgTeamMembershipDto from a dict
update_org_team_membership_dto_from_dict = UpdateOrgTeamMembershipDto.from_dict(update_org_team_membership_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


