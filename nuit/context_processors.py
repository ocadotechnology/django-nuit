'''Context Processors for Nuit'''
from django.conf import settings
from django.utils.importlib import import_module
from compressor.utils import get_mod_func

def nuit(request):

    context = {}
    context['NUIT_APPLICATIONS'] = getattr(settings, 'NUIT_APPLICATIONS', None)
    
    return context
