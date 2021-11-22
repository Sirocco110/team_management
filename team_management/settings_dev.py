from .settings_common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# ロギング設定
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    #ロガーの設定
    "loggers": {

        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },

        "schedule": {
            "handlers": ["console"],
            "level": "DEBUG",   
        },

        "absent": {
            "handlers": ["console"],
            "level": "DEBUG",   
        },

    },

    #　ハンドラの設定
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "dev"
        },
    },

    "formatters": {
        "dev": {
            "format": "\t".join([
                "%(asctime)s",
                "[%(levelname)s]",
                "%(pathname)s(Line:$|%(lineno)d)",
                "%(message)s"
            ])
        },
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Twilio SendGrid
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'


