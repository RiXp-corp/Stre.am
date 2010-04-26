from django.conf import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('stream.streams.views',
	(r'^streams/', include('stream.streams.urls')),
	(r'^$|^home/$', 'index'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views',
	(r'^static/(?P<path>.*)$', 'static.serve', {'document_root': settings.STATIC_MEDIA_ROOT, 'show_indexes': True}), 
)
