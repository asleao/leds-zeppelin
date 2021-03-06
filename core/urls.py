"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from docs.views import schema_view
from users.api.viewsets import UserViewSet
from languages.api.viewsets import LanguageViewSet
from projects.api.viewsets import ProjectViewSet
from tools.api.viewsets import ToolViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='UserViewSet')
router.register(r'projects', ProjectViewSet, base_name='ProjectViewSet')
router.register(r'tools', ToolViewSet, base_name='ToolViewSet')
router.register(r'languages', LanguageViewSet, base_name='LanguageViewSet')

urlpatterns = [
    path('api/v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
