from base import *
import dj_database_url


DEBUG = False

# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# PayPal Settings
PAYPAL_NOTIFY_URL = 'https://rainbow-felt-designs.herokuapp.com/temp-complicated-url/'
PAYPAL_RECEIVER_EMAIL = 'futoisaru-facilitator@gmail.com'

SITE_URL = 'https://rainbow-felt-designs.herokuapp.com/'
ALLOWED_HOSTS.append('rainbow-felt-designs.herokuapp.com')


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
