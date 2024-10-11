# CreateEventTypeInput20240614ConfirmationPolicy

Specify how the booking needs to be manually confirmed before it is pushed to the integrations and a confirmation mail is sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The policy that determines when confirmation is required | 
**notice_threshold** | [**NoticeThreshold20240614**](NoticeThreshold20240614.md) | The notice threshold required before confirmation is needed. Required when type is &#39;time&#39;. | [optional] 
**disabled** | **bool** | Indicates if the option is disabled | [default to False]

## Example

```python
from openapi_client.models.create_event_type_input20240614_confirmation_policy import CreateEventTypeInput20240614ConfirmationPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventTypeInput20240614ConfirmationPolicy from a JSON string
create_event_type_input20240614_confirmation_policy_instance = CreateEventTypeInput20240614ConfirmationPolicy.from_json(json)
# print the JSON string representation of the object
print(CreateEventTypeInput20240614ConfirmationPolicy.to_json())

# convert the object into a dict
create_event_type_input20240614_confirmation_policy_dict = create_event_type_input20240614_confirmation_policy_instance.to_dict()
# create an instance of CreateEventTypeInput20240614ConfirmationPolicy from a dict
create_event_type_input20240614_confirmation_policy_from_dict = CreateEventTypeInput20240614ConfirmationPolicy.from_dict(create_event_type_input20240614_confirmation_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


