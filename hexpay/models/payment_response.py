from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.payment_status import PaymentStatus
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
    from ..models.payment_details import PaymentDetails
    from ..models.payment_timer_response import PaymentTimerResponse


T = TypeVar("T", bound="PaymentResponse")


@_attrs_define
class PaymentResponse:
    """Full payment object. Returned by the create, retrieve, list, and cancel endpoints.

    Attributes:
        id (UUID): Unique payment identifier. Example: 019327c6-2058-7901-b234-56789abcdeff.
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
        amount (str): The denomination amount recorded at creation time. Mirrors the `amount`
            field from the create request.
             Example: 100.00.
        currency (str): The denomination currency ticker recorded at creation time. Mirrors the
            `currency` field from the create request. May be a fiat code or a coin ticker.
             Example: USD.
        timer (PaymentTimerResponse): Lifecycle timing information for the payment.
        payment_details (PaymentDetails | Unset): Cryptocurrency payment instructions. Populated when the payment
            transitions
            from `created` to `pending`.

            The customer must send exactly `coinAmount` of `coin` to `address` on the
            TON blockchain.
        checkout_url (str | Unset): URL of the HexPay-hosted checkout page for this payment. Redirect the
            customer to this URL to let them complete the payment.
             Example: https://payment.hexpay.io/019327c6-2058-7901-b234-56789abcdeff.
        order_id (str | Unset): Merchant-defined external order identifier, if provided at creation. Example:
            order-2026-00123.
        description (str | Unset): Payment description Example: Premium subscription — 1 year.
    """

    id: UUID
    status: PaymentStatus
    amount: str
    currency: str
    timer: PaymentTimerResponse
    payment_details: PaymentDetails | Unset = UNSET
    checkout_url: str | Unset = UNSET
    order_id: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.payment_details import PaymentDetails
        from ..models.payment_timer_response import PaymentTimerResponse

        id = str(self.id)

        status = self.status.value

        amount = self.amount

        currency = self.currency

        timer = self.timer.to_dict()

        payment_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payment_details, Unset):
            payment_details = self.payment_details.to_dict()

        checkout_url = self.checkout_url

        order_id = self.order_id

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "amount": amount,
                "currency": currency,
                "timer": timer,
            }
        )
        if payment_details is not UNSET:
            field_dict["paymentDetails"] = payment_details
        if checkout_url is not UNSET:
            field_dict["checkoutURL"] = checkout_url
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_details import PaymentDetails
        from ..models.payment_timer_response import PaymentTimerResponse

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = PaymentStatus(d.pop("status"))

        amount = d.pop("amount")

        currency = d.pop("currency")

        timer = PaymentTimerResponse.from_dict(d.pop("timer"))

        _payment_details = d.pop("paymentDetails", UNSET)
        payment_details: PaymentDetails | Unset
        if isinstance(_payment_details, Unset):
            payment_details = UNSET
        else:
            payment_details = PaymentDetails.from_dict(_payment_details)

        checkout_url = d.pop("checkoutURL", UNSET)

        order_id = d.pop("order_id", UNSET)

        description = d.pop("description", UNSET)

        payment_response = cls(
            id=id,
            status=status,
            amount=amount,
            currency=currency,
            timer=timer,
            payment_details=payment_details,
            checkout_url=checkout_url,
            order_id=order_id,
            description=description,
        )

        payment_response.additional_properties = d
        return payment_response

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
