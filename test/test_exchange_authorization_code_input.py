# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.exchange_authorization_code_input import ExchangeAuthorizationCodeInput

class TestExchangeAuthorizationCodeInput(unittest.TestCase):
    """ExchangeAuthorizationCodeInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExchangeAuthorizationCodeInput:
        """Test ExchangeAuthorizationCodeInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExchangeAuthorizationCodeInput`
        """
        model = ExchangeAuthorizationCodeInput()
        if include_optional:
            return ExchangeAuthorizationCodeInput(
                client_secret = ''
            )
        else:
            return ExchangeAuthorizationCodeInput(
                client_secret = '',
        )
        """

    def testExchangeAuthorizationCodeInput(self):
        """Test ExchangeAuthorizationCodeInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
