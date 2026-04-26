FROM ghcr.io/sirmar/dev-typescript:v0.0.3 AS base

FROM base AS deps
WORKDIR /workspace
COPY webpage/package.json webpage/pnpm-lock.yaml webpage/astro.config.mjs webpage/tsconfig.json webpage/biome.json ./
RUN --mount=type=cache,target=/root/.local/share/pnpm/store \
    pnpm install --frozen-lockfile

FROM deps AS lint
ENTRYPOINT ["/usr/local/bin/lint-entrypoint.sh"]

FROM deps AS format
ENTRYPOINT ["/usr/local/bin/format-entrypoint.sh"]

FROM deps AS types
ENTRYPOINT ["/usr/local/bin/types-entrypoint.sh"]

FROM deps AS security
ENTRYPOINT ["/usr/local/bin/security-entrypoint.sh"]

FROM deps AS watch
COPY webpage/public ./public
COPY resume.yaml .
EXPOSE 4321
ENTRYPOINT ["/usr/local/bin/watch-entrypoint.sh"]

FROM deps AS builder
COPY webpage/. .
COPY resume.yaml .
RUN pnpm build

FROM nginx:alpine AS prod
COPY --from=builder /workspace/dist /usr/share/nginx/html
EXPOSE 80
