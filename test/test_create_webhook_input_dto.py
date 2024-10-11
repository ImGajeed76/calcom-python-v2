# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_webhook_input_dto import CreateWebhookInputDto

class TestCreateWebhookInputDto(unittest.TestCase):
    """CreateWebhookInputDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateWebhookInputDto:
        """Test CreateWebhookInputDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateWebhookInputDto`
        """
        model = CreateWebhookInputDto()
        if include_optional:
            return CreateWebhookInputDto(
                payload_template = '{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}',
                triggers = '["BOOKING_CREATED","BOOKING_RESCHEDULED","BOOKING_CANCELLED","BOOKING_CONFIRMED","BOOKING_REJECTED","BOOKING_COMPLETED","BOOKING_NO_SHOW","BOOKING_REOPENED"]',
                active = True,
                subscriber_url = '',
                secret = ''
            )
        else:
            return CreateWebhookInputDto(
                triggers = '["BOOKING_CREATED","BOOKING_RESCHEDULED","BOOKING_CANCELLED","BOOKING_CONFIRMED","BOOKING_REJECTED","BOOKING_COMPLETED","BOOKING_NO_SHOW","BOOKING_REOPENED"]',
                active = True,
                subscriber_url = '',
        )
        """

    def testCreateWebhookInputDto(self):
        """Test CreateWebhookInputDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
