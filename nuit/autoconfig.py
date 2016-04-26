'''Nuit autoconfig'''
import django


SETTINGS = {
    'TEMPLATE_CONTEXT_PROCESSORS': [
        'django.core.context_processors.request',
        'nuit.context_processors.nuit',
    ],
    'INSTALLED_APPS': [
        'django.contrib.staticfiles',
        'foundation_scss',
        'foundation_icons',
        'jquery',
        'bourbon',
        'pipeline',
    ],
    'PIPELINE': {
        'COMPILERS': (
            'pipeline.compilers.sass.SASSCompiler',
        ),
        'CSS_COMPRESSOR': None,
        'SASS_ARGUMENTS': '--quiet',
        'STYLESHEETS': {
            'nuit': {
                'source_filenames': (
                  'nuit.scss',
                ),
                'output_filename': 'nuit.css',
            },
        },
    },
    'STATICFILES_FINDERS': [
        'pipeline.finders.PipelineFinder',
    ],
    'STATICFILES_STORAGE': 'pipeline.storage.PipelineStorage',
    'TEMPLATES': [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                    'nuit.context_processors.nuit',
                ],
            },
        },
    ],
}

if django.VERSION >= (1,9):
    SETTINGS['TEMPLATES'][0]['OPTIONS']['builtins'] = [
        'nuit.templatetags.nuit',
    ]

# We need to add this globally as we're making a new ExtendsNode
# and this needs to be the first node in the template.
try:
    from django.template.base import add_to_builtins
except ImportError:
    pass
else:
    add_to_builtins('nuit.templatetags.nuit')
