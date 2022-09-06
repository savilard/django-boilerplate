from typing import Tuple

DJANGO_APPS: Tuple[str, ...] = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

THIRD_PARTY_APPS: Tuple[str, ...] = (
    'behaviors.apps.BehaviorsConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
)

LOCAL_APPS: Tuple[str, ...] = (
    'apps.core',
    'apps.users',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
