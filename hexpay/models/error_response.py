from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.error import Error


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """Top-level error envelope returned for all non-2xx responses. All error
    information is nested under the `error` key to allow safe envelope detection
    without inspecting the HTTP status code.

        Attributes:
            error (Error): Structured error object. `type` gives the broad category, `code` is the
                machine-readable discriminator for programmatic handling, `message` is a
                human-readable explanation, and the optional `param` names the specific
                request field that caused the error.
    """

    error: Error
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.error import Error

        error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error import Error

        d = dict(src_dict)
        error = Error.from_dict(d.pop("error"))

        error_response = cls(
            error=error,
        )

        error_response.additional_properties = d
        return error_response

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
