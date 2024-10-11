# DeleteCalendarCredentialsInputBodyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Credential ID of the calendar to delete, as returned by the /calendars endpoint | 

## Example

```python
from openapi_client.models.delete_calendar_credentials_input_body_dto import DeleteCalendarCredentialsInputBodyDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCalendarCredentialsInputBodyDto from a JSON string
delete_calendar_credentials_input_body_dto_instance = DeleteCalendarCredentialsInputBodyDto.from_json(json)
# print the JSON string representation of the object
print(DeleteCalendarCredentialsInputBodyDto.to_json())

# convert the object into a dict
delete_calendar_credentials_input_body_dto_dict = delete_calendar_credentials_input_body_dto_instance.to_dict()
# create an instance of DeleteCalendarCredentialsInputBodyDto from a dict
delete_calendar_credentials_input_body_dto_from_dict = DeleteCalendarCredentialsInputBodyDto.from_dict(delete_calendar_credentials_input_body_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


