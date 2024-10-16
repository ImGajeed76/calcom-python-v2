# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.attribute import Attribute

class TestAttribute(unittest.TestCase):
    """Attribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Attribute:
        """Test Attribute
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Attribute`
        """
        model = Attribute()
        if include_optional:
            return Attribute(
                id = 'attr_123',
                team_id = 1,
                type = 'TEXT',
                name = 'Attribute Name',
                slug = 'attribute-name',
                enabled = True,
                users_can_edit_relation = True
            )
        else:
            return Attribute(
                id = 'attr_123',
                team_id = 1,
                type = 'TEXT',
                name = 'Attribute Name',
                slug = 'attribute-name',
                enabled = True,
        )
        """

    def testAttribute(self):
        """Test Attribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
