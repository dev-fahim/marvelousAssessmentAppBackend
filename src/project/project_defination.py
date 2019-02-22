import os
from django.contrib.messages import constants as message_constants
from django.contrib import messages
from django.urls import reverse_lazy
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

LOGIN_URL = reverse_lazy("auth:login_view") if DEBUG else reverse_lazy("core:login")

MESSAGE_LEVEL = message_constants.DEBUG

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True
