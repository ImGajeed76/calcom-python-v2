# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_ics_feed_output_response_dto import CreateIcsFeedOutputResponseDto

class TestCreateIcsFeedOutputResponseDto(unittest.TestCase):
    """CreateIcsFeedOutputResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateIcsFeedOutputResponseDto:
        """Test CreateIcsFeedOutputResponseDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateIcsFeedOutputResponseDto`
        """
        model = CreateIcsFeedOutputResponseDto()
        if include_optional:
            return CreateIcsFeedOutputResponseDto(
                status = 'success',
                data = openapi_client.models.create_ics_feed_output.CreateIcsFeedOutput(
                    id = 1234567890, 
                    type = 'ics-feed_calendar', 
                    user_id = 1234567890, 
                    team_id = 1234567890, 
                    app_id = 'ics-feed', 
                    invalid = False, )
            )
        else:
            return CreateIcsFeedOutputResponseDto(
                status = 'success',
                data = openapi_client.models.create_ics_feed_output.CreateIcsFeedOutput(
                    id = 1234567890, 
                    type = 'ics-feed_calendar', 
                    user_id = 1234567890, 
                    team_id = 1234567890, 
                    app_id = 'ics-feed', 
                    invalid = False, ),
        )
        """

    def testCreateIcsFeedOutputResponseDto(self):
        """Test CreateIcsFeedOutputResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
