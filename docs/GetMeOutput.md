# GetMeOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**MeOutput**](MeOutput.md) |  | 

## Example

```python
from openapi_client.models.get_me_output import GetMeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetMeOutput from a JSON string
get_me_output_instance = GetMeOutput.from_json(json)
# print the JSON string representation of the object
print(GetMeOutput.to_json())

# convert the object into a dict
get_me_output_dict = get_me_output_instance.to_dict()
# create an instance of GetMeOutput from a dict
get_me_output_from_dict = GetMeOutput.from_dict(get_me_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


