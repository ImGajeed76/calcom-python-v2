# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.update_me_output import UpdateMeOutput

class TestUpdateMeOutput(unittest.TestCase):
    """UpdateMeOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateMeOutput:
        """Test UpdateMeOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateMeOutput`
        """
        model = UpdateMeOutput()
        if include_optional:
            return UpdateMeOutput(
                status = 'success',
                data = openapi_client.models.me_output.MeOutput(
                    id = 1.337, 
                    username = '', 
                    email = '', 
                    time_format = 1.337, 
                    default_schedule_id = 1.337, 
                    week_start = '', 
                    time_zone = '', 
                    organization_id = 1.337, 
                    organization = openapi_client.models.me_org_output.MeOrgOutput(
                        is_platform = True, 
                        id = 1.337, ), )
            )
        else:
            return UpdateMeOutput(
                status = 'success',
                data = openapi_client.models.me_output.MeOutput(
                    id = 1.337, 
                    username = '', 
                    email = '', 
                    time_format = 1.337, 
                    default_schedule_id = 1.337, 
                    week_start = '', 
                    time_zone = '', 
                    organization_id = 1.337, 
                    organization = openapi_client.models.me_org_output.MeOrgOutput(
                        is_platform = True, 
                        id = 1.337, ), ),
        )
        """

    def testUpdateMeOutput(self):
        """Test UpdateMeOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
