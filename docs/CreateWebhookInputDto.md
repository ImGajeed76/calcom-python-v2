# CreateWebhookInputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload_template** | **str** | The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information | [optional] 
**triggers** | **str** |  | 
**active** | **bool** |  | 
**subscriber_url** | **str** |  | 
**secret** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_webhook_input_dto import CreateWebhookInputDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookInputDto from a JSON string
create_webhook_input_dto_instance = CreateWebhookInputDto.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookInputDto.to_json())

# convert the object into a dict
create_webhook_input_dto_dict = create_webhook_input_dto_instance.to_dict()
# create an instance of CreateWebhookInputDto from a dict
create_webhook_input_dto_from_dict = CreateWebhookInputDto.from_dict(create_webhook_input_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


