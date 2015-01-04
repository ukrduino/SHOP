from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('store.urls')),
                       url(r'^cart/', include('cart.urls')),)

urlpatterns += patterns('',
                        url(r'^captcha/', include('captcha.urls')),)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )