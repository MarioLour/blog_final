#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r blog/requirements.txt

python blog/manage.py collectstatic --no-input