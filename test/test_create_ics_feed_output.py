# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_ics_feed_output import CreateIcsFeedOutput

class TestCreateIcsFeedOutput(unittest.TestCase):
    """CreateIcsFeedOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateIcsFeedOutput:
        """Test CreateIcsFeedOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateIcsFeedOutput`
        """
        model = CreateIcsFeedOutput()
        if include_optional:
            return CreateIcsFeedOutput(
                id = 1234567890,
                type = 'ics-feed_calendar',
                user_id = 1234567890,
                team_id = 1234567890,
                app_id = 'ics-feed',
                invalid = False
            )
        else:
            return CreateIcsFeedOutput(
                id = 1234567890,
                type = 'ics-feed_calendar',
                user_id = 1234567890,
                team_id = 1234567890,
                app_id = 'ics-feed',
                invalid = False,
        )
        """

    def testCreateIcsFeedOutput(self):
        """Test CreateIcsFeedOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
