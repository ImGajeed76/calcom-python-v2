# openapi_client.OrgsSchedulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_schedules_controller_create_user_schedule**](OrgsSchedulesApi.md#organizations_schedules_controller_create_user_schedule) | **POST** /v2/organizations/{orgId}/users/{userId}/schedules | Create a schedule
[**organizations_schedules_controller_delete_user_schedule**](OrgsSchedulesApi.md#organizations_schedules_controller_delete_user_schedule) | **DELETE** /v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId} | Delete a schedule
[**organizations_schedules_controller_get_organization_schedules**](OrgsSchedulesApi.md#organizations_schedules_controller_get_organization_schedules) | **GET** /v2/organizations/{orgId}/schedules | Get all schedules
[**organizations_schedules_controller_get_user_schedule**](OrgsSchedulesApi.md#organizations_schedules_controller_get_user_schedule) | **GET** /v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId} | Get a schedule
[**organizations_schedules_controller_get_user_schedules**](OrgsSchedulesApi.md#organizations_schedules_controller_get_user_schedules) | **GET** /v2/organizations/{orgId}/users/{userId}/schedules | Get all schedules
[**organizations_schedules_controller_update_user_schedule**](OrgsSchedulesApi.md#organizations_schedules_controller_update_user_schedule) | **PATCH** /v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId} | Update a schedule


# **organizations_schedules_controller_create_user_schedule**
> CreateScheduleOutput20240611 organizations_schedules_controller_create_user_schedule(user_id, create_schedule_input20240611)

Create a schedule

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
    api_instance = openapi_client.OrgsSchedulesApi(api_client)
    user_id = 3.4 # float | 
    create_schedule_input20240611 = openapi_client.CreateScheduleInput20240611() # CreateScheduleInput20240611 | 

    try:
        # Create a schedule
        api_response = api_instance.organizations_schedules_controller_create_user_schedule(user_id, create_schedule_input20240611)
        print("The response of OrgsSchedulesApi->organizations_schedules_controller_create_user_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsSchedulesApi->organizations_schedules_controller_create_user_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
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

# **organizations_schedules_controller_delete_user_schedule**
> DeleteScheduleOutput20240611 organizations_schedules_controller_delete_user_schedule(user_id, schedule_id)

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
    api_instance = openapi_client.OrgsSchedulesApi(api_client)
    user_id = 3.4 # float | 
    schedule_id = 3.4 # float | 

    try:
        # Delete a schedule
        api_response = api_instance.organizations_schedules_controller_delete_user_schedule(user_id, schedule_id)
        print("The response of OrgsSchedulesApi->organizations_schedules_controller_delete_user_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsSchedulesApi->organizations_schedules_controller_delete_user_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
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

# **organizations_schedules_controller_get_organization_schedules**
> GetSchedulesOutput20240611 organizations_schedules_controller_get_organization_schedules(org_id, take=take, skip=skip)

Get all schedules

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
    api_instance = openapi_client.OrgsSchedulesApi(api_client)
    org_id = 3.4 # float | 
    take = 10 # float | The number of items to return (optional)
    skip = 0 # float | The number of items to skip (optional)

    try:
        # Get all schedules
        api_response = api_instance.organizations_schedules_controller_get_organization_schedules(org_id, take=take, skip=skip)
        print("The response of OrgsSchedulesApi->organizations_schedules_controller_get_organization_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsSchedulesApi->organizations_schedules_controller_get_organization_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **take** | **float**| The number of items to return | [optional] 
 **skip** | **float**| The number of items to skip | [optional] 

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

# **organizations_schedules_controller_get_user_schedule**
> GetScheduleOutput20240611 organizations_schedules_controller_get_user_schedule(user_id, schedule_id)

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
    api_instance = openapi_client.OrgsSchedulesApi(api_client)
    user_id = 3.4 # float | 
    schedule_id = 3.4 # float | 

    try:
        # Get a schedule
        api_response = api_instance.organizations_schedules_controller_get_user_schedule(user_id, schedule_id)
        print("The response of OrgsSchedulesApi->organizations_schedules_controller_get_user_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsSchedulesApi->organizations_schedules_controller_get_user_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
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

# **organizations_schedules_controller_get_user_schedules**
> GetSchedulesOutput20240611 organizations_schedules_controller_get_user_schedules(user_id)

Get all schedules

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
    api_instance = openapi_client.OrgsSchedulesApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get all schedules
        api_response = api_instance.organizations_schedules_controller_get_user_schedules(user_id)
        print("The response of OrgsSchedulesApi->organizations_schedules_controller_get_user_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsSchedulesApi->organizations_schedules_controller_get_user_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

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

# **organizations_schedules_controller_update_user_schedule**
> UpdateScheduleOutput20240611 organizations_schedules_controller_update_user_schedule(user_id, schedule_id, update_schedule_input20240611)

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
    api_instance = openapi_client.OrgsSchedulesApi(api_client)
    user_id = 3.4 # float | 
    schedule_id = 3.4 # float | 
    update_schedule_input20240611 = openapi_client.UpdateScheduleInput20240611() # UpdateScheduleInput20240611 | 

    try:
        # Update a schedule
        api_response = api_instance.organizations_schedules_controller_update_user_schedule(user_id, schedule_id, update_schedule_input20240611)
        print("The response of OrgsSchedulesApi->organizations_schedules_controller_update_user_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsSchedulesApi->organizations_schedules_controller_update_user_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **schedule_id** | **float**|  | 
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

