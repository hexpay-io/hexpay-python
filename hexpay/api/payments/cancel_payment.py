from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.payment_cancel_response import PaymentCancelResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    payment_id: UUID,
    *,
    x_idempotency_key: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_idempotency_key, Unset):
        headers["X-Idempotency-Key"] = x_idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/payments/{payment_id}/cancel".format(
            payment_id=quote(str(payment_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PaymentCancelResponse | None:
    if response.status_code == 200:
        response_200 = PaymentCancelResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | PaymentCancelResponse]:
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
    x_idempotency_key: UUID | Unset = UNSET,
) -> Response[ErrorResponse | PaymentCancelResponse]:
    """Cancel a payment

     Cancels a payment and returns the updated status `cancelled`.

    Cancellation is permitted from `created` or `pending` status only. Payments
    already in a terminal state (`completed`, `expired`, or `cancelled`) cannot
    be cancelled.

    Args:
        payment_id (UUID):  Example: 019327c6-2058-7901-b234-56789abcdeff.
        x_idempotency_key (UUID | Unset):  Example: a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaymentCancelResponse]
    """

    kwargs = _get_kwargs(
        payment_id=payment_id,
        x_idempotency_key=x_idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    payment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_idempotency_key: UUID | Unset = UNSET,
) -> ErrorResponse | PaymentCancelResponse | None:
    """Cancel a payment

     Cancels a payment and returns the updated status `cancelled`.

    Cancellation is permitted from `created` or `pending` status only. Payments
    already in a terminal state (`completed`, `expired`, or `cancelled`) cannot
    be cancelled.

    Args:
        payment_id (UUID):  Example: 019327c6-2058-7901-b234-56789abcdeff.
        x_idempotency_key (UUID | Unset):  Example: a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaymentCancelResponse
    """

    return sync_detailed(
        payment_id=payment_id,
        client=client,
        x_idempotency_key=x_idempotency_key,
    ).parsed


async def asyncio_detailed(
    payment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_idempotency_key: UUID | Unset = UNSET,
) -> Response[ErrorResponse | PaymentCancelResponse]:
    """Cancel a payment

     Cancels a payment and returns the updated status `cancelled`.

    Cancellation is permitted from `created` or `pending` status only. Payments
    already in a terminal state (`completed`, `expired`, or `cancelled`) cannot
    be cancelled.

    Args:
        payment_id (UUID):  Example: 019327c6-2058-7901-b234-56789abcdeff.
        x_idempotency_key (UUID | Unset):  Example: a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaymentCancelResponse]
    """

    kwargs = _get_kwargs(
        payment_id=payment_id,
        x_idempotency_key=x_idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    payment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_idempotency_key: UUID | Unset = UNSET,
) -> ErrorResponse | PaymentCancelResponse | None:
    """Cancel a payment

     Cancels a payment and returns the updated status `cancelled`.

    Cancellation is permitted from `created` or `pending` status only. Payments
    already in a terminal state (`completed`, `expired`, or `cancelled`) cannot
    be cancelled.

    Args:
        payment_id (UUID):  Example: 019327c6-2058-7901-b234-56789abcdeff.
        x_idempotency_key (UUID | Unset):  Example: a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaymentCancelResponse
    """

    return (
        await asyncio_detailed(
            payment_id=payment_id,
            client=client,
            x_idempotency_key=x_idempotency_key,
        )
    ).parsed
