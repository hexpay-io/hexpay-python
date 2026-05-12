from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.chain_response import ChainResponse
    from ..models.coin_response import CoinResponse


T = TypeVar("T", bound="PaymentDetails")


@_attrs_define
class PaymentDetails:
    """Cryptocurrency payment instructions. Populated when the payment transitions
    from `created` to `pending`.

    The customer must send exactly `coinAmount` of `coin` to `address` on the
    TON blockchain.

        Attributes:
            address (str): TON blockchain address the customer must send the cryptocurrency to. Example:
                UQBf_DO8wsBddOcMnGEOyREEHPPKMBL2F26GQFOV7FQdYY_a.
            coin_amount (str): Exact cryptocurrency amount the customer must transfer. Sending less
                than this amount will result in an underpayment.
                 Example: 35.782.
            coin (CoinResponse): Cryptocurrency (coin) metadata.
            chain (ChainResponse): Blockchain network metadata. Currently only TON is supported.
            transaction_signatures (list[str] | Unset): On-chain transaction hash(es) confirming the payment.
                Present only when status is `completed`.
                 Example: ['a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2'].
    """

    address: str
    coin_amount: str
    coin: CoinResponse
    chain: ChainResponse
    transaction_signatures: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.chain_response import ChainResponse
        from ..models.coin_response import CoinResponse

        address = self.address

        coin_amount = self.coin_amount

        coin = self.coin.to_dict()

        chain = self.chain.to_dict()

        transaction_signatures: list[str] | Unset = UNSET
        if not isinstance(self.transaction_signatures, Unset):
            transaction_signatures = self.transaction_signatures

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "coinAmount": coin_amount,
                "coin": coin,
                "chain": chain,
            }
        )
        if transaction_signatures is not UNSET:
            field_dict["transactionSignatures"] = transaction_signatures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chain_response import ChainResponse
        from ..models.coin_response import CoinResponse

        d = dict(src_dict)
        address = d.pop("address")

        coin_amount = d.pop("coinAmount")

        coin = CoinResponse.from_dict(d.pop("coin"))

        chain = ChainResponse.from_dict(d.pop("chain"))

        transaction_signatures = cast(list[str], d.pop("transactionSignatures", UNSET))

        payment_details = cls(
            address=address,
            coin_amount=coin_amount,
            coin=coin,
            chain=chain,
            transaction_signatures=transaction_signatures,
        )

        payment_details.additional_properties = d
        return payment_details

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
