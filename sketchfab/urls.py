from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^models/', include(('model3d.urls'), namespace="models")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls', namespace="auth")),
    
]
