# CreateEventTypeInput20240614Seats

Create an event type with multiple seats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seats_per_time_slot** | **float** | Number of seats available per time slot | 
**show_attendee_info** | **bool** | Show attendee information to other guests | 
**show_availability_count** | **bool** | Display the count of available seats | 
**disabled** | **bool** | Indicates if the option is disabled | [default to False]

## Example

```python
from openapi_client.models.create_event_type_input20240614_seats import CreateEventTypeInput20240614Seats

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventTypeInput20240614Seats from a JSON string
create_event_type_input20240614_seats_instance = CreateEventTypeInput20240614Seats.from_json(json)
# print the JSON string representation of the object
print(CreateEventTypeInput20240614Seats.to_json())

# convert the object into a dict
create_event_type_input20240614_seats_dict = create_event_type_input20240614_seats_instance.to_dict()
# create an instance of CreateEventTypeInput20240614Seats from a dict
create_event_type_input20240614_seats_from_dict = CreateEventTypeInput20240614Seats.from_dict(create_event_type_input20240614_seats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


