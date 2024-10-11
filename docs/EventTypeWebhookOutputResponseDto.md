# EventTypeWebhookOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**EventTypeWebhookOutputDto**](EventTypeWebhookOutputDto.md) |  | 

## Example

```python
from openapi_client.models.event_type_webhook_output_response_dto import EventTypeWebhookOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of EventTypeWebhookOutputResponseDto from a JSON string
event_type_webhook_output_response_dto_instance = EventTypeWebhookOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(EventTypeWebhookOutputResponseDto.to_json())

# convert the object into a dict
event_type_webhook_output_response_dto_dict = event_type_webhook_output_response_dto_instance.to_dict()
# create an instance of EventTypeWebhookOutputResponseDto from a dict
event_type_webhook_output_response_dto_from_dict = EventTypeWebhookOutputResponseDto.from_dict(event_type_webhook_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


