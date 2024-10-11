# openapi_client.PlatformConferencingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conferencing_controller_connect**](PlatformConferencingApi.md#conferencing_controller_connect) | **POST** /v2/conferencing/{app}/connect | connect your conferencing application
[**conferencing_controller_default**](PlatformConferencingApi.md#conferencing_controller_default) | **POST** /v2/conferencing/{app}/default | set your default conferencing application
[**conferencing_controller_disconnect**](PlatformConferencingApi.md#conferencing_controller_disconnect) | **DELETE** /v2/conferencing/{app}/disconnect | disconnect your conferencing application
[**conferencing_controller_list_conferencing_apps**](PlatformConferencingApi.md#conferencing_controller_list_conferencing_apps) | **GET** /v2/conferencing | list your conferencing applications


# **conferencing_controller_connect**
> ConferencingAppOutputResponseDto conferencing_controller_connect(app)

connect your conferencing application

### Example


```python
import openapi_client
from openapi_client.models.conferencing_app_output_response_dto import ConferencingAppOutputResponseDto
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
    api_instance = openapi_client.PlatformConferencingApi(api_client)
    app = 'app_example' # str | 

    try:
        # connect your conferencing application
        api_response = api_instance.conferencing_controller_connect(app)
        print("The response of PlatformConferencingApi->conferencing_controller_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformConferencingApi->conferencing_controller_connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**|  | 

### Return type

[**ConferencingAppOutputResponseDto**](ConferencingAppOutputResponseDto.md)

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

# **conferencing_controller_default**
> SetDefaultConferencingAppOutputResponseDto conferencing_controller_default(app)

set your default conferencing application

### Example


```python
import openapi_client
from openapi_client.models.set_default_conferencing_app_output_response_dto import SetDefaultConferencingAppOutputResponseDto
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
    api_instance = openapi_client.PlatformConferencingApi(api_client)
    app = 'app_example' # str | 

    try:
        # set your default conferencing application
        api_response = api_instance.conferencing_controller_default(app)
        print("The response of PlatformConferencingApi->conferencing_controller_default:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformConferencingApi->conferencing_controller_default: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**|  | 

### Return type

[**SetDefaultConferencingAppOutputResponseDto**](SetDefaultConferencingAppOutputResponseDto.md)

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

# **conferencing_controller_disconnect**
> ConferencingAppOutputResponseDto conferencing_controller_disconnect(app)

disconnect your conferencing application

### Example


```python
import openapi_client
from openapi_client.models.conferencing_app_output_response_dto import ConferencingAppOutputResponseDto
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
    api_instance = openapi_client.PlatformConferencingApi(api_client)
    app = 'app_example' # str | 

    try:
        # disconnect your conferencing application
        api_response = api_instance.conferencing_controller_disconnect(app)
        print("The response of PlatformConferencingApi->conferencing_controller_disconnect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformConferencingApi->conferencing_controller_disconnect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**|  | 

### Return type

[**ConferencingAppOutputResponseDto**](ConferencingAppOutputResponseDto.md)

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

# **conferencing_controller_list_conferencing_apps**
> ConferencingAppsOutputResponseDto conferencing_controller_list_conferencing_apps()

list your conferencing applications

### Example


```python
import openapi_client
from openapi_client.models.conferencing_apps_output_response_dto import ConferencingAppsOutputResponseDto
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
    api_instance = openapi_client.PlatformConferencingApi(api_client)

    try:
        # list your conferencing applications
        api_response = api_instance.conferencing_controller_list_conferencing_apps()
        print("The response of PlatformConferencingApi->conferencing_controller_list_conferencing_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformConferencingApi->conferencing_controller_list_conferencing_apps: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ConferencingAppsOutputResponseDto**](ConferencingAppsOutputResponseDto.md)

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

