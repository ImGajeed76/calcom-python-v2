# LocationDefaultFieldOutput20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **object** | This property is always true because it&#39;s a default field | 
**slug** | **str** |  | [default to 'location']
**type** | **str** |  | [default to 'radioInput']
**required** | **bool** |  | 

## Example

```python
from openapi_client.models.location_default_field_output20240614 import LocationDefaultFieldOutput20240614

# TODO update the JSON string below
json = "{}"
# create an instance of LocationDefaultFieldOutput20240614 from a JSON string
location_default_field_output20240614_instance = LocationDefaultFieldOutput20240614.from_json(json)
# print the JSON string representation of the object
print(LocationDefaultFieldOutput20240614.to_json())

# convert the object into a dict
location_default_field_output20240614_dict = location_default_field_output20240614_instance.to_dict()
# create an instance of LocationDefaultFieldOutput20240614 from a dict
location_default_field_output20240614_from_dict = LocationDefaultFieldOutput20240614.from_dict(location_default_field_output20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


