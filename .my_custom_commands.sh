#!/bin/bash

# prints the input
function create() {
	cd
    source .env
    python3 create.py $1 $2
    cd $FILEPATH$1/$2
    git init
    git remote add origin https://github.com/$USERNAME/$2.git
    echo "$2" >> README.md
    git add .
    git commit -m "Initial commit"
    git push origin master
    code .
}
