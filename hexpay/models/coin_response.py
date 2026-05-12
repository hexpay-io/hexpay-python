from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.coin_response_symbol import CoinResponseSymbol


T = TypeVar("T", bound="CoinResponse")


@_attrs_define
class CoinResponse:
    """Cryptocurrency (coin) metadata.

    Attributes:
        name (str): Human-readable name of the cryptocurrency. Example: Tether.
        symbol (CoinResponseSymbol): Ticker symbol. Use this value as the `coin` field in
            `payment_options.methods` when creating payments.
             Example: USDT.
        img_url (str): URL of the coin logo image. Example: https://assets.hexpay.io/coins/usdt.svg.
    """

    name: str
    symbol: CoinResponseSymbol
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

        symbol = CoinResponseSymbol(d.pop("symbol"))

        img_url = d.pop("imgUrl")

        coin_response = cls(
            name=name,
            symbol=symbol,
            img_url=img_url,
        )

        coin_response.additional_properties = d
        return coin_response

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
