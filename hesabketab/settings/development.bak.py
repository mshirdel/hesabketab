from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
INTERNAL_IPS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hesabketab-dev',
        'USER': 'postgres',
        'PASSWORD': 'pg123',
        'HOST': '',
        'PORT': '5432',
    }
}
