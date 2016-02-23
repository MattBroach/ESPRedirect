from redirect.settings import *

ROOT_URLCONF = 'redirect.urls'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Staticfiles settings
STATIC_ROOT = '/esp/static/'
MEDIA_ROOT = '/esp/media/'

# Net settings
ALLOWED_HOSTS = ['*']
