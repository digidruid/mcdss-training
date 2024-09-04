#!/bin/bash

cd ~/mocdss/mcdss-training
source bin/activate

python manage.py runserver 0.0.0.0:8890 >> /opt/support/$(date -I)-django-api.log 2>&1 &

