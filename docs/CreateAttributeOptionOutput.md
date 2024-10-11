# CreateAttributeOptionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**OptionOutput**](OptionOutput.md) |  | 

## Example

```python
from openapi_client.models.create_attribute_option_output import CreateAttributeOptionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAttributeOptionOutput from a JSON string
create_attribute_option_output_instance = CreateAttributeOptionOutput.from_json(json)
# print the JSON string representation of the object
print(CreateAttributeOptionOutput.to_json())

# convert the object into a dict
create_attribute_option_output_dict = create_attribute_option_output_instance.to_dict()
# create an instance of CreateAttributeOptionOutput from a dict
create_attribute_option_output_from_dict = CreateAttributeOptionOutput.from_dict(create_attribute_option_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


