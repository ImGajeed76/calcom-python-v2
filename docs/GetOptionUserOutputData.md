# GetOptionUserOutputData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the option assigned to the user | 
**attribute_id** | **str** | The ID of the attribute | 
**value** | **str** | The value of the option | 
**slug** | **str** | The slug of the option | 

## Example

```python
from openapi_client.models.get_option_user_output_data import GetOptionUserOutputData

# TODO update the JSON string below
json = "{}"
# create an instance of GetOptionUserOutputData from a JSON string
get_option_user_output_data_instance = GetOptionUserOutputData.from_json(json)
# print the JSON string representation of the object
print(GetOptionUserOutputData.to_json())

# convert the object into a dict
get_option_user_output_data_dict = get_option_user_output_data_instance.to_dict()
# create an instance of GetOptionUserOutputData from a dict
get_option_user_output_data_from_dict = GetOptionUserOutputData.from_dict(get_option_user_output_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


