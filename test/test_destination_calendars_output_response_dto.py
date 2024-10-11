# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.destination_calendars_output_response_dto import DestinationCalendarsOutputResponseDto

class TestDestinationCalendarsOutputResponseDto(unittest.TestCase):
    """DestinationCalendarsOutputResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DestinationCalendarsOutputResponseDto:
        """Test DestinationCalendarsOutputResponseDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DestinationCalendarsOutputResponseDto`
        """
        model = DestinationCalendarsOutputResponseDto()
        if include_optional:
            return DestinationCalendarsOutputResponseDto(
                status = 'success',
                data = openapi_client.models.destination_calendars_output_dto.DestinationCalendarsOutputDto(
                    user_id = 1.337, 
                    integration = '', 
                    external_id = '', 
                    credential_id = 1.337, )
            )
        else:
            return DestinationCalendarsOutputResponseDto(
                status = 'success',
                data = openapi_client.models.destination_calendars_output_dto.DestinationCalendarsOutputDto(
                    user_id = 1.337, 
                    integration = '', 
                    external_id = '', 
                    credential_id = 1.337, ),
        )
        """

    def testDestinationCalendarsOutputResponseDto(self):
        """Test DestinationCalendarsOutputResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
