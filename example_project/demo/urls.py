'''Demo URLs'''
from django.conf.urls import patterns, url
from demo.views import MyListView

urlpatterns = patterns('',
    url(r'^$', 'demo.views.test_table', name='test_table'),
    url(r'^publishers/$', MyListView.as_view(), name='publishers_list'),
    url(r'^publishers/add/$', 'demo.views.test_form', name='publishers_add'),
)
