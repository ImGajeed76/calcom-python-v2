# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_schedule_output20240611 import GetScheduleOutput20240611

class TestGetScheduleOutput20240611(unittest.TestCase):
    """GetScheduleOutput20240611 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetScheduleOutput20240611:
        """Test GetScheduleOutput20240611
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetScheduleOutput20240611`
        """
        model = GetScheduleOutput20240611()
        if include_optional:
            return GetScheduleOutput20240611(
                status = 'success',
                data = openapi_client.models.schedule_output_2024_06_11.ScheduleOutput_2024_06_11(
                    id = 254, 
                    owner_id = 478, 
                    name = 'Catch up hours', 
                    time_zone = 'Europe/Rome', 
                    availability = [{"days":["Monday","Tuesday"],"startTime":"17:00","endTime":"19:00"},{"days":["Wednesday","Thursday"],"startTime":"16:00","endTime":"20:00"}], 
                    is_default = True, 
                    overrides = [{"date":"2024-05-20","startTime":"18:00","endTime":"21:00"}], ),
                error = None
            )
        else:
            return GetScheduleOutput20240611(
                status = 'success',
                data = openapi_client.models.schedule_output_2024_06_11.ScheduleOutput_2024_06_11(
                    id = 254, 
                    owner_id = 478, 
                    name = 'Catch up hours', 
                    time_zone = 'Europe/Rome', 
                    availability = [{"days":["Monday","Tuesday"],"startTime":"17:00","endTime":"19:00"},{"days":["Wednesday","Thursday"],"startTime":"16:00","endTime":"20:00"}], 
                    is_default = True, 
                    overrides = [{"date":"2024-05-20","startTime":"18:00","endTime":"21:00"}], ),
        )
        """

    def testGetScheduleOutput20240611(self):
        """Test GetScheduleOutput20240611"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
