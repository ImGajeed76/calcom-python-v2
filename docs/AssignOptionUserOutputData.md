# AssignOptionUserOutputData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the option assigned to the user | 
**member_id** | **float** | The ID form the org membership for the user | 
**attribute_option_id** | **str** | The value of the option | 

## Example

```python
from openapi_client.models.assign_option_user_output_data import AssignOptionUserOutputData

# TODO update the JSON string below
json = "{}"
# create an instance of AssignOptionUserOutputData from a JSON string
assign_option_user_output_data_instance = AssignOptionUserOutputData.from_json(json)
# print the JSON string representation of the object
print(AssignOptionUserOutputData.to_json())

# convert the object into a dict
assign_option_user_output_data_dict = assign_option_user_output_data_instance.to_dict()
# create an instance of AssignOptionUserOutputData from a dict
assign_option_user_output_data_from_dict = AssignOptionUserOutputData.from_dict(assign_option_user_output_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


