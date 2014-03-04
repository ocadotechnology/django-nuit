'''setup.py for nuit'''
from setuptools import setup, find_packages
from nuit.version import __VERSION__

setup(
    name                 = 'django-nuit',
    version              = __VERSION__,
    description          = 'Django Netnix User Interface Tools',
    author               = 'Ben Cardy',
    author_email         = 'ben.cardy@ocado.com',
    maintainer           = 'Netnix Team',
    maintainer_email     = 'netnix@ocado.com',
    packages             = find_packages(),
    install_requires     = [
        'django-foundation-statics',
        'django-compressor',
        'django-jquery',
        'django-foundation-icons',
        'django',
        'django-autoconfig',
        'django-bourbon',
    ],
    include_package_data = True,
    test_suite           = 'setuptest.setuptest.SetupTestSuite',
    tests_require        = ['django-setuptest', 'beautifulsoup',],
)
