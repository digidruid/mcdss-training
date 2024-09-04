#!/bin/bash

cd ~/mocdss/mcdss-training
source venv/bin/activate


cd ~/mocdss/mcdss-training/api
python manage.py runserver 0.0.0.0:8890 >> /opt/support/$(date -I)-django-api.log 2>&1 &

