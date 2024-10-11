# SlotsControllerReserveSlot201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**SlotsControllerReserveSlot201ResponseData**](SlotsControllerReserveSlot201ResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.slots_controller_reserve_slot201_response import SlotsControllerReserveSlot201Response

# TODO update the JSON string below
json = "{}"
# create an instance of SlotsControllerReserveSlot201Response from a JSON string
slots_controller_reserve_slot201_response_instance = SlotsControllerReserveSlot201Response.from_json(json)
# print the JSON string representation of the object
print(SlotsControllerReserveSlot201Response.to_json())

# convert the object into a dict
slots_controller_reserve_slot201_response_dict = slots_controller_reserve_slot201_response_instance.to_dict()
# create an instance of SlotsControllerReserveSlot201Response from a dict
slots_controller_reserve_slot201_response_from_dict = SlotsControllerReserveSlot201Response.from_dict(slots_controller_reserve_slot201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


