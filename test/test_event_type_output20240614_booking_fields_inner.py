# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.event_type_output20240614_booking_fields_inner import EventTypeOutput20240614BookingFieldsInner

class TestEventTypeOutput20240614BookingFieldsInner(unittest.TestCase):
    """EventTypeOutput20240614BookingFieldsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EventTypeOutput20240614BookingFieldsInner:
        """Test EventTypeOutput20240614BookingFieldsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventTypeOutput20240614BookingFieldsInner`
        """
        model = EventTypeOutput20240614BookingFieldsInner()
        if include_optional:
            return EventTypeOutput20240614BookingFieldsInner(
                is_default = false,
                slug = 'some-slug',
                type = 'multiemail',
                required = True,
                label = 'Agree to terms?',
                placeholder = 'e.g., example@example.com',
                options = [Radio 1, Radio 2]
            )
        else:
            return EventTypeOutput20240614BookingFieldsInner(
                is_default = false,
                slug = 'some-slug',
                type = 'multiemail',
                required = True,
                label = 'Agree to terms?',
                options = [Radio 1, Radio 2],
        )
        """

    def testEventTypeOutput20240614BookingFieldsInner(self):
        """Test EventTypeOutput20240614BookingFieldsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
