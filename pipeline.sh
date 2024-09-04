#!/bin/bash 

echo "$(date -Iseconds) Updating from git"
cd /home/ubuntu/mocdss/mcdss-training
git stash
git pull

echo "$(date -Iseconds) Deploying into www directory"
cp -r /home/ubuntu/mocdss/mcdss-training/html/. /var/www/training/html/.

chgrp -R adm /var/www/training/html

chmod 744 *.sh

