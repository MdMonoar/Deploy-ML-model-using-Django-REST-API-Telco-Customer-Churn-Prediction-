#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install

# install required packages from requirements.txt

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate
