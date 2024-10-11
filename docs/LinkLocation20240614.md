# LinkLocation20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | only allowed value for type is &#x60;link&#x60; | 
**link** | **str** |  | 
**public** | **bool** |  | 

## Example

```python
from openapi_client.models.link_location20240614 import LinkLocation20240614

# TODO update the JSON string below
json = "{}"
# create an instance of LinkLocation20240614 from a JSON string
link_location20240614_instance = LinkLocation20240614.from_json(json)
# print the JSON string representation of the object
print(LinkLocation20240614.to_json())

# convert the object into a dict
link_location20240614_dict = link_location20240614_instance.to_dict()
# create an instance of LinkLocation20240614 from a dict
link_location20240614_from_dict = LinkLocation20240614.from_dict(link_location20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


