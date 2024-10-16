# openapi_client.TimezonesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timezones_controller_get_time_zones**](TimezonesApi.md#timezones_controller_get_time_zones) | **GET** /v2/timezones | Get all timezones


# **timezones_controller_get_time_zones**
> object timezones_controller_get_time_zones()

Get all timezones

### Example


```python
import openapi_client
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
    api_instance = openapi_client.TimezonesApi(api_client)

    try:
        # Get all timezones
        api_response = api_instance.timezones_controller_get_time_zones()
        print("The response of TimezonesApi->timezones_controller_get_time_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimezonesApi->timezones_controller_get_time_zones: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

