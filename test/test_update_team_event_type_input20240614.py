# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.update_team_event_type_input20240614 import UpdateTeamEventTypeInput20240614

class TestUpdateTeamEventTypeInput20240614(unittest.TestCase):
    """UpdateTeamEventTypeInput20240614 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateTeamEventTypeInput20240614:
        """Test UpdateTeamEventTypeInput20240614
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateTeamEventTypeInput20240614`
        """
        model = UpdateTeamEventTypeInput20240614()
        if include_optional:
            return UpdateTeamEventTypeInput20240614(
                length_in_minutes = 60,
                title = 'Learn the secrets of masterchief!',
                slug = 'learn-the-secrets-of-masterchief',
                description = 'Discover the culinary wonders of the Argentina by making the best flan ever!',
                locations = [
                    null
                    ],
                booking_fields = [
                    null
                    ],
                disable_guests = True,
                slot_interval = 1.337,
                minimum_booking_notice = 1.337,
                before_event_buffer = 1.337,
                after_event_buffer = 1.337,
                schedule_id = 1.337,
                booking_limits_count = None,
                only_show_first_available_slot = True,
                booking_limits_duration = None,
                booking_window = None,
                offset_start = 1.337,
                booker_layouts = openapi_client.models.booker_layouts_2024_06_14.BookerLayouts_2024_06_14(
                    default_layout = 'month', 
                    enabled_layouts = [
                        'month'
                        ], ),
                confirmation_policy = None,
                recurrence = None,
                requires_booker_email_verification = True,
                hide_calendar_notes = True,
                lock_time_zone_toggle_on_booking_page = True,
                color = openapi_client.models.event_type_color_2024_06_14.EventTypeColor_2024_06_14(
                    light_theme_hex = '#292929', 
                    dark_theme_hex = '#fafafa', ),
                seats = None,
                custom_name = '{Event type title} between {Organiser} and {Scheduler}',
                destination_calendar = openapi_client.models.destination_calendar_2024_06_14.DestinationCalendar_2024_06_14(
                    integration = '', 
                    external_id = '', ),
                use_destination_calendar_email = True,
                hide_calendar_event_details = True,
                hosts = [
                    openapi_client.models.host.Host(
                        user_id = 1.337, 
                        mandatory = True, 
                        priority = 'lowest', )
                    ],
                assign_all_team_members = True
            )
        else:
            return UpdateTeamEventTypeInput20240614(
        )
        """

    def testUpdateTeamEventTypeInput20240614(self):
        """Test UpdateTeamEventTypeInput20240614"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
