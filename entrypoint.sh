#!/bin/bash

cd /resumecvs

python manage.py collectstatic --clear --noinput

python manage.py migrate

exec "$@"