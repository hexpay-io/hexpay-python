"""Fetch the full payment object by ID.

Usage:
    export HEXPAY_TOKEN="<your-merchant-jwt>"
    python examples/retrieve_payment.py <paymentID>
"""

from __future__ import annotations

import os
import sys

from hexpay import AuthenticatedClient
from hexpay.api.payments import get_payment


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: retrieve_payment.py <paymentID>")

    token = os.environ.get("HEXPAY_TOKEN")
    if not token:
        raise SystemExit("error: set HEXPAY_TOKEN to your merchant JWT")

    client = AuthenticatedClient(
        base_url=os.environ.get("HEXPAY_BASE_URL", "https://api.hexpay.io"),
        token=token,
        timeout=30.0,
    )

    payment = get_payment.sync(client=client, payment_id=sys.argv[1])

    print(f"id          {payment.id}")
    print(f"status      {payment.status}")
    print(f"order_id    {payment.order_id}")
    print(f"amount      {payment.amount} {payment.currency}")
    print(f"checkoutURL {payment.checkout_url}")

    if payment.payment_details:
        details = payment.payment_details
        print("payment details:")
        print(f"  address     {details.address}")
        print(f"  coinAmount  {details.coin_amount} {details.coin.symbol} on {details.chain.symbol}")
        if details.transaction_signatures:
            print(f"  txs         {', '.join(details.transaction_signatures)}")


if __name__ == "__main__":
    main()
