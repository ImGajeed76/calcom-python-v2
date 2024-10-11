# CreateEventTypeInput20240614Recurrence

Create a recurring event type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **float** | Repeats every {count} week | month | year | 
**occurrences** | **float** | Repeats for a maximum of {count} events | 
**frequency** | **str** |  | 
**disabled** | **bool** | Indicates if the option is disabled | [default to False]

## Example

```python
from openapi_client.models.create_event_type_input20240614_recurrence import CreateEventTypeInput20240614Recurrence

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventTypeInput20240614Recurrence from a JSON string
create_event_type_input20240614_recurrence_instance = CreateEventTypeInput20240614Recurrence.from_json(json)
# print the JSON string representation of the object
print(CreateEventTypeInput20240614Recurrence.to_json())

# convert the object into a dict
create_event_type_input20240614_recurrence_dict = create_event_type_input20240614_recurrence_instance.to_dict()
# create an instance of CreateEventTypeInput20240614Recurrence from a dict
create_event_type_input20240614_recurrence_from_dict = CreateEventTypeInput20240614Recurrence.from_dict(create_event_type_input20240614_recurrence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


