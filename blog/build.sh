#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r blog_final/requirements.txt

python blog_final/manage.py collectstatic --no-input
