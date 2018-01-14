from django.urls.conf import path

from ep03 import views

app_name = 'ep03'

urlpatterns = [
    path('posts/', views.PostListAPIView.as_view()),
    path('posts/<int:pk>/', views.PostDetailAPIView.as_view()),
]
