# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UpdateWebhookInputDto(BaseModel):
    """
    UpdateWebhookInputDto
    """ # noqa: E501
    payload_template: Optional[StrictStr] = Field(default=None, description="The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information", alias="payloadTemplate")
    triggers: Optional[StrictStr] = None
    active: Optional[StrictBool] = None
    subscriber_url: Optional[StrictStr] = Field(default=None, alias="subscriberUrl")
    secret: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["payloadTemplate", "triggers", "active", "subscriberUrl", "secret"]

    @field_validator('triggers')
    def triggers_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['BOOKING_CREATED', 'BOOKING_PAYMENT_INITIATED', 'BOOKING_PAID', 'BOOKING_RESCHEDULED', 'BOOKING_REQUESTED', 'BOOKING_CANCELLED', 'BOOKING_REJECTED', 'BOOKING_NO_SHOW_UPDATED', 'FORM_SUBMITTED', 'MEETING_ENDED', 'MEETING_STARTED', 'RECORDING_READY', 'INSTANT_MEETING', 'RECORDING_TRANSCRIPTION_GENERATED', 'OOO_CREATED']):
            raise ValueError("must be one of enum values ('BOOKING_CREATED', 'BOOKING_PAYMENT_INITIATED', 'BOOKING_PAID', 'BOOKING_RESCHEDULED', 'BOOKING_REQUESTED', 'BOOKING_CANCELLED', 'BOOKING_REJECTED', 'BOOKING_NO_SHOW_UPDATED', 'FORM_SUBMITTED', 'MEETING_ENDED', 'MEETING_STARTED', 'RECORDING_READY', 'INSTANT_MEETING', 'RECORDING_TRANSCRIPTION_GENERATED', 'OOO_CREATED')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UpdateWebhookInputDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateWebhookInputDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "payloadTemplate": obj.get("payloadTemplate"),
            "triggers": obj.get("triggers"),
            "active": obj.get("active"),
            "subscriberUrl": obj.get("subscriberUrl"),
            "secret": obj.get("secret")
        })
        return _obj


