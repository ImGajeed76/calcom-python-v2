# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_org_team_membership_dto import CreateOrgTeamMembershipDto

class TestCreateOrgTeamMembershipDto(unittest.TestCase):
    """CreateOrgTeamMembershipDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateOrgTeamMembershipDto:
        """Test CreateOrgTeamMembershipDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateOrgTeamMembershipDto`
        """
        model = CreateOrgTeamMembershipDto()
        if include_optional:
            return CreateOrgTeamMembershipDto(
                role = 'MEMBER',
                user_id = 1.337,
                accepted = True,
                disable_impersonation = True
            )
        else:
            return CreateOrgTeamMembershipDto(
                role = 'MEMBER',
                user_id = 1.337,
        )
        """

    def testCreateOrgTeamMembershipDto(self):
        """Test CreateOrgTeamMembershipDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
