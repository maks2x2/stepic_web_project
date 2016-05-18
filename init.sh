rm /etc/nginx/sites-enabled/nginx.conf
﻿#ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/nginx.conf
cp /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/nginx.conf
rm /etc/nginx/sites-enabled/default

chmod -R 777 /home/box/web/* 
/etc/init.d/nginx restart
gunicorn -b 0.0.0.0:8080 wsgi

