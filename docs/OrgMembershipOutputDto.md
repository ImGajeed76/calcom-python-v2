# OrgMembershipOutputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**id** | **float** |  | 
**user_id** | **float** |  | 
**team_id** | **float** |  | 
**accepted** | **bool** |  | 
**disable_impersonation** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.org_membership_output_dto import OrgMembershipOutputDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrgMembershipOutputDto from a JSON string
org_membership_output_dto_instance = OrgMembershipOutputDto.from_json(json)
# print the JSON string representation of the object
print(OrgMembershipOutputDto.to_json())

# convert the object into a dict
org_membership_output_dto_dict = org_membership_output_dto_instance.to_dict()
# create an instance of OrgMembershipOutputDto from a dict
org_membership_output_dto_from_dict = OrgMembershipOutputDto.from_dict(org_membership_output_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


