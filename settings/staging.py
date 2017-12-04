from base import *


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# PayPal Settings
PAYPAL_NOTIFY_URL = 'https://rainbow-felt-designs.herokuapp.com/temp-complicated-url/'
PAYPAL_RECEIVER_EMAIL = 'futoisaru-facilitator@gmail.com'

SITE_URL = 'https://rainbow-felt-designs.herokuapp.com/'
ALLOWED_HOSTS.append('rainbow-felt-designs.herokuapp.com/')


# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}