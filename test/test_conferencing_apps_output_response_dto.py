# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.conferencing_apps_output_response_dto import ConferencingAppsOutputResponseDto

class TestConferencingAppsOutputResponseDto(unittest.TestCase):
    """ConferencingAppsOutputResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConferencingAppsOutputResponseDto:
        """Test ConferencingAppsOutputResponseDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConferencingAppsOutputResponseDto`
        """
        model = ConferencingAppsOutputResponseDto()
        if include_optional:
            return ConferencingAppsOutputResponseDto(
                status = 'success',
                data = [
                    openapi_client.models.conferencing_apps_output_dto.ConferencingAppsOutputDto(
                        id = 1.337, 
                        type = 'google_video', 
                        user_id = 1.337, 
                        invalid = True, )
                    ]
            )
        else:
            return ConferencingAppsOutputResponseDto(
                status = 'success',
                data = [
                    openapi_client.models.conferencing_apps_output_dto.ConferencingAppsOutputDto(
                        id = 1.337, 
                        type = 'google_video', 
                        user_id = 1.337, 
                        invalid = True, )
                    ],
        )
        """

    def testConferencingAppsOutputResponseDto(self):
        """Test ConferencingAppsOutputResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
