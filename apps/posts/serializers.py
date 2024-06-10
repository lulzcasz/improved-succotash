from rest_framework.serializers import ModelSerializer, CharField

from apps.posts.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post  
        fields = ('id', 'title', 'slug', 'body', 'category', 'created_at', 'updated_at')
