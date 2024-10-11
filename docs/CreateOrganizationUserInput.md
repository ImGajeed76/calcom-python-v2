# CreateOrganizationUserInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email address | 
**username** | **str** | Username | [optional] 
**weekday** | **str** | Preferred weekday | [optional] 
**brand_color** | **str** | Brand color in HEX format | [optional] 
**dark_brand_color** | **str** | Dark brand color in HEX format | [optional] 
**hide_branding** | **bool** | Hide branding | [optional] 
**time_zone** | **str** | Time zone | [optional] 
**theme** | **str** | Theme | [optional] 
**app_theme** | **str** | Application theme | [optional] 
**time_format** | **float** | Time format | [optional] 
**default_schedule_id** | **float** | Default schedule ID | [optional] 
**locale** | **str** | Locale | [optional] [default to 'en']
**avatar_url** | **str** | Avatar URL | [optional] 
**organization_role** | **object** |  | 
**auto_accept** | **object** |  | 

## Example

```python
from openapi_client.models.create_organization_user_input import CreateOrganizationUserInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationUserInput from a JSON string
create_organization_user_input_instance = CreateOrganizationUserInput.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationUserInput.to_json())

# convert the object into a dict
create_organization_user_input_dict = create_organization_user_input_instance.to_dict()
# create an instance of CreateOrganizationUserInput from a dict
create_organization_user_input_from_dict = CreateOrganizationUserInput.from_dict(create_organization_user_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


