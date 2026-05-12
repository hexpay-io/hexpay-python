"""Walk every page of payments using cursor-based pagination.

Optionally filter by status — pass any combination of:
    created | pending | completed | expired | cancelled

Usage:
    export HEXPAY_TOKEN="<your-merchant-jwt>"
    python examples/list_payments.py                   # all statuses
    python examples/list_payments.py pending completed # only these statuses
"""

from __future__ import annotations

import os
import sys

from hexpay import AuthenticatedClient
from hexpay.api.payments import list_payments
from hexpay.models import PaymentStatus
from hexpay.types import UNSET

PAGE_SIZE = 50


def main() -> None:
    token = os.environ.get("HEXPAY_TOKEN")
    if not token:
        raise SystemExit("error: set HEXPAY_TOKEN to your merchant JWT")

    client = AuthenticatedClient(
        base_url=os.environ.get("HEXPAY_BASE_URL", "https://api.hexpay.io"),
        token=token,
        timeout=30.0,
    )

    statuses = [PaymentStatus(s) for s in sys.argv[1:]] if len(sys.argv) > 1 else UNSET
    cursor = UNSET
    total = 0

    while True:
        page = list_payments.sync(
            client=client,
            limit=PAGE_SIZE,
            cursor=cursor,
            status=statuses,
        )
        for p in page.payments:
            total += 1
            print(f"{p.id}  {p.status:<10}  {p.amount} {p.currency}  order={p.order_id or '-'}")

        if not page.cursor:
            break
        cursor = page.cursor

    print(f"\n{total} payment(s) total")


if __name__ == "__main__":
    main()
