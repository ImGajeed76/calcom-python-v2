# DeletedCalendarCredentialsOutputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**type** | **str** |  | 
**user_id** | **float** |  | 
**team_id** | **float** |  | 
**app_id** | **str** |  | 
**invalid** | **bool** |  | 

## Example

```python
from openapi_client.models.deleted_calendar_credentials_output_dto import DeletedCalendarCredentialsOutputDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedCalendarCredentialsOutputDto from a JSON string
deleted_calendar_credentials_output_dto_instance = DeletedCalendarCredentialsOutputDto.from_json(json)
# print the JSON string representation of the object
print(DeletedCalendarCredentialsOutputDto.to_json())

# convert the object into a dict
deleted_calendar_credentials_output_dto_dict = deleted_calendar_credentials_output_dto_instance.to_dict()
# create an instance of DeletedCalendarCredentialsOutputDto from a dict
deleted_calendar_credentials_output_dto_from_dict = DeletedCalendarCredentialsOutputDto.from_dict(deleted_calendar_credentials_output_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


