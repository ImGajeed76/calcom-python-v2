# CreateIcsFeedInputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **List[str]** | An array of ICS URLs | 
**read_only** | **bool** | Whether to allowing writing to the calendar or not | [optional] [default to True]

## Example

```python
from openapi_client.models.create_ics_feed_input_dto import CreateIcsFeedInputDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIcsFeedInputDto from a JSON string
create_ics_feed_input_dto_instance = CreateIcsFeedInputDto.from_json(json)
# print the JSON string representation of the object
print(CreateIcsFeedInputDto.to_json())

# convert the object into a dict
create_ics_feed_input_dto_dict = create_ics_feed_input_dto_instance.to_dict()
# create an instance of CreateIcsFeedInputDto from a dict
create_ics_feed_input_dto_from_dict = CreateIcsFeedInputDto.from_dict(create_ics_feed_input_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


