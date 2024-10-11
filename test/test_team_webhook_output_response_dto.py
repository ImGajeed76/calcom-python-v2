# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.team_webhook_output_response_dto import TeamWebhookOutputResponseDto

class TestTeamWebhookOutputResponseDto(unittest.TestCase):
    """TeamWebhookOutputResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamWebhookOutputResponseDto:
        """Test TeamWebhookOutputResponseDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamWebhookOutputResponseDto`
        """
        model = TeamWebhookOutputResponseDto()
        if include_optional:
            return TeamWebhookOutputResponseDto(
                status = 'success',
                data = openapi_client.models.team_webhook_output_dto.TeamWebhookOutputDto(
                    payload_template = '{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}', 
                    team_id = 1.337, 
                    id = 1.337, 
                    triggers = [
                        None
                        ], 
                    subscriber_url = '', 
                    active = True, 
                    secret = '', )
            )
        else:
            return TeamWebhookOutputResponseDto(
                status = 'success',
                data = openapi_client.models.team_webhook_output_dto.TeamWebhookOutputDto(
                    payload_template = '{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}', 
                    team_id = 1.337, 
                    id = 1.337, 
                    triggers = [
                        None
                        ], 
                    subscriber_url = '', 
                    active = True, 
                    secret = '', ),
        )
        """

    def testTeamWebhookOutputResponseDto(self):
        """Test TeamWebhookOutputResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
