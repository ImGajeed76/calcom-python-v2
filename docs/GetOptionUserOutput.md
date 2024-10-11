# GetOptionUserOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[GetOptionUserOutputData]**](GetOptionUserOutputData.md) |  | 

## Example

```python
from openapi_client.models.get_option_user_output import GetOptionUserOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetOptionUserOutput from a JSON string
get_option_user_output_instance = GetOptionUserOutput.from_json(json)
# print the JSON string representation of the object
print(GetOptionUserOutput.to_json())

# convert the object into a dict
get_option_user_output_dict = get_option_user_output_instance.to_dict()
# create an instance of GetOptionUserOutput from a dict
get_option_user_output_from_dict = GetOptionUserOutput.from_dict(get_option_user_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


