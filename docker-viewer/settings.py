import os
from viewer.settings_common import *

DEBUG_LOGGING = True

ALLOWED_HOSTS.append('127.0.0.1')
ALLOWED_HOSTS.append('localhost')

STATIC_TILE_URL_B = 'http://{s}.imagine.legacysurvey.org/static/tiles/{id}/{ver}/{z}/{x}/{y}.jpg'
SUBDOMAINS_B = ['a','b','c','d']

#DATABASE_ROUTERS = ['cat.models.Router']

HOSTNAME = 'localhost'

ROOT_URL = ''
SUBDOMAINS = []

STATIC_URL = '/static/'
STATIC_ROOT = None

TILE_URL = 'http://{s}.%s%s/{id}/{ver}/{z}/{x}/{y}.jpg' % ('legacysurvey.org', '/viewer-dev')
CAT_URL = '/{id}/{ver}/{z}/{x}/{y}.cat.json'
STATIC_TILE_URL = 'http://{s}.legacysurvey.org/viewer-dev/static/tiles/{id}/{ver}/{z}/{x}/{y}.jpg'

