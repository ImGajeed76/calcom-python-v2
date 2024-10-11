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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CreatePhoneCallInput(BaseModel):
    """
    CreatePhoneCallInput
    """ # noqa: E501
    your_phone_number: Annotated[str, Field(strict=True)] = Field(description="Your phone number", alias="yourPhoneNumber")
    number_to_call: Annotated[str, Field(strict=True)] = Field(description="Number to call", alias="numberToCall")
    cal_api_key: StrictStr = Field(description="CAL API Key", alias="calApiKey")
    enabled: Dict[str, Any] = Field(description="Enabled status")
    template_type: StrictStr = Field(description="Template type", alias="templateType")
    scheduler_name: Optional[StrictStr] = Field(default=None, description="Scheduler name", alias="schedulerName")
    guest_name: Optional[StrictStr] = Field(default=None, description="Guest name", alias="guestName")
    guest_email: Optional[StrictStr] = Field(default=None, description="Guest email", alias="guestEmail")
    guest_company: Optional[StrictStr] = Field(default=None, description="Guest company", alias="guestCompany")
    begin_message: Optional[StrictStr] = Field(default=None, description="Begin message", alias="beginMessage")
    general_prompt: Optional[StrictStr] = Field(default=None, description="General prompt", alias="generalPrompt")
    __properties: ClassVar[List[str]] = ["yourPhoneNumber", "numberToCall", "calApiKey", "enabled", "templateType", "schedulerName", "guestName", "guestEmail", "guestCompany", "beginMessage", "generalPrompt"]

    @field_validator('your_phone_number')
    def your_phone_number_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\+[1-9]\d{1,14}$", value):
            raise ValueError(r"must validate the regular expression /^\+[1-9]\d{1,14}$/")
        return value

    @field_validator('number_to_call')
    def number_to_call_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\+[1-9]\d{1,14}$", value):
            raise ValueError(r"must validate the regular expression /^\+[1-9]\d{1,14}$/")
        return value

    @field_validator('template_type')
    def template_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CHECK_IN_APPOINTMENT', 'CUSTOM_TEMPLATE']):
            raise ValueError("must be one of enum values ('CHECK_IN_APPOINTMENT', 'CUSTOM_TEMPLATE')")
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
        """Create an instance of CreatePhoneCallInput from a JSON string"""
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
        """Create an instance of CreatePhoneCallInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "yourPhoneNumber": obj.get("yourPhoneNumber"),
            "numberToCall": obj.get("numberToCall"),
            "calApiKey": obj.get("calApiKey"),
            "enabled": obj.get("enabled"),
            "templateType": obj.get("templateType") if obj.get("templateType") is not None else 'CUSTOM_TEMPLATE',
            "schedulerName": obj.get("schedulerName"),
            "guestName": obj.get("guestName"),
            "guestEmail": obj.get("guestEmail"),
            "guestCompany": obj.get("guestCompany"),
            "beginMessage": obj.get("beginMessage"),
            "generalPrompt": obj.get("generalPrompt")
        })
        return _obj


