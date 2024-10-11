# GetManagedUserOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**ManagedUserOutput**](ManagedUserOutput.md) |  | 

## Example

```python
from openapi_client.models.get_managed_user_output import GetManagedUserOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedUserOutput from a JSON string
get_managed_user_output_instance = GetManagedUserOutput.from_json(json)
# print the JSON string representation of the object
print(GetManagedUserOutput.to_json())

# convert the object into a dict
get_managed_user_output_dict = get_managed_user_output_instance.to_dict()
# create an instance of GetManagedUserOutput from a dict
get_managed_user_output_from_dict = GetManagedUserOutput.from_dict(get_managed_user_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


