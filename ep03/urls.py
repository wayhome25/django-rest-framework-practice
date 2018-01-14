from rest_framework.routers import DefaultRouter

from django.urls.conf import include
from django.urls.conf import path

from ep03 import views

app_name = 'ep03'

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'user', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

