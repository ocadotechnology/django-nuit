'''setup.py for nuitng'''
from setuptools import setup, find_packages
from nuitng.version import __VERSION__

setup(
    name                 = 'django-nuitng',
    version              = __VERSION__,
    description          = 'Django Netnix User Interface Tools - Next Generation',
    author               = 'Ben Cardy',
    author_email         = 'ben.cardy@ocado.com',
    maintainer           = 'Netnix Team',
    maintainer_email     = 'netnix@ocado.com',
    packages             = find_packages(),
    include_package_data = True,
)
