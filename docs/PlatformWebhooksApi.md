# openapi_client.PlatformWebhooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_auth_client_webhooks_controller_create_o_auth_client_webhook**](PlatformWebhooksApi.md#o_auth_client_webhooks_controller_create_o_auth_client_webhook) | **POST** /v2/oauth-clients/{clientId}/webhooks | Create a webhook
[**o_auth_client_webhooks_controller_delete_all_o_auth_client_webhooks**](PlatformWebhooksApi.md#o_auth_client_webhooks_controller_delete_all_o_auth_client_webhooks) | **DELETE** /v2/oauth-clients/{clientId}/webhooks | Delete all webhooks
[**o_auth_client_webhooks_controller_delete_o_auth_client_webhook**](PlatformWebhooksApi.md#o_auth_client_webhooks_controller_delete_o_auth_client_webhook) | **DELETE** /v2/oauth-clients/{clientId}/webhooks/{webhookId} | Delete a webhook
[**o_auth_client_webhooks_controller_get_o_auth_client_webhook**](PlatformWebhooksApi.md#o_auth_client_webhooks_controller_get_o_auth_client_webhook) | **GET** /v2/oauth-clients/{clientId}/webhooks/{webhookId} | Get a webhook
[**o_auth_client_webhooks_controller_get_o_auth_client_webhooks**](PlatformWebhooksApi.md#o_auth_client_webhooks_controller_get_o_auth_client_webhooks) | **GET** /v2/oauth-clients/{clientId}/webhooks | Get all webhooks
[**o_auth_client_webhooks_controller_update_o_auth_client_webhook**](PlatformWebhooksApi.md#o_auth_client_webhooks_controller_update_o_auth_client_webhook) | **PATCH** /v2/oauth-clients/{clientId}/webhooks/{webhookId} | Update a webhook


# **o_auth_client_webhooks_controller_create_o_auth_client_webhook**
> OAuthClientWebhookOutputResponseDto o_auth_client_webhooks_controller_create_o_auth_client_webhook(client_id, create_webhook_input_dto)

Create a webhook

### Example


```python
import openapi_client
from openapi_client.models.create_webhook_input_dto import CreateWebhookInputDto
from openapi_client.models.o_auth_client_webhook_output_response_dto import OAuthClientWebhookOutputResponseDto
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
    api_instance = openapi_client.PlatformWebhooksApi(api_client)
    client_id = 'client_id_example' # str | 
    create_webhook_input_dto = openapi_client.CreateWebhookInputDto() # CreateWebhookInputDto | 

    try:
        # Create a webhook
        api_response = api_instance.o_auth_client_webhooks_controller_create_o_auth_client_webhook(client_id, create_webhook_input_dto)
        print("The response of PlatformWebhooksApi->o_auth_client_webhooks_controller_create_o_auth_client_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWebhooksApi->o_auth_client_webhooks_controller_create_o_auth_client_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **create_webhook_input_dto** | [**CreateWebhookInputDto**](CreateWebhookInputDto.md)|  | 

### Return type

[**OAuthClientWebhookOutputResponseDto**](OAuthClientWebhookOutputResponseDto.md)

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

# **o_auth_client_webhooks_controller_delete_all_o_auth_client_webhooks**
> DeleteManyWebhooksOutputResponseDto o_auth_client_webhooks_controller_delete_all_o_auth_client_webhooks(client_id)

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
    api_instance = openapi_client.PlatformWebhooksApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Delete all webhooks
        api_response = api_instance.o_auth_client_webhooks_controller_delete_all_o_auth_client_webhooks(client_id)
        print("The response of PlatformWebhooksApi->o_auth_client_webhooks_controller_delete_all_o_auth_client_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWebhooksApi->o_auth_client_webhooks_controller_delete_all_o_auth_client_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

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

# **o_auth_client_webhooks_controller_delete_o_auth_client_webhook**
> OAuthClientWebhookOutputResponseDto o_auth_client_webhooks_controller_delete_o_auth_client_webhook()

Delete a webhook

### Example


```python
import openapi_client
from openapi_client.models.o_auth_client_webhook_output_response_dto import OAuthClientWebhookOutputResponseDto
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
    api_instance = openapi_client.PlatformWebhooksApi(api_client)

    try:
        # Delete a webhook
        api_response = api_instance.o_auth_client_webhooks_controller_delete_o_auth_client_webhook()
        print("The response of PlatformWebhooksApi->o_auth_client_webhooks_controller_delete_o_auth_client_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWebhooksApi->o_auth_client_webhooks_controller_delete_o_auth_client_webhook: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OAuthClientWebhookOutputResponseDto**](OAuthClientWebhookOutputResponseDto.md)

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

# **o_auth_client_webhooks_controller_get_o_auth_client_webhook**
> OAuthClientWebhookOutputResponseDto o_auth_client_webhooks_controller_get_o_auth_client_webhook()

Get a webhook

### Example


```python
import openapi_client
from openapi_client.models.o_auth_client_webhook_output_response_dto import OAuthClientWebhookOutputResponseDto
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
    api_instance = openapi_client.PlatformWebhooksApi(api_client)

    try:
        # Get a webhook
        api_response = api_instance.o_auth_client_webhooks_controller_get_o_auth_client_webhook()
        print("The response of PlatformWebhooksApi->o_auth_client_webhooks_controller_get_o_auth_client_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWebhooksApi->o_auth_client_webhooks_controller_get_o_auth_client_webhook: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OAuthClientWebhookOutputResponseDto**](OAuthClientWebhookOutputResponseDto.md)

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

# **o_auth_client_webhooks_controller_get_o_auth_client_webhooks**
> OAuthClientWebhooksOutputResponseDto o_auth_client_webhooks_controller_get_o_auth_client_webhooks(client_id, take=take, skip=skip)

Get all webhooks

### Example


```python
import openapi_client
from openapi_client.models.o_auth_client_webhooks_output_response_dto import OAuthClientWebhooksOutputResponseDto
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
    api_instance = openapi_client.PlatformWebhooksApi(api_client)
    client_id = 'client_id_example' # str | 
    take = 10 # float | The number of items to return (optional)
    skip = 0 # float | The number of items to skip (optional)

    try:
        # Get all webhooks
        api_response = api_instance.o_auth_client_webhooks_controller_get_o_auth_client_webhooks(client_id, take=take, skip=skip)
        print("The response of PlatformWebhooksApi->o_auth_client_webhooks_controller_get_o_auth_client_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWebhooksApi->o_auth_client_webhooks_controller_get_o_auth_client_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **take** | **float**| The number of items to return | [optional] 
 **skip** | **float**| The number of items to skip | [optional] 

### Return type

[**OAuthClientWebhooksOutputResponseDto**](OAuthClientWebhooksOutputResponseDto.md)

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

# **o_auth_client_webhooks_controller_update_o_auth_client_webhook**
> OAuthClientWebhookOutputResponseDto o_auth_client_webhooks_controller_update_o_auth_client_webhook(webhook_id, update_webhook_input_dto)

Update a webhook

### Example


```python
import openapi_client
from openapi_client.models.o_auth_client_webhook_output_response_dto import OAuthClientWebhookOutputResponseDto
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
    api_instance = openapi_client.PlatformWebhooksApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    update_webhook_input_dto = openapi_client.UpdateWebhookInputDto() # UpdateWebhookInputDto | 

    try:
        # Update a webhook
        api_response = api_instance.o_auth_client_webhooks_controller_update_o_auth_client_webhook(webhook_id, update_webhook_input_dto)
        print("The response of PlatformWebhooksApi->o_auth_client_webhooks_controller_update_o_auth_client_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWebhooksApi->o_auth_client_webhooks_controller_update_o_auth_client_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **update_webhook_input_dto** | [**UpdateWebhookInputDto**](UpdateWebhookInputDto.md)|  | 

### Return type

[**OAuthClientWebhookOutputResponseDto**](OAuthClientWebhookOutputResponseDto.md)

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

