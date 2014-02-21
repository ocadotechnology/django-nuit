'''Context Processors for Nuit'''
from django.conf import settings
from django.utils.importlib import import_module
from compressor.utils import get_mod_func

def nuit(request):

    context = {
        'NUIT_APPLICATIONS': getattr(settings, 'NUIT_APPLICATIONS', None),
        'NUIT_GLOBAL_TITLE': getattr(settings, 'NUIT_GLOBAL_TITLE', None),
    }
    
    return context
