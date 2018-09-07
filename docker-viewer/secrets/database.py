import os
BASE_DIR   = os.path.dirname(os.path.dirname(__file__))

COSMO_DB = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'cosmo.sqlite3'),
}
DR2_DB = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'dr2.sqlite3'),
}
