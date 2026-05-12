from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.payment_response import PaymentResponse
from typing import cast
from uuid import UUID


def _get_kwargs(
    payment_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/payments/{payment_id}".format(
            payment_id=quote(str(payment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PaymentResponse | None:
    if response.status_code == 200:
        response_200 = PaymentResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | PaymentResponse]:
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
) -> Response[ErrorResponse | PaymentResponse]:
    """Retrieve a payment

     Retrieves the full details of a payment by its unique identifier.

    The response structure varies by status:
    - **`created`** — `amount`, `currency` and timer are present.
      `paymentDetails` is absent — the customer has not yet selected a payment method.
    - **`pending`** — `paymentDetails` is populated with the blockchain address and
      exact coin amount. The customer must send the transfer.
    - **`completed`** — `paymentDetails` includes `transactionSignatures` confirming
      the on-chain transfer.
    - **`expired`** — Elapsed TTL. Reachable from both `created` and `pending`.
      `paymentDetails` is present only if the payment had reached `pending` first.
    - **`cancelled`** — Canceled by the merchant. Reachable from both `created` and
      `pending`. `paymentDetails` is present only if the payment had reached `pending`.

    Args:
        payment_id (UUID):  Example: 019327c6-2058-7901-b234-56789abcdeff.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaymentResponse]
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
) -> ErrorResponse | PaymentResponse | None:
    """Retrieve a payment

     Retrieves the full details of a payment by its unique identifier.

    The response structure varies by status:
    - **`created`** — `amount`, `currency` and timer are present.
      `paymentDetails` is absent — the customer has not yet selected a payment method.
    - **`pending`** — `paymentDetails` is populated with the blockchain address and
      exact coin amount. The customer must send the transfer.
    - **`completed`** — `paymentDetails` includes `transactionSignatures` confirming
      the on-chain transfer.
    - **`expired`** — Elapsed TTL. Reachable from both `created` and `pending`.
      `paymentDetails` is present only if the payment had reached `pending` first.
    - **`cancelled`** — Canceled by the merchant. Reachable from both `created` and
      `pending`. `paymentDetails` is present only if the payment had reached `pending`.

    Args:
        payment_id (UUID):  Example: 019327c6-2058-7901-b234-56789abcdeff.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaymentResponse
    """

    return sync_detailed(
        payment_id=payment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    payment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | PaymentResponse]:
    """Retrieve a payment

     Retrieves the full details of a payment by its unique identifier.

    The response structure varies by status:
    - **`created`** — `amount`, `currency` and timer are present.
      `paymentDetails` is absent — the customer has not yet selected a payment method.
    - **`pending`** — `paymentDetails` is populated with the blockchain address and
      exact coin amount. The customer must send the transfer.
    - **`completed`** — `paymentDetails` includes `transactionSignatures` confirming
      the on-chain transfer.
    - **`expired`** — Elapsed TTL. Reachable from both `created` and `pending`.
      `paymentDetails` is present only if the payment had reached `pending` first.
    - **`cancelled`** — Canceled by the merchant. Reachable from both `created` and
      `pending`. `paymentDetails` is present only if the payment had reached `pending`.

    Args:
        payment_id (UUID):  Example: 019327c6-2058-7901-b234-56789abcdeff.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaymentResponse]
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
) -> ErrorResponse | PaymentResponse | None:
    """Retrieve a payment

     Retrieves the full details of a payment by its unique identifier.

    The response structure varies by status:
    - **`created`** — `amount`, `currency` and timer are present.
      `paymentDetails` is absent — the customer has not yet selected a payment method.
    - **`pending`** — `paymentDetails` is populated with the blockchain address and
      exact coin amount. The customer must send the transfer.
    - **`completed`** — `paymentDetails` includes `transactionSignatures` confirming
      the on-chain transfer.
    - **`expired`** — Elapsed TTL. Reachable from both `created` and `pending`.
      `paymentDetails` is present only if the payment had reached `pending` first.
    - **`cancelled`** — Canceled by the merchant. Reachable from both `created` and
      `pending`. `paymentDetails` is present only if the payment had reached `pending`.

    Args:
        payment_id (UUID):  Example: 019327c6-2058-7901-b234-56789abcdeff.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaymentResponse
    """

    return (
        await asyncio_detailed(
            payment_id=payment_id,
            client=client,
        )
    ).parsed
