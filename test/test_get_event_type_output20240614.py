# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_event_type_output20240614 import GetEventTypeOutput20240614

class TestGetEventTypeOutput20240614(unittest.TestCase):
    """GetEventTypeOutput20240614 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetEventTypeOutput20240614:
        """Test GetEventTypeOutput20240614
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEventTypeOutput20240614`
        """
        model = GetEventTypeOutput20240614()
        if include_optional:
            return GetEventTypeOutput20240614(
                status = 'success',
                data = openapi_client.models.event_type_output_2024_06_14.EventTypeOutput_2024_06_14(
                    id = 1, 
                    length_in_minutes = 60, 
                    title = 'Learn the secrets of masterchief!', 
                    slug = 'learn-the-secrets-of-masterchief', 
                    description = 'Discover the culinary wonders of Argentina by making the best flan ever!', 
                    locations = [
                        null
                        ], 
                    booking_fields = [
                        null
                        ], 
                    disable_guests = True, 
                    slot_interval = 60, 
                    minimum_booking_notice = 0, 
                    before_event_buffer = 0, 
                    after_event_buffer = 0, 
                    recurrence = openapi_client.models.recurrence.recurrence(), 
                    metadata = openapi_client.models.metadata.metadata(), 
                    price = 1.337, 
                    currency = '', 
                    lock_time_zone_toggle_on_booking_page = True, 
                    seats_per_time_slot = openapi_client.models.seats_per_time_slot.seatsPerTimeSlot(), 
                    forward_params_success_redirect = openapi_client.models.forward_params_success_redirect.forwardParamsSuccessRedirect(), 
                    success_redirect_url = openapi_client.models.success_redirect_url.successRedirectUrl(), 
                    is_instant_event = True, 
                    seats_show_availability_count = openapi_client.models.seats_show_availability_count.seatsShowAvailabilityCount(), 
                    schedule_id = openapi_client.models.schedule_id.scheduleId(), 
                    booking_limits_count = openapi_client.models.booking_limits_count.bookingLimitsCount(), 
                    only_show_first_available_slot = True, 
                    booking_limits_duration = openapi_client.models.booking_limits_duration.bookingLimitsDuration(), 
                    booking_window = [
                        null
                        ], 
                    booker_layouts = openapi_client.models.booker_layouts_2024_06_14.BookerLayouts_2024_06_14(
                        default_layout = 'month', 
                        enabled_layouts = [
                            'month'
                            ], ), 
                    confirmation_policy = openapi_client.models.confirmation_policy.confirmationPolicy(), 
                    requires_booker_email_verification = True, 
                    hide_calendar_notes = True, 
                    color = openapi_client.models.event_type_color_2024_06_14.EventTypeColor_2024_06_14(
                        light_theme_hex = '#292929', 
                        dark_theme_hex = '#fafafa', ), 
                    seats = openapi_client.models.seats_2024_06_14.Seats_2024_06_14(
                        seats_per_time_slot = 4, 
                        show_attendee_info = True, 
                        show_availability_count = True, ), 
                    offset_start = 1.337, 
                    custom_name = '', 
                    destination_calendar = openapi_client.models.destination_calendar_2024_06_14.DestinationCalendar_2024_06_14(
                        integration = '', 
                        external_id = '', ), 
                    use_destination_calendar_email = True, 
                    hide_calendar_event_details = True, 
                    owner_id = 10, 
                    users = [
                        ''
                        ], )
            )
        else:
            return GetEventTypeOutput20240614(
                status = 'success',
                data = openapi_client.models.event_type_output_2024_06_14.EventTypeOutput_2024_06_14(
                    id = 1, 
                    length_in_minutes = 60, 
                    title = 'Learn the secrets of masterchief!', 
                    slug = 'learn-the-secrets-of-masterchief', 
                    description = 'Discover the culinary wonders of Argentina by making the best flan ever!', 
                    locations = [
                        null
                        ], 
                    booking_fields = [
                        null
                        ], 
                    disable_guests = True, 
                    slot_interval = 60, 
                    minimum_booking_notice = 0, 
                    before_event_buffer = 0, 
                    after_event_buffer = 0, 
                    recurrence = openapi_client.models.recurrence.recurrence(), 
                    metadata = openapi_client.models.metadata.metadata(), 
                    price = 1.337, 
                    currency = '', 
                    lock_time_zone_toggle_on_booking_page = True, 
                    seats_per_time_slot = openapi_client.models.seats_per_time_slot.seatsPerTimeSlot(), 
                    forward_params_success_redirect = openapi_client.models.forward_params_success_redirect.forwardParamsSuccessRedirect(), 
                    success_redirect_url = openapi_client.models.success_redirect_url.successRedirectUrl(), 
                    is_instant_event = True, 
                    seats_show_availability_count = openapi_client.models.seats_show_availability_count.seatsShowAvailabilityCount(), 
                    schedule_id = openapi_client.models.schedule_id.scheduleId(), 
                    booking_limits_count = openapi_client.models.booking_limits_count.bookingLimitsCount(), 
                    only_show_first_available_slot = True, 
                    booking_limits_duration = openapi_client.models.booking_limits_duration.bookingLimitsDuration(), 
                    booking_window = [
                        null
                        ], 
                    booker_layouts = openapi_client.models.booker_layouts_2024_06_14.BookerLayouts_2024_06_14(
                        default_layout = 'month', 
                        enabled_layouts = [
                            'month'
                            ], ), 
                    confirmation_policy = openapi_client.models.confirmation_policy.confirmationPolicy(), 
                    requires_booker_email_verification = True, 
                    hide_calendar_notes = True, 
                    color = openapi_client.models.event_type_color_2024_06_14.EventTypeColor_2024_06_14(
                        light_theme_hex = '#292929', 
                        dark_theme_hex = '#fafafa', ), 
                    seats = openapi_client.models.seats_2024_06_14.Seats_2024_06_14(
                        seats_per_time_slot = 4, 
                        show_attendee_info = True, 
                        show_availability_count = True, ), 
                    offset_start = 1.337, 
                    custom_name = '', 
                    destination_calendar = openapi_client.models.destination_calendar_2024_06_14.DestinationCalendar_2024_06_14(
                        integration = '', 
                        external_id = '', ), 
                    use_destination_calendar_email = True, 
                    hide_calendar_event_details = True, 
                    owner_id = 10, 
                    users = [
                        ''
                        ], ),
        )
        """

    def testGetEventTypeOutput20240614(self):
        """Test GetEventTypeOutput20240614"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
