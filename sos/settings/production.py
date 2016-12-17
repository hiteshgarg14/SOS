from common import *
import psycopg2
import urlparse

"""
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#TEMPLATE_DIR = os.path.join(BASE_DIR, '../templates')
STATIC_DIR = os.path.join(BASE_DIR, '../static')
STATIC_ROOT = os.path.join(BASE_DIR, '../collectstatic')

STATICFILES_DIRS = [STATIC_DIR,]


STATIC_URL = '/collectstatic/'



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#To be updated
ALLOWED_HOSTS = ['*']

#heroku plugins:install https://github.com/naaman/heroku-vim
#heroku vim

#SITE_ID = 4	

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }
}

#Reason:-Server Error(500)
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
