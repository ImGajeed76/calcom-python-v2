# BaseConfirmationPolicy20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The policy that determines when confirmation is required | 
**notice_threshold** | [**NoticeThreshold20240614**](NoticeThreshold20240614.md) | The notice threshold required before confirmation is needed. Required when type is &#39;time&#39;. | [optional] 

## Example

```python
from openapi_client.models.base_confirmation_policy20240614 import BaseConfirmationPolicy20240614

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConfirmationPolicy20240614 from a JSON string
base_confirmation_policy20240614_instance = BaseConfirmationPolicy20240614.from_json(json)
# print the JSON string representation of the object
print(BaseConfirmationPolicy20240614.to_json())

# convert the object into a dict
base_confirmation_policy20240614_dict = base_confirmation_policy20240614_instance.to_dict()
# create an instance of BaseConfirmationPolicy20240614 from a dict
base_confirmation_policy20240614_from_dict = BaseConfirmationPolicy20240614.from_dict(base_confirmation_policy20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


