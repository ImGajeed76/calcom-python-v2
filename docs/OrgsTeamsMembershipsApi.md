# openapi_client.OrgsTeamsMembershipsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_teams_memberships_controller_create_org_team_membership**](OrgsTeamsMembershipsApi.md#organizations_teams_memberships_controller_create_org_team_membership) | **POST** /v2/organizations/{orgId}/teams/{teamId}/memberships | Create a membership
[**organizations_teams_memberships_controller_delete_org_team_membership**](OrgsTeamsMembershipsApi.md#organizations_teams_memberships_controller_delete_org_team_membership) | **DELETE** /v2/organizations/{orgId}/teams/{teamId}/memberships/{membershipId} | Delete a membership
[**organizations_teams_memberships_controller_get_all_org_team_memberships**](OrgsTeamsMembershipsApi.md#organizations_teams_memberships_controller_get_all_org_team_memberships) | **GET** /v2/organizations/{orgId}/teams/{teamId}/memberships | Get all memberships
[**organizations_teams_memberships_controller_get_org_team_membership**](OrgsTeamsMembershipsApi.md#organizations_teams_memberships_controller_get_org_team_membership) | **GET** /v2/organizations/{orgId}/teams/{teamId}/memberships/{membershipId} | Get a membership
[**organizations_teams_memberships_controller_update_org_team_membership**](OrgsTeamsMembershipsApi.md#organizations_teams_memberships_controller_update_org_team_membership) | **PATCH** /v2/organizations/{orgId}/teams/{teamId}/memberships/{membershipId} | Update a membership


# **organizations_teams_memberships_controller_create_org_team_membership**
> OrgTeamMembershipOutputResponseDto organizations_teams_memberships_controller_create_org_team_membership(org_id, team_id, create_org_team_membership_dto)

Create a membership

### Example


```python
import openapi_client
from openapi_client.models.create_org_team_membership_dto import CreateOrgTeamMembershipDto
from openapi_client.models.org_team_membership_output_response_dto import OrgTeamMembershipOutputResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OrgsTeamsMembershipsApi(api_client)
    org_id = 3.4 # float | 
    team_id = 3.4 # float | 
    create_org_team_membership_dto = openapi_client.CreateOrgTeamMembershipDto() # CreateOrgTeamMembershipDto | 

    try:
        # Create a membership
        api_response = api_instance.organizations_teams_memberships_controller_create_org_team_membership(org_id, team_id, create_org_team_membership_dto)
        print("The response of OrgsTeamsMembershipsApi->organizations_teams_memberships_controller_create_org_team_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsTeamsMembershipsApi->organizations_teams_memberships_controller_create_org_team_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **team_id** | **float**|  | 
 **create_org_team_membership_dto** | [**CreateOrgTeamMembershipDto**](CreateOrgTeamMembershipDto.md)|  | 

### Return type

[**OrgTeamMembershipOutputResponseDto**](OrgTeamMembershipOutputResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_teams_memberships_controller_delete_org_team_membership**
> OrgTeamMembershipOutputResponseDto organizations_teams_memberships_controller_delete_org_team_membership(org_id, team_id, membership_id)

Delete a membership

### Example


```python
import openapi_client
from openapi_client.models.org_team_membership_output_response_dto import OrgTeamMembershipOutputResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OrgsTeamsMembershipsApi(api_client)
    org_id = 3.4 # float | 
    team_id = 3.4 # float | 
    membership_id = 3.4 # float | 

    try:
        # Delete a membership
        api_response = api_instance.organizations_teams_memberships_controller_delete_org_team_membership(org_id, team_id, membership_id)
        print("The response of OrgsTeamsMembershipsApi->organizations_teams_memberships_controller_delete_org_team_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsTeamsMembershipsApi->organizations_teams_memberships_controller_delete_org_team_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **team_id** | **float**|  | 
 **membership_id** | **float**|  | 

### Return type

[**OrgTeamMembershipOutputResponseDto**](OrgTeamMembershipOutputResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_teams_memberships_controller_get_all_org_team_memberships**
> OrgTeamMembershipsOutputResponseDto organizations_teams_memberships_controller_get_all_org_team_memberships(org_id, team_id, take=take, skip=skip)

Get all memberships

### Example


```python
import openapi_client
from openapi_client.models.org_team_memberships_output_response_dto import OrgTeamMembershipsOutputResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OrgsTeamsMembershipsApi(api_client)
    org_id = 3.4 # float | 
    team_id = 3.4 # float | 
    take = 10 # float | The number of items to return (optional)
    skip = 0 # float | The number of items to skip (optional)

    try:
        # Get all memberships
        api_response = api_instance.organizations_teams_memberships_controller_get_all_org_team_memberships(org_id, team_id, take=take, skip=skip)
        print("The response of OrgsTeamsMembershipsApi->organizations_teams_memberships_controller_get_all_org_team_memberships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsTeamsMembershipsApi->organizations_teams_memberships_controller_get_all_org_team_memberships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **team_id** | **float**|  | 
 **take** | **float**| The number of items to return | [optional] 
 **skip** | **float**| The number of items to skip | [optional] 

### Return type

[**OrgTeamMembershipsOutputResponseDto**](OrgTeamMembershipsOutputResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_teams_memberships_controller_get_org_team_membership**
> OrgTeamMembershipOutputResponseDto organizations_teams_memberships_controller_get_org_team_membership(org_id, team_id, membership_id)

Get a membership

### Example


```python
import openapi_client
from openapi_client.models.org_team_membership_output_response_dto import OrgTeamMembershipOutputResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OrgsTeamsMembershipsApi(api_client)
    org_id = 3.4 # float | 
    team_id = 3.4 # float | 
    membership_id = 3.4 # float | 

    try:
        # Get a membership
        api_response = api_instance.organizations_teams_memberships_controller_get_org_team_membership(org_id, team_id, membership_id)
        print("The response of OrgsTeamsMembershipsApi->organizations_teams_memberships_controller_get_org_team_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsTeamsMembershipsApi->organizations_teams_memberships_controller_get_org_team_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **team_id** | **float**|  | 
 **membership_id** | **float**|  | 

### Return type

[**OrgTeamMembershipOutputResponseDto**](OrgTeamMembershipOutputResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_teams_memberships_controller_update_org_team_membership**
> OrgTeamMembershipOutputResponseDto organizations_teams_memberships_controller_update_org_team_membership(org_id, team_id, membership_id, update_org_team_membership_dto)

Update a membership

### Example


```python
import openapi_client
from openapi_client.models.org_team_membership_output_response_dto import OrgTeamMembershipOutputResponseDto
from openapi_client.models.update_org_team_membership_dto import UpdateOrgTeamMembershipDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OrgsTeamsMembershipsApi(api_client)
    org_id = 3.4 # float | 
    team_id = 3.4 # float | 
    membership_id = 3.4 # float | 
    update_org_team_membership_dto = openapi_client.UpdateOrgTeamMembershipDto() # UpdateOrgTeamMembershipDto | 

    try:
        # Update a membership
        api_response = api_instance.organizations_teams_memberships_controller_update_org_team_membership(org_id, team_id, membership_id, update_org_team_membership_dto)
        print("The response of OrgsTeamsMembershipsApi->organizations_teams_memberships_controller_update_org_team_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsTeamsMembershipsApi->organizations_teams_memberships_controller_update_org_team_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **team_id** | **float**|  | 
 **membership_id** | **float**|  | 
 **update_org_team_membership_dto** | [**UpdateOrgTeamMembershipDto**](UpdateOrgTeamMembershipDto.md)|  | 

### Return type

[**OrgTeamMembershipOutputResponseDto**](OrgTeamMembershipOutputResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

