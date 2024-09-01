#!/bin/bash

cd ~/mocdss/demo1
source bin/activate

python manage.py runserver 0.0.0.0:8899 >> /opt/support/django-$(date -I).log 2>&1 &

