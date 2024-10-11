# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_single_attribute_output import GetSingleAttributeOutput

class TestGetSingleAttributeOutput(unittest.TestCase):
    """GetSingleAttributeOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSingleAttributeOutput:
        """Test GetSingleAttributeOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSingleAttributeOutput`
        """
        model = GetSingleAttributeOutput()
        if include_optional:
            return GetSingleAttributeOutput(
                status = 'success',
                data = openapi_client.models.attribute.Attribute(
                    id = 'attr_123', 
                    team_id = 1, 
                    type = 'TEXT', 
                    name = 'Attribute Name', 
                    slug = 'attribute-name', 
                    enabled = True, 
                    users_can_edit_relation = True, )
            )
        else:
            return GetSingleAttributeOutput(
                status = 'success',
                data = openapi_client.models.attribute.Attribute(
                    id = 'attr_123', 
                    team_id = 1, 
                    type = 'TEXT', 
                    name = 'Attribute Name', 
                    slug = 'attribute-name', 
                    enabled = True, 
                    users_can_edit_relation = True, ),
        )
        """

    def testGetSingleAttributeOutput(self):
        """Test GetSingleAttributeOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
