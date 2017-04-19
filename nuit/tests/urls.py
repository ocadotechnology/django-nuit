'''Test URLs'''
from django.conf.urls import url
from .. import handlers

urlpatterns = [
    url(r'^error400/$', handlers.handler400),
    url(r'^error403/$', handlers.handler403),
    url(r'^error404/$', handlers.handler404),
    url(r'^error500/$', handlers.handler500),
]
