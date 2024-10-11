# openapi_client.CalendarsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calendars_controller_check**](CalendarsApi.md#calendars_controller_check) | **GET** /v2/calendars/{calendar}/check | Check a calendar connection
[**calendars_controller_check_ics_feed**](CalendarsApi.md#calendars_controller_check_ics_feed) | **GET** /v2/calendars/ics-feed/check | Check an ICS feed
[**calendars_controller_create_ics_feed**](CalendarsApi.md#calendars_controller_create_ics_feed) | **POST** /v2/calendars/ics-feed/save | Save an ICS feed
[**calendars_controller_delete_calendar_credentials**](CalendarsApi.md#calendars_controller_delete_calendar_credentials) | **POST** /v2/calendars/{calendar}/disconnect | Disconnect a calendar
[**calendars_controller_get_busy_times**](CalendarsApi.md#calendars_controller_get_busy_times) | **GET** /v2/calendars/busy-times | Get busy times
[**calendars_controller_get_calendars**](CalendarsApi.md#calendars_controller_get_calendars) | **GET** /v2/calendars | Get all calendars
[**calendars_controller_redirect**](CalendarsApi.md#calendars_controller_redirect) | **GET** /v2/calendars/{calendar}/connect | Get connect URL
[**calendars_controller_save**](CalendarsApi.md#calendars_controller_save) | **GET** /v2/calendars/{calendar}/save | Save a calendar
[**calendars_controller_sync_credentials**](CalendarsApi.md#calendars_controller_sync_credentials) | **POST** /v2/calendars/{calendar}/credentials | Sync credentials


# **calendars_controller_check**
> object calendars_controller_check(calendar)

Check a calendar connection

### Example


```python
import openapi_client
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
    api_instance = openapi_client.CalendarsApi(api_client)
    calendar = 'calendar_example' # str | 

    try:
        # Check a calendar connection
        api_response = api_instance.calendars_controller_check(calendar)
        print("The response of CalendarsApi->calendars_controller_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->calendars_controller_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar** | **str**|  | 

### Return type

**object**

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

# **calendars_controller_check_ics_feed**
> object calendars_controller_check_ics_feed()

Check an ICS feed

### Example


```python
import openapi_client
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
    api_instance = openapi_client.CalendarsApi(api_client)

    try:
        # Check an ICS feed
        api_response = api_instance.calendars_controller_check_ics_feed()
        print("The response of CalendarsApi->calendars_controller_check_ics_feed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->calendars_controller_check_ics_feed: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **calendars_controller_create_ics_feed**
> CreateIcsFeedOutputResponseDto calendars_controller_create_ics_feed(create_ics_feed_input_dto)

Save an ICS feed

### Example


```python
import openapi_client
from openapi_client.models.create_ics_feed_input_dto import CreateIcsFeedInputDto
from openapi_client.models.create_ics_feed_output_response_dto import CreateIcsFeedOutputResponseDto
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
    api_instance = openapi_client.CalendarsApi(api_client)
    create_ics_feed_input_dto = openapi_client.CreateIcsFeedInputDto() # CreateIcsFeedInputDto | 

    try:
        # Save an ICS feed
        api_response = api_instance.calendars_controller_create_ics_feed(create_ics_feed_input_dto)
        print("The response of CalendarsApi->calendars_controller_create_ics_feed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->calendars_controller_create_ics_feed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_ics_feed_input_dto** | [**CreateIcsFeedInputDto**](CreateIcsFeedInputDto.md)|  | 

### Return type

[**CreateIcsFeedOutputResponseDto**](CreateIcsFeedOutputResponseDto.md)

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

# **calendars_controller_delete_calendar_credentials**
> DeletedCalendarCredentialsOutputResponseDto calendars_controller_delete_calendar_credentials(calendar, delete_calendar_credentials_input_body_dto)

Disconnect a calendar

### Example


```python
import openapi_client
from openapi_client.models.delete_calendar_credentials_input_body_dto import DeleteCalendarCredentialsInputBodyDto
from openapi_client.models.deleted_calendar_credentials_output_response_dto import DeletedCalendarCredentialsOutputResponseDto
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
    api_instance = openapi_client.CalendarsApi(api_client)
    calendar = 'calendar_example' # str | 
    delete_calendar_credentials_input_body_dto = openapi_client.DeleteCalendarCredentialsInputBodyDto() # DeleteCalendarCredentialsInputBodyDto | 

    try:
        # Disconnect a calendar
        api_response = api_instance.calendars_controller_delete_calendar_credentials(calendar, delete_calendar_credentials_input_body_dto)
        print("The response of CalendarsApi->calendars_controller_delete_calendar_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->calendars_controller_delete_calendar_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar** | **str**|  | 
 **delete_calendar_credentials_input_body_dto** | [**DeleteCalendarCredentialsInputBodyDto**](DeleteCalendarCredentialsInputBodyDto.md)|  | 

### Return type

[**DeletedCalendarCredentialsOutputResponseDto**](DeletedCalendarCredentialsOutputResponseDto.md)

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

# **calendars_controller_get_busy_times**
> GetBusyTimesOutput calendars_controller_get_busy_times(logged_in_users_tz, calendars_to_load)

Get busy times

### Example


```python
import openapi_client
from openapi_client.models.get_busy_times_output import GetBusyTimesOutput
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
    api_instance = openapi_client.CalendarsApi(api_client)
    logged_in_users_tz = 'America/New_York' # str | The timezone of the logged in user represented as a string
    calendars_to_load = ['[{ credentialId: \"1\", externalId: \"AQgtJE7RnHEeyisVq2ENs2gAAAgEGAAAACgtJE7RnHEeyisVq2ENs2gAAAhSDAAAA\" }, { credentialId: \"2\", externalId: \"AQM7RnHEeyisVq2ENs2gAAAhFDBBBBB\" }]'] # List[str] | An array of Calendar objects representing the calendars to be loaded

    try:
        # Get busy times
        api_response = api_instance.calendars_controller_get_busy_times(logged_in_users_tz, calendars_to_load)
        print("The response of CalendarsApi->calendars_controller_get_busy_times:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->calendars_controller_get_busy_times: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logged_in_users_tz** | **str**| The timezone of the logged in user represented as a string | 
 **calendars_to_load** | [**List[str]**](str.md)| An array of Calendar objects representing the calendars to be loaded | 

### Return type

[**GetBusyTimesOutput**](GetBusyTimesOutput.md)

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

# **calendars_controller_get_calendars**
> ConnectedCalendarsOutput calendars_controller_get_calendars()

Get all calendars

### Example


```python
import openapi_client
from openapi_client.models.connected_calendars_output import ConnectedCalendarsOutput
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
    api_instance = openapi_client.CalendarsApi(api_client)

    try:
        # Get all calendars
        api_response = api_instance.calendars_controller_get_calendars()
        print("The response of CalendarsApi->calendars_controller_get_calendars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->calendars_controller_get_calendars: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ConnectedCalendarsOutput**](ConnectedCalendarsOutput.md)

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

# **calendars_controller_redirect**
> object calendars_controller_redirect(authorization, calendar)

Get connect URL

### Example


```python
import openapi_client
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
    api_instance = openapi_client.CalendarsApi(api_client)
    authorization = 'authorization_example' # str | 
    calendar = 'calendar_example' # str | 

    try:
        # Get connect URL
        api_response = api_instance.calendars_controller_redirect(authorization, calendar)
        print("The response of CalendarsApi->calendars_controller_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->calendars_controller_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **calendar** | **str**|  | 

### Return type

**object**

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

# **calendars_controller_save**
> calendars_controller_save(state, code, calendar)

Save a calendar

### Example


```python
import openapi_client
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
    api_instance = openapi_client.CalendarsApi(api_client)
    state = 'state_example' # str | 
    code = 'code_example' # str | 
    calendar = 'calendar_example' # str | 

    try:
        # Save a calendar
        api_instance.calendars_controller_save(state, code, calendar)
    except Exception as e:
        print("Exception when calling CalendarsApi->calendars_controller_save: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 
 **code** | **str**|  | 
 **calendar** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendars_controller_sync_credentials**
> calendars_controller_sync_credentials(calendar)

Sync credentials

### Example


```python
import openapi_client
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
    api_instance = openapi_client.CalendarsApi(api_client)
    calendar = 'calendar_example' # str | 

    try:
        # Sync credentials
        api_instance.calendars_controller_sync_credentials(calendar)
    except Exception as e:
        print("Exception when calling CalendarsApi->calendars_controller_sync_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

