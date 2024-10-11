# RescheduleReasonDefaultFieldOutput20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **object** | This property is always true because it&#39;s a default field | 
**slug** | **str** |  | [default to 'rescheduleReason']
**type** | **str** |  | [default to 'textarea']
**required** | **bool** |  | 

## Example

```python
from openapi_client.models.reschedule_reason_default_field_output20240614 import RescheduleReasonDefaultFieldOutput20240614

# TODO update the JSON string below
json = "{}"
# create an instance of RescheduleReasonDefaultFieldOutput20240614 from a JSON string
reschedule_reason_default_field_output20240614_instance = RescheduleReasonDefaultFieldOutput20240614.from_json(json)
# print the JSON string representation of the object
print(RescheduleReasonDefaultFieldOutput20240614.to_json())

# convert the object into a dict
reschedule_reason_default_field_output20240614_dict = reschedule_reason_default_field_output20240614_instance.to_dict()
# create an instance of RescheduleReasonDefaultFieldOutput20240614 from a dict
reschedule_reason_default_field_output20240614_from_dict = RescheduleReasonDefaultFieldOutput20240614.from_dict(reschedule_reason_default_field_output20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


