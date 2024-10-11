# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.phone_field_output20240614 import PhoneFieldOutput20240614

class TestPhoneFieldOutput20240614(unittest.TestCase):
    """PhoneFieldOutput20240614 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PhoneFieldOutput20240614:
        """Test PhoneFieldOutput20240614
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PhoneFieldOutput20240614`
        """
        model = PhoneFieldOutput20240614()
        if include_optional:
            return PhoneFieldOutput20240614(
                type = 'phone',
                slug = 'some-slug',
                label = '',
                required = True,
                placeholder = '',
                is_default = false
            )
        else:
            return PhoneFieldOutput20240614(
                type = 'phone',
                slug = 'some-slug',
                label = '',
                required = True,
                is_default = false,
        )
        """

    def testPhoneFieldOutput20240614(self):
        """Test PhoneFieldOutput20240614"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
