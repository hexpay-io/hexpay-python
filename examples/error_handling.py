"""Inspect structured errors returned by the API.

Use `*_detailed` variants of the operations to receive a `Response[T]` wrapper
that exposes the raw HTTP status, headers, and the parsed error envelope.

Usage:
    export HEXPAY_TOKEN="<your-merchant-jwt>"
    python examples/error_handling.py
"""

from __future__ import annotations

import os
import uuid

from hexpay import AuthenticatedClient
from hexpay.api.payments import create_payment
from hexpay.models import CreatePaymentRequest, ErrorResponse


def main() -> None:
    token = os.environ.get("HEXPAY_TOKEN")
    if not token:
        raise SystemExit("error: set HEXPAY_TOKEN to your merchant JWT")

    client = AuthenticatedClient(
        base_url=os.environ.get("HEXPAY_BASE_URL", "https://api.hexpay.io"),
        token=token,
        timeout=30.0,
    )

    # Intentionally bad request: negative amount.
    body = CreatePaymentRequest(amount="-1", currency="USD")

    response = create_payment.sync_detailed(
        client=client,
        body=body,
        x_idempotency_key=str(uuid.uuid4()),
    )

    print(f"http status   {response.status_code}")

    if isinstance(response.parsed, ErrorResponse):
        err = response.parsed.error
        print(f"error type    {err.type_}")
        print(f"error code    {err.code}")
        print(f"message       {err.message}")
        if err.param:
            print(f"param         {err.param}")
        if response.status_code == 429:
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                print(f"retry after   {retry_after}s")


if __name__ == "__main__":
    main()
