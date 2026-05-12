from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.payment_list_response import PaymentListResponse
from ...models.payment_status import PaymentStatus
from ...types import UNSET, Unset
from typing import cast


def _get_kwargs(
    *,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
    status: list[PaymentStatus] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/payments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PaymentListResponse | None:
    if response.status_code == 200:
        response_200 = PaymentListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | PaymentListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
    status: list[PaymentStatus] | Unset = UNSET,
) -> Response[ErrorResponse | PaymentListResponse]:
    """List payments

     Returns a paginated list of payments for your store, ordered by creation date
    (most recent first).

    Use cursor-based pagination: if the response contains a `cursor` field, pass
    its value as the `cursor` query parameter to fetch the next page. The absence of
    `cursor` in the response means there are no more pages.

    Use the `status` parameter to filter payments by one or more statuses.

    Args:
        limit (int | Unset):  Default: 10. Example: 20.
        cursor (str | Unset):  Example:
            eyJpZCI6IjAxOTMyN2M2LTIwNTgtNzkwMS1iMjM0LTU2Nzg5YWJjZGVmZiJ9.
        status (list[PaymentStatus] | Unset):  Example: ['pending', 'completed'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaymentListResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
    status: list[PaymentStatus] | Unset = UNSET,
) -> ErrorResponse | PaymentListResponse | None:
    """List payments

     Returns a paginated list of payments for your store, ordered by creation date
    (most recent first).

    Use cursor-based pagination: if the response contains a `cursor` field, pass
    its value as the `cursor` query parameter to fetch the next page. The absence of
    `cursor` in the response means there are no more pages.

    Use the `status` parameter to filter payments by one or more statuses.

    Args:
        limit (int | Unset):  Default: 10. Example: 20.
        cursor (str | Unset):  Example:
            eyJpZCI6IjAxOTMyN2M2LTIwNTgtNzkwMS1iMjM0LTU2Nzg5YWJjZGVmZiJ9.
        status (list[PaymentStatus] | Unset):  Example: ['pending', 'completed'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaymentListResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
    status: list[PaymentStatus] | Unset = UNSET,
) -> Response[ErrorResponse | PaymentListResponse]:
    """List payments

     Returns a paginated list of payments for your store, ordered by creation date
    (most recent first).

    Use cursor-based pagination: if the response contains a `cursor` field, pass
    its value as the `cursor` query parameter to fetch the next page. The absence of
    `cursor` in the response means there are no more pages.

    Use the `status` parameter to filter payments by one or more statuses.

    Args:
        limit (int | Unset):  Default: 10. Example: 20.
        cursor (str | Unset):  Example:
            eyJpZCI6IjAxOTMyN2M2LTIwNTgtNzkwMS1iMjM0LTU2Nzg5YWJjZGVmZiJ9.
        status (list[PaymentStatus] | Unset):  Example: ['pending', 'completed'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaymentListResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
    status: list[PaymentStatus] | Unset = UNSET,
) -> ErrorResponse | PaymentListResponse | None:
    """List payments

     Returns a paginated list of payments for your store, ordered by creation date
    (most recent first).

    Use cursor-based pagination: if the response contains a `cursor` field, pass
    its value as the `cursor` query parameter to fetch the next page. The absence of
    `cursor` in the response means there are no more pages.

    Use the `status` parameter to filter payments by one or more statuses.

    Args:
        limit (int | Unset):  Default: 10. Example: 20.
        cursor (str | Unset):  Example:
            eyJpZCI6IjAxOTMyN2M2LTIwNTgtNzkwMS1iMjM0LTU2Nzg5YWJjZGVmZiJ9.
        status (list[PaymentStatus] | Unset):  Example: ['pending', 'completed'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaymentListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            status=status,
        )
    ).parsed
