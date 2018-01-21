from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter

from ep04 import views

app_name = 'ep04'

router = DefaultRouter()
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
