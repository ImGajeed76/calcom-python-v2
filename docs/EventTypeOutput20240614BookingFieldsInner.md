# EventTypeOutput20240614BookingFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **object** | This property is always false because it&#39;s not default field but custom field | 
**slug** | **str** | Unique identifier for the field in format &#x60;some-slug&#x60;. It is used to access response to this booking field during the booking | 
**type** | **str** |  | [default to 'multiemail']
**required** | **bool** |  | 
**label** | **str** |  | 
**placeholder** | **str** |  | [optional] 
**options** | **List[str]** |  | 

## Example

```python
from openapi_client.models.event_type_output20240614_booking_fields_inner import EventTypeOutput20240614BookingFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EventTypeOutput20240614BookingFieldsInner from a JSON string
event_type_output20240614_booking_fields_inner_instance = EventTypeOutput20240614BookingFieldsInner.from_json(json)
# print the JSON string representation of the object
print(EventTypeOutput20240614BookingFieldsInner.to_json())

# convert the object into a dict
event_type_output20240614_booking_fields_inner_dict = event_type_output20240614_booking_fields_inner_instance.to_dict()
# create an instance of EventTypeOutput20240614BookingFieldsInner from a dict
event_type_output20240614_booking_fields_inner_from_dict = EventTypeOutput20240614BookingFieldsInner.from_dict(event_type_output20240614_booking_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


