import os
from django.urls import reverse_lazy


def get_debug_mode():

    """ GETTING DEBUG MODE FROM ENVIRONMENT VARIABLE """

    debug_mode = os.environ.get('ON_DEBUG_MODE')

    if debug_mode == "1":
        return True
    return False


DEBUG = get_debug_mode()

""" IMPORTING SETTINGS MODULE DEPENDING ON ENVIRONMENT """

if DEBUG is True:
    try:
        from settings_modules.development import *
        from project.core.rest_framework_settings_development import *
    except ImportError as exc:
        raise ImportError(
            "Couldn't import development settings from settings_module."
        ) from exc
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'statics')
    ]
elif DEBUG is False:
    try:
        from settings_modules.production import *
        from project.core.rest_framework_settings_production import *
    except ImportError as exc:
        raise ImportError(
            "Couldn't import production settings from settings_module."
        ) from exc

""" IMPORTING SETTINGS MODULE DEPENDING ON ENVIRONMENT """

try:
    from project.core.project_apps_settings import *
except ImportError as exc:
    raise ImportError(
        "Couldn't import rest_framework_settings and project_apps_settings from src.project.core settings."
    ) from exc

""" REST FRAMEWORK SETTINGS """

""" REST FRAMEWORK SETTINGS END """


""" PROJECT APPLICATIONS """

if DEBUG:
    INSTALLED_APPS += [app for app in PROJECT_APPS_DEV]

INSTALLED_APPS += [app for app in PROJECT_APPS]

LOGIN_URL = reverse_lazy("core:login")

""" PROJECT APPLICATIONS END """

