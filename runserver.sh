#!/bin/bash

cd ~/mocdss/mcdss-training
source venv/bin/activate

python manage.py runserver 0.0.0.0:8899 >> /opt/support/$(date -I)-django-web.log 2>&1 &

