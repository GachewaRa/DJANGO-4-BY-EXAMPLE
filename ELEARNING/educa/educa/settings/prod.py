import os
from .base import *

#call CUY3BGcCb58yMwf

DEBUG = False

ADMINS = [
    ('Gachewa A', 'gachewaadrian@gmail.com'),
]
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}