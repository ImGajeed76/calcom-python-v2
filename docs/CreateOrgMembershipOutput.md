# CreateOrgMembershipOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | [**OrgMembershipOutputDto**](OrgMembershipOutputDto.md) |  | 

## Example

```python
from openapi_client.models.create_org_membership_output import CreateOrgMembershipOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrgMembershipOutput from a JSON string
create_org_membership_output_instance = CreateOrgMembershipOutput.from_json(json)
# print the JSON string representation of the object
print(CreateOrgMembershipOutput.to_json())

# convert the object into a dict
create_org_membership_output_dict = create_org_membership_output_instance.to_dict()
# create an instance of CreateOrgMembershipOutput from a dict
create_org_membership_output_from_dict = CreateOrgMembershipOutput.from_dict(create_org_membership_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


