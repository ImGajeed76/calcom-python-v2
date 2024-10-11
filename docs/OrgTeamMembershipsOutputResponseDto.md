# OrgTeamMembershipsOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[OrgTeamMembershipOutputDto]**](OrgTeamMembershipOutputDto.md) |  | 

## Example

```python
from openapi_client.models.org_team_memberships_output_response_dto import OrgTeamMembershipsOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrgTeamMembershipsOutputResponseDto from a JSON string
org_team_memberships_output_response_dto_instance = OrgTeamMembershipsOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(OrgTeamMembershipsOutputResponseDto.to_json())

# convert the object into a dict
org_team_memberships_output_response_dto_dict = org_team_memberships_output_response_dto_instance.to_dict()
# create an instance of OrgTeamMembershipsOutputResponseDto from a dict
org_team_memberships_output_response_dto_from_dict = OrgTeamMembershipsOutputResponseDto.from_dict(org_team_memberships_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


