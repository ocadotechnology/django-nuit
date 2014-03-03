# Django settings for example_project project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

INTERNAL_IPS = ('127.0.0.1', '10.252.24.0/24',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'dbfile'),
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: '/home/media/media.lawrence.com/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: 'http://media.lawrence.com/media/', 'http://example.com/media/'
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' 'static/' subdirectories and in STATICFILES_DIRS.
# Example: '/home/media/media.lawrence.com/static/'
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
STATIC_URL = '/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'j$w9t$1(e7k*=c!ks!z&amp;w0s6af!xrku1%&amp;6!c@_5wwicjg&amp;c_c'

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'example_project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'example_project.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nuit',
    'demo',
    'debug_toolbar',
    'django_jenkins',
)

try:
    from local_settings import *
except ImportError:
    pass

from django_autoconfig.autoconfig import configure_settings
configure_settings(globals())

COMPRESS_OFFLINE = False

NUIT_GLOBAL_TITLE = 'Test Project'
NUIT_GLOBAL_LINK = 'http://www.google.com'
NUIT_APPLICATIONS = (
    {
        'name': 'Asset Management',
        'link': 'https://infmis.ocado.com/',
    },
    {
        'name': 'Network Access & Management',
        'subs': (
            {
                'name': 'RADIUS',
                'link': 'https://infmis.ocado.com/',
            },
            {
                'name': 'Wireless Tools',
                'link': 'https://infmis.ocado.com/wireless/guest-passphrase/',
            },
            {
                'name': 'DHCP Management',
                'link': 'https://infmis.ocado.com/',
            },
            {
                'name': 'IPTool',
                'link': 'https://iptool.tech.lastmile.com/iptool/api/v1/?format=json',
            },
        ),
    },
    {
        'name': 'Dashboards & Insight',
        'subs': (
            {
                'name': 'Forest Fire',
                'link': 'https://forestfire.tech.lastmile.com',
            },
            {
                'name': 'Flocked',
                'link': '#',
            },
            {
                'name': 'Shuttle Track',
                'link': '#',
            },
        ),
    },
    {
        'name': 'Self Service',
        'subs': (
            {
                'name': 'User Provisioning',
                'link': 'https://lss.ocado.com/',
            },
            {
                'name': 'VM Provisioning',
                'link': 'https://lss.ocado.com/vmpro/',
            },
            {
                'name': 'Database Users',
                'link': 'https://lss.ocado.com/dumi/',
            },
            {
                'name': 'Apparition',
                'link': 'https://lss.ocado.com/apparition/',
            },
        ),
    },
    {
        'name': 'Warehouse Management',
        'subs': (
            {
                'name': 'NFDC Pickstations',
                'link': 'https://pickman.ocado.com/',
            },
        ),
    },
)
