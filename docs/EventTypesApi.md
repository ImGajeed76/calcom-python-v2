# openapi_client.EventTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_types_controller20240614_create_event_type**](EventTypesApi.md#event_types_controller20240614_create_event_type) | **POST** /v2/event-types | Create an event type
[**event_types_controller20240614_delete_event_type**](EventTypesApi.md#event_types_controller20240614_delete_event_type) | **DELETE** /v2/event-types/{eventTypeId} | Delete an event type
[**event_types_controller20240614_get_event_type_by_id**](EventTypesApi.md#event_types_controller20240614_get_event_type_by_id) | **GET** /v2/event-types/{eventTypeId} | Get an event type
[**event_types_controller20240614_get_event_types**](EventTypesApi.md#event_types_controller20240614_get_event_types) | **GET** /v2/event-types | Get all event types
[**event_types_controller20240614_update_event_type**](EventTypesApi.md#event_types_controller20240614_update_event_type) | **PATCH** /v2/event-types/{eventTypeId} | Update an event type


# **event_types_controller20240614_create_event_type**
> CreateEventTypeOutput20240614 event_types_controller20240614_create_event_type(cal_api_version, authorization, create_event_type_input20240614)

Create an event type

### Example


```python
import openapi_client
from openapi_client.models.create_event_type_input20240614 import CreateEventTypeInput20240614
from openapi_client.models.create_event_type_output20240614 import CreateEventTypeOutput20240614
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
    api_instance = openapi_client.EventTypesApi(api_client)
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-06-14`
    authorization = 'authorization_example' # str | value must be `Bearer <token>` where `<token>` either managed user access token or api key prefixed with cal_
    create_event_type_input20240614 = openapi_client.CreateEventTypeInput20240614() # CreateEventTypeInput20240614 | 

    try:
        # Create an event type
        api_response = api_instance.event_types_controller20240614_create_event_type(cal_api_version, authorization, create_event_type_input20240614)
        print("The response of EventTypesApi->event_types_controller20240614_create_event_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventTypesApi->event_types_controller20240614_create_event_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cal_api_version** | **str**| Must be set to &#x60;2024-06-14&#x60; | 
 **authorization** | **str**| value must be &#x60;Bearer &lt;token&gt;&#x60; where &#x60;&lt;token&gt;&#x60; either managed user access token or api key prefixed with cal_ | 
 **create_event_type_input20240614** | [**CreateEventTypeInput20240614**](CreateEventTypeInput20240614.md)|  | 

### Return type

[**CreateEventTypeOutput20240614**](CreateEventTypeOutput20240614.md)

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

# **event_types_controller20240614_delete_event_type**
> DeleteEventTypeOutput20240614 event_types_controller20240614_delete_event_type(cal_api_version, event_type_id, authorization)

Delete an event type

### Example


```python
import openapi_client
from openapi_client.models.delete_event_type_output20240614 import DeleteEventTypeOutput20240614
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
    api_instance = openapi_client.EventTypesApi(api_client)
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-06-14`
    event_type_id = 3.4 # float | 
    authorization = 'authorization_example' # str | value must be `Bearer <token>` where `<token>` either managed user access token or api key prefixed with cal_

    try:
        # Delete an event type
        api_response = api_instance.event_types_controller20240614_delete_event_type(cal_api_version, event_type_id, authorization)
        print("The response of EventTypesApi->event_types_controller20240614_delete_event_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventTypesApi->event_types_controller20240614_delete_event_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cal_api_version** | **str**| Must be set to &#x60;2024-06-14&#x60; | 
 **event_type_id** | **float**|  | 
 **authorization** | **str**| value must be &#x60;Bearer &lt;token&gt;&#x60; where &#x60;&lt;token&gt;&#x60; either managed user access token or api key prefixed with cal_ | 

### Return type

[**DeleteEventTypeOutput20240614**](DeleteEventTypeOutput20240614.md)

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

# **event_types_controller20240614_get_event_type_by_id**
> GetEventTypeOutput20240614 event_types_controller20240614_get_event_type_by_id(cal_api_version, event_type_id, authorization)

Get an event type

### Example


```python
import openapi_client
from openapi_client.models.get_event_type_output20240614 import GetEventTypeOutput20240614
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
    api_instance = openapi_client.EventTypesApi(api_client)
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-06-14`
    event_type_id = 'event_type_id_example' # str | 
    authorization = 'authorization_example' # str | value must be `Bearer <token>` where `<token>` either managed user access token or api key prefixed with cal_

    try:
        # Get an event type
        api_response = api_instance.event_types_controller20240614_get_event_type_by_id(cal_api_version, event_type_id, authorization)
        print("The response of EventTypesApi->event_types_controller20240614_get_event_type_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventTypesApi->event_types_controller20240614_get_event_type_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cal_api_version** | **str**| Must be set to &#x60;2024-06-14&#x60; | 
 **event_type_id** | **str**|  | 
 **authorization** | **str**| value must be &#x60;Bearer &lt;token&gt;&#x60; where &#x60;&lt;token&gt;&#x60; either managed user access token or api key prefixed with cal_ | 

### Return type

[**GetEventTypeOutput20240614**](GetEventTypeOutput20240614.md)

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

# **event_types_controller20240614_get_event_types**
> GetEventTypesOutput20240614 event_types_controller20240614_get_event_types(cal_api_version, username=username, event_slug=event_slug, usernames=usernames)

Get all event types

### Example


```python
import openapi_client
from openapi_client.models.get_event_types_output20240614 import GetEventTypesOutput20240614
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
    api_instance = openapi_client.EventTypesApi(api_client)
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-06-14`
    username = 'username_example' # str | The username of the user to get event types for. If only username provided will get all event types. (optional)
    event_slug = 'event_slug_example' # str | Slug of event type to return. Notably, if eventSlug is provided then username must be provided too, because multiple users can have event with same slug. (optional)
    usernames = 'usernames_example' # str | Get dynamic event type for multiple usernames separated by comma. e.g `usernames=alice,bob` (optional)

    try:
        # Get all event types
        api_response = api_instance.event_types_controller20240614_get_event_types(cal_api_version, username=username, event_slug=event_slug, usernames=usernames)
        print("The response of EventTypesApi->event_types_controller20240614_get_event_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventTypesApi->event_types_controller20240614_get_event_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cal_api_version** | **str**| Must be set to &#x60;2024-06-14&#x60; | 
 **username** | **str**| The username of the user to get event types for. If only username provided will get all event types. | [optional] 
 **event_slug** | **str**| Slug of event type to return. Notably, if eventSlug is provided then username must be provided too, because multiple users can have event with same slug. | [optional] 
 **usernames** | **str**| Get dynamic event type for multiple usernames separated by comma. e.g &#x60;usernames&#x3D;alice,bob&#x60; | [optional] 

### Return type

[**GetEventTypesOutput20240614**](GetEventTypesOutput20240614.md)

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

# **event_types_controller20240614_update_event_type**
> UpdateEventTypeOutput20240614 event_types_controller20240614_update_event_type(cal_api_version, event_type_id, authorization, update_event_type_input20240614)

Update an event type

### Example


```python
import openapi_client
from openapi_client.models.update_event_type_input20240614 import UpdateEventTypeInput20240614
from openapi_client.models.update_event_type_output20240614 import UpdateEventTypeOutput20240614
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
    api_instance = openapi_client.EventTypesApi(api_client)
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-06-14`
    event_type_id = 3.4 # float | 
    authorization = 'authorization_example' # str | value must be `Bearer <token>` where `<token>` either managed user access token or api key prefixed with cal_
    update_event_type_input20240614 = openapi_client.UpdateEventTypeInput20240614() # UpdateEventTypeInput20240614 | 

    try:
        # Update an event type
        api_response = api_instance.event_types_controller20240614_update_event_type(cal_api_version, event_type_id, authorization, update_event_type_input20240614)
        print("The response of EventTypesApi->event_types_controller20240614_update_event_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventTypesApi->event_types_controller20240614_update_event_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cal_api_version** | **str**| Must be set to &#x60;2024-06-14&#x60; | 
 **event_type_id** | **float**|  | 
 **authorization** | **str**| value must be &#x60;Bearer &lt;token&gt;&#x60; where &#x60;&lt;token&gt;&#x60; either managed user access token or api key prefixed with cal_ | 
 **update_event_type_input20240614** | [**UpdateEventTypeInput20240614**](UpdateEventTypeInput20240614.md)|  | 

### Return type

[**UpdateEventTypeOutput20240614**](UpdateEventTypeOutput20240614.md)

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

