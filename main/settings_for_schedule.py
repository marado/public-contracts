"""
Settings file for the scheduler. Requires a ``settings_local`` with private
information about the database and cache.
"""
from celery.schedules import crontab

from . import settings_local
from . import domain

INSTALLED_APPS = (
    'deputies',
    'law',
    'contracts',
    'main'
)

# for celery
BROKER_URL = settings_local.BROKER_URL

CELERYBEAT_SCHEDULE = {
    'sync-databases': {
        'task': 'main.tasks.update',
        'schedule': crontab(minute=0, hour=4),
    },
}

DATABASES = settings_local.DATABASES

SECRET_KEY = settings_local.SECRET_KEY

CACHES = settings_local.CACHES

ADMINS = settings_local.ADMINS

TIME_ZONE = 'Europe/Lisbon'

if hasattr(settings_local, 'EMAIL_HOST'):
    EMAIL_HOST = settings_local.EMAIL_HOST
    EMAIL_HOST_USER = settings_local.EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD = settings_local.EMAIL_HOST_PASSWORD
    DEFAULT_FROM_EMAIL = settings_local.DEFAULT_FROM_EMAIL
    SERVER_EMAIL = settings_local.SERVER_EMAIL
    EMAIL_SUBJECT_PREFIX = '[%s] ' % domain.SITE_DOMAIN


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
    },
    'handlers': {
        # INFO to console.
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        # errors to admins
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        # This is the "catch all" logger
        '': {
            'handlers': ['console', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

# ignore requests logging
import logging
logging.getLogger("requests").setLevel(logging.WARNING)
