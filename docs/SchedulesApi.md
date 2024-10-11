# openapi_client.SchedulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedules_controller20240611_create_schedule**](SchedulesApi.md#schedules_controller20240611_create_schedule) | **POST** /v2/schedules | Create a schedule
[**schedules_controller20240611_delete_schedule**](SchedulesApi.md#schedules_controller20240611_delete_schedule) | **DELETE** /v2/schedules/{scheduleId} | Delete a schedule
[**schedules_controller20240611_get_default_schedule**](SchedulesApi.md#schedules_controller20240611_get_default_schedule) | **GET** /v2/schedules/default | Get default schedule
[**schedules_controller20240611_get_schedule**](SchedulesApi.md#schedules_controller20240611_get_schedule) | **GET** /v2/schedules/{scheduleId} | Get a schedule
[**schedules_controller20240611_get_schedules**](SchedulesApi.md#schedules_controller20240611_get_schedules) | **GET** /v2/schedules | Get all schedules
[**schedules_controller20240611_update_schedule**](SchedulesApi.md#schedules_controller20240611_update_schedule) | **PATCH** /v2/schedules/{scheduleId} | Update a schedule


# **schedules_controller20240611_create_schedule**
> CreateScheduleOutput20240611 schedules_controller20240611_create_schedule(authorization, cal_api_version, create_schedule_input20240611)

Create a schedule

       Create a schedule for the authenticated user.        The point of creating schedules is for event types to be available at specific times.        The first goal of schedules is to have a default schedule. If you are platform customer and created managed users, then it is important to note that each managed user should have a default schedule.       1. If you passed `timeZone` when creating managed user, then the default schedule from Monday to Friday from 9AM to 5PM will be created with that timezone. The managed user can then change the default schedule via the `AvailabilitySettings` atom.       2. If you did not, then we assume you want the user to have this specific schedule right away. You should create a default schedule by specifying       `\"isDefault\": true` in the request body. Until the user has a default schedule the user can't be booked nor manage their schedule via the AvailabilitySettings atom.        The second goal of schedules is to create another schedule that event types can point to. This is useful for when an event is booked because availability is not checked against the default schedule but instead against that specific schedule.       After creating a non-default schedule, you can update an event type to point to that schedule via the PATCH `event-types/{eventTypeId}` endpoint.        When specifying start time and end time for each day use the 24 hour format e.g. 08:00, 15:00 etc.       

### Example


```python
import openapi_client
from openapi_client.models.create_schedule_input20240611 import CreateScheduleInput20240611
from openapi_client.models.create_schedule_output20240611 import CreateScheduleOutput20240611
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
    api_instance = openapi_client.SchedulesApi(api_client)
    authorization = 'authorization_example' # str | value must be `Bearer <token>` where `<token>` either managed user access token or api key prefixed with cal_
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-06-11`
    create_schedule_input20240611 = openapi_client.CreateScheduleInput20240611() # CreateScheduleInput20240611 | 

    try:
        # Create a schedule
        api_response = api_instance.schedules_controller20240611_create_schedule(authorization, cal_api_version, create_schedule_input20240611)
        print("The response of SchedulesApi->schedules_controller20240611_create_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->schedules_controller20240611_create_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| value must be &#x60;Bearer &lt;token&gt;&#x60; where &#x60;&lt;token&gt;&#x60; either managed user access token or api key prefixed with cal_ | 
 **cal_api_version** | **str**| Must be set to &#x60;2024-06-11&#x60; | 
 **create_schedule_input20240611** | [**CreateScheduleInput20240611**](CreateScheduleInput20240611.md)|  | 

### Return type

[**CreateScheduleOutput20240611**](CreateScheduleOutput20240611.md)

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

# **schedules_controller20240611_delete_schedule**
> DeleteScheduleOutput20240611 schedules_controller20240611_delete_schedule(authorization, cal_api_version, schedule_id)

Delete a schedule

### Example


```python
import openapi_client
from openapi_client.models.delete_schedule_output20240611 import DeleteScheduleOutput20240611
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
    api_instance = openapi_client.SchedulesApi(api_client)
    authorization = 'authorization_example' # str | value must be `Bearer <token>` where `<token>` either managed user access token or api key prefixed with cal_
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-06-11`
    schedule_id = 3.4 # float | 

    try:
        # Delete a schedule
        api_response = api_instance.schedules_controller20240611_delete_schedule(authorization, cal_api_version, schedule_id)
        print("The response of SchedulesApi->schedules_controller20240611_delete_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->schedules_controller20240611_delete_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| value must be &#x60;Bearer &lt;token&gt;&#x60; where &#x60;&lt;token&gt;&#x60; either managed user access token or api key prefixed with cal_ | 
 **cal_api_version** | **str**| Must be set to &#x60;2024-06-11&#x60; | 
 **schedule_id** | **float**|  | 

### Return type

[**DeleteScheduleOutput20240611**](DeleteScheduleOutput20240611.md)

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

# **schedules_controller20240611_get_default_schedule**
> GetDefaultScheduleOutput20240611 schedules_controller20240611_get_default_schedule(authorization, cal_api_version)

Get default schedule

Get the default schedule of the authenticated user.

### Example


```python
import openapi_client
from openapi_client.models.get_default_schedule_output20240611 import GetDefaultScheduleOutput20240611
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
    api_instance = openapi_client.SchedulesApi(api_client)
    authorization = 'authorization_example' # str | value must be `Bearer <token>` where `<token>` either managed user access token or api key prefixed with cal_
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-06-11`

    try:
        # Get default schedule
        api_response = api_instance.schedules_controller20240611_get_default_schedule(authorization, cal_api_version)
        print("The response of SchedulesApi->schedules_controller20240611_get_default_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->schedules_controller20240611_get_default_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| value must be &#x60;Bearer &lt;token&gt;&#x60; where &#x60;&lt;token&gt;&#x60; either managed user access token or api key prefixed with cal_ | 
 **cal_api_version** | **str**| Must be set to &#x60;2024-06-11&#x60; | 

### Return type

[**GetDefaultScheduleOutput20240611**](GetDefaultScheduleOutput20240611.md)

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

# **schedules_controller20240611_get_schedule**
> GetScheduleOutput20240611 schedules_controller20240611_get_schedule(authorization, cal_api_version, schedule_id)

Get a schedule

### Example


```python
import openapi_client
from openapi_client.models.get_schedule_output20240611 import GetScheduleOutput20240611
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
    api_instance = openapi_client.SchedulesApi(api_client)
    authorization = 'authorization_example' # str | value must be `Bearer <token>` where `<token>` either managed user access token or api key prefixed with cal_
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-06-11`
    schedule_id = 3.4 # float | 

    try:
        # Get a schedule
        api_response = api_instance.schedules_controller20240611_get_schedule(authorization, cal_api_version, schedule_id)
        print("The response of SchedulesApi->schedules_controller20240611_get_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->schedules_controller20240611_get_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| value must be &#x60;Bearer &lt;token&gt;&#x60; where &#x60;&lt;token&gt;&#x60; either managed user access token or api key prefixed with cal_ | 
 **cal_api_version** | **str**| Must be set to &#x60;2024-06-11&#x60; | 
 **schedule_id** | **float**|  | 

### Return type

[**GetScheduleOutput20240611**](GetScheduleOutput20240611.md)

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

# **schedules_controller20240611_get_schedules**
> GetSchedulesOutput20240611 schedules_controller20240611_get_schedules(authorization, cal_api_version)

Get all schedules

Get all schedules of the authenticated user.

### Example


```python
import openapi_client
from openapi_client.models.get_schedules_output20240611 import GetSchedulesOutput20240611
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
    api_instance = openapi_client.SchedulesApi(api_client)
    authorization = 'authorization_example' # str | value must be `Bearer <token>` where `<token>` either managed user access token or api key prefixed with cal_
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-06-11`

    try:
        # Get all schedules
        api_response = api_instance.schedules_controller20240611_get_schedules(authorization, cal_api_version)
        print("The response of SchedulesApi->schedules_controller20240611_get_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->schedules_controller20240611_get_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| value must be &#x60;Bearer &lt;token&gt;&#x60; where &#x60;&lt;token&gt;&#x60; either managed user access token or api key prefixed with cal_ | 
 **cal_api_version** | **str**| Must be set to &#x60;2024-06-11&#x60; | 

### Return type

[**GetSchedulesOutput20240611**](GetSchedulesOutput20240611.md)

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

# **schedules_controller20240611_update_schedule**
> UpdateScheduleOutput20240611 schedules_controller20240611_update_schedule(authorization, cal_api_version, schedule_id, update_schedule_input20240611)

Update a schedule

### Example


```python
import openapi_client
from openapi_client.models.update_schedule_input20240611 import UpdateScheduleInput20240611
from openapi_client.models.update_schedule_output20240611 import UpdateScheduleOutput20240611
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
    api_instance = openapi_client.SchedulesApi(api_client)
    authorization = 'authorization_example' # str | value must be `Bearer <token>` where `<token>` either managed user access token or api key prefixed with cal_
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-06-11`
    schedule_id = 'schedule_id_example' # str | 
    update_schedule_input20240611 = openapi_client.UpdateScheduleInput20240611() # UpdateScheduleInput20240611 | 

    try:
        # Update a schedule
        api_response = api_instance.schedules_controller20240611_update_schedule(authorization, cal_api_version, schedule_id, update_schedule_input20240611)
        print("The response of SchedulesApi->schedules_controller20240611_update_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->schedules_controller20240611_update_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| value must be &#x60;Bearer &lt;token&gt;&#x60; where &#x60;&lt;token&gt;&#x60; either managed user access token or api key prefixed with cal_ | 
 **cal_api_version** | **str**| Must be set to &#x60;2024-06-11&#x60; | 
 **schedule_id** | **str**|  | 
 **update_schedule_input20240611** | [**UpdateScheduleInput20240611**](UpdateScheduleInput20240611.md)|  | 

### Return type

[**UpdateScheduleOutput20240611**](UpdateScheduleOutput20240611.md)

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

