# AddressFieldOutput20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | only allowed value for type is &#x60;address&#x60; | 
**slug** | **str** | Unique identifier for the field in format &#x60;some-slug&#x60;. It is used to access response to this booking field during the booking | 
**label** | **str** |  | 
**required** | **bool** |  | 
**placeholder** | **str** |  | [optional] 
**is_default** | **object** | This property is always false because it&#39;s not default field but custom field | 

## Example

```python
from openapi_client.models.address_field_output20240614 import AddressFieldOutput20240614

# TODO update the JSON string below
json = "{}"
# create an instance of AddressFieldOutput20240614 from a JSON string
address_field_output20240614_instance = AddressFieldOutput20240614.from_json(json)
# print the JSON string representation of the object
print(AddressFieldOutput20240614.to_json())

# convert the object into a dict
address_field_output20240614_dict = address_field_output20240614_instance.to_dict()
# create an instance of AddressFieldOutput20240614 from a dict
address_field_output20240614_from_dict = AddressFieldOutput20240614.from_dict(address_field_output20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


