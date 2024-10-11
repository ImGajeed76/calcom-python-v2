# SlotsControllerGetAvailableSlots200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**SlotsControllerGetAvailableSlots200ResponseData**](SlotsControllerGetAvailableSlots200ResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.slots_controller_get_available_slots200_response import SlotsControllerGetAvailableSlots200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SlotsControllerGetAvailableSlots200Response from a JSON string
slots_controller_get_available_slots200_response_instance = SlotsControllerGetAvailableSlots200Response.from_json(json)
# print the JSON string representation of the object
print(SlotsControllerGetAvailableSlots200Response.to_json())

# convert the object into a dict
slots_controller_get_available_slots200_response_dict = slots_controller_get_available_slots200_response_instance.to_dict()
# create an instance of SlotsControllerGetAvailableSlots200Response from a dict
slots_controller_get_available_slots200_response_from_dict = SlotsControllerGetAvailableSlots200Response.from_dict(slots_controller_get_available_slots200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


