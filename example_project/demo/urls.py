'''Demo URLs'''
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from demo.views import MyListView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='demo/introduction.html'), name='introduction'),
    url(r'^kitchen-sink/$', 'demo.views.kitchen_sink', name='kitchen_sink'),
    url(r'^list-view/$', MyListView.as_view(), name='list_view'),
    url(r'^forms/$', 'demo.views.test_form', name='forms'),
    url(r'^400/$', 'demo.views.error', {'code': 400}, name='400'),
    url(r'^403/$', 'demo.views.error', {'code': 403}, name='403'),
    url(r'^404/$', 'demo.views.error', {'code': 404}, name='404'),
    url(r'^500/$', 'demo.views.error', {'code': 500}, name='500'),
)
