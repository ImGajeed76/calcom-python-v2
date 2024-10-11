# openapi_client.PlatformGoogleCalendarApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gcal_controller_check**](PlatformGoogleCalendarApi.md#gcal_controller_check) | **GET** /v2/gcal/check | Check a calendar connection status
[**gcal_controller_redirect**](PlatformGoogleCalendarApi.md#gcal_controller_redirect) | **GET** /v2/gcal/oauth/auth-url | Get auth URL
[**gcal_controller_save**](PlatformGoogleCalendarApi.md#gcal_controller_save) | **GET** /v2/gcal/oauth/save | Connect a calendar


# **gcal_controller_check**
> GcalCheckOutput gcal_controller_check()

Check a calendar connection status

### Example


```python
import openapi_client
from openapi_client.models.gcal_check_output import GcalCheckOutput
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
    api_instance = openapi_client.PlatformGoogleCalendarApi(api_client)

    try:
        # Check a calendar connection status
        api_response = api_instance.gcal_controller_check()
        print("The response of PlatformGoogleCalendarApi->gcal_controller_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformGoogleCalendarApi->gcal_controller_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GcalCheckOutput**](GcalCheckOutput.md)

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

# **gcal_controller_redirect**
> GcalAuthUrlOutput gcal_controller_redirect(authorization)

Get auth URL

### Example


```python
import openapi_client
from openapi_client.models.gcal_auth_url_output import GcalAuthUrlOutput
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
    api_instance = openapi_client.PlatformGoogleCalendarApi(api_client)
    authorization = 'authorization_example' # str | 

    try:
        # Get auth URL
        api_response = api_instance.gcal_controller_redirect(authorization)
        print("The response of PlatformGoogleCalendarApi->gcal_controller_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformGoogleCalendarApi->gcal_controller_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 

### Return type

[**GcalAuthUrlOutput**](GcalAuthUrlOutput.md)

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

# **gcal_controller_save**
> GcalSaveRedirectOutput gcal_controller_save(state, code)

Connect a calendar

### Example


```python
import openapi_client
from openapi_client.models.gcal_save_redirect_output import GcalSaveRedirectOutput
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
    api_instance = openapi_client.PlatformGoogleCalendarApi(api_client)
    state = 'state_example' # str | 
    code = 'code_example' # str | 

    try:
        # Connect a calendar
        api_response = api_instance.gcal_controller_save(state, code)
        print("The response of PlatformGoogleCalendarApi->gcal_controller_save:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformGoogleCalendarApi->gcal_controller_save: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 
 **code** | **str**|  | 

### Return type

[**GcalSaveRedirectOutput**](GcalSaveRedirectOutput.md)

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

