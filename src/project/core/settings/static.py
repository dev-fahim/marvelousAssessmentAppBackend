from project.project_defination import DEBUG, BASE_DIR
import os

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

if DEBUG is False:
    STATIC_ROOT = os.path.join(BASE_DIR, 'statics')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'statics')
    ]
