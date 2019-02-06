
"""djangopro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from api import api_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from rest_framework.authtoken import views as token_views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'bands', api_views.BandViewSet)
router.register(r'playlist', api_views.PlaylistViewSet)


urlpatterns = [
	path('',  views.indexx, name='indexx'),
    path('admin/', admin.site.urls),
    path('example/', include('example.urls')),
    
    path('api/', include(router.urls)),
    path('api-token-auth/', token_views.obtain_auth_token)

# curl -d '{"username":"","password":""}' -H "Content-Type: application/x-www-form-urlencoded" -X POST http://localhost:8000/api-token-auth/
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
