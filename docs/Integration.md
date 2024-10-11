# Integration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_data** | **object** |  | [optional] 
**dir_name** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | 
**installed** | **bool** |  | [optional] 
**type** | **str** |  | 
**title** | **str** |  | [optional] 
**variant** | **str** |  | 
**category** | **str** |  | [optional] 
**categories** | **List[str]** |  | 
**logo** | **str** |  | 
**publisher** | **str** |  | 
**slug** | **str** |  | 
**url** | **str** |  | 
**email** | **str** |  | 
**location_option** | **object** |  | 

## Example

```python
from openapi_client.models.integration import Integration

# TODO update the JSON string below
json = "{}"
# create an instance of Integration from a JSON string
integration_instance = Integration.from_json(json)
# print the JSON string representation of the object
print(Integration.to_json())

# convert the object into a dict
integration_dict = integration_instance.to_dict()
# create an instance of Integration from a dict
integration_from_dict = Integration.from_dict(integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


