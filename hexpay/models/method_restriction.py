from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.method_restriction_chain import MethodRestrictionChain
from ..models.method_restriction_coin import MethodRestrictionCoin


T = TypeVar("T", bound="MethodRestriction")


@_attrs_define
class MethodRestriction:
    """A payment method allowed for this payment, identified by coin and chain.
    Both `coin` and `chain` are required.

    Use the exact `symbol` values returned by `GET /v1/payment-methods`.
    Values are case-sensitive.

        Attributes:
            coin (MethodRestrictionCoin): Coin ticker. Must be a coin supported by HexPay on TON. Example: USDT.
            chain (MethodRestrictionChain): Chain ticker. Currently only `TON` is supported. Example: TON.
    """

    coin: MethodRestrictionCoin
    chain: MethodRestrictionChain
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        coin = self.coin.value

        chain = self.chain.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "coin": coin,
                "chain": chain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        coin = MethodRestrictionCoin(d.pop("coin"))

        chain = MethodRestrictionChain(d.pop("chain"))

        method_restriction = cls(
            coin=coin,
            chain=chain,
        )

        method_restriction.additional_properties = d
        return method_restriction

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
