# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.stripe_api import StripeApi


class TestStripeApi(unittest.TestCase):
    """StripeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StripeApi()

    def tearDown(self) -> None:
        pass

    def test_stripe_controller_check(self) -> None:
        """Test case for stripe_controller_check

        Check stripe connection
        """
        pass

    def test_stripe_controller_redirect(self) -> None:
        """Test case for stripe_controller_redirect

        Get stripe connect URL
        """
        pass

    def test_stripe_controller_save(self) -> None:
        """Test case for stripe_controller_save

        Save stripe credentials
        """
        pass


if __name__ == '__main__':
    unittest.main()
