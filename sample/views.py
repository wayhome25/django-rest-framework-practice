from django.shortcuts import render
from rest_framework import viewsets

from sample.models import Post
from sample.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
