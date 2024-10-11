# openapi_client.OrgsUsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_users_controller_create_organization_user**](OrgsUsersApi.md#organizations_users_controller_create_organization_user) | **POST** /v2/organizations/{orgId}/users | Create a user
[**organizations_users_controller_delete_organization_user**](OrgsUsersApi.md#organizations_users_controller_delete_organization_user) | **DELETE** /v2/organizations/{orgId}/users/{userId} | Delete a user
[**organizations_users_controller_get_organizations_users**](OrgsUsersApi.md#organizations_users_controller_get_organizations_users) | **GET** /v2/organizations/{orgId}/users | Get all users
[**organizations_users_controller_update_organization_user**](OrgsUsersApi.md#organizations_users_controller_update_organization_user) | **PATCH** /v2/organizations/{orgId}/users/{userId} | Update a user


# **organizations_users_controller_create_organization_user**
> GetOrganizationUserOutput organizations_users_controller_create_organization_user(org_id, create_organization_user_input)

Create a user

### Example


```python
import openapi_client
from openapi_client.models.create_organization_user_input import CreateOrganizationUserInput
from openapi_client.models.get_organization_user_output import GetOrganizationUserOutput
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
    api_instance = openapi_client.OrgsUsersApi(api_client)
    org_id = 3.4 # float | 
    create_organization_user_input = openapi_client.CreateOrganizationUserInput() # CreateOrganizationUserInput | 

    try:
        # Create a user
        api_response = api_instance.organizations_users_controller_create_organization_user(org_id, create_organization_user_input)
        print("The response of OrgsUsersApi->organizations_users_controller_create_organization_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsUsersApi->organizations_users_controller_create_organization_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **create_organization_user_input** | [**CreateOrganizationUserInput**](CreateOrganizationUserInput.md)|  | 

### Return type

[**GetOrganizationUserOutput**](GetOrganizationUserOutput.md)

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

# **organizations_users_controller_delete_organization_user**
> GetOrganizationUserOutput organizations_users_controller_delete_organization_user(org_id, user_id)

Delete a user

### Example


```python
import openapi_client
from openapi_client.models.get_organization_user_output import GetOrganizationUserOutput
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
    api_instance = openapi_client.OrgsUsersApi(api_client)
    org_id = 3.4 # float | 
    user_id = 3.4 # float | 

    try:
        # Delete a user
        api_response = api_instance.organizations_users_controller_delete_organization_user(org_id, user_id)
        print("The response of OrgsUsersApi->organizations_users_controller_delete_organization_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsUsersApi->organizations_users_controller_delete_organization_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **user_id** | **float**|  | 

### Return type

[**GetOrganizationUserOutput**](GetOrganizationUserOutput.md)

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

# **organizations_users_controller_get_organizations_users**
> GetOrganizationUsersOutput organizations_users_controller_get_organizations_users(org_id, take=take, skip=skip, emails=emails)

Get all users

### Example


```python
import openapi_client
from openapi_client.models.get_organization_users_output import GetOrganizationUsersOutput
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
    api_instance = openapi_client.OrgsUsersApi(api_client)
    org_id = 3.4 # float | 
    take = 10 # float | The number of items to return (optional)
    skip = 0 # float | The number of items to skip (optional)
    emails = ['emails_example'] # List[str] | The email address or an array of email addresses to filter by (optional)

    try:
        # Get all users
        api_response = api_instance.organizations_users_controller_get_organizations_users(org_id, take=take, skip=skip, emails=emails)
        print("The response of OrgsUsersApi->organizations_users_controller_get_organizations_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsUsersApi->organizations_users_controller_get_organizations_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **take** | **float**| The number of items to return | [optional] 
 **skip** | **float**| The number of items to skip | [optional] 
 **emails** | [**List[str]**](str.md)| The email address or an array of email addresses to filter by | [optional] 

### Return type

[**GetOrganizationUsersOutput**](GetOrganizationUsersOutput.md)

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

# **organizations_users_controller_update_organization_user**
> GetOrganizationUserOutput organizations_users_controller_update_organization_user(org_id, user_id, body)

Update a user

### Example


```python
import openapi_client
from openapi_client.models.get_organization_user_output import GetOrganizationUserOutput
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
    api_instance = openapi_client.OrgsUsersApi(api_client)
    org_id = 3.4 # float | 
    user_id = 3.4 # float | 
    body = None # object | 

    try:
        # Update a user
        api_response = api_instance.organizations_users_controller_update_organization_user(org_id, user_id, body)
        print("The response of OrgsUsersApi->organizations_users_controller_update_organization_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsUsersApi->organizations_users_controller_update_organization_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **user_id** | **float**|  | 
 **body** | **object**|  | 

### Return type

[**GetOrganizationUserOutput**](GetOrganizationUserOutput.md)

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

