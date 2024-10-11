# ReserveSlotInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type_id** | **float** | Event Type ID for which timeslot is being reserved. | 
**slot_utc_start_date** | **str** | Start date of the slot in UTC timezone. | 
**slot_utc_end_date** | **str** | End date of the slot in UTC timezone. | 
**booking_uid** | **str** | Optional but only for events with seats. Used to retrieve booking of a seated event. | [optional] 

## Example

```python
from openapi_client.models.reserve_slot_input import ReserveSlotInput

# TODO update the JSON string below
json = "{}"
# create an instance of ReserveSlotInput from a JSON string
reserve_slot_input_instance = ReserveSlotInput.from_json(json)
# print the JSON string representation of the object
print(ReserveSlotInput.to_json())

# convert the object into a dict
reserve_slot_input_dict = reserve_slot_input_instance.to_dict()
# create an instance of ReserveSlotInput from a dict
reserve_slot_input_from_dict = ReserveSlotInput.from_dict(reserve_slot_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


