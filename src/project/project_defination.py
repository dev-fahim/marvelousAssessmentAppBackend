import os
from project.core.keys import SECRET_KEY

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = SECRET_KEY

DEFAULT_JWT_ENCRYPTION_ALGORITHM = 'HS256'

USE_PRIVATE_KEY_BASE_JWT = True

if USE_PRIVATE_KEY_BASE_JWT:
    JWT_ENCRYPTION_ALGORITHM = 'RS256'
else:
    JWT_ENCRYPTION_ALGORITHM = DEFAULT_JWT_ENCRYPTION_ALGORITHM

DEBUG = True if os.environ.get('ON_DEBUG_MODE', '1') == "1" else False

ALLOWED_HOSTS = []

ROOT_TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

ROOT_STATIC_DIR = os.path.join(BASE_DIR, 'statics')

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True
