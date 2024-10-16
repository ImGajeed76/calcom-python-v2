# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.platform_managed_users_api import PlatformManagedUsersApi


class TestPlatformManagedUsersApi(unittest.TestCase):
    """PlatformManagedUsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlatformManagedUsersApi()

    def tearDown(self) -> None:
        pass

    def test_o_auth_client_users_controller_create_user(self) -> None:
        """Test case for o_auth_client_users_controller_create_user

        Create a managed user
        """
        pass

    def test_o_auth_client_users_controller_delete_user(self) -> None:
        """Test case for o_auth_client_users_controller_delete_user

        Delete a managed user
        """
        pass

    def test_o_auth_client_users_controller_force_refresh(self) -> None:
        """Test case for o_auth_client_users_controller_force_refresh

        Force refresh tokens
        """
        pass

    def test_o_auth_client_users_controller_get_managed_users(self) -> None:
        """Test case for o_auth_client_users_controller_get_managed_users

        Get all managed users
        """
        pass

    def test_o_auth_client_users_controller_get_user_by_id(self) -> None:
        """Test case for o_auth_client_users_controller_get_user_by_id

        Get a managed user
        """
        pass

    def test_o_auth_client_users_controller_update_user(self) -> None:
        """Test case for o_auth_client_users_controller_update_user

        Update a managed user
        """
        pass


if __name__ == '__main__':
    unittest.main()
