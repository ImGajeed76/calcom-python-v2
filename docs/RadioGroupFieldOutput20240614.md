# RadioGroupFieldOutput20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | only allowed value for type is &#x60;radio&#x60; | 
**slug** | **str** | Unique identifier for the field in format &#x60;some-slug&#x60;. It is used to access response to this booking field during the booking | 
**label** | **str** |  | 
**required** | **bool** |  | 
**options** | **List[str]** |  | 
**is_default** | **object** | This property is always false because it&#39;s not default field but custom field | 

## Example

```python
from openapi_client.models.radio_group_field_output20240614 import RadioGroupFieldOutput20240614

# TODO update the JSON string below
json = "{}"
# create an instance of RadioGroupFieldOutput20240614 from a JSON string
radio_group_field_output20240614_instance = RadioGroupFieldOutput20240614.from_json(json)
# print the JSON string representation of the object
print(RadioGroupFieldOutput20240614.to_json())

# convert the object into a dict
radio_group_field_output20240614_dict = radio_group_field_output20240614_instance.to_dict()
# create an instance of RadioGroupFieldOutput20240614 from a dict
radio_group_field_output20240614_from_dict = RadioGroupFieldOutput20240614.from_dict(radio_group_field_output20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


