"""
Django settings for TEDx project.
Generated by 'django-admin startproject' using Django 3.0.2.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import mimetypes

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "z#j+0d9jx0yme*if+&7htan5@u-2o=ln+x^x%0uv=ypg@jb8jz"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "maintenance_mode",
    "products",
    "crispy_forms",
    "base",
    "users",
    "payment",
    "dashboard",
    "ckeditor",
    "colorfield",
    "debug_toolbar",
    "pwa",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "maintenance_mode.middleware.MaintenanceModeMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "htmlmin.middleware.HtmlMinifyMiddleware",
    "htmlmin.middleware.MarkRequestMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "TEDx.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "maintenance_mode.context_processors.maintenance_mode",
            ],
        },
    },
]

WSGI_APPLICATION = "TEDx.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }

}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en"  #'en-us'
LANGUAGES = [("en", "English"), ("ar", "Arabic")]

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


SITE_ROOT = os.path.dirname(os.path.realpath(__name__))
LOCALE_PATHS = (os.path.join(SITE_ROOT, "locale"),)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGIN_REDIRECT_URL = "Home"

LOGIN_URL = "Login"

CRISPY_TEMPLATE_PACK = "bootstrap4"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"

EMAIL_PORT = 465

EMAIL_USE_TLS = False

EMAIL_HOST_USER = "wildlifemain1@gmail.com"

EMAIL_HOST_PASSWORD = "ekvslubsdblgmnlo"

EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "TEDxManaratAlFarouk <noreply@tedxmanaratalfarouk.com>"

# MAINTENANCEEE

MAINTENANCE_MODE = False

# MAINTENANCE_MODE_IGNORE_SUPERUSER = True

MAINTENANCE_MODE_STATE_FILE_PATH = os.path.join(
    BASE_DIR, "maintenance/maintenance_mode_state.txt"
)

MAINTENANCE_MODE_TEMPLATE = os.path.join(BASE_DIR, "base/templates/base/503.html")

INTERNAL_IPS = ["127.0.0.1"]

mimetypes.add_type("application/javascript", ".js", True)


# PWA

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, "static/base/js", "serviceworker.js")

PWA_APP_NAME = "TEDx MFIS"
PWA_APP_DESCRIPTION = "TEDxMFIS Pwa"
PWA_APP_THEME_COLOR = "#0A0302"
PWA_APP_BACKGROUND_COLOR = "#ffffff"
PWA_APP_DISPLAY = "standalone"
PWA_APP_SCOPE = "/"
PWA_APP_ORIENTATION = "any"
PWA_APP_START_URL = "/"
PWA_APP_STATUS_BAR_COLOR = "default"
PWA_APP_ICONS = [{"src": "/static/base/img/icon.png", "sizes": "160x160"}]
PWA_APP_ICONS_APPLE = [{"src": "/static/base/img/icon.png", "sizes": "160x160"}]
PWA_APP_SPLASH_SCREEN = [
    {
        "src": "/static/base/img/icon.png",
        "media": "(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)",
    }
]
PWA_APP_DIR = "ltr"
PWA_APP_LANG = "en-US"

# HTMLMIN
HTML_MINIFY = True

EXCLUDE_FROM_MINIFYING = "^us/"

if not DEBUG:
    # SECURE_SSL_REDIRECT = True

    SECURE_HSTS_SECONDS = 3600

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    SECURE_HSTS_PRELOAD = True

    SECURE_CONTENT_TYPE_NOSNIFF = True

    # SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
