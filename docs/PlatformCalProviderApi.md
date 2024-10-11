# openapi_client.PlatformCalProviderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cal_provider_controller_verify_access_token**](PlatformCalProviderApi.md#cal_provider_controller_verify_access_token) | **GET** /v2/provider/{clientId}/access-token | Verify an access token
[**cal_provider_controller_verify_client_id**](PlatformCalProviderApi.md#cal_provider_controller_verify_client_id) | **GET** /v2/provider/{clientId} | Get a provider


# **cal_provider_controller_verify_access_token**
> ProviderVerifyAccessTokenOutput cal_provider_controller_verify_access_token(client_id)

Verify an access token

### Example


```python
import openapi_client
from openapi_client.models.provider_verify_access_token_output import ProviderVerifyAccessTokenOutput
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
    api_instance = openapi_client.PlatformCalProviderApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Verify an access token
        api_response = api_instance.cal_provider_controller_verify_access_token(client_id)
        print("The response of PlatformCalProviderApi->cal_provider_controller_verify_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformCalProviderApi->cal_provider_controller_verify_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

[**ProviderVerifyAccessTokenOutput**](ProviderVerifyAccessTokenOutput.md)

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

# **cal_provider_controller_verify_client_id**
> ProviderVerifyClientOutput cal_provider_controller_verify_client_id(client_id)

Get a provider

### Example


```python
import openapi_client
from openapi_client.models.provider_verify_client_output import ProviderVerifyClientOutput
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
    api_instance = openapi_client.PlatformCalProviderApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Get a provider
        api_response = api_instance.cal_provider_controller_verify_client_id(client_id)
        print("The response of PlatformCalProviderApi->cal_provider_controller_verify_client_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformCalProviderApi->cal_provider_controller_verify_client_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

[**ProviderVerifyClientOutput**](ProviderVerifyClientOutput.md)

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

