# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.destination_calendar import DestinationCalendar

class TestDestinationCalendar(unittest.TestCase):
    """DestinationCalendar unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DestinationCalendar:
        """Test DestinationCalendar
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DestinationCalendar`
        """
        model = DestinationCalendar()
        if include_optional:
            return DestinationCalendar(
                id = 1.337,
                integration = '',
                external_id = '',
                primary_email = '',
                user_id = 1.337,
                event_type_id = 1.337,
                credential_id = 1.337,
                name = '',
                primary = True,
                read_only = True,
                email = '',
                integration_title = ''
            )
        else:
            return DestinationCalendar(
                id = 1.337,
                integration = '',
                external_id = '',
                primary_email = '',
                user_id = 1.337,
                event_type_id = 1.337,
                credential_id = 1.337,
        )
        """

    def testDestinationCalendar(self):
        """Test DestinationCalendar"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
