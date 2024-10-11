# CreateManagedUserOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**CreateManagedUserData**](CreateManagedUserData.md) |  | 

## Example

```python
from openapi_client.models.create_managed_user_output import CreateManagedUserOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateManagedUserOutput from a JSON string
create_managed_user_output_instance = CreateManagedUserOutput.from_json(json)
# print the JSON string representation of the object
print(CreateManagedUserOutput.to_json())

# convert the object into a dict
create_managed_user_output_dict = create_managed_user_output_instance.to_dict()
# create an instance of CreateManagedUserOutput from a dict
create_managed_user_output_from_dict = CreateManagedUserOutput.from_dict(create_managed_user_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


