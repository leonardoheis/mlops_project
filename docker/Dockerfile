FROM ghcr.io/astral-sh/uv:python3.9-bookworm-slim AS builder
# Using Python 3.9 and UV as requested

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_PYTHON_DOWNLOADS=0

WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-default-groups

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-default-groups

FROM python:3.9-slim-bookworm

COPY --from=builder --chown=app:app /app /app

ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Expose both ports (API and Streamlit)
EXPOSE 8000 8501

# Execute the unified entrypoint
CMD ["python", "-m", "src.interface"]
