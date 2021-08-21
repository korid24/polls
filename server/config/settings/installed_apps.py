INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
]

LOCAL_APPS = [
    'apps.core',
    'apps.polls',
    'apps.users',
]

INSTALLED_APPS += LOCAL_APPS
