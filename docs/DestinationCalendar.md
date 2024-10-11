# DestinationCalendar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**integration** | **str** |  | 
**external_id** | **str** |  | 
**primary_email** | **str** |  | 
**user_id** | **float** |  | 
**event_type_id** | **float** |  | 
**credential_id** | **float** |  | 
**name** | **str** |  | [optional] 
**primary** | **bool** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**integration_title** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.destination_calendar import DestinationCalendar

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationCalendar from a JSON string
destination_calendar_instance = DestinationCalendar.from_json(json)
# print the JSON string representation of the object
print(DestinationCalendar.to_json())

# convert the object into a dict
destination_calendar_dict = destination_calendar_instance.to_dict()
# create an instance of DestinationCalendar from a dict
destination_calendar_from_dict = DestinationCalendar.from_dict(destination_calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


