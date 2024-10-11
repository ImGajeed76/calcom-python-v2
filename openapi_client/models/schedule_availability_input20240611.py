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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ScheduleAvailabilityInput20240611(BaseModel):
    """
    ScheduleAvailabilityInput20240611
    """ # noqa: E501
    days: StrictStr = Field(description="Array of days when schedule is active.")
    start_time: Annotated[str, Field(strict=True)] = Field(description="startTime must be a valid time in format HH:MM e.g. 08:00", alias="startTime")
    end_time: Annotated[str, Field(strict=True)] = Field(description="endTime must be a valid time in format HH:MM e.g. 15:00", alias="endTime")
    __properties: ClassVar[List[str]] = ["days", "startTime", "endTime"]

    @field_validator('days')
    def days_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']):
            raise ValueError("must be one of enum values ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')")
        return value

    @field_validator('start_time')
    def start_time_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"TIME_FORMAT_HH_MM", value):
            raise ValueError(r"must validate the regular expression /TIME_FORMAT_HH_MM/")
        return value

    @field_validator('end_time')
    def end_time_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"TIME_FORMAT_HH_MM", value):
            raise ValueError(r"must validate the regular expression /TIME_FORMAT_HH_MM/")
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
        """Create an instance of ScheduleAvailabilityInput20240611 from a JSON string"""
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
        """Create an instance of ScheduleAvailabilityInput20240611 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "days": obj.get("days"),
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime")
        })
        return _obj


