# DestinationCalendarsOutputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **float** |  | 
**integration** | **str** |  | 
**external_id** | **str** |  | 
**credential_id** | **float** |  | 

## Example

```python
from openapi_client.models.destination_calendars_output_dto import DestinationCalendarsOutputDto

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationCalendarsOutputDto from a JSON string
destination_calendars_output_dto_instance = DestinationCalendarsOutputDto.from_json(json)
# print the JSON string representation of the object
print(DestinationCalendarsOutputDto.to_json())

# convert the object into a dict
destination_calendars_output_dto_dict = destination_calendars_output_dto_instance.to_dict()
# create an instance of DestinationCalendarsOutputDto from a dict
destination_calendars_output_dto_from_dict = DestinationCalendarsOutputDto.from_dict(destination_calendars_output_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


