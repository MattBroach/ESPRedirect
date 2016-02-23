from redirect.settings import *

ROOT_URLCONF = 'redirect.dev_urls'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Staticfiles settings
STATIC_ROOT = '/vagrant/static/'
MEDIA_ROOT = '/vagrant/media/'

# Debug toolbar settings
DEBUG_TOOLBAR_PATCH_SETTINGS = False

INSTALLED_APPS += ['debug_toolbar',]
INTERNAL_IPS = ('::ffff:10.0.2.2',)

MIDDLEWARE_CLASSES.insert(0,'debug_toolbar.middleware.DebugToolbarMiddleware')

# Net settings
ALLOWED_HOSTS = []
