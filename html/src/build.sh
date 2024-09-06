#!/bin/bash


git pull


./quick-build.sh

cd ../..

git pull
git add .
git commit -a -m "Updated from build.sh"
git push





