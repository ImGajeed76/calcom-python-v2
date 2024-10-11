# openapi_client.DestinationCalendarsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**destination_calendars_controller_update_destination_calendars**](DestinationCalendarsApi.md#destination_calendars_controller_update_destination_calendars) | **PUT** /v2/destination-calendars | Update destination calendars


# **destination_calendars_controller_update_destination_calendars**
> DestinationCalendarsOutputResponseDto destination_calendars_controller_update_destination_calendars(destination_calendars_input_body_dto)

Update destination calendars

### Example


```python
import openapi_client
from openapi_client.models.destination_calendars_input_body_dto import DestinationCalendarsInputBodyDto
from openapi_client.models.destination_calendars_output_response_dto import DestinationCalendarsOutputResponseDto
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
    api_instance = openapi_client.DestinationCalendarsApi(api_client)
    destination_calendars_input_body_dto = openapi_client.DestinationCalendarsInputBodyDto() # DestinationCalendarsInputBodyDto | 

    try:
        # Update destination calendars
        api_response = api_instance.destination_calendars_controller_update_destination_calendars(destination_calendars_input_body_dto)
        print("The response of DestinationCalendarsApi->destination_calendars_controller_update_destination_calendars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationCalendarsApi->destination_calendars_controller_update_destination_calendars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_calendars_input_body_dto** | [**DestinationCalendarsInputBodyDto**](DestinationCalendarsInputBodyDto.md)|  | 

### Return type

[**DestinationCalendarsOutputResponseDto**](DestinationCalendarsOutputResponseDto.md)

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

