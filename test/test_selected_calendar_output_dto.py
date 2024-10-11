# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.selected_calendar_output_dto import SelectedCalendarOutputDto

class TestSelectedCalendarOutputDto(unittest.TestCase):
    """SelectedCalendarOutputDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SelectedCalendarOutputDto:
        """Test SelectedCalendarOutputDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SelectedCalendarOutputDto`
        """
        model = SelectedCalendarOutputDto()
        if include_optional:
            return SelectedCalendarOutputDto(
                user_id = 1.337,
                integration = '',
                external_id = '',
                credential_id = 1.337
            )
        else:
            return SelectedCalendarOutputDto(
                user_id = 1.337,
                integration = '',
                external_id = '',
                credential_id = 1.337,
        )
        """

    def testSelectedCalendarOutputDto(self):
        """Test SelectedCalendarOutputDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
