SPEC    := oapi/api.yaml
PACKAGE := hexpay
CONFIG  := openapi-python-client.yaml

# Hermetic generation via Docker — no host Python required for `gen`. The
# generator image is built locally from gen.Dockerfile, which pins the
# openapi-python-client version. Bump that pin deliberately.
GEN_IMAGE      := hexpay-python-sdk-gen:local
GEN_DOCKERFILE := gen.Dockerfile
DOCKER         ?= docker

# Local dev helpers (`install`, `lint`) use a self-managed venv so they work
# on Homebrew / Debian Pythons without tripping PEP 668.
PYTHON ?= python3
VENV   := .venv
VBIN   := $(VENV)/bin
VPY    := $(VBIN)/python
VPIP   := $(VPY) -m pip

REPO_ROOT := $(shell pwd)

.PHONY: gen venv install lint clean

gen:
	@command -v $(DOCKER) >/dev/null 2>&1 || { echo "docker is required for 'make gen'"; exit 1; }
	$(DOCKER) build --quiet -t $(GEN_IMAGE) -f $(GEN_DOCKERFILE) .
	@rm -rf $(PACKAGE)
	$(DOCKER) run --rm \
		--user "$$(id -u):$$(id -g)" \
		-v "$(REPO_ROOT)":/workspace \
		-w /workspace \
		$(GEN_IMAGE) generate \
			--path /workspace/$(SPEC) \
			--config $(CONFIG) \
			--meta none \
			--output-path $(PACKAGE) \
			--overwrite
	@touch $(PACKAGE)/py.typed

venv:
	@if [ ! -x $(VBIN)/python ]; then \
		$(PYTHON) -m venv $(VENV) && \
		$(VPIP) install --quiet --upgrade pip; \
	fi

install: venv
	$(VPIP) install -e .

lint: venv
	@[ -x $(VBIN)/ruff ] || $(VPIP) install --quiet ruff
	$(VBIN)/ruff check $(PACKAGE) examples

clean:
	rm -rf $(PACKAGE) build dist *.egg-info .ruff_cache .mypy_cache $(VENV)
