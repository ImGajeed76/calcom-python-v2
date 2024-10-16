# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_organization_attributes_output import CreateOrganizationAttributesOutput

class TestCreateOrganizationAttributesOutput(unittest.TestCase):
    """CreateOrganizationAttributesOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateOrganizationAttributesOutput:
        """Test CreateOrganizationAttributesOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateOrganizationAttributesOutput`
        """
        model = CreateOrganizationAttributesOutput()
        if include_optional:
            return CreateOrganizationAttributesOutput(
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
            return CreateOrganizationAttributesOutput(
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

    def testCreateOrganizationAttributesOutput(self):
        """Test CreateOrganizationAttributesOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
