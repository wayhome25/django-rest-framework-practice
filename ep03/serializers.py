from rest_framework.serializers import ModelSerializer

from django.contrib.auth import get_user_model

from ep03.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['pk', 'username', 'email']
