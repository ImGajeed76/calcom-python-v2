# UpdateAttributeOptionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**OptionOutput**](OptionOutput.md) |  | 

## Example

```python
from openapi_client.models.update_attribute_option_output import UpdateAttributeOptionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAttributeOptionOutput from a JSON string
update_attribute_option_output_instance = UpdateAttributeOptionOutput.from_json(json)
# print the JSON string representation of the object
print(UpdateAttributeOptionOutput.to_json())

# convert the object into a dict
update_attribute_option_output_dict = update_attribute_option_output_instance.to_dict()
# create an instance of UpdateAttributeOptionOutput from a dict
update_attribute_option_output_from_dict = UpdateAttributeOptionOutput.from_dict(update_attribute_option_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


