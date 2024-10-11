# UpdateManagedUserInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_format** | **float** | Must be 12 or 24 | [optional] 
**week_start** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**default_schedule_id** | **float** |  | [optional] 
**time_zone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_managed_user_input import UpdateManagedUserInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateManagedUserInput from a JSON string
update_managed_user_input_instance = UpdateManagedUserInput.from_json(json)
# print the JSON string representation of the object
print(UpdateManagedUserInput.to_json())

# convert the object into a dict
update_managed_user_input_dict = update_managed_user_input_instance.to_dict()
# create an instance of UpdateManagedUserInput from a dict
update_managed_user_input_from_dict = UpdateManagedUserInput.from_dict(update_managed_user_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


