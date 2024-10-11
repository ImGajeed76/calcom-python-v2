# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.destination_calendars_input_body_dto import DestinationCalendarsInputBodyDto

class TestDestinationCalendarsInputBodyDto(unittest.TestCase):
    """DestinationCalendarsInputBodyDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DestinationCalendarsInputBodyDto:
        """Test DestinationCalendarsInputBodyDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DestinationCalendarsInputBodyDto`
        """
        model = DestinationCalendarsInputBodyDto()
        if include_optional:
            return DestinationCalendarsInputBodyDto(
                integration = 'apple_calendar',
                external_id = 'https://caldav.icloud.com/26962146906/calendars/1644422A-1945-4438-BBC0-4F0Q23A57R7S/'
            )
        else:
            return DestinationCalendarsInputBodyDto(
                integration = 'apple_calendar',
                external_id = 'https://caldav.icloud.com/26962146906/calendars/1644422A-1945-4438-BBC0-4F0Q23A57R7S/',
        )
        """

    def testDestinationCalendarsInputBodyDto(self):
        """Test DestinationCalendarsInputBodyDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
