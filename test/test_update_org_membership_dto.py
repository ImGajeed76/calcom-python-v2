# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.update_org_membership_dto import UpdateOrgMembershipDto

class TestUpdateOrgMembershipDto(unittest.TestCase):
    """UpdateOrgMembershipDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateOrgMembershipDto:
        """Test UpdateOrgMembershipDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateOrgMembershipDto`
        """
        model = UpdateOrgMembershipDto()
        if include_optional:
            return UpdateOrgMembershipDto(
                role = 'MEMBER',
                accepted = True,
                disable_impersonation = True
            )
        else:
            return UpdateOrgMembershipDto(
        )
        """

    def testUpdateOrgMembershipDto(self):
        """Test UpdateOrgMembershipDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
