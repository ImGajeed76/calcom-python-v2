# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_o_auth_clients_response_dto import GetOAuthClientsResponseDto

class TestGetOAuthClientsResponseDto(unittest.TestCase):
    """GetOAuthClientsResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetOAuthClientsResponseDto:
        """Test GetOAuthClientsResponseDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetOAuthClientsResponseDto`
        """
        model = GetOAuthClientsResponseDto()
        if include_optional:
            return GetOAuthClientsResponseDto(
                status = 'success',
                data = [
                    openapi_client.models.platform_o_auth_client_dto.PlatformOAuthClientDto(
                        id = 'clsx38nbl0001vkhlwin9fmt0', 
                        name = 'MyClient', 
                        secret = 'secretValue', 
                        permissions = 3, 
                        logo = 'https://example.com/logo.png', 
                        redirect_uris = ["https://example.com/callback"], 
                        organization_id = 1, 
                        created_at = '2024-03-23T08:33:21.851Z', )
                    ]
            )
        else:
            return GetOAuthClientsResponseDto(
                status = 'success',
                data = [
                    openapi_client.models.platform_o_auth_client_dto.PlatformOAuthClientDto(
                        id = 'clsx38nbl0001vkhlwin9fmt0', 
                        name = 'MyClient', 
                        secret = 'secretValue', 
                        permissions = 3, 
                        logo = 'https://example.com/logo.png', 
                        redirect_uris = ["https://example.com/callback"], 
                        organization_id = 1, 
                        created_at = '2024-03-23T08:33:21.851Z', )
                    ],
        )
        """

    def testGetOAuthClientsResponseDto(self):
        """Test GetOAuthClientsResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
