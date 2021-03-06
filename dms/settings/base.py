"""
Django settings for Data Management System project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# ===================================== APPLICATION DEFINITION =====================================
# ==================================================================================================

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
]

LOCAL_APPS = [
    "home",
    "search",
    "apps.administrative_area",
    "apps.civic_structure",
    "apps.landform",
    "apps.tourist_attraction",
    "apps.users",
    "apps.utils",
]

THIRDPARTY_APPS = [
    "corsheaders",
    "django_celery_beat",
    "django_celery_results",
    "django_extensions",
    "leaflet",
    "modelcluster",
    "strawberry_django",
    "taggit",
]

WAGTAIL_APPS = [
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRDPARTY_APPS + WAGTAIL_APPS

WSGI_APPLICATION = "dms.wsgi.application"
ROOT_URLCONF = "dms.urls"

DJANGO_ADMIN = os.environ.get("DJANGO_ADMIN", "dj-admin/")
WAGTAIL_ADMIN = os.environ.get("WAGTAIL_ADMIN", "cms-admin/")

# ======================================= MIDDLEWARE SETTINGS ======================================
# ==================================================================================================

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

# ======================================= TEMPLATES SETTINGS =======================================
# ==================================================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]


# ============================= Static and media files (CSS, JavaScript, Images) ===================
# ==================================================================================================
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/staticfiles/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# ====================================== Database definition =======================================
# ==================================================================================================
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DATABASE_ENGINE", "django.contrib.gis.db.backends.postgis"),
        "NAME": os.environ.get("DATABASE_NAME", "postgres"),
        "USER": os.environ.get("DATABASE_USERNAME", "postgres"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", "postgres"),
        "HOST": os.environ.get("DATABASE_HOST", "postgres"),
        "PORT": os.environ.get("DATABASE_PORT", "5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation" ".UserAttributeSimilarityValidator",
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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Iceland"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# =================================== DJANGO EMAIL CONFIGURATION ===================================
# ==================================================================================================

# EMAIL_BACKEND = os.environ.get("EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")

# EMAIL_HOST = os.environ.get("EMAIL_HOST", "django.core.mail.backends.console.EmailBackend")
# EMAIL_PORT = int(os.environ.get("EMAIL_PORT", default=587))
# EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
# EMAIL_USE_TLS = int(os.environ.get("EMAIL_USE_TLS", default=0))
# DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "Wagtail")


# ======================================= WAGTAIL SETTINGS =========================================
# ==================================================================================================

WAGTAIL_SITE_NAME = "dms"
WAGTAILADMIN_RECENT_EDITS_LIMIT = 3
WAGTAILIMAGES_MAX_UPLOAD_SIZE = 10 * 1024 * 1024
WAGTAILIMAGES_INDEX_PAGE_SIZE = 30
WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = os.environ.get("WAGTAILADMIN_NOTIFICATION_FROM_EMAIL")
WAGTAILADMIN_NOTIFICATION_USE_HTML = True
WAGTAIL_PASSWORD_RESET_ENABLED = True
TAG_LIMIT = 20

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = os.environ.get("BASE_URL", "http://localhost:8000")
PLATFORM_TIER = os.environ.get("PLATFORM_TIER", "local")

# ======================================== WAGTAIL SEARCH ==========================================
# ==================================================================================================
# https://docs.wagtail.io/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = "http://example.com"

# ======================================== DJANGO LOGGING ==========================================
# ==================================================================================================

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        "prd-console": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "logging.StreamHandler",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "": {
            "handlers": ["prd-console"],
            "level": "ERROR",
        },
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

# ======================================== JUPYTER NOTEBOOK CONF====================================
# ==================================================================================================

SHELL_PLUS = "ipython"

SHELL_PLUS_PRINT_SQL = True

NOTEBOOK_ARGUMENTS = [
    "--ip",
    "0.0.0.0",
    "--port",
    "8888",
    "--allow-root",
    "--no-browser",
]

IPYTHON_ARGUMENTS = [
    "--ext",
    "django_extensions.management.notebook_extension",
    "--debug",
]

IPYTHON_KERNEL_DISPLAY_NAME = "Django Shell-Plus"

SHELL_PLUS_POST_IMPORTS = [  # extra things to import in notebook
    ("module1.submodule", ("func1", "func2", "class1", "etc")),
    ("module2.submodule", ("func1", "func2", "class1", "etc")),
]

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"  # only use in development


# ======================================== MAPS DISPLAY CONFIG +====================================
# ==================================================================================================

LEAFLET_CONFIG = {
    "DEFAULT_CENTER": (-1.94, 29.87),
    "DEFAULT_ZOOM": 8,
    "MAX_ZOOM": 25,
    "SCALE": "both",
    "TILES": [
        ("Street Map", "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {}),
        (
            "ArcGis Satellite",
            "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/" "MapServer/tile/{z}/{y}/{x}.png",
            {},
        ),
        (
            "Monochrome Map",
            "https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}{r}.png",
            {},
        ),
        (
            "CartoDB TopoMap",
            "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png",
            {},
        ),
        ("Topo Map", "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png", {}),
    ],
}


# ======================================= CELERY SETTINGS ==========================================
# ==================================================================================================

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://platform-redis:6379/0")
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "default"
CELERY_TIMEZONE = "Iceland"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60


# ======================================= REDIS and CACHING ========================================
# ==================================================================================================

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get("DB_CACHING", "redis://platform-redis:6379/1"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}

# ======================================= CORS HEADERS =============================================
# ==================================================================================================

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
