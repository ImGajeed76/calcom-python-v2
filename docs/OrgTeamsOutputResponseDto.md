# OrgTeamsOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[OrgTeamOutputDto]**](OrgTeamOutputDto.md) |  | 

## Example

```python
from openapi_client.models.org_teams_output_response_dto import OrgTeamsOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrgTeamsOutputResponseDto from a JSON string
org_teams_output_response_dto_instance = OrgTeamsOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(OrgTeamsOutputResponseDto.to_json())

# convert the object into a dict
org_teams_output_response_dto_dict = org_teams_output_response_dto_instance.to_dict()
# create an instance of OrgTeamsOutputResponseDto from a dict
org_teams_output_response_dto_from_dict = OrgTeamsOutputResponseDto.from_dict(org_teams_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


