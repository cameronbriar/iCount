from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Counter.views',
    # Examples:
    # url(r'^$', 'iCount.views.home', name='home'),
    # url(r'^iCount/', include('iCount.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^count/$', 'index'),
    url(r'^count/create/$', 'create'),
    url(r'^count/update/$', 'update'),
    url(r'^count/remove/$', 'remove'),
)
