#!/bin/bash 

echo "$(date -Iseconds) Updating from git"
cd /home/ubuntu/mocdss/demo1/mcdss-training
git stash
git pull

echo "$(date -Iseconds) Deploying into www directory"
cp -r /home/ubuntu/mocdss/demo1/mcdss-training/html/. /var/www/training/html/.

chgrp -R adm /var/www/training/html


