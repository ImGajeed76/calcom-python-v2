# openapi_client.EventTypesWebhooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_type_webhooks_controller_create_event_type_webhook**](EventTypesWebhooksApi.md#event_type_webhooks_controller_create_event_type_webhook) | **POST** /v2/event-types/{eventTypeId}/webhooks | Create a webhook
[**event_type_webhooks_controller_delete_all_event_type_webhooks**](EventTypesWebhooksApi.md#event_type_webhooks_controller_delete_all_event_type_webhooks) | **DELETE** /v2/event-types/{eventTypeId}/webhooks | Delete all webhooks
[**event_type_webhooks_controller_delete_event_type_webhook**](EventTypesWebhooksApi.md#event_type_webhooks_controller_delete_event_type_webhook) | **DELETE** /v2/event-types/{eventTypeId}/webhooks/{webhookId} | Delete a webhook
[**event_type_webhooks_controller_get_event_type_webhook**](EventTypesWebhooksApi.md#event_type_webhooks_controller_get_event_type_webhook) | **GET** /v2/event-types/{eventTypeId}/webhooks/{webhookId} | Get a webhook
[**event_type_webhooks_controller_get_event_type_webhooks**](EventTypesWebhooksApi.md#event_type_webhooks_controller_get_event_type_webhooks) | **GET** /v2/event-types/{eventTypeId}/webhooks | Get all webhooks
[**event_type_webhooks_controller_update_event_type_webhook**](EventTypesWebhooksApi.md#event_type_webhooks_controller_update_event_type_webhook) | **PATCH** /v2/event-types/{eventTypeId}/webhooks/{webhookId} | Update a webhook


# **event_type_webhooks_controller_create_event_type_webhook**
> EventTypeWebhookOutputResponseDto event_type_webhooks_controller_create_event_type_webhook(event_type_id, create_webhook_input_dto)

Create a webhook

### Example


```python
import openapi_client
from openapi_client.models.create_webhook_input_dto import CreateWebhookInputDto
from openapi_client.models.event_type_webhook_output_response_dto import EventTypeWebhookOutputResponseDto
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
    api_instance = openapi_client.EventTypesWebhooksApi(api_client)
    event_type_id = 3.4 # float | 
    create_webhook_input_dto = openapi_client.CreateWebhookInputDto() # CreateWebhookInputDto | 

    try:
        # Create a webhook
        api_response = api_instance.event_type_webhooks_controller_create_event_type_webhook(event_type_id, create_webhook_input_dto)
        print("The response of EventTypesWebhooksApi->event_type_webhooks_controller_create_event_type_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventTypesWebhooksApi->event_type_webhooks_controller_create_event_type_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type_id** | **float**|  | 
 **create_webhook_input_dto** | [**CreateWebhookInputDto**](CreateWebhookInputDto.md)|  | 

### Return type

[**EventTypeWebhookOutputResponseDto**](EventTypeWebhookOutputResponseDto.md)

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

# **event_type_webhooks_controller_delete_all_event_type_webhooks**
> DeleteManyWebhooksOutputResponseDto event_type_webhooks_controller_delete_all_event_type_webhooks(event_type_id)

Delete all webhooks

### Example


```python
import openapi_client
from openapi_client.models.delete_many_webhooks_output_response_dto import DeleteManyWebhooksOutputResponseDto
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
    api_instance = openapi_client.EventTypesWebhooksApi(api_client)
    event_type_id = 3.4 # float | 

    try:
        # Delete all webhooks
        api_response = api_instance.event_type_webhooks_controller_delete_all_event_type_webhooks(event_type_id)
        print("The response of EventTypesWebhooksApi->event_type_webhooks_controller_delete_all_event_type_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventTypesWebhooksApi->event_type_webhooks_controller_delete_all_event_type_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type_id** | **float**|  | 

### Return type

[**DeleteManyWebhooksOutputResponseDto**](DeleteManyWebhooksOutputResponseDto.md)

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

# **event_type_webhooks_controller_delete_event_type_webhook**
> EventTypeWebhookOutputResponseDto event_type_webhooks_controller_delete_event_type_webhook()

Delete a webhook

### Example


```python
import openapi_client
from openapi_client.models.event_type_webhook_output_response_dto import EventTypeWebhookOutputResponseDto
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
    api_instance = openapi_client.EventTypesWebhooksApi(api_client)

    try:
        # Delete a webhook
        api_response = api_instance.event_type_webhooks_controller_delete_event_type_webhook()
        print("The response of EventTypesWebhooksApi->event_type_webhooks_controller_delete_event_type_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventTypesWebhooksApi->event_type_webhooks_controller_delete_event_type_webhook: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EventTypeWebhookOutputResponseDto**](EventTypeWebhookOutputResponseDto.md)

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

# **event_type_webhooks_controller_get_event_type_webhook**
> EventTypeWebhookOutputResponseDto event_type_webhooks_controller_get_event_type_webhook()

Get a webhook

### Example


```python
import openapi_client
from openapi_client.models.event_type_webhook_output_response_dto import EventTypeWebhookOutputResponseDto
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
    api_instance = openapi_client.EventTypesWebhooksApi(api_client)

    try:
        # Get a webhook
        api_response = api_instance.event_type_webhooks_controller_get_event_type_webhook()
        print("The response of EventTypesWebhooksApi->event_type_webhooks_controller_get_event_type_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventTypesWebhooksApi->event_type_webhooks_controller_get_event_type_webhook: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EventTypeWebhookOutputResponseDto**](EventTypeWebhookOutputResponseDto.md)

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

# **event_type_webhooks_controller_get_event_type_webhooks**
> EventTypeWebhooksOutputResponseDto event_type_webhooks_controller_get_event_type_webhooks(event_type_id, take=take, skip=skip)

Get all webhooks

### Example


```python
import openapi_client
from openapi_client.models.event_type_webhooks_output_response_dto import EventTypeWebhooksOutputResponseDto
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
    api_instance = openapi_client.EventTypesWebhooksApi(api_client)
    event_type_id = 3.4 # float | 
    take = 10 # float | The number of items to return (optional)
    skip = 0 # float | The number of items to skip (optional)

    try:
        # Get all webhooks
        api_response = api_instance.event_type_webhooks_controller_get_event_type_webhooks(event_type_id, take=take, skip=skip)
        print("The response of EventTypesWebhooksApi->event_type_webhooks_controller_get_event_type_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventTypesWebhooksApi->event_type_webhooks_controller_get_event_type_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type_id** | **float**|  | 
 **take** | **float**| The number of items to return | [optional] 
 **skip** | **float**| The number of items to skip | [optional] 

### Return type

[**EventTypeWebhooksOutputResponseDto**](EventTypeWebhooksOutputResponseDto.md)

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

# **event_type_webhooks_controller_update_event_type_webhook**
> EventTypeWebhookOutputResponseDto event_type_webhooks_controller_update_event_type_webhook(webhook_id, update_webhook_input_dto)

Update a webhook

### Example


```python
import openapi_client
from openapi_client.models.event_type_webhook_output_response_dto import EventTypeWebhookOutputResponseDto
from openapi_client.models.update_webhook_input_dto import UpdateWebhookInputDto
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
    api_instance = openapi_client.EventTypesWebhooksApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    update_webhook_input_dto = openapi_client.UpdateWebhookInputDto() # UpdateWebhookInputDto | 

    try:
        # Update a webhook
        api_response = api_instance.event_type_webhooks_controller_update_event_type_webhook(webhook_id, update_webhook_input_dto)
        print("The response of EventTypesWebhooksApi->event_type_webhooks_controller_update_event_type_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventTypesWebhooksApi->event_type_webhooks_controller_update_event_type_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **update_webhook_input_dto** | [**UpdateWebhookInputDto**](UpdateWebhookInputDto.md)|  | 

### Return type

[**EventTypeWebhookOutputResponseDto**](EventTypeWebhookOutputResponseDto.md)

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

