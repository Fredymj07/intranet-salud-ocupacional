from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbintranetsalud',
        'USER': 'devmontana',
        'PASSWORD': '@CronoS900107',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static'] # carpeta base static

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media' # carpeta base media