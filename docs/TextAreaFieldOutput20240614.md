# TextAreaFieldOutput20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | only allowed value for type is &#x60;textarea&#x60; | 
**slug** | **str** | Unique identifier for the field in format &#x60;some-slug&#x60;. It is used to access response to this booking field during the booking | 
**label** | **str** |  | 
**required** | **bool** |  | 
**placeholder** | **str** |  | [optional] 
**is_default** | **object** | This property is always false because it&#39;s not default field but custom field | 

## Example

```python
from openapi_client.models.text_area_field_output20240614 import TextAreaFieldOutput20240614

# TODO update the JSON string below
json = "{}"
# create an instance of TextAreaFieldOutput20240614 from a JSON string
text_area_field_output20240614_instance = TextAreaFieldOutput20240614.from_json(json)
# print the JSON string representation of the object
print(TextAreaFieldOutput20240614.to_json())

# convert the object into a dict
text_area_field_output20240614_dict = text_area_field_output20240614_instance.to_dict()
# create an instance of TextAreaFieldOutput20240614 from a dict
text_area_field_output20240614_from_dict = TextAreaFieldOutput20240614.from_dict(text_area_field_output20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


