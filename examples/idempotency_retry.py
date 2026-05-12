"""Safe retry loop preserving the `X-Idempotency-Key`.

The HexPay API requires a UUID v4 `X-Idempotency-Key` on every POST. The
server caches the response for that key for 24 hours, so repeating a request
with the SAME key returns the cached result instead of creating a duplicate
payment.

The two rules to follow:
  1. Generate ONE key per logical operation.
  2. Reuse THAT SAME key on every retry attempt for that operation
     (network error, timeout, 5xx, 429). Never regenerate inside the loop —
     a fresh UUID makes the second request "new" from the server's point of
     view and you'll create a duplicate payment.

A naive `for _ in range(3): create_payment(...key=str(uuid.uuid4()))` loop
gets this wrong; the helper below does it right.

Usage:
    export HEXPAY_TOKEN="<your-merchant-jwt>"
    python examples/idempotency_retry.py
"""

from __future__ import annotations

import os
import time
import uuid

import httpx

from hexpay import AuthenticatedClient
from hexpay.api.payments import create_payment
from hexpay.models import CreatePaymentRequest, ErrorResponse, PaymentResponse
from hexpay.types import Response

# Retry on transport errors and on the HTTP statuses the server documents as
# transient. Do NOT retry on 4xx (other than 429) — those are deterministic
# rejections that won't change on retry.
RETRY_HTTP_STATUSES = {429, 500, 502, 503, 504}
MAX_ATTEMPTS = 5
BASE_BACKOFF_SECONDS = 1.0


def create_payment_with_retry(
    client: AuthenticatedClient,
    body: CreatePaymentRequest,
) -> PaymentResponse:
    """Create a payment, retrying transient failures with the same idempotency key."""
    # Generated ONCE per logical operation, BEFORE the retry loop.
    idempotency_key = str(uuid.uuid4())

    last_error: Exception | None = None

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            response: Response[PaymentResponse | ErrorResponse] = create_payment.sync_detailed(
                client=client,
                body=body,
                x_idempotency_key=idempotency_key,  # same key every attempt
            )
        except (httpx.TransportError, httpx.TimeoutException) as exc:
            last_error = exc
            print(f"[attempt {attempt}] network error: {exc!r}")
            _sleep_backoff(attempt, retry_after=None)
            continue

        if 200 <= response.status_code < 300 and isinstance(response.parsed, PaymentResponse):
            print(f"[attempt {attempt}] success — http {response.status_code}")
            return response.parsed

        if response.status_code in RETRY_HTTP_STATUSES:
            retry_after = response.headers.get("Retry-After")
            print(f"[attempt {attempt}] http {response.status_code}, retrying (retry-after={retry_after})")
            _sleep_backoff(attempt, retry_after=retry_after)
            continue

        # Non-transient error (e.g. 400 validation, 401 auth) — fail fast.
        message = _format_api_error(response)
        raise RuntimeError(f"non-retryable error from HexPay: http {response.status_code}: {message}")

    raise RuntimeError(
        f"giving up after {MAX_ATTEMPTS} attempts; last error: {last_error!r}"
    )


def _sleep_backoff(attempt: int, *, retry_after: str | None) -> None:
    """Honour Retry-After if the server provided one, otherwise exponential backoff."""
    if retry_after is not None:
        try:
            time.sleep(float(retry_after))
            return
        except ValueError:
            pass
    time.sleep(BASE_BACKOFF_SECONDS * (2 ** (attempt - 1)))


def _format_api_error(response: Response[PaymentResponse | ErrorResponse]) -> str:
    if isinstance(response.parsed, ErrorResponse):
        err = response.parsed.error
        return f"{err.type_}/{err.code}: {err.message}"
    return "<unparsed body>"


def main() -> None:
    token = os.environ.get("HEXPAY_TOKEN")
    if not token:
        raise SystemExit("error: set HEXPAY_TOKEN to your merchant JWT")

    client = AuthenticatedClient(
        base_url=os.environ.get("HEXPAY_BASE_URL", "https://api.hexpay.io"),
        token=token,
        # Short timeout to make transient failures more likely on flaky links.
        timeout=10.0,
    )

    body = CreatePaymentRequest(
        amount="100.00",
        currency="USD",
        order_id="order-2026-00200",
        webhook_url="https://merchant.example.com/webhooks/hexpay",
    )

    payment = create_payment_with_retry(client, body)

    print()
    print(f"id          {payment.id}")
    print(f"status      {payment.status}")
    print(f"checkoutURL {payment.checkout_url}")


if __name__ == "__main__":
    main()
