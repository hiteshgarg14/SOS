from common import *
import psycopg2
import urlparse


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#To be updated
ALLOWED_HOSTS = ['*' ]

#heroku plugins:install https://github.com/naaman/heroku-vim
#heroku vim

SITE_ID = 4	

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

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
