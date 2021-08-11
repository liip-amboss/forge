#!/bin/sh
chown 1000 /uploads
/usr/local/bin/uwsgi --http-auto-chunked --http-keepalive --static-map /media=/uploads
