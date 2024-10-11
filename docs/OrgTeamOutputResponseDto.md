# OrgTeamOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**OrgTeamOutputDto**](OrgTeamOutputDto.md) |  | 

## Example

```python
from openapi_client.models.org_team_output_response_dto import OrgTeamOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrgTeamOutputResponseDto from a JSON string
org_team_output_response_dto_instance = OrgTeamOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(OrgTeamOutputResponseDto.to_json())

# convert the object into a dict
org_team_output_response_dto_dict = org_team_output_response_dto_instance.to_dict()
# create an instance of OrgTeamOutputResponseDto from a dict
org_team_output_response_dto_from_dict = OrgTeamOutputResponseDto.from_dict(org_team_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


