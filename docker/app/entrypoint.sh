#!/usr/bin/env bash

#shellcheck disable=SC2124
cmd="$@"

set -o errexit
set -o pipefail
set -o nounset

# [wait_postgres]-[BEGIN]
if [ -z "${POSTGRES_USER}" ]; then
  base_postgres_image_default_user="postgres"
  export POSTGRES_USER="${base_postgres_image_default_user}"
fi
export DATABASE_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"

postgres_ready() {
  python <<END
import sys

import psycopg2

try:
      psycopg2.connect(
          dbname="${POSTGRES_DB}",
          user="${POSTGRES_USER}",
          password="${POSTGRES_PASSWORD}",
          host="${POSTGRES_HOST}",
          port="${POSTGRES_PORT}",
      )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)

END
}

until postgres_ready; do
  echo >&2 'PostgreSQL is unavailable (sleeping)...'
  sleep 1
done

echo >&2 'PostgreSQL is up - continuing...'
# [wait_postgres]-[END]

# shellcheck disable=SC2086
exec $cmd
