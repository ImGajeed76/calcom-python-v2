# openapi_client.OrgsAttributesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_attributes_controller_create_organization_attribute**](OrgsAttributesApi.md#organizations_attributes_controller_create_organization_attribute) | **POST** /v2/organizations/{orgId}/attributes | Create an attribute
[**organizations_attributes_controller_delete_organization_attribute**](OrgsAttributesApi.md#organizations_attributes_controller_delete_organization_attribute) | **DELETE** /v2/organizations/{orgId}/attributes/{attributeId} | Delete an attribute
[**organizations_attributes_controller_get_organization_attribute**](OrgsAttributesApi.md#organizations_attributes_controller_get_organization_attribute) | **GET** /v2/organizations/{orgId}/attributes/{attributeId} | Get an attribute
[**organizations_attributes_controller_get_organization_attributes**](OrgsAttributesApi.md#organizations_attributes_controller_get_organization_attributes) | **GET** /v2/organizations/{orgId}/attributes | Get all attributes
[**organizations_attributes_controller_update_organization_attribute**](OrgsAttributesApi.md#organizations_attributes_controller_update_organization_attribute) | **PATCH** /v2/organizations/{orgId}/attributes/{attributeId} | Update an attribute


# **organizations_attributes_controller_create_organization_attribute**
> CreateOrganizationAttributesOutput organizations_attributes_controller_create_organization_attribute(org_id, create_organization_attribute_input)

Create an attribute

### Example


```python
import openapi_client
from openapi_client.models.create_organization_attribute_input import CreateOrganizationAttributeInput
from openapi_client.models.create_organization_attributes_output import CreateOrganizationAttributesOutput
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
    api_instance = openapi_client.OrgsAttributesApi(api_client)
    org_id = 3.4 # float | 
    create_organization_attribute_input = openapi_client.CreateOrganizationAttributeInput() # CreateOrganizationAttributeInput | 

    try:
        # Create an attribute
        api_response = api_instance.organizations_attributes_controller_create_organization_attribute(org_id, create_organization_attribute_input)
        print("The response of OrgsAttributesApi->organizations_attributes_controller_create_organization_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsAttributesApi->organizations_attributes_controller_create_organization_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **create_organization_attribute_input** | [**CreateOrganizationAttributeInput**](CreateOrganizationAttributeInput.md)|  | 

### Return type

[**CreateOrganizationAttributesOutput**](CreateOrganizationAttributesOutput.md)

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

# **organizations_attributes_controller_delete_organization_attribute**
> DeleteOrganizationAttributesOutput organizations_attributes_controller_delete_organization_attribute(org_id, attribute_id)

Delete an attribute

### Example


```python
import openapi_client
from openapi_client.models.delete_organization_attributes_output import DeleteOrganizationAttributesOutput
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
    api_instance = openapi_client.OrgsAttributesApi(api_client)
    org_id = 3.4 # float | 
    attribute_id = 'attribute_id_example' # str | 

    try:
        # Delete an attribute
        api_response = api_instance.organizations_attributes_controller_delete_organization_attribute(org_id, attribute_id)
        print("The response of OrgsAttributesApi->organizations_attributes_controller_delete_organization_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsAttributesApi->organizations_attributes_controller_delete_organization_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **attribute_id** | **str**|  | 

### Return type

[**DeleteOrganizationAttributesOutput**](DeleteOrganizationAttributesOutput.md)

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

# **organizations_attributes_controller_get_organization_attribute**
> GetSingleAttributeOutput organizations_attributes_controller_get_organization_attribute(org_id, attribute_id)

Get an attribute

### Example


```python
import openapi_client
from openapi_client.models.get_single_attribute_output import GetSingleAttributeOutput
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
    api_instance = openapi_client.OrgsAttributesApi(api_client)
    org_id = 3.4 # float | 
    attribute_id = 'attribute_id_example' # str | 

    try:
        # Get an attribute
        api_response = api_instance.organizations_attributes_controller_get_organization_attribute(org_id, attribute_id)
        print("The response of OrgsAttributesApi->organizations_attributes_controller_get_organization_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsAttributesApi->organizations_attributes_controller_get_organization_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **attribute_id** | **str**|  | 

### Return type

[**GetSingleAttributeOutput**](GetSingleAttributeOutput.md)

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

# **organizations_attributes_controller_get_organization_attributes**
> GetOrganizationAttributesOutput organizations_attributes_controller_get_organization_attributes(org_id, take=take, skip=skip)

Get all attributes

### Example


```python
import openapi_client
from openapi_client.models.get_organization_attributes_output import GetOrganizationAttributesOutput
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
    api_instance = openapi_client.OrgsAttributesApi(api_client)
    org_id = 3.4 # float | 
    take = 10 # float | The number of items to return (optional)
    skip = 0 # float | The number of items to skip (optional)

    try:
        # Get all attributes
        api_response = api_instance.organizations_attributes_controller_get_organization_attributes(org_id, take=take, skip=skip)
        print("The response of OrgsAttributesApi->organizations_attributes_controller_get_organization_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsAttributesApi->organizations_attributes_controller_get_organization_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **take** | **float**| The number of items to return | [optional] 
 **skip** | **float**| The number of items to skip | [optional] 

### Return type

[**GetOrganizationAttributesOutput**](GetOrganizationAttributesOutput.md)

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

# **organizations_attributes_controller_update_organization_attribute**
> UpdateOrganizationAttributesOutput organizations_attributes_controller_update_organization_attribute(org_id, attribute_id, update_organization_attribute_input)

Update an attribute

### Example


```python
import openapi_client
from openapi_client.models.update_organization_attribute_input import UpdateOrganizationAttributeInput
from openapi_client.models.update_organization_attributes_output import UpdateOrganizationAttributesOutput
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
    api_instance = openapi_client.OrgsAttributesApi(api_client)
    org_id = 3.4 # float | 
    attribute_id = 'attribute_id_example' # str | 
    update_organization_attribute_input = openapi_client.UpdateOrganizationAttributeInput() # UpdateOrganizationAttributeInput | 

    try:
        # Update an attribute
        api_response = api_instance.organizations_attributes_controller_update_organization_attribute(org_id, attribute_id, update_organization_attribute_input)
        print("The response of OrgsAttributesApi->organizations_attributes_controller_update_organization_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsAttributesApi->organizations_attributes_controller_update_organization_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **float**|  | 
 **attribute_id** | **str**|  | 
 **update_organization_attribute_input** | [**UpdateOrganizationAttributeInput**](UpdateOrganizationAttributeInput.md)|  | 

### Return type

[**UpdateOrganizationAttributesOutput**](UpdateOrganizationAttributesOutput.md)

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

