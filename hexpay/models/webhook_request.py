from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.webhook_payload import WebhookPayload


T = TypeVar("T", bound="WebhookRequest")


@_attrs_define
class WebhookRequest:
    """Body of the webhook HexPay POSTs to `webhookUrl` when a payment reaches
    `completed`. Signed with Ed25519; the signature is in the `X-Signature`
    header and the key ID in `X-Signature-Kid`.

        Attributes:
            payload (WebhookPayload):
            sign_at (datetime.datetime): Signing timestamp (RFC 3339, UTC). Example: 2026-01-20T10:12:00Z.
    """

    payload: WebhookPayload
    sign_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_payload import WebhookPayload

        payload = self.payload.to_dict()

        sign_at = self.sign_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payload": payload,
                "signAt": sign_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_payload import WebhookPayload

        d = dict(src_dict)
        payload = WebhookPayload.from_dict(d.pop("payload"))

        sign_at = isoparse(d.pop("signAt"))

        webhook_request = cls(
            payload=payload,
            sign_at=sign_at,
        )

        webhook_request.additional_properties = d
        return webhook_request

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
