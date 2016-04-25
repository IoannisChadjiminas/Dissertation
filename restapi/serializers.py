from restapi.models import Post
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """
    Provides a way to serializing and deserializing into json
    """
    class Meta:
        model = Post
        fields = ('author', 'text', 'published_date')
