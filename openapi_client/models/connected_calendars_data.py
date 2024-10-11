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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from openapi_client.models.connected_calendar import ConnectedCalendar
from openapi_client.models.destination_calendar import DestinationCalendar
from typing import Optional, Set
from typing_extensions import Self

class ConnectedCalendarsData(BaseModel):
    """
    ConnectedCalendarsData
    """ # noqa: E501
    connected_calendars: List[ConnectedCalendar] = Field(alias="connectedCalendars")
    destination_calendar: DestinationCalendar = Field(alias="destinationCalendar")
    __properties: ClassVar[List[str]] = ["connectedCalendars", "destinationCalendar"]

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
        """Create an instance of ConnectedCalendarsData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in connected_calendars (list)
        _items = []
        if self.connected_calendars:
            for _item_connected_calendars in self.connected_calendars:
                if _item_connected_calendars:
                    _items.append(_item_connected_calendars.to_dict())
            _dict['connectedCalendars'] = _items
        # override the default output from pydantic by calling `to_dict()` of destination_calendar
        if self.destination_calendar:
            _dict['destinationCalendar'] = self.destination_calendar.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConnectedCalendarsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connectedCalendars": [ConnectedCalendar.from_dict(_item) for _item in obj["connectedCalendars"]] if obj.get("connectedCalendars") is not None else None,
            "destinationCalendar": DestinationCalendar.from_dict(obj["destinationCalendar"]) if obj.get("destinationCalendar") is not None else None
        })
        return _obj


