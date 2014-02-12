'''Context Processors for Nuit'''
from django.conf import settings
from django.utils.importlib import import_module
from compressor.utils import get_mod_func

def nuit(request):

    context = {}

    context['NUIT_APPLICATIONS'] = getattr(settings, 'NUIT_APPLICATIONS', None)

    nuit_app_menu = getattr(settings, 'NUIT_APP_MENU', None)
    if nuit_app_menu:
        mod_name, func_name = get_mod_func(nuit_app_menu)
        try:
            mod = import_module(mod_name)
        except ImportError:
            context['NUIT_APP_MENU'] = nuit_app_menu
        else:
            try:
                app_menu_func = getattr(mod, func_name)
            except AttribtueError:
                context['NUIT_APP_MENU'] = nuit_app_menu
            else:
                context['NUIT_APP_MENU'] = app_menu_func(request)

    context['NUIT_APP_TITLE'] = getattr(settings, 'NUIT_APP_TITLE', None)
    
    return context
