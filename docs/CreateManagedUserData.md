# CreateManagedUserData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**ManagedUserOutput**](ManagedUserOutput.md) |  | 
**access_token** | **str** |  | 
**refresh_token** | **str** |  | 
**access_token_expires_at** | **float** |  | 

## Example

```python
from openapi_client.models.create_managed_user_data import CreateManagedUserData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateManagedUserData from a JSON string
create_managed_user_data_instance = CreateManagedUserData.from_json(json)
# print the JSON string representation of the object
print(CreateManagedUserData.to_json())

# convert the object into a dict
create_managed_user_data_dict = create_managed_user_data_instance.to_dict()
# create an instance of CreateManagedUserData from a dict
create_managed_user_data_from_dict = CreateManagedUserData.from_dict(create_managed_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


