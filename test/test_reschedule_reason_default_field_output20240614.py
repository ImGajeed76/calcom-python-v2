# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.reschedule_reason_default_field_output20240614 import RescheduleReasonDefaultFieldOutput20240614

class TestRescheduleReasonDefaultFieldOutput20240614(unittest.TestCase):
    """RescheduleReasonDefaultFieldOutput20240614 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RescheduleReasonDefaultFieldOutput20240614:
        """Test RescheduleReasonDefaultFieldOutput20240614
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RescheduleReasonDefaultFieldOutput20240614`
        """
        model = RescheduleReasonDefaultFieldOutput20240614()
        if include_optional:
            return RescheduleReasonDefaultFieldOutput20240614(
                is_default = true,
                slug = 'rescheduleReason',
                type = 'textarea',
                required = True
            )
        else:
            return RescheduleReasonDefaultFieldOutput20240614(
                is_default = true,
                slug = 'rescheduleReason',
                type = 'textarea',
                required = True,
        )
        """

    def testRescheduleReasonDefaultFieldOutput20240614(self):
        """Test RescheduleReasonDefaultFieldOutput20240614"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
