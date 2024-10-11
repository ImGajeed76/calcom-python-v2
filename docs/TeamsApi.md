# openapi_client.TeamsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_teams_controller_get_all_teams_0**](TeamsApi.md#organizations_teams_controller_get_all_teams_0) | **GET** /v2/organizations/{orgId}/teams | Get all teams


# **organizations_teams_controller_get_all_teams_0**
> OrgTeamsOutputResponseDto organizations_teams_controller_get_all_teams_0(org_id, take=take, skip=skip)

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
    api_instance = openapi_client.TeamsApi(api_client)
    org_id = 3.4 # float | 
    take = 10 # float | The number of items to return (optional)
    skip = 0 # float | The number of items to skip (optional)

    try:
        # Get all teams
        api_response = api_instance.organizations_teams_controller_get_all_teams_0(org_id, take=take, skip=skip)
        print("The response of TeamsApi->organizations_teams_controller_get_all_teams_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->organizations_teams_controller_get_all_teams_0: %s\n" % e)
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

