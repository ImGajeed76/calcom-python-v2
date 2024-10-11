# openapi_client.OrgsMembershipsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_memberships_controller_create_membership**](OrgsMembershipsApi.md#organizations_memberships_controller_create_membership) | **POST** /v2/organizations/{orgId}/memberships | Create a membership
[**organizations_memberships_controller_delete_membership**](OrgsMembershipsApi.md#organizations_memberships_controller_delete_membership) | **DELETE** /v2/organizations/{orgId}/memberships/{membershipId} | Delete a membership
[**organizations_memberships_controller_get_all_memberships**](OrgsMembershipsApi.md#organizations_memberships_controller_get_all_memberships) | **GET** /v2/organizations/{orgId}/memberships | Get all memberships
[**organizations_memberships_controller_get_org_membership**](OrgsMembershipsApi.md#organizations_memberships_controller_get_org_membership) | **GET** /v2/organizations/{orgId}/memberships/{membershipId} | Get a membership
[**organizations_memberships_controller_update_membership**](OrgsMembershipsApi.md#organizations_memberships_controller_update_membership) | **PATCH** /v2/organizations/{orgId}/memberships/{membershipId} | Update a membership


# **organizations_memberships_controller_create_membership**
> CreateOrgMembershipOutput organizations_memberships_controller_create_membership(org_id, create_org_membership_dto)

Create a membership

### Example


```python
import openapi_client
from openapi_client.models.create_org_membership_dto import CreateOrgMembershipDto
from openapi_client.models.create_org_membership_output import CreateOrgMembershipOutput
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
    api_instance = openapi_client.OrgsMembershipsApi(api_client)
    org_id = 3.4 # float | 
    create_org_membership_dto = openapi_client.CreateOrgMembershipDto() # CreateOrgMembershipDto | 

    try:
        # Create a membership
        api_response = api_instance.organizations_memberships_controller_create_membership(org_id, create_org_membership_dto)
        print("The response of OrgsMembershipsApi->organizations_memberships_controller_create_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsMembershipsApi->organizations_memberships_controller_create_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **create_org_membership_dto** | [**CreateOrgMembershipDto**](CreateOrgMembershipDto.md)|  | 

### Return type

[**CreateOrgMembershipOutput**](CreateOrgMembershipOutput.md)

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

# **organizations_memberships_controller_delete_membership**
> DeleteOrgMembership organizations_memberships_controller_delete_membership(org_id, membership_id)

Delete a membership

### Example


```python
import openapi_client
from openapi_client.models.delete_org_membership import DeleteOrgMembership
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
    api_instance = openapi_client.OrgsMembershipsApi(api_client)
    org_id = 3.4 # float | 
    membership_id = 3.4 # float | 

    try:
        # Delete a membership
        api_response = api_instance.organizations_memberships_controller_delete_membership(org_id, membership_id)
        print("The response of OrgsMembershipsApi->organizations_memberships_controller_delete_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsMembershipsApi->organizations_memberships_controller_delete_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **membership_id** | **float**|  | 

### Return type

[**DeleteOrgMembership**](DeleteOrgMembership.md)

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

# **organizations_memberships_controller_get_all_memberships**
> GetAllOrgMemberships organizations_memberships_controller_get_all_memberships(org_id, take=take, skip=skip)

Get all memberships

### Example


```python
import openapi_client
from openapi_client.models.get_all_org_memberships import GetAllOrgMemberships
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
    api_instance = openapi_client.OrgsMembershipsApi(api_client)
    org_id = 3.4 # float | 
    take = 10 # float | The number of items to return (optional)
    skip = 0 # float | The number of items to skip (optional)

    try:
        # Get all memberships
        api_response = api_instance.organizations_memberships_controller_get_all_memberships(org_id, take=take, skip=skip)
        print("The response of OrgsMembershipsApi->organizations_memberships_controller_get_all_memberships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsMembershipsApi->organizations_memberships_controller_get_all_memberships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **take** | **float**| The number of items to return | [optional] 
 **skip** | **float**| The number of items to skip | [optional] 

### Return type

[**GetAllOrgMemberships**](GetAllOrgMemberships.md)

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

# **organizations_memberships_controller_get_org_membership**
> GetOrgMembership organizations_memberships_controller_get_org_membership(org_id, membership_id)

Get a membership

### Example


```python
import openapi_client
from openapi_client.models.get_org_membership import GetOrgMembership
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
    api_instance = openapi_client.OrgsMembershipsApi(api_client)
    org_id = 3.4 # float | 
    membership_id = 3.4 # float | 

    try:
        # Get a membership
        api_response = api_instance.organizations_memberships_controller_get_org_membership(org_id, membership_id)
        print("The response of OrgsMembershipsApi->organizations_memberships_controller_get_org_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsMembershipsApi->organizations_memberships_controller_get_org_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **membership_id** | **float**|  | 

### Return type

[**GetOrgMembership**](GetOrgMembership.md)

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

# **organizations_memberships_controller_update_membership**
> UpdateOrgMembership organizations_memberships_controller_update_membership(org_id, membership_id, update_org_membership_dto)

Update a membership

### Example


```python
import openapi_client
from openapi_client.models.update_org_membership import UpdateOrgMembership
from openapi_client.models.update_org_membership_dto import UpdateOrgMembershipDto
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
    api_instance = openapi_client.OrgsMembershipsApi(api_client)
    org_id = 3.4 # float | 
    membership_id = 3.4 # float | 
    update_org_membership_dto = openapi_client.UpdateOrgMembershipDto() # UpdateOrgMembershipDto | 

    try:
        # Update a membership
        api_response = api_instance.organizations_memberships_controller_update_membership(org_id, membership_id, update_org_membership_dto)
        print("The response of OrgsMembershipsApi->organizations_memberships_controller_update_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsMembershipsApi->organizations_memberships_controller_update_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **membership_id** | **float**|  | 
 **update_org_membership_dto** | [**UpdateOrgMembershipDto**](UpdateOrgMembershipDto.md)|  | 

### Return type

[**UpdateOrgMembership**](UpdateOrgMembership.md)

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

