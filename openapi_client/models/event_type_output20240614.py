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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from openapi_client.models.booker_layouts20240614 import BookerLayouts20240614
from openapi_client.models.create_event_type_input20240614_locations_inner import CreateEventTypeInput20240614LocationsInner
from openapi_client.models.destination_calendar20240614 import DestinationCalendar20240614
from openapi_client.models.event_type_color20240614 import EventTypeColor20240614
from openapi_client.models.event_type_output20240614_booking_fields_inner import EventTypeOutput20240614BookingFieldsInner
from openapi_client.models.event_type_output20240614_booking_window_inner import EventTypeOutput20240614BookingWindowInner
from openapi_client.models.seats20240614 import Seats20240614
from typing import Optional, Set
from typing_extensions import Self

class EventTypeOutput20240614(BaseModel):
    """
    EventTypeOutput20240614
    """ # noqa: E501
    id: Union[StrictFloat, StrictInt]
    length_in_minutes: Union[StrictFloat, StrictInt] = Field(alias="lengthInMinutes")
    title: StrictStr
    slug: StrictStr
    description: StrictStr
    locations: List[CreateEventTypeInput20240614LocationsInner]
    booking_fields: List[EventTypeOutput20240614BookingFieldsInner] = Field(alias="bookingFields")
    disable_guests: StrictBool = Field(alias="disableGuests")
    slot_interval: Union[StrictFloat, StrictInt] = Field(alias="slotInterval")
    minimum_booking_notice: Union[StrictFloat, StrictInt] = Field(alias="minimumBookingNotice")
    before_event_buffer: Union[StrictFloat, StrictInt] = Field(alias="beforeEventBuffer")
    after_event_buffer: Union[StrictFloat, StrictInt] = Field(alias="afterEventBuffer")
    recurrence: Dict[str, Any]
    metadata: Dict[str, Any]
    price: Union[StrictFloat, StrictInt]
    currency: StrictStr
    lock_time_zone_toggle_on_booking_page: StrictBool = Field(alias="lockTimeZoneToggleOnBookingPage")
    seats_per_time_slot: Dict[str, Any] = Field(alias="seatsPerTimeSlot")
    forward_params_success_redirect: Dict[str, Any] = Field(alias="forwardParamsSuccessRedirect")
    success_redirect_url: Dict[str, Any] = Field(alias="successRedirectUrl")
    is_instant_event: StrictBool = Field(alias="isInstantEvent")
    seats_show_availability_count: Dict[str, Any] = Field(alias="seatsShowAvailabilityCount")
    schedule_id: Dict[str, Any] = Field(alias="scheduleId")
    booking_limits_count: Dict[str, Any] = Field(alias="bookingLimitsCount")
    only_show_first_available_slot: StrictBool = Field(alias="onlyShowFirstAvailableSlot")
    booking_limits_duration: Dict[str, Any] = Field(alias="bookingLimitsDuration")
    booking_window: List[EventTypeOutput20240614BookingWindowInner] = Field(description="Limit how far in the future this event can be booked", alias="bookingWindow")
    booker_layouts: BookerLayouts20240614 = Field(alias="bookerLayouts")
    confirmation_policy: Dict[str, Any] = Field(alias="confirmationPolicy")
    requires_booker_email_verification: StrictBool = Field(alias="requiresBookerEmailVerification")
    hide_calendar_notes: StrictBool = Field(alias="hideCalendarNotes")
    color: EventTypeColor20240614
    seats: Seats20240614
    offset_start: Union[StrictFloat, StrictInt] = Field(alias="offsetStart")
    custom_name: StrictStr = Field(alias="customName")
    destination_calendar: DestinationCalendar20240614 = Field(alias="destinationCalendar")
    use_destination_calendar_email: StrictBool = Field(alias="useDestinationCalendarEmail")
    hide_calendar_event_details: StrictBool = Field(alias="hideCalendarEventDetails")
    owner_id: Union[StrictFloat, StrictInt] = Field(alias="ownerId")
    users: List[StrictStr]
    __properties: ClassVar[List[str]] = ["id", "lengthInMinutes", "title", "slug", "description", "locations", "bookingFields", "disableGuests", "slotInterval", "minimumBookingNotice", "beforeEventBuffer", "afterEventBuffer", "recurrence", "metadata", "price", "currency", "lockTimeZoneToggleOnBookingPage", "seatsPerTimeSlot", "forwardParamsSuccessRedirect", "successRedirectUrl", "isInstantEvent", "seatsShowAvailabilityCount", "scheduleId", "bookingLimitsCount", "onlyShowFirstAvailableSlot", "bookingLimitsDuration", "bookingWindow", "bookerLayouts", "confirmationPolicy", "requiresBookerEmailVerification", "hideCalendarNotes", "color", "seats", "offsetStart", "customName", "destinationCalendar", "useDestinationCalendarEmail", "hideCalendarEventDetails", "ownerId", "users"]

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
        """Create an instance of EventTypeOutput20240614 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in locations (list)
        _items = []
        if self.locations:
            for _item_locations in self.locations:
                if _item_locations:
                    _items.append(_item_locations.to_dict())
            _dict['locations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in booking_fields (list)
        _items = []
        if self.booking_fields:
            for _item_booking_fields in self.booking_fields:
                if _item_booking_fields:
                    _items.append(_item_booking_fields.to_dict())
            _dict['bookingFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in booking_window (list)
        _items = []
        if self.booking_window:
            for _item_booking_window in self.booking_window:
                if _item_booking_window:
                    _items.append(_item_booking_window.to_dict())
            _dict['bookingWindow'] = _items
        # override the default output from pydantic by calling `to_dict()` of booker_layouts
        if self.booker_layouts:
            _dict['bookerLayouts'] = self.booker_layouts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of color
        if self.color:
            _dict['color'] = self.color.to_dict()
        # override the default output from pydantic by calling `to_dict()` of seats
        if self.seats:
            _dict['seats'] = self.seats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination_calendar
        if self.destination_calendar:
            _dict['destinationCalendar'] = self.destination_calendar.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EventTypeOutput20240614 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "lengthInMinutes": obj.get("lengthInMinutes"),
            "title": obj.get("title"),
            "slug": obj.get("slug"),
            "description": obj.get("description"),
            "locations": [CreateEventTypeInput20240614LocationsInner.from_dict(_item) for _item in obj["locations"]] if obj.get("locations") is not None else None,
            "bookingFields": [EventTypeOutput20240614BookingFieldsInner.from_dict(_item) for _item in obj["bookingFields"]] if obj.get("bookingFields") is not None else None,
            "disableGuests": obj.get("disableGuests"),
            "slotInterval": obj.get("slotInterval"),
            "minimumBookingNotice": obj.get("minimumBookingNotice"),
            "beforeEventBuffer": obj.get("beforeEventBuffer"),
            "afterEventBuffer": obj.get("afterEventBuffer"),
            "recurrence": obj.get("recurrence"),
            "metadata": obj.get("metadata"),
            "price": obj.get("price"),
            "currency": obj.get("currency"),
            "lockTimeZoneToggleOnBookingPage": obj.get("lockTimeZoneToggleOnBookingPage"),
            "seatsPerTimeSlot": obj.get("seatsPerTimeSlot"),
            "forwardParamsSuccessRedirect": obj.get("forwardParamsSuccessRedirect"),
            "successRedirectUrl": obj.get("successRedirectUrl"),
            "isInstantEvent": obj.get("isInstantEvent"),
            "seatsShowAvailabilityCount": obj.get("seatsShowAvailabilityCount"),
            "scheduleId": obj.get("scheduleId"),
            "bookingLimitsCount": obj.get("bookingLimitsCount"),
            "onlyShowFirstAvailableSlot": obj.get("onlyShowFirstAvailableSlot"),
            "bookingLimitsDuration": obj.get("bookingLimitsDuration"),
            "bookingWindow": [EventTypeOutput20240614BookingWindowInner.from_dict(_item) for _item in obj["bookingWindow"]] if obj.get("bookingWindow") is not None else None,
            "bookerLayouts": BookerLayouts20240614.from_dict(obj["bookerLayouts"]) if obj.get("bookerLayouts") is not None else None,
            "confirmationPolicy": obj.get("confirmationPolicy"),
            "requiresBookerEmailVerification": obj.get("requiresBookerEmailVerification"),
            "hideCalendarNotes": obj.get("hideCalendarNotes"),
            "color": EventTypeColor20240614.from_dict(obj["color"]) if obj.get("color") is not None else None,
            "seats": Seats20240614.from_dict(obj["seats"]) if obj.get("seats") is not None else None,
            "offsetStart": obj.get("offsetStart"),
            "customName": obj.get("customName"),
            "destinationCalendar": DestinationCalendar20240614.from_dict(obj["destinationCalendar"]) if obj.get("destinationCalendar") is not None else None,
            "useDestinationCalendarEmail": obj.get("useDestinationCalendarEmail"),
            "hideCalendarEventDetails": obj.get("hideCalendarEventDetails"),
            "ownerId": obj.get("ownerId"),
            "users": obj.get("users")
        })
        return _obj


