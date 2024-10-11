# openapi_client.PlatformManagedUsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_auth_client_users_controller_create_user**](PlatformManagedUsersApi.md#o_auth_client_users_controller_create_user) | **POST** /v2/oauth-clients/{clientId}/users | Create a managed user
[**o_auth_client_users_controller_delete_user**](PlatformManagedUsersApi.md#o_auth_client_users_controller_delete_user) | **DELETE** /v2/oauth-clients/{clientId}/users/{userId} | Delete a managed user
[**o_auth_client_users_controller_force_refresh**](PlatformManagedUsersApi.md#o_auth_client_users_controller_force_refresh) | **POST** /v2/oauth-clients/{clientId}/users/{userId}/force-refresh | Force refresh tokens
[**o_auth_client_users_controller_get_managed_users**](PlatformManagedUsersApi.md#o_auth_client_users_controller_get_managed_users) | **GET** /v2/oauth-clients/{clientId}/users | Get all managed users
[**o_auth_client_users_controller_get_user_by_id**](PlatformManagedUsersApi.md#o_auth_client_users_controller_get_user_by_id) | **GET** /v2/oauth-clients/{clientId}/users/{userId} | Get a managed user
[**o_auth_client_users_controller_update_user**](PlatformManagedUsersApi.md#o_auth_client_users_controller_update_user) | **PATCH** /v2/oauth-clients/{clientId}/users/{userId} | Update a managed user


# **o_auth_client_users_controller_create_user**
> CreateManagedUserOutput o_auth_client_users_controller_create_user(client_id, create_managed_user_input)

Create a managed user

### Example


```python
import openapi_client
from openapi_client.models.create_managed_user_input import CreateManagedUserInput
from openapi_client.models.create_managed_user_output import CreateManagedUserOutput
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
    api_instance = openapi_client.PlatformManagedUsersApi(api_client)
    client_id = 'client_id_example' # str | 
    create_managed_user_input = openapi_client.CreateManagedUserInput() # CreateManagedUserInput | 

    try:
        # Create a managed user
        api_response = api_instance.o_auth_client_users_controller_create_user(client_id, create_managed_user_input)
        print("The response of PlatformManagedUsersApi->o_auth_client_users_controller_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformManagedUsersApi->o_auth_client_users_controller_create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **create_managed_user_input** | [**CreateManagedUserInput**](CreateManagedUserInput.md)|  | 

### Return type

[**CreateManagedUserOutput**](CreateManagedUserOutput.md)

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

# **o_auth_client_users_controller_delete_user**
> GetManagedUserOutput o_auth_client_users_controller_delete_user(client_id, user_id)

Delete a managed user

### Example


```python
import openapi_client
from openapi_client.models.get_managed_user_output import GetManagedUserOutput
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
    api_instance = openapi_client.PlatformManagedUsersApi(api_client)
    client_id = 'client_id_example' # str | 
    user_id = 3.4 # float | 

    try:
        # Delete a managed user
        api_response = api_instance.o_auth_client_users_controller_delete_user(client_id, user_id)
        print("The response of PlatformManagedUsersApi->o_auth_client_users_controller_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformManagedUsersApi->o_auth_client_users_controller_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **user_id** | **float**|  | 

### Return type

[**GetManagedUserOutput**](GetManagedUserOutput.md)

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

# **o_auth_client_users_controller_force_refresh**
> KeysResponseDto o_auth_client_users_controller_force_refresh(user_id, client_id)

Force refresh tokens

### Example


```python
import openapi_client
from openapi_client.models.keys_response_dto import KeysResponseDto
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
    api_instance = openapi_client.PlatformManagedUsersApi(api_client)
    user_id = 3.4 # float | 
    client_id = 'client_id_example' # str | 

    try:
        # Force refresh tokens
        api_response = api_instance.o_auth_client_users_controller_force_refresh(user_id, client_id)
        print("The response of PlatformManagedUsersApi->o_auth_client_users_controller_force_refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformManagedUsersApi->o_auth_client_users_controller_force_refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **client_id** | **str**|  | 

### Return type

[**KeysResponseDto**](KeysResponseDto.md)

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

# **o_auth_client_users_controller_get_managed_users**
> GetManagedUsersOutput o_auth_client_users_controller_get_managed_users(client_id, limit=limit)

Get all managed users

### Example


```python
import openapi_client
from openapi_client.models.get_managed_users_output import GetManagedUsersOutput
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
    api_instance = openapi_client.PlatformManagedUsersApi(api_client)
    client_id = 'client_id_example' # str | 
    limit = 10 # float | The number of items to return (optional)

    try:
        # Get all managed users
        api_response = api_instance.o_auth_client_users_controller_get_managed_users(client_id, limit=limit)
        print("The response of PlatformManagedUsersApi->o_auth_client_users_controller_get_managed_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformManagedUsersApi->o_auth_client_users_controller_get_managed_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **limit** | **float**| The number of items to return | [optional] 

### Return type

[**GetManagedUsersOutput**](GetManagedUsersOutput.md)

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

# **o_auth_client_users_controller_get_user_by_id**
> GetManagedUserOutput o_auth_client_users_controller_get_user_by_id(client_id, user_id)

Get a managed user

### Example


```python
import openapi_client
from openapi_client.models.get_managed_user_output import GetManagedUserOutput
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
    api_instance = openapi_client.PlatformManagedUsersApi(api_client)
    client_id = 'client_id_example' # str | 
    user_id = 3.4 # float | 

    try:
        # Get a managed user
        api_response = api_instance.o_auth_client_users_controller_get_user_by_id(client_id, user_id)
        print("The response of PlatformManagedUsersApi->o_auth_client_users_controller_get_user_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformManagedUsersApi->o_auth_client_users_controller_get_user_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **user_id** | **float**|  | 

### Return type

[**GetManagedUserOutput**](GetManagedUserOutput.md)

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

# **o_auth_client_users_controller_update_user**
> GetManagedUserOutput o_auth_client_users_controller_update_user(client_id, user_id, update_managed_user_input)

Update a managed user

### Example


```python
import openapi_client
from openapi_client.models.get_managed_user_output import GetManagedUserOutput
from openapi_client.models.update_managed_user_input import UpdateManagedUserInput
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
    api_instance = openapi_client.PlatformManagedUsersApi(api_client)
    client_id = 'client_id_example' # str | 
    user_id = 3.4 # float | 
    update_managed_user_input = openapi_client.UpdateManagedUserInput() # UpdateManagedUserInput | 

    try:
        # Update a managed user
        api_response = api_instance.o_auth_client_users_controller_update_user(client_id, user_id, update_managed_user_input)
        print("The response of PlatformManagedUsersApi->o_auth_client_users_controller_update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformManagedUsersApi->o_auth_client_users_controller_update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **user_id** | **float**|  | 
 **update_managed_user_input** | [**UpdateManagedUserInput**](UpdateManagedUserInput.md)|  | 

### Return type

[**GetManagedUserOutput**](GetManagedUserOutput.md)

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

