"""Poll the lightweight `/status` endpoint until a terminal state is reached.

`get_payment_status` is much cheaper than `get_payment` — use it for tight
polling loops where you only need to detect status transitions.

Usage:
    export HEXPAY_TOKEN="<your-merchant-jwt>"
    python examples/poll_payment_status.py <paymentID>
"""

from __future__ import annotations

import os
import sys
import time

from hexpay import AuthenticatedClient
from hexpay.api.payments import get_payment_status
from hexpay.models import PaymentStatus

TERMINAL = {PaymentStatus.COMPLETED, PaymentStatus.EXPIRED, PaymentStatus.CANCELLED}
POLL_INTERVAL_SECONDS = 5


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: poll_payment_status.py <paymentID>")

    token = os.environ.get("HEXPAY_TOKEN")
    if not token:
        raise SystemExit("error: set HEXPAY_TOKEN to your merchant JWT")

    client = AuthenticatedClient(
        base_url=os.environ.get("HEXPAY_BASE_URL", "https://api.hexpay.io"),
        token=token,
        timeout=30.0,
    )

    payment_id = sys.argv[1]
    last = None
    while True:
        result = get_payment_status.sync(client=client, payment_id=payment_id)
        if result.status != last:
            print(f"status -> {result.status}")
            last = result.status
        if result.status in TERMINAL:
            return
        time.sleep(POLL_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
