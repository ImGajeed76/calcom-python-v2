# DeleteAttributeOptionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**OptionOutput**](OptionOutput.md) |  | 

## Example

```python
from openapi_client.models.delete_attribute_option_output import DeleteAttributeOptionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAttributeOptionOutput from a JSON string
delete_attribute_option_output_instance = DeleteAttributeOptionOutput.from_json(json)
# print the JSON string representation of the object
print(DeleteAttributeOptionOutput.to_json())

# convert the object into a dict
delete_attribute_option_output_dict = delete_attribute_option_output_instance.to_dict()
# create an instance of DeleteAttributeOptionOutput from a dict
delete_attribute_option_output_from_dict = DeleteAttributeOptionOutput.from_dict(delete_attribute_option_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


