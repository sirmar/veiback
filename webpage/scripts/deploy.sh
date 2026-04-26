#!/bin/sh
set -eu

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

if [ -f "${ROOT_DIR}/.env" ]; then
  . "${ROOT_DIR}/.env"
fi

: "${DEPLOY_USER:?DEPLOY_USER is not set — check .env}"
: "${DEPLOY_HOST:?DEPLOY_HOST is not set — check .env}"
: "${DEPLOY_PATH:?DEPLOY_PATH is not set — check .env}"

IMAGE="veiback-se"

echo "Extracting dist from Docker image..."
CONTAINER=$(docker create "$IMAGE")
TMPDIR=$(mktemp -d)
docker cp "${CONTAINER}:/usr/share/nginx/html/." "${TMPDIR}/dist"
docker rm "${CONTAINER}" > /dev/null

echo "Deploying to ${DEPLOY_USER}@${DEPLOY_HOST}:${DEPLOY_PATH}..."
rsync -avz "${TMPDIR}/dist/" "${DEPLOY_USER}@${DEPLOY_HOST}:${DEPLOY_PATH}"

rm -rf "${TMPDIR}"
echo "Done."
