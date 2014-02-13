from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('nuit.urls')),
    url(r'^demo/', include('demo.urls')),
)
