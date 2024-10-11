# BusinessDaysWindow20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Whether the window should be business days, calendar days or a range of dates | 
**value** | **float** | How many business day into the future can this event be booked | 
**rolling** | **bool** | If true, the window will be rolling aka from the moment that someone is trying to book this event. Otherwise it will be specified amount of days from the current date. | [optional] 

## Example

```python
from openapi_client.models.business_days_window20240614 import BusinessDaysWindow20240614

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDaysWindow20240614 from a JSON string
business_days_window20240614_instance = BusinessDaysWindow20240614.from_json(json)
# print the JSON string representation of the object
print(BusinessDaysWindow20240614.to_json())

# convert the object into a dict
business_days_window20240614_dict = business_days_window20240614_instance.to_dict()
# create an instance of BusinessDaysWindow20240614 from a dict
business_days_window20240614_from_dict = BusinessDaysWindow20240614.from_dict(business_days_window20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


