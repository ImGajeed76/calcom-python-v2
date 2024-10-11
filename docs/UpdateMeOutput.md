# UpdateMeOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**MeOutput**](MeOutput.md) |  | 

## Example

```python
from openapi_client.models.update_me_output import UpdateMeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMeOutput from a JSON string
update_me_output_instance = UpdateMeOutput.from_json(json)
# print the JSON string representation of the object
print(UpdateMeOutput.to_json())

# convert the object into a dict
update_me_output_dict = update_me_output_instance.to_dict()
# create an instance of UpdateMeOutput from a dict
update_me_output_from_dict = UpdateMeOutput.from_dict(update_me_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


