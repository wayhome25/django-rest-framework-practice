from rest_framework import viewsets

from django.contrib.auth import get_user_model

from ep03.models import Post
from ep03.serializers import PostSerializer
from ep03.serializers import UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
