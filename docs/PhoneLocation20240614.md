# PhoneLocation20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | only allowed value for type is &#x60;phone&#x60; | 
**phone** | **str** |  | 
**public** | **bool** |  | 

## Example

```python
from openapi_client.models.phone_location20240614 import PhoneLocation20240614

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneLocation20240614 from a JSON string
phone_location20240614_instance = PhoneLocation20240614.from_json(json)
# print the JSON string representation of the object
print(PhoneLocation20240614.to_json())

# convert the object into a dict
phone_location20240614_dict = phone_location20240614_instance.to_dict()
# create an instance of PhoneLocation20240614 from a dict
phone_location20240614_from_dict = PhoneLocation20240614.from_dict(phone_location20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


