# GetSingleAttributeOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**Attribute**](Attribute.md) |  | 

## Example

```python
from openapi_client.models.get_single_attribute_output import GetSingleAttributeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetSingleAttributeOutput from a JSON string
get_single_attribute_output_instance = GetSingleAttributeOutput.from_json(json)
# print the JSON string representation of the object
print(GetSingleAttributeOutput.to_json())

# convert the object into a dict
get_single_attribute_output_dict = get_single_attribute_output_instance.to_dict()
# create an instance of GetSingleAttributeOutput from a dict
get_single_attribute_output_from_dict = GetSingleAttributeOutput.from_dict(get_single_attribute_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


