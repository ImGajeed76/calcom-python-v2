# UpdateWebhookInputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload_template** | **str** | The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information | [optional] 
**triggers** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**subscriber_url** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_webhook_input_dto import UpdateWebhookInputDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookInputDto from a JSON string
update_webhook_input_dto_instance = UpdateWebhookInputDto.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookInputDto.to_json())

# convert the object into a dict
update_webhook_input_dto_dict = update_webhook_input_dto_instance.to_dict()
# create an instance of UpdateWebhookInputDto from a dict
update_webhook_input_dto_from_dict = UpdateWebhookInputDto.from_dict(update_webhook_input_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


