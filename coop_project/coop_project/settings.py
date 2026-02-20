"""
Django settings for coop_project.
Reads sensitive values from environment variables (or .env via python-decouple).
"""
import os
from pathlib import Path

# python-decouple for clean env var management
try:
    from decouple import config, Csv
except ImportError:
    # Fallback if decouple not installed yet
    def config(key, default=None, cast=None):
        val = os.environ.get(key, default)
        return cast(val) if cast and val is not None else val
    def Csv():
        return lambda v: [x.strip() for x in v.split(",")]

BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------------------------------------------
# Security
# ----------------------------------------------------------------
SECRET_KEY = config("SECRET_KEY", default="change-me-in-production-please")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="bcp-dev.pythonanywhere.com,localhost,127.0.0.1",
    cast=Csv(),
)

# ----------------------------------------------------------------
# Application definition
# ----------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "core.middleware.COOPPermissionMiddleware",
]

ROOT_URLCONF = "coop_project.urls"

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
                "core.context_processors.current_division",
            ],
        },
    },
]

WSGI_APPLICATION = "coop_project.wsgi.application"

# ----------------------------------------------------------------
# Database — MySQL on PythonAnywhere free tier
# ----------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DB_NAME", default="bcp_dev$coopdb"),
        "USER": config("DB_USER", default="bcp_dev"),
        "PASSWORD": config("DB_PASSWORD", default=""),
        "HOST": config("DB_HOST", default="bcp-dev.mysql.pythonanywhere-services.com"),
        "PORT": config("DB_PORT", default="3306"),
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# ----------------------------------------------------------------
# Password validation
# ----------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ----------------------------------------------------------------
# Internationalisation
# ----------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Chicago"
USE_I18N = True
USE_TZ = True

# ----------------------------------------------------------------
# Static & media files
# ----------------------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = config("MEDIA_ROOT", default=str(BASE_DIR / "media"))

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ----------------------------------------------------------------
# Auth redirects
# ----------------------------------------------------------------
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/divisions/"
LOGOUT_REDIRECT_URL = "/accounts/login/"

# ----------------------------------------------------------------
# Django REST Framework
# ----------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# ----------------------------------------------------------------
# ServiceNow integration (optional — set in .env)
# ----------------------------------------------------------------
SNOW_INSTANCE_URL = config("SNOW_INSTANCE_URL", default="")
SNOW_USERNAME = config("SNOW_USERNAME", default="")
SNOW_PASSWORD = config("SNOW_PASSWORD", default="")
SNOW_APP_TABLE = config("SNOW_APP_TABLE", default="cmdb_ci_service")

# ----------------------------------------------------------------
# Logging
# ----------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "app": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
