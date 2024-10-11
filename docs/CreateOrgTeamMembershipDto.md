# CreateOrgTeamMembershipDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [default to 'MEMBER']
**user_id** | **float** |  | 
**accepted** | **bool** |  | [optional] [default to False]
**disable_impersonation** | **bool** |  | [optional] [default to False]

## Example

```python
from openapi_client.models.create_org_team_membership_dto import CreateOrgTeamMembershipDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrgTeamMembershipDto from a JSON string
create_org_team_membership_dto_instance = CreateOrgTeamMembershipDto.from_json(json)
# print the JSON string representation of the object
print(CreateOrgTeamMembershipDto.to_json())

# convert the object into a dict
create_org_team_membership_dto_dict = create_org_team_membership_dto_instance.to_dict()
# create an instance of CreateOrgTeamMembershipDto from a dict
create_org_team_membership_dto_from_dict = CreateOrgTeamMembershipDto.from_dict(create_org_team_membership_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


