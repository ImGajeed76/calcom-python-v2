# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.range_window20240614 import RangeWindow20240614

class TestRangeWindow20240614(unittest.TestCase):
    """RangeWindow20240614 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RangeWindow20240614:
        """Test RangeWindow20240614
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RangeWindow20240614`
        """
        model = RangeWindow20240614()
        if include_optional:
            return RangeWindow20240614(
                type = 'businessDays',
                value = ["2030-09-05","2030-09-09"]
            )
        else:
            return RangeWindow20240614(
                type = 'businessDays',
                value = ["2030-09-05","2030-09-09"],
        )
        """

    def testRangeWindow20240614(self):
        """Test RangeWindow20240614"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
