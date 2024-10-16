# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.strip_connect_output_response_dto import StripConnectOutputResponseDto

class TestStripConnectOutputResponseDto(unittest.TestCase):
    """StripConnectOutputResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StripConnectOutputResponseDto:
        """Test StripConnectOutputResponseDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StripConnectOutputResponseDto`
        """
        model = StripConnectOutputResponseDto()
        if include_optional:
            return StripConnectOutputResponseDto(
                status = 'success',
                data = openapi_client.models.strip_connect_output_dto.StripConnectOutputDto(
                    auth_url = '', )
            )
        else:
            return StripConnectOutputResponseDto(
                status = 'success',
                data = openapi_client.models.strip_connect_output_dto.StripConnectOutputDto(
                    auth_url = '', ),
        )
        """

    def testStripConnectOutputResponseDto(self):
        """Test StripConnectOutputResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
