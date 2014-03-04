from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('demo.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'nuit/generic/login.html'}),
)
