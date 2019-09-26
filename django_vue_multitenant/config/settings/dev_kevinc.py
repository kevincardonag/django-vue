from .base import *
from .installed_apps import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DOMAIN = "localhost"
PORT = "8080"

ALLOWED_HOSTS = ['*']
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'pizzeria',
        'USER': 'pizzeria',
        'PASSWORD': 'multitenant',
        'HOST': "localhost",
    },
    'db_logs': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'logs.db',
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
