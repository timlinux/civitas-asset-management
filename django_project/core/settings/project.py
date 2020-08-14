# coding=utf-8

"""Project level settings.

Adjust these values as needed but don't commit passwords etc. to any public
repository!
"""

import os  # noqa
from django.utils.translation import ugettext_lazy as _
from .base import *  # noqa

# Extra installed apps
INSTALLED_APPS = INSTALLED_APPS + (
    # 3rd party
    'rest_framework',
    'rest_framework_gis',

    # apps
    'core',
    'aim',
    'web-app',
)

# databases
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USERNAME'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': 5432,
        'TEST_NAME': 'unittests',
    }
}
# AIM database
AIM_DATABASE = 'aim'
DATABASES[AIM_DATABASE] = {
    'ENGINE': 'django.contrib.gis.db.backends.postgis',
    'NAME': os.environ['DATABASE_AIM_NAME'],
    'USER': os.environ['DATABASE_USERNAME'],
    'PASSWORD': os.environ['DATABASE_PASSWORD'],
    'HOST': os.environ['DATABASE_HOST'],
    'PORT': 5432,
    'TEST_NAME': 'unittests',
}
DATABASE_ROUTERS = ['aim.router.Router']

# Admins and allowed hosts
ADMINS = (
    ('Irwan Fathurrahman', 'meomancer@gmail.com'),
)
ALLOWED_HOSTS = ['*']

# Set languages which want to be translated
LANGUAGES = (
    ('en', _('English')),
)

# Create APP as the key, after that group it by it's model
ADMIN_GROUP = {
    'aim': {
        'base feature': [
            'AssetClass', 'AssetSubClass', 'FeatureCode'
        ],
        'community': [
            'Province', 'Region', 'Community'
        ],
        'water_supply': [
            'Tank', 'TankBrand', 'TankType'
        ]
    }
}
