# openapi_client.OrgsAttributesOptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_options_attributes_controller_assign_organization_attribute_option_to_user**](OrgsAttributesOptionsApi.md#organizations_options_attributes_controller_assign_organization_attribute_option_to_user) | **POST** /v2/organizations/{orgId}/attributes/options/{userId} | Assign an attribute to a user
[**organizations_options_attributes_controller_create_organization_attribute_option**](OrgsAttributesOptionsApi.md#organizations_options_attributes_controller_create_organization_attribute_option) | **POST** /v2/organizations/{orgId}/attributes/{attributeId}/options | Create an attribute option
[**organizations_options_attributes_controller_delete_organization_attribute_option**](OrgsAttributesOptionsApi.md#organizations_options_attributes_controller_delete_organization_attribute_option) | **DELETE** /v2/organizations/{orgId}/attributes/{attributeId}/options/{optionId} | Delete an attribute option
[**organizations_options_attributes_controller_get_organization_attribute_options**](OrgsAttributesOptionsApi.md#organizations_options_attributes_controller_get_organization_attribute_options) | **GET** /v2/organizations/{orgId}/attributes/{attributeId}/options | Get all attribute options
[**organizations_options_attributes_controller_get_organization_attribute_options_for_user**](OrgsAttributesOptionsApi.md#organizations_options_attributes_controller_get_organization_attribute_options_for_user) | **GET** /v2/organizations/{orgId}/attributes/options/{userId} | Get all attribute options for a user
[**organizations_options_attributes_controller_unassign_organization_attribute_option_from_user**](OrgsAttributesOptionsApi.md#organizations_options_attributes_controller_unassign_organization_attribute_option_from_user) | **DELETE** /v2/organizations/{orgId}/attributes/options/{userId}/{attributeOptionId} | Unassign an attribute from a user
[**organizations_options_attributes_controller_update_organization_attribute_option**](OrgsAttributesOptionsApi.md#organizations_options_attributes_controller_update_organization_attribute_option) | **PATCH** /v2/organizations/{orgId}/attributes/{attributeId}/options/{optionId} | Update an attribute option


# **organizations_options_attributes_controller_assign_organization_attribute_option_to_user**
> AssignOptionUserOutput organizations_options_attributes_controller_assign_organization_attribute_option_to_user(org_id, user_id, assign_organization_attribute_option_to_user_input)

Assign an attribute to a user

### Example


```python
import openapi_client
from openapi_client.models.assign_option_user_output import AssignOptionUserOutput
from openapi_client.models.assign_organization_attribute_option_to_user_input import AssignOrganizationAttributeOptionToUserInput
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
    api_instance = openapi_client.OrgsAttributesOptionsApi(api_client)
    org_id = 3.4 # float | 
    user_id = 3.4 # float | 
    assign_organization_attribute_option_to_user_input = openapi_client.AssignOrganizationAttributeOptionToUserInput() # AssignOrganizationAttributeOptionToUserInput | 

    try:
        # Assign an attribute to a user
        api_response = api_instance.organizations_options_attributes_controller_assign_organization_attribute_option_to_user(org_id, user_id, assign_organization_attribute_option_to_user_input)
        print("The response of OrgsAttributesOptionsApi->organizations_options_attributes_controller_assign_organization_attribute_option_to_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsAttributesOptionsApi->organizations_options_attributes_controller_assign_organization_attribute_option_to_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **user_id** | **float**|  | 
 **assign_organization_attribute_option_to_user_input** | [**AssignOrganizationAttributeOptionToUserInput**](AssignOrganizationAttributeOptionToUserInput.md)|  | 

### Return type

[**AssignOptionUserOutput**](AssignOptionUserOutput.md)

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

# **organizations_options_attributes_controller_create_organization_attribute_option**
> CreateAttributeOptionOutput organizations_options_attributes_controller_create_organization_attribute_option(org_id, attribute_id, create_organization_attribute_option_input)

Create an attribute option

### Example


```python
import openapi_client
from openapi_client.models.create_attribute_option_output import CreateAttributeOptionOutput
from openapi_client.models.create_organization_attribute_option_input import CreateOrganizationAttributeOptionInput
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
    api_instance = openapi_client.OrgsAttributesOptionsApi(api_client)
    org_id = 3.4 # float | 
    attribute_id = 'attribute_id_example' # str | 
    create_organization_attribute_option_input = openapi_client.CreateOrganizationAttributeOptionInput() # CreateOrganizationAttributeOptionInput | 

    try:
        # Create an attribute option
        api_response = api_instance.organizations_options_attributes_controller_create_organization_attribute_option(org_id, attribute_id, create_organization_attribute_option_input)
        print("The response of OrgsAttributesOptionsApi->organizations_options_attributes_controller_create_organization_attribute_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsAttributesOptionsApi->organizations_options_attributes_controller_create_organization_attribute_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **attribute_id** | **str**|  | 
 **create_organization_attribute_option_input** | [**CreateOrganizationAttributeOptionInput**](CreateOrganizationAttributeOptionInput.md)|  | 

### Return type

[**CreateAttributeOptionOutput**](CreateAttributeOptionOutput.md)

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

# **organizations_options_attributes_controller_delete_organization_attribute_option**
> DeleteAttributeOptionOutput organizations_options_attributes_controller_delete_organization_attribute_option(org_id, attribute_id, option_id)

Delete an attribute option

### Example


```python
import openapi_client
from openapi_client.models.delete_attribute_option_output import DeleteAttributeOptionOutput
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
    api_instance = openapi_client.OrgsAttributesOptionsApi(api_client)
    org_id = 3.4 # float | 
    attribute_id = 'attribute_id_example' # str | 
    option_id = 'option_id_example' # str | 

    try:
        # Delete an attribute option
        api_response = api_instance.organizations_options_attributes_controller_delete_organization_attribute_option(org_id, attribute_id, option_id)
        print("The response of OrgsAttributesOptionsApi->organizations_options_attributes_controller_delete_organization_attribute_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsAttributesOptionsApi->organizations_options_attributes_controller_delete_organization_attribute_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **attribute_id** | **str**|  | 
 **option_id** | **str**|  | 

### Return type

[**DeleteAttributeOptionOutput**](DeleteAttributeOptionOutput.md)

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

# **organizations_options_attributes_controller_get_organization_attribute_options**
> GetAllAttributeOptionOutput organizations_options_attributes_controller_get_organization_attribute_options(org_id, attribute_id)

Get all attribute options

### Example


```python
import openapi_client
from openapi_client.models.get_all_attribute_option_output import GetAllAttributeOptionOutput
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
    api_instance = openapi_client.OrgsAttributesOptionsApi(api_client)
    org_id = 3.4 # float | 
    attribute_id = 'attribute_id_example' # str | 

    try:
        # Get all attribute options
        api_response = api_instance.organizations_options_attributes_controller_get_organization_attribute_options(org_id, attribute_id)
        print("The response of OrgsAttributesOptionsApi->organizations_options_attributes_controller_get_organization_attribute_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsAttributesOptionsApi->organizations_options_attributes_controller_get_organization_attribute_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **attribute_id** | **str**|  | 

### Return type

[**GetAllAttributeOptionOutput**](GetAllAttributeOptionOutput.md)

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

# **organizations_options_attributes_controller_get_organization_attribute_options_for_user**
> GetOptionUserOutput organizations_options_attributes_controller_get_organization_attribute_options_for_user(org_id, user_id)

Get all attribute options for a user

### Example


```python
import openapi_client
from openapi_client.models.get_option_user_output import GetOptionUserOutput
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
    api_instance = openapi_client.OrgsAttributesOptionsApi(api_client)
    org_id = 3.4 # float | 
    user_id = 3.4 # float | 

    try:
        # Get all attribute options for a user
        api_response = api_instance.organizations_options_attributes_controller_get_organization_attribute_options_for_user(org_id, user_id)
        print("The response of OrgsAttributesOptionsApi->organizations_options_attributes_controller_get_organization_attribute_options_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsAttributesOptionsApi->organizations_options_attributes_controller_get_organization_attribute_options_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **user_id** | **float**|  | 

### Return type

[**GetOptionUserOutput**](GetOptionUserOutput.md)

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

# **organizations_options_attributes_controller_unassign_organization_attribute_option_from_user**
> UnassignOptionUserOutput organizations_options_attributes_controller_unassign_organization_attribute_option_from_user(org_id, user_id, attribute_option_id)

Unassign an attribute from a user

### Example


```python
import openapi_client
from openapi_client.models.unassign_option_user_output import UnassignOptionUserOutput
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
    api_instance = openapi_client.OrgsAttributesOptionsApi(api_client)
    org_id = 3.4 # float | 
    user_id = 3.4 # float | 
    attribute_option_id = 'attribute_option_id_example' # str | 

    try:
        # Unassign an attribute from a user
        api_response = api_instance.organizations_options_attributes_controller_unassign_organization_attribute_option_from_user(org_id, user_id, attribute_option_id)
        print("The response of OrgsAttributesOptionsApi->organizations_options_attributes_controller_unassign_organization_attribute_option_from_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsAttributesOptionsApi->organizations_options_attributes_controller_unassign_organization_attribute_option_from_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **user_id** | **float**|  | 
 **attribute_option_id** | **str**|  | 

### Return type

[**UnassignOptionUserOutput**](UnassignOptionUserOutput.md)

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

# **organizations_options_attributes_controller_update_organization_attribute_option**
> UpdateAttributeOptionOutput organizations_options_attributes_controller_update_organization_attribute_option(org_id, attribute_id, option_id, update_organization_attribute_option_input)

Update an attribute option

### Example


```python
import openapi_client
from openapi_client.models.update_attribute_option_output import UpdateAttributeOptionOutput
from openapi_client.models.update_organization_attribute_option_input import UpdateOrganizationAttributeOptionInput
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
    api_instance = openapi_client.OrgsAttributesOptionsApi(api_client)
    org_id = 3.4 # float | 
    attribute_id = 'attribute_id_example' # str | 
    option_id = 'option_id_example' # str | 
    update_organization_attribute_option_input = openapi_client.UpdateOrganizationAttributeOptionInput() # UpdateOrganizationAttributeOptionInput | 

    try:
        # Update an attribute option
        api_response = api_instance.organizations_options_attributes_controller_update_organization_attribute_option(org_id, attribute_id, option_id, update_organization_attribute_option_input)
        print("The response of OrgsAttributesOptionsApi->organizations_options_attributes_controller_update_organization_attribute_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsAttributesOptionsApi->organizations_options_attributes_controller_update_organization_attribute_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **attribute_id** | **str**|  | 
 **option_id** | **str**|  | 
 **update_organization_attribute_option_input** | [**UpdateOrganizationAttributeOptionInput**](UpdateOrganizationAttributeOptionInput.md)|  | 

### Return type

[**UpdateAttributeOptionOutput**](UpdateAttributeOptionOutput.md)

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

