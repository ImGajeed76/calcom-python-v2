# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.reserve_slot_input import ReserveSlotInput

class TestReserveSlotInput(unittest.TestCase):
    """ReserveSlotInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReserveSlotInput:
        """Test ReserveSlotInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReserveSlotInput`
        """
        model = ReserveSlotInput()
        if include_optional:
            return ReserveSlotInput(
                event_type_id = 100,
                slot_utc_start_date = '2022-06-14T00:00:00.000Z',
                slot_utc_end_date = '2022-06-14T00:30:00.000Z',
                booking_uid = ''
            )
        else:
            return ReserveSlotInput(
                event_type_id = 100,
                slot_utc_start_date = '2022-06-14T00:00:00.000Z',
                slot_utc_end_date = '2022-06-14T00:30:00.000Z',
        )
        """

    def testReserveSlotInput(self):
        """Test ReserveSlotInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
