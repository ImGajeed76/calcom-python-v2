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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class Attribute(BaseModel):
    """
    Attribute
    """ # noqa: E501
    id: StrictStr = Field(description="The ID of the attribute")
    team_id: Union[StrictFloat, StrictInt] = Field(description="The team ID associated with the attribute", alias="teamId")
    type: StrictStr = Field(description="The type of the attribute")
    name: StrictStr = Field(description="The name of the attribute")
    slug: StrictStr = Field(description="The slug of the attribute")
    enabled: StrictBool = Field(description="Whether the attribute is enabled and displayed on their profile")
    users_can_edit_relation: Optional[StrictBool] = Field(default=None, description="Whether users can edit the relation", alias="usersCanEditRelation")
    __properties: ClassVar[List[str]] = ["id", "teamId", "type", "name", "slug", "enabled", "usersCanEditRelation"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['TEXT', 'NUMBER', 'SINGLE_SELECT', 'MULTI_SELECT']):
            raise ValueError("must be one of enum values ('TEXT', 'NUMBER', 'SINGLE_SELECT', 'MULTI_SELECT')")
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
        """Create an instance of Attribute from a JSON string"""
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
        """Create an instance of Attribute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "teamId": obj.get("teamId"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "enabled": obj.get("enabled"),
            "usersCanEditRelation": obj.get("usersCanEditRelation")
        })
        return _obj


