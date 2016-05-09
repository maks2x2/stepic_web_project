rm /etc/nginx/sites-enabled/test.conf
﻿#ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
cp /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
rm /etc/nginx/sites-enabled/default
chmod -R 777 /home/box/web/* 
/etc/init.d/nginx restart
