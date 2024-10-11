# ManagedUserOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**email** | **str** |  | 
**username** | **str** |  | 
**name** | **str** |  | 
**time_zone** | **str** |  | 
**week_start** | **str** |  | 
**created_date** | **str** |  | 
**time_format** | **float** |  | 
**default_schedule_id** | **float** |  | 
**locale** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.managed_user_output import ManagedUserOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedUserOutput from a JSON string
managed_user_output_instance = ManagedUserOutput.from_json(json)
# print the JSON string representation of the object
print(ManagedUserOutput.to_json())

# convert the object into a dict
managed_user_output_dict = managed_user_output_instance.to_dict()
# create an instance of ManagedUserOutput from a dict
managed_user_output_from_dict = ManagedUserOutput.from_dict(managed_user_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


