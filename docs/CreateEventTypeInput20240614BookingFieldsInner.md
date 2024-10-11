# CreateEventTypeInput20240614BookingFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | only allowed value for type is &#x60;boolean&#x60; | 
**slug** | **str** | Unique identifier for the field in format &#x60;some-slug&#x60;. It is used to access response to this booking field during the booking | 
**label** | **str** |  | 
**required** | **bool** |  | 
**placeholder** | **str** |  | 
**options** | **List[str]** |  | 

## Example

```python
from openapi_client.models.create_event_type_input20240614_booking_fields_inner import CreateEventTypeInput20240614BookingFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventTypeInput20240614BookingFieldsInner from a JSON string
create_event_type_input20240614_booking_fields_inner_instance = CreateEventTypeInput20240614BookingFieldsInner.from_json(json)
# print the JSON string representation of the object
print(CreateEventTypeInput20240614BookingFieldsInner.to_json())

# convert the object into a dict
create_event_type_input20240614_booking_fields_inner_dict = create_event_type_input20240614_booking_fields_inner_instance.to_dict()
# create an instance of CreateEventTypeInput20240614BookingFieldsInner from a dict
create_event_type_input20240614_booking_fields_inner_from_dict = CreateEventTypeInput20240614BookingFieldsInner.from_dict(create_event_type_input20240614_booking_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


