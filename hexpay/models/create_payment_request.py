from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.create_payment_request_metadata import CreatePaymentRequestMetadata
    from ..models.payment_options import PaymentOptions


T = TypeVar("T", bound="CreatePaymentRequest")


@_attrs_define
class CreatePaymentRequest:
    """Request body for creating a new payment. The body is intentionally flat:
    `amount`, `currency`, and all optional fields are top-level. The only nested
    structure is `payment_options.methods`, which describes an allowlist of
    acceptable payment methods.

        Attributes:
            amount (str): The payment value as a positive decimal string. No leading zeros are
                permitted on the integer part (`"007"` is invalid; use `"7"`).
                For fiat currencies up to 2 decimal places are recommended.
                For crypto tickers precision depends on the coin.
                 Example: 100.00.
            currency (str): Ticker symbol for the denomination. Accepts fiat codes (e.g. `USD`, `EUR`,
                `RUB`) or TON-ecosystem coin tickers (e.g. `TON`, `USDT`).

                This field defines the **unit of value** — it does not determine the coin
                the customer pays with. Payment coin is controlled by `payment_options.methods`.

                For the full list of accepted values use `GET /v1/payment-methods` (coins)
                or refer to the supported fiat codes in your store settings.
                 Example: USD.
            payment_options (PaymentOptions | Unset): Optional constraints on which payment methods are available at
                checkout.
                When omitted entirely, all payment methods enabled for your store are shown
                and the payment is created in `created` status.
            ttl (int | Unset): Time-to-live in seconds. Defines how long the payment remains active
                from the moment of creation. Once the TTL elapses the payment moves to
                `expired` status — this can happen from either `created` or `pending`.

                Minimum: `900` (15 minutes). Maximum: `43200` (12 hours).
                Defaults to `3600` (1 hour) if not specified.
                 Default: 3600. Example: 3600.
            order_id (str | Unset): Merchant-defined external order identifier. Use this to correlate a HexPay
                payment with your internal order or invoice system. Returned on all payment
                objects and included in webhook payloads.
                 Example: order-2026-00123.
            description (str | Unset): Human-readable description of the payment purpose. May be displayed to
                the customer on the payment page.
                 Example: Premium subscription — 1 year.
            metadata (CreatePaymentRequestMetadata | Unset): Arbitrary key-value pairs for merchant use. All values must be
                strings.
                Returned on all payment objects and included in webhook payloads.
                Maximum 10 keys; key names up to 64 characters, values up to 512 characters.
                 Example: {'customer_id': 'cust_abc123', 'customer_email': 'customer@example.com'}.
            webhook_url (str | Unset): HTTPS URL to which HexPay will POST webhook notifications for this
                payment's lifecycle events (e.g., transitions to `pending` or `completed`).

                Requirements:
                - Must use HTTPS. Plain HTTP URLs are rejected.
                - Must be publicly reachable from the internet. Loopback addresses
                  (`localhost`, `127.x.x.x`) and private network ranges (`10.x.x.x`,
                  `192.168.x.x`, `172.16–31.x.x`) are not allowed.
                - Make sure your server is configured to accept POST requests at this URL
                  before creating payments.
                 Example: https://merchant.com/webhooks/hexpay.
    """

    amount: str
    currency: str
    payment_options: PaymentOptions | Unset = UNSET
    ttl: int | Unset = 3600
    order_id: str | Unset = UNSET
    description: str | Unset = UNSET
    metadata: CreatePaymentRequestMetadata | Unset = UNSET
    webhook_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_payment_request_metadata import CreatePaymentRequestMetadata
        from ..models.payment_options import PaymentOptions

        amount = self.amount

        currency = self.currency

        payment_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payment_options, Unset):
            payment_options = self.payment_options.to_dict()

        ttl = self.ttl

        order_id = self.order_id

        description = self.description

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        webhook_url = self.webhook_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "currency": currency,
            }
        )
        if payment_options is not UNSET:
            field_dict["payment_options"] = payment_options
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if webhook_url is not UNSET:
            field_dict["webhookURL"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_payment_request_metadata import CreatePaymentRequestMetadata
        from ..models.payment_options import PaymentOptions

        d = dict(src_dict)
        amount = d.pop("amount")

        currency = d.pop("currency")

        _payment_options = d.pop("payment_options", UNSET)
        payment_options: PaymentOptions | Unset
        if isinstance(_payment_options, Unset):
            payment_options = UNSET
        else:
            payment_options = PaymentOptions.from_dict(_payment_options)

        ttl = d.pop("ttl", UNSET)

        order_id = d.pop("order_id", UNSET)

        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreatePaymentRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreatePaymentRequestMetadata.from_dict(_metadata)

        webhook_url = d.pop("webhookURL", UNSET)

        create_payment_request = cls(
            amount=amount,
            currency=currency,
            payment_options=payment_options,
            ttl=ttl,
            order_id=order_id,
            description=description,
            metadata=metadata,
            webhook_url=webhook_url,
        )

        create_payment_request.additional_properties = d
        return create_payment_request

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
