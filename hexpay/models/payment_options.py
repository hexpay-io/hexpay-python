from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.method_restriction import MethodRestriction


T = TypeVar("T", bound="PaymentOptions")


@_attrs_define
class PaymentOptions:
    """Optional restriction on which payment methods are offered at checkout.
    When omitted entirely, all payment methods enabled for your store are shown
    and the payment is created in `created` status.

        Attributes:
            methods (list[MethodRestriction] | Unset): Payment methods the customer is allowed to pay with.

                Currently exactly one entry with both `coin` and `chain` is supported.
                HexPay then selects this method on behalf of the customer: the payment is
                created directly in `pending` status with `paymentDetails` populated
                (Preselected). Allowing several methods is planned.

                Omit `paymentOptions` entirely to let the customer select a payment method
                at checkout — payment starts in `created` status (Customer Choice).
    """

    methods: list[MethodRestriction] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.method_restriction import MethodRestriction

        methods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.methods, Unset):
            methods = []
            for methods_item_data in self.methods:
                methods_item = methods_item_data.to_dict()
                methods.append(methods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if methods is not UNSET:
            field_dict["methods"] = methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.method_restriction import MethodRestriction

        d = dict(src_dict)
        _methods = d.pop("methods", UNSET)
        methods: list[MethodRestriction] | Unset = UNSET
        if _methods is not UNSET:
            methods = []
            for methods_item_data in _methods:
                methods_item = MethodRestriction.from_dict(methods_item_data)

                methods.append(methods_item)

        payment_options = cls(
            methods=methods,
        )

        payment_options.additional_properties = d
        return payment_options

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
