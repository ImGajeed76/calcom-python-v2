# DeletedCalendarCredentialsOutputResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**DeletedCalendarCredentialsOutputDto**](DeletedCalendarCredentialsOutputDto.md) |  | 

## Example

```python
from openapi_client.models.deleted_calendar_credentials_output_response_dto import DeletedCalendarCredentialsOutputResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedCalendarCredentialsOutputResponseDto from a JSON string
deleted_calendar_credentials_output_response_dto_instance = DeletedCalendarCredentialsOutputResponseDto.from_json(json)
# print the JSON string representation of the object
print(DeletedCalendarCredentialsOutputResponseDto.to_json())

# convert the object into a dict
deleted_calendar_credentials_output_response_dto_dict = deleted_calendar_credentials_output_response_dto_instance.to_dict()
# create an instance of DeletedCalendarCredentialsOutputResponseDto from a dict
deleted_calendar_credentials_output_response_dto_from_dict = DeletedCalendarCredentialsOutputResponseDto.from_dict(deleted_calendar_credentials_output_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


