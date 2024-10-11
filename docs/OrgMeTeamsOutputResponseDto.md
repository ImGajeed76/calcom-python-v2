# OrgMeTeamsOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[OrgTeamOutputDto]**](OrgTeamOutputDto.md) |  | 

## Example

```python
from openapi_client.models.org_me_teams_output_response_dto import OrgMeTeamsOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrgMeTeamsOutputResponseDto from a JSON string
org_me_teams_output_response_dto_instance = OrgMeTeamsOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(OrgMeTeamsOutputResponseDto.to_json())

# convert the object into a dict
org_me_teams_output_response_dto_dict = org_me_teams_output_response_dto_instance.to_dict()
# create an instance of OrgMeTeamsOutputResponseDto from a dict
org_me_teams_output_response_dto_from_dict = OrgMeTeamsOutputResponseDto.from_dict(org_me_teams_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


