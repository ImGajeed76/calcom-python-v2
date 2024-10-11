# UserWebhookOutputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload_template** | **str** | The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information | 
**user_id** | **float** |  | 
**id** | **float** |  | 
**triggers** | **List[object]** |  | 
**subscriber_url** | **str** |  | 
**active** | **bool** |  | 
**secret** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_webhook_output_dto import UserWebhookOutputDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserWebhookOutputDto from a JSON string
user_webhook_output_dto_instance = UserWebhookOutputDto.from_json(json)
# print the JSON string representation of the object
print(UserWebhookOutputDto.to_json())

# convert the object into a dict
user_webhook_output_dto_dict = user_webhook_output_dto_instance.to_dict()
# create an instance of UserWebhookOutputDto from a dict
user_webhook_output_dto_from_dict = UserWebhookOutputDto.from_dict(user_webhook_output_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


