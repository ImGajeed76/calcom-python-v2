# openapi_client.SelectedCalendarsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**selected_calendars_controller_add_selected_calendar**](SelectedCalendarsApi.md#selected_calendars_controller_add_selected_calendar) | **POST** /v2/selected-calendars | Add a selected calendar
[**selected_calendars_controller_remove_selected_calendar**](SelectedCalendarsApi.md#selected_calendars_controller_remove_selected_calendar) | **DELETE** /v2/selected-calendars | Delete a selected calendar


# **selected_calendars_controller_add_selected_calendar**
> SelectedCalendarOutputResponseDto selected_calendars_controller_add_selected_calendar(selected_calendars_input_dto)

Add a selected calendar

### Example


```python
import openapi_client
from openapi_client.models.selected_calendar_output_response_dto import SelectedCalendarOutputResponseDto
from openapi_client.models.selected_calendars_input_dto import SelectedCalendarsInputDto
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
    api_instance = openapi_client.SelectedCalendarsApi(api_client)
    selected_calendars_input_dto = openapi_client.SelectedCalendarsInputDto() # SelectedCalendarsInputDto | 

    try:
        # Add a selected calendar
        api_response = api_instance.selected_calendars_controller_add_selected_calendar(selected_calendars_input_dto)
        print("The response of SelectedCalendarsApi->selected_calendars_controller_add_selected_calendar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelectedCalendarsApi->selected_calendars_controller_add_selected_calendar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selected_calendars_input_dto** | [**SelectedCalendarsInputDto**](SelectedCalendarsInputDto.md)|  | 

### Return type

[**SelectedCalendarOutputResponseDto**](SelectedCalendarOutputResponseDto.md)

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

# **selected_calendars_controller_remove_selected_calendar**
> SelectedCalendarOutputResponseDto selected_calendars_controller_remove_selected_calendar(integration, external_id, credential_id)

Delete a selected calendar

### Example


```python
import openapi_client
from openapi_client.models.selected_calendar_output_response_dto import SelectedCalendarOutputResponseDto
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
    api_instance = openapi_client.SelectedCalendarsApi(api_client)
    integration = 'integration_example' # str | 
    external_id = 'external_id_example' # str | 
    credential_id = 'credential_id_example' # str | 

    try:
        # Delete a selected calendar
        api_response = api_instance.selected_calendars_controller_remove_selected_calendar(integration, external_id, credential_id)
        print("The response of SelectedCalendarsApi->selected_calendars_controller_remove_selected_calendar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelectedCalendarsApi->selected_calendars_controller_remove_selected_calendar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**|  | 
 **external_id** | **str**|  | 
 **credential_id** | **str**|  | 

### Return type

[**SelectedCalendarOutputResponseDto**](SelectedCalendarOutputResponseDto.md)

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

