from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_payment_request import CreatePaymentRequest
from ...models.error_response import ErrorResponse
from ...models.payment_response import PaymentResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID


def _get_kwargs(
    *,
    body: CreatePaymentRequest,
    x_idempotency_key: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_idempotency_key, Unset):
        headers["X-Idempotency-Key"] = x_idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/payments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PaymentResponse | None:
    if response.status_code == 201:
        response_201 = PaymentResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

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
    *,
    client: AuthenticatedClient | Client,
    body: CreatePaymentRequest,
    x_idempotency_key: UUID | Unset = UNSET,
) -> Response[ErrorResponse | PaymentResponse]:
    r"""Create a payment

     Creates a new payment for your store and returns the full payment object.

    ### Denomination
    Specify the value the customer owes via the top-level `amount` (decimal string)
    and `currency` (fiat code or coin ticker) fields.

    ---

    ### Preselected
    Pass `payment_options.methods` with **exactly one entry** containing **both** `coin`
    and `chain`. The server resolves the address immediately and returns the payment in
    `pending` status with `paymentDetails` populated. The customer proceeds straight to
    the deposit screen without any method selection step.

    ### Customer Choice
    Omit `payment_options`. All store-enabled payment methods are offered to the customer
    at checkout. The payment starts in `created` status.

    ---

    ### Supported combinations
    | `currency` | `payment_options.methods`          | Initial status | `paymentDetails` |
    |------------|------------------------------------|----------------|------------------|
    | `USD`      | *(omitted)*                        | `created`      | absent           |
    | `TON`      | *(omitted)*                        | `created`      | absent           |
    | `USD`      | `[{coin:\"USDT\",chain:\"TON\"}]`      | `pending`      | **populated**    |
    | `TON`      | `[{coin:\"USDT\",chain:\"TON\"}]`      | `pending`      | **populated**    |
    | `TON`      | `[{coin:\"TON\",chain:\"TON\"}]`       | `pending`      | **populated**    |

    Args:
        x_idempotency_key (UUID | Unset):  Example: a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d.
        body (CreatePaymentRequest): Request body for creating a new payment. The body is
            intentionally flat:
            `amount`, `currency`, and all optional fields are top-level. The only nested
            structure is `payment_options.methods`, which describes an allowlist of
            acceptable payment methods.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaymentResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        x_idempotency_key=x_idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePaymentRequest,
    x_idempotency_key: UUID | Unset = UNSET,
) -> ErrorResponse | PaymentResponse | None:
    r"""Create a payment

     Creates a new payment for your store and returns the full payment object.

    ### Denomination
    Specify the value the customer owes via the top-level `amount` (decimal string)
    and `currency` (fiat code or coin ticker) fields.

    ---

    ### Preselected
    Pass `payment_options.methods` with **exactly one entry** containing **both** `coin`
    and `chain`. The server resolves the address immediately and returns the payment in
    `pending` status with `paymentDetails` populated. The customer proceeds straight to
    the deposit screen without any method selection step.

    ### Customer Choice
    Omit `payment_options`. All store-enabled payment methods are offered to the customer
    at checkout. The payment starts in `created` status.

    ---

    ### Supported combinations
    | `currency` | `payment_options.methods`          | Initial status | `paymentDetails` |
    |------------|------------------------------------|----------------|------------------|
    | `USD`      | *(omitted)*                        | `created`      | absent           |
    | `TON`      | *(omitted)*                        | `created`      | absent           |
    | `USD`      | `[{coin:\"USDT\",chain:\"TON\"}]`      | `pending`      | **populated**    |
    | `TON`      | `[{coin:\"USDT\",chain:\"TON\"}]`      | `pending`      | **populated**    |
    | `TON`      | `[{coin:\"TON\",chain:\"TON\"}]`       | `pending`      | **populated**    |

    Args:
        x_idempotency_key (UUID | Unset):  Example: a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d.
        body (CreatePaymentRequest): Request body for creating a new payment. The body is
            intentionally flat:
            `amount`, `currency`, and all optional fields are top-level. The only nested
            structure is `payment_options.methods`, which describes an allowlist of
            acceptable payment methods.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaymentResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        x_idempotency_key=x_idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePaymentRequest,
    x_idempotency_key: UUID | Unset = UNSET,
) -> Response[ErrorResponse | PaymentResponse]:
    r"""Create a payment

     Creates a new payment for your store and returns the full payment object.

    ### Denomination
    Specify the value the customer owes via the top-level `amount` (decimal string)
    and `currency` (fiat code or coin ticker) fields.

    ---

    ### Preselected
    Pass `payment_options.methods` with **exactly one entry** containing **both** `coin`
    and `chain`. The server resolves the address immediately and returns the payment in
    `pending` status with `paymentDetails` populated. The customer proceeds straight to
    the deposit screen without any method selection step.

    ### Customer Choice
    Omit `payment_options`. All store-enabled payment methods are offered to the customer
    at checkout. The payment starts in `created` status.

    ---

    ### Supported combinations
    | `currency` | `payment_options.methods`          | Initial status | `paymentDetails` |
    |------------|------------------------------------|----------------|------------------|
    | `USD`      | *(omitted)*                        | `created`      | absent           |
    | `TON`      | *(omitted)*                        | `created`      | absent           |
    | `USD`      | `[{coin:\"USDT\",chain:\"TON\"}]`      | `pending`      | **populated**    |
    | `TON`      | `[{coin:\"USDT\",chain:\"TON\"}]`      | `pending`      | **populated**    |
    | `TON`      | `[{coin:\"TON\",chain:\"TON\"}]`       | `pending`      | **populated**    |

    Args:
        x_idempotency_key (UUID | Unset):  Example: a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d.
        body (CreatePaymentRequest): Request body for creating a new payment. The body is
            intentionally flat:
            `amount`, `currency`, and all optional fields are top-level. The only nested
            structure is `payment_options.methods`, which describes an allowlist of
            acceptable payment methods.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PaymentResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        x_idempotency_key=x_idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePaymentRequest,
    x_idempotency_key: UUID | Unset = UNSET,
) -> ErrorResponse | PaymentResponse | None:
    r"""Create a payment

     Creates a new payment for your store and returns the full payment object.

    ### Denomination
    Specify the value the customer owes via the top-level `amount` (decimal string)
    and `currency` (fiat code or coin ticker) fields.

    ---

    ### Preselected
    Pass `payment_options.methods` with **exactly one entry** containing **both** `coin`
    and `chain`. The server resolves the address immediately and returns the payment in
    `pending` status with `paymentDetails` populated. The customer proceeds straight to
    the deposit screen without any method selection step.

    ### Customer Choice
    Omit `payment_options`. All store-enabled payment methods are offered to the customer
    at checkout. The payment starts in `created` status.

    ---

    ### Supported combinations
    | `currency` | `payment_options.methods`          | Initial status | `paymentDetails` |
    |------------|------------------------------------|----------------|------------------|
    | `USD`      | *(omitted)*                        | `created`      | absent           |
    | `TON`      | *(omitted)*                        | `created`      | absent           |
    | `USD`      | `[{coin:\"USDT\",chain:\"TON\"}]`      | `pending`      | **populated**    |
    | `TON`      | `[{coin:\"USDT\",chain:\"TON\"}]`      | `pending`      | **populated**    |
    | `TON`      | `[{coin:\"TON\",chain:\"TON\"}]`       | `pending`      | **populated**    |

    Args:
        x_idempotency_key (UUID | Unset):  Example: a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d.
        body (CreatePaymentRequest): Request body for creating a new payment. The body is
            intentionally flat:
            `amount`, `currency`, and all optional fields are top-level. The only nested
            structure is `payment_options.methods`, which describes an allowlist of
            acceptable payment methods.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PaymentResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_idempotency_key=x_idempotency_key,
        )
    ).parsed
