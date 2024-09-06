#!/bin/bash


git pull


./quick_build.sh

cd ../..

git pull
git add .
git commit -a -m "Updated from build.sh"
git push





