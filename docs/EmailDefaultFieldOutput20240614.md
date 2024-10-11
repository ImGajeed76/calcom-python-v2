# EmailDefaultFieldOutput20240614


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **object** | This property is always true because it&#39;s a default field | 
**slug** | **str** |  | [default to 'email']
**type** | **str** |  | [default to 'email']
**required** | **bool** |  | 

## Example

```python
from openapi_client.models.email_default_field_output20240614 import EmailDefaultFieldOutput20240614

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDefaultFieldOutput20240614 from a JSON string
email_default_field_output20240614_instance = EmailDefaultFieldOutput20240614.from_json(json)
# print the JSON string representation of the object
print(EmailDefaultFieldOutput20240614.to_json())

# convert the object into a dict
email_default_field_output20240614_dict = email_default_field_output20240614_instance.to_dict()
# create an instance of EmailDefaultFieldOutput20240614 from a dict
email_default_field_output20240614_from_dict = EmailDefaultFieldOutput20240614.from_dict(email_default_field_output20240614_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


