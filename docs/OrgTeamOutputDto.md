# OrgTeamOutputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**parent_id** | **float** |  | [optional] 
**name** | **str** |  | 
**slug** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**cal_video_logo** | **str** |  | [optional] 
**app_logo** | **str** |  | [optional] 
**app_icon_logo** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**hide_branding** | **bool** |  | [optional] 
**is_organization** | **bool** |  | [optional] 
**is_private** | **bool** |  | [optional] 
**hide_book_a_team_member** | **bool** |  | [optional] [default to False]
**metadata** | **str** |  | [optional] 
**theme** | **str** |  | [optional] 
**brand_color** | **str** |  | [optional] 
**dark_brand_color** | **str** |  | [optional] 
**banner_url** | **str** |  | [optional] 
**time_format** | **float** |  | [optional] 
**time_zone** | **str** |  | [optional] [default to 'Europe/London']
**week_start** | **str** |  | [optional] [default to 'Sunday']

## Example

```python
from openapi_client.models.org_team_output_dto import OrgTeamOutputDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrgTeamOutputDto from a JSON string
org_team_output_dto_instance = OrgTeamOutputDto.from_json(json)
# print the JSON string representation of the object
print(OrgTeamOutputDto.to_json())

# convert the object into a dict
org_team_output_dto_dict = org_team_output_dto_instance.to_dict()
# create an instance of OrgTeamOutputDto from a dict
org_team_output_dto_from_dict = OrgTeamOutputDto.from_dict(org_team_output_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


