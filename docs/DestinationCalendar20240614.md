# DestinationCalendar20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration** | **str** | The integration type of the destination calendar. Refer to the /api/v2/calendars endpoint to retrieve the integration type of your connected calendars. | 
**external_id** | **str** | The external ID of the destination calendar. Refer to the /api/v2/calendars endpoint to retrieve the external IDs of your connected calendars. | 

## Example

```python
from openapi_client.models.destination_calendar20240614 import DestinationCalendar20240614

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationCalendar20240614 from a JSON string
destination_calendar20240614_instance = DestinationCalendar20240614.from_json(json)
# print the JSON string representation of the object
print(DestinationCalendar20240614.to_json())

# convert the object into a dict
destination_calendar20240614_dict = destination_calendar20240614_instance.to_dict()
# create an instance of DestinationCalendar20240614 from a dict
destination_calendar20240614_from_dict = DestinationCalendar20240614.from_dict(destination_calendar20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


