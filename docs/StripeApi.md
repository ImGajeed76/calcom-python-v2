# openapi_client.StripeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stripe_controller_check**](StripeApi.md#stripe_controller_check) | **GET** /v2/stripe/check | Check stripe connection
[**stripe_controller_redirect**](StripeApi.md#stripe_controller_redirect) | **GET** /v2/stripe/connect | Get stripe connect URL
[**stripe_controller_save**](StripeApi.md#stripe_controller_save) | **GET** /v2/stripe/save | Save stripe credentials


# **stripe_controller_check**
> StripCredentialsCheckOutputResponseDto stripe_controller_check()

Check stripe connection

### Example


```python
import openapi_client
from openapi_client.models.strip_credentials_check_output_response_dto import StripCredentialsCheckOutputResponseDto
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
    api_instance = openapi_client.StripeApi(api_client)

    try:
        # Check stripe connection
        api_response = api_instance.stripe_controller_check()
        print("The response of StripeApi->stripe_controller_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->stripe_controller_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StripCredentialsCheckOutputResponseDto**](StripCredentialsCheckOutputResponseDto.md)

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

# **stripe_controller_redirect**
> StripConnectOutputResponseDto stripe_controller_redirect(authorization)

Get stripe connect URL

### Example


```python
import openapi_client
from openapi_client.models.strip_connect_output_response_dto import StripConnectOutputResponseDto
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
    api_instance = openapi_client.StripeApi(api_client)
    authorization = 'authorization_example' # str | 

    try:
        # Get stripe connect URL
        api_response = api_instance.stripe_controller_redirect(authorization)
        print("The response of StripeApi->stripe_controller_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->stripe_controller_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 

### Return type

[**StripConnectOutputResponseDto**](StripConnectOutputResponseDto.md)

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

# **stripe_controller_save**
> StripCredentialsSaveOutputResponseDto stripe_controller_save(state, code)

Save stripe credentials

### Example


```python
import openapi_client
from openapi_client.models.strip_credentials_save_output_response_dto import StripCredentialsSaveOutputResponseDto
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
    api_instance = openapi_client.StripeApi(api_client)
    state = 'state_example' # str | 
    code = 'code_example' # str | 

    try:
        # Save stripe credentials
        api_response = api_instance.stripe_controller_save(state, code)
        print("The response of StripeApi->stripe_controller_save:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->stripe_controller_save: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 
 **code** | **str**|  | 

### Return type

[**StripCredentialsSaveOutputResponseDto**](StripCredentialsSaveOutputResponseDto.md)

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

