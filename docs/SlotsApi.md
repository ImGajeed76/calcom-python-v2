# openapi_client.SlotsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slots_controller_delete_selected_slot**](SlotsApi.md#slots_controller_delete_selected_slot) | **DELETE** /v2/slots/selected-slot | Delete a selected slot
[**slots_controller_get_available_slots**](SlotsApi.md#slots_controller_get_available_slots) | **GET** /v2/slots/available | Get available slots
[**slots_controller_reserve_slot**](SlotsApi.md#slots_controller_reserve_slot) | **POST** /v2/slots/reserve | Reserve a slot


# **slots_controller_delete_selected_slot**
> SlotsControllerDeleteSelectedSlot200Response slots_controller_delete_selected_slot(uid)

Delete a selected slot

### Example


```python
import openapi_client
from openapi_client.models.slots_controller_delete_selected_slot200_response import SlotsControllerDeleteSelectedSlot200Response
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
    api_instance = openapi_client.SlotsApi(api_client)
    uid = 'e2a7bcf9-cc7b-40a0-80d3-657d391775a6' # str | Unique identifier for the slot to be removed.

    try:
        # Delete a selected slot
        api_response = api_instance.slots_controller_delete_selected_slot(uid)
        print("The response of SlotsApi->slots_controller_delete_selected_slot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlotsApi->slots_controller_delete_selected_slot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Unique identifier for the slot to be removed. | 

### Return type

[**SlotsControllerDeleteSelectedSlot200Response**](SlotsControllerDeleteSelectedSlot200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response deleting reserved slot by uid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slots_controller_get_available_slots**
> SlotsControllerGetAvailableSlots200Response slots_controller_get_available_slots(start_time, end_time, event_type_id, event_type_slug, username_list, duration)

Get available slots

### Example


```python
import openapi_client
from openapi_client.models.slots_controller_get_available_slots200_response import SlotsControllerGetAvailableSlots200Response
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
    api_instance = openapi_client.SlotsApi(api_client)
    start_time = '2022-06-14T00:00:00.000Z' # str | Start date string starting from which to fetch slots in UTC timezone.
    end_time = '2022-06-14T23:59:59.999Z' # str | End date string until which to fetch slots in UTC timezone.
    event_type_id = 100 # float | Event Type ID for which slots are being fetched.
    event_type_slug = 'event_type_slug_example' # str | Slug of the event type for which slots are being fetched.
    username_list = ['username_list_example'] # List[str] | Only for dynamic events - list of usernames for which slots are being fetched.
    duration = 3.4 # float | Only for dynamic events - length of returned slots.

    try:
        # Get available slots
        api_response = api_instance.slots_controller_get_available_slots(start_time, end_time, event_type_id, event_type_slug, username_list, duration)
        print("The response of SlotsApi->slots_controller_get_available_slots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlotsApi->slots_controller_get_available_slots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **str**| Start date string starting from which to fetch slots in UTC timezone. | 
 **end_time** | **str**| End date string until which to fetch slots in UTC timezone. | 
 **event_type_id** | **float**| Event Type ID for which slots are being fetched. | 
 **event_type_slug** | **str**| Slug of the event type for which slots are being fetched. | 
 **username_list** | [**List[str]**](str.md)| Only for dynamic events - list of usernames for which slots are being fetched. | 
 **duration** | **float**| Only for dynamic events - length of returned slots. | 

### Return type

[**SlotsControllerGetAvailableSlots200Response**](SlotsControllerGetAvailableSlots200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available time slots retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slots_controller_reserve_slot**
> SlotsControllerReserveSlot201Response slots_controller_reserve_slot(reserve_slot_input)

Reserve a slot

### Example


```python
import openapi_client
from openapi_client.models.reserve_slot_input import ReserveSlotInput
from openapi_client.models.slots_controller_reserve_slot201_response import SlotsControllerReserveSlot201Response
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
    api_instance = openapi_client.SlotsApi(api_client)
    reserve_slot_input = openapi_client.ReserveSlotInput() # ReserveSlotInput | 

    try:
        # Reserve a slot
        api_response = api_instance.slots_controller_reserve_slot(reserve_slot_input)
        print("The response of SlotsApi->slots_controller_reserve_slot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlotsApi->slots_controller_reserve_slot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reserve_slot_input** | [**ReserveSlotInput**](ReserveSlotInput.md)|  | 

### Return type

[**SlotsControllerReserveSlot201Response**](SlotsControllerReserveSlot201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response returning uid of reserved slot. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

