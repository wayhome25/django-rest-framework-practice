from rest_framework.routers import DefaultRouter

from django.urls.conf import include
from django.urls.conf import path

from sample import views


app_name='sample'

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
