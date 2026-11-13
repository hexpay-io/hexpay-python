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
        data (list[PaymentResponse]): Array of payment objects for the current page.
        cursor (str | Unset): Opaque pagination cursor. Present only when there are more pages of results.
            Pass this value unchanged as the `cursor` query parameter to retrieve the
            next page. When absent, the current page is the last one.
             Example: 019327c6-1234-7901-b234-56789abcde00.
    """

    data: list[PaymentResponse]
    cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.payment_response import PaymentResponse

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_response import PaymentResponse

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = PaymentResponse.from_dict(data_item_data)

            data.append(data_item)

        cursor = d.pop("cursor", UNSET)

        payment_list_response = cls(
            data=data,
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
