# TeamWebhooksOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[TeamWebhookOutputDto]**](TeamWebhookOutputDto.md) |  | 

## Example

```python
from openapi_client.models.team_webhooks_output_response_dto import TeamWebhooksOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of TeamWebhooksOutputResponseDto from a JSON string
team_webhooks_output_response_dto_instance = TeamWebhooksOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(TeamWebhooksOutputResponseDto.to_json())

# convert the object into a dict
team_webhooks_output_response_dto_dict = team_webhooks_output_response_dto_instance.to_dict()
# create an instance of TeamWebhooksOutputResponseDto from a dict
team_webhooks_output_response_dto_from_dict = TeamWebhooksOutputResponseDto.from_dict(team_webhooks_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


