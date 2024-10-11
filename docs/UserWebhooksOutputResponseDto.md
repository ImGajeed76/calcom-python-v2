# UserWebhooksOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[UserWebhookOutputDto]**](UserWebhookOutputDto.md) |  | 

## Example

```python
from openapi_client.models.user_webhooks_output_response_dto import UserWebhooksOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserWebhooksOutputResponseDto from a JSON string
user_webhooks_output_response_dto_instance = UserWebhooksOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(UserWebhooksOutputResponseDto.to_json())

# convert the object into a dict
user_webhooks_output_response_dto_dict = user_webhooks_output_response_dto_instance.to_dict()
# create an instance of UserWebhooksOutputResponseDto from a dict
user_webhooks_output_response_dto_from_dict = UserWebhooksOutputResponseDto.from_dict(user_webhooks_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


