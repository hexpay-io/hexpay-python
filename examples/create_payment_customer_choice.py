"""Customer-Choice mode: $100 USD, customer picks any enabled coin/chain at checkout.

Resulting payment starts in `created` status. `paymentDetails` are populated only
once the customer selects a method on the hosted checkout page.

Usage:
    export HEXPAY_TOKEN="<your-merchant-jwt>"
    python examples/create_payment_customer_choice.py
"""

from __future__ import annotations

import os
import uuid

from hexpay import AuthenticatedClient
from hexpay.api.payments import create_payment
from hexpay.models import CreatePaymentRequest


def main() -> None:
    token = os.environ.get("HEXPAY_TOKEN")
    if not token:
        raise SystemExit("error: set HEXPAY_TOKEN to your merchant JWT")

    client = AuthenticatedClient(
        base_url=os.environ.get("HEXPAY_BASE_URL", "https://api.hexpay.io"),
        token=token,
        timeout=30.0,
    )

    body = CreatePaymentRequest(
        amount="100.00",
        currency="USD",
        order_id="order-2026-00123",
        webhook_url="https://merchant.example.com/webhooks/hexpay",
    )

    payment = create_payment.sync(
        client=client,
        body=body,
        x_idempotency_key=str(uuid.uuid4()),
    )

    print(f"id          {payment.id}")
    print(f"status      {payment.status}")
    print(f"checkoutURL {payment.checkout_url}")
    print(f"expires at  {payment.timer.expires_at.isoformat()}")


if __name__ == "__main__":
    main()
