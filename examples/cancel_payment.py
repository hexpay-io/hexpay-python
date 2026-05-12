"""Cancel an active payment.

Cancellation is allowed only from `created` or `pending` — already-terminal
payments (`completed`, `expired`, `cancelled`) return 400 `payment_not_cancellable`.

Usage:
    export HEXPAY_TOKEN="<your-merchant-jwt>"
    python examples/cancel_payment.py <paymentID>
"""

from __future__ import annotations

import os
import sys
import uuid

from hexpay import AuthenticatedClient
from hexpay.api.payments import cancel_payment


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: cancel_payment.py <paymentID>")

    token = os.environ.get("HEXPAY_TOKEN")
    if not token:
        raise SystemExit("error: set HEXPAY_TOKEN to your merchant JWT")

    client = AuthenticatedClient(
        base_url=os.environ.get("HEXPAY_BASE_URL", "https://api.hexpay.io"),
        token=token,
        timeout=30.0,
    )

    result = cancel_payment.sync(
        client=client,
        payment_id=sys.argv[1],
        x_idempotency_key=str(uuid.uuid4()),
    )

    print(f"status -> {result.status}")


if __name__ == "__main__":
    main()
