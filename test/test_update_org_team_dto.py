# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.update_org_team_dto import UpdateOrgTeamDto

class TestUpdateOrgTeamDto(unittest.TestCase):
    """UpdateOrgTeamDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateOrgTeamDto:
        """Test UpdateOrgTeamDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateOrgTeamDto`
        """
        model = UpdateOrgTeamDto()
        if include_optional:
            return UpdateOrgTeamDto(
                name = '0',
                slug = '',
                logo_url = '',
                cal_video_logo = '',
                app_logo = '',
                app_icon_logo = '',
                bio = '',
                hide_branding = True,
                is_private = True,
                hide_book_a_team_member = True,
                metadata = '',
                theme = '',
                brand_color = '',
                dark_brand_color = '',
                banner_url = '',
                time_format = 1.337,
                time_zone = 'Europe/London',
                week_start = 'Sunday',
                booking_limits = '',
                include_managed_events_in_limits = True
            )
        else:
            return UpdateOrgTeamDto(
        )
        """

    def testUpdateOrgTeamDto(self):
        """Test UpdateOrgTeamDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
