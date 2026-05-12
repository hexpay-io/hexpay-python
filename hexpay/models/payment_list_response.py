from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.payment_response import PaymentResponse


T = TypeVar("T", bound="PaymentListResponse")


@_attrs_define
class PaymentListResponse:
    """Paginated list of payments with cursor-based navigation metadata.

    Attributes:
        payments (list[PaymentResponse]): Array of payment objects for the current page.
        cursor (str | Unset): Opaque pagination cursor. Present only when there are more pages of results.
            Pass this value as the `cursor` query parameter to retrieve the next page.
            When absent, the current page is the last one.
             Example: eyJpZCI6IjAxOTMyN2M2LTIwNTgtNzkwMS1iMjM0LTU2Nzg5YWJjZGVmZiJ9.
    """

    payments: list[PaymentResponse]
    cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.payment_response import PaymentResponse

        payments = []
        for payments_item_data in self.payments:
            payments_item = payments_item_data.to_dict()
            payments.append(payments_item)

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payments": payments,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_response import PaymentResponse

        d = dict(src_dict)
        payments = []
        _payments = d.pop("payments")
        for payments_item_data in _payments:
            payments_item = PaymentResponse.from_dict(payments_item_data)

            payments.append(payments_item)

        cursor = d.pop("cursor", UNSET)

        payment_list_response = cls(
            payments=payments,
            cursor=cursor,
        )

        payment_list_response.additional_properties = d
        return payment_list_response

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
