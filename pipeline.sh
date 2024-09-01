#!/bin/bash 

cd /home/ubuntu/mocdss/demo1/mcdss-training
git pull

cp -r /home/ubuntu/mocdss/demo1/mcdss-training/html/. /var/www/training/html/.

chgrp -R adm /var/www/trainin/html


