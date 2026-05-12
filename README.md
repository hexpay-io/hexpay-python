# HexPay Python SDK

Official Python client for the [HexPay Merchant API](https://hexpay.io) — TON-blockchain
cryptocurrency payments.

The client in [`hexpay/`](hexpay/) is **fully auto-generated** from the OpenAPI spec at
[`oapi/api.yaml`](oapi/api.yaml). Do not edit it by hand — your changes will be
overwritten on the next regeneration.

## Installation

```bash
pip install "git+https://github.com/hexpay/hexpay-python.git"
```

Or pin to a release tag:

```bash
pip install "git+https://github.com/hexpay/hexpay-python.git@v0.0.1"
```

## Quickstart

```python
import os
import uuid

from hexpay import AuthenticatedClient
from hexpay.api.payments import create_payment
from hexpay.models import CreatePaymentRequest

client = AuthenticatedClient(
    base_url="https://api.hexpay.io",
    token=os.environ["HEXPAY_TOKEN"],
)

payment = create_payment.sync(
    client=client,
    body=CreatePaymentRequest(amount="100.00", currency="USD"),
    x_idempotency_key=str(uuid.uuid4()),
)

print(payment.id, payment.checkout_url)
```

## Authentication

All endpoints require a JWT obtained from the HexPay merchant dashboard. Pass it as
the `token` argument to `AuthenticatedClient`. Never hard-code tokens — load them
from environment variables, a secrets manager, or your config layer.

## Idempotency

Every `POST` request requires a UUID v4 `X-Idempotency-Key`. The SDK exposes it as
the `x_idempotency_key` argument on every mutating operation.

**Reuse the same key when retrying** a failed request — the server returns the
cached response from the first attempt instead of creating a duplicate payment.
**Generate a fresh key for each new logical operation.**

See [`examples/idempotency_retry.py`](examples/idempotency_retry.py) for a complete
retry loop that gets this right.

## Async

Every endpoint exposes both `sync` and `asyncio` entry points:

```python
import asyncio
from hexpay.api.payments import list_payments

async def main():
    page = await list_payments.asyncio(client=client, limit=20)
    for p in page.payments:
        print(p.id, p.status)

asyncio.run(main())
```

## Examples

Runnable scripts under [`examples/`](examples/) — each is self-contained and reads
`HEXPAY_TOKEN` (and optionally `HEXPAY_BASE_URL`) from the environment:

| File                                                                              | What it shows                                  |
|-----------------------------------------------------------------------------------|------------------------------------------------|
| [`create_payment_customer_choice.py`](examples/create_payment_customer_choice.py) | Customer-Choice mode — checkout picks the method |
| [`create_payment_preselected.py`](examples/create_payment_preselected.py)         | Preselected USDT/TON — `pending` immediately     |
| [`retrieve_payment.py`](examples/retrieve_payment.py)                             | Fetch full payment details                     |
| [`poll_payment_status.py`](examples/poll_payment_status.py)                       | Lightweight status polling loop                |
| [`list_payments.py`](examples/list_payments.py)                                   | Cursor-based pagination                        |
| [`cancel_payment.py`](examples/cancel_payment.py)                                 | Cancel an active payment                       |
| [`list_payment_methods.py`](examples/list_payment_methods.py)                     | Discover store-enabled coin/chain combos       |
| [`error_handling.py`](examples/error_handling.py)                                 | Pattern for inspecting structured errors       |
| [`idempotency_retry.py`](examples/idempotency_retry.py)                           | Safe retry loop preserving the idempotency key |

Run them with:

```bash
make gen install                # generate client + install into .venv/
export HEXPAY_TOKEN="<your-jwt>"
.venv/bin/python examples/create_payment_customer_choice.py
```

Or activate the venv once and use plain `python`:

```bash
source .venv/bin/activate
python examples/create_payment_customer_choice.py
```

## Regeneration

```bash
make gen      # rebuild hexpay/ from oapi/api.yaml — runs in Docker
make install  # editable install into a local venv
make lint     # ruff check
```

`make gen` builds a small image from [`gen.Dockerfile`](gen.Dockerfile)
(based on `python:3.12-slim` with
[`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client)
preinstalled) and runs it against the spec — no host Python required. The
generator version is pinned by `OPENAPI_PYTHON_CLIENT_VERSION` in the
Dockerfile.

CI ([`.github/workflows/generate.yml`](.github/workflows/generate.yml)) runs the
same `make gen` on every push to a non-`main` branch and commits the regenerated
client back to the branch.

## Compatibility

- Python ≥ 3.9
- httpx ≥ 0.23, < 0.29
- Type hints throughout (`py.typed`)
