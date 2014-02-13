'''Demo URLs'''
from django.conf.urls import patterns, url
from demo.views import MyListView

urlpatterns = patterns('',
    url(r'^publishers/$', MyListView.as_view()),
)
