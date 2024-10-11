# openapi_client.MeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**me_controller_get_me**](MeApi.md#me_controller_get_me) | **GET** /v2/me | Get my profile
[**me_controller_update_me**](MeApi.md#me_controller_update_me) | **PATCH** /v2/me | Update my profile


# **me_controller_get_me**
> GetMeOutput me_controller_get_me()

Get my profile

### Example


```python
import openapi_client
from openapi_client.models.get_me_output import GetMeOutput
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
    api_instance = openapi_client.MeApi(api_client)

    try:
        # Get my profile
        api_response = api_instance.me_controller_get_me()
        print("The response of MeApi->me_controller_get_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->me_controller_get_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMeOutput**](GetMeOutput.md)

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

# **me_controller_update_me**
> UpdateMeOutput me_controller_update_me(update_managed_user_input)

Update my profile

### Example


```python
import openapi_client
from openapi_client.models.update_managed_user_input import UpdateManagedUserInput
from openapi_client.models.update_me_output import UpdateMeOutput
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
    api_instance = openapi_client.MeApi(api_client)
    update_managed_user_input = openapi_client.UpdateManagedUserInput() # UpdateManagedUserInput | 

    try:
        # Update my profile
        api_response = api_instance.me_controller_update_me(update_managed_user_input)
        print("The response of MeApi->me_controller_update_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->me_controller_update_me: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_managed_user_input** | [**UpdateManagedUserInput**](UpdateManagedUserInput.md)|  | 

### Return type

[**UpdateMeOutput**](UpdateMeOutput.md)

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

