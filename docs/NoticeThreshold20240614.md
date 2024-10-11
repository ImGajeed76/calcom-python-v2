# NoticeThreshold20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | The unit of time for the notice threshold (e.g., minutes, hours) | 
**count** | **float** | The time value for the notice threshold | 

## Example

```python
from openapi_client.models.notice_threshold20240614 import NoticeThreshold20240614

# TODO update the JSON string below
json = "{}"
# create an instance of NoticeThreshold20240614 from a JSON string
notice_threshold20240614_instance = NoticeThreshold20240614.from_json(json)
# print the JSON string representation of the object
print(NoticeThreshold20240614.to_json())

# convert the object into a dict
notice_threshold20240614_dict = notice_threshold20240614_instance.to_dict()
# create an instance of NoticeThreshold20240614 from a dict
notice_threshold20240614_from_dict = NoticeThreshold20240614.from_dict(notice_threshold20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


