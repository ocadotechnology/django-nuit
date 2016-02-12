DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}
ROOT_URLCONF = 'django_autoconfig.autourlconf'
INSTALLED_APPS = [
    'django.contrib.auth',
    'nuit',
]
STATIC_URL = '/static/'
STATIC_ROOT = '.'
from django_autoconfig.autoconfig import configure_settings
configure_settings(globals())
