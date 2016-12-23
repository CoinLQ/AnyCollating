# coding=utf-8

from base import *

DEBUG = True


DEV_APPS = [
    'django_extensions',
]

INSTALLED_APPS += DEV_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'conf', 'db.sqlite3'),
    }
}