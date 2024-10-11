# CreatePhoneCallOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**Data**](Data.md) |  | 

## Example

```python
from openapi_client.models.create_phone_call_output import CreatePhoneCallOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePhoneCallOutput from a JSON string
create_phone_call_output_instance = CreatePhoneCallOutput.from_json(json)
# print the JSON string representation of the object
print(CreatePhoneCallOutput.to_json())

# convert the object into a dict
create_phone_call_output_dict = create_phone_call_output_instance.to_dict()
# create an instance of CreatePhoneCallOutput from a dict
create_phone_call_output_from_dict = CreatePhoneCallOutput.from_dict(create_phone_call_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


