from project.project_defination import *

SECRET_KEY = SECRET_KEY

""" IMPORTING SETTINGS MODULE DEPENDING ON ENVIRONMENT """

if DEBUG is True:
    try:
        from settings_modules.development import *
    except ImportError as exc:
        raise ImportError(
            "Couldn't import development settings from settings_module."
        ) from exc
    ALLOWED_HOSTS = []
elif DEBUG is False:
    try:
        from settings_modules.production import *
    except ImportError as exc:
        raise ImportError(
            "Couldn't import production settings from settings_module."
        ) from exc
    ALLOWED_HOSTS = ['localhost', ]

""" IMPORTING SETTINGS MODULE DEPENDING ON ENVIRONMENT END """

try:
    from project.core.project_apps_settings import *
    from project.core.settings.rest_framework_settings import *
except ImportError as exc:
    raise ImportError(
        "Couldn't import rest_framework_settings and project_apps_settings from project.core.settings settings."
    ) from exc

""" PROJECT APPLICATIONS """

if DEBUG:
    INSTALLED_APPS += [app for app in PROJECT_APPS_DEV]

INSTALLED_APPS += [app for app in PROJECT_APPS]

""" PROJECT APPLICATIONS END """
