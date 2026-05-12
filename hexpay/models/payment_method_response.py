from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID

if TYPE_CHECKING:
    from ..models.chain_response import ChainResponse
    from ..models.coin_response import CoinResponse


T = TypeVar("T", bound="PaymentMethodResponse")


@_attrs_define
class PaymentMethodResponse:
    """A single payment method — a coin + chain combination accepted by the store.
    The `coin.symbol` / `chain.symbol` pair uniquely identifies the method for
    use in `payment_options.methods` filters.

        Attributes:
            id (UUID): Unique identifier for this payment method configuration. Example:
                0197ef69-6825-7bb4-8cd8-770ab407e240.
            coin (CoinResponse): Cryptocurrency (coin) metadata.
            chain (ChainResponse): Blockchain network metadata. Currently only TON is supported.
    """

    id: UUID
    coin: CoinResponse
    chain: ChainResponse
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.chain_response import ChainResponse
        from ..models.coin_response import CoinResponse

        id = str(self.id)

        coin = self.coin.to_dict()

        chain = self.chain.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "coin": coin,
                "chain": chain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chain_response import ChainResponse
        from ..models.coin_response import CoinResponse

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        coin = CoinResponse.from_dict(d.pop("coin"))

        chain = ChainResponse.from_dict(d.pop("chain"))

        payment_method_response = cls(
            id=id,
            coin=coin,
            chain=chain,
        )

        payment_method_response.additional_properties = d
        return payment_method_response

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
