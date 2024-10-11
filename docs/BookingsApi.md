# openapi_client.BookingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bookings_controller20240813_cancel_booking**](BookingsApi.md#bookings_controller20240813_cancel_booking) | **POST** /v2/bookings/{bookingUid}/cancel | Cancel a booking
[**bookings_controller20240813_create_booking**](BookingsApi.md#bookings_controller20240813_create_booking) | **POST** /v2/bookings | Create a booking
[**bookings_controller20240813_get_booking**](BookingsApi.md#bookings_controller20240813_get_booking) | **GET** /v2/bookings/{bookingUid} | Get a booking
[**bookings_controller20240813_get_bookings**](BookingsApi.md#bookings_controller20240813_get_bookings) | **GET** /v2/bookings | Get all bookings
[**bookings_controller20240813_mark_no_show**](BookingsApi.md#bookings_controller20240813_mark_no_show) | **POST** /v2/bookings/{bookingUid}/mark-absent | Mark a booking absence
[**bookings_controller20240813_reschedule_booking**](BookingsApi.md#bookings_controller20240813_reschedule_booking) | **POST** /v2/bookings/{bookingUid}/reschedule | Reschedule a booking


# **bookings_controller20240813_cancel_booking**
> CancelBookingOutput20240813 bookings_controller20240813_cancel_booking(cal_api_version, booking_uid, cancel_booking_input20240813)

Cancel a booking

### Example


```python
import openapi_client
from openapi_client.models.cancel_booking_input20240813 import CancelBookingInput20240813
from openapi_client.models.cancel_booking_output20240813 import CancelBookingOutput20240813
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
    api_instance = openapi_client.BookingsApi(api_client)
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-08-13`
    booking_uid = 'booking_uid_example' # str | 
    cancel_booking_input20240813 = openapi_client.CancelBookingInput20240813() # CancelBookingInput20240813 | 

    try:
        # Cancel a booking
        api_response = api_instance.bookings_controller20240813_cancel_booking(cal_api_version, booking_uid, cancel_booking_input20240813)
        print("The response of BookingsApi->bookings_controller20240813_cancel_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookingsApi->bookings_controller20240813_cancel_booking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cal_api_version** | **str**| Must be set to &#x60;2024-08-13&#x60; | 
 **booking_uid** | **str**|  | 
 **cancel_booking_input20240813** | [**CancelBookingInput20240813**](CancelBookingInput20240813.md)|  | 

### Return type

[**CancelBookingOutput20240813**](CancelBookingOutput20240813.md)

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

# **bookings_controller20240813_create_booking**
> CreateBookingOutput20240813 bookings_controller20240813_create_booking(cal_api_version, bookings_controller20240813_create_booking_request)

Create a booking

       POST /v2/bookings is used to create regular bookings, recurring bookings and instant bookings. The request bodies for all 3 are almost the same except:       If eventTypeId in the request body is id of a regular event, then regular booking is created.        If it is an id of a recurring event type, then recurring booking is created.        Meaning that the request bodies are equal but the outcome depends on what kind of event type it is with the goal of making it as seamless for developers as possible.        For team event types it is possible to create instant meeting. To do that just pass `\"instant\": true` to the request body.        The start needs to be in UTC aka if the timezone is GMT+2 in Rome and meeting should start at 11, then UTC time should have hours 09:00 aka without time zone.       

### Example


```python
import openapi_client
from openapi_client.models.bookings_controller20240813_create_booking_request import BookingsController20240813CreateBookingRequest
from openapi_client.models.create_booking_output20240813 import CreateBookingOutput20240813
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
    api_instance = openapi_client.BookingsApi(api_client)
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-08-13`
    bookings_controller20240813_create_booking_request = openapi_client.BookingsController20240813CreateBookingRequest() # BookingsController20240813CreateBookingRequest | Accepts different types of booking input: CreateBookingInput_2024_08_13, CreateInstantBookingInput_2024_08_13, or CreateRecurringBookingInput_2024_08_13

    try:
        # Create a booking
        api_response = api_instance.bookings_controller20240813_create_booking(cal_api_version, bookings_controller20240813_create_booking_request)
        print("The response of BookingsApi->bookings_controller20240813_create_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookingsApi->bookings_controller20240813_create_booking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cal_api_version** | **str**| Must be set to &#x60;2024-08-13&#x60; | 
 **bookings_controller20240813_create_booking_request** | [**BookingsController20240813CreateBookingRequest**](BookingsController20240813CreateBookingRequest.md)| Accepts different types of booking input: CreateBookingInput_2024_08_13, CreateInstantBookingInput_2024_08_13, or CreateRecurringBookingInput_2024_08_13 | 

### Return type

[**CreateBookingOutput20240813**](CreateBookingOutput20240813.md)

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

# **bookings_controller20240813_get_booking**
> GetBookingOutput20240813 bookings_controller20240813_get_booking(cal_api_version, booking_uid)

Get a booking

`:bookingUid` can be        1. uid of a normal booking        2. uid of one of the recurring booking recurrences        3. uid of recurring booking which will return an array of all recurring booking recurrences (stored as recurringBookingUid on one of the individual recurrences).

### Example


```python
import openapi_client
from openapi_client.models.get_booking_output20240813 import GetBookingOutput20240813
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
    api_instance = openapi_client.BookingsApi(api_client)
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-08-13`
    booking_uid = 'booking_uid_example' # str | 

    try:
        # Get a booking
        api_response = api_instance.bookings_controller20240813_get_booking(cal_api_version, booking_uid)
        print("The response of BookingsApi->bookings_controller20240813_get_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookingsApi->bookings_controller20240813_get_booking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cal_api_version** | **str**| Must be set to &#x60;2024-08-13&#x60; | 
 **booking_uid** | **str**|  | 

### Return type

[**GetBookingOutput20240813**](GetBookingOutput20240813.md)

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

# **bookings_controller20240813_get_bookings**
> GetBookingsOutput20240813 bookings_controller20240813_get_bookings(cal_api_version, authorization, status=status, attendee_email=attendee_email, attendee_name=attendee_name, event_type_ids=event_type_ids, event_type_id=event_type_id, teams_ids=teams_ids, team_id=team_id, after_start=after_start, before_end=before_end, sort_start=sort_start, sort_end=sort_end, sort_created=sort_created, take=take, skip=skip)

Get all bookings

### Example


```python
import openapi_client
from openapi_client.models.get_bookings_output20240813 import GetBookingsOutput20240813
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
    api_instance = openapi_client.BookingsApi(api_client)
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-08-13`
    authorization = 'authorization_example' # str | value must be `Bearer <token>` where `<token>` either managed user access token or api key prefixed with cal_
    status = ['?status=upcoming,past'] # List[str] | Filter bookings by status. If you want to filter by multiple statuses, separate them with a comma. (optional)
    attendee_email = 'example@domain.com' # str | Filter bookings by the attendee's email address. (optional)
    attendee_name = 'John Doe' # str | Filter bookings by the attendee's name. (optional)
    event_type_ids = '?eventTypeIds=100,200' # str | Filter bookings by event type ids belonging to the user. Event type ids must be separated by a comma. (optional)
    event_type_id = '?eventTypeId=100' # str | Filter bookings by event type id belonging to the user. (optional)
    teams_ids = '?teamIds=50,60' # str | Filter bookings by team ids that user is part of. Team ids must be separated by a comma. (optional)
    team_id = '?teamId=50' # str | Filter bookings by team id that user is part of (optional)
    after_start = '?afterStart=2025-03-07T10:00:00.000Z' # str | Filter bookings with start after this date string. (optional)
    before_end = '?beforeEnd=2025-03-07T11:00:00.000Z' # str | Filter bookings with end before this date string. (optional)
    sort_start = '?sortStart=asc OR ?sortStart=desc' # str | Sort results by their start time in ascending or descending order. (optional)
    sort_end = '?sortEnd=asc OR ?sortEnd=desc' # str | Sort results by their end time in ascending or descending order. (optional)
    sort_created = '?sortEnd=asc OR ?sortEnd=desc' # str | Sort results by their creation time (when booking was made) in ascending or descending order. (optional)
    take = 10 # float | The number of items to return (optional)
    skip = 0 # float | The number of items to skip (optional)

    try:
        # Get all bookings
        api_response = api_instance.bookings_controller20240813_get_bookings(cal_api_version, authorization, status=status, attendee_email=attendee_email, attendee_name=attendee_name, event_type_ids=event_type_ids, event_type_id=event_type_id, teams_ids=teams_ids, team_id=team_id, after_start=after_start, before_end=before_end, sort_start=sort_start, sort_end=sort_end, sort_created=sort_created, take=take, skip=skip)
        print("The response of BookingsApi->bookings_controller20240813_get_bookings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookingsApi->bookings_controller20240813_get_bookings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cal_api_version** | **str**| Must be set to &#x60;2024-08-13&#x60; | 
 **authorization** | **str**| value must be &#x60;Bearer &lt;token&gt;&#x60; where &#x60;&lt;token&gt;&#x60; either managed user access token or api key prefixed with cal_ | 
 **status** | [**List[str]**](str.md)| Filter bookings by status. If you want to filter by multiple statuses, separate them with a comma. | [optional] 
 **attendee_email** | **str**| Filter bookings by the attendee&#39;s email address. | [optional] 
 **attendee_name** | **str**| Filter bookings by the attendee&#39;s name. | [optional] 
 **event_type_ids** | **str**| Filter bookings by event type ids belonging to the user. Event type ids must be separated by a comma. | [optional] 
 **event_type_id** | **str**| Filter bookings by event type id belonging to the user. | [optional] 
 **teams_ids** | **str**| Filter bookings by team ids that user is part of. Team ids must be separated by a comma. | [optional] 
 **team_id** | **str**| Filter bookings by team id that user is part of | [optional] 
 **after_start** | **str**| Filter bookings with start after this date string. | [optional] 
 **before_end** | **str**| Filter bookings with end before this date string. | [optional] 
 **sort_start** | **str**| Sort results by their start time in ascending or descending order. | [optional] 
 **sort_end** | **str**| Sort results by their end time in ascending or descending order. | [optional] 
 **sort_created** | **str**| Sort results by their creation time (when booking was made) in ascending or descending order. | [optional] 
 **take** | **float**| The number of items to return | [optional] 
 **skip** | **float**| The number of items to skip | [optional] 

### Return type

[**GetBookingsOutput20240813**](GetBookingsOutput20240813.md)

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

# **bookings_controller20240813_mark_no_show**
> MarkAbsentBookingOutput20240813 bookings_controller20240813_mark_no_show(cal_api_version, booking_uid, authorization, mark_absent_booking_input20240813)

Mark a booking absence

### Example


```python
import openapi_client
from openapi_client.models.mark_absent_booking_input20240813 import MarkAbsentBookingInput20240813
from openapi_client.models.mark_absent_booking_output20240813 import MarkAbsentBookingOutput20240813
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
    api_instance = openapi_client.BookingsApi(api_client)
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-08-13`
    booking_uid = 'booking_uid_example' # str | 
    authorization = 'authorization_example' # str | value must be `Bearer <token>` where `<token>` either managed user access token or api key prefixed with cal_
    mark_absent_booking_input20240813 = openapi_client.MarkAbsentBookingInput20240813() # MarkAbsentBookingInput20240813 | 

    try:
        # Mark a booking absence
        api_response = api_instance.bookings_controller20240813_mark_no_show(cal_api_version, booking_uid, authorization, mark_absent_booking_input20240813)
        print("The response of BookingsApi->bookings_controller20240813_mark_no_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookingsApi->bookings_controller20240813_mark_no_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cal_api_version** | **str**| Must be set to &#x60;2024-08-13&#x60; | 
 **booking_uid** | **str**|  | 
 **authorization** | **str**| value must be &#x60;Bearer &lt;token&gt;&#x60; where &#x60;&lt;token&gt;&#x60; either managed user access token or api key prefixed with cal_ | 
 **mark_absent_booking_input20240813** | [**MarkAbsentBookingInput20240813**](MarkAbsentBookingInput20240813.md)|  | 

### Return type

[**MarkAbsentBookingOutput20240813**](MarkAbsentBookingOutput20240813.md)

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

# **bookings_controller20240813_reschedule_booking**
> RescheduleBookingOutput20240813 bookings_controller20240813_reschedule_booking(cal_api_version, booking_uid, reschedule_booking_input20240813)

Reschedule a booking

Reschedule a booking by passing `:bookingUid` of the booking that should be rescheduled and pass request body with a new start time to create a new booking.

### Example


```python
import openapi_client
from openapi_client.models.reschedule_booking_input20240813 import RescheduleBookingInput20240813
from openapi_client.models.reschedule_booking_output20240813 import RescheduleBookingOutput20240813
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
    api_instance = openapi_client.BookingsApi(api_client)
    cal_api_version = 'cal_api_version_example' # str | Must be set to `2024-08-13`
    booking_uid = 'booking_uid_example' # str | 
    reschedule_booking_input20240813 = openapi_client.RescheduleBookingInput20240813() # RescheduleBookingInput20240813 | 

    try:
        # Reschedule a booking
        api_response = api_instance.bookings_controller20240813_reschedule_booking(cal_api_version, booking_uid, reschedule_booking_input20240813)
        print("The response of BookingsApi->bookings_controller20240813_reschedule_booking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookingsApi->bookings_controller20240813_reschedule_booking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cal_api_version** | **str**| Must be set to &#x60;2024-08-13&#x60; | 
 **booking_uid** | **str**|  | 
 **reschedule_booking_input20240813** | [**RescheduleBookingInput20240813**](RescheduleBookingInput20240813.md)|  | 

### Return type

[**RescheduleBookingOutput20240813**](RescheduleBookingOutput20240813.md)

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

