#!/bin/bash

for page in $(ls -1 pages/.)
do
    echo "Building ${page}"
    cat header.html pages/${page} footer.html > ../$page
done

cp ../training.html ../index.html

git pull
git add .
git commit -a -m "Updated from build.sh"
git push





