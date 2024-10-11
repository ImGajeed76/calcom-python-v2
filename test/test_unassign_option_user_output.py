# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unassign_option_user_output import UnassignOptionUserOutput

class TestUnassignOptionUserOutput(unittest.TestCase):
    """UnassignOptionUserOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnassignOptionUserOutput:
        """Test UnassignOptionUserOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnassignOptionUserOutput`
        """
        model = UnassignOptionUserOutput()
        if include_optional:
            return UnassignOptionUserOutput(
                status = 'success',
                data = openapi_client.models.assign_option_user_output_data.AssignOptionUserOutputData(
                    id = '', 
                    member_id = 1.337, 
                    attribute_option_id = '', )
            )
        else:
            return UnassignOptionUserOutput(
                status = 'success',
                data = openapi_client.models.assign_option_user_output_data.AssignOptionUserOutputData(
                    id = '', 
                    member_id = 1.337, 
                    attribute_option_id = '', ),
        )
        """

    def testUnassignOptionUserOutput(self):
        """Test UnassignOptionUserOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
