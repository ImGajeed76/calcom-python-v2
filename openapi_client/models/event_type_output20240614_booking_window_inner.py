# coding: utf-8

"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from openapi_client.models.business_days_window20240614 import BusinessDaysWindow20240614
from openapi_client.models.calendar_days_window20240614 import CalendarDaysWindow20240614
from openapi_client.models.range_window20240614 import RangeWindow20240614
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

EVENTTYPEOUTPUT20240614BOOKINGWINDOWINNER_ONE_OF_SCHEMAS = ["BusinessDaysWindow20240614", "CalendarDaysWindow20240614", "RangeWindow20240614"]

class EventTypeOutput20240614BookingWindowInner(BaseModel):
    """
    EventTypeOutput20240614BookingWindowInner
    """
    # data type: BusinessDaysWindow20240614
    oneof_schema_1_validator: Optional[BusinessDaysWindow20240614] = None
    # data type: CalendarDaysWindow20240614
    oneof_schema_2_validator: Optional[CalendarDaysWindow20240614] = None
    # data type: RangeWindow20240614
    oneof_schema_3_validator: Optional[RangeWindow20240614] = None
    actual_instance: Optional[Union[BusinessDaysWindow20240614, CalendarDaysWindow20240614, RangeWindow20240614]] = None
    one_of_schemas: Set[str] = { "BusinessDaysWindow20240614", "CalendarDaysWindow20240614", "RangeWindow20240614" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = EventTypeOutput20240614BookingWindowInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: BusinessDaysWindow20240614
        if not isinstance(v, BusinessDaysWindow20240614):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BusinessDaysWindow20240614`")
        else:
            match += 1
        # validate data type: CalendarDaysWindow20240614
        if not isinstance(v, CalendarDaysWindow20240614):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CalendarDaysWindow20240614`")
        else:
            match += 1
        # validate data type: RangeWindow20240614
        if not isinstance(v, RangeWindow20240614):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RangeWindow20240614`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in EventTypeOutput20240614BookingWindowInner with oneOf schemas: BusinessDaysWindow20240614, CalendarDaysWindow20240614, RangeWindow20240614. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in EventTypeOutput20240614BookingWindowInner with oneOf schemas: BusinessDaysWindow20240614, CalendarDaysWindow20240614, RangeWindow20240614. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into BusinessDaysWindow20240614
        try:
            instance.actual_instance = BusinessDaysWindow20240614.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CalendarDaysWindow20240614
        try:
            instance.actual_instance = CalendarDaysWindow20240614.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RangeWindow20240614
        try:
            instance.actual_instance = RangeWindow20240614.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into EventTypeOutput20240614BookingWindowInner with oneOf schemas: BusinessDaysWindow20240614, CalendarDaysWindow20240614, RangeWindow20240614. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into EventTypeOutput20240614BookingWindowInner with oneOf schemas: BusinessDaysWindow20240614, CalendarDaysWindow20240614, RangeWindow20240614. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], BusinessDaysWindow20240614, CalendarDaysWindow20240614, RangeWindow20240614]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


