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
    'sass_processor',

    # apps
    'core',
    'civitas',
    'web-app',

    # helpdesk
    'bootstrap4form',

    'account',  # Required by pinax-teams
    'pinax.invitations',  # required by pinax-teams
    'pinax.teams',  # team support
    'helpdesk',  # This is us!
    'reversion',  # required by pinax-teams
)
SASS_PROCESSOR_ROOT = STATIC_ROOT
STATICFILES_FINDERS += ('sass_processor.finders.CssFinder',)
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
# CIVITAS database
CIVITAS_DATABASE = 'civitas'
DATABASES[CIVITAS_DATABASE] = {
    'ENGINE': 'django.contrib.gis.db.backends.postgis',
    'NAME': os.environ['DATABASE_CIVITAS_NAME'],
    'USER': os.environ['DATABASE_CIVITAS_USERNAME'],
    'PASSWORD': os.environ['DATABASE_CIVITAS_PASSWORD'],
    'HOST': os.environ['DATABASE_CIVITAS_HOST'],
    'PORT': os.environ['DATABASE_CIVITAS_PORT'],
    'OPTIONS': {'sslmode': 'require'},
    'TEST_NAME': 'unittests',
}
DATABASE_ROUTERS = ['civitas.router.Router']

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
    'core': {
        'Authentication and authorization': ['User', 'UserTitle']
    },
    'civitas': {
        'config': [
            'Unit',
            'Condition',
            'Deterioration'
        ],
        'risk': [
            'POF',
            'COF',
            'Risk'
        ],
        'feature identifier': [
            'FeatureClass',
            'FeatureSubClass',
            'FeatureType',
            'FeatureSubType',
            'FeatureTypeCombination'
        ],
        'community': [
            'Province', 'Region', 'Community', 'CapitalProject', 'CivicAddress'
        ],
        'feature': [
            'System',
            'FeatureBase',
            'FeatureGeometry',
            'FeatureCalculation'
        ]
    }
}
AUTH_USER_MODEL = 'core.User'
