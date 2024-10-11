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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.slots_controller_get_available_slots200_response_data_slots_value_inner import SlotsControllerGetAvailableSlots200ResponseDataSlotsValueInner
from typing import Optional, Set
from typing_extensions import Self

class SlotsControllerGetAvailableSlots200ResponseData(BaseModel):
    """
    SlotsControllerGetAvailableSlots200ResponseData
    """ # noqa: E501
    slots: Optional[Dict[str, List[SlotsControllerGetAvailableSlots200ResponseDataSlotsValueInner]]] = None
    __properties: ClassVar[List[str]] = ["slots"]

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
        """Create an instance of SlotsControllerGetAvailableSlots200ResponseData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in slots (dict of array)
        _field_dict_of_array = {}
        if self.slots:
            for _key_slots in self.slots:
                if self.slots[_key_slots] is not None:
                    _field_dict_of_array[_key_slots] = [
                        _item.to_dict() for _item in self.slots[_key_slots]
                    ]
            _dict['slots'] = _field_dict_of_array
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SlotsControllerGetAvailableSlots200ResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "slots": dict(
                (_k,
                        [SlotsControllerGetAvailableSlots200ResponseDataSlotsValueInner.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("slots", {}).items()
            )
        })
        return _obj


