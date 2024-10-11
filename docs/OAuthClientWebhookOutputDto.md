# OAuthClientWebhookOutputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload_template** | **str** | The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information | 
**o_auth_client_id** | **str** |  | 
**id** | **float** |  | 
**triggers** | **List[object]** |  | 
**subscriber_url** | **str** |  | 
**active** | **bool** |  | 
**secret** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.o_auth_client_webhook_output_dto import OAuthClientWebhookOutputDto

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthClientWebhookOutputDto from a JSON string
o_auth_client_webhook_output_dto_instance = OAuthClientWebhookOutputDto.from_json(json)
# print the JSON string representation of the object
print(OAuthClientWebhookOutputDto.to_json())

# convert the object into a dict
o_auth_client_webhook_output_dto_dict = o_auth_client_webhook_output_dto_instance.to_dict()
# create an instance of OAuthClientWebhookOutputDto from a dict
o_auth_client_webhook_output_dto_from_dict = OAuthClientWebhookOutputDto.from_dict(o_auth_client_webhook_output_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


