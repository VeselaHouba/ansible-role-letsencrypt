#!/usr/bin/env sh
if [ -e /etc/nginx ]; then
  /bin/systemctl restart nginx
fi
