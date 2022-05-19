#!/bin/sh
gunicorn --bind :9000 --workers 2 mainsite.wsgi:application