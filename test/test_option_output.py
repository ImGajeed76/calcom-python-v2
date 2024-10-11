# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.option_output import OptionOutput

class TestOptionOutput(unittest.TestCase):
    """OptionOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OptionOutput:
        """Test OptionOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptionOutput`
        """
        model = OptionOutput()
        if include_optional:
            return OptionOutput(
                id = 'attr_option_id',
                attribute_id = 'attr_id',
                value = 'option_value',
                slug = 'option-slug'
            )
        else:
            return OptionOutput(
                id = 'attr_option_id',
                attribute_id = 'attr_id',
                value = 'option_value',
                slug = 'option-slug',
        )
        """

    def testOptionOutput(self):
        """Test OptionOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
