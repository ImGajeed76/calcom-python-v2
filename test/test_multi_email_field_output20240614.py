# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.multi_email_field_output20240614 import MultiEmailFieldOutput20240614

class TestMultiEmailFieldOutput20240614(unittest.TestCase):
    """MultiEmailFieldOutput20240614 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MultiEmailFieldOutput20240614:
        """Test MultiEmailFieldOutput20240614
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MultiEmailFieldOutput20240614`
        """
        model = MultiEmailFieldOutput20240614()
        if include_optional:
            return MultiEmailFieldOutput20240614(
                type = 'multiemail',
                slug = 'some-slug',
                label = 'Please enter multiple emails',
                required = True,
                placeholder = 'e.g., example@example.com',
                is_default = false
            )
        else:
            return MultiEmailFieldOutput20240614(
                type = 'multiemail',
                slug = 'some-slug',
                label = 'Please enter multiple emails',
                required = True,
                is_default = false,
        )
        """

    def testMultiEmailFieldOutput20240614(self):
        """Test MultiEmailFieldOutput20240614"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
