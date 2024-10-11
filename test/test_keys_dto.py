# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.keys_dto import KeysDto

class TestKeysDto(unittest.TestCase):
    """KeysDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KeysDto:
        """Test KeysDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KeysDto`
        """
        model = KeysDto()
        if include_optional:
            return KeysDto(
                access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9',
                refresh_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9',
                access_token_expires_at = 1.337
            )
        else:
            return KeysDto(
                access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9',
                refresh_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9',
                access_token_expires_at = 1.337,
        )
        """

    def testKeysDto(self):
        """Test KeysDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
