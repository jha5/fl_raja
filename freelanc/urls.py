"""freelanc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from ft.api.views import *

#router = DefaultRouter()

#router.register(r'api/enter', LocationSaveViewSet, base_name = "loc-search")
#router.register(r'api/city', AllCityViewSet, base_name = "city-name")

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^rest-auth/', include('rest_auth.urls')),
	url(r'^api/loc/(?P<lat>[0-9.]+)/(?P<lng>[0-9.]+)/(?P<city>[A-Za-z]+)', locationSave),
	url(r'^api/city/(?P<name>[A-Za-z]+)/', allcity )
]
