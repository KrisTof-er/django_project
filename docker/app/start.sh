#!/usr/bin/env bash

make migrate

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py runserver 0.0.0.0:8000