# UserWebhookOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**UserWebhookOutputDto**](UserWebhookOutputDto.md) |  | 

## Example

```python
from openapi_client.models.user_webhook_output_response_dto import UserWebhookOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserWebhookOutputResponseDto from a JSON string
user_webhook_output_response_dto_instance = UserWebhookOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(UserWebhookOutputResponseDto.to_json())

# convert the object into a dict
user_webhook_output_response_dto_dict = user_webhook_output_response_dto_instance.to_dict()
# create an instance of UserWebhookOutputResponseDto from a dict
user_webhook_output_response_dto_from_dict = UserWebhookOutputResponseDto.from_dict(user_webhook_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


