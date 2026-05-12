"""List the coin/chain combinations enabled for the merchant store.

Use the printed `coin.symbol` / `chain.symbol` values when building a
`MethodFilter` for Preselected payments.

Usage:
    export HEXPAY_TOKEN="<your-merchant-jwt>"
    python examples/list_payment_methods.py
"""

from __future__ import annotations

import os

from hexpay import AuthenticatedClient
from hexpay.api.payment_methods import list_payment_methods


def main() -> None:
    token = os.environ.get("HEXPAY_TOKEN")
    if not token:
        raise SystemExit("error: set HEXPAY_TOKEN to your merchant JWT")

    client = AuthenticatedClient(
        base_url=os.environ.get("HEXPAY_BASE_URL", "https://api.hexpay.io"),
        token=token,
        timeout=30.0,
    )

    response = list_payment_methods.sync(client=client)
    for m in response.data:
        print(f"{m.coin.symbol:<8} on {m.chain.symbol:<6}  ({m.coin.name})")


if __name__ == "__main__":
    main()
