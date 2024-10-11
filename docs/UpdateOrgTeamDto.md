# UpdateOrgTeamDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
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
**booking_limits** | **str** |  | [optional] 
**include_managed_events_in_limits** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.update_org_team_dto import UpdateOrgTeamDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrgTeamDto from a JSON string
update_org_team_dto_instance = UpdateOrgTeamDto.from_json(json)
# print the JSON string representation of the object
print(UpdateOrgTeamDto.to_json())

# convert the object into a dict
update_org_team_dto_dict = update_org_team_dto_instance.to_dict()
# create an instance of UpdateOrgTeamDto from a dict
update_org_team_dto_from_dict = UpdateOrgTeamDto.from_dict(update_org_team_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


