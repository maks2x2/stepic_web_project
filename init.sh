ln -sf ./etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
rm /etc/nginx/sites-enabled/default
/etc/init.d/nginx restart
