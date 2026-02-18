FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# copy config file fo rcaching
COPY pyproject.toml uv.lock ./

# 2. Abhängigkeiten installieren
# --frozen: use versions from uv.lock
# --no-install-project: do not load the code yet, just the libs
RUN uv sync --frozen --no-install-project

# Copy rest of the code
COPY . .


RUN uv sync --frozen

# Start backend
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]