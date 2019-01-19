# Technical tips

### SeLinux and port permissions
show open ports:
```sh
semanage port -l | grep http_port_t
```
add new port to selinux list (for example 8090):
```sh
semanage port -a -t http_port_t  -p tcp 8090
```

### uwsgi and Django tutorial:
Read [uwsgi documets](https://uwsgi.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)

### Django static files
copy all static files to STATIC_ROOT (defined in settings.py)
```sh
python manage.py collectstatic
```