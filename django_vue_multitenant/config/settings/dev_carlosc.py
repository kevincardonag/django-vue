from .base import *
from .installed_apps import *

# SECURITY WARNING: don't run with debug turned on in production!

DOMAIN = "localhost"
PORT = "8000"

ALLOWED_HOSTS = ['*']
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': get_secret('DATABASE_NAME_SERVER_TEST'),
        'USER': get_secret('DATABASE_USER_SERVER_TEST'),
        'PASSWORD': get_secret('DATABASE_PASS_SERVER_TEST'),
        'HOST': get_secret('DATABASE_HOST_SERVER_TEST'),
        'PORT': '',
    }
}
# config emails
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'carlos.almario@correounivalle.edu.co'
EMAIL_HOST_PASSWORD = 'stiph3n0413'
EMAIL_PORT = '587'
EMAIL_USE_TLS  = True
