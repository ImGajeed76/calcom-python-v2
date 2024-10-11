# OrgTeamMembershipOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**OrgTeamMembershipOutputDto**](OrgTeamMembershipOutputDto.md) |  | 

## Example

```python
from openapi_client.models.org_team_membership_output_response_dto import OrgTeamMembershipOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrgTeamMembershipOutputResponseDto from a JSON string
org_team_membership_output_response_dto_instance = OrgTeamMembershipOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(OrgTeamMembershipOutputResponseDto.to_json())

# convert the object into a dict
org_team_membership_output_response_dto_dict = org_team_membership_output_response_dto_instance.to_dict()
# create an instance of OrgTeamMembershipOutputResponseDto from a dict
org_team_membership_output_response_dto_from_dict = OrgTeamMembershipOutputResponseDto.from_dict(org_team_membership_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


