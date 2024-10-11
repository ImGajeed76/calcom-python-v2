# TeamWebhookOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**TeamWebhookOutputDto**](TeamWebhookOutputDto.md) |  | 

## Example

```python
from openapi_client.models.team_webhook_output_response_dto import TeamWebhookOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of TeamWebhookOutputResponseDto from a JSON string
team_webhook_output_response_dto_instance = TeamWebhookOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(TeamWebhookOutputResponseDto.to_json())

# convert the object into a dict
team_webhook_output_response_dto_dict = team_webhook_output_response_dto_instance.to_dict()
# create an instance of TeamWebhookOutputResponseDto from a dict
team_webhook_output_response_dto_from_dict = TeamWebhookOutputResponseDto.from_dict(team_webhook_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


