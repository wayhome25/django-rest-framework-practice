from rest_framework.routers import DefaultRouter

from django.urls.conf import include
from django.urls.conf import path

from api import views

app_name = 'api'

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

