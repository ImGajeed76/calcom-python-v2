# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_user_output import GetUserOutput

class TestGetUserOutput(unittest.TestCase):
    """GetUserOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUserOutput:
        """Test GetUserOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUserOutput`
        """
        model = GetUserOutput()
        if include_optional:
            return GetUserOutput(
                id = 1,
                username = 'john_doe',
                name = 'John Doe',
                email = 'john@example.com',
                email_verified = '2022-01-01T00:00Z',
                bio = 'I am a software developer',
                avatar_url = 'https://example.com/avatar.jpg',
                time_zone = 'America/New_York',
                week_start = 'Monday',
                app_theme = 'light',
                theme = 'default',
                default_schedule_id = 1,
                locale = 'en-US',
                time_format = 12,
                hide_branding = False,
                brand_color = '#ffffff',
                dark_brand_color = '#000000',
                allow_dynamic_booking = True,
                created_date = '2022-01-01T00:00Z',
                verified = True,
                invited_to = 1
            )
        else:
            return GetUserOutput(
                id = 1,
                email = 'john@example.com',
                time_zone = 'America/New_York',
                week_start = 'Monday',
                hide_branding = False,
                created_date = '2022-01-01T00:00Z',
        )
        """

    def testGetUserOutput(self):
        """Test GetUserOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
