# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.platform_conferencing_api import PlatformConferencingApi


class TestPlatformConferencingApi(unittest.TestCase):
    """PlatformConferencingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlatformConferencingApi()

    def tearDown(self) -> None:
        pass

    def test_conferencing_controller_connect(self) -> None:
        """Test case for conferencing_controller_connect

        connect your conferencing application
        """
        pass

    def test_conferencing_controller_default(self) -> None:
        """Test case for conferencing_controller_default

        set your default conferencing application
        """
        pass

    def test_conferencing_controller_disconnect(self) -> None:
        """Test case for conferencing_controller_disconnect

        disconnect your conferencing application
        """
        pass

    def test_conferencing_controller_list_conferencing_apps(self) -> None:
        """Test case for conferencing_controller_list_conferencing_apps

        list your conferencing applications
        """
        pass


if __name__ == '__main__':
    unittest.main()
