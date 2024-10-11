# openapi_client.OrgsTeamsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_teams_controller_create_team**](OrgsTeamsApi.md#organizations_teams_controller_create_team) | **POST** /v2/organizations/{orgId}/teams | Create a team
[**organizations_teams_controller_delete_team**](OrgsTeamsApi.md#organizations_teams_controller_delete_team) | **DELETE** /v2/organizations/{orgId}/teams/{teamId} | Delete a team
[**organizations_teams_controller_get_all_teams**](OrgsTeamsApi.md#organizations_teams_controller_get_all_teams) | **GET** /v2/organizations/{orgId}/teams | Get all teams
[**organizations_teams_controller_get_my_teams**](OrgsTeamsApi.md#organizations_teams_controller_get_my_teams) | **GET** /v2/organizations/{orgId}/teams/me | Get team membership for user
[**organizations_teams_controller_get_team**](OrgsTeamsApi.md#organizations_teams_controller_get_team) | **GET** /v2/organizations/{orgId}/teams/{teamId} | Get a team
[**organizations_teams_controller_update_team**](OrgsTeamsApi.md#organizations_teams_controller_update_team) | **PATCH** /v2/organizations/{orgId}/teams/{teamId} | Update a team


# **organizations_teams_controller_create_team**
> OrgTeamOutputResponseDto organizations_teams_controller_create_team(org_id, x_cal_client_id, create_org_team_dto)

Create a team

### Example


```python
import openapi_client
from openapi_client.models.create_org_team_dto import CreateOrgTeamDto
from openapi_client.models.org_team_output_response_dto import OrgTeamOutputResponseDto
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
    api_instance = openapi_client.OrgsTeamsApi(api_client)
    org_id = 3.4 # float | 
    x_cal_client_id = 'x_cal_client_id_example' # str | 
    create_org_team_dto = openapi_client.CreateOrgTeamDto() # CreateOrgTeamDto | 

    try:
        # Create a team
        api_response = api_instance.organizations_teams_controller_create_team(org_id, x_cal_client_id, create_org_team_dto)
        print("The response of OrgsTeamsApi->organizations_teams_controller_create_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsTeamsApi->organizations_teams_controller_create_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **x_cal_client_id** | **str**|  | 
 **create_org_team_dto** | [**CreateOrgTeamDto**](CreateOrgTeamDto.md)|  | 

### Return type

[**OrgTeamOutputResponseDto**](OrgTeamOutputResponseDto.md)

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

# **organizations_teams_controller_delete_team**
> OrgTeamOutputResponseDto organizations_teams_controller_delete_team(org_id, team_id)

Delete a team

### Example


```python
import openapi_client
from openapi_client.models.org_team_output_response_dto import OrgTeamOutputResponseDto
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
    api_instance = openapi_client.OrgsTeamsApi(api_client)
    org_id = 3.4 # float | 
    team_id = 3.4 # float | 

    try:
        # Delete a team
        api_response = api_instance.organizations_teams_controller_delete_team(org_id, team_id)
        print("The response of OrgsTeamsApi->organizations_teams_controller_delete_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsTeamsApi->organizations_teams_controller_delete_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **team_id** | **float**|  | 

### Return type

[**OrgTeamOutputResponseDto**](OrgTeamOutputResponseDto.md)

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

# **organizations_teams_controller_get_all_teams**
> OrgTeamsOutputResponseDto organizations_teams_controller_get_all_teams(org_id, take=take, skip=skip)

Get all teams

### Example


```python
import openapi_client
from openapi_client.models.org_teams_output_response_dto import OrgTeamsOutputResponseDto
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
    api_instance = openapi_client.OrgsTeamsApi(api_client)
    org_id = 3.4 # float | 
    take = 10 # float | The number of items to return (optional)
    skip = 0 # float | The number of items to skip (optional)

    try:
        # Get all teams
        api_response = api_instance.organizations_teams_controller_get_all_teams(org_id, take=take, skip=skip)
        print("The response of OrgsTeamsApi->organizations_teams_controller_get_all_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsTeamsApi->organizations_teams_controller_get_all_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **take** | **float**| The number of items to return | [optional] 
 **skip** | **float**| The number of items to skip | [optional] 

### Return type

[**OrgTeamsOutputResponseDto**](OrgTeamsOutputResponseDto.md)

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

# **organizations_teams_controller_get_my_teams**
> OrgMeTeamsOutputResponseDto organizations_teams_controller_get_my_teams(org_id, take=take, skip=skip)

Get team membership for user

### Example


```python
import openapi_client
from openapi_client.models.org_me_teams_output_response_dto import OrgMeTeamsOutputResponseDto
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
    api_instance = openapi_client.OrgsTeamsApi(api_client)
    org_id = 3.4 # float | 
    take = 10 # float | The number of items to return (optional)
    skip = 0 # float | The number of items to skip (optional)

    try:
        # Get team membership for user
        api_response = api_instance.organizations_teams_controller_get_my_teams(org_id, take=take, skip=skip)
        print("The response of OrgsTeamsApi->organizations_teams_controller_get_my_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsTeamsApi->organizations_teams_controller_get_my_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **take** | **float**| The number of items to return | [optional] 
 **skip** | **float**| The number of items to skip | [optional] 

### Return type

[**OrgMeTeamsOutputResponseDto**](OrgMeTeamsOutputResponseDto.md)

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

# **organizations_teams_controller_get_team**
> OrgTeamOutputResponseDto organizations_teams_controller_get_team()

Get a team

### Example


```python
import openapi_client
from openapi_client.models.org_team_output_response_dto import OrgTeamOutputResponseDto
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
    api_instance = openapi_client.OrgsTeamsApi(api_client)

    try:
        # Get a team
        api_response = api_instance.organizations_teams_controller_get_team()
        print("The response of OrgsTeamsApi->organizations_teams_controller_get_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsTeamsApi->organizations_teams_controller_get_team: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgTeamOutputResponseDto**](OrgTeamOutputResponseDto.md)

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

# **organizations_teams_controller_update_team**
> OrgTeamOutputResponseDto organizations_teams_controller_update_team(org_id, team_id, update_org_team_dto)

Update a team

### Example


```python
import openapi_client
from openapi_client.models.org_team_output_response_dto import OrgTeamOutputResponseDto
from openapi_client.models.update_org_team_dto import UpdateOrgTeamDto
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
    api_instance = openapi_client.OrgsTeamsApi(api_client)
    org_id = 3.4 # float | 
    team_id = 3.4 # float | 
    update_org_team_dto = openapi_client.UpdateOrgTeamDto() # UpdateOrgTeamDto | 

    try:
        # Update a team
        api_response = api_instance.organizations_teams_controller_update_team(org_id, team_id, update_org_team_dto)
        print("The response of OrgsTeamsApi->organizations_teams_controller_update_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsTeamsApi->organizations_teams_controller_update_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **team_id** | **float**|  | 
 **update_org_team_dto** | [**UpdateOrgTeamDto**](UpdateOrgTeamDto.md)|  | 

### Return type

[**OrgTeamOutputResponseDto**](OrgTeamOutputResponseDto.md)

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

