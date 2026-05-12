from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime


T = TypeVar("T", bound="PaymentTimerResponse")


@_attrs_define
class PaymentTimerResponse:
    """Lifecycle timing information for the payment.

    Attributes:
        created_at (datetime.datetime): Payment creation timestamp in RFC 3339 format (UTC). Example:
            2026-01-20T10:00:00Z.
        expires_at (datetime.datetime): Timestamp (RFC 3339, UTC) at which the payment automatically moves to
            `expired` status. Subtract `createdAt` to derive the total TTL window.
             Example: 2026-01-20T10:15:00Z.
        paid_at (datetime.datetime | Unset): Timestamp (RFC 3339, UTC) at which the payment has been paid
             Example: 2026-01-20T10:12:00Z.
    """

    created_at: datetime.datetime
    expires_at: datetime.datetime
    paid_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        paid_at: str | Unset = UNSET
        if not isinstance(self.paid_at, Unset):
            paid_at = self.paid_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "expiresAt": expires_at,
            }
        )
        if paid_at is not UNSET:
            field_dict["paidAt"] = paid_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        expires_at = isoparse(d.pop("expiresAt"))

        _paid_at = d.pop("paidAt", UNSET)
        paid_at: datetime.datetime | Unset
        if isinstance(_paid_at, Unset):
            paid_at = UNSET
        else:
            paid_at = isoparse(_paid_at)

        payment_timer_response = cls(
            created_at=created_at,
            expires_at=expires_at,
            paid_at=paid_at,
        )

        payment_timer_response.additional_properties = d
        return payment_timer_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
