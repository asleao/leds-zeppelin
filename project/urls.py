from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('zeppelin.urls')),    
    url(r'^api/v1/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/token/', obtain_jwt_token),
]