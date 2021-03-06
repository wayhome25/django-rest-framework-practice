"""drf URL Configuration

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
from django.urls.conf import include
from django.urls.conf import path
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', ObtainAuthToken.as_view()),
    path('sample/', include('sample.urls', namespace='sample')),
    path('ep03/', include('ep03.urls', namespace='ep03')),
    path('ep04/', include('ep04.urls', namespace='ep04')),
    path('ep06/', include('ep06.urls', namespace='ep06')),
    path('api/', include('api.urls', namespace='api')),
]
