#!/bin/bash

python3 -m venv /home/toto/django/.venv
source /home/toto/django/.venv/bin/activate
pip3 install django django-admin mysqlclient gunicorn

python3 /home/toto/django/manage.py makemigration
python3 /home/toto/django/manage.py migrate
python3 /home/toto/django/manage.py collectstatic

#python3 /home/toto/django/manage.py runserver
#/home/toto/django/.venv/bin/gunicorn --bind 0.0.0.0:8000 SAE23.wsgi
