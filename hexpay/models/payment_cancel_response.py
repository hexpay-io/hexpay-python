from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.payment_status import PaymentStatus


T = TypeVar("T", bound="PaymentCancelResponse")


@_attrs_define
class PaymentCancelResponse:
    """
    Attributes:
        status (PaymentStatus): Lifecycle status of a payment:
            - `created`   — Payment created; customer has not yet selected a payment method.
              `paymentDetails` is absent.
            - `pending`   — Method confirmed; `paymentDetails` populated with the blockchain
              address and exact coin amount. Awaiting on-chain transfer.
            - `completed` — On-chain transfer confirmed. `transactionSignatures` are present.
            - `expired`   — Payment TTL elapsed without a confirmed transfer. Reachable from
              **both** `created` (customer never selected a method) and `pending` (customer
              selected but did not send the transfer in time).
            - `cancelled` — Canceled by the merchant via `POST /v1/payments/{id}/cancel`.
              Reachable from both `created` and `pending`.
             Example: created.
    """

    status: PaymentStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = PaymentStatus(d.pop("status"))

        payment_cancel_response = cls(
            status=status,
        )

        payment_cancel_response.additional_properties = d
        return payment_cancel_response

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
