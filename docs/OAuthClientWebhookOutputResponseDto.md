# OAuthClientWebhookOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**OAuthClientWebhookOutputDto**](OAuthClientWebhookOutputDto.md) |  | 

## Example

```python
from openapi_client.models.o_auth_client_webhook_output_response_dto import OAuthClientWebhookOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthClientWebhookOutputResponseDto from a JSON string
o_auth_client_webhook_output_response_dto_instance = OAuthClientWebhookOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(OAuthClientWebhookOutputResponseDto.to_json())

# convert the object into a dict
o_auth_client_webhook_output_response_dto_dict = o_auth_client_webhook_output_response_dto_instance.to_dict()
# create an instance of OAuthClientWebhookOutputResponseDto from a dict
o_auth_client_webhook_output_response_dto_from_dict = OAuthClientWebhookOutputResponseDto.from_dict(o_auth_client_webhook_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


