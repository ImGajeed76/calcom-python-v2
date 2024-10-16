# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.bookings_api import BookingsApi


class TestBookingsApi(unittest.TestCase):
    """BookingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BookingsApi()

    def tearDown(self) -> None:
        pass

    def test_bookings_controller20240813_cancel_booking(self) -> None:
        """Test case for bookings_controller20240813_cancel_booking

        Cancel a booking
        """
        pass

    def test_bookings_controller20240813_create_booking(self) -> None:
        """Test case for bookings_controller20240813_create_booking

        Create a booking
        """
        pass

    def test_bookings_controller20240813_get_booking(self) -> None:
        """Test case for bookings_controller20240813_get_booking

        Get a booking
        """
        pass

    def test_bookings_controller20240813_get_bookings(self) -> None:
        """Test case for bookings_controller20240813_get_bookings

        Get all bookings
        """
        pass

    def test_bookings_controller20240813_mark_no_show(self) -> None:
        """Test case for bookings_controller20240813_mark_no_show

        Mark a booking absence
        """
        pass

    def test_bookings_controller20240813_reschedule_booking(self) -> None:
        """Test case for bookings_controller20240813_reschedule_booking

        Reschedule a booking
        """
        pass


if __name__ == '__main__':
    unittest.main()
