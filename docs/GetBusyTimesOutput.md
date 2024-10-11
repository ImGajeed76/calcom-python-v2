# GetBusyTimesOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[BusyTimesOutput]**](BusyTimesOutput.md) |  | 

## Example

```python
from openapi_client.models.get_busy_times_output import GetBusyTimesOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetBusyTimesOutput from a JSON string
get_busy_times_output_instance = GetBusyTimesOutput.from_json(json)
# print the JSON string representation of the object
print(GetBusyTimesOutput.to_json())

# convert the object into a dict
get_busy_times_output_dict = get_busy_times_output_instance.to_dict()
# create an instance of GetBusyTimesOutput from a dict
get_busy_times_output_from_dict = GetBusyTimesOutput.from_dict(get_busy_times_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


