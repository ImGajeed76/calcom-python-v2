# Host


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **float** | Which user is the host of this event | 
**mandatory** | **bool** | Only relevant for round robin event types. If true then the user must attend round robin event always. | [optional] 
**priority** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.host import Host

# TODO update the JSON string below
json = "{}"
# create an instance of Host from a JSON string
host_instance = Host.from_json(json)
# print the JSON string representation of the object
print(Host.to_json())

# convert the object into a dict
host_dict = host_instance.to_dict()
# create an instance of Host from a dict
host_from_dict = Host.from_dict(host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


