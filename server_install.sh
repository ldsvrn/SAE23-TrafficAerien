#!/bin/bash

apt update
apt install git mariadb-server nginx python3 python3-pip python3-venv python3-dev libmariadb-dev ufw -y

mysql -sfu root <<EOS
-- set root password
UPDATE mysql.user SET Password=PASSWORD('toto') WHERE User='root';
-- delete anonymous users
DELETE FROM mysql.user WHERE User='';
-- drop database 'test'
DROP DATABASE IF EXISTS test;
-- also make sure there are lingering permissions to it
DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
-- make changes immediately
FLUSH PRIVILEGES;
-- création utilisateur toto
CREATE USER 'toto'@'localhost';
EOS

useradd -m toto
su - toto -c "git clone https://github.com/ldsvrn/SAE23-TraficAerien /home/toto/django"
chmod 774 /home/toto/django/user_install.sh

mysql -u root -p'toto' < /home/toto/django/SAE_23_BDD.sql

mysql -sfu root <<EOS
-- permission d'acces à la base de donnée
GRANT ALL PRIVILEGES ON sae_23.* TO 'toto'@'localhost';
EOS

su - toto -c '/home/toto/django/user_install.sh'

cat << EOS > /etc/systemd/system/gunicorn.socket
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
EOS

cat << EOF > /etc/systemd/system/gunicorn.service
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=toto
Group=www-data
WorkingDirectory=/home/toto/django
ExecStart=/home/toto/django/.venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock SAE23.wsgi:application

[Install]
WantedBy=multi-user.target
EOF

systemctl start gunicorn.socket
systemctl enable gunicorn.socket

cat << EOF > /etc/nginx/sites-available/sae23
server {
    listen 80;
    server_name sae23.louis.systems;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/toto/django;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
EOF

ln -s /etc/nginx/sites-available/sae23 /etc/nginx/sites-enabled/

systemctl restart nginx

ufw enable
ufw allow 22/tcp
ufw allow 80/tcp