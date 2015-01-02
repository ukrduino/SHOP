"""
Django settings for SHOP project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR,  'templates'),
# )
# стандартные настройки BASE_DIR и TEMPLATE_DIRS заменены теми что ниже

# http://stackoverflow.com/a/3038572
# It's better to set up relative paths for your path variables
# This way you can move your Django project and your path roots will update automatically.
# This is useful when you're setting up your production server.


PROJECT_PATH = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))

TEMPLATE_DIRS = (PROJECT_PATH + '/templates/', )

STATICFILES_DIRS = (os.path.join(PROJECT_PATH, 'static'),)  # директория для статики: картинки, css, js

# MEDIA_ROOT = PROJECT_PATH + '/media/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2po#ou!%^8s9c#pb%c=)hrkvz1l*k@!^6l#3d3*#avvbyzpzb6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'cart',
    'bootstrap3',
    'captcha',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SHOP.urls'

WSGI_APPLICATION = 'SHOP.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Kiev'  # я с Украины, драсьте

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


# https://github.com/django-admin-bootstrapped/django-admin-bootstrapped
DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'


#TODO  In your templates, load the bootstrap3 library and use the bootstrap_* tags
#https://github.com/dyve/django-bootstrap3




