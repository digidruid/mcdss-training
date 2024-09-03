#!/bin/bash

cd ~/mocdss/demo1
source bin/activate

cd ~/mocdss/demo1/mcdss-training
python manage.py runserver 0.0.0.0:8899 >> /opt/support/django-$(date -I).log 2>&1 &

