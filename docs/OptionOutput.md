# OptionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the option | 
**attribute_id** | **str** | The ID of the attribute | 
**value** | **str** | The value of the option | 
**slug** | **str** | The slug of the option | 

## Example

```python
from openapi_client.models.option_output import OptionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of OptionOutput from a JSON string
option_output_instance = OptionOutput.from_json(json)
# print the JSON string representation of the object
print(OptionOutput.to_json())

# convert the object into a dict
option_output_dict = option_output_instance.to_dict()
# create an instance of OptionOutput from a dict
option_output_from_dict = OptionOutput.from_dict(option_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


