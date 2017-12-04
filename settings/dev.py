from base import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# PayPal Settings
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://127.0.0.1/temp-complicated-url/'
PAYPAL_RECEIVER_EMAIL = 'futoisaru-facilitator@gmail.com'