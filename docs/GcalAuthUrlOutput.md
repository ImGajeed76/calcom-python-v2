# GcalAuthUrlOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**AuthUrlData**](AuthUrlData.md) |  | 

## Example

```python
from openapi_client.models.gcal_auth_url_output import GcalAuthUrlOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GcalAuthUrlOutput from a JSON string
gcal_auth_url_output_instance = GcalAuthUrlOutput.from_json(json)
# print the JSON string representation of the object
print(GcalAuthUrlOutput.to_json())

# convert the object into a dict
gcal_auth_url_output_dict = gcal_auth_url_output_instance.to_dict()
# create an instance of GcalAuthUrlOutput from a dict
gcal_auth_url_output_from_dict = GcalAuthUrlOutput.from_dict(gcal_auth_url_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


