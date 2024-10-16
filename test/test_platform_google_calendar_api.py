# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.platform_google_calendar_api import PlatformGoogleCalendarApi


class TestPlatformGoogleCalendarApi(unittest.TestCase):
    """PlatformGoogleCalendarApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlatformGoogleCalendarApi()

    def tearDown(self) -> None:
        pass

    def test_gcal_controller_check(self) -> None:
        """Test case for gcal_controller_check

        Check a calendar connection status
        """
        pass

    def test_gcal_controller_redirect(self) -> None:
        """Test case for gcal_controller_redirect

        Get auth URL
        """
        pass

    def test_gcal_controller_save(self) -> None:
        """Test case for gcal_controller_save

        Connect a calendar
        """
        pass


if __name__ == '__main__':
    unittest.main()
