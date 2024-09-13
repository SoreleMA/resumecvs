#!/bin/bash

cd /app

python manage.py collectstatic --clear --noinput

python manage.py migrate

exec "$@"