'''Nuit Status Code Handlers'''
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render

def generic_handler(request, template, status, context={}):
    return render(request, template, context, status=status)

def handler500(request, template='nuit/generic/500.html'):
    return generic_handler(request, template, 500)

def handler403(request, template='nuit/generic/403.html'):
    return generic_handler(request, template, 403)

def handler404(request, template='nuit/generic/404.html'):
    return generic_handler(request, template, 404)
