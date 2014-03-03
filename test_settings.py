DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}
INSTALLED_APPS = ['nuit']
STATIC_URL = '/static/'
from django_autoconfig.autoconfig import configure_settings
configure_settings(globals())
