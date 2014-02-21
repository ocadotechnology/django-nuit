'''Nuit Status Code Handlers'''
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render

def generic_handler(request, template, status, context={}):
    '''
    Return a response with a particular status code, rendering a template with a specified context.
    '''
    return render(request, template, context, status=status)

def handler500(request, template='nuit/generic/500.html'):
    '''
    View handling execeptions, to be used as :data:`django.conf.urls.handler500`
    '''
    return generic_handler(request, template, 500)

def handler400(request, template='nuit/generic/400.html'):
    '''
    View handling bad requests, to be used as :data:`django.conf.urls.handler400`
    '''
    return generic_handler(request, template, 400)

def handler403(request, template='nuit/generic/403.html'):
    '''
    View handling permission denied exceptions, to be used as :data:`django.conf.urls.handler403`
    '''
    return generic_handler(request, template, 403)

def handler404(request, template='nuit/generic/404.html'):
    '''
    View handling invalid URLs, to be used as :data:`django.conf.urls.handler404`
    '''
    return generic_handler(request, template, 404)
