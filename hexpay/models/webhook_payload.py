from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.webhook_payload_status import WebhookPayloadStatus
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
    from ..models.webhook_payload_metadata_type_0 import WebhookPayloadMetadataType0


T = TypeVar("T", bound="WebhookPayload")


@_attrs_define
class WebhookPayload:
    """
    Attributes:
        payment_id (UUID): Payment identifier. Example: 019327c6-2058-7901-b234-56789abcdeff.
        status (WebhookPayloadStatus): Payment status. Always `completed`. Example: completed.
        order_id (None | str): Merchant order identifier from the create request, or `null`. Example: order-2026-00123.
        metadata (None | WebhookPayloadMetadataType0): Metadata from the create request, or `null`. Example:
            {'customer_id': 'cust_abc123'}.
    """

    payment_id: UUID
    status: WebhookPayloadStatus
    order_id: None | str
    metadata: None | WebhookPayloadMetadataType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_payload_metadata_type_0 import WebhookPayloadMetadataType0

        payment_id = str(self.payment_id)

        status = self.status.value

        order_id: None | str
        order_id = self.order_id

        metadata: dict[str, Any] | None
        if isinstance(self.metadata, WebhookPayloadMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paymentId": payment_id,
                "status": status,
                "orderId": order_id,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_payload_metadata_type_0 import WebhookPayloadMetadataType0

        d = dict(src_dict)
        payment_id = UUID(d.pop("paymentId"))

        status = WebhookPayloadStatus(d.pop("status"))

        def _parse_order_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        order_id = _parse_order_id(d.pop("orderId"))

        def _parse_metadata(data: object) -> None | WebhookPayloadMetadataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = WebhookPayloadMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WebhookPayloadMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata"))

        webhook_payload = cls(
            payment_id=payment_id,
            status=status,
            order_id=order_id,
            metadata=metadata,
        )

        webhook_payload.additional_properties = d
        return webhook_payload

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
