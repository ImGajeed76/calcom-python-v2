# openapi_client.OAuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_auth_flow_controller_authorize**](OAuthApi.md#o_auth_flow_controller_authorize) | **POST** /v2/oauth/{clientId}/authorize | Authorize an OAuth client
[**o_auth_flow_controller_exchange**](OAuthApi.md#o_auth_flow_controller_exchange) | **POST** /v2/oauth/{clientId}/exchange | Exchange authorization code for access tokens
[**o_auth_flow_controller_refresh_access_token**](OAuthApi.md#o_auth_flow_controller_refresh_access_token) | **POST** /v2/oauth/{clientId}/refresh | 


# **o_auth_flow_controller_authorize**
> o_auth_flow_controller_authorize(client_id, o_auth_authorize_input)

Authorize an OAuth client

Redirects the user to the specified 'redirect_uri' with an authorization code in query parameter if the client is authorized successfully. The code is then exchanged for access and refresh tokens via the `/exchange` endpoint.

### Example


```python
import openapi_client
from openapi_client.models.o_auth_authorize_input import OAuthAuthorizeInput
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
    api_instance = openapi_client.OAuthApi(api_client)
    client_id = 'client_id_example' # str | 
    o_auth_authorize_input = openapi_client.OAuthAuthorizeInput() # OAuthAuthorizeInput | 

    try:
        # Authorize an OAuth client
        api_instance.o_auth_flow_controller_authorize(client_id, o_auth_authorize_input)
    except Exception as e:
        print("Exception when calling OAuthApi->o_auth_flow_controller_authorize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **o_auth_authorize_input** | [**OAuthAuthorizeInput**](OAuthAuthorizeInput.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user is redirected to the &#39;redirect_uri&#39; with an authorization code in query parameter e.g. &#x60;redirectUri?code&#x3D;secretcode.&#x60; |  -  |
**400** | Bad request if the OAuth client is not found, if the redirect URI is invalid, or if the user has already authorized the client. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_auth_flow_controller_exchange**
> KeysResponseDto o_auth_flow_controller_exchange(authorization, client_id, exchange_authorization_code_input)

Exchange authorization code for access tokens

Exchanges the authorization code received from the `/authorize` endpoint for access and refresh tokens. The authorization code should be provided in the 'Authorization' header prefixed with 'Bearer '.

### Example


```python
import openapi_client
from openapi_client.models.exchange_authorization_code_input import ExchangeAuthorizationCodeInput
from openapi_client.models.keys_response_dto import KeysResponseDto
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
    api_instance = openapi_client.OAuthApi(api_client)
    authorization = 'authorization_example' # str | 
    client_id = 'client_id_example' # str | 
    exchange_authorization_code_input = openapi_client.ExchangeAuthorizationCodeInput() # ExchangeAuthorizationCodeInput | 

    try:
        # Exchange authorization code for access tokens
        api_response = api_instance.o_auth_flow_controller_exchange(authorization, client_id, exchange_authorization_code_input)
        print("The response of OAuthApi->o_auth_flow_controller_exchange:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->o_auth_flow_controller_exchange: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **str**|  | 
 **exchange_authorization_code_input** | [**ExchangeAuthorizationCodeInput**](ExchangeAuthorizationCodeInput.md)|  | 

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
**200** | Successfully exchanged authorization code for access and refresh tokens. |  -  |
**400** | Bad request if the authorization code is missing, invalid, or if the client ID and secret do not match. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_auth_flow_controller_refresh_access_token**
> KeysResponseDto o_auth_flow_controller_refresh_access_token(client_id, x_cal_secret_key, refresh_token_input)



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
    api_instance = openapi_client.OAuthApi(api_client)
    client_id = 'client_id_example' # str | 
    x_cal_secret_key = 'x_cal_secret_key_example' # str | OAuth client secret key.
    refresh_token_input = openapi_client.RefreshTokenInput() # RefreshTokenInput | 

    try:
        api_response = api_instance.o_auth_flow_controller_refresh_access_token(client_id, x_cal_secret_key, refresh_token_input)
        print("The response of OAuthApi->o_auth_flow_controller_refresh_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->o_auth_flow_controller_refresh_access_token: %s\n" % e)
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

