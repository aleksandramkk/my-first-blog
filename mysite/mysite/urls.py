from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^blogdjango/', include('blogdjango.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
