from restapi.models import Post
from restapi.serializers import PostSerializer
from rest_framework import generics
# Create your views here.


class PostList(generics.ListCreateAPIView):
    """
    List all posts, or create a new post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a post instance
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
