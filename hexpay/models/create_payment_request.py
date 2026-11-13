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
    structure is `paymentOptions.methods`, which restricts the payment methods
    offered to the customer.

        Attributes:
            amount (str): The payment value as a positive decimal string. Zero is not allowed.
                No leading zeros are permitted on the integer part (`"007"` is invalid; use `"7"`).
                For fiat currencies up to 2 decimal places are recommended.
                For crypto tickers precision depends on the coin.
                 Example: 100.00.
            currency (str): Ticker symbol for the denomination. Accepts fiat codes (`USD`, `EUR`, `RUB`)
                or TON-ecosystem coin tickers (`TON`, `USDT`, `NOT`, `DOGS`, `BUILD`, `BLUM`,
                `DUST`, `DYOR`, `STON`, `XAUt0`).

                This field defines the **unit of value** — it does not determine the coin
                the customer pays with. Payment coin is controlled by `paymentOptions.methods`.

                Any supported ticker is accepted, regardless of which payment methods are
                enabled for your store.
                 Example: USD.
            payment_options (PaymentOptions | Unset): Optional restriction on which payment methods are offered at checkout.
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
                objects and included in the webhook payload.
                 Example: order-2026-00123.
            description (str | Unset): Human-readable description of the payment purpose. May be displayed to
                the customer on the payment page.
                 Example: Premium subscription — 1 year.
            metadata (CreatePaymentRequestMetadata | Unset): Arbitrary key-value pairs for merchant use. All values must be
                strings.
                Returned on all payment objects and included in the webhook payload.
                Maximum 10 keys; key names up to 64 characters, values up to 512 characters.
                Keys are stored as provided and are not renamed.
                 Example: {'customer_id': 'cust_abc123', 'customer_email': 'customer@example.com'}.
            webhook_url (str | Unset): HTTPS URL to which HexPay will POST a webhook notification when this
                payment reaches `completed` status. No webhooks are sent for other statuses.

                Requirements:
                - Must use HTTPS. Plain HTTP URLs are rejected.
                - Must be publicly reachable from the internet. Non-public addresses are
                  rejected, and host names that resolve to them are blocked at delivery time.
                - Make sure your server is configured to accept POST requests at this URL
                  before creating payments.
                 Example: https://merchant.com/webhooks/hexpay.
            redirect_url (str | Unset): HTTPS URL of your page (e.g. the order page) that the checkout page links to
                once the payment is finished (`completed`, `expired` or `cancelled`), so the
                customer can return to your store.

                Requirements:
                - Must be an absolute HTTPS URL. Plain HTTP and other schemes are rejected.
                - Maximum 512 characters.

                If omitted, the checkout page uses the default HexPay URL.
                 Example: https://merchant.com/orders/order-2026-00123.
    """

    amount: str
    currency: str
    payment_options: PaymentOptions | Unset = UNSET
    ttl: int | Unset = 3600
    order_id: str | Unset = UNSET
    description: str | Unset = UNSET
    metadata: CreatePaymentRequestMetadata | Unset = UNSET
    webhook_url: str | Unset = UNSET
    redirect_url: str | Unset = UNSET
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

        redirect_url = self.redirect_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "currency": currency,
            }
        )
        if payment_options is not UNSET:
            field_dict["paymentOptions"] = payment_options
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url
        if redirect_url is not UNSET:
            field_dict["redirectUrl"] = redirect_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_payment_request_metadata import CreatePaymentRequestMetadata
        from ..models.payment_options import PaymentOptions

        d = dict(src_dict)
        amount = d.pop("amount")

        currency = d.pop("currency")

        _payment_options = d.pop("paymentOptions", UNSET)
        payment_options: PaymentOptions | Unset
        if isinstance(_payment_options, Unset):
            payment_options = UNSET
        else:
            payment_options = PaymentOptions.from_dict(_payment_options)

        ttl = d.pop("ttl", UNSET)

        order_id = d.pop("orderId", UNSET)

        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreatePaymentRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreatePaymentRequestMetadata.from_dict(_metadata)

        webhook_url = d.pop("webhookUrl", UNSET)

        redirect_url = d.pop("redirectUrl", UNSET)

        create_payment_request = cls(
            amount=amount,
            currency=currency,
            payment_options=payment_options,
            ttl=ttl,
            order_id=order_id,
            description=description,
            metadata=metadata,
            webhook_url=webhook_url,
            redirect_url=redirect_url,
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
