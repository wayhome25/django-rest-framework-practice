from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from ep04.models import Post
from ep04.serializers import PostSerializer


class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

post_list = PostViewSet.as_view({
    'get': 'list',
})
