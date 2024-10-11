# openapi_client.WebhooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooks_controller_create_webhook**](WebhooksApi.md#webhooks_controller_create_webhook) | **POST** /v2/webhooks | Create a webhook
[**webhooks_controller_delete_webhook**](WebhooksApi.md#webhooks_controller_delete_webhook) | **DELETE** /v2/webhooks/{webhookId} | Delete a webhook
[**webhooks_controller_get_webhook**](WebhooksApi.md#webhooks_controller_get_webhook) | **GET** /v2/webhooks/{webhookId} | Get a webhook
[**webhooks_controller_get_webhooks**](WebhooksApi.md#webhooks_controller_get_webhooks) | **GET** /v2/webhooks | Get all webooks (paginated)
[**webhooks_controller_update_webhook**](WebhooksApi.md#webhooks_controller_update_webhook) | **PATCH** /v2/webhooks/{webhookId} | Update a webhook


# **webhooks_controller_create_webhook**
> UserWebhookOutputResponseDto webhooks_controller_create_webhook(create_webhook_input_dto)

Create a webhook

### Example


```python
import openapi_client
from openapi_client.models.create_webhook_input_dto import CreateWebhookInputDto
from openapi_client.models.user_webhook_output_response_dto import UserWebhookOutputResponseDto
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
    api_instance = openapi_client.WebhooksApi(api_client)
    create_webhook_input_dto = openapi_client.CreateWebhookInputDto() # CreateWebhookInputDto | 

    try:
        # Create a webhook
        api_response = api_instance.webhooks_controller_create_webhook(create_webhook_input_dto)
        print("The response of WebhooksApi->webhooks_controller_create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_controller_create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_input_dto** | [**CreateWebhookInputDto**](CreateWebhookInputDto.md)|  | 

### Return type

[**UserWebhookOutputResponseDto**](UserWebhookOutputResponseDto.md)

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

# **webhooks_controller_delete_webhook**
> UserWebhookOutputResponseDto webhooks_controller_delete_webhook(webhook_id)

Delete a webhook

### Example


```python
import openapi_client
from openapi_client.models.user_webhook_output_response_dto import UserWebhookOutputResponseDto
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
    api_instance = openapi_client.WebhooksApi(api_client)
    webhook_id = 'webhook_id_example' # str | 

    try:
        # Delete a webhook
        api_response = api_instance.webhooks_controller_delete_webhook(webhook_id)
        print("The response of WebhooksApi->webhooks_controller_delete_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_controller_delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 

### Return type

[**UserWebhookOutputResponseDto**](UserWebhookOutputResponseDto.md)

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

# **webhooks_controller_get_webhook**
> UserWebhookOutputResponseDto webhooks_controller_get_webhook()

Get a webhook

### Example


```python
import openapi_client
from openapi_client.models.user_webhook_output_response_dto import UserWebhookOutputResponseDto
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
    api_instance = openapi_client.WebhooksApi(api_client)

    try:
        # Get a webhook
        api_response = api_instance.webhooks_controller_get_webhook()
        print("The response of WebhooksApi->webhooks_controller_get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_controller_get_webhook: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserWebhookOutputResponseDto**](UserWebhookOutputResponseDto.md)

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

# **webhooks_controller_get_webhooks**
> UserWebhooksOutputResponseDto webhooks_controller_get_webhooks(take=take, skip=skip)

Get all webooks (paginated)

### Example


```python
import openapi_client
from openapi_client.models.user_webhooks_output_response_dto import UserWebhooksOutputResponseDto
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
    api_instance = openapi_client.WebhooksApi(api_client)
    take = 10 # float | The number of items to return (optional)
    skip = 0 # float | The number of items to skip (optional)

    try:
        # Get all webooks (paginated)
        api_response = api_instance.webhooks_controller_get_webhooks(take=take, skip=skip)
        print("The response of WebhooksApi->webhooks_controller_get_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_controller_get_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **float**| The number of items to return | [optional] 
 **skip** | **float**| The number of items to skip | [optional] 

### Return type

[**UserWebhooksOutputResponseDto**](UserWebhooksOutputResponseDto.md)

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

# **webhooks_controller_update_webhook**
> UserWebhookOutputResponseDto webhooks_controller_update_webhook(webhook_id, update_webhook_input_dto)

Update a webhook

### Example


```python
import openapi_client
from openapi_client.models.update_webhook_input_dto import UpdateWebhookInputDto
from openapi_client.models.user_webhook_output_response_dto import UserWebhookOutputResponseDto
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
    api_instance = openapi_client.WebhooksApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    update_webhook_input_dto = openapi_client.UpdateWebhookInputDto() # UpdateWebhookInputDto | 

    try:
        # Update a webhook
        api_response = api_instance.webhooks_controller_update_webhook(webhook_id, update_webhook_input_dto)
        print("The response of WebhooksApi->webhooks_controller_update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->webhooks_controller_update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **update_webhook_input_dto** | [**UpdateWebhookInputDto**](UpdateWebhookInputDto.md)|  | 

### Return type

[**UserWebhookOutputResponseDto**](UserWebhookOutputResponseDto.md)

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

