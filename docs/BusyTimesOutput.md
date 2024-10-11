# BusyTimesOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** |  | 
**end** | **datetime** |  | 
**source** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.busy_times_output import BusyTimesOutput

# TODO update the JSON string below
json = "{}"
# create an instance of BusyTimesOutput from a JSON string
busy_times_output_instance = BusyTimesOutput.from_json(json)
# print the JSON string representation of the object
print(BusyTimesOutput.to_json())

# convert the object into a dict
busy_times_output_dict = busy_times_output_instance.to_dict()
# create an instance of BusyTimesOutput from a dict
busy_times_output_from_dict = BusyTimesOutput.from_dict(busy_times_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


