"""
 _     ___ ___ ____    _____ ___  ____   ____ _____
| |   |_ _|_ _|  _ \  |  ___/ _ \|  _ \ / ___| ____|
| |    | | | || |_) | | |_ | | | | |_) | |  _|  _|
| |___ | | | ||  __/  |  _|| |_| |  _ <| |_| | |___
|_____|___|___|_|     |_|   \___/|_| \_\\____|_____|

Django settings for liip forge project.

"""

import os
import environ

gettext = lambda s: s  # noqa

########################
# ENVIRONMENT SETTINGS #
########################
env = environ.Env()
ENV_PATH = os.path.join('..', '..', '.env')

if os.path.exists(ENV_PATH):
    environ.Env.read_env(ENV_PATH)

#################
# PATH SETTINGS #
#################
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'

STATIC_ROOT = env('STATIC_ROOT', default='/tmp/static/')
STATIC_URL = env('STATIC_URL', default='/static/')

MEDIA_ROOT = env('MEDIA_ROOT', default='/tmp/static/media')
MEDIA_URL = env('MEDIA_URL', default='/media/')

LOCALE_PATHS = env.list('LOCALE_PATHS', default=['locale/'])


#################
# I18N SETTINGS #
#################
TIME_ZONE = 'Europe/Zurich'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGE_CODE = 'de'
LANGUAGES = (
    ('de', gettext('German')),
)

#####################
# SECURITY SETTINGS #
#####################
SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[])
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

################
# APP SETTINGS #
################
DATABASES = {
    'default': env.db(),
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
