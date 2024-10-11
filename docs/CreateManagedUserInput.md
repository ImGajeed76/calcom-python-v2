# CreateManagedUserInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**name** | **str** | Managed user&#39;s name is used in emails | 
**time_format** | **float** | Must be a number 12 or 24 | [optional] 
**week_start** | **str** |  | [optional] 
**time_zone** | **str** | Timezone is used to create user&#39;s default schedule from Monday to Friday from 9AM to 5PM. If it is not passed then user does not have       a default schedule and it must be created manually via the /schedules endpoint. Until the schedule is created, the user can&#39;t access availability atom to set his / her availability nor booked. | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_managed_user_input import CreateManagedUserInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateManagedUserInput from a JSON string
create_managed_user_input_instance = CreateManagedUserInput.from_json(json)
# print the JSON string representation of the object
print(CreateManagedUserInput.to_json())

# convert the object into a dict
create_managed_user_input_dict = create_managed_user_input_instance.to_dict()
# create an instance of CreateManagedUserInput from a dict
create_managed_user_input_from_dict = CreateManagedUserInput.from_dict(create_managed_user_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


