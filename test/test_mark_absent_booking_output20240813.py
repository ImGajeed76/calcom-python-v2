# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.mark_absent_booking_output20240813 import MarkAbsentBookingOutput20240813

class TestMarkAbsentBookingOutput20240813(unittest.TestCase):
    """MarkAbsentBookingOutput20240813 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarkAbsentBookingOutput20240813:
        """Test MarkAbsentBookingOutput20240813
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarkAbsentBookingOutput20240813`
        """
        model = MarkAbsentBookingOutput20240813()
        if include_optional:
            return MarkAbsentBookingOutput20240813(
                status = 'success',
                data = None
            )
        else:
            return MarkAbsentBookingOutput20240813(
                status = 'success',
                data = None,
        )
        """

    def testMarkAbsentBookingOutput20240813(self):
        """Test MarkAbsentBookingOutput20240813"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
