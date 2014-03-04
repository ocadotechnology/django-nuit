'''Demo URLs'''
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from demo.views import MyListView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='demo/introduction.html'), name='introduction'),
    url(r'^kitchen-sink/$', 'demo.views.kitchen_sink', name='kitchen_sink'),
    url(r'^list-view/$', MyListView.as_view(), name='list_view'),
    url(r'^forms/$', 'demo.views.test_form', name='forms'),
)
