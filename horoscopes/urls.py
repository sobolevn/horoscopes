from django.conf.urls import patterns, include, url
from HoroscopeView import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.login),
    (r'^static_media/(?P<path>.*)$',
     'django.views.static.serve', {'document_root': '/Users/sobolev/Documents/django/horoscopes/static'}),
    # url(r'^horoscopes/', include('horoscopes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
