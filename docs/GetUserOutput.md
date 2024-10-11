# GetUserOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | The ID of the user | 
**username** | **str** | The username of the user | [optional] 
**name** | **str** | The name of the user | [optional] 
**email** | **str** | The email of the user | 
**email_verified** | **datetime** | The date when the email was verified | [optional] 
**bio** | **str** | The bio of the user | [optional] 
**avatar_url** | **str** | The URL of the user&#39;s avatar | [optional] 
**time_zone** | **str** | The time zone of the user | 
**week_start** | **str** | The week start day of the user | 
**app_theme** | **str** | The app theme of the user | [optional] 
**theme** | **str** | The theme of the user | [optional] 
**default_schedule_id** | **float** | The ID of the default schedule for the user | [optional] 
**locale** | **str** | The locale of the user | [optional] 
**time_format** | **float** | The time format of the user | [optional] 
**hide_branding** | **bool** | Whether to hide branding for the user | 
**brand_color** | **str** | The brand color of the user | [optional] 
**dark_brand_color** | **str** | The dark brand color of the user | [optional] 
**allow_dynamic_booking** | **bool** | Whether dynamic booking is allowed for the user | [optional] 
**created_date** | **datetime** | The date when the user was created | 
**verified** | **bool** | Whether the user is verified | [optional] 
**invited_to** | **float** | The ID of the user who invited this user | [optional] 

## Example

```python
from openapi_client.models.get_user_output import GetUserOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserOutput from a JSON string
get_user_output_instance = GetUserOutput.from_json(json)
# print the JSON string representation of the object
print(GetUserOutput.to_json())

# convert the object into a dict
get_user_output_dict = get_user_output_instance.to_dict()
# create an instance of GetUserOutput from a dict
get_user_output_from_dict = GetUserOutput.from_dict(get_user_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


