#!/bin/bash

apt update
apt install git mariadb-server nginx python3 python3-pip python3-venv python3-dev libmariadb-dev -y

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
