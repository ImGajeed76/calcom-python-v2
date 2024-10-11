# Recurrence20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **float** | Repeats every {count} week | month | year | 
**occurrences** | **float** | Repeats for a maximum of {count} events | 
**frequency** | **str** |  | 

## Example

```python
from openapi_client.models.recurrence20240614 import Recurrence20240614

# TODO update the JSON string below
json = "{}"
# create an instance of Recurrence20240614 from a JSON string
recurrence20240614_instance = Recurrence20240614.from_json(json)
# print the JSON string representation of the object
print(Recurrence20240614.to_json())

# convert the object into a dict
recurrence20240614_dict = recurrence20240614_instance.to_dict()
# create an instance of Recurrence20240614 from a dict
recurrence20240614_from_dict = Recurrence20240614.from_dict(recurrence20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


