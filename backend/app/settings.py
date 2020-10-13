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
from datetime import timedelta
from django.utils.translation import ugettext_lazy as _

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
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'

STATIC_ROOT = env('STATIC_ROOT', default='/code/static')
STATIC_URL = env('STATIC_URL', default='/static/')
MEDIA_ROOT = env('MEDIA_ROOT', default='/code/media')
MEDIA_URL = env('MEDIA_URL', default='/media/')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

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
    ('de', _('German')),
)

#####################
# SECURITY SETTINGS #
#####################
SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

################
# APP SETTINGS #
################
database_url = env(env.DEFAULT_DATABASE_ENV, default=None)
if database_url:
    default_database = env.db_url_config(database_url)
    DATABASES = {
        'default': default_database,
    }

INSTALLED_APPS = [
    "accounts.apps.AccountsConfig",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
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

##################
# REST FRAMEWORK #
##################
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
}

##################
# SECURITY       #
##################
CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST', default=[])
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(
        minutes=env('ACCESS_TOKEN_LIFETIME', default=15)
    ),
    'REFRESH_TOKEN_LIFETIME': timedelta(
        minutes=env('REFRESH_TOKEN_LIFETIME', default=120)
    ),
    'ROTATE_REFRESH_TOKENS': True,
}

##################
# AUTHENTICATION #
##################
AUTH_USER_MODEL = "accounts.User"
