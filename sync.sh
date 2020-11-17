#!/bin/sh

git fetch -- all
git pull
pip install -r requirements.txt
