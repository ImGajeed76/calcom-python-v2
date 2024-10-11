# openapi_client.OrgsEventTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_event_types_controller_create_phone_call**](OrgsEventTypesApi.md#organizations_event_types_controller_create_phone_call) | **POST** /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId}/create-phone-call | Create a phone call
[**organizations_event_types_controller_create_team_event_type**](OrgsEventTypesApi.md#organizations_event_types_controller_create_team_event_type) | **POST** /v2/organizations/{orgId}/teams/{teamId}/event-types | Create an event type
[**organizations_event_types_controller_delete_team_event_type**](OrgsEventTypesApi.md#organizations_event_types_controller_delete_team_event_type) | **DELETE** /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId} | Delete a team event type
[**organizations_event_types_controller_get_team_event_type**](OrgsEventTypesApi.md#organizations_event_types_controller_get_team_event_type) | **GET** /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId} | Get an event type
[**organizations_event_types_controller_get_team_event_types**](OrgsEventTypesApi.md#organizations_event_types_controller_get_team_event_types) | **GET** /v2/organizations/{orgId}/teams/{teamId}/event-types | Get a team event type
[**organizations_event_types_controller_get_teams_event_types**](OrgsEventTypesApi.md#organizations_event_types_controller_get_teams_event_types) | **GET** /v2/organizations/{orgId}/teams/event-types | Get all team event types
[**organizations_event_types_controller_update_team_event_type**](OrgsEventTypesApi.md#organizations_event_types_controller_update_team_event_type) | **PATCH** /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId} | Update a team event type


# **organizations_event_types_controller_create_phone_call**
> CreatePhoneCallOutput organizations_event_types_controller_create_phone_call(event_type_id, org_id, create_phone_call_input)

Create a phone call

### Example


```python
import openapi_client
from openapi_client.models.create_phone_call_input import CreatePhoneCallInput
from openapi_client.models.create_phone_call_output import CreatePhoneCallOutput
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
    api_instance = openapi_client.OrgsEventTypesApi(api_client)
    event_type_id = 3.4 # float | 
    org_id = 3.4 # float | 
    create_phone_call_input = openapi_client.CreatePhoneCallInput() # CreatePhoneCallInput | 

    try:
        # Create a phone call
        api_response = api_instance.organizations_event_types_controller_create_phone_call(event_type_id, org_id, create_phone_call_input)
        print("The response of OrgsEventTypesApi->organizations_event_types_controller_create_phone_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsEventTypesApi->organizations_event_types_controller_create_phone_call: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type_id** | **float**|  | 
 **org_id** | **float**|  | 
 **create_phone_call_input** | [**CreatePhoneCallInput**](CreatePhoneCallInput.md)|  | 

### Return type

[**CreatePhoneCallOutput**](CreatePhoneCallOutput.md)

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

# **organizations_event_types_controller_create_team_event_type**
> CreateTeamEventTypeOutput organizations_event_types_controller_create_team_event_type(team_id, org_id, create_team_event_type_input20240614)

Create an event type

### Example


```python
import openapi_client
from openapi_client.models.create_team_event_type_input20240614 import CreateTeamEventTypeInput20240614
from openapi_client.models.create_team_event_type_output import CreateTeamEventTypeOutput
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
    api_instance = openapi_client.OrgsEventTypesApi(api_client)
    team_id = 3.4 # float | 
    org_id = 3.4 # float | 
    create_team_event_type_input20240614 = openapi_client.CreateTeamEventTypeInput20240614() # CreateTeamEventTypeInput20240614 | 

    try:
        # Create an event type
        api_response = api_instance.organizations_event_types_controller_create_team_event_type(team_id, org_id, create_team_event_type_input20240614)
        print("The response of OrgsEventTypesApi->organizations_event_types_controller_create_team_event_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsEventTypesApi->organizations_event_types_controller_create_team_event_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **float**|  | 
 **org_id** | **float**|  | 
 **create_team_event_type_input20240614** | [**CreateTeamEventTypeInput20240614**](CreateTeamEventTypeInput20240614.md)|  | 

### Return type

[**CreateTeamEventTypeOutput**](CreateTeamEventTypeOutput.md)

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

# **organizations_event_types_controller_delete_team_event_type**
> DeleteTeamEventTypeOutput organizations_event_types_controller_delete_team_event_type(team_id, event_type_id)

Delete a team event type

### Example


```python
import openapi_client
from openapi_client.models.delete_team_event_type_output import DeleteTeamEventTypeOutput
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
    api_instance = openapi_client.OrgsEventTypesApi(api_client)
    team_id = 3.4 # float | 
    event_type_id = 3.4 # float | 

    try:
        # Delete a team event type
        api_response = api_instance.organizations_event_types_controller_delete_team_event_type(team_id, event_type_id)
        print("The response of OrgsEventTypesApi->organizations_event_types_controller_delete_team_event_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsEventTypesApi->organizations_event_types_controller_delete_team_event_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **float**|  | 
 **event_type_id** | **float**|  | 

### Return type

[**DeleteTeamEventTypeOutput**](DeleteTeamEventTypeOutput.md)

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

# **organizations_event_types_controller_get_team_event_type**
> GetTeamEventTypeOutput organizations_event_types_controller_get_team_event_type(team_id, event_type_id)

Get an event type

### Example


```python
import openapi_client
from openapi_client.models.get_team_event_type_output import GetTeamEventTypeOutput
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
    api_instance = openapi_client.OrgsEventTypesApi(api_client)
    team_id = 3.4 # float | 
    event_type_id = 3.4 # float | 

    try:
        # Get an event type
        api_response = api_instance.organizations_event_types_controller_get_team_event_type(team_id, event_type_id)
        print("The response of OrgsEventTypesApi->organizations_event_types_controller_get_team_event_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsEventTypesApi->organizations_event_types_controller_get_team_event_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **float**|  | 
 **event_type_id** | **float**|  | 

### Return type

[**GetTeamEventTypeOutput**](GetTeamEventTypeOutput.md)

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

# **organizations_event_types_controller_get_team_event_types**
> GetTeamEventTypesOutput organizations_event_types_controller_get_team_event_types(team_id, event_slug=event_slug)

Get a team event type

### Example


```python
import openapi_client
from openapi_client.models.get_team_event_types_output import GetTeamEventTypesOutput
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
    api_instance = openapi_client.OrgsEventTypesApi(api_client)
    team_id = 3.4 # float | 
    event_slug = 'event_slug_example' # str | Slug of team event type to return. (optional)

    try:
        # Get a team event type
        api_response = api_instance.organizations_event_types_controller_get_team_event_types(team_id, event_slug=event_slug)
        print("The response of OrgsEventTypesApi->organizations_event_types_controller_get_team_event_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsEventTypesApi->organizations_event_types_controller_get_team_event_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **float**|  | 
 **event_slug** | **str**| Slug of team event type to return. | [optional] 

### Return type

[**GetTeamEventTypesOutput**](GetTeamEventTypesOutput.md)

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

# **organizations_event_types_controller_get_teams_event_types**
> GetTeamEventTypesOutput organizations_event_types_controller_get_teams_event_types(org_id, take=take, skip=skip)

Get all team event types

### Example


```python
import openapi_client
from openapi_client.models.get_team_event_types_output import GetTeamEventTypesOutput
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
    api_instance = openapi_client.OrgsEventTypesApi(api_client)
    org_id = 3.4 # float | 
    take = 10 # float | The number of items to return (optional)
    skip = 0 # float | The number of items to skip (optional)

    try:
        # Get all team event types
        api_response = api_instance.organizations_event_types_controller_get_teams_event_types(org_id, take=take, skip=skip)
        print("The response of OrgsEventTypesApi->organizations_event_types_controller_get_teams_event_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsEventTypesApi->organizations_event_types_controller_get_teams_event_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **take** | **float**| The number of items to return | [optional] 
 **skip** | **float**| The number of items to skip | [optional] 

### Return type

[**GetTeamEventTypesOutput**](GetTeamEventTypesOutput.md)

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

# **organizations_event_types_controller_update_team_event_type**
> UpdateTeamEventTypeOutput organizations_event_types_controller_update_team_event_type(team_id, event_type_id, update_team_event_type_input20240614)

Update a team event type

### Example


```python
import openapi_client
from openapi_client.models.update_team_event_type_input20240614 import UpdateTeamEventTypeInput20240614
from openapi_client.models.update_team_event_type_output import UpdateTeamEventTypeOutput
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
    api_instance = openapi_client.OrgsEventTypesApi(api_client)
    team_id = 3.4 # float | 
    event_type_id = 3.4 # float | 
    update_team_event_type_input20240614 = openapi_client.UpdateTeamEventTypeInput20240614() # UpdateTeamEventTypeInput20240614 | 

    try:
        # Update a team event type
        api_response = api_instance.organizations_event_types_controller_update_team_event_type(team_id, event_type_id, update_team_event_type_input20240614)
        print("The response of OrgsEventTypesApi->organizations_event_types_controller_update_team_event_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsEventTypesApi->organizations_event_types_controller_update_team_event_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **float**|  | 
 **event_type_id** | **float**|  | 
 **update_team_event_type_input20240614** | [**UpdateTeamEventTypeInput20240614**](UpdateTeamEventTypeInput20240614.md)|  | 

### Return type

[**UpdateTeamEventTypeOutput**](UpdateTeamEventTypeOutput.md)

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

