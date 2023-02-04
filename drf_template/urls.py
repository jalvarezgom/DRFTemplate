"""drf_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from schema_graph.views import Schema

from apps.app_1.urls import router as router_app1
from apps.app_2.urls import router as router_app2
from apps.app_3.urls import router as router_app3
from apps.authentication.urls import router as router_auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path(settings.BASE_URL+'django/', include('rest_framework.urls', namespace='rest_framework')),
    path(settings.BASE_URL+'schema/', Schema.as_view()), #Endpoint - DatabaseSchema

    path(settings.BASE_URL+'api-auth/', include(router_auth)),
    path(settings.BASE_URL+'api-app_1/', include(router_app1)),
    path(settings.BASE_URL+'api-app_2/', include(router_app2)),
    path(settings.BASE_URL+'api-app_3/', include(router_app3))
]
