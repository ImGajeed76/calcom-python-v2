# openapi_client.ManagedUsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_auth_flow_controller_refresh_access_token_0**](ManagedUsersApi.md#o_auth_flow_controller_refresh_access_token_0) | **POST** /v2/oauth/{clientId}/refresh | 


# **o_auth_flow_controller_refresh_access_token_0**
> KeysResponseDto o_auth_flow_controller_refresh_access_token_0(client_id, x_cal_secret_key, refresh_token_input)



### Example


```python
import openapi_client
from openapi_client.models.keys_response_dto import KeysResponseDto
from openapi_client.models.refresh_token_input import RefreshTokenInput
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
    api_instance = openapi_client.ManagedUsersApi(api_client)
    client_id = 'client_id_example' # str | 
    x_cal_secret_key = 'x_cal_secret_key_example' # str | OAuth client secret key.
    refresh_token_input = openapi_client.RefreshTokenInput() # RefreshTokenInput | 

    try:
        api_response = api_instance.o_auth_flow_controller_refresh_access_token_0(client_id, x_cal_secret_key, refresh_token_input)
        print("The response of ManagedUsersApi->o_auth_flow_controller_refresh_access_token_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedUsersApi->o_auth_flow_controller_refresh_access_token_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **x_cal_secret_key** | **str**| OAuth client secret key. | 
 **refresh_token_input** | [**RefreshTokenInput**](RefreshTokenInput.md)|  | 

### Return type

[**KeysResponseDto**](KeysResponseDto.md)

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

