from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter

from ep06 import views

app_name = 'ep06'

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
