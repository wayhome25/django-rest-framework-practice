from django.urls.conf import path

from ep04 import views

app_name = 'ep04'

urlpatterns = [
    path('post/', views.post_list),
]
