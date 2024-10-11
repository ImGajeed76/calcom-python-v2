# RangeWindow20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Whether the window should be business days, calendar days or a range of dates | 
**value** | **List[str]** | Date range for when this event can be booked. | 

## Example

```python
from openapi_client.models.range_window20240614 import RangeWindow20240614

# TODO update the JSON string below
json = "{}"
# create an instance of RangeWindow20240614 from a JSON string
range_window20240614_instance = RangeWindow20240614.from_json(json)
# print the JSON string representation of the object
print(RangeWindow20240614.to_json())

# convert the object into a dict
range_window20240614_dict = range_window20240614_instance.to_dict()
# create an instance of RangeWindow20240614 from a dict
range_window20240614_from_dict = RangeWindow20240614.from_dict(range_window20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


