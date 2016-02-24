from redirect.settings import *

ROOT_URLCONF = 'redirect.urls'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Staticfiles settings
STATIC_ROOT = '/ESPRedirect/static/'
MEDIA_ROOT = '/ESPRedirect/media/'

# Net settings
ALLOWED_HOSTS = ['*']
