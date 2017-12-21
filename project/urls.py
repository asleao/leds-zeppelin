from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('zeppelin.urls')),
    url(r'^oauth/', include('rest_framework_social_oauth2.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'accounts/', include('rest_auth.urls')),
    url(r'^accounts/registration/', include('rest_auth.registration.urls')),
]
