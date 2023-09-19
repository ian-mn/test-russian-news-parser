#!/usr/bin/env bash

python manage.py collectstatic --noinput
python manage.py flush --no-input 
python manage.py migrate
python manage.py createsuperuser --noinput
uwsgi --ini uwsgi.ini