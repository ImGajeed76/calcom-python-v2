# CreateOrgMembershipDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [default to 'MEMBER']
**user_id** | **float** |  | 
**accepted** | **bool** |  | [optional] [default to False]
**disable_impersonation** | **bool** |  | [optional] [default to False]

## Example

```python
from openapi_client.models.create_org_membership_dto import CreateOrgMembershipDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrgMembershipDto from a JSON string
create_org_membership_dto_instance = CreateOrgMembershipDto.from_json(json)
# print the JSON string representation of the object
print(CreateOrgMembershipDto.to_json())

# convert the object into a dict
create_org_membership_dto_dict = create_org_membership_dto_instance.to_dict()
# create an instance of CreateOrgMembershipDto from a dict
create_org_membership_dto_from_dict = CreateOrgMembershipDto.from_dict(create_org_membership_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


