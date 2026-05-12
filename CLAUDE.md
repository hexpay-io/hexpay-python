# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **fully auto-generated** Python SDK for the HexPay Merchant API. The OpenAPI
spec at `oapi/api.yaml` is the single source of truth. Everything under
`hexpay/` is produced by `openapi-python-client` (version pinned in
`gen.Dockerfile`) and **must not be hand-edited** — changes there will be
overwritten on the next regeneration.

To change SDK behavior you almost always edit `oapi/api.yaml` and regenerate.

## Common commands

```bash
make gen        # regenerate hexpay/ from oapi/api.yaml (runs in Docker, no host Python)
make install    # create .venv/ and pip install -e .  (PEP 668-safe)
make lint       # ruff check on examples/  (hexpay/ is excluded — generated code)
make clean      # nuke hexpay/, .venv/, caches

# Run an example after `make install`:
source .venv/bin/activate
export HEXPAY_TOKEN="<merchant-jwt>"
python examples/create_payment_customer_choice.py
```

The Makefile pattern: `gen` runs entirely in a Docker image built from
`gen.Dockerfile`; `install`/`lint` use a self-managed `.venv/` (no global
pip — works on Homebrew/Debian Pythons without PEP 668 issues). Override
the interpreter with `make PYTHON=/path/to/python3.x install`.

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/). Type
prefix is required; scope is optional.

- `feat:` — new endpoint, field, or example
- `fix:` — bug or spec correction (e.g. `fix: mark checkoutURL optional`)
- `chore:` — regeneration, tooling, deps (CI uses `chore: regenerate sdk`)
- `docs:` — README, CLAUDE.md, comments
- `refactor:`, `test:`, `ci:`, `build:` as standard

Breaking changes: append `!` (e.g. `feat!: rename PaymentResponse.amount`)
or include a `BREAKING CHANGE:` footer — these drive SemVer major bumps
once release automation lands.

## Regeneration flow

`make gen`:
1. Builds image `hexpay-python-sdk-gen:local` from `gen.Dockerfile` (cached
   layer if `OPENAPI_PYTHON_CLIENT_VERSION` is unchanged).
2. Runs the container with the repo bind-mounted at `/workspace`, passes
   `--meta none` so only the package directory is produced (no nested
   pyproject) and `--output-path hexpay` so it lands at the repo root.
3. Touches `hexpay/py.typed` (PEP 561 marker — without it, downstream
   type-checkers ignore our types).

The generated `hexpay/` directory **is committed** to the repo (not
gitignored). Consumers `pip install git+https://...` and expect a ready
package.

## CI behavior

`.github/workflows/generate.yml` runs `make gen` on every push to a
non-`main` branch and auto-commits the regenerated client back to that
branch. The loop is broken by `paths:` filtering (the auto-commit doesn't
touch `oapi/**` or the workflow config, so it doesn't re-trigger).
Open a PR to `main` to merge once the regeneration is green.

If you change something the workflow should react to (e.g. generator
config), update the `paths:` block too.

## Idempotency contract (relevant for examples and any retry logic)

Every POST in this API requires a UUID v4 `X-Idempotency-Key`. The SDK
exposes it as `x_idempotency_key=`. Two rules:

1. **One key per logical operation** — generate it with `str(uuid.uuid4())`.
2. **Reuse the same key across retries** for that operation. A fresh UUID
   inside a retry loop turns a transient failure into a duplicate payment.

`examples/idempotency_retry.py` is the canonical correct implementation
(`uuid.uuid4()` is called once *before* the retry loop). When writing or
reviewing retry code, double-check this.

## openapi-python-client peculiarities to know

- **Python-keyword fields are renamed with a trailing underscore.** The
  spec's `error.type` becomes `err.type_` in Python. Same trap for any
  future field named `class`, `from`, `id` (id is fine actually), etc.
  When examples break with `AttributeError`, this is the first thing to
  check.
- **Optional fields with no value use a sentinel `UNSET`** from
  `hexpay.types`, not `None`. Pass `UNSET` to skip a query parameter
  entirely — see `examples/list_payments.py` for the pattern.
- **Operations expose both `sync` and `asyncio` entry points**, plus
  `sync_detailed`/`asyncio_detailed` returning a `Response[T]` with raw
  status / headers — needed for inspecting error envelopes and
  `Retry-After`.
- **Inline enums** in the spec become classes named after the parent
  schema + field (e.g. `MethodFilterCoin.USDT`, `MethodFilterChain.TON`).
  If you rename a schema in the spec, the generated enum name moves with
  it — update examples accordingly.

## Files you'll most often touch

- `oapi/api.yaml` — the spec; almost every functional change starts here
- `examples/*.py` — keep each script fully self-contained (no shared
  helpers); each reads `HEXPAY_TOKEN` and optionally `HEXPAY_BASE_URL`
  from env
- `gen.Dockerfile` — bump `OPENAPI_PYTHON_CLIENT_VERSION` deliberately;
  the regenerated diff goes through PR review
- `pyproject.toml` — package metadata; the `hexpay/**` glob under
  `tool.ruff.lint.per-file-ignores` intentionally disables linting on
  generated code
