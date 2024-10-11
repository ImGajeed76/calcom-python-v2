# GetManagedUsersOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[ManagedUserOutput]**](ManagedUserOutput.md) |  | 

## Example

```python
from openapi_client.models.get_managed_users_output import GetManagedUsersOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedUsersOutput from a JSON string
get_managed_users_output_instance = GetManagedUsersOutput.from_json(json)
# print the JSON string representation of the object
print(GetManagedUsersOutput.to_json())

# convert the object into a dict
get_managed_users_output_dict = get_managed_users_output_instance.to_dict()
# create an instance of GetManagedUsersOutput from a dict
get_managed_users_output_from_dict = GetManagedUsersOutput.from_dict(get_managed_users_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


