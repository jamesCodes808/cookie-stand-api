"""
Django settings for cookie_stand_project project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import environ

env = environ.Env(
    DEBUG=(bool, False),
    ENVIRONMENT=(str, "PRODUCTION"),
    ALLOW_ALL_ORIGINS=(bool, False),
    ALLOWED_HOSTS=(list, []),
    ALLOWED_ORIGINS=(list, []),
    CSRF_TRUSTED_ORIGINS=(list, []),  # lab 39
    # DATABASE_ENGINE=(str, "django.db.backends.sqlite3"),
    # DATABASE_NAME=(str, BASE_DIR / "db.sqlite3"),
    # DATABASE_USER=(str, ""),
    # DATABASE_PASSWORD=(str, ""),
    # DATABASE_HOST=(str, ""),
    # DATABASE_PORT=(int, 5432),
)

environ.Env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ENVIRONMENT = env.str('ENVIRONMENT')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')
    # "django-insecure-zb(h(y1*$2*9g7fo%i9tia+57@dy*d&p4$t71^-ez9-0=)se5c"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG')

ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS'))
    # ['0.0.0.0', 'localhost']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Local
    "cookie_stands",
    # 3rd Party 
    "rest_framework",
    "whitenoise",
    "corsheaders"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware"
]

ROOT_URLCONF = "cookie_stand_project.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "cookie_stand_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": env.str("DATABASE_ENGINE"),
#         "NAME": BASE_DIR/ "db.sqlite3",
#         "USER": env.str("DATABASE_USER"),
#         "PASSWORD": env.str("DATABASE_PASSWORD"),
#         "HOST": env.str("DATABASE_HOST"),
#         "PORT": env.int("DATABASE_PORT"),
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": env.str("DATABASE_ENGINE"),
        "NAME": env.str("DATABASE_NAME"),
        "USER": env.str("DATABASE_USER"),
        "PASSWORD": env.str("DATABASE_PASSWORD"),
        "HOST": env.str("DATABASE_HOST"),
        "PORT": env.int("DATABASE_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ],
}

# Needed to allow requests from cross-origin
CSRF_TRUSTED_ORIGINS = tuple(env.list('CSRF_TRUSTED_ORIGINS'))

CORS_ALLOW_ALL_ORIGINS = env.bool("ALLOW_ALL_ORIGINS")
CORS_ALLOWED_ORIGINS = [ 'http://localhost:3000', ]
CORS_ALLOWED_METHODS = [ 'GET', 'POST', 'DELETE' ]
CORS_ALLOWED_HEADERS = [ 'X-CSRFToken', 'Content-Type', ]
CORS_ORIGIN_WHITELIST = tuple(env.list("ALLOWED_ORIGINS"))
