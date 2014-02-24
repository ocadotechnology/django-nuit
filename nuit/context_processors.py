'''Context Processors for Nuit'''
from django.conf import settings
from django.utils.importlib import import_module
from compressor.utils import get_mod_func

def nuit(request):

    context = {
        'NUIT_APPLICATIONS': getattr(settings, 'NUIT_APPLICATIONS', None),
        'NUIT_GLOBAL_TITLE': getattr(settings, 'NUIT_GLOBAL_TITLE', None),
        'NUIT_LARGE_ICON': getattr(settings, 'NUIT_LARGE_ICON', None),
        'NUIT_SMALL_ICON': getattr(settings, 'NUIT_SMALL_ICON', None),
    }
    
    return context
