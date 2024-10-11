# AddressLocation20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | only allowed value for type is &#x60;address&#x60; | 
**address** | **str** |  | 
**public** | **bool** |  | 

## Example

```python
from openapi_client.models.address_location20240614 import AddressLocation20240614

# TODO update the JSON string below
json = "{}"
# create an instance of AddressLocation20240614 from a JSON string
address_location20240614_instance = AddressLocation20240614.from_json(json)
# print the JSON string representation of the object
print(AddressLocation20240614.to_json())

# convert the object into a dict
address_location20240614_dict = address_location20240614_instance.to_dict()
# create an instance of AddressLocation20240614 from a dict
address_location20240614_from_dict = AddressLocation20240614.from_dict(address_location20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


