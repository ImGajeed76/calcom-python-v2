# MultiSelectFieldInput20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | only allowed value for type is &#x60;multiselect&#x60; | 
**slug** | **str** | Unique identifier for the field in format &#x60;some-slug&#x60;. It is used to access response to this booking field during the booking | 
**label** | **str** |  | 
**required** | **bool** |  | 
**options** | **List[str]** |  | 

## Example

```python
from openapi_client.models.multi_select_field_input20240614 import MultiSelectFieldInput20240614

# TODO update the JSON string below
json = "{}"
# create an instance of MultiSelectFieldInput20240614 from a JSON string
multi_select_field_input20240614_instance = MultiSelectFieldInput20240614.from_json(json)
# print the JSON string representation of the object
print(MultiSelectFieldInput20240614.to_json())

# convert the object into a dict
multi_select_field_input20240614_dict = multi_select_field_input20240614_instance.to_dict()
# create an instance of MultiSelectFieldInput20240614 from a dict
multi_select_field_input20240614_from_dict = MultiSelectFieldInput20240614.from_dict(multi_select_field_input20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


