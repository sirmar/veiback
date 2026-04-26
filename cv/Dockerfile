FROM ghcr.io/sirmar/dev-python:v0.0.3 AS base
WORKDIR /workspace

FROM base AS deps
ENV PYTHONPATH=/workspace/src
COPY cv/pyproject.toml cv/uv.lock ./
RUN uv sync --extra dev

FROM deps AS lint
ENTRYPOINT ["lint-entrypoint.sh"]

FROM deps AS format
ENTRYPOINT ["format-entrypoint.sh"]

FROM deps AS types
ENTRYPOINT ["types-entrypoint.sh"]

FROM base AS prod
RUN apt-get update && apt-get install -y --no-install-recommends \
  chromium=147.0.7727.55-1~deb13u1 \
  fonts-liberation=1:2.1.5-3 \
  && rm -rf /var/lib/apt/lists/*
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium
ENV PYTHONPATH=/workspace/src
COPY cv/pyproject.toml cv/uv.lock ./
RUN uv sync --no-dev
COPY cv/src/ src/
COPY resume.yaml .
ENTRYPOINT ["python", "src/main.py"]
