# MeOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**username** | **str** |  | 
**email** | **str** |  | 
**time_format** | **float** |  | 
**default_schedule_id** | **float** |  | 
**week_start** | **str** |  | 
**time_zone** | **str** |  | 
**organization_id** | **float** |  | 
**organization** | [**MeOrgOutput**](MeOrgOutput.md) |  | [optional] 

## Example

```python
from openapi_client.models.me_output import MeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of MeOutput from a JSON string
me_output_instance = MeOutput.from_json(json)
# print the JSON string representation of the object
print(MeOutput.to_json())

# convert the object into a dict
me_output_dict = me_output_instance.to_dict()
# create an instance of MeOutput from a dict
me_output_from_dict = MeOutput.from_dict(me_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


