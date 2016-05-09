sudo rm /etc/nginx/sites-enabled/test.conf
sudo /bin/﻿ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo chmod -R 777 /home/box/web/* 
sudo /etc/init.d/nginx restart
