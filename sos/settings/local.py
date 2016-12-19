from common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = MEDIA_DIR
#TEMPLATE_DIR = os.path.join(BASE_DIR, '../templates')
STATIC_DIR = os.path.join(BASE_DIR, '../static')
STATIC_ROOT = os.path.join(BASE_DIR, '../collectstatic')

STATICFILES_DIRS = [STATIC_DIR,]


STATIC_URL = '/collectstatic/'
MEDIA_URL = '/media/'

ALLOWED_HOSTS = []

SITE_ID = 2
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sos',
        'USER': 'sosuser',
        'PASSWORD': 'sospassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}