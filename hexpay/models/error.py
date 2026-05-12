from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.error_type import ErrorType
from ..types import UNSET, Unset


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """Structured error object. `type` gives the broad category, `code` is the
    machine-readable discriminator for programmatic handling, `message` is a
    human-readable explanation, and the optional `param` names the specific
    request field that caused the error.

        Attributes:
            type_ (ErrorType): High-level error category. Use this to determine the general class of
                the error without parsing `code`.
                 Example: invalid_request_error.
            message (str): Human-readable description of the error, intended for developers. Example: Amount must be a
                positive decimal number.
            code (str): Machine-readable error identifier. Use this in conditional logic to branch
                on specific error conditions (e.g., retry on `rate_limit_exceeded`,
                surface to user on `payment_not_cancellable`).
                 Example: invalid_amount.
            param (str | Unset): The name of the request field that caused the error, using dot notation
                for nested fields (e.g., `currency`, `payment_options.methods[0]`).
                Present only when the error is attributable to a specific parameter.
                 Example: amount.
    """

    type_: ErrorType
    message: str
    code: str
    param: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        message = self.message

        code = self.code

        param = self.param

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "message": message,
                "code": code,
            }
        )
        if param is not UNSET:
            field_dict["param"] = param

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ErrorType(d.pop("type"))

        message = d.pop("message")

        code = d.pop("code")

        param = d.pop("param", UNSET)

        error = cls(
            type_=type_,
            message=message,
            code=code,
            param=param,
        )

        error.additional_properties = d
        return error

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
