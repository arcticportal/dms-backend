#!/bin/bash
#set -o errexit
#set -o pipefail
#set -o nounset
# . ./.env
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
