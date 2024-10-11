# CreatePhoneCallInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**your_phone_number** | **str** | Your phone number | 
**number_to_call** | **str** | Number to call | 
**cal_api_key** | **str** | CAL API Key | 
**enabled** | **object** | Enabled status | 
**template_type** | **str** | Template type | [default to 'CUSTOM_TEMPLATE']
**scheduler_name** | **str** | Scheduler name | [optional] 
**guest_name** | **str** | Guest name | [optional] 
**guest_email** | **str** | Guest email | [optional] 
**guest_company** | **str** | Guest company | [optional] 
**begin_message** | **str** | Begin message | [optional] 
**general_prompt** | **str** | General prompt | [optional] 

## Example

```python
from openapi_client.models.create_phone_call_input import CreatePhoneCallInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePhoneCallInput from a JSON string
create_phone_call_input_instance = CreatePhoneCallInput.from_json(json)
# print the JSON string representation of the object
print(CreatePhoneCallInput.to_json())

# convert the object into a dict
create_phone_call_input_dict = create_phone_call_input_instance.to_dict()
# create an instance of CreatePhoneCallInput from a dict
create_phone_call_input_from_dict = CreatePhoneCallInput.from_dict(create_phone_call_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


