# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.delete_schedule_output20240611 import DeleteScheduleOutput20240611

class TestDeleteScheduleOutput20240611(unittest.TestCase):
    """DeleteScheduleOutput20240611 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteScheduleOutput20240611:
        """Test DeleteScheduleOutput20240611
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteScheduleOutput20240611`
        """
        model = DeleteScheduleOutput20240611()
        if include_optional:
            return DeleteScheduleOutput20240611(
                status = 'success'
            )
        else:
            return DeleteScheduleOutput20240611(
                status = 'success',
        )
        """

    def testDeleteScheduleOutput20240611(self):
        """Test DeleteScheduleOutput20240611"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
