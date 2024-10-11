# UnassignOptionUserOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**AssignOptionUserOutputData**](AssignOptionUserOutputData.md) |  | 

## Example

```python
from openapi_client.models.unassign_option_user_output import UnassignOptionUserOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UnassignOptionUserOutput from a JSON string
unassign_option_user_output_instance = UnassignOptionUserOutput.from_json(json)
# print the JSON string representation of the object
print(UnassignOptionUserOutput.to_json())

# convert the object into a dict
unassign_option_user_output_dict = unassign_option_user_output_instance.to_dict()
# create an instance of UnassignOptionUserOutput from a dict
unassign_option_user_output_from_dict = UnassignOptionUserOutput.from_dict(unassign_option_user_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


