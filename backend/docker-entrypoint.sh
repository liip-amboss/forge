#!/bin/sh
chown 1000 /uploads
/usr/local/bin/uwsgi --ini uwsgi.ini
