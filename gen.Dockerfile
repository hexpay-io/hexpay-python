FROM python:3.12-slim

ARG OPENAPI_PYTHON_CLIENT_VERSION=0.28.3

RUN pip install --no-cache-dir \
        "openapi-python-client==${OPENAPI_PYTHON_CLIENT_VERSION}"

# When run with `--user $(id -u):$(id -g)`, the host UID has no entry in the
# container's /etc/passwd, so $HOME is undefined. Point it at a writable
# location so any tool reaching for ~/.cache or ~/.config doesn't crash.
ENV HOME=/tmp

ENTRYPOINT ["openapi-python-client"]
