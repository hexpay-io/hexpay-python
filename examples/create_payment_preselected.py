"""Preselected mode: $100 USD payable in USDT on TON.

Both `coin` and `chain` are specified, so the payment is returned in `pending`
status with `paymentDetails` already populated — no method-selection screen.

Usage:
    export HEXPAY_TOKEN="<your-merchant-jwt>"
    python examples/create_payment_preselected.py
"""

from __future__ import annotations

import os
import uuid

from hexpay import AuthenticatedClient
from hexpay.api.payments import create_payment
from hexpay.models import (
    CreatePaymentRequest,
    MethodFilter,
    MethodFilterChain,
    MethodFilterCoin,
    PaymentOptions,
)


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
        payment_options=PaymentOptions(
            methods=[
                MethodFilter(
                    coin=MethodFilterCoin.USDT,
                    chain=MethodFilterChain.TON,
                ),
            ],
        ),
        order_id="order-2026-00124",
        webhook_url="https://merchant.example.com/webhooks/hexpay",
    )

    payment = create_payment.sync(
        client=client,
        body=body,
        x_idempotency_key=str(uuid.uuid4()),
    )

    details = payment.payment_details
    print(f"id           {payment.id}")
    print(f"status       {payment.status}")
    print(f"address      {details.address}")
    print(f"coin amount  {details.coin_amount} {details.coin.symbol}")
    print(f"chain        {details.chain.symbol}")
    print(f"expires at   {payment.timer.expires_at.isoformat()}")


if __name__ == "__main__":
    main()
