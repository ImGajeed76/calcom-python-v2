# GetAllAttributeOptionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**List[OptionOutput]**](OptionOutput.md) |  | 

## Example

```python
from openapi_client.models.get_all_attribute_option_output import GetAllAttributeOptionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllAttributeOptionOutput from a JSON string
get_all_attribute_option_output_instance = GetAllAttributeOptionOutput.from_json(json)
# print the JSON string representation of the object
print(GetAllAttributeOptionOutput.to_json())

# convert the object into a dict
get_all_attribute_option_output_dict = get_all_attribute_option_output_instance.to_dict()
# create an instance of GetAllAttributeOptionOutput from a dict
get_all_attribute_option_output_from_dict = GetAllAttributeOptionOutput.from_dict(get_all_attribute_option_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


