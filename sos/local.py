from common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 3
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sos',
        'USER': 'sosuser',
        'PASSWORD': 'sospassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
