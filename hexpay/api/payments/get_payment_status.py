from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.payment_status_response import PaymentStatusResponse
from typing import cast
from uuid import UUID


def _get_kwargs(
    payment_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/payments/{payment_id}/status".format(
            payment_id=quote(str(payment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PaymentStatusResponse | None:
    if response.status_code == 200:
        response_200 = PaymentStatusResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | PaymentStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    payment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | PaymentStatusResponse]:
    """Retrieve payment status

     Returns only the current status of a payment. Use this lightweight endpoint
    for high-frequency polling where you only need to detect status changes
    without the overhead of fetching the full payment object.

    Args:
        payment_id (UUID):  Example: 019327c6-2058-7901-b234-56789abcdeff.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaymentStatusResponse]
    """

    kwargs = _get_kwargs(
        payment_id=payment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    payment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | PaymentStatusResponse | None:
    """Retrieve payment status

     Returns only the current status of a payment. Use this lightweight endpoint
    for high-frequency polling where you only need to detect status changes
    without the overhead of fetching the full payment object.

    Args:
        payment_id (UUID):  Example: 019327c6-2058-7901-b234-56789abcdeff.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaymentStatusResponse
    """

    return sync_detailed(
        payment_id=payment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    payment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | PaymentStatusResponse]:
    """Retrieve payment status

     Returns only the current status of a payment. Use this lightweight endpoint
    for high-frequency polling where you only need to detect status changes
    without the overhead of fetching the full payment object.

    Args:
        payment_id (UUID):  Example: 019327c6-2058-7901-b234-56789abcdeff.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaymentStatusResponse]
    """

    kwargs = _get_kwargs(
        payment_id=payment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    payment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | PaymentStatusResponse | None:
    """Retrieve payment status

     Returns only the current status of a payment. Use this lightweight endpoint
    for high-frequency polling where you only need to detect status changes
    without the overhead of fetching the full payment object.

    Args:
        payment_id (UUID):  Example: 019327c6-2058-7901-b234-56789abcdeff.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaymentStatusResponse
    """

    return (
        await asyncio_detailed(
            payment_id=payment_id,
            client=client,
        )
    ).parsed
