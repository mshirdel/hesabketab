# Deploy Django project using uWSGI and nginx

This document is for installing and configuring requirements for deploying a Django web application on ubuntu server.

### Deployment checklist
[Official document](https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/)


### Install git
```shell
sudo apt install git-core
```

### Install and Configure Nginx as a Reverse Proxy
```shell
sudo apt install nginx
```

### Install and Configure VirtualEnv
```shell
sudo apt install python3-pip
sudo pip3 install virtualenv 
virtualenv env
source env/bin/activate
```

### Clone and install requirements of project
```shell
git clone https://github.com/mshirdel/hesabketab.git
cd hesabketab
pip install -r requirments.txt
```

### Install Postgresql and configure
```shell
sudo apt install postgresql postgresql-contrib
# Configure PostgreSQL to start up upon server boot:
update-rc.d postgresql enable 
service postgresql start
# Switch over to the postgres account on your server by typing:
sudo -i -u postgres
# You can now access a Postgres prompt immediately:
psql
# change password for postgres user:
\password
# and enter new password
```

### Create database
```sql
CREATE DATABASE hesabketab WITH OWNER='postgres';
```

### Migrate project models
```shell
python manage.py migrate
```
If you encounter with error:
```
Peer authentication failed for user 'postgres'
```
edit this file:
```
/etc/postgresql/10/main/pg_hba.conf
```
change below line:
```
local   all             postgres         peer
```
to
```
local   all             postgres         md5
```
and the reset postgrsql:
```shell
sudo service postgresql restart
```
### Install uWSGI into your virtualenv
```shell
pip install uwsgi
```

### Running project with uwsgi
```shell
# with port
uwsgi --socket :8001 --module hesabketab.wsgi
# socket
uwsgi --socket hesabketab.sock --module hesabketab.wsgi --chmod-socket=666
```

