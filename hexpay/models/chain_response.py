from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.chain_response_symbol import ChainResponseSymbol


T = TypeVar("T", bound="ChainResponse")


@_attrs_define
class ChainResponse:
    """Blockchain network metadata. Currently only TON is supported.

    Attributes:
        name (str): Human-readable name of the blockchain network. Example: TON.
        symbol (ChainResponseSymbol): Ticker symbol. Use this value as the `chain` field in
            `payment_options.methods` when creating payments.
             Example: TON.
        img_url (str): URL of the chain logo image. Example: https://assets.hexpay.io/chains/ton.svg.
    """

    name: str
    symbol: ChainResponseSymbol
    img_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        symbol = self.symbol.value

        img_url = self.img_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "symbol": symbol,
                "imgUrl": img_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        symbol = ChainResponseSymbol(d.pop("symbol"))

        img_url = d.pop("imgUrl")

        chain_response = cls(
            name=name,
            symbol=symbol,
            img_url=img_url,
        )

        chain_response.additional_properties = d
        return chain_response

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
