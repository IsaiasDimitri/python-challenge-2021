#!/bin/bash

python manage.py crontab add
python manage.py makemigrations
python manage.py migrate --no-input
python manage.py loaddata product.json
python manage.py runserver 0.0.0.0:8000