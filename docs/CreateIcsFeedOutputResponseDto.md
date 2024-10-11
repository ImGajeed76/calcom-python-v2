# CreateIcsFeedOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**CreateIcsFeedOutput**](CreateIcsFeedOutput.md) |  | 

## Example

```python
from openapi_client.models.create_ics_feed_output_response_dto import CreateIcsFeedOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIcsFeedOutputResponseDto from a JSON string
create_ics_feed_output_response_dto_instance = CreateIcsFeedOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreateIcsFeedOutputResponseDto.to_json())

# convert the object into a dict
create_ics_feed_output_response_dto_dict = create_ics_feed_output_response_dto_instance.to_dict()
# create an instance of CreateIcsFeedOutputResponseDto from a dict
create_ics_feed_output_response_dto_from_dict = CreateIcsFeedOutputResponseDto.from_dict(create_ics_feed_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


