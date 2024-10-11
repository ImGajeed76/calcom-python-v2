# coding: utf-8

# flake8: noqa
"""
    Cal.com API v2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from openapi_client.models.address_field_input20240614 import AddressFieldInput20240614
from openapi_client.models.address_field_output20240614 import AddressFieldOutput20240614
from openapi_client.models.address_location20240614 import AddressLocation20240614
from openapi_client.models.assign_option_user_output import AssignOptionUserOutput
from openapi_client.models.assign_option_user_output_data import AssignOptionUserOutputData
from openapi_client.models.assign_organization_attribute_option_to_user_input import AssignOrganizationAttributeOptionToUserInput
from openapi_client.models.attendee import Attendee
from openapi_client.models.attribute import Attribute
from openapi_client.models.auth_url_data import AuthUrlData
from openapi_client.models.base_booking_limits_count20240614 import BaseBookingLimitsCount20240614
from openapi_client.models.base_booking_limits_duration20240614 import BaseBookingLimitsDuration20240614
from openapi_client.models.base_confirmation_policy20240614 import BaseConfirmationPolicy20240614
from openapi_client.models.booker_layouts20240614 import BookerLayouts20240614
from openapi_client.models.booking_output20240813 import BookingOutput20240813
from openapi_client.models.bookings_controller20240813_create_booking_request import BookingsController20240813CreateBookingRequest
from openapi_client.models.boolean_field_input20240614 import BooleanFieldInput20240614
from openapi_client.models.boolean_field_output20240614 import BooleanFieldOutput20240614
from openapi_client.models.business_days_window20240614 import BusinessDaysWindow20240614
from openapi_client.models.busy_times_output import BusyTimesOutput
from openapi_client.models.calendar import Calendar
from openapi_client.models.calendar_days_window20240614 import CalendarDaysWindow20240614
from openapi_client.models.cancel_booking_input20240813 import CancelBookingInput20240813
from openapi_client.models.cancel_booking_output20240813 import CancelBookingOutput20240813
from openapi_client.models.checkbox_group_field_input20240614 import CheckboxGroupFieldInput20240614
from openapi_client.models.checkbox_group_field_output20240614 import CheckboxGroupFieldOutput20240614
from openapi_client.models.conferencing_app_output_response_dto import ConferencingAppOutputResponseDto
from openapi_client.models.conferencing_apps_output_dto import ConferencingAppsOutputDto
from openapi_client.models.conferencing_apps_output_response_dto import ConferencingAppsOutputResponseDto
from openapi_client.models.connected_calendar import ConnectedCalendar
from openapi_client.models.connected_calendars_data import ConnectedCalendarsData
from openapi_client.models.connected_calendars_output import ConnectedCalendarsOutput
from openapi_client.models.create_attribute_option_output import CreateAttributeOptionOutput
from openapi_client.models.create_booking_input20240813 import CreateBookingInput20240813
from openapi_client.models.create_booking_output20240813 import CreateBookingOutput20240813
from openapi_client.models.create_booking_output20240813_data import CreateBookingOutput20240813Data
from openapi_client.models.create_event_type_input20240614 import CreateEventTypeInput20240614
from openapi_client.models.create_event_type_input20240614_booking_fields_inner import CreateEventTypeInput20240614BookingFieldsInner
from openapi_client.models.create_event_type_input20240614_booking_limits_count import CreateEventTypeInput20240614BookingLimitsCount
from openapi_client.models.create_event_type_input20240614_booking_limits_duration import CreateEventTypeInput20240614BookingLimitsDuration
from openapi_client.models.create_event_type_input20240614_booking_window import CreateEventTypeInput20240614BookingWindow
from openapi_client.models.create_event_type_input20240614_confirmation_policy import CreateEventTypeInput20240614ConfirmationPolicy
from openapi_client.models.create_event_type_input20240614_locations_inner import CreateEventTypeInput20240614LocationsInner
from openapi_client.models.create_event_type_input20240614_recurrence import CreateEventTypeInput20240614Recurrence
from openapi_client.models.create_event_type_input20240614_seats import CreateEventTypeInput20240614Seats
from openapi_client.models.create_event_type_output20240614 import CreateEventTypeOutput20240614
from openapi_client.models.create_ics_feed_input_dto import CreateIcsFeedInputDto
from openapi_client.models.create_ics_feed_output import CreateIcsFeedOutput
from openapi_client.models.create_ics_feed_output_response_dto import CreateIcsFeedOutputResponseDto
from openapi_client.models.create_instant_booking_input20240813 import CreateInstantBookingInput20240813
from openapi_client.models.create_managed_user_data import CreateManagedUserData
from openapi_client.models.create_managed_user_input import CreateManagedUserInput
from openapi_client.models.create_managed_user_output import CreateManagedUserOutput
from openapi_client.models.create_o_auth_client_response_dto import CreateOAuthClientResponseDto
from openapi_client.models.create_org_membership_dto import CreateOrgMembershipDto
from openapi_client.models.create_org_membership_output import CreateOrgMembershipOutput
from openapi_client.models.create_org_team_dto import CreateOrgTeamDto
from openapi_client.models.create_org_team_membership_dto import CreateOrgTeamMembershipDto
from openapi_client.models.create_organization_attribute_input import CreateOrganizationAttributeInput
from openapi_client.models.create_organization_attribute_option_input import CreateOrganizationAttributeOptionInput
from openapi_client.models.create_organization_attributes_output import CreateOrganizationAttributesOutput
from openapi_client.models.create_organization_user_input import CreateOrganizationUserInput
from openapi_client.models.create_phone_call_input import CreatePhoneCallInput
from openapi_client.models.create_phone_call_output import CreatePhoneCallOutput
from openapi_client.models.create_recurring_booking_input20240813 import CreateRecurringBookingInput20240813
from openapi_client.models.create_schedule_input20240611 import CreateScheduleInput20240611
from openapi_client.models.create_schedule_output20240611 import CreateScheduleOutput20240611
from openapi_client.models.create_team_event_type_input20240614 import CreateTeamEventTypeInput20240614
from openapi_client.models.create_team_event_type_output import CreateTeamEventTypeOutput
from openapi_client.models.create_team_event_type_output_data import CreateTeamEventTypeOutputData
from openapi_client.models.create_webhook_input_dto import CreateWebhookInputDto
from openapi_client.models.data import Data
from openapi_client.models.data_dto import DataDto
from openapi_client.models.delete_attribute_option_output import DeleteAttributeOptionOutput
from openapi_client.models.delete_calendar_credentials_input_body_dto import DeleteCalendarCredentialsInputBodyDto
from openapi_client.models.delete_data20240614 import DeleteData20240614
from openapi_client.models.delete_event_type_output20240614 import DeleteEventTypeOutput20240614
from openapi_client.models.delete_many_webhooks_output_response_dto import DeleteManyWebhooksOutputResponseDto
from openapi_client.models.delete_org_membership import DeleteOrgMembership
from openapi_client.models.delete_organization_attributes_output import DeleteOrganizationAttributesOutput
from openapi_client.models.delete_schedule_output20240611 import DeleteScheduleOutput20240611
from openapi_client.models.delete_team_event_type_output import DeleteTeamEventTypeOutput
from openapi_client.models.deleted_calendar_credentials_output_dto import DeletedCalendarCredentialsOutputDto
from openapi_client.models.deleted_calendar_credentials_output_response_dto import DeletedCalendarCredentialsOutputResponseDto
from openapi_client.models.destination_calendar import DestinationCalendar
from openapi_client.models.destination_calendar20240614 import DestinationCalendar20240614
from openapi_client.models.destination_calendars_input_body_dto import DestinationCalendarsInputBodyDto
from openapi_client.models.destination_calendars_output_dto import DestinationCalendarsOutputDto
from openapi_client.models.destination_calendars_output_response_dto import DestinationCalendarsOutputResponseDto
from openapi_client.models.disabled20240614 import Disabled20240614
from openapi_client.models.email_default_field_output20240614 import EmailDefaultFieldOutput20240614
from openapi_client.models.event_type import EventType
from openapi_client.models.event_type_color20240614 import EventTypeColor20240614
from openapi_client.models.event_type_output20240614 import EventTypeOutput20240614
from openapi_client.models.event_type_output20240614_booking_fields_inner import EventTypeOutput20240614BookingFieldsInner
from openapi_client.models.event_type_output20240614_booking_window_inner import EventTypeOutput20240614BookingWindowInner
from openapi_client.models.event_type_webhook_output_dto import EventTypeWebhookOutputDto
from openapi_client.models.event_type_webhook_output_response_dto import EventTypeWebhookOutputResponseDto
from openapi_client.models.event_type_webhooks_output_response_dto import EventTypeWebhooksOutputResponseDto
from openapi_client.models.exchange_authorization_code_input import ExchangeAuthorizationCodeInput
from openapi_client.models.gcal_auth_url_output import GcalAuthUrlOutput
from openapi_client.models.gcal_check_output import GcalCheckOutput
from openapi_client.models.gcal_save_redirect_output import GcalSaveRedirectOutput
from openapi_client.models.get_all_attribute_option_output import GetAllAttributeOptionOutput
from openapi_client.models.get_all_org_memberships import GetAllOrgMemberships
from openapi_client.models.get_booking_output20240813 import GetBookingOutput20240813
from openapi_client.models.get_booking_output20240813_data import GetBookingOutput20240813Data
from openapi_client.models.get_bookings_output20240813 import GetBookingsOutput20240813
from openapi_client.models.get_bookings_output20240813_data_inner import GetBookingsOutput20240813DataInner
from openapi_client.models.get_busy_times_output import GetBusyTimesOutput
from openapi_client.models.get_default_schedule_output20240611 import GetDefaultScheduleOutput20240611
from openapi_client.models.get_event_type_output20240614 import GetEventTypeOutput20240614
from openapi_client.models.get_event_types_output20240614 import GetEventTypesOutput20240614
from openapi_client.models.get_managed_user_output import GetManagedUserOutput
from openapi_client.models.get_managed_users_output import GetManagedUsersOutput
from openapi_client.models.get_me_output import GetMeOutput
from openapi_client.models.get_o_auth_client_response_dto import GetOAuthClientResponseDto
from openapi_client.models.get_o_auth_clients_response_dto import GetOAuthClientsResponseDto
from openapi_client.models.get_option_user_output import GetOptionUserOutput
from openapi_client.models.get_option_user_output_data import GetOptionUserOutputData
from openapi_client.models.get_org_membership import GetOrgMembership
from openapi_client.models.get_organization_attributes_output import GetOrganizationAttributesOutput
from openapi_client.models.get_organization_user_output import GetOrganizationUserOutput
from openapi_client.models.get_organization_users_output import GetOrganizationUsersOutput
from openapi_client.models.get_schedule_output20240611 import GetScheduleOutput20240611
from openapi_client.models.get_schedules_output20240611 import GetSchedulesOutput20240611
from openapi_client.models.get_single_attribute_output import GetSingleAttributeOutput
from openapi_client.models.get_team_event_type_output import GetTeamEventTypeOutput
from openapi_client.models.get_team_event_types_output import GetTeamEventTypesOutput
from openapi_client.models.get_user_output import GetUserOutput
from openapi_client.models.guests_default_field_output20240614 import GuestsDefaultFieldOutput20240614
from openapi_client.models.host import Host
from openapi_client.models.integration import Integration
from openapi_client.models.integration_location20240614 import IntegrationLocation20240614
from openapi_client.models.keys_dto import KeysDto
from openapi_client.models.keys_response_dto import KeysResponseDto
from openapi_client.models.link_location20240614 import LinkLocation20240614
from openapi_client.models.location_default_field_output20240614 import LocationDefaultFieldOutput20240614
from openapi_client.models.managed_user_output import ManagedUserOutput
from openapi_client.models.mark_absent_booking_input20240813 import MarkAbsentBookingInput20240813
from openapi_client.models.mark_absent_booking_output20240813 import MarkAbsentBookingOutput20240813
from openapi_client.models.me_org_output import MeOrgOutput
from openapi_client.models.me_output import MeOutput
from openapi_client.models.multi_email_field_input20240614 import MultiEmailFieldInput20240614
from openapi_client.models.multi_email_field_output20240614 import MultiEmailFieldOutput20240614
from openapi_client.models.multi_select_field_input20240614 import MultiSelectFieldInput20240614
from openapi_client.models.multi_select_field_output20240614 import MultiSelectFieldOutput20240614
from openapi_client.models.name_default_field_output20240614 import NameDefaultFieldOutput20240614
from openapi_client.models.notes_default_field_output20240614 import NotesDefaultFieldOutput20240614
from openapi_client.models.notice_threshold20240614 import NoticeThreshold20240614
from openapi_client.models.number_field_input20240614 import NumberFieldInput20240614
from openapi_client.models.number_field_output20240614 import NumberFieldOutput20240614
from openapi_client.models.o_auth_authorize_input import OAuthAuthorizeInput
from openapi_client.models.o_auth_client_webhook_output_dto import OAuthClientWebhookOutputDto
from openapi_client.models.o_auth_client_webhook_output_response_dto import OAuthClientWebhookOutputResponseDto
from openapi_client.models.o_auth_client_webhooks_output_response_dto import OAuthClientWebhooksOutputResponseDto
from openapi_client.models.option_output import OptionOutput
from openapi_client.models.org_me_teams_output_response_dto import OrgMeTeamsOutputResponseDto
from openapi_client.models.org_membership_output_dto import OrgMembershipOutputDto
from openapi_client.models.org_team_membership_output_dto import OrgTeamMembershipOutputDto
from openapi_client.models.org_team_membership_output_response_dto import OrgTeamMembershipOutputResponseDto
from openapi_client.models.org_team_memberships_output_response_dto import OrgTeamMembershipsOutputResponseDto
from openapi_client.models.org_team_output_dto import OrgTeamOutputDto
from openapi_client.models.org_team_output_response_dto import OrgTeamOutputResponseDto
from openapi_client.models.org_teams_output_response_dto import OrgTeamsOutputResponseDto
from openapi_client.models.phone_field_input20240614 import PhoneFieldInput20240614
from openapi_client.models.phone_field_output20240614 import PhoneFieldOutput20240614
from openapi_client.models.phone_location20240614 import PhoneLocation20240614
from openapi_client.models.platform_o_auth_client_dto import PlatformOAuthClientDto
from openapi_client.models.primary import Primary
from openapi_client.models.provider_verify_access_token_output import ProviderVerifyAccessTokenOutput
from openapi_client.models.provider_verify_client_data import ProviderVerifyClientData
from openapi_client.models.provider_verify_client_output import ProviderVerifyClientOutput
from openapi_client.models.radio_group_field_input20240614 import RadioGroupFieldInput20240614
from openapi_client.models.radio_group_field_output20240614 import RadioGroupFieldOutput20240614
from openapi_client.models.range_window20240614 import RangeWindow20240614
from openapi_client.models.recurrence20240614 import Recurrence20240614
from openapi_client.models.recurring_booking_output20240813 import RecurringBookingOutput20240813
from openapi_client.models.refresh_token_input import RefreshTokenInput
from openapi_client.models.reschedule_booking_input20240813 import RescheduleBookingInput20240813
from openapi_client.models.reschedule_booking_output20240813 import RescheduleBookingOutput20240813
from openapi_client.models.reschedule_booking_output20240813_data import RescheduleBookingOutput20240813Data
from openapi_client.models.reschedule_reason_default_field_output20240614 import RescheduleReasonDefaultFieldOutput20240614
from openapi_client.models.reserve_slot_input import ReserveSlotInput
from openapi_client.models.schedule_availability_input20240611 import ScheduleAvailabilityInput20240611
from openapi_client.models.schedule_output20240611 import ScheduleOutput20240611
from openapi_client.models.schedule_override_input20240611 import ScheduleOverrideInput20240611
from openapi_client.models.seats20240614 import Seats20240614
from openapi_client.models.select_field_input20240614 import SelectFieldInput20240614
from openapi_client.models.select_field_output20240614 import SelectFieldOutput20240614
from openapi_client.models.selected_calendar_output_dto import SelectedCalendarOutputDto
from openapi_client.models.selected_calendar_output_response_dto import SelectedCalendarOutputResponseDto
from openapi_client.models.selected_calendars_input_dto import SelectedCalendarsInputDto
from openapi_client.models.set_default_conferencing_app_output_response_dto import SetDefaultConferencingAppOutputResponseDto
from openapi_client.models.slots_controller_delete_selected_slot200_response import SlotsControllerDeleteSelectedSlot200Response
from openapi_client.models.slots_controller_get_available_slots200_response import SlotsControllerGetAvailableSlots200Response
from openapi_client.models.slots_controller_get_available_slots200_response_data import SlotsControllerGetAvailableSlots200ResponseData
from openapi_client.models.slots_controller_get_available_slots200_response_data_slots_value_inner import SlotsControllerGetAvailableSlots200ResponseDataSlotsValueInner
from openapi_client.models.slots_controller_reserve_slot201_response import SlotsControllerReserveSlot201Response
from openapi_client.models.slots_controller_reserve_slot201_response_data import SlotsControllerReserveSlot201ResponseData
from openapi_client.models.strip_connect_output_dto import StripConnectOutputDto
from openapi_client.models.strip_connect_output_response_dto import StripConnectOutputResponseDto
from openapi_client.models.strip_credentials_check_output_response_dto import StripCredentialsCheckOutputResponseDto
from openapi_client.models.strip_credentials_save_output_response_dto import StripCredentialsSaveOutputResponseDto
from openapi_client.models.team_event_type_output20240614 import TeamEventTypeOutput20240614
from openapi_client.models.team_event_type_response_host import TeamEventTypeResponseHost
from openapi_client.models.team_webhook_output_dto import TeamWebhookOutputDto
from openapi_client.models.team_webhook_output_response_dto import TeamWebhookOutputResponseDto
from openapi_client.models.team_webhooks_output_response_dto import TeamWebhooksOutputResponseDto
from openapi_client.models.text_area_field_input20240614 import TextAreaFieldInput20240614
from openapi_client.models.text_area_field_output20240614 import TextAreaFieldOutput20240614
from openapi_client.models.text_field_input20240614 import TextFieldInput20240614
from openapi_client.models.text_field_output20240614 import TextFieldOutput20240614
from openapi_client.models.title_default_field_output20240614 import TitleDefaultFieldOutput20240614
from openapi_client.models.unassign_option_user_output import UnassignOptionUserOutput
from openapi_client.models.update_attribute_option_output import UpdateAttributeOptionOutput
from openapi_client.models.update_event_type_input20240614 import UpdateEventTypeInput20240614
from openapi_client.models.update_event_type_output20240614 import UpdateEventTypeOutput20240614
from openapi_client.models.update_managed_user_input import UpdateManagedUserInput
from openapi_client.models.update_me_output import UpdateMeOutput
from openapi_client.models.update_o_auth_client_input import UpdateOAuthClientInput
from openapi_client.models.update_org_membership import UpdateOrgMembership
from openapi_client.models.update_org_membership_dto import UpdateOrgMembershipDto
from openapi_client.models.update_org_team_dto import UpdateOrgTeamDto
from openapi_client.models.update_org_team_membership_dto import UpdateOrgTeamMembershipDto
from openapi_client.models.update_organization_attribute_input import UpdateOrganizationAttributeInput
from openapi_client.models.update_organization_attribute_option_input import UpdateOrganizationAttributeOptionInput
from openapi_client.models.update_organization_attributes_output import UpdateOrganizationAttributesOutput
from openapi_client.models.update_schedule_input20240611 import UpdateScheduleInput20240611
from openapi_client.models.update_schedule_output20240611 import UpdateScheduleOutput20240611
from openapi_client.models.update_team_event_type_input20240614 import UpdateTeamEventTypeInput20240614
from openapi_client.models.update_team_event_type_output import UpdateTeamEventTypeOutput
from openapi_client.models.update_webhook_input_dto import UpdateWebhookInputDto
from openapi_client.models.user_webhook_output_dto import UserWebhookOutputDto
from openapi_client.models.user_webhook_output_response_dto import UserWebhookOutputResponseDto
from openapi_client.models.user_webhooks_output_response_dto import UserWebhooksOutputResponseDto
