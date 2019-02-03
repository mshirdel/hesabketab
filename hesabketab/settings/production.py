from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hesabketab',
        'USER': 'postgres',
        'PASSWORD': 'pg123',
        'HOST': '',
        'PORT': '5432',
    }
}
