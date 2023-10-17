#!/bin/sh
# start gunicorn
cd /python-docker

exec gunicorn -b :5000 --workers=5 --access-logfile - --error-logfile - index:app --reload
