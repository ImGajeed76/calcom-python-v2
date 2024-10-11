# CreateOrgTeamDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**slug** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**cal_video_logo** | **str** |  | [optional] 
**app_logo** | **str** |  | [optional] 
**app_icon_logo** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**hide_branding** | **bool** |  | [optional] [default to False]
**is_private** | **bool** |  | [optional] 
**hide_book_a_team_member** | **bool** |  | [optional] 
**metadata** | **str** |  | [optional] 
**theme** | **str** |  | [optional] 
**brand_color** | **str** |  | [optional] 
**dark_brand_color** | **str** |  | [optional] 
**banner_url** | **str** |  | [optional] 
**time_format** | **float** |  | [optional] 
**time_zone** | **str** |  | [optional] [default to 'Europe/London']
**week_start** | **str** |  | [optional] [default to 'Sunday']
**auto_accept_creator** | **bool** |  | [optional] [default to True]

## Example

```python
from openapi_client.models.create_org_team_dto import CreateOrgTeamDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrgTeamDto from a JSON string
create_org_team_dto_instance = CreateOrgTeamDto.from_json(json)
# print the JSON string representation of the object
print(CreateOrgTeamDto.to_json())

# convert the object into a dict
create_org_team_dto_dict = create_org_team_dto_instance.to_dict()
# create an instance of CreateOrgTeamDto from a dict
create_org_team_dto_from_dict = CreateOrgTeamDto.from_dict(create_org_team_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


